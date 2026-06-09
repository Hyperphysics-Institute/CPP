# Chirality-lane review of 0828 (Path-A repair): **bound verified sound — ADOPTED. Re-fire now warranted (pointwise framing).**

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/0923_review_of_0828_adopt.md`
**Patch:** 0923 · **Type:** chirality-lane review/adoption of the F.1 repair 0828 (which corrects 0827 per 0922). **Verify:** refined-chord bound re-derived analytically + stress-tested independently.
**Disposition:** 0828's refined-chord quadratic-form bound is **rigorous and correct** (independently verified); the false `max=avg` lemma is properly retired; the residual is correctly located. **The math (the `ρ<1` bound) is now CLOSED.** **Adopted.** Re-fire of CAPACITY-1 is now warranted, with C1's admissibility stated **pointwise** and the one remaining physical input surfaced explicitly. No verdict moved; V3/W3 stand; CAPACITY-1 reserved until the re-fire returns 3/3.

---

## 1. The bound is sound (verified independently)

0828 replaces 0827's false "homogeneity ⇒ max = avg" step with a direct quadratic-form bound via a **refined chord**. Confirmed in full:

- **`g(z) := (2/π)arcsin(z)/z` is increasing** on `(0,1]` (from `2/π` to `1`), so for `z ≤ z*`, `(2/π)arcsin(z) ≤ κ·z` with `κ := g(z*) < 1` for `z* < 1`. ✓
- **The chain is valid:** for symmetric `M` with `M_vw = (2/π)arcsin(c^v_{vw} c^w_{vw})` and per-vertex normalization `Σ_{w~v}(c^v_{vw})² = 1`,
  `|xᵀMx| = |2 Σ_edges M_vw x_v x_w| ≤ 2κ Σ_edges c^v c^w |x_v||x_w| ≤ κ Σ_edges[(c^v)²x_v² + (c^w)²x_w²] = κ Σ_v x_v² = κ‖x‖²`,
  hence **`ρ(M) ≤ κ(z*)`**, `z* =` realized max single-edge product (`≤ c_max²`). The steps are the refined chord, then `2ab ≤ a²+b²`, then the normalization collapse. **No homogeneity, no vertex-transitivity** — it holds for the n̂-dependent rules that broke 0827. ✓
- **Stress test (mine):** `ρ(M) ≤ κ(z*)` checked over **120 arbitrary non-homogeneous weightings** (n̂-aligned concentration, heavy-tailed random, adjacent mutual-spike, near-degenerate two-edge) — **0 violations**. The tight construction (every vertex `c_max = 0.707` on a common edge label) sits at `ρ = 0.616 ≤ κ = 0.667`. ✓
- **Pointwise floor:** `p(v) ≥ 4 ⇒ Σc⁴ ≤ 1/4 ⇒ c_max ≤ (1/4)^{1/4} = 0.707 ⇒ z* ≤ 0.5 ⇒ κ ≤ 2/3`, **margin 33%**. The full table (`p*` = 1.5→12 gives `κ` = 0.745→0.646) reproduces. ✓

So the step 0922 flagged as "empirical, not yet proven" is **now a theorem**. The repair is cleaner than the thing it replaced.

## 2. Process note

0828 owns the 0827 error without hedging (including the self-criticism that the non-transitivity of the n̂-rule had been noted and then bypassed for the convenient matching numerics). That is the right response to a caught error, and it is the reason reading the artifact and stressing the load-bearing step — rather than the convenient one — is the standing discipline. No defensiveness, no re-assertion; a proof, not a bigger sample.

## 3. Where the closure now stands — two cleanly separated pieces

- **Piece 2 — the bound: CLOSED (proven).** Pointwise `c_max ≤ c* < 1` ⇒ `ρ(M) ≤ κ(c*²) < 1`, closed form, homogeneity-free, verified. The det-coset order parameter cannot condense for any normalized, **pointwise non-degenerate** local η.
- **Piece 1 — orientation ⇒ pointwise non-degeneracy of the *dynamical* η: the located residual.** That a genuine local handedness is non-degenerate at *every* vertex is definitional for "handedness field"; whether the substrate's dynamics *guarantees* the dynamical η is pointwise non-degenerate (rather than degenerating at the n̂-extremal vertices, where the counterexample lived) is the η-identity in its **final, narrowest form**. If that must be *derived* from the substrate rather than taken as definitional, this is the narrow door where the PCD layer re-enters.

**This is genuine progress, and the door to outcome 2 is now narrow but honest.** Crucially, the open item is no longer a *hidden math gap* (which is what drew the 0827 RESTATE) — it is a *single, explicitly named physical conditionality*. That changes what a re-fire is adjudicating.

## 4. Re-fire is now warranted — framing

Re-fire CAPACITY-1 with C1 amended as follows:

- **Admissibility, stated pointwise:** *normalized, **pointwise non-degenerate** — `p(v) ≥ 4` at every vertex (equivalently `c_max(v) ≤ (1/4)^{1/4}`), as required for a local 4-D enantiomorph at each vertex.*
- **Closed-form bound:** under that condition, `ρ(M) ≤ κ(z*) ≤ 2/3 < 1` (refined-chord quadratic form, 0828; margin 33%), **no homogeneity assumed**. This pre-empts the n̂-concentration reconstruction a sharp reviewer would build against any *mean*-floor claim.
- **The one thing reviewers should adjudicate (piece 1), surfaced plainly:** the theorem is conditional on the dynamical η being pointwise non-degenerate — a sub-condition of Mechanism A, on the same footing as per-edge independence (0920). The honest question for the panel is *whether pointwise non-degeneracy is acceptable as a Mechanism-A conditionality* (a scope judgment), **not** whether there is an unflagged falsifier (there is not — the math is closed).

A RESTATE this time would therefore be a scope/conditionality judgment, not a broken proof. That is the correct posture for a conditional status theorem, and it is the form ChatGPT explicitly said he would CONFIRM ("state an effective-participation condition") — now pointwise and backed by a theorem rather than an assertion.

## 5. Recommendation

1. **Build the re-fire C1 package** with the pointwise admissibility condition + κ-bound + piece-1 surfaced (chirality lane).
2. **Bank Path B in parallel** — the explicit narrowed theorem over the equal-weight / bounded-pointwise-concentration class — as free insurance; it passes now and gives the airtight minimal version alongside the (conditional) universal one.
3. Verdict enactment stays gated on a re-fired **3/3**; nothing here moves it.

## Scope held

Chirality-lane review/adoption. **No verdict moved, no THEO registered, no CHIR.md edit, no count change.** CAPACITY-1 reserved; OPEN-CHIR-1d-β OPEN. The weight-concentration falsifier's **math is closed** (0828, verified); the live residual is now the single physical conditionality "the dynamical η is pointwise non-degenerate," carried under Mechanism A. Conditional on Mechanism A (OPEN-FP-F1-2).
