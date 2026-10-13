import json
from pathlib import Path
from unittest.mock import Mock

from homeassistant.auth.permissions.const import POLICY_READ
from homeassistant.components import frontend
from homeassistant.helpers import entity_registry as er

from custom_components.mango_tuya_local.const import DOMAIN
from custom_components.mango_tuya_local.dashboard import CARD_URL, PANEL_PATH, dashboard_data, load_catalog
from tools.build_description_catalog import build

from .test_homeassistant import DATA, entity_id, setup


def test_every_parameter_has_a_deterministic_english_description():
    root = Path(__file__).parents[1] / "custom_components" / DOMAIN
    catalog = load_catalog()
    assert catalog == build(json.loads((root / "profile.json").read_text()))
    assert len(catalog["parameters"]) == 770 and len(catalog["groups"]) == 17
    assert all(
        len(p["description"]) >= 30 and p["description"].isascii() for p in catalog["parameters"].values()
    )
    assert catalog["parameters"]["0:20"]["confidence"] == "verified_options"
    assert all(p["confidence"] != "verified_options" for k, p in catalog["parameters"].items() if k != "0:20")
    assert "units are unverified" in catalog["parameters"]["14:16"]["description"]


async def test_automatic_panel_and_card_registration(hass, mocked_client, hardware):
    await setup(hass, mocked_client)
    assert frontend.async_panel_exists(hass, PANEL_PATH)
    assert CARD_URL in hass.data[frontend.DATA_EXTRA_MODULE_URL].urls
    assert hardware.writes == 0


async def test_dashboard_uses_actual_registry_ids_and_describes_all_controls(hass, mocked_client):
    await setup(hass, mocked_client)
    permissions = Mock()
    permissions.check_entity.return_value = True
    data = dashboard_data(hass, permissions)
    pump = data["devices"][0]
    rows = [p for g in pump["groups"] for p in g["parameters"]]
    assert len(rows) == 770 and len(pump["groups"][14]["parameters"]) == 46
    assert all(p["entity_id"] in hass.states.async_entity_ids() and p["description"] for p in rows)
    assert sum(p["domain"] == "select" for p in rows) == 1
    assert all(pump["sensors"].values()) and pump["refresh_entity"]
    encoded = json.dumps(data)
    assert (
        DATA["device_id"] not in encoded and DATA["local_key"] not in encoded and DATA["host"] not in encoded
    )


async def test_renamed_entity_is_resolved_without_guessing_a_slug(hass, mocked_client):
    await setup(hass, mocked_client)
    old = entity_id(hass, "number", "0x06BF")
    er.async_get(hass).async_update_entity(old, new_entity_id="number.renamed_working_frequency")
    permissions = Mock()
    permissions.check_entity.return_value = True
    data = dashboard_data(hass, permissions)
    row = next(p for g in data["devices"][0]["groups"] for p in g["parameters"] if p["key"] == "14:16")
    assert row["entity_id"] == "number.renamed_working_frequency"


async def test_dashboard_honours_existing_entity_read_permissions(hass, mocked_client):
    await setup(hass, mocked_client)
    blocked = entity_id(hass, "number", "0x06BF")
    permissions = Mock()
    permissions.check_entity.side_effect = lambda eid, policy: eid != blocked
    data = dashboard_data(hass, permissions)
    assert blocked not in json.dumps(data)
    assert sum(len(g["parameters"]) for g in data["devices"][0]["groups"]) == 769
    permissions.check_entity.return_value = False
    permissions.check_entity.side_effect = None
    assert dashboard_data(hass, permissions)["devices"] == []


async def test_entity_more_info_contains_english_help(hass, mocked_client):
    await setup(hass, mocked_client)
    target = entity_id(hass, "number", "0x03A1")
    attrs = hass.states.get(target).attributes
    assert "Raw 1 is confirmed" in attrs["description"]
    assert attrs["description_confidence"] == "label_inferred"


async def test_unloaded_device_is_removed_from_dashboard(hass, mocked_client):
    entry = await setup(hass, mocked_client)
    assert await hass.config_entries.async_unload(entry.entry_id)
    permissions = Mock()
    permissions.check_entity.return_value = True
    assert dashboard_data(hass, permissions)["devices"] == []


async def test_read_only_account_keeps_help_but_cannot_control(hass, mocked_client):
    await setup(hass, mocked_client)
    permissions = Mock()
    permissions.check_entity.side_effect = lambda eid, policy: policy == POLICY_READ
    data = dashboard_data(hass, permissions)
    rows = [p for g in data["devices"][0]["groups"] for p in g["parameters"]]
    assert len(rows) == 770
    assert all(not p["can_control"] for p in rows)


async def test_authenticated_websocket_returns_the_dashboard(hass, mocked_client, hass_ws_client):
    await setup(hass, mocked_client)
    client = await hass_ws_client(hass)
    await client.send_json({"id": 9, "type": "mango_tuya_local/dashboard"})
    response = await client.receive_json()
    assert response["success"]
    assert sum(len(g["parameters"]) for g in response["result"]["devices"][0]["groups"]) == 770
