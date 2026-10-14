# v0.2.1 - Local connection recovery (beta)

Fixes software behaviour that made all Mango entities briefly unavailable after
one failed status request. The precise cause of the owner's network/protocol
failures remains unconfirmed; this release improves recovery and diagnostics.

- Wait for actual DPS data after an ACK instead of rejecting it immediately.
- Use a three-second status socket timeout, restoring the one-second group receive timeout afterwards.
- Retry status once on a fresh local connection.
- Keep confirmed values during a bounded recovery window (100 seconds at the default poll interval; capped at 120 seconds), visibly labelled as last confirmed data.
- Preserve temperature freshness limits, missing-data handling and sustained-outage unavailability. No optimistic or indefinite online state.
- Retry a failed parameter group on the next poll once, then continue round-robin reads.
- Add redacted transport/recovery diagnostics and original data timestamps.
- Update GitHub links to the renamed chinaheatpump-tuya-local-home-assistant repository.

## Validation

75 tests against Home Assistant Core 2026.10.1 with simulated transport, including
13 recovery regressions, plus 11 frontend behaviour tests. Physical verification
of this patch in the owner's installation is still pending. Existing credentials,
entity identities, 770 routes and write/readback/rollback validation are retained.
