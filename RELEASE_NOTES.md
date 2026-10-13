# v0.2.0 - Mango Control Room (beta)

This beta adds a complete parameter dashboard to the local Mango heat-pump
integration. **Mango Control** appears automatically in the Home Assistant
sidebar after updating the integration, restarting HA and refreshing the browser.

## Dashboard

- 770 parameter controls in 17 categories.
- All 46 WorkingFreq entries with separate heating/cooling table filters.
- Short English explanations beneath every parameter and sensor metric.
- Global search, live entity-registry mapping and multi-pump selection.
- Responsive desktop and mobile layouts; no extra HACS card dependencies.
- Individual Apply actions, device readback/recovery results and full refresh.
- A reusable custom card and dedicated Lovelace dashboard YAML.

## Validation

- 62 automated tests against Home Assistant Core 2026.10.1 with simulated transport.
- 10 frontend behaviour tests.
- Real Chromium checks of desktop/mobile rendering, search, category filters,
  explicit service calls, refused writes and refresh.
- Interface screenshots use synthetic values and are labelled DEMO.

## Compatibility and limits

The device profile is the captured Mango Energy product `tfmjnk5uytzacmma`,
using local Tuya 3.5. Requires Home Assistant 2026.10 or newer.
Descriptions inferred from abbreviated device labels are marked as inferred;
unverified functions are marked separately. Unconfirmed scales remain raw.
The release does not prove all 770 individual hardware write permissions or
claim a complete climate entity. The first full physical HA dashboard test is
still an owner validation step.

Existing integration credentials and entity unique IDs are retained on update.
Current source code is in this release's source archives; a full project ZIP
and the dashboard YAML are also attached.
