# H-NESS Lift, Steps 1–2: η on the 600-Cell, and the Symmetric χ_η (finite-vs-critical, settled)

**Patch:** 0813 (Session 156, 8 June 2026) · **Work item:** F.1 §14.17 / H-NESS lift, build steps 1–2
**Lane:** F.1 / `dynamical_substrate_law/` (lift = shared infrastructure; the chirality verdict stays review-gated).
**Predecessor:** lift scoping go/no-go (0812).
**Verify:** `code/0813_eta_symmetric_chi.py` (600-cell build; η; symmetric χ; robustness sweep).
**Type:** infrastructure computation. The chirality **verdict is not moved here** (DG-3); its implication is handed to the chirality review.

---

## Step 1 — η on the 600-cell

Built the 600-cell explicitly: the 120 unit-quaternion vertices (8 of `(±1,0,0,0)`, 16 of `(±½)⁴`, 96 even-permutations of `(0,±½,±1/2φ,±φ/2)`), nearest-neighbour adjacency at edge length `1/φ`, every vertex of degree 12 (the icosahedral vertex figure). Verified.

The local enantiomorph indicator: with a generic axis `n̂` (no projection ties), each vertex selects its 4 highest-`n̂`-projection neighbours (a canonical frame), and `η_v = sign det[ neighbour-direction vectors ]` — a **local ℤ₂-valued pseudoscalar**. Checks: `η_v` depends only on the closed neighbourhood `N[v]`; its homogeneous mean is `⟨η⟩ ≈ 0` (consistent with the bare 600-cell's achirality — H₄ contains reflections, so no net handedness in the unperturbed polytope); and it **flips sign under a global reflection** — the expected enantiomorph-label behaviour.

(η here is a defensible *proxy* local pseudoscalar, not necessarily the precise chirality-lane H₄/H₄⁺ representation-theoretic object. The step-2 result is robust to the exact local form — see below — but the chirality review must confirm the real η is local.)

## Step 2 — the symmetric χ_η in the product base: **FINITE & POSITIVE**

The symmetric base is the product (ZRP-template) measure: i.i.d. fluctuations across vertices, zero correlation length. Computed the connected susceptibility `χ_η = Σ_w ⟨η_v η_w⟩_c` by Monte Carlo:

- **By graph distance:** `⟨η_v η_w⟩_c` is `≈ 1` at `d=0` (the on-site variance) and **at noise level (~10⁻⁴) for all `d ≥ 1`.** The product base produces no inter-site connected correlation.
- **χ_η = 1.00** (per site), with `χ` restricted to `d ≤ 2` already equal to the full sum — finite support.
- **Robustness:** across perturbation strengths `σ ∈ {0.15, 0.25, 0.40}`, `χ_η ∈ [0.87, 1.01]`, on-site variance `≈ 1`, inter-site connected sum `→ 0`. Finite and `O(1)` throughout.

So the symmetric susceptibility is **finite and positive — off-critical.** The structural reason is clean and robust to the exact η: a **local** observable convolved with a **zero-correlation-length (product)** measure has finite-support connected correlations, hence finite χ. Divergence (criticality) would require a *correlated, non-product* symmetric base; the n_s-arc ZRP base (0772–0775) is product, so finite χ is the structurally-expected outcome, now confirmed numerically.

## What this settles — and what stays in the review lane

The finite-vs-critical fork was the cheapest decisive sub-result, and it came out **finite**. Per the scoping framework (0694 §4, `χ_η⁻¹ = 2μ²`):

- **Chirality (implication handed to the review, DG-3 — not asserted here).** A finite-positive symmetric χ_η means `χ_η⁻¹ = 2μ² > 0`, i.e. **μ² > 0 → η = 0 stable → no chiral vacuum → V3 stands by principle** (chirality emergent at the engine level, not merely at determination). Because the symmetric part is **non-marginal**, the O(δ³) current (step 3) can only *perturb* μ², not flip its sign — so V3 is not at risk from the current. This would close the deep chirality engine question favorably. **That verdict move belongs to the chirality lane's swarm review; this patch only supplies the infrastructure computation and its implication.**
- **DM-2 (mine).** No criticality in the symmetric base, plus the symmetric measure carrying no skew (0810), confirms **clean horizon-only Λ on the favorable branch.** The O(δ³) current's possible skew contribution is the separate, divergence-free residual that 0810 already isolated and bounded.

So both sectors land favorably from one computation, as the scoping pass anticipated.

## Step 3 status

Step 3 (the O(δ³) current correction) is **no longer sign-determining** for chirality, because step 2 came out finite/non-marginal — the symmetric part sets μ²>0 and the current only perturbs it. Step 3 remains worth running to *quantify* the perturbation and to read DM-2's residual skew explicitly, but it cannot change the favorable conclusion of either sector. It is a refinement, not a gate.

## Honest hedges (the result is conditional)

1. **η is a proxy.** The precise chirality-lane η (H₄/H₄⁺ coset field) must be confirmed local; the finiteness is robust to the exact local form, but "local" itself must hold for the real η.
2. **Product-base inheritance.** That the η-*correlator* inherits the n_s ZRP product (off-critical) structure is assumed from the template; the real lift must confirm the η-field — not just the occupation — is off-critical.
3. **Mechanism A.** The whole route is conditional on OPEN-FP-F1-2 (Mechanism A is a framework axiom, not yet derived from A1–A11).
4. **No verdict moved.** The chirality V3→V1 question is the review's to adjudicate; this is infrastructure plus a flagged implication.

## Scope held

No chirality verdict moved (V3/W3 stand; DG-3 respected). No THEO, no ID minted, no reserved-ID consumed. No CHIR.md / chirality_derivations / predictions / theorem-registry edits. CONJ-COSMO-1 unchanged. The DM-2 favorable-branch read is recorded; the chirality implication is handed to the review. Conditional on Mechanism A throughout.
