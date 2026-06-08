# §14.17 / H-NESS Lift — Scoping and Go/No-Go (the triple-shared gate)

**Patch:** 0812 (Session 156, 8 June 2026) · **Work item:** F.1 §14.17 effective action → the H-NESS lift
**Lane:** F.1 / `dynamical_substrate_law/` (disjoint from CHIR.md and `sea_gravitation/`).
**Predecessor:** chirality determination closure (0903); the NESS construction + H-NESS gap (0694); DM-2 Steps 0–2b (0802–0810).
**Verify:** `code/0812_hness_lift_scope.py` (lift constructible; finite-vs-critical fork computable).
**Type:** scoping/feasibility (NOT a derivation, NOT a verdict). Analogue of DM-2 Step 0.

---

## Why this node, now

The chirality determination closure (0903) collapsed the remaining chirality frontier onto the exact object DM-2 bottomed out on. Three threads share one gate:

- **Chirality μ²-sign** (V3→V1, spatial engine) — the η-susceptibility *sign*.
- **Chirality temporal** (W3→W1) — the same effective action.
- **DM-2 Λ-cleanliness** (0809–0810) — the *third moment* of the same lifted measure.

§14.17 is a **programme-level target** (Patch 0528 §14.17), not a section sitting in the F.1 paper. The concrete, already-reduced gate is the **H-NESS lift** (0694): the single-walker Mechanism-A NESS measure π is *built* (120-state, current at O(δ³), tilt at O(δ¹)); the residual is to **lift π to the η-field measure (or justify the single-site reduction), then read one correlator.** Building it once feeds all three threads — the highest-leverage target in the program.

## The two lift routes — and why they converge

The H-NESS gap names two routes (0694 §5). They are not independent:

- **Route (i) — occupation/field lift.** Promote Mechanism A to a many-walker / occupation-field process whose stationary measure is a measure over η-configurations. If the walkers are non-interacting, the stationary measure **factorizes into a product** (the connected correlator between distinct sites vanishes), and field correlators reduce to single-site quantities.
- **Route (ii) — single-site / mean-field reduction.** Assume the single-walker π's η-moments equal the field's. This is exactly **justified, not merely assumed, to the extent the lift is a product measure** — for a product base the single-site marginal carries the moments exactly.

So the two routes converge: **a product-measure base makes the single-site reduction exact for the symmetric part**, and the only place they can diverge is the correlated (non-product) piece — the O(δ³) current.

## The cross-arc connection (the reason this is tractable)

The n_s / EU-1 arc (Patches 0772–0775) **already derived** the substrate occupation dynamics as a *symmetric, constant-rate zero-range process (ZRP) with a product-Poisson stationary measure* (zero correlation length). That is a derived template — possibly the literal object — for the **symmetric base** of the H-NESS lift. Three arcs (chirality, DM-2, n_s/EU-1) thus meet at one substrate occupation measure. The methodological payoff is concrete: in a product base the connected susceptibility `χ_η = Σ_w ⟨η_v η_w⟩_c` collapses to the **on-site variance — finite and positive**.

This is a structural observation offered to the build, **not** a proven identity: the n_s ZRP is an occupation measure, whereas η is the *enantiomorph label*. That the η-correlator inherits the product (off-critical) structure is precisely what the build must check.

## Minimal deliverable + the cheapest decisive computation

The go/no-go quantity (0694 §4, stage 3): **is the symmetric η-susceptibility FINITE or DIVERGENT?**

- **Finite (off-critical)** → `χ_η⁻¹ = 2μ² > 0` → chirality **V3 stands by principle** (emergent confirmed at the *engine* level) **and**, by the DM-2 current-vs-skew result (0810), the symmetric measure has no skew → DM-2 **clean horizon-only Λ**. *Both sectors resolve favorably from one computation.*
- **Divergent (critical)** → the symmetric part is marginal → the O(δ³) current becomes sign-determining → chirality may go V3→V1 and DM-2 may acquire a skew residual; even then 0810 keeps the DM skew a separate question from the chirality flip.

## Feasibility results (verify 0812)

- **CHECK A — the lift base is constructible.** On a small tilted ring: a conservative (gradient) tilt gives J ≈ 0 (detailed balance); a constant non-conservative bias gives J ≠ 0 (a genuine NESS). π is positive, normalized, computable in both cases. The method scales to the real 120-vertex 600-cell (where the current onset is O(δ³), a cycle-structure feature, 0689).
- **CHECK B — the fork is a well-posed, decidable quantity.** For a field with correlation length ξ, `χ` is finite off-critical and diverges only as ξ→∞: product base (ξ=0) → χ = 1 (finite); near-critical (ξ=10⁶) → χ ≈ 4×10⁴. The product (ZRP-template) base lands squarely in the finite-positive, favorable branch.

## Go/No-Go: **GO** (not a wall)

The lift is **tractable**: the base measure is computable; the decisive quantity (finite vs critical χ) is well-posed; and the n_s-arc ZRP product measure is a derived template for the symmetric base that puts the favorable branch within reach. This is a genuine reduction, not the full §14.17 effective action. The build, in order:

1. **Define η on the 600-cell** (stage 2 — the local enantiomorph indicator of a vertex's neighborhood frame; the field whose homogeneous value is the STATUS-2 H₄/H₄⁺ label). Bounded geometric/representation-theoretic task.
2. **Compute the symmetric χ_η in the product (ZRP-template) base** — settle finite-positive vs critical. *This is the cheapest decisive sub-result and moves both sectors.*
3. **Add the O(δ³) current correction** (the generalized fluctuation–response / frenetic term) — only sign-determining if step 2 comes out critical.
4. **Read off:** the DM-2 third moment (mine), and hand the **sign(μ²) → V3→V1 extraction to the chirality review** (DG-3 gated).

## Lane discipline

The **lift and its scoping are shared F.1 infrastructure** (this window, `dynamical_substrate_law/`) — not verdict-moving. The **sign(μ²) → V3→V1 extraction is verdict-moving and review-gated** (DG-3, chirality lane's swarm process); I build/scope the lift and read the DM third moment, but do not move the chirality verdict from this window. The n_s/ZRP reference is read-only.

## Scope held

No verdict moved (chirality V3/W3 and CONJ-COSMO-1 untouched). No THEO, no ID minted, no reserved-ID consumed. No CHIR.md / chirality_derivations / predictions / theorem-registry edits. The cross-arc ZRP connection is a scoping observation offered to the build, not a claim of identity. Conditional on Mechanism A (OPEN-FP-F1-2), as the whole route is.
