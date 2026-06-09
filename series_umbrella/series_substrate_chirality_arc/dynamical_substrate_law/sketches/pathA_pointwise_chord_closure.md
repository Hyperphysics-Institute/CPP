# Path A repair — the max=avg lemma was false; the pointwise floor closes via a refined-chord quadratic-form bound

**Patch:** 0828 (Session 156, 8 June 2026) · **Type:** infrastructure (corrects 0827) · **Lane:** F.1 / `dynamical_substrate_law/`.
**Answers:** chirality-lane 0922 — the n̂-concentration counterexample to 0827. **Verify:** `code/0828_pathA_pointwise_chord_bound.py`. Replaces 0827 §(b)'s max=avg step.

---

## What 0827 got wrong (owned)

0827 proved the average-row-sum bound `Σ_v RowSum_v ≤ N ⇒ avg ≤ 1` — that part is rigorous and stands. But it then used **"homogeneity ⇒ all row sums equal ⇒ max = avg ≤ 1,"** which is **false** for the physical η: an n̂-dependent rule is the same functional form everywhere but is **not H4-invariant**, so its row sums are not equal. Reproduced directly (rule `c_e ∝ align_e^β`): as `β` grows, `ρ(M) → 1` while *mean* participation stays `≈ 2` — the n̂-extremal vertices drive `c_max → 1` locally and saturate one shared link to `arc(1)=1`, so `max/avg ≈ 1.7`. A floor on the **mean** participation does not prevent it. The chirality lane (0922) is correct; I had even flagged the non-transitivity of the n̂-rule in my own 0827 notes and then leaned on a transitive matching rule for the numerics anyway. That was the error.

## The correct closure — a pointwise bound, no homogeneity needed

Drop max=avg. Bound the spectral radius directly through the quadratic form, using a **refined chord**: since `(2/π)arcsin(z)/z` is increasing, for `z ≤ z*`,
`(2/π)arcsin(z) ≤ κ·z`, with `κ := (2/π)arcsin(z*)/z* < 1` (for `z* < 1`).

Then for any `‖x‖=1`, with normalized weights `Σ_{w~v}(c^v_{vw})² = 1`:
```
|xᵀMx| = |2 Σ_edges M_vw x_v x_w|
       ≤ 2 Σ_edges κ·c^v_{vw} c^w_{vw} |x_v||x_w|        (refined chord; needs c^v c^w ≤ z*)
       ≤ κ Σ_edges [(c^v_{vw})² x_v² + (c^w_{vw})² x_w²]    (2ab ≤ a²+b²)
       = κ Σ_v x_v² Σ_{w~v}(c^v_{vw})² = κ‖x‖².
```
So **`ρ(M) ≤ κ(z*) = (2/π)arcsin(z*)/z*`**, where `z* = (max weight on any single edge, over all vertices)²`. **No homogeneity, no vertex-transitivity** — it holds for n̂-dependent rules, exactly the family that broke 0827.

The only input is a **pointwise** cap: `c_max(v) ≤ c*` at *every* vertex ⇒ `c^v c^w ≤ c*² = z*` on every edge. A pointwise participation floor `p(v) ≥ p*` gives `c_max(v) ≤ (1/p*)^{1/4}`, hence `z* ≤ 1/√p*` and a closed-form bound:

| pointwise floor p* | 1.5 | 2 | 3 | **4** | 6 | 12 |
|---|---|---|---|---|---|---|
| `ρ ≤ κ` | 0.745 | 0.707 | 0.679 | **0.667** | 0.656 | 0.646 |
| margin | 25% | 29% | 32% | **33%** | 34% | 35% |

So **pointwise `p ≥ 4` ⇒ `ρ(M) ≤ 2/3`, margin 33%.** Verified: adversarial search over 400 n̂-dependent rules capped pointwise at `c_max ≤ (1/4)^{1/4}=0.707` gives worst `ρ = 0.634 ≤ 2/3` ✓ (matching the chirality lane's 0.642). The closed-form `κ` bound is what 0922 asked for; Cauchy–Schwarz / max-row-sum alone was too loose, but the refined-chord quadratic form is tight enough.

## Part (a) — the floor is inherently pointwise

The orientation requirement is itself pointwise: η is a local handedness *at every vertex*, so it must be non-degenerate *at every vertex*. The n̂-concentration counterexample makes `η_v` collapse to a single edge (`p(v) → 1`) at the n̂-extremal vertices — i.e. *no handedness is defined there* — so it is not an admissible handedness field. A genuine 4-D enantiomorph at `v` is the sign of a 4-direction determinant ⇒ `p(v) ≥ 4` at every vertex. That is exactly the pointwise floor the bound needs.

## Honest disposition — outcome 1, on a narrowed footing

Path A's outcome now rests on two clearly separated pieces:
1. **The bound (this patch): PROVEN.** Pointwise `c_max ≤ c* < 1` ⇒ `ρ(M) ≤ κ(c*²) < 1`, closed form, no homogeneity. The empirical-only step 0922 noted is now a theorem.
2. **Orientation ⇒ pointwise non-degeneracy: physically natural, the located residual.** That a genuine local handedness is non-degenerate at *every* vertex is definitional; whether the substrate's dynamics *guarantees* the dynamical η is pointwise non-degenerate (rather than degenerating at special n̂-extremal vertices) is the η-identity in its final, narrowest form. If that guarantee must be *derived* from the substrate rather than taken from "a handedness field is non-degenerate everywhere," this is where the PCD layer re-enters.

So the door to outcome 2 is **narrow but not shut** (the chirality lane's read): the math is closed; the residual is the single physical statement "the dynamical η is pointwise non-degenerate." The verdict is robust across the entire pointwise-non-degenerate class — homogeneous or not.

## Recommendation

Re-fire C1 with the admissibility condition stated **pointwise**: *normalized, pointwise non-degenerate (`p(v) ≥ 4` at every vertex; equivalently `c_max(v) ≤ (1/4)^{1/4}`)*, under which `ρ(M) ≤ 2/3 < 1` by the closed-form refined-chord bound (margin 33%). This preempts the n̂-concentration reconstruction a sharp reviewer would otherwise build against a mean-floor claim. Bank Path B (the explicit narrowed theorem) in parallel as free insurance.

## Scope held

F.1 infrastructure: corrects 0827 §(b). **No verdict moved** (V3/W3 stand; CAPACITY-1 reserved; OPEN-CHIR-1d-β open). No THEO, no ID, no CHIR.md / package edits. Conditional on Mechanism A (OPEN-FP-F1-2); homogeneity is no longer required, but pointwise non-degeneracy of the dynamical η is the load-bearing physical input and is flagged as the residual.
