# G3 — the Λ-residual normalization derived from the equation's own λ (Patch 2314, 7 July 2026)

**Campaign:** `gate1_b1_campaign.md` claim G3. **Charge (DeepSeek red-team SCRATCH, adjudicated
2311):** "the 1/8π rides on the c05/c07 field-energy normalization; the reduction must DERIVE that
normalization, not import it." **Verify:** `code/2314_g3_lambda_normalization.py` (6/6 PASS, exact
sympy throughout). **No resting paper touched.**

## Verdict up front

**G3 DISCHARGED-with-disclosure. No correction to any registered number.** The 1/8π in
ρ_Λ = c⁴/(8πG L²) is **forced by the A3′-derived λ = 16πG/c⁴** through a two-step chain with no
c05/c07 import anywhere:

1. **λ → Poisson.** The derived equation's weak-field statics (h̄₀₀ = 4Φ/c², □h̄_μν = −λT_μν,
   T₀₀ = ρc²) force ∇²Φ = 4πGρ — the 4πG is λc⁴/4, nothing inserted. (Statics protected by
   THEO-SR-EIN-2; recomputed symbolically at 2314.)
2. **Poisson + the operational ledger → the coefficient.** Under THEO-SR-EIN-4 (C5 is the *only*
   field↔matter coupling; energy = work by the assembled metric — the unique ledger-balancing
   bookkeeping, DG-3-ratified), the field-energy assignment is the assembly work:
   W = ½∫ρΦ dV = −(1/8πG)∫|∇Φ|² dV, the second equality by Poisson + parts. **General identity
   (verified): ∇²Φ = κρ ⇒ energy coefficient = 1/(2κ); κ = 4πG ⇒ 1/(8πG).** A different λ would
   move the coefficient proportionally — the 1/8π is not adjustable independently of the ratified
   field equation. Exact concrete check: uniform sphere, both routes give W = −3GM²/5R identically.

So DM-2 §5's sentence "both the (l_P/L)² scaling and the 1/8π coefficient are derived, not
inserted" is **upgraded from resting-on-c05/c07 to traceable-to-λ** — DeepSeek's specific charge is
discharged, and the pedigree is now: λ (registered 1130, zero new parameters) → 4πG → 1/8π.

## The honest residual (disclosure-level; already inside the paper's stated band)

What is **not** derived: the O(1) mode-convention factors in applying the static normalization to a
coherent *mode* — time-averaging (1 vs ½), the kinetic term (gradient-only vs equipartition ×2),
and the wavenumber convention (k = 1/L vs 2π/L, ×4π²). Enumerated span: **½ to 8π² ≈ 79** around
the paper's amplitude-level point (= 1). The observed/CPP magnitude ratio (~2.07) sits comfortably
inside this span, as does the Li-dynamics coefficient c ≈ 0.8. Two consequences, both already
consistent with the paper's own disclosures ("factor ~2"; the scale L tagged CONJECTURED):

- The **scaling** (l_P/L)² and the **static normalization** 1/8π are derived; the residual
  **O(1) precision is convention-limited** and must not be over-claimed. Wording note entered in
  the deposit errata queue (non-blocking): §5 may add "(static-normalization level; O(1)
  mode-convention factors disclosed, span ~½–8π²)".
- The famous non-localizability of gravitational field energy (pseudotensor ambiguity) is handled
  by the *operational* definition: under THEO-SR-EIN-4 the assembly-work ledger is the unique
  bookkeeping consistent with C5-only coupling — the assignment is registered, not aesthetic.

## Release coupling

Per the campaign's pre-stated rule: G3 was errata-level unless structural. Outcome: no structural
error, no numeric correction; SCRATCH discharged with a wording-level disclosure queued.
Not release-blocking. Ledger updated; next per cheap-kill order: **G2** (EP at Eötvös precision).
