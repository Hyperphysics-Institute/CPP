# Letter to Reviewers — SS-7 Table 1 Isotope-Choice Question

**From:** Thomas Lee Abshier ND (Hyperphysics Institute) and Claude Opus (Anthropic), co-authors of SS-7
**To:** SS-7 reviewers (ChatGPT, Copilot, and Grok both round-2 "accept with minor revisions")
**Subject:** Data-verification request — possible diagnostic error in SS-7 §5.1 / Table 1 (N_α ≥ 12 rows) and OPEN-SS-22 framing
**Date:** 21 April 2026
**Attachment:** `SS-7_alpha_cluster_edge_formula.tex` (source file; do not work from the compiled PDF — a prior round of reviews showed that superscript rendering in the PDF caused reliable misreadings of `1/z` as `1/2` in the residual-band formula)

---

Hello,

During Phase 1 exploration for SS-8 on 21 April 2026, an empirical-map step intended to extend SS-7's Table 1 across the full N=Z alpha-chain surfaced a finding that may affect SS-7 v1.1 itself, not just SS-8. We want your independent verification before acting on it.

## The finding (in one paragraph)

SS-7 Table 1 at N_α ≥ 12 (lines 777–780 of the `.tex`) uses ⁴⁸Ti (Z=22, N=26), ⁵²Cr (Z=24, N=28), ⁵⁶Fe (Z=26, N=30) as the data anchors for the "structural onset" at N_α ≥ 12 that motivates OPEN-SS-22. These three nuclei each carry +4 neutron excess over N=Z. The ⁴⁸Cr row at line 777 is listed with `---` for the measured value and the annotation `(not N=Z)`, but ⁴⁸Cr is Z=24, N=24 — it **is** N=Z, and its binding energy is present in AME 2020. When the formula is applied to the strict N=Z alpha-chain (⁴⁸Cr, ⁵²Fe, ⁵⁶Ni) instead of to the paper's chosen non-N=Z nuclei, the −2 to −2.5% "flat residuals" disappear. The N=Z values are in family with the primary 8-nucleus set.

If this reproduces under your verification, OPEN-SS-22's empirical anchor — the paragraph at lines 785–787 of the `.tex` ("The residuals at N_α ≥ 12 are approximately flat at −2 to −2.5% … The icosahedron is the unique closed convex polytope on exactly 12 vertices …") — is anchored on a pattern that is an isotope-selection artifact, not a structural signature. The paper's OPEN-SS-22 hypothesis would need to be retired or substantially reframed, and SS-8 would pivot from OPEN-SS-22 (icosahedral closure) to OPEN-SS-23 (non-N=Z extension).

## What we are asking you to verify

**Task 1 — AME 2020 binding energies for the strict N=Z alpha-chain.** Please independently look up or compute the AME 2020 binding energies for:

| N_α | Nuclide | Z | N | Claude's AME value (MeV) |
|-----|---------|---|---|--------------------------|
| 11 | ⁴⁴Ti | 22 | 22 | 375.475 |
| 12 | ⁴⁸Cr | 24 | 24 | 411.462 |
| 13 | ⁵²Fe | 26 | 26 | 447.696 |
| 14 | ⁵⁶Ni | 28 | 28 | 483.990 |

and for comparison, the paper's current Table 1 choices:

| N_α | Nuclide | Z | N | Claude's AME value (MeV) |
|-----|---------|---|---|--------------------------|
| 12 | ⁴⁸Ti | 22 | 26 | 418.699 |
| 13 | ⁵²Cr | 24 | 28 | 456.349 |
| 14 | ⁵⁶Fe | 26 | 30 | 492.254 |

Please report your AME values for each nuclide. If any disagree with Claude's recall, flag which.

