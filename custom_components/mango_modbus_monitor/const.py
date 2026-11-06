"""Configured HA entity keys. The integration does not query Modbus directly."""

DOMAIN = "mango_modbus_monitor"
NAME = "Mango Modbus Monitor"

FIELD_LABELS = {
    "compressor_rps": "Compressor speed (RPS)",
    "outdoor_temperature": "Outdoor temperature",
    "supply_temperature": "Water supply temperature",
    "return_temperature": "Water return temperature",
    "flow_rate": "Water flow",
    "electric_power": "Electrical input power",
    "thermal_power": "Measured thermal output",
    "reported_cop": "Existing COP sensor",
    "superheat": "Suction superheat",
    "eev_position": "EEV position",
    "heat_setpoint": "Heating setpoint (Mango Tuya entity)",
    "defrost": "Defrost active (binary sensor)",
}
