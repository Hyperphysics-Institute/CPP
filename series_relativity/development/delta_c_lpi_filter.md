# Brick #4 follow-up: the Δc / LPI filter — does density-dependent c_eff survive the data?

*Patch 0739, Session 154. The cheap falsifier flagged in Brick #4 (0738) — run first because it
could sink the most work for the least effort. Filter + verify:
`series_phenomena/cosmology/early_universe/scripts/0739_delta_c_filter.py`. NO THEO (filter / bound
check). Result: the construction is NOT falsified, and the danger collapses to a single decidable
structural question about the DP Sea.*

## The question

Branch V makes c_eff = l_P_eff/t_P depend on local absolute SSV (qDP density, polarization, DP-Sea
state). So c_eff differs between galactic and intergalactic space. Is that ruled out by the observed
near-constancy of fundamental constants?

## The key physics (why this is a fork, not a yes/no)

A position-dependent c that is fully absorbed into the **metric** just reproduces gravity (GR) — it is
not constrained; it is exactly what CPP's c07 weak-field derivation already does (gravitational time
dilation *is* a position-dependent rate). What the data bound is variation of the **dimensionless**
constant α = e²/(4πε₀ℏc). In CPP the DP Sea *is* the electromagnetic medium, so c_eff = 1/√(με) and
α ∝ √(μ/ε) (the medium impedance). To first order, with d_μ, d_ε the fractional DP-Sea responses of
μ, ε to an SSV change:

- Δc/c ≈ −½(d_μ + d_ε)  — the **product** με sets c;
- Δα/α ≈ +½(d_μ − d_ε)  — the **ratio** μ/ε sets α.

Define the response **asymmetry** A = (d_μ − d_ε)/(d_μ + d_ε). Then Δα/α = −A·Δc/c, and since the
metric part Δc/c tracks the gravitational potential ΔΦ/c², the LPI coupling is **k_α = A**. The entire
danger is governed by one number.

## Observational inputs (searched, 2026)

- **Spatial α dipole** (Webb/King/Murphy, VLT+Keck): amplitude few×10⁻⁶ across cosmological
  distances, ~4σ, still debated/systematics-limited.
- **α vs gravitational potential, white dwarf G191-B2B** (Berengut, Flambaum, Ong, Webb, Barrow,
  Barstow, Preval, Holberg 2013): Δα/α = (4.2±1.6)×10⁻⁵ at ΔΦ ≈ 5×10⁻⁵ ⇒ k_α ≈ 0.8±0.3 — a **weak**
  bound, |k_α| ≲ 1.
- **Atomic-clock LPI** (Sr/Dy/Rb–Cs comparisons over Earth's orbit): the **tight** bound,
  |k_α| ≲ 10⁻⁶.

## The fork (filter output)

| asymmetry A = k_α | vs clock bound 10⁻⁶ | verdict |
|---|---|---|
| 0 | — | SAFE: pure metric = gravity = c07/GR |
| 10⁻⁹…10⁻⁶ | ≤ 1× | PASS (within clock LPI) |
| 10⁻³ | ×10³ | FAIL |
| O(1) | ×10⁶ | FAIL by ~6 orders |

So **Branch V is safe iff the DP-Sea response to SSV is μ↔ε symmetric to ~1 part in 10⁶**:
- **Symmetric (A ≲ 10⁻⁶):** c varies, α fixed. The galactic/intergalactic c difference is purely
  gravitational — real but not novel and not dangerous. Survives every bound.
- **Asymmetric (A ~ O(1)):** α tracks the potential as strongly as c → k_α ~ 1 → falsified by ~6
  orders vs the clock bound.

## What is already known (the partial answer)

The **gravitational** SSV channel must already be near-symmetric: c07 reproduces gravitational time
dilation while LPI holds to k_α ≲ 10⁻⁶, so the gravity-driven part of the DP-Sea response has
A_grav ≲ 10⁻⁶ — observationally forced. That means half the worry is already retired. The **only**
open question is the **composition channel**: does changing qDP *density* (not potential) also move μ
and ε symmetrically? If the DP-Sea structure makes SSV couple to μ and ε by the same mechanism (so
density and potential both act through the symmetric mode), A stays ≲ 10⁻⁶ and the picture survives.

## Verdict

**The construction is not falsified.** The filter did its job: it converted a vague worry ("is a
varying c ruled out?") into one sharp, decidable, first-principles question —

> *Does an SSV change move the DP-Sea μ and ε symmetrically (in particular through the qDP-density /
> composition channel)?*

— with a clear pass condition (symmetric ⇒ c-variation is just gravity, α fixed) and a clear fail
mode (O(1) asymmetric ⇒ dead by 10⁶). The gravity channel is already known symmetric; the composition
channel is the next target and is decidable from the four-DP-species structure and how SSV polarizes
them.

## Debts updated

- Δc bound: **retired as a gross falsifier**; reduced to the μ↔ε symmetry question (now the live
  first-principles target, alongside the superposition-thinning roll-off law from 0738).
- The symmetry question is *constructive*: if the DP-Sea response is provably symmetric, it
  simultaneously (a) keeps α fixed, (b) confirms c07's gravity as the symmetric mode, and (c) makes
  the density-dependent c_eff a clean gravitational statement.

## Pointers

- From: `brick4_branch_v_adoption_and_toy_spec.md` (0738) debts ledger.
- Filter + verify: `series_phenomena/cosmology/early_universe/scripts/0739_delta_c_filter.py`.
- Reasoning: `series_relativity/development/reasoning/0739_delta_c_filter.md`.
- Next first-principles targets: (1) DP-Sea μ↔ε symmetry of the SSV/composition response (this filter);
  (2) superposition-thinning roll-off law (0738, upgrades n_s tuning→prediction).
