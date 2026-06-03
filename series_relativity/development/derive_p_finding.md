# Brick #4 follow-up: deriving p — the spectrum reduces to "smooth graceful exit vs cliff"

*Patch 0744, Session 154. The decisive attempt to derive p (in n_s = 1 − p/N_*) from the substrate and
turn n_s into a genuine prediction. Toy + verify:
`series_phenomena/cosmology/early_universe/scripts/0744_derive_p.py`. NO THEO. **Result, reported
straight: p does NOT cleanly derive to 2. The literal H-axiom gives the excluded n_s = 1; the data
value p = 2 corresponds to a smooth graceful exit (H_eff ∝ e-folds-remaining), which is plausible and
canonical but not derived. n_s = 0.965 is not yet a CPP prediction — but the open question is now a
single, physically natural fork.***

## The reduction (rigorous)

The δN formalism gives the curvature perturbation as the fluctuation in the number of e-folds,
ζ = δN = (1/3)(δn̄/n̄). Frozen at horizon crossing with dimensionless power P ~ H_eff², so

  n_s − 1 = d ln P/d ln k = **2 · d ln H_eff/dN**  (at crossing).

Therefore **p is fixed entirely by how the expansion rate H_eff depends on the superposition state** —
i.e. by what the boost rule does as the mean occupancy n̄(N) = n̄_init·e^{−3N} dilutes. This is a real
reduction: p is no longer a free parameter, it is a property of the boost rule, computable.

## What the substrate gives (toy, pivot at N_rem ≈ 57)

| boost-depth coupling | H_eff | n_s | verdict |
|---|---|---|---|
| **depth-independent** (per-GP: boost once if superposed, the *literal* axiom) | const (→ cliff in f) | **1.0000** | Harrison–Zel'dovich, **excluded ~8σ** |
| **log of occupancy** (H_eff ∝ ln n̄ ∝ N_rem) | smooth wind-down | **0.9649** | **matches Planck on the nose** |
| **linear** (per-CP: each stacked CP boosts) | ∝ n̄ | −5 | far too red, excluded |

## What this means (the honest fork)

The whole spectrum question collapses to **whether the graceful exit is a smooth wind-down or a cliff**:

- The **literal on/off axiom** ("a GP boosts its PSR once if superposed, regardless of stack depth")
  is depth-independent. H_eff stays constant while the superposed *fraction* f ≈ 1, then f cliffs in
  the final ~1 e-fold (the 0741 result). A cliff gives **zero tilt over observable scales → n_s = 1,
  excluded.** This is why 0741 failed, now understood structurally: the bare axiom is a cliff.

- The **per-CP** reading (boost scales with stack depth linearly) gives H_eff ∝ n̄ → wildly red,
  excluded.

- The **data value p = 2** (n_s = 1 − 2/N_* = 0.9649) corresponds to H_eff ∝ ln(n̄) ∝ N_rem: the
  expansion rate **winds down linearly with e-folds-remaining.** That is a *smooth* graceful exit, and
  it is exactly the **canonical slow-roll form** (the m²φ² value, n_s = 1 − 2/N). It tracks the mean
  stack **depth** ln n̄ (which declines smoothly as e^{−3N}) rather than the superposed **fraction** f
  (which cliffs).

So **n_s = 0.965 follows if and only if CPP's superposition depletion drives a smooth depth-tracking
wind-down of H_eff, rather than the literal fraction-based cliff.**

## Honest verdict

- **Not a clean prediction.** The bare on/off axiom (fraction-based, cliff) predicts the *excluded*
  n_s = 1. CPP does not currently derive the depth-logarithmic coupling that gives 0.965.
- **But the gap is now a single, physically natural condition**, not a free function or a free integer:
  *does H_eff track the smooth mean depth ln(n̄) ∝ e-folds-remaining (→ 0.9649, canonical slow-roll), or
  the cliffing fraction f (→ excluded n_s = 1)?*
- **Plausibly favorable, not proven.** Realistic graceful exits are smooth, not cliffs; the mean depth
  n̄ *does* decline smoothly throughout inflation (only the fraction f cliffs); and H_eff ∝ N_rem is the
  textbook slow-roll behavior that gives n_s = 1 − 2/N. So a depth-tracking H_eff is physically
  reasonable and lands *exactly* on Planck. But the bare axiom as written is fraction-based, and the
  depth-coupling is not derived — so honesty forbids calling 0.965 a prediction yet.

## What would close it (sharp, single computation)

Show, from the substrate dynamics, that the expansion rate H_eff tracks the **mean superposition depth
ln(n̄)** (smooth, ∝ e-folds-remaining) rather than the **superposed fraction f** (cliff). Equivalently:
that the per-tick boost compounds with stack depth such that H_eff winds down ∝ N_rem near the exit.
If it does, n_s = 1 − 2/N_* = 0.965 becomes a genuine zero-parameter CPP prediction (N_* already fixed
by the CP count) and the spectrum thread closes. If H_eff is genuinely fraction-based (cliff), CPP
predicts the excluded n_s = 1 and the tilt is a real vulnerability.

## Where the sector stands after this brick

- Gaussianity (CLT) — solid.
- Amplitude A_s — one tuning.
- Horizon — early high c_eff.
- Δc / LPI — survives, reduced to Z₀-geometric (0740).
- **Tilt n_s — reduced to one physically natural fork** (smooth depth-tracking exit → 0.965, vs
  fraction cliff → excluded 1). Plausibly favorable; the deciding computation is whether H_eff tracks
  depth or fraction. The CP-count-fixed N_* ≈ 60 means *if* the exit is smooth, the value is 0.965 with
  zero free parameters.

## Pointers

- Builds on 0741 (cliff = excluded n_s=1) and 0742 (n_s = 1 − p/N_*, N_* from CP count).
- Toy + verify: `.../early_universe/scripts/0744_derive_p.py`.
- Reasoning: `series_relativity/development/reasoning/0744_derive_p.md`.
- THE deciding computation: does H_eff track mean depth ln(n̄) (smooth, → 0.965) or fraction f
  (cliff, → excluded)? This is now the single gating question for the whole spectrum thread.
