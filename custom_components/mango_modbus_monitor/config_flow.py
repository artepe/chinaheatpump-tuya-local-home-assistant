"""Select already-existing HA sensors. No Modbus address guessing or polling."""

from __future__ import annotations

import probatio as schema
from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from homeassistant.helpers.selector import EntitySelector, EntitySelectorConfig

from .const import DOMAIN, FIELD_LABELS, NAME


def _data_schema(values=None):
    values = values or {}
    fields = {
        schema.Required(CONF_NAME, default=values.get(CONF_NAME, NAME)): str,
    }
    for key in FIELD_LABELS:
        selector = EntitySelector(
            EntitySelectorConfig(domain="binary_sensor" if key == "defrost" else (
                ["number", "sensor"] if key == "heat_setpoint" else "sensor"
            ))
        )
        marker = (schema.Optional(key, default=values[key]) if values.get(key)
                  else schema.Optional(key))
        fields[marker] = selector
    return schema.Schema(fields)


def _has_sensor(data):
    return any(data.get(key) for key in FIELD_LABELS)


class MangoModbusMonitorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            if not _has_sensor(user_input):
                errors["base"] = "missing_sensor"
            else:
                await self.async_set_unique_id(DOMAIN)
                self._abort_if_unique_id_configured()
                return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)
        return self.async_show_form(
            step_id="user", data_schema=_data_schema(user_input), errors=errors
        )

    async def async_step_reconfigure(self, user_input=None):
        entry = self._get_reconfigure_entry()
        errors = {}
        if user_input is not None:
            if not _has_sensor(user_input):
                errors["base"] = "missing_sensor"
            else:
                return self.async_update_reload_and_abort(entry, data_updates=user_input)
        return self.async_show_form(
            step_id="reconfigure",
            data_schema=_data_schema(user_input or entry.data),
            errors=errors,
        )
