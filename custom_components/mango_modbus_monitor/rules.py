"""Conservative, read-only plausibility checks on numeric sensor readings.

These are diagnostic heuristics, NOT manufacturer safety limits or controls.
Missing units disable calculations rather than guessing W/kW or l/h/m3/h.
"""

from __future__ import annotations

import math


def _number(readings, key):
    value = readings.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value) if math.isfinite(value) else None


def _power_kw(readings, units, key):
    value = _number(readings, key)
    if value is None:
        return None
    unit = str(units.get(key, "")).strip().lower()
    if unit == "w":
        return value / 1000
    if unit == "kw":
        return value
    return None


def _flow_lh(readings, units):
    value = _number(readings, "flow_rate")
    unit = str(units.get("flow_rate", "")).strip().lower().replace("³", "3")
    if value is None:
        return None
    if unit in ("l/h", "lph", "l/hour"):
        return value
    if unit in ("l/min", "lpm"):
        return value * 60
    if unit in ("m3/h", "m3/hour"):
        return value * 1000
    return None


def evaluate(readings, units):
    """Return a transparent report with traceable heuristics.

    Calculated heat uses WATER cp ~= 1.163 Wh/(l K). Glycol mixes differ.
    Do not suggest compressor/EEV/defrost writes from these values alone.
    """
    issues = []
    metrics = {}

    rps = _number(readings, "compressor_rps")
    supply = _number(readings, "supply_temperature")
    return_temp = _number(readings, "return_temperature")
    electrical_kw = _power_kw(readings, units, "electric_power")
    measured_heat_kw = _power_kw(readings, units, "thermal_power")
    flow_lh = _flow_lh(readings, units)
    defrost = readings.get("defrost") is True

    if rps is not None and (rps < 0 or rps > 120):
        issues.append("Compressor speed outside general plausibility range (0–120 RPS); verify sensor scaling.")

    if electrical_kw is not None and electrical_kw < 0:
        issues.append("Electrical power is negative; verify sign convention and register scale.")
    if measured_heat_kw is not None and measured_heat_kw < 0 and not defrost:
        issues.append("Thermal power is negative outside reported defrost; verify sign convention.")

    if supply is not None and return_temp is not None:
        delta_t = round(supply - return_temp, 2)
        metrics["water_delta_t_c"] = delta_t
        if rps is not None and rps > 15 and delta_t < -1 and not defrost:
            issues.append("Supply colder than return while compressor runs; check flow/sensor placement or defrost.")

        if flow_lh is not None and flow_lh > 0:
            calc_heat_kw = round(flow_lh * 1.163 * delta_t / 1000, 2)
            metrics["water_side_heat_kw"] = calc_heat_kw
            if (measured_heat_kw is not None and measured_heat_kw > 0.5
                    and calc_heat_kw > 0.5 and not defrost):
                deviation = abs(calc_heat_kw - measured_heat_kw) / measured_heat_kw * 100
                metrics["heat_balance_deviation_pct"] = round(deviation, 1)
                if deviation > 40:
                    issues.append("Water-side heat differs from measured heat by >40%; verify flow, units and glycol.")

    if (electrical_kw is not None and measured_heat_kw is not None
            and electrical_kw > 0.3 and measured_heat_kw >= 0):
        calculated_cop = measured_heat_kw / electrical_kw
        metrics["calculated_cop"] = round(calculated_cop, 2)
        if not defrost and rps is not None and rps > 15:
            if calculated_cop < 0.8 or calculated_cop > 8:
                issues.append("Calculated COP is outside a broad 0.8–8 plausibility band; check measurement scope.")
        reported_cop = _number(readings, "reported_cop")
        if (reported_cop is not None and reported_cop > 0 and calculated_cop > 0
                and not defrost):
            deviation = abs(reported_cop - calculated_cop) / calculated_cop * 100
            metrics["cop_deviation_pct"] = round(deviation, 1)
            if deviation > 30:
                issues.append("Reported COP differs from heat/electricity ratio by >30%; compare meter boundaries.")

    metrics["defrost_reported"] = defrost
    return {
        "status": "warning" if issues else "ok",
        "issues": issues,
        "metrics": metrics,
        "readings": {key: value for key, value in readings.items()
                     if not isinstance(value, float) or math.isfinite(value)},
        "units": dict(units),
    }
