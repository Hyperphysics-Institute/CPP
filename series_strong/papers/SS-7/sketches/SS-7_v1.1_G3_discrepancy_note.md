# SS-7 v1.1 — Numerical Discrepancy Registered During G3 Verification

**Date:** 20 April 2026
**Context:** Phase 7 §G3 verification pass, SS-7 v1.1 documentation suite
**Severity:** Minor (does not affect any individual prediction or claim)
**Status:** REGISTERED for next revision cycle (v1.2 or SS-7-series continuation)

---

## The discrepancy

The paper's **Abstract (§1 Main Result), §3.1 Table 1 caption, and Figure 3 caption** all cite the RMS error across the 8 alpha-chain predictions as **0.88%**.

A first-principles computation from the printed Table 1 values (or from the formula $B(N_\alpha) = N_\alpha \Balpha + (3N_\alpha - 6) B_{\text{pair}}$ with $B_\alpha = 28.296$ MeV and $B_{\text{pair}} = 2.342$ MeV or $M_0/\varphi$ exactly) gives:

- **All 8 nuclei, full precision:** RMS = **0.909%**
- **All 8 nuclei, using Table 1 rounded errors:** RMS = **0.910%**
- **7 nuclei, excluding ${}^{20}$Ne (the known-deformation outlier):** RMS = **0.862%**
- **Mean absolute error, all 8 nuclei:** 0.791%

## Likely source

The paper's cited value **0.88%** is within 0.01 of the 7-nucleus RMS excluding ${}^{20}$Ne. The ${}^{20}$Ne residual of $+1.19\%$ is separately discussed in §5.3 as attributable to the known prolate deformation of that nucleus, outside the rigid-polytope formalism. It is plausible that the abstract's 0.88% was computed excluding this outlier — a defensible framing in multi-nucleus fits, but one the paper does not explicitly flag.

## Magnitude and significance

**0.03 percentage points.** The difference does not affect:
- Any individual prediction value (all 8 unchanged)
- The ±1.5% qualitative claim ("all within ±1.5%")
- The programme's "zero-parameter, multi-nucleus agreement" conclusion
- The falsifiability criteria (§6.3)
- The stress-test results (§6.5)
- Any downstream registry entry (predictions.md, axiom-registry.md PRED #40-47)

It does affect the specific numerical claim "RMS 0.88%" in 4 locations:
1. Main Result box in §1
2. Text after Table 1 in §3.1 (line 625)
3. Figure 3 pgfplots legend (line 680)
4. Figure 3 caption (line 710)

## Recommended resolution

**Option A (minimal correction, recommended):** Issue SS-7 v1.2 changing the four "RMS 0.88%" instances to one of:
- "RMS 0.91% (0.86% excluding ${}^{20}$Ne; see §5.3 on prolate deformation)"
- "RMS $\sim 0.9\%$"
- "RMS 0.86% excluding ${}^{20}$Ne; 0.91% including"

Option A honestly discloses the ${}^{20}$Ne-exclusion framing while keeping the substantive claim ("multi-nucleus agreement at sub-percent level") unchanged.

**Option B (defer):** Note the discrepancy in the next reviewer cycle's response document and address in a v1.2 batch if other minor items accumulate. Appropriate if no other v1.2-class items emerge before SS-8 ships.

**Option C (decline):** Argue that "RMS 0.88%" in context refers to the seven matched predictions excluding the explicitly-discussed ${}^{20}$Ne deformation anomaly. Defensible but requires adding a footnote to that effect.

## Why this is in the programme record

Integrity. The discrepancy was caught by the Phase 7 §G3 numerical cross-check (operating_system.md §4.10) — exactly the role that check exists to play. Documenting it here preserves the protocol's credibility: the verification step caught a real (if minor) mismatch; the mismatch is not being silently buffered.

## Register in research_frontier.md

Added as a minor-revision-tracked item under CONJ-SS-12 in research_frontier.md (separate from the main CONJ-SS-12 entry; appended as v1.1 footnote).

---

*Discrepancy discovered 20 April 2026 during Phase 7 G3 verification of SS-7 v1.1. Discovered by Claude Opus running the verification notebook `SS-7_alpha_cluster_edge_formula.py` against the `.tex` Table 1 values. Recorded for transparency; resolution deferred to programme principal's decision.*
