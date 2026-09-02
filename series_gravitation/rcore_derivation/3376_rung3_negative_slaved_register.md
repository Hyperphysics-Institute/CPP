# OPEN-GR-ROT-1 rung 3 — NEGATIVE: two skin models rejected in code; the register is SLAVED, and rung 3 is a static-nonlinear boundary condition, not a dynamical peel

**Patch 3376, Session 161, 2 Sep 2026.** Verify `code/3376_peeling_contact_reflection_verify.py` (12/12 — the checks assert the *failures*). Reasoning `reasoning/3376.md`.

**Standing:** no value of the O(kd) correction is claimed. GR-2 caveat (a) stays "bounded, uncomputed." What 3375 established (both limits; the mirror as δ → 0) stands. What 3375 got wrong in *language* — "a register peeled off a ceiling it is pressed against" — is corrected: the register has no inertia and nothing presses it; it is slaved to the demand.

## §1 Two models, two physics errors

| Model | Formulation | Result | Why it is wrong |
|---|---|---|---|
| **F (force)** | excess `e(x)` as a body force toward the cap; cap as a stiff lossless one-sided spring; leapfrog | reflected/incident flux **1.18** at kd = 0.03, 1.04 at kd = 1 — energy created | The register is a *computed* quantity with no inertia. A body force on an inertial string is not a model of it. |
| **T (threshold)** | `w = min(v + e, 0)` applied as a projection each step; `v` the free-propagated field | lossless; \|R\| = 0.9999, phase 177.76° — **identical for kd = 0.03, 0.3, 1** | The per-step recovery `w → min(w + e, 0)` closes a peeled deviation in `\|w₀\| dt/e` → 0 as dt → 0. The scheme has no parameter left to carry kd. It computes the Dirichlet limit, for every amplitude, and nothing else. |

Both calibrated against a hard Dirichlet wall (|R| = 1.0004, phase 179.56°, flux 1.0000).

## §2 What the second failure says about the physics

Model T's recovery rate is `e` per *step*; physically it is `e` per **Moment** (t_P). For any macroscopic wave the Moment is instantaneous. So the register in the skin does not *evolve*: at each Moment it is simply

    w(x) = min( e(x) + δD(x), 0 ),

the arriving demand deviation, attenuated by the local excess, clipped at the cap — **slaved** to the demand. Where `w = 0` (pinned) the GP re-emits no deviation: opaque. Where `w < 0` it re-emits *less* deviation than it received (by `e(x)`): a refusing, position-dependent attenuator. The "peel" of 3375 is not a contact line with dynamics; it is the set of GPs where `δD < −e(x)` at that Moment.

Rung 3 is therefore a **static-nonlinear boundary condition** on the exterior wave: at the surface, per half-cycle, the exterior field meets a layer whose re-emission is `min(e + δD, 0)`. Its linear limit is Dirichlet at the surface (3375). Its O(kd) correction is the reflection phase of a thin layer with linearly-rising refusal — a one-dimensional nonlinear scattering problem in the demand variable, solvable half-cycle by half-cycle (the compression half sees Dirichlet at 0; the rarefaction half sees the attenuator), **not** by a leapfrog with a projection.

## §3 Sequencing (PD-006)

I have spent one patch on two wrong schemes. The right formulation is now written down and it is not a finite-difference problem. Rather than guess a third scheme, the formulation goes to the panel as **CONV-039 Q-numerical** — a seat with numerical-methods depth is asked for the scattering solution or its small-kd expansion — bundled with the ℓ = 2 spherical rung (which does not depend on the O(kd) term, since it is computed at the Dirichlet limit) so the round carries physics and not only a method request. Until then: the flagship stands at the Dirichlet limit with the correction bounded as at 3375.

## §4 What stands after this patch

- 3375 theorem (interior at cap) — stands.
- Law (D) limits — stand: compression exact Dirichlet; rarefaction in [Dirichlet at 0, Dirichlet at d].
- The mirror as the δ → 0 limit — stands, with a derivation.
- 3375's "pressed against a ceiling" *language* — withdrawn; replaced by "slaved to the demand, attenuated by the excess."
- The O(kd) number — owed; owner: CONV-039.
