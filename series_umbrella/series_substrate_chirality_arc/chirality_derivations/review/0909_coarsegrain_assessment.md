# Chirality-lane assessment — coarse-graining probe (Patch 0820)

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/0909_coarsegrain_assessment.md`
**Patch:** 0909 · **Reviews:** Patch 0820 (F.1/DSL window — coarse-graining → effective η resolves to the canonical m=12 indicator → primitive lean).
**Disposition:** Strong infrastructure result; **both 0908 asks substantially addressed.** Defensible **primitive lean** at a stated rigor — **NOT a verdict.** V3/W3 stand; THEO-CHIR-CAPACITY-1 reserved; DG-3 not yet met.

---

## 1. What 0820 delivered, against the two 0908 asks

**Ask (a) — derive the η-identity, don't assume it: substantially met, geometrically.** 0820 argues the canonical local enantiomorph reads all **12 incident edges** of the vertex figure as a *symmetric* function (participation ratio 12), and that the 4-edge determinant (which would read m=4 → emergent) is a *non-canonical, arbitrary* sub-choice. So m=12 is now argued from geometric canonicity, plus a direct MC of an explicit geometric pseudoscalar: `C_nn ≈ −0.054 ⇒ |K_lift|/K_c ≈ 0.65 < 1 → off-critical → primitive`. This converts 0908's "unproven identification" from an assumption into a *canonically-argued + computed* object — real progress.

**Ask (b) — carry the current through: partially met.** 0820 checked the **bias** (O(δ) tilt): it shifts edge *means* (the harmless homogeneous skew, 0814) but leaves the reading *weights* uniform (m stays 12) and the *connected* coupling ≈δ-independent (`C_nn ≈ −0.054` at δ=0, `−0.059` at δ=0.10). That clears 0907 §3-(1) (the bias does not push the effective coupling toward K_c). See §3 for what this does *not* yet clear.

## 2. Chirality-lane strengthening: CHI-1 independently grounds m=12

A second, *already review-closed* ground for the m=12 identity, which 0820 did not invoke: **THEO-CHIR-CHI-1** (0638, 3/3) established by its locality criterion that the host vertex's nearest neighbourhood — the **icosahedral vertex figure (12 neighbours, d=φ⁻¹), where `n̂` breaks H₄→H₃=I_h** — is the local scale that selects χ=φ⁻³. That is the *same* 12-neighbour vertex figure 0820's canonical η reads. So the effective-η identity now rests on **two independent grounds — 0820's geometric canonicity and CHI-1's review-closed locality — both selecting the 12-neighbour vertex figure.** This materially raises confidence that the relevant object is the vertex-figure η (m=12), well above the m≈8 crossover.

## 3. What is still open (precise, not diffuse)

1. **Dynamical = geometric η (0820 Residual 1 — the core residual, = 0908's caution narrowed).** Both grounds in §1–§2 are *static/geometric*. The verdict needs the *dynamically-selected* effective η — the actual slow mode of Mechanism A — to **be** that vertex-figure object. 0820 reports "no evident mechanism" makes it more local, but that is not a proof. This is the genuine remaining identification step. It is now *narrow* (the geometric target is fixed and doubly-grounded; the question is only whether the dynamics selects it), and 0820's own read is that it "looks like a tractable slow-mode identification, not a creative-mechanism task." Concur: this is the place PCD insight *could* enter, but it is not yet shown to require it.
2. **The O(δ³) current-induced-ordering check (0907 §3-(2)) is NOT decisively cleared.** 0820 cleared the O(δ) *bias* effect, but the broken-detailed-balance **current** is O(δ³) ≈ 10⁻³ at the δ=0.10 probed — too small there to register in the connected-coupling MC, and current-*induced ordering* is a qualitatively distinct (non-equilibrium) effect a small-δ equilibrium-style measurement need not capture. So it is *plausibly negligible by smallness*, not *proven* absent. This remains a named residual.
3. **AFM/frustration vs the K_c=1/12 comparison.** The coupling came out **antiferromagnetic** (C_nn<0). The K_c=1/12 used is the *ferromagnetic* mean-field critical coupling; the correct comparison for an AFM coupling on the frustrated icosahedral/600-cell lattice is the (frustrated) AFM critical coupling, which frustration pushes *higher* — i.e. **even more favourable to the primitive (off-critical) reading.** So the AFM finding is favourable, but the clean "|K_lift|/K_c" number should eventually use the frustrated-AFM K_c (0820 Residual 3). Plus the standing true-K_c > mean-field margin (favourable) and Mechanism-A conditionality (OPEN-FP-F1-2).

## 4. Verdict-owner's read

This is a **well-grounded primitive lean**, not a verdict — and the important meta-result is that **the probe did not bottom out at the PCD layer.** The residuals (§3) are sharp refinements, not walls: the η-identity is doubly-grounded with only the dynamical-selection step open; the current is plausibly negligible by O(δ³) smallness; the AFM/frustration cuts favourably. So the season now looks **closable toward THEO-CHIR-CAPACITY-1 (V3 confirmed / V1 excluded) without requiring the PCD insight** — which, if it holds, is the "chirality as a theorem (primitive)" outcome Thomas asked whether was reachable.

**No verdict move.** DG-3 unmet: §3-(1) (dynamical=geometric η) and §3-(2) (O(δ³) current ordering) must close, and the comparison should move past mean-field K_c, before any verdict language. V3/W3 stand; THEO-CHIR-CAPACITY-1 reserved; header count unchanged; conditional on Mechanism A.

## 5. Recommended next steps (toward a DG-3 verdict claim)

In rough priority, all infrastructure-side (F.1 lane drives; chirality lane reviews + owns the verdict):
1. **Dynamical slow-mode identification** — confirm Mechanism A's coarse-grained order-parameter mode is the vertex-figure η (closes §3-(1), the core residual; the predicted PCD-entry point if anywhere).
2. **O(δ³) current-induced-ordering check** — test for staggered/current-driven η order at larger δ or via the NESS directly, not just the small-δ connected coupling (closes §3-(2)).
3. **Frustrated-AFM K_c + true (beyond-mean-field) K_c** — the correct, more-favourable comparison (tightens §3-(3)).
Once 1–2 close and 3 is quantified, the chirality lane runs the DG-3 swarm review on the CAPACITY-1 claim.
