"""Evaluate existing HA sensor states without opening any Modbus connection."""

from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN, FIELD_LABELS
from .rules import evaluate

_LOGGER = logging.getLogger(__name__)


class MangoModbusCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, entry):
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            config_entry=entry,
            update_interval=timedelta(seconds=30),
        )
        self.entry = entry

    async def _async_update_data(self):
        readings = {}
        units = {}
        missing = []
        entity_ids = {}
        for key in FIELD_LABELS:
            entity_id = self.entry.data.get(key)
            if not entity_id:
                continue
            entity_ids[key] = entity_id
            state = self.hass.states.get(entity_id)
            if state is None or state.state in ("unavailable", "unknown", ""):
                missing.append(key)
                continue
            if key == "defrost":
                if state.state in ("on", "off"):
                    readings[key] = state.state == "on"
                else:
                    missing.append(key)
                continue
            try:
                number = float(state.state)
            except (TypeError, ValueError):
                missing.append(key)
                continue
            readings[key] = number
            units[key] = state.attributes.get("unit_of_measurement", "")
        report = evaluate(readings, units)
        report["entity_ids"] = entity_ids
        report["unavailable"] = missing
        if not readings:
            report["status"] = "no_data"
        elif missing and report["status"] == "ok":
            report["status"] = "incomplete"
        return report
