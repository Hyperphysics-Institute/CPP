# Reasoning capture — Patch 2106: aggregate CONV-001 review of the Capture-and-Audit Protocol (Step 6)

**STATUS: verbatim (captured at-patch).** Window: 2100-band. Opus worker; integrator = TLA.

Step 6: integrated the 4-reviewer CONV-001 panel response to the Capture-and-Audit Protocol (DRAFT, Patch 2102)
into `templates/reviews-capture_and_audit_protocol.md`. No status moved; ratification is TLA's.

Aggregation decisions:
- **Attribution by TLA receipt labels, not self-labels** (`review_dispatch_protocol.md` §4.1). 4 responses = 4
  independent reads, no double-count. One cross-wiring recorded: the Gemini read self-labelled "ChatGPT" in the
  received text. Verdicts are label-independent so the 4/4 count is unaffected. Flagged one discrepancy for TLA:
  his receipt note said the Gemini response "identified self as Copilot," but the received doc self-labels
  "ChatGPT" — recorded for steer-accuracy, no verdict impact.
- **Tally:** RATIFY-WITH-CHANGES 4/4. T2 (the 2B collapse) ratified SOUND 4/4 — my 2102 design call holds. T1
  (keystone overclaim) and T3 (founder-promote graduation) unanimous CONCERN. T4 split 2/2 but reconciles: the
  two SOUND verdicts assume immediate durable persistence, which the two CONCERN verdicts say must be made
  explicit — no real disagreement, only an unstated premise. T5 3-CONCERN/1-conditional-SOUND converging on
  three closable seams (corpus-completeness, [REVIEW]-queue ownership, the daytime procedural-turn judgment-leak).
- **Change set C1–C8** mapped to protocol sections, kept faithful to what reviewers actually required (did not
  inflate or soften). C7 (schema-validation, partial-night handling, regression suite) routed to the Step-4
  macro build rather than protocol prose, since they are implementation requirements.
- **C3 surfaced as a TLA decision, not auto-resolved.** Three reviewers want measurable graduation gates; Gemini
  wants v2 struck entirely (permanent staged). This is a judgment about automated writes to TLA's own voice in a
  canonical file — his call, not mine. My recommendation (recorded for him): keep v1 staged as the standing
  default and make v2 require explicit TLA enable after measurable criteria, so it never auto-graduates —
  functionally close to Gemini's stricter posture but leaving a defined path.

The protocol stays DRAFT until TLA ratifies the change set (and C3), the revision lands (next patch, 2107), and
TLA declares canonical. NO THEO. Owned this patch: `templates/reviews-capture_and_audit_protocol.md`, this
fragment. No status move; no canonical edit.

Next: on TLA's ratification + C3 call, write the 2102 revision (2107) folding in C1–C6/C8; route C7 to Step 4.

Track: WORKFLOW
