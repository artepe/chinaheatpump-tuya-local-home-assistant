import json

from custom_components.mango_tuya_local.config_flow import CREDENTIAL_FILE
from custom_components.mango_tuya_local.const import DOMAIN

from .test_homeassistant import DATA, setup


async def test_manual_config_validates_only_reads_and_creates_entry(hass, mocked_client, hardware):
    result = await hass.config_entries.flow.async_init(DOMAIN, context={"source": "user"})
    assert result["type"] == "menu"
    result = await hass.config_entries.flow.async_configure(result["flow_id"], {"next_step_id": "manual"})
    assert result["step_id"] == "manual"
    result = await hass.config_entries.flow.async_configure(result["flow_id"], DATA)
    assert result["type"] == "create_entry" and result["data"] == DATA
    assert hardware.writes == 0
    await hass.async_block_till_done(wait_background_tasks=True)


async def test_invalid_key_is_not_created_or_written(hass, mocked_client, hardware):
    result = await hass.config_entries.flow.async_init(DOMAIN, context={"source": "user"})
    result = await hass.config_entries.flow.async_configure(result["flow_id"], {"next_step_id": "manual"})
    result = await hass.config_entries.flow.async_configure(result["flow_id"], {**DATA, "local_key": "bad"})
    assert result["type"] == "form" and result["errors"]["base"] == "invalid_credentials"
    assert hardware.writes == 0


async def test_unreachable_device_does_not_create_entry(hass, mocked_client, hardware):
    hardware.status_error = True
    result = await hass.config_entries.flow.async_init(DOMAIN, context={"source": "user"})
    result = await hass.config_entries.flow.async_configure(result["flow_id"], {"next_step_id": "manual"})
    result = await hass.config_entries.flow.async_configure(result["flow_id"], DATA)
    assert result["type"] == "form" and result["errors"]["base"] == "cannot_connect"
    assert hardware.writes == 0


async def test_pi_export_missing_is_a_clear_form_error(hass, mocked_client):
    result = await hass.config_entries.flow.async_init(DOMAIN, context={"source": "user"})
    result = await hass.config_entries.flow.async_configure(result["flow_id"], {"next_step_id": "pi"})
    result = await hass.config_entries.flow.async_configure(result["flow_id"], {})
    assert result["errors"]["base"] == "pi_credentials_missing"


async def test_pi_export_is_read_locally_then_removed_after_success(hass, mocked_client, tmp_path):
    hass.config.config_dir = str(tmp_path)
    export = tmp_path / CREDENTIAL_FILE
    export.write_text(json.dumps({"format": "mango_tuya_local_credentials_v1", **DATA}))
    result = await hass.config_entries.flow.async_init(DOMAIN, context={"source": "user"})
    result = await hass.config_entries.flow.async_configure(result["flow_id"], {"next_step_id": "pi"})
    result = await hass.config_entries.flow.async_configure(result["flow_id"], {})
    assert result["type"] == "create_entry" and result["data"] == DATA
    assert not export.exists()
    await hass.async_block_till_done(wait_background_tasks=True)


async def test_options_change_reloads_with_one_new_client(hass, mocked_client):
    entry = await setup(hass, mocked_client)
    result = await hass.config_entries.options.async_init(entry.entry_id)
    assert result["step_id"] == "init"
    result = await hass.config_entries.options.async_configure(result["flow_id"], {"poll_interval": 60})
    assert result["type"] == "create_entry"
    await hass.async_block_till_done(wait_background_tasks=True)
    assert entry.runtime_data.interval == 60
    assert mocked_client[0]._closed


async def test_reconfigure_changes_host_preserving_device_identity(hass, mocked_client):
    entry = await setup(hass, mocked_client)
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": "reconfigure", "entry_id": entry.entry_id}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"host": "127.0.0.2", "local_key": ""}
    )
    assert result["type"] == "abort" and result["reason"] == "reconfigure_successful"
    await hass.async_block_till_done(wait_background_tasks=True)
    assert entry.data["host"] == "127.0.0.2" and entry.data["local_key"] == DATA["local_key"]
    assert entry.unique_id == "TEST_DEVICE"
