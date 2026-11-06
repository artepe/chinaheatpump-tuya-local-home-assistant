"""Monitoring status and derived read-only sensors for Home Assistant."""

from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, NAME


async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities(
        MangoMonitorSensor(entry.runtime_data, entry, key)
        for key in ("status", "calculated_cop", "water_side_heat_kw", "heat_balance_deviation_pct")
    )


class MangoMonitorSensor(CoordinatorEntity, SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, coordinator, entry, key):
        super().__init__(coordinator)
        self.key = key
        self._attr_unique_id = f"{entry.entry_id}_{key}"
        self._attr_name = {
            "status": "Status",
            "calculated_cop": "Calculated COP",
            "water_side_heat_kw": "Water side heat",
            "heat_balance_deviation_pct": "Heat balance deviation",
        }[key]
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name=NAME,
            manufacturer="Community",
            model="Existing HA entity monitor",
        )
        if key != "status":
            self._attr_state_class = SensorStateClass.MEASUREMENT
            if key == "water_side_heat_kw":
                self._attr_native_unit_of_measurement = "kW"
            if key == "heat_balance_deviation_pct":
                self._attr_native_unit_of_measurement = "%"

    @property
    def available(self):
        return self.coordinator.last_update_success

    @property
    def native_value(self):
        data = self.coordinator.data or {}
        if self.key == "status":
            return data.get("status", "no_data")
        return data.get("metrics", {}).get(self.key)

    @property
    def extra_state_attributes(self):
        if self.key != "status":
            return None
        data = self.coordinator.data or {}
        return {
            "issues": data.get("issues", []),
            "metrics": data.get("metrics", {}),
            "readings": data.get("readings", {}),
            "units": data.get("units", {}),
            "unavailable_inputs": data.get("unavailable", []),
            "mapped_entities": data.get("entity_ids", {}),
        }
