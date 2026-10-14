"""Real HA availability and transport regressions for intermittent replies."""

import base64
import json
import struct
import time

import pytest
from homeassistant.helpers import entity_registry as er

from custom_components.mango_tuya_local.client import MangoClient
from custom_components.mango_tuya_local.const import DOMAIN
from custom_components.mango_tuya_local.diagnostics import async_get_config_entry_diagnostics
from custom_components.mango_tuya_local.protocol import MangoReadError

from .fake_device import Hardware
from .test_homeassistant import entity_id, setup


def temperature_reply():
    raw = bytearray(244)
    raw[:6] = bytes.fromhex("010100010001")
    struct.pack_into(">h", raw, 14, 60)
    struct.pack_into(">h", raw, 92, 627)
    return {"dps": {"105": base64.b64encode(raw).decode()}}


def transport():
    from custom_components.mango_tuya_local.protocol import Profile

    hw = Hardware(Profile.load())
    client = MangoClient(
        "127.0.0.1",
        "TEST_DEVICE",
        "0000000000000000",
        hw.profile,
        device_factory=hw.factory,
        clock=lambda: 0,
        pause=lambda n: None,
    )
    return client, hw


def test_ack_then_delayed_status_is_accepted_without_reconnection():
    client, hw = transport()
    hw.status_responses = [None]
    hw.status_followups = [temperature_reply()]
    client.status()
    assert hw.factories == 1 and client.status_reconnects == 0
    assert client.temperatures["current_temperature"] == 62.7
    assert hw.socket_timeouts == [3, 1]
    assert hw.writes == 0


def test_non_dps_ack_is_followed_by_data():
    client, hw = transport()
    hw.status_responses = [{"ack": True}]
    hw.status_followups = [{"ack": True}, {"dps": {}}]
    client.status()
    assert hw.factories == 1 and client.last_status_received_at > 0
    assert not client.temperatures


def test_transient_status_error_reconnects_once_and_recovers():
    client, hw = transport()
    hw.status_responses = [{"Error": "PRIVATE_PAYLOAD", "Err": "901"}, {"dps": {}}]
    client.status()
    assert hw.factories == 2 and hw.closes == 1
    assert client.status_reconnects == 1 and client.last_transport_error is None
    assert hw.writes == 0


def test_ack_without_data_fails_bounded_and_never_claims_freshness():
    client, hw = transport()
    hw.status_responses = [None, None]
    with pytest.raises(MangoReadError, match="status_data_timeout"):
        client.status()
    assert hw.factories == 2 and client.last_status_received_at == 0
    assert not client.temperatures


def test_transport_diagnostic_keeps_only_safe_error_code():
    client, hw = transport()
    hw.status_responses = [{"Error": "PRIVATE_PAYLOAD", "Err": "PRIVATE_KEY"}] * 2
    with pytest.raises(MangoReadError, match="status_error_unknown"):
        client.status()
    assert client.last_transport_error == "status_error_unknown"


async def test_one_failed_poll_keeps_confirmed_data_and_recovery_clears_retrying(
    hass, mocked_client, hardware
):
    hardware.status_responses = [temperature_reply()]
    entry = await setup(hass, mocked_client)
    c = entry.runtime_data
    target = entity_id(hass, "number", "0x06BF")
    temp = er.async_get(hass).async_get_entity_id("sensor", DOMAIN, "TEST_DEVICE_current_temperature")
    received_at = c.client.temperature_received_at
    hardware.status_error = True
    await c.async_refresh()
    assert c.last_update_success and c.connection_state == "retrying"
    assert hass.states.get(target).state == "30.0"
    assert hass.states.get(temp).state == "62.7"
    assert hass.states.get(temp).attributes["communication_state"] == "retrying"
    assert c.client.temperature_received_at == received_at
    hardware.status_error = False
    await c.async_refresh()
    assert c.connection_state == "connected" and c.consecutive_status_failures == 0
    assert hardware.writes == 0


