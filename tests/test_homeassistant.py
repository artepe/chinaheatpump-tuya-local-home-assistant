import asyncio
import json
import threading
from dataclasses import replace

import pytest
from homeassistant.config_entries import ConfigEntryState
from homeassistant.exceptions import HomeAssistantError, ServiceValidationError
from homeassistant.helpers import entity_registry as er
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.mango_tuya_local.const import DOMAIN
from custom_components.mango_tuya_local.diagnostics import async_get_config_entry_diagnostics

DATA = {"host": "127.0.0.1", "device_id": "TEST_DEVICE", "local_key": "0000000000000000"}


async def setup(hass, mocked_client):
    entry = MockConfigEntry(domain=DOMAIN, unique_id="TEST_DEVICE", title="Mango test", data=DATA)
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done(wait_background_tasks=True)
    return entry


def entity_id(hass, platform, parameter_id):
    registry = er.async_get(hass)
    return registry.async_get_entity_id(platform, DOMAIN, f"TEST_DEVICE_{parameter_id}")


async def test_real_ha_setup_registers_all_770_parameters_and_46_workingfreq(hass, mocked_client, hardware):
    entry = await setup(hass, mocked_client)
    registry = er.async_get(hass)
    entities = er.async_entries_for_config_entry(registry, entry.entry_id)
    assert len([e for e in entities if e.domain == "number"]) == 769
    assert len([e for e in entities if e.domain == "select"]) == 1
    assert len(entities) == 774
    coordinator = entry.runtime_data
    assert sum(len(s.fields) for s in coordinator.snapshots.values()) == 770
    assert len(coordinator.snapshots[14].fields) == 46
    assert hardware.writes == 0
    assert not entity_id(hass, "number", "0x0890")
    assert entry.state is ConfigEntryState.LOADED


async def test_number_service_writes_only_selected_workingfreq_field(hass, mocked_client, hardware):
    await setup(hass, mocked_client)
    target = entity_id(hass, "number", "0x06BF")
    assert hass.states.get(target).state == "30.0"
    await hass.services.async_call("number", "set_value", {"entity_id": target, "value": 31}, blocking=True)
    assert hass.states.get(target).state == "31.0"
    assert hardware.values["14:16"] == 31 and hardware.writes == 1


async def test_confirmed_decimal_scale_and_reject_fractional_raw_step(hass, mocked_client, hardware):
    await setup(hass, mocked_client)
    target = entity_id(hass, "number", "0x03A1")
    state = hass.states.get(target)
    assert state.state == "0.1" and state.attributes["step"] == 0.1
    await hass.services.async_call("number", "set_value", {"entity_id": target, "value": 0.0}, blocking=True)
    assert hardware.values["1:10"] == 0
    with pytest.raises(ServiceValidationError):
        await hass.services.async_call(
            "number", "set_value", {"entity_id": target, "value": 0.15}, blocking=True
        )
    assert hardware.writes == 1


async def test_alarm_select_known_labels_and_raw_unmapped_codes(hass, mocked_client, hardware):
    await setup(hass, mocked_client)
    target = entity_id(hass, "select", "0x037B")
    state = hass.states.get(target)
    assert state.state == "Once 10sec"
    assert state.attributes["options"] == ["Raw 0", "Sound On", "Once 10sec", "Raw 3"]
    await hass.services.async_call(
        "select", "select_option", {"entity_id": target, "option": "Sound On"}, blocking=True
    )
    assert hardware.values["0:20"] == 1 and hass.states.get(target).state == "Sound On"


async def test_failed_write_restores_state_and_reports_error(hass, mocked_client, hardware):
    entry = await setup(hass, mocked_client)
    target = entity_id(hass, "number", "0x06BF")
    start = hardware.reads
    hardware.plans = {start + 2: "missing", start + 3: "missing"}
    with pytest.raises(HomeAssistantError, match="Original value was restored"):
        await hass.services.async_call(
            "number", "set_value", {"entity_id": target, "value": 31}, blocking=True
        )
    assert hardware.values["14:16"] == 30
    assert hass.states.get(target).state == "30.0"
    assert entry.runtime_data.client.last_operation["restore_verified"]


async def test_diagnostics_redact_credentials_and_do_not_include_status_payload(hass, mocked_client):
    entry = await setup(hass, mocked_client)
    result = await async_get_config_entry_diagnostics(hass, entry)
    encoded = json.dumps(result)
    assert (
        DATA["local_key"] not in encoded and DATA["device_id"] not in encoded and DATA["host"] not in encoded
    )
    assert "PRIVATE_VALUE" not in encoded
    assert result["parameters_read"] == 770


async def test_unload_closes_transport_and_background_scan(hass, mocked_client, hardware):
    entry = await setup(hass, mocked_client)
    assert await hass.config_entries.async_unload(entry.entry_id)
    await hass.async_block_till_done(wait_background_tasks=True)
    assert hardware.closes and mocked_client[-1]._closed
    assert entry.state is ConfigEntryState.NOT_LOADED


async def test_missing_temperature_is_unavailable_not_zero(hass, mocked_client):
    await setup(hass, mocked_client)
    registry = er.async_get(hass)
    target = registry.async_get_entity_id("sensor", DOMAIN, "TEST_DEVICE_current_temperature")
    assert hass.states.get(target).state == "unavailable"


async def test_stale_parameter_group_is_unavailable(hass, mocked_client):
    entry = await setup(hass, mocked_client)
    coordinator = entry.runtime_data
    coordinator.snapshots[14] = replace(coordinator.snapshots[14], received_at=1)
    coordinator.async_set_updated_data(coordinator.current_data())
    assert hass.states.get(entity_id(hass, "number", "0x06BF")).state == "unavailable"


async def test_raw_non_integer_and_out_of_range_service_never_write(hass, mocked_client, hardware):
    await setup(hass, mocked_client)
    target = entity_id(hass, "number", "0x06BF")
    for value in (30.5, 151):
        with pytest.raises(ServiceValidationError):
            await hass.services.async_call(
                "number", "set_value", {"entity_id": target, "value": value}, blocking=True
            )
    assert hardware.writes == 0


async def test_cancelled_ha_write_keeps_lock_until_rollback_and_marks_group_unknown(
    hass, mocked_client, hardware
):
    entry = await setup(hass, mocked_client)
    coordinator = entry.runtime_data
    started, release = threading.Event(), threading.Event()
    hardware.hold_read = started, release
    hardware.hold_only_after_write = True
    task = asyncio.create_task(coordinator.async_set_raw(coordinator.profile.parameter(14, 16), 31))
    assert await hass.async_add_executor_job(started.wait, 3)
    task.cancel()
    await asyncio.sleep(0)
    assert coordinator._io_lock.locked()
    release.set()
    with pytest.raises(asyncio.CancelledError):
        await task
    assert hardware.values["14:16"] == 30
    assert coordinator.client.last_operation["restore_verified"]
    assert 14 in coordinator.failed_groups
    assert hass.states.get(entity_id(hass, "number", "0x06BF")).state == "unavailable"
