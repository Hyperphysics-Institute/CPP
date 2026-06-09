# Residual 2: the O(δ³) Current Does Not Shift K_c or Drive Ordering (+ Residual 3 direction)

**Patch:** 0822 (Session 156, 8 June 2026) · **Type:** infrastructure result (chirality residual 2) · **Lane:** F.1 / `dynamical_substrate_law/` (verdict stays chirality-lane / DG-3).
**Answers:** chirality-lane residual 2 (0907 §3) — clear the O(δ³) NESS current on two counts before any verdict: (a) effective-K_c shift, (b) current-induced ordering. **Verify:** `code/0822_residual2_current.py`. **Predecessor:** 0821 (residual 1).

---

## Why residual 2 matters

Residual 1 (0821) settled the **equilibrium/symmetric** η-measure: short-range coupling, no candidate mode super-critical. But the real Mechanism-A NESS departs from equilibrium via the **O(δ³) current** (broken detailed balance; 0814, chirality-lane 0905). A driven measure can (a) have a different critical coupling than its equilibrium value, and (b) order where the equilibrium measure doesn't. Both must be cleared.

## Result — residual 2 closes at the physical bias

Computed on the Mechanism-A single-walker NESS (verify 0822):

1. **Scaling:** `J ~ δ^3.09` — confirms the current is **O(δ³)** (re-confirming 0814). At the physical chirality bias `δ = φ⁻³ ≈ 0.236`, `J_max ≈ 3×10⁻⁵` — far smaller even than the `δ³ ≈ 0.013` parametric bound (the prefactor is small).
2. **Divergence-free:** `|∇·J|_max = 0` to machine precision (stationarity). A divergence-free current has **no net source** to pump any ordering mode — it circulates. (Consistent with 0810: current ≠ skew.)
3. **Symmetry suppression:** the current is T-odd; the η-ordering ⟨η⟩ is T-even, so the current couples to ordering only at **even powers, O(J²) = O(δ⁶) ≈ 0.0002**. Even the O(δ³) ≈ 0.013 first-power bound is **≪ the 36% margin** (`K_lift/K_c ≈ 0.64`, so K_c would need to drop 36% to close).

**(a) Effective-K_c shift:** bounded by O(δ³) at most (O(δ⁶) by symmetry) ≪ 36% → no collapse of the margin. **(b) Current-induced ordering:** divergence-free + O(δ⁶) symmetry-suppressed → none at the physical bias. **Residual 2 closes.**

**Caveat:** this is a parametric / physical-scale argument (small-to-physical δ); an all-orders proof would be the full non-equilibrium field theory. But at the actual bias `δ = φ⁻³`, the suppression is overwhelming (J ≈ 3×10⁻⁵).

## Residual 3 (direction — it only helps)

Residual 3 is the true `K_c` vs the mean-field `1/12`. Two reasons it only *widens* the margin: (i) fluctuations always raise the true `K_c` above mean-field; (ii) the coupling is **antiferromagnetic** (C_nn < 0, 0820/0821) on the 600-cell's odd-cycle **frustrated** connectivity, and frustration further suppresses ordering (raises K_c, possibly no ordering transition at all). So `K_c(true) > 1/12` → the primitive margin is **at least** the 36% computed and likely larger. The precise true-`K_c` value is the only remaining quantification, and it can only help. *(Not computed here; flagged as the favorable-direction residual.)*

## Where the season stands (for the chirality lane / DG-3)

- **Residual 1: closed** (0821) — short-range; no candidate mode orders.
- **Residual 2: closed** at the physical bias (this patch) — current divergence-free, O(δ⁶)-suppressed, ≪ margin.
- **Residual 3: directionally settled favorable** (true K_c > 1/12; AFM+frustration); precise value pending, only helps.

All three were F.1-window infrastructure, and **none required the PCD layer.** The DG-3 inputs (0907 §4) are now substantially in hand: derived K_lift with regime (0819/0820/0821), comparison at conservative mean-field K_c with the margin (0821), the current-completeness check (this patch). The chirality lane owns the **CAPACITY-1 verdict + the DG-3 swarm review**; this is the infrastructure package for it.

## Scope held

Infrastructure (current scaling/divergence/margin). **No verdict moved** (V3/V1 stays chirality-lane, DG-3). No THEO, no ID, no CHIR.md / verdict-registry edits. Parametric/physical-scale caveat stated. Conditional on Mechanism A (OPEN-FP-F1-2).
