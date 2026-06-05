# The Debye √n̄ residual: real in the continuum, cut off before cosmological occupation

*Patch 0757, Session 154. Takes head-on the one threat that survives charge neutrality: a Debye–Hückel
excess chemical potential μ_excess ∝ −√n̄, which — being a power of n̄ — would dominate the ln n̄ that
carries the tilt at the cosmological occupation n̄ ~ 10⁷⁴. Analysis + numerics:
`series_phenomena/cosmology/early_universe/scripts/0757_debye_residual.py`. NO THEO. **Verdict: the √n̄ is
real for a continuum charge-neutral Coulomb plasma, but it is cut off below cosmological occupation by
(i) the Debye-regime exit and (ii) the absence of sub-GP spatial structure for the on-GP stack. The
tilt-carrying ln n̄ survives, except in a narrow, checkable corner (absurdly weak long-range SSV).
Substantially de-risked; not fully closed.***

## Why neutrality is not enough, and why this is the real threat

The 0756 run showed charge neutrality cancels the **leading** mean-field, μ_excess ∝ (K−K_att)·n̄ → 0 at
K = K_att. But the Debye–Hückel correction is the **next** order: for a charge-neutral Coulomb plasma,
μ_excess/kT = −½·(q²κ/kT) with the inverse Debye length κ² ∝ n q²/kT, so μ_excess ∝ −√n. Neutrality does
**not** remove it. And at the cosmological pivot n̄ ~ 10⁷⁴:

  ln n̄ ≈ 170,  √n̄ ≈ 10³⁷,  n̄^{1/3} ≈ 5×10²⁴.

**Any** surviving power of n̄ beats ln n̄ by ≥ 35 orders. So the tilt survives only if the power residual is
*absent* at cosmological occupation. That is the question.

## Three reasons the √n̄ does not reach n̄ ~ 10⁷⁴

**1. Debye–Hückel is weak-coupling only, and cuts off far below 10⁷⁴.** The √n law requires a
well-populated Debye sphere, N_D = (4π/3)·n·λ_D³ ≫ 1. Since λ_D ∝ n^{−1/2}, N_D ∝ (kT/q²)^{3/2}·n^{−1/2} —
it *decreases* with n. DH (hence the √n law) holds only for n < n_* with **n_* ~ (kT/q²)³** (lattice
units). Above n_*, λ_D drops below the interparticle spacing, no screening cloud forms, DH is invalid, and
the √n law simply does not apply. Numerically, n_* reaches 10⁷⁴ only if **kT/q² ≳ 10²⁴·⁷** — i.e. the SSV
coupling q² would have to be ~25 orders of magnitude below kT. For any appreciable SSV coupling the Debye
regime is exited far below cosmological occupation, and the √n never gets there.

**2. The on-GP stack has no spatial substrate for a screening cloud.** The √n is a 3D
spatial-charge-correlation effect (screening clouds over space). By A1 a CP's position *is* the GP;
co-located CPs in a stack share **one** lattice position with no sub-GP coordinates. There is no space
within a stack over which a screening cloud could form, so the on-GP stack interaction is necessarily
**on-site/contact** — and a charge-balanced on-site interaction cancels with *no* power residual.
Confirmed numerically: the balanced on-site μ_excess fit over λ ∈ {5,10,20,40,80} gives slope vs √n =
−0.002 (≈ 0, no Debye term) and slope vs n = −0.0001 (≈ 0, mean-field cancelled) — only the ideal ln n
survives.

**3. Strong coupling doesn't rescue the residual either.** Above n_* the plasma is strongly coupled, where
the excess would scale as the Madelung ∝ −n^{1/3} — but that requires a regular spatial *lattice* of the
charges (spacing ∝ n^{−1/3}), which again does not exist for CPs pinned to a single GP point. So neither
the weak-coupling √n nor the strong-coupling n^{1/3} has a spatial substrate in the point-stack.

## Verdict

- The √n̄ residual is **real** for a continuum charge-neutral Coulomb plasma and would sink the tilt — so
  the worry was correct and neutrality alone is *not* sufficient.
- But it **does not survive to cosmological occupation** in the CPP setting: the Debye regime is exited at
  n_* ~ (kT/q²)³ ≪ 10⁷⁴ for any appreciable coupling, and the on-GP stack has no spatial structure to
  support either a Debye screening cloud (√n) or a Madelung lattice (n^{1/3}). What remains is the on-site
  combinatorial ln n̄ (the tilt), with the ∝ n̄ mean-field cancelled by neutrality.
- **The only escape for the residual** is long-range *inter-GP* SSV with an absurdly weak coupling
  (kT/q² ≳ 10²⁴·⁷, so n_* ≳ 10⁷⁴). That is a sharp, falsifiable knife-edge — not a generic killer.

## Honest caveats (what this does and does not close)

- O(1) prefactors are dropped; the crossover n_* ~ (kT/q²)³ is an order-of-magnitude statement, which is
  all that is needed against the 35-order gap, but the real SSV coupling value must be plugged in.
- The on-GP point-stack argument (reason 2) is the strongest leg and rests on A1 (no sub-GP position). The
  inter-GP long-range case (reason 1) is argued via the Debye crossover, **not** simulated with a real
  lattice Coulomb; that inter-GP lattice-plasma calculation, with the actual SSV range, is the remaining
  check.
- A genuinely long-range SSV could couple the stack to the surrounding plasma; whether that re-introduces
  a surviving residual reduces to the same crossover condition (n_* vs 10⁷⁴) and is checkable once the SSV
  range is fixed.

## Status

- The √n̄ residual — "the one thing that could still sink it even under neutrality" — is **de-risked**: it
  is confined to a narrow, checkable corner (absurdly weak long-range coupling), and is absent for the
  on-GP stack by A1.
- n_s = 0.9649 stays a zero-NEW-axiom prediction conditional on: (a) the bath (toy-supported, 0756);
  (b) charge neutrality (0756); (c) the SSV coupling not being absurdly weak / the interaction being
  effectively on-site for the stack (this patch). All three are falsifiable.
- Remaining physics check: the **real SSV interaction range** + an inter-GP lattice-plasma chemical-
  potential calculation. Worth adding to the swarm request.

## Pointers

- Analysis/numerics: `.../scripts/0757_debye_residual.py`. Builds on 0756 (neutrality requirement).
- Reasoning: `.../reasoning/0757_debye_residual.md`.