async def test_sustained_outage_expires_grace_and_all_fields_become_unavailable(
    hass, mocked_client, hardware
):
    entry = await setup(hass, mocked_client)
    c = entry.runtime_data
    c._last_contact_monotonic = time.monotonic() - c.connection_grace_seconds - 1
    hardware.status_error = True
    await c.async_refresh()
    assert not c.last_update_success and c.connection_state == "offline"
    assert hass.states.get(entity_id(hass, "number", "0x06BF")).state == "unavailable"
    hardware.status_error = False
    await c.async_refresh()
    assert c.last_update_success and hass.states.get(entity_id(hass, "number", "0x06BF")).state == "30.0"


async def test_grace_never_keeps_a_stale_temperature_available(hass, mocked_client, hardware):
    entry = await setup(hass, mocked_client)
    c = entry.runtime_data
    c.client.temperatures = {"current_temperature": 62.7}
    c.client.temperature_received_at = time.time() - c.interval * 3 - 11
    hardware.status_error = True
    await c.async_refresh()
    temp = er.async_get(hass).async_get_entity_id("sensor", DOMAIN, "TEST_DEVICE_current_temperature")
    assert c.last_update_success and hass.states.get(temp).state == "unavailable"


async def test_missing_group_is_retried_next_poll_without_starving_other_groups(
    hass, mocked_client, hardware
):
    entry = await setup(hass, mocked_client)
    c = entry.runtime_data
    c._next_group = 14
    hardware.plans = {hardware.reads + 1: "missing", hardware.reads + 2: "missing"}
    await c.async_refresh()
    assert c._retry_group == 14 and c._next_group == 15
    assert hass.states.get(entity_id(hass, "number", "0x06BF")).state == "unavailable"
    await c.async_refresh()
    assert c._retry_group is None and c._next_group == 15
    assert hass.states.get(entity_id(hass, "number", "0x06BF")).state == "30.0"
    hardware.plans = {hardware.reads + n: "missing" for n in (1, 2, 3, 4)}
    await c.async_refresh()
    await c.async_refresh()
    assert c._next_group == 16 and c._retry_group is None
    await c.async_refresh()
    assert c._next_group == 0


async def test_initial_failure_has_no_grace_without_confirmed_data(hass, mocked_client, hardware):
    hardware.status_error = True
    from pytest_homeassistant_custom_component.common import MockConfigEntry

    from .test_homeassistant import DATA

    entry = MockConfigEntry(domain=DOMAIN, unique_id="TEST_DEVICE", data=DATA)
    entry.add_to_hass(hass)
    assert not await hass.config_entries.async_setup(entry.entry_id)
    assert not entry.runtime_data.snapshots


async def test_recovery_diagnostics_are_redacted(hass, mocked_client, hardware):
    entry = await setup(hass, mocked_client)
    hardware.status_error = True
    await entry.runtime_data.async_refresh()
    data = await async_get_config_entry_diagnostics(hass, entry)
    assert data["last_transport_error"] == "status_error_901"
    assert data["communication_state"] == "retrying"
    assert "PRIVATE_STATUS_PAYLOAD" not in json.dumps(data)
    assert "0000000000000000" not in json.dumps(data)


async def test_connection_grace_is_capped_for_long_polling(hass, mocked_client):
    entry = await setup(hass, mocked_client)
    entry.runtime_data.interval = 300
    assert entry.runtime_data.connection_grace_seconds == 120


async def test_cached_updates_cannot_resurrect_an_offline_device(hass, mocked_client):
    entry = await setup(hass, mocked_client)
    c = entry.runtime_data
    c.connection_state = "offline"
    c.async_set_updated_data(c.current_data())
    assert hass.states.get(entity_id(hass, "number", "0x06BF")).state == "unavailable"
    count = er.async_get(hass).async_get_entity_id("sensor", DOMAIN, "TEST_DEVICE_parameters_read")
    assert hass.states.get(count).state == "unavailable"