**Task 2 — Residual computation against the SS-7 formula.** Using $B_\alpha = 28.296$ MeV and $B_{\text{pair}} = 2.342$ MeV (the paper's inputs), compute

$$B_{\text{pred}}(N_\alpha) = N_\alpha \cdot B_\alpha + (3 N_\alpha - 6) \cdot B_{\text{pair}}$$

for N_α = 11, 12, 13, 14. Report predicted binding and residual `(B_exp − B_pred)/B_exp × 100%` for each of the seven nuclides in Task 1. Claude's values, for you to check against:

| Nuclide | N_α | Predicted | Residual |
|---------|-----|-----------|----------|
| ⁴⁴Ti | 11 | 374.490 | +0.26% |
| ⁴⁸Cr | 12 | 409.812 | +0.40% |
| ⁵²Fe | 13 | 445.134 | +0.57% |
| ⁵⁶Ni | 14 | 480.456 | +0.73% |
| ⁴⁸Ti | 12 | 409.812 | +2.12% |
| ⁵²Cr | 13 | 445.134 | +2.46% |
| ⁵⁶Fe | 14 | 480.456 | +2.40% |

**Task 3 — Interpretation question.** Two possibilities frame the finding differently:

- **(a)** The paper's N_α ≥ 12 Table 1 rows were chosen by isotope abundance (⁴⁸Ti, ⁵²Cr, ⁵⁶Fe are the most-abundant isotopes of their elements). The choice conflates neutron-excess binding (~2 MeV per extra neutron, structure-independent) with a hypothesized icosahedral-closure signal. OPEN-SS-22 is misdiagnosed; the correct question is OPEN-SS-23 (neutron-excess extension).

- **(b)** There is a principled physical reason to include the +4-neutron isotopes rather than the strict N=Z alpha-chain at N_α ≥ 12. The two ΔN = +4 could (for example) track shell-closure physics that supplements the alpha-cluster binding and is part of what OPEN-SS-22 is trying to describe. In this case OPEN-SS-22 survives but must explicitly specify that the relevant data includes non-N=Z isotopes and explain why.

Question for you: which interpretation do you find more defensible given the data? If (a), do you see other passages in the paper that need to change beyond what is outlined in the v1.2 plan (below)? If (b), what is the mechanism that would justify the isotope choice?

**Task 4 — Is the labeling on line 777 a data error, a framing error, or both?** The entry

`${}^{48}$Cr & 12 & 30 & 409.82 & --- & (not N=Z) \\`

has two distinct defects:
- The `---` for measured BE: AME 2020 gives 411.462 MeV; this is not missing data.
- The `(not N=Z)` annotation: ⁴⁸Cr is Z=N=24.

At minimum, v1.2 must replace this row with the correct 411.462 MeV value and remove the annotation, regardless of how the broader OPEN-SS-22 question resolves.

## What does not change regardless of outcome

The paper's central contribution — Theorem 2.1, the formula $B = N_\alpha B_\alpha + (3N_\alpha - 6) B_{\text{pair}}$, the ⁸Be in-formula derivation, the adversarial stress test at §7.5, the primary 8-nucleus result for N_α = 3–10 — is not called into question by this finding. If interpretation (a) holds, the primary set's fit quality *improves* (N_α = 11, 12, 13, 14 in-family at +0.26% to +0.73% rather than diverging at N_α ≥ 12). The finding narrows OPEN-SS-22's scope; it does not undermine SS-7's positive result.

## What we are preparing as v1.2

Independently of how you answer Task 3, a v1.2 revision combining this finding with the previously-registered G3 RMS discrepancy (0.88% cited vs. 0.91% first-principles; see `SS-7_v1.1_G3_discrepancy_note.md`) is being drafted. Scope:

1. Correct the line-777 data error on ⁴⁸Cr regardless.
2. Replace or supplement the N_α ≥ 12 Table 1 rows based on your Task 3 answer.
3. Update the RMS citation to 0.91% (all 8, first-principles) or equivalent honest framing.
4. Rewrite §5.1 and the OPEN-SS-22 discussion in keeping with Task 3.
5. Update abstract accordingly.
6. Retire or rewrite OPEN-SS-22. If retired, recover the registry slot; if reframed, specify the new empirical anchor.

## Methodological note on this cycle

This finding was surfaced by Claude Opus during SS-8 Phase 1 exploration — i.e., during a discovery step whose ostensible purpose was to extend the empirical map, not to audit SS-7. We are treating it with the same symmetric-honesty standard that the G3 discrepancy triggered (see `templates/relationship_protocol.md` §2.6): the finding is flagged openly, no result is silently adjusted, and verification is requested before corrective action.

A secondary methodological item: this letter is being sent with the `.tex` source attached, not the compiled PDF. Two round-2 reviewers independently misread `φ^{1/z}` as `φ^{1/2}` in the compiled PDF (the superscript `z` ligaturing at small size). We have updated the submission protocol accordingly; please read from the `.tex` for any passages where numerical symbols matter.

## Response format requested

A short response document addressing Tasks 1–4 in order. Equations and AME values in plain text (or LaTeX) rather than embedded images. If your independent computation disagrees with Claude's on any value, please show your arithmetic so we can reconcile.

If your answer to Task 3 is "(b) there is a principled reason to use the non-N=Z isotopes," please state the reason concretely. If you cannot construct a concrete reason and default to (a) by elimination, please say so — "I cannot think of a defensible reason for (b)" is a valid answer.

Thank you for continuing at the round-2 standard through this unplanned revision cycle.

Respectfully,

**Thomas Lee Abshier ND**
Hyperphysics Institute, Kalispell, Montana

**Claude Opus (Anthropic)**
SS-7 co-author
