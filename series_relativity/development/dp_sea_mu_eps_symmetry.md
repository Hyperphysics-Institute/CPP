# Brick #4 follow-up: the DP-Sea μ↔ε symmetry — α-variation IS impedance-variation

*Patch 0740, Session 154. Resolves the residual left by the Δc/LPI filter (0739): is the DP-Sea
response to SSV μ↔ε symmetric, so a density-dependent c_eff is purely gravitational and survives the
varying-constants bounds? Demonstrator + verify:
`series_phenomena/cosmology/early_universe/scripts/0740_mu_eps_impedance_symmetry.py`. NO THEO
(structural reduction + corpus-grounded argument, conditional on one registered computation).*

## The clean reduction

Two defining relations fix the DP-Sea μ₀ and ε₀:
- c = 1/√(μ₀ε₀) — the broadcast / null-trajectory speed (the **product**);
- Z₀ = √(μ₀/ε₀) — the impedance of free space (the **ratio**).

Solving: μ₀ = Z₀/c, ε₀ = 1/(Z₀c). Under an SSV step, writing dc, dZ for the fractional changes in
speed and impedance, and using α ∝ √(μ/ε):

- Δc/c = −½(d_μ + d_ε) = **dc**
- Δα/α = +½(d_μ − d_ε) = **dZ**  ← **α-variation = impedance-variation, exactly**
- A = (d_μ − d_ε)/(d_μ + d_ε) = **−dZ/dc**

(Algebra confirmed numerically in the script.) So the entire μ↔ε symmetry question collapses to **one
quantity: does the impedance Z₀ change under SSV?** Δα/α = Δ ln Z₀. If Z₀ is a fixed geometric constant
of the lattice, α is fixed (A = 0) and the c_eff variation is pure gravity; if Z₀ inherits the
SSV-variable stiffness, α tracks the potential and the picture is falsified.

## Why Z₀ is geometric (three corpus facts)

1. **B is the curl of the polarization pattern, not an independent susceptibility.** c06: the photon's
   magnetic component "arises from the curl of the propagating SSV pattern." So μ and ε are two views
   of one ZDC propagation, locked by the curl over the GP network — not two free knobs that could
   move oppositely.
2. **The GPs are fixed and eternal (Brick #2 / SR-1).** The curl/broadcast geometry that sets the
   E↔B locking — hence Z₀ — is a property of the *fixed* lattice. SSV changes the stiffness C and the
   reach c (so the product μ₀ε₀ = 1/c² moves, c varies), but it cannot change a fixed-lattice
   geometric ratio. Brick #2's eternal GPs are precisely what guarantees Z₀ is geometric.
3. **All four DP species participate equally** in ZDC formation (c06). There is no species-selective
   channel that could split the electric vs magnetic response with composition (qDP density), which
   is exactly the channel the 0739 filter flagged as the open one.

Together these say: SSV moves the **product** (c varies = gravity, the c07 metric effect) but not the
**ratio** (Z₀ geometric ⇒ α fixed ⇒ A = 0). The density-dependent c_eff, including its qDP-density /
composition part, is purely gravitational.

## The result, stated honestly

The symmetry residual reduces **exactly** to: *is Z₀ geometric?* — and Δα/α = Δ ln Z₀. The three
corpus facts all point to Z₀ = pure 600-cell geometry, hence A = 0, hence the construction SURVIVES.
This is **conditional on one explicit computation that CPP already has on its books**: c06's registered
future-work item, *"express μ₀ and ε₀ in terms of the 600-cell stiffness C and the shell-broadcast
speed c."* The sharp, falsifiable form:

> **Prediction / internal-consistency test:** when μ₀(C,c), ε₀(C,c) are derived, Z₀ = √(μ₀/ε₀) in
> lattice units must come out as a **pure 600-cell geometric constant, independent of the
> SSV-variable stiffness C.** If it does, the μ↔ε symmetry is proven, A = 0, and the Δc residual is
> CLOSED. If Z₀ instead carries C, then A ≠ 0 (k_α ~ 1, failing the clock LPI bound by ~6 orders) and
> the density-dependent-c picture must be revisited.

Experimental headroom: the clock LPI bound |Δα/α| ≲ 10⁻⁶ becomes |Δ ln Z₀| ≲ 10⁻⁶ — the impedance
must be geometric to ~1 ppm. The fixed-lattice structure delivers Z₀ exactly geometric (dZ = 0
structurally), comfortably inside that headroom.

## Why this is not make-work

The Z₀(C,c) derivation is needed independently by c06 for the photon emission envelope and natural
linewidth (Δν ∝ ν³, the Einstein-A consistency). So the same computation that closes the cosmology
Δc residual also advances the EM-substrate sector. One derivation, two payoffs.

## Debts updated

- μ↔ε symmetry: **reduced to a single registered computation** (Z₀ from C,c) with a clear pass
  condition (Z₀ = pure geometry) and a clear fail mode (Z₀ ∝ C). Strongly indicated to pass by the
  fixed-lattice structure; not yet proven.
- This is the natural point where the cosmology thread hands a concrete task to the EM sector (c06).
- Remaining Brick-#4 first-principles target: the superposition-thinning roll-off law (0738), which
  upgrades n_s from a tuning to a prediction. Independent of this thread.

## Pointers

- From: `delta_c_lpi_filter.md` (0739) residual.
- Demonstrator + verify: `.../early_universe/scripts/0740_mu_eps_impedance_symmetry.py`.
- Registered computation it reduces to: c06
  (`series_relativity/SR_companion_papers/c06_DP_chaining_as_mass_and_EM_substrate/`) future-work item
  on μ₀, ε₀ from stiffness C and speed c.
- Reasoning: `series_relativity/development/reasoning/0740_mu_eps_symmetry.md`.
- Ties to Brick #2 (fixed/eternal GPs ⇒ geometric Z₀).
