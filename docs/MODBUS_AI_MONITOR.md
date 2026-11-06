# Mango Modbus Monitor (experimental)

**Branch:** `feature/modbus-ai-monitor`

Read-only Home Assistant integration that consumes **existing Home Assistant
entities** (such as entities published by the Modbus integration). It does
not open TCP connections, assume register addresses, read raw registers,
write setpoints, or make any AI API calls on its own.

It is an optional second integration in this repository. The existing
`mango_tuya_local` component and all of its parameter writes remain
unchanged.

## Install in Home Assistant OS Terminal & SSH

```sh
cd /config
git clone --depth 1 --branch feature/modbus-ai-monitor \
  https://github.com/artepe/chinaheatpump-tuya-local-home-assistant.git \
  /tmp/mango-monitor-install
mkdir -p /config/custom_components
cp -R /tmp/mango-monitor-install/custom_components/mango_modbus_monitor \
  /config/custom_components/
ha core restart
```

If `/tmp/mango-monitor-install` already exists, remove that **temporary
clone only** before cloning again. Do not remove or replace the existing
Mango Tuya integration folder.

Then open **Settings → Devices & services → Add integration → Mango Modbus
Monitor** and select the Home Assistant entities you already have. Configure
at least one sensor; mapping more sensors produces more diagnostics. Use
the integration's **Reconfigure** action later to change selections.

The UI offers these input mappings:

| Mapping | Unit / meaning |
|---|---|
| Compressor RPS | rps (mechanical revolutions per second, not raw register value) |
| Outdoor temperature | °C |
| Supply water | °C |
| Return water | °C |
| Water flow | l/h, l/min, or m³/h |
| Electrical power | W or kW |
| Thermal power | W or kW |
| Reported COP | dimensionless |
| Superheat | °C / K (display only; location must be verified) |
| EEV position | steps or percentage (display only; no unverified comparison) |
| Heating setpoint | Existing Mango Tuya number entity if available |
| Defrost | binary_sensor (on/off) |

The monitor runs every 30 seconds using `hass.states.get`. It **does not
increase Modbus polling frequency**. Entity mapping is in the config entry.
When units are missing or not W/kW or l/h/l/min/m³/h, power and flow-based
checks are skipped rather than guessing the scale.

## Exposed sensors

- `sensor.mango_modbus_monitor_status`: `ok`, `warning`, `incomplete`,
  or `no_data` (the generated entity ID may vary).
- `sensor.mango_modbus_monitor_calculated_cop`: heat output / electrical
  input, when both powers have usable units.
- `sensor.mango_modbus_monitor_water_side_heat`: estimate based on water
  flow and supply/return ΔT, **assuming water**.
- `sensor.mango_modbus_monitor_heat_balance_deviation`: percentage
  difference between the water-side calculation and measured thermal power.

The status sensor has attributes `issues`, `metrics`, `readings`,
`units`, `unavailable_inputs`, and `mapped_entities`, so the monitor
can be used in Lovelace, templates, Grafana, and Home Assistant AI Task.

## AI analysis (optional)

Home Assistant's `ai_task.generate_data` can send these diagnostics to a
configured AI provider, including local AI solutions when supported. Add a
preferred AI Task entity/provider, then use
[`examples/mango_ai_report_automation.yaml`](../examples/mango_ai_report_automation.yaml)
in `automations.yaml`. It analyzes warnings at most once every 30 minutes
and displays a persistent notification. Check the status entity ID in
Developer Tools first.

The example sends **only** the selected entity states, values and diagnostic
descriptions to the configured AI provider. A cloud provider transfers those
values outside the local network; choose a local provider if that is not
acceptable. **The AI only creates text; it does not write commands.**

## Limitations / safety

- This is a **prototype**, not verified on the physical user's Modbus setup.
- This checks selected *measurements*, not all 770 Tuya settings. Tuya values
  are available as input only if the matching Mango entity is selected.
  Automatic 770-parameter configuration auditing is a separate workstream.
- Physical plausibility thresholds are advisory, not manufacturer limits.
  For example water-side heat uses `1.163 Wh/(l K)`, which is unsuitable
  for unknown antifreeze/glycol concentration.
- COP comparisons can disagree when power meters cover different loads,
  e.g. inverter-only consumption versus whole heat-pump consumption.
- Negative superheat may indicate incorrect sensors or measurement location;
  no compressor protection should be changed on this basis.
- No stale-data watchdog yet: `unknown`/`unavailable` states are excluded,
  but a sensor that silently freezes at a valid number could be missed.
- Defrost state must be mapped if you want COP/temperature checks suspended
  during defrost. Do not use it as an interlock.
- Never use this module in place of factory protections, pressure switches,
  electrical protection or refrigerant safety systems.

## Developer checks

```sh
python3 -m compileall -q custom_components/mango_modbus_monitor
python3 -m pytest tests/test_mango_modbus_rules.py
```

See `rules.py` for every actual condition; no unverified Modbus register
mapping is baked into the repository.
