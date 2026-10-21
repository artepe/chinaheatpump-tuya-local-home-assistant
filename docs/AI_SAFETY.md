# Local Mango integration: automation contract

The captured 770-parameter profile is **not** a validated physical service
manual. A successful read or write/readback proves only communication and
storage of a raw value, not the engineering meaning of the parameter.

The entity attribute `scale_verified` reports whether a captured scaling was
independently established; `local_write_evidence` describes protocol evidence.
`ai_write_mapping_verified` is intentionally **false** for unverified mappings,
even if raw writing works. `ai_requires_owner_approval` is true for those keys.

## For external optimizers

- Require an explicit, narrowly scoped owner-approved list of parameter keys.
  Do not infer that `Heat Sv5`, `Heat Min OD5` or other labels represent
  verified quantities in kelvins, percents or steps.
- Observe the `data_received_at` timestamp, `parameter_id`, raw bounds,
  `communication_state` and freshness. 17 groups are polled sequentially;
  a status update does not imply the cached parameter group was reread.
- Use read-confirmed single-parameter writes, compare the exact raw readback,
  and pause on unexpected responses. The local integration already attempts
  to restore the old value on write failure; verify recovery before proceeding.
- A temperature sensor, compressor power signal or safety alarm from another
  integration must be validated on its own merits.
- Keep all manufacturer protections active. The Home Assistant entity layer is
  not a replacement for independent compressor safety limits.

The corresponding AI_heatpump_controller has a fail-closed whitelist
`mango_cop_ai.vahvistetut_parametrit` and additional measurement/fault guards.

## Next commissioning tasks

Verify Heat Sv1–9, Heat Min OD1–9 and the active operating-zone mapping with
the manufacturer or a controlled test, using a known-good physical reference,
one step at a time, and logging `data_received_at` for each observation.
Do not promote raw parameter scale evidence automatically based on a successful
transaction.
