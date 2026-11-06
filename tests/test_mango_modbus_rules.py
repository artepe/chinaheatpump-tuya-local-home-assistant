"""Pure diagnostic checks; no hardware or Modbus required."""

import importlib.util
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "custom_components" / "mango_modbus_monitor" / "rules.py"
spec = importlib.util.spec_from_file_location("mango_monitor_rules", MODULE)
rules = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rules)


def test_water_energy_and_cop():
    reading = {
        "compressor_rps": 34,
        "supply_temperature": 55,
        "return_temperature": 52,
        "flow_rate": 2066,
        "electric_power": 1600,
        "thermal_power": 7200,
    }
    units = {"flow_rate": "l/h", "electric_power": "W", "thermal_power": "W"}
    report = rules.evaluate(reading, units)
    assert report["status"] == "ok"
    assert 7.1 <= report["metrics"]["water_side_heat_kw"] <= 7.3
    assert report["metrics"]["calculated_cop"] == 4.5


def test_missing_units_are_not_guessed():
    report = rules.evaluate({"thermal_power": 8000, "electric_power": 1500}, {})
    assert "calculated_cop" not in report["metrics"]


def test_cop_outlier_warning():
    report = rules.evaluate(
        {"compressor_rps": 35, "thermal_power": 10000, "electric_power": 1000},
        {"thermal_power": "W", "electric_power": "W"},
    )
    assert report["status"] == "warning"
    assert any("COP" in issue for issue in report["issues"])


def test_defrost_excludes_cop_outlier():
    report = rules.evaluate(
        {"defrost": True, "compressor_rps": 35, "thermal_power": 10000, "electric_power": 1000},
        {"thermal_power": "W", "electric_power": "W"},
    )
    assert report["status"] == "ok"


def test_m3_per_hour_conversion():
    report = rules.evaluate(
        {"flow_rate": 2, "supply_temperature": 50, "return_temperature": 47},
        {"flow_rate": "m³/h"},
    )
    assert report["metrics"]["water_side_heat_kw"] == 6.98
