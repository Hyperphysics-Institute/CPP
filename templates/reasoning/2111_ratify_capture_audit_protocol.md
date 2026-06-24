# Reasoning capture — Patch 2111: ratify the Capture-and-Audit Protocol (canonical)

**STATUS: verbatim (captured at-patch).** Window: 2100-band. Integrator/founder = TLA. **This is a TLA-authorized STATUS move** ("ratify").

TLA ratified the v1.0-candidate after the clean confirmatory pass (panel RATIFY 4/4, two CONV-001 rounds).
Flipped the protocol STATUS to CANONICAL and lifted the DRAFT markers across all touch points:
`capture_and_audit_protocol.md` (STATUS, §3.1, §12), `operating_system.md` (§2 row, §4 paper-production
subsection + Phase-5 pointer, §6 capture subsection + capture-table row), `bootup.md` (Step-2 heartbeat check,
§5 row), `paper_completion_checklist.md` (parallel-window collision note). Reviews file closed with a ratification
record.

**Key distinction preserved (not a silent over-lift): ratified ≠ operational.** The panel cleared the protocol
"safe to adopt as standing practice ONCE the §3.1 capture mechanism is implemented," and §3.1 makes the keystone
guarantee contingent on that mechanism. So 2111 lifts the *ratification* gate (DRAFT → canonical) but KEEPS an
explicit *activation* gate: the protocol is not operational until (a) the §3.1 always-on/zero-touch/fsync-durable
capture mechanism and (b) the Step-4 nightly macro exist and are scheduled. Until then, windows continue current
capture/registry practice — and critically, the paper-production `Registries_pending/` deferral stays inactive
(a pending write would never reach canonical without the overnight merge that does not yet exist). Lifting that
safeguard prematurely would have silently broken registry updates. This honors ChatGPT's archival caution that
§3.1 implementation verification is part of validation, not a mere engineering detail.

NO THEO. Owned this patch: STATUS/DRAFT-marker edits across the four files + reviews ratification record; this
fragment. This is the one authorized status move of the campaign (TLA "ratify").
Next: the Step-4 build — Phase-2 classifier + Phase-4 extractor (replace the skeleton stubs), §4.3 hardening
(schema-validation, partial-night handling, regression suite), and the §3.1 capture mechanism + nightly scheduler
(gated on TLA/Isak decisions on the capture mechanism and the local-machine scheduler). Activation flips when
those land.

Track: WORKFLOW
