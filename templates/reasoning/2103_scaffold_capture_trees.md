# Reasoning capture — Patch 2103: scaffold the capture trees (Step 3)

**STATUS: verbatim (captured at-patch).** Window: 2100-band. Opus worker; integrator = TLA.

Step 3 of the campaign: scaffolded `Development/transcripts/` (flat by-window raw capture, ground truth) and
`Development/audit_log.md` (the heartbeat log), plus a thin `Development/README.md`. All greenfield; no canonical
file touched, no status move, no THEO.

Decisions taken:
- **No `Registries_temp/`.** Per the 2102 reframe (§8 of the protocol doc), the write-partitioned registry-temp
  collapsed — universal raw capture + the nightly macro's registry-delta extraction make a separate daytime
  write path redundant. So Step 3 scaffolds only the two surviving pieces. (If TLA later wants same-day
  cross-window registry visibility, it returns as a read-only render, not a scaffolded write target — nothing
  here forecloses that.)
- **Heartbeat line format pinned.** This is the one non-trivial decision in the patch: the macro (§4) and the
  bootup-check both depend on a shared shape, so it is fixed now rather than improvised later. Chosen format
  leads with the run DATE (so "did last night run?" is a trivial date-grep), and carries enough counts
  (transcripts read; fragments filed by class; founders staged/review/promoted) to make a run auditable at a
  glance. A written `run=FAIL` is recoverable; only a MISSING line is the loud/blocking case — that asymmetry is
  the whole point of the rail.
- **Honest seed, no fake run.** `audit_log.md` is seeded with the contract and an explicit "SCAFFOLDED — no
  audit has run yet" marker. The macro does not exist until Step 4, so writing any heartbeat line implying a run
  would be a fabrication. The log records only that it is ready to receive lines.
- **Capture-mechanism note carried forward.** The transcripts README restates protocol §3: capture must be
  mechanical (automatic dump/export), not a worker remembering to write each turn, else the root-cause judgment
  reappears one level down. Mechanism is TBD with TLA + Isak; flagged, not assumed.

NO THEO. Owned this patch: `Development/README.md`, `Development/transcripts/README.md`,
`Development/audit_log.md`, this fragment. Next: Step 4 — the macro skeleton (Patch 2104).

Track: WORKFLOW
