# Reasoning capture — Patch 2105: wire raw-capture + registry-read rules into the OS (Step 5)

**STATUS: verbatim (captured at-patch).** Window: 2100-band. Opus worker; integrator = TLA.

Step 5: wired the Capture-and-Audit Protocol's standing rules into `templates/operating_system.md` and
`bootup.md` so all future windows adopt it — but as **DRAFT, pending CONV-001 ratification (Step 6)**, never as a
live canonical rule yet.

Edits:
- `operating_system.md` §2 (Workflow table): added the `capture_and_audit_protocol.md` row (DRAFT).
- `operating_system.md` §6 (What gets captured): added the flat by-window raw-transcript row, and a new
  "Raw capture + overnight audit (DRAFT)" subsection carrying the three standing rules — the raw-capture rule
  (daytime = record only, no filing/registry/founder-capture), the reframed registry read protocol, and the
  heartbeat rule.
- `bootup.md` Step 2 (Check what happened last): added the bootup heartbeat check (DRAFT).
- `bootup.md` §5 (Workflow documents): added the protocol-doc row (DRAFT).

Decisions:
- **The "registry READ protocol" the handover §5.5 specified (glob `Registries_temp/*.md`) is VOID and was NOT
  wired.** 2B collapsed in the 2102 reframe (protocol §8) — there are no registry-temps, so there is nothing to
  glob. What I wired instead is the honest reframed rule: during the day the canonical registries reflect
  last-overnight-audit state; same-day cross-window changes are not visible until the next audit. Wiring the
  original glob would have pointed every window at a directory that does not exist. If same-day visibility is
  later wanted, it returns as a read-only render, not a shared write target. Flagged for TLA ratification.
- **DRAFT-not-live, with a safeguard.** The protocol is not canonical until Step 6 (panel) + TLA ratification,
  and it changes how every window works. So every inserted block is marked DRAFT and carries the safeguard:
  *until ratified, keep current capture practice* (curated transcripts, best-effort per-patch §10). This makes
  the half-state safe — a window applying 2105 before the panel will not prematurely abandon current capture or
  start checking a heartbeat that no audit writes yet. **Recommend TLA HOLD application of 2105 until Step 6
  ratifies, or apply now understanding it is announced-but-provisional.** His call — he controls timing since he
  applies all patches.
- **No renumbering.** Avoided touching the §1 Quick Start numbered list; the operational heartbeat check lives in
  bootup.md Step 2 (bulleted) and operating_system.md §6, not as a renumbered Quick Start step.

NO THEO. Owned this patch: edits to `templates/operating_system.md`, `bootup.md`; this fragment. No status move;
no registry value changed; the protocol remains DRAFT. Next: Step 6 — CONV-001 panel review of the protocol
before it is declared canonical and these DRAFT markers are lifted.

Track: WORKFLOW
