# Chirality-lane assessment — residual closures 0821 / 0822, and the DG-3 readiness ruling

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/0911_residual_closures_dg3_readiness.md`
**Patch:** 0911 · **Reviews:** Patch 0821 (residual 1 — η-identity), Patch 0822 (residual 2 — O(δ³) current).
**Ruling:** **C1 and C2 substantially discharged; C3 NOT yet discharged.** **HOLD the DG-3 review until residual 3 (the precise AFM-frustrated K_c) is quantified.** No verdict; V3/W3 stand; THEO-CHIR-CAPACITY-1 reserved; conditional on Mechanism A.

---

## 1. C1 (residual 1, 0821) — discharged, one caveat for DG-3 Q1

- **Locality: clean.** The vertex-figure η correlator is nearest-neighbour only (d=1: −0.053; d=2: +0.0004; d=3: ≈0). The effective η-theory is short-range → a local-coupling model → the order parameter is the local vertex-figure η. ✔
- **No candidate mode orders (stronger than C1 asked).** Scan m∈{4,6,8,12} × 3 frames → all |K_lift|/K_c ∈ [0.50, 0.64], sub-critical. So the verdict-lean does **not** hinge on pinning the exact effective η — whichever local mode the dynamics selects, none condenses. This is a more robust discharge than "dynamical = geometric η." ✔✔
- **Caveat (→ DG-3 Q1, not a blocker):** the worst-case small-m coupling has now been computed **three times with three answers** — arcsin model 1.95 K_c (super-critical), 0820 single-pair ≈0, 0821 full-correlator 0.50 K_c. The 0821 full-correlator is the faithful one and the reconciliation is sound (the arcsin model overestimated via an assumed coherent shared-edge term; genuine geometric orientation-signs partially cancel). But the volatility means **Q1 must confirm the 0821 computation rather than take 0.50 on faith**, and the mode-scan is a sample, not a proof (honestly flagged in 0821). The tight consistency across frames argues genericity.

## 2. C2 (residual 2, 0822) — discharged at the physical bias

- Current is O(δ³) (J ∼ δ^3.09), tiny at the physical bias δ=φ⁻³ (J≈3×10⁻⁵). ✔
- **The load-bearing argument is the T-parity suppression, not div J=0.** The current is T-odd; the η-ordering ⟨η⟩ is T-even; so the current couples to ordering only at even powers, O(J²)=O(δ⁶)≈0.0002 ≪ the margin. This is sound. (Worth stating explicitly: *div J=0 alone would not suffice* — a divergence-free/circulating current can still drive ordering in driven systems — but the T-parity O(δ⁶) suppression does the work, and the smallness at physical δ makes it overwhelming.) ✔
- **Caveat (→ DG-3 Q2):** parametric / physical-scale + symmetry argument, not an all-orders proof. Appropriate at the physical bias; flagged honestly.

## 3. C3 (residual 3) — NOT discharged; this is the one real hold

**The key point a verdict cannot skip:** every margin in §1–§2 (the 0.50–0.64 ratios) is computed against **K_c = 1/12 = 1/λ_max — the *ferromagnetic* mean-field critical coupling.** But the coupling is **antiferromagnetic** (C_nn < 0). The rigorous comparison is |K_lift| against the **AFM** critical coupling ≈ 1/|λ_min| (mean-field) plus the frustration correction — and 0821's code does **not** compute λ_min or the AFM K_c. So the present verdict-lean rests on a *ferromagnetic K_c proxy for an antiferromagnetic coupling*.

- It is *likely* conservative: for the non-bipartite / odd-cycle-frustrated 600-cell, |λ_min| < λ_max = 12, so the AFM K_c = 1/|λ_min| > 1/12 — i.e. 1/12 *understates* the relevant K_c, making the true margin wider; and frustration raises it further. But "likely conservative" must be **computed (λ_min), not assumed**, before a verdict.
- The margins (0.50–0.64) are **moderate, not ≪ 1**, so the 0910 §5 "clean K_lift ≪ 1/12 conservative pass" shortcut is **not** met — the precise comparison is needed.
- This is exactly **DG-3 Q3**. Firing the review now invites the objection "you used the ferromagnetic K_c for an AFM coupling."

## 4. Ruling: HOLD DG-3 for residual 3

Quantify residual 3 — compute λ_min and the **AFM-frustrated, beyond-mean-field K_c**, and confirm |K_lift| sits below it with an exact margin — **before** firing the DG-3 swarm review. Accept the F.1 window's offer to do this. Rationale: (a) it is the C3 criterion as written in 0910 (the correct AFM K_c, not 1/12); (b) it is the reviewer's Q3; (c) it is one readily-computable quantity, and the direction is favorable; (d) the margins are moderate, so the conservative shortcut does not apply; (e) closing it first is cleaner than running on a proxy and patching post-review. This is a **short, favorable-direction hold** — it does not change the expected outcome, it makes the verdict airtight.

When residual 3 lands, all three conditions are discharged and the DG-3 scaffold (0910) fires against a frozen, complete package.

## 5. Big picture (the question that was open all season)

The decisive residual (1) closed **by computation**, the completeness residual (2) closed, and **neither needed the PCD layer** — the single spot flagged as possibly requiring Thomas's mechanism-invention resolved mechanically. So **THEO-CHIR-CAPACITY-1 (chirality a genuine primitive, V3 confirmed / V1 excluded) looks set to pass DG-3**, conditional on C3 closing favorably — which it directionally does. The insight stays in reserve and may not be called at all.

**Framing guard holds throughout:** μ²>0 / off-critical ⇒ chirality **primitive**, not emergent. **No verdict moved.** V3/W3 stand; THEO-CHIR-CAPACITY-1 reserved until DG-3 runs on the C1+C2+C3-complete package. Conditional on Mechanism A (OPEN-FP-F1-2).
