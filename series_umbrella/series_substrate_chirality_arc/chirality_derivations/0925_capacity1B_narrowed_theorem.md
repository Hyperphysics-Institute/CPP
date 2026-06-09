# Path B — THEO-CHIR-CAPACITY-1B (narrowed): no det-coset condensation over the pointwise-non-degenerate η class

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/0925_capacity1B_narrowed_theorem.md`
**Patch:** 0925 · **Type:** banked fallback theorem draft (the airtight minimal version of CAPACITY-1). **Status:** DRAFT, not registered, not enacted. **Relation:** the unconditional-on-piece-1 sibling of the Path-A re-fire (0924). They are not exclusive.

---

## Why this exists

The Path-A re-fire (0924) claims chirality is a primitive (V3), **conditional on the dynamical η being pointwise non-degenerate** (piece 1). If the swarm accepts that conditionality (Q5), Path A is the stronger headline and this draft stays in reserve. If a reviewer declines to grant piece 1 as a Mechanism-A sub-condition but finds **no Q1 falsifier**, this narrowed theorem is what we register instead: it makes the *scope* explicit rather than asserting it, so it carries **no piece-1 dependence**. Its cost is a weaker headline; its benefit is that it is airtight today.

## THEO-CHIR-CAPACITY-1B (narrowed, proposed)

*Over the class of normalized, **pointwise non-degenerate** CHI-1-confined local handedness observables — i.e. order parameters `η_v = sign(Σ_{e∈R_v} w_e x_e)` with `p(v) ≥ 4` at every vertex (equivalently `c_max(v) ≤ (1/4)^{1/4}`) — the det-coset order parameter does not condense, at the physical bias `δ = φ⁻³`, conditional on Mechanism A. Equivalently: **within the pointwise-non-degenerate class, spontaneous breaking of the global det-coset ℤ₂ (uniform or staggered) is excluded.***

What this **does** establish: *if* the dynamical η is pointwise non-degenerate, chirality cannot be emergent-by-condensation — so emergence (V1) would require a degenerate (single-edge-collapsing) dynamical η. What this **does not** claim: it does **not** assert the dynamical η is in the class; hence it does not, on its own, certify FI-C-9 as a primitive "full stop." That extra step is exactly the piece-1 conditionality carried by Path A.

## Proof (three parts, all independently reviewed-or-verified)

1. **No condensation in the class (the bound).** On the per-edge-independent Mechanism-A measure the connected η-coupling is nearest-neighbour only (0826), `M_vw = (2/π)arcsin(c^v_{(v,w)} c^w_{(v,w)})`, per-vertex normalized. Since `g(z)=(2/π)arcsin(z)/z` is increasing, the refined-chord quadratic-form bound (0828) gives `ρ(M) ≤ κ(z*) = (2/π)arcsin(z*)/z*` with `z* = ` max single-edge product `≤ c_max²`. Pointwise non-degeneracy `p(v) ≥ 4 ⇒ c_max ≤ (1/4)^{1/4} ⇒ z* ≤ 1/2 ⇒ ρ(M) ≤ 2/3 < 1` — **margin 33%, no homogeneity assumed.** `ρ(M) < 1` bounds `|λ|` for both the most-positive (uniform/FM) and most-negative (staggered/AFM) eigenmodes, so **both ℤ₂-breaking channels are excluded by the one bound.** *(Verified: 120 adversarial non-homogeneous weightings, 0 violations; tight construction ρ = 0.616.)*
2. **The non-equilibrium current is inert (C2, 0822).** NESS current `~δ^{3.09}`, `J≈3×10⁻⁵` at `δ=φ⁻³`, divergence-free, T-odd; couples to T-even η-ordering only at `O(J²)≈2×10⁻⁴`. No threshold shift, no current-driven ordering at the physical bias.
3. **Coupling below both thresholds (C3, 0823–0825).** `|K_lift|≈0.053 < K_c^{uniform}≈0.095` and `< K_c^{staggered}≈0.27`; consistent with the spectral bound (1).

## Scope and conditionalities

- Conditional on **Mechanism A** (OPEN-FP-F1-2) and per-edge independence of its measure (proof part 1). **Not** conditional on piece 1 — non-degeneracy is the explicit *domain of quantification*, not an assertion about the substrate's η.
- At the physical bias `δ = φ⁻³` (C2/C3 scope).
- Status result over a restricted class; **not** a derivation of chirality. Temporal axis and OPEN-SM-4 untouched. Bridge-side cap (BRIDGE-1) inherited where applicable.

## Disposition

Banked, **not registered**. Decision rule after the 0924 swarm:
- **Q5 conditionality accepted + 3/3** → register **Path A** (CAPACITY-1, V3 confirmed / V1 excluded, conditional on Mechanism A incl. pointwise non-degeneracy). 1B stays in reserve as the minimal statement.
- **No Q1 falsifier but Q5 conditionality declined** → register **1B** (this theorem) as the certified result; leave the primitive-"full-stop" claim open pending a substrate-level derivation that the dynamical η is pointwise non-degenerate (the located PCD residual).
- **Any Q1 falsifier** → neither registers; back to F.1.

## Scope held

Draft only. **No verdict moved, no THEO registered, no CHIR.md edit, no count change.** CAPACITY-1 / 1B both reserved. Conditional on Mechanism A.
