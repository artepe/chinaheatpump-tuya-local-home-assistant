# Mango Tuya Local for Home Assistant

[![Tests](https://github.com/artepe/mango-tuya-local-home-assistant/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/artepe/mango-tuya-local-home-assistant/actions/workflows/tests.yml)

**Mango Control Room: 770 parameters, 17 categories, English explanations.**

![Dashboard demo](docs/images/dashboard-desktop.png)

*UI preview with synthetic demo values. The live dashboard uses your HA entities.*

[Dashboard guide](docs/DASHBOARD.md) | [English parameter reference](docs/PARAMETERS.md) | [Releases](https://github.com/artepe/mango-tuya-local-home-assistant/releases)

Local parameter control for the captured Mango Energy Tuya heat-pump profile.
This initial version exposes **770 parameter routes in 17 sections**, including
all **46 WorkingFreq fields**. It uses Tuya protocol 3.5 and does not need a
cloud API account during normal operation.

**Version 0.2.0 beta.** The protocol has physical-device evidence for selected
routes; the Home Assistant component is tested with a simulated transport.
The HA component itself still needs its first installation test on the owner
device. Individual write permissions and most display scales are not yet
known for every parameter.

[Suomenkielinen ohje](README_FI.md)

## Included

- Automatic **Mango Control** sidebar dashboard with all 17 categories.
- A short English explanation below every field, with inferred functions labelled.
- Global search, four WorkingFreq table filters, and desktop/mobile layouts.

- 769 number entities and one Alarm Sound Set select: 770 real parameters.
- 46 WorkingFreq controls, not a single hard-coded test parameter.
- One shared local connection and serialized reads/writes.
- Fresh complete group metadata before every write; exact parameter ID/order
  and current device bounds are checked.
- A separate fresh read confirms the requested value. No optimistic state.
- Failed or cancelled writes attempt bounded original-value recovery.
- Observed DP105 current/target temperature sensors, parameter scan count,
  and a button to refresh all parameter groups.
- UI configuration, polling options, connection reconfiguration, and
  credential-redacted diagnostics.

There are 774 entities in total: 770 controls, three sensors and one button.
The 34 repeated `bak` rows in SYS Para 2 are not entities or write targets.
First setup reads parameters in the background. Fields remain unavailable
until their matching complete group has been received. Initial setup and
polling do not send parameter writes.

## Values and compatibility

Cool Ctrl Cpst uses its confirmed display scale: raw 1 is displayed as 0.1.
Other numbers use raw integers and are named with `(raw)` when their scale
is unconfirmed. No decimal scale or write permission is inferred from flags.
Alarm Sound Set maps raw 1 to Sound On and raw 2 to Once 10sec. The other
two codes are shown as Raw 0 and Raw 3; their labels are not claimed verified.

Fixed device bounds, such as 3..3, allow no other target. The integration
does not bypass limits. Presence of an entity does not prove the device will
accept a change. A denied or unconfirmed write raises an error and attempts
to restore the fresh original value.

The profile contains the captured label/ID order and raw bounds for product
`tfmjnk5uytzacmma`. Other Tuya heat pumps are not assumed compatible. Every
description page must match the expected group, page count, declared count,
record IDs, header and padding. No Modbus register stride is assumed.

This release focuses on parameters. It does not claim a complete climate
entity, operating mode command, compressor telemetry or calculated COP.
Temperatures only use observed DP105 fields. Missing/stale data is not zero
and the previously stale DP16 value is not used as a fallback.

## Install

Tested against Home Assistant Core **2026.10.1** and Python **3.14.8**.
The manifest installs `tinytuya==1.17.4` in the Home Assistant environment.

With HACS, add this repository as a custom **Integration** repository,
download Mango Tuya Local, and restart Home Assistant. Otherwise copy
`custom_components/mango_tuya_local` to the Home Assistant
`custom_components` folder and restart.

After updating, **Mango Control** is added to the sidebar automatically.
Restart Home Assistant and refresh the browser. No additional frontend cards
or manual entity-ID mapping are needed.

Then go to **Settings > Devices & services > Add integration > Mango Tuya
Local**. Choose manual credentials (pump IP, device ID, local key), or use
the Pi session exporter below. The IP is the pump's local IP.

### Existing research session on the Pi

From the downloaded repository root in the same Terminal & SSH environment
as the successful research probes:

```bash
python3 tools/install_local.py
/tmp/mango-tuya/bin/python tools/import_pi_session.py --host PUMP_IP
ha core restart
```

Replace `PUMP_IP` with the pump IP. The exporter selects exactly one device
named Mango Energy from the existing session. It writes a temporary local
HA credential file with mode 0600, prints no keys, and makes no parameter
writes. Choose **Use credentials exported from the Pi session** in the UI.
Successful setup removes the temporary file. Credentials are not in this
repository or its tests. The installer preserves an existing component
outside `custom_components` before replacing it.

## Refresh and writes

Default polling is 30 seconds: status plus one parameter group. A complete
initial scan is performed once in the background. Use **Refresh all
parameters** after changing many values from another client. Options allow
15-300 second polling; normal parameter writes immediately refresh their
own group.

Avoid editing the same parameter from another app during a write. Local
operations are serialized, but an external app cannot participate in that
lock. Recovery requires a running process and a working local connection;
power loss cannot execute a rollback. An unconfirmed restore explicitly
reports the parameter and original raw value.

## Device evidence

| Parameter | Group / slot | Evidence |
|---|---|---|
| Cool Ctrl Cpst | 1 / 10 | Local raw write/read packets: 1 -> 0 -> 1 |
| HtUpEnv28In20(50) | 14 / 16 | Local raw packets: 30 -> 31 -> 30; new general client also confirmed in the owner terminal |
| Alarm Sound Set | 0 / 20 | App codes 1/2; new general client write and restore confirmed in the owner terminal |
| Max Warm Tim | 1 / 24 | App write/state evidence for raw 998/999 |

Owner terminal confirmations are recorded separately from raw-packet
validation. Simulator successes do not promote other fields to physically
verified write permissions. The four fixture write frames are value-only
research requests and contain no device credentials or account data.

## Development

```bash
python3.14 -m venv .venv
.venv/bin/pip install -r requirements-test.txt
.venv/bin/pytest
.venv/bin/ruff check custom_components tests tools
```

Tests cover all 770 real routes, exact observed write bytes, wrong headers
and IDs, fresh limits, decimal conversion, rejected/delayed writes, rollback,
cancelled operations, real HA entity registration and service actions,
configuration, options, reconfiguration, unloading and diagnostics.
Tests use a simulated local transport; they do not connect to a heat pump.

## Sources

- Owner-supplied raw packet study and local test results, 12-13 October 2026.
- [Home Assistant integration patterns](https://developers.home-assistant.io/docs/integration_fetching_data/).
- [Home Assistant config flows](https://developers.home-assistant.io/docs/core/integration/config_flow/).
- [TinyTuya](https://github.com/jasonacox/tinytuya).

MIT license. This is a community integration, not a manufacturer release.
