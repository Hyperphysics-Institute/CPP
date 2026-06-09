# Path A closes — the weight-concentration falsifier is defeated by vertex-transitivity (the loose adversary is non-homogeneous)

**Patch:** 0827 (Session 156, 8 June 2026) · **Type:** infrastructure (the two-part Path-A computation 0921 §1) · **Lane:** F.1 / `dynamical_substrate_law/` (verdict + DG-3 + CAPACITY-1 stay chirality-lane).
**Answers:** chirality-lane 0921 — the ChatGPT weight-concentration falsifier. **Verify:** `code/0827_pathA_weight_concentration.py`. Builds on 0826 (the equal-weight closure). The two parts 0921 asked for: **(a)** orientation ⇒ participation floor, **(b)** worst-case row sum under vertex-transitivity.

---

## The falsifier (granted, it is real)

`R(m) = m·(2/π)arcsin(1/m)` assumed equal-weight reads (shared-edge correlation `1/m`). A weighted observable can concentrate weight `W` on one shared edge: nominally `m ≥ 4`, but spectrally it slides toward the critical single-edge `m=1`. The chirality lane verified the loose worst case (`Σ_i (2/π)arcsin(w_i a_i)`) stays `> 1` even at participation `p = 4–5`. So a bare `m_eff ≥ 4` floor does not, by itself, restore `ρ < 1`. Correct. The equal-weight assumption was doing silent work.

## Part (b) — vertex-transitivity is the missing ingredient (the loose adversary is unphysical)

The connected coupling is still shared-edge-only (0826), so with normalized weights `Σ_e (c^v_e)² = 1` the per-link entry is `M_vw = (2/π)arcsin(c^v_{(v,w)}·c^w_{(v,w)})`. Two facts:

1. **AM–GM row-sum identity.** `arcsin` is convex on `[0,1]`, so it lies below its chord: `(2/π)arcsin(z) ≤ z`. Hence
   `Σ_v RowSum_v ≤ Σ_v Σ_w c^v_{(v,w)} c^w_{(v,w)} = Σ_edges 2·c^v c^w ≤ Σ_edges (c^v² + c^w²) = Σ_v 1 = N.`
   So the **average** row sum `≤ 1`, for *any* normalized weighting whatsoever. Equality needs `z∈{0,1}` and `c^v=c^w` on every edge — i.e. **full single-edge concentration**, nothing milder.

2. **Homogeneity makes the average the maximum.** A single translation-invariant rule on the (edge-transitive) 600-cell gives every vertex the *same* row sum `R*`. Then `R* ≤ 1` by (1), and `ρ(M) ≤ ρ(|M|) = R*` (Perron; `|M|≥0` vertex-transitive ⇒ uniform mode saturates). So **`ρ(M) ≤ R* ≤ 1`, strict (`< 1`) for any participation `p > 1`.**

**Why the loose adversary is excluded:** its `Σ ≈ 1.7` requires *every* neighbour of `v` to concentrate its weight onto the edge to `v` — in-degree `12` at `v`. But each vertex concentrates on *one* edge (out-degree 1), so the in-degrees average to 1; a high-in-degree vertex forces low-in-degree vertices elsewhere. A single homogeneous rule cannot give every vertex the special row — the average bound (1) forbids it. The loose worst case is **non-homogeneous**, hence not an admissible order parameter.

Verified on the 600-cell (worst-case homogeneous rule = reciprocal perfect-matching concentration, weight `W`, rest `ε`):

| participation p | 12 | 7.4 | 3.7 | 2.0 | 1.4 | 1.1 | →1 |
|---|---|---|---|---|---|---|---|
| ρ(M) = R* | 0.637 | 0.640 | 0.652 | 0.685 | 0.742 | 0.830 | →1 |
| margin | 36% | 36% | 35% | 32% | 26% | 17% | →0 |

`ρ(M)` rises monotonically from the equal-weight `0.637` toward `1` **only** as `p → 1` (full concentration). Random non-uniform weightings give average row sum `≈ 0.28`, max `≈ 0.6–0.77` — all sub-critical.

## Part (a) — orientation ⇒ participation floor

The AM–GM bound already gives `ρ < 1` for *every* homogeneous weighting except full single-edge concentration (`p=1`). And `p=1` is `η_v = sign(w_e x_e)` — the sign of one edge variable times a fixed weight, carrying **no configurational handedness** (the orientation is entirely in the precomputed `w_e`; the dynamics is just the sign of one Gaussian). A genuine enantiomorph indicator resolves an orientation, which in 4-D is the sign of a `4×4` determinant of `≥ 4` directions, so its participation floor is `p ≥ 4` → `ρ ≤ R*(4) ≈ 0.65`, **margin ≈ 35%**. Even the minimal non-degenerate handedness (`p > 1`) is strictly sub-critical.

## What this closes, and what it rests on

**Path A closes** for the homogeneous, non-degenerate admissible class — which is effectively universal: the *only* excluded observable is the single-edge `p=1`, which is not a handedness. The verdict is robust across the whole weight class (it depends only on `p > 1`, satisfied by any genuine enantiomorph), so **the η-identity is dissolved for the verdict** — the substrate does not need to pin the exact η-weighting, and **Thomas's PCD-layer insight is not called** (outcome 1, not outcome 2). This is the part 0921 flagged as "a real computation not yet done": both pieces — the homogeneous worst-case row-sum bound (b) and the orientation floor (a) — are now done.

**Load-bearing input:** *homogeneity* (vertex-transitivity) of the dynamical η. This is what excludes the loose adversary, and it is grounded in the substrate's homogeneity — the dynamical order parameter on a homogeneous substrate has a translation-invariant coupling; a non-homogeneous η would require spontaneous *translation*-symmetry breaking, a separate instability, not the chirality verdict. It is a property of the Mechanism-A measure (the per-edge-independent, homogeneous fluctuation structure of 0826 §1), so it sits within the standing Mechanism-A conditionality, but it is the structural fact the closure rides on and is stated as such.

## Recommendation

Hand to the chirality lane to re-fire with C1 amended to carry the explicit admissibility condition ChatGPT asked for: **homogeneous (translation-invariant) + non-degenerate participation (`p > 1`; physically `p ≥ 4` for a 4-D enantiomorph)**, under which `ρ(M) ≤ R*(p) < 1` (margin ≈ 35% at the orientation floor). This is exactly ChatGPT's "state an effective-participation condition," now with the homogeneous worst-case bound computed — which is what the two CONFIRMs asserted but did not test. Expected to clear the live Q1 successor for a real 3/3.

## Scope held

F.1 infrastructure: the two-part Path-A computation. **No verdict moved** (V3/W3 stand; CAPACITY-1 reserved; OPEN-CHIR-1d-β open). No THEO, no ID, no CHIR.md / package / verdict-registry edits. Builds on 0826. Conditional on Mechanism A (OPEN-FP-F1-2), with the homogeneity input made explicit.
