#!/usr/bin/env python3
"""Create clearly labelled synthetic UI data; never read owner credentials."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMPONENT = ROOT / "custom_components" / "mango_tuya_local"


def build():
    profile = json.loads((COMPONENT / "profile.json").read_text())
    catalog = json.loads((COMPONENT / "descriptions.json").read_text())
    groups = [{**g, "parameters": []} for g in catalog["groups"]]
    states = {}
    for r in profile["routes"]:
        key = f"{r['group']}:{r['slot']}"
        platform = "select" if key == "0:20" else "number"
        eid = f"{platform}.demo_field_{r['group']}_{r['slot']}"
        p = {
            "key": key,
            "name": r["name"],
            "domain": platform,
            "entity_id": eid,
            "scale_verified": r.get("scale_verified", False),
            **catalog["parameters"][key],
        }
        groups[r["group"]]["parameters"].append(p)
        scale = r.get("scale", 1)
        raw = max(r["raw_lower"], min(r["raw_upper"], 30 if r["group"] == 14 else 10))
        if key == "1:10":
            raw = 1
        attrs = {"min": r["raw_lower"] / scale, "max": r["raw_upper"] / scale, "step": 1 / scale}
        if platform == "select":
            state = "Once 10sec"
            attrs = {"options": ["Raw 0", "Sound On", "Once 10sec", "Raw 3"]}
        else:
            state = str(raw / scale)
        states[eid] = {"entity_id": eid, "state": state, "attributes": attrs}
    sensors = {}
    for key, value in [
        ("current_temperature", "63.5"),
        ("target_temperature", "60.0"),
        ("parameters_read", "770"),
    ]:
        eid = "sensor.demo_" + key
        sensors[key] = eid
        states[eid] = {
            "entity_id": eid,
            "state": value,
            "attributes": {} if key == "parameters_read" else {"unit_of_measurement": "\u00b0C"},
        }
    refresh = "button.demo_refresh"
    states[refresh] = {"entity_id": refresh, "state": "unknown", "attributes": {}}
    return {
        "catalog": {
            "version": "0.2.0",
            "devices": [
                {
                    "entry_id": "demo-pump",
                    "name": "DEMO / simulated values",
                    "groups": groups,
                    "sensors": sensors,
                    "refresh_entity": refresh,
                }
            ],
        },
        "states": states,
    }


if __name__ == "__main__":
    (ROOT / "tests" / "frontend").mkdir(exist_ok=True)
    (ROOT / "tests" / "frontend" / "demo-data.json").write_text(json.dumps(build(), ensure_ascii=True) + "\n")
    print("Synthetic dashboard fixture generated: 770 controls.")
