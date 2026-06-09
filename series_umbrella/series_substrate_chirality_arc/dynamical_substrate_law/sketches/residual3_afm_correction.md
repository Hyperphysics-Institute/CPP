# Residual 3 — Corrected: the Margin Against the Right (Antiferromagnetic) Threshold is ~80%

**Patch:** 0824 (Session 156, 8 June 2026) · **Type:** infrastructure correction (chirality residual 3) · **Lane:** F.1 / `dynamical_substrate_law/` (verdict stays chirality-lane / DG-3).
**Answers:** chirality-lane ruling 0911 — C3 hold: 0821–0823 compared `K_lift` to the **ferromagnetic** `K_c = 1/12 = 1/λ_max`, but the measured coupling is **antiferromagnetic**, so the rigorous threshold is the AFM one (`1/|λ_min|` + frustration). **Verify:** `code/0824_afm_threshold.py`. **Supersedes** the threshold used in 0821/0823.

---

## The imprecision, owned

The chirality lane (0911) is correct: every margin in 0821–0823 (the 0.50–0.64 ratios) was measured against `K_c^FM = 1/λ_max = 1/12`. But the coupling is antiferromagnetic, and an AFM coupling's instability is the **staggered** mode (eigenvalue `λ_min`), not the uniform one. So the right comparison is `|K_lift|` vs `K_c^AFM ≈ 1/|λ_min|`. My 0823 hand-waved this ("staggered isn't net handedness") — but staggered order *does* break the enantiomorph (η→−η) symmetry, so it is verdict-relevant and must be cleared by computation, not dismissed. Here it is.

## The correct threshold and the exact margin (verify 0824)

The 600-cell adjacency spectrum: `λ_max = 12` (uniform/FM), `λ_min = −3.708` — so `|λ_min| ≈ 3.71 ≪ 12`, i.e. the graph is **strongly non-bipartite** (dense in triangles; frustrated for AFM).

| ordering channel | threshold | `|K_lift|/K_c` | margin |
|---|---|---|---|
| uniform / FM (`1/λ_max`) — *suppressed* for AFM coupling | 0.0833 | 0.64 | 36% (the proxy used in 0821–0823) |
| **staggered / AFM (`1/|λ_min|`)** — the *correct* instability channel | **0.2697** | **0.197** | **≈ 80%** |

The criticality product is `|K_lift|·|λ_min| = 0.053 × 3.71 = 0.197` — far below the ordering value of 1. So against the **correct** (AFM/staggered) threshold the margin is **~80%**, *more than double* the ferromagnetic-proxy 36%. The frustration (|λ_min| ≪ λ_max) is exactly what widens it.

**Frustration-corrected MC.** Antiferromagnetic Ising MC (`H = +|K|Σ s_v s_w`), staggered susceptibility via the `λ_min` eigenvector: `χ_stag` stays flat and tiny (≈ 0.004–0.006) all the way to `|K| = 0.20` — **no staggered ordering signal** even at ~4× `|K_lift|`. So the true (frustration-corrected) AFM threshold is at least `0.20` and plausibly absent; the mean-field `0.27` is conservative, and the margin is **≥ 80%**.

**Both channels cleared:** uniform/FM is *suppressed* for AFM coupling (`χ_uniform ≈ 0.6 < 1`), and staggered/AFM is sub-critical by ~80%. There is no ordering instability at `|K_lift|`.

## Effect on residual 1 (0821) — it strengthens

0821's mode-scan margins (all `≈ 0.05` in `K_lift`) were also stated against `K_c^FM`. Recomputed against `K_c^AFM ≈ 0.27`, every candidate mode sits at `≈ 0.18–0.20` of threshold — **all sub-critical by ~80%**. So the "no candidate mode orders" conclusion is *reinforced*, not weakened, by the correct threshold.

## Q1 reconciliation (for the review's note)

The worst-mode small-`m` coupling was computed three times (1.95 → ~0 → 0.50 of `K_c^FM`). The reconciliation (0821) stands: the arcsin model over-counted the shared edge; the `~0` was a single-pair artifact; the **full-correlator value (≈ 0.50 of `K_c^FM`, i.e. ≈ 0.20 of `K_c^AFM`)** is the correct one. The review (Q1) should confirm this rather than take it on faith — but it is sound.

## Status — C3 discharged

With the correct AFM-frustrated threshold: `|K_lift|/K_c^AFM ≈ 0.20`, **margin ≈ 80%** (mean-field; MC ≥ 80%, frustration only widens). All three residuals are now closed against the *right* thresholds:
- **C1** (0821): short-range; no candidate mode orders (margins ~80% against AFM threshold).
- **C2** (0822): O(δ³) current divergence-free, T-parity O(δ⁶)-suppressed.
- **C3** (this patch): exact margin ~80% against the AFM/staggered threshold; frustration-confirmed.

The DG-3 input package (0907 §4) is complete against the correct thresholds. **CAPACITY-1 verdict + DG-3 swarm review remain the chirality lane's.**

## Scope held

Infrastructure (correct AFM threshold + exact margin). **No verdict moved** (V3/V1 stays chirality-lane, DG-3). No THEO, no ID, no CHIR.md / verdict-registry edits. Corrects the threshold used in 0821/0823. Conditional on Mechanism A (OPEN-FP-F1-2).
