# Reasoning capture — Patch 1126 (Task 5 cycle-opening: the DG-3 dispatch package)

**Protocol:** `templates/reasoning_capture_protocol.md` + `templates/review_dispatch_protocol.md`.
Session 156 lane (band 11xx), 11 June 2026. Companion to
`review/a3prime_axiom_review_package_v1.0.md`.

## Package design decisions

- **Self-containment per the Patch-0656 learning:** the three construction-phase verify scripts
  (1123/1124/1125) are embedded in full in §7 — these back every claim under adjudication, so a
  reviewer can reach SCRIPT-EXECUTED from the package alone. The diagnostic-phase scripts
  (1115/1116/1119/1120) support the *necessity* context and are summarized in §2 with repo paths;
  T6 invites reviewers to attack the necessity claims, fetching those files if they wish.
- **Triage order:** T1 = the OB-2 chain (the kill switch — constraint inheritance, leak hunting,
  the energy argument) and T2 = the completion rule's status, because these are the two places a
  verdict can flip. T3–T7 are calibration-grade unless something breaks. The two architect-flagged
  honesty questions (Q1 → T2; Q2 → T5) are posed verbatim rather than softened.
- **Maximum-scrutiny framing:** stated in the header that this is the programme's first axiom-level
  change put to the panel. The panel should treat it accordingly.
- **Steers per the protocol §5 defaults,** specialized: Grok → run + recompute (branching, Peters,
  symbolic cancellation), T1(ii) leak-hunting; Copilot → C3→C4→C5 structural chain + T2/T5
  adjudication; ChatGPT → T1(iii) energy argument + overclaim sweep + the disambiguation rider.
- **Response format** requires the CONFIRM/RESTATE/REJECT trichotomy with verdict-flipping vs
  calibration separation, per the MERGE-2/STATUS/CAPACITY-1 cycle pattern.

## Discipline notes

- Built on the pushed 1125 (architect's hash 7d988a1). Private-lane only (new review/ subfolder +
  README/INDEX notes). NO VERDICT MOVED — the package *requests* the verdict; registration still
  waits on 3/3 + sign-off, then the single STOP-and-warn registry patch.
- Responses will aggregate in `review/reviews-A3PRIME.md` (created at integration, per the
  TARROW/CAPACITY-1 pattern).
