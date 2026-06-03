# Brick #4 follow-up: the roll-off law — a FOUND PROBLEM (simplest version predicts n_s = 1, excluded)

*Patch 0741, Session 154. The first-principles attempt to turn n_s from a tuning (Brick #4 / 0738)
into a prediction. Toy + verify: `series_phenomena/cosmology/early_universe/scripts/0741_rolloff_law.py`.
NO THEO. **This is a negative/tension result, reported straight: the simplest faithful roll-off
predicts the Harrison–Zel'dovich value n_s = 1, which Planck excludes at ~8σ.** n_s is not yet a CPP
prediction; the path to the observed tilt is identified but not delivered.*

## The first-principles roll-off (faithful to the H-axiom)

- **Engine.** The H-axiom boosts a GP's PSR_base by (1+H) each tick it is superposed (≥2 CPs),
  factor 1 otherwise. So the background expansion rate is the *fraction of GPs still superposed*:
  H_eff(N) = H₀·f(N).
- **Dilution.** Scale factor a = e^N, occupied-GP volume ~ a³, so mean occupancy dilutes as
  n̄(N) = n̄_init·e^{−3N}, with n̄_init = N_CP/N_GP_init = 10⁸⁰/13 ≈ 7.7×10⁷⁸.
- **Statistics.** Poisson occupancy ⇒ f(N) = 1 − e^{−n̄}(1 + n̄) (the fraction with ≥2 CPs).
- **Spectrum.** Each mode freezes at horizon crossing with amplitude ~ H_eff, so
  n_s − 1 = 2·d ln H_eff/dN = 2·d ln f/dN at crossing.

No tuning anywhere: every quantity is fixed by the H-axiom, the dilution, and Poisson statistics.

## The result

End of inflation (f = 0.5) lands at N_end ≈ 60.4 e-folds — consistent with Brick #4 Test C. But across
the **entire observable CMB window** (the ~7–8 e-folds of scales that crossed ~47–55 e-folds before the
end), the occupancy is still astronomically large (n̄ ≳ 10⁶¹), so f = 1 to machine precision and

> **n_s = 1.000000 across all observable scales — Harrison–Zel'dovich.**

The red tilt only appears in the **final ~1 e-fold** (n̄ drops to ~7), where n_s plunges from 1 through
0.82 and crashes to large negative values — a sharp, fast-running feature confined to the *smallest,
sub-observable* scales. Planck excludes n_s = 1 at ~8σ (and the observed spectrum is gently red and
nearly running-free, not flat-then-cliff).

## Why it fails (the structural reason)

The H-axiom's superposition rule is effectively **on/off**: while n̄ ≫ 1 essentially every GP is
superposed (f ≈ 1, H_eff ≈ H₀ constant ⇒ exact de Sitter ⇒ n_s = 1), and the only departure is the
graceful-exit cliff when n̄ finally falls to ~1. That cliff is **too sharp** — it occupies the last ~1
e-fold, i.e. the smallest scales — to produce the gentle red tilt that the data show *across the whole
observable window*. The observable modes all crossed when superposition was still total, so they all
freeze at the same H₀ → scale-invariant.

This is the opposite of the optimistic 0738 framing ("a modest roll-off lands n_s ≈ 0.965"). That 0738
roll-off was a *posited* smooth decline of the injected variance; the *actual* first-principles
dynamics give no such smooth decline — they give a step. **The 0738 tilt was a tuning with no dynamical
support, and the simplest dynamics that do exist give the excluded HZ value.**

## What the tilt would require (the constructive redirect, NOT a fix)

To match Planck you need a **sustained, gentle** decline d ln H_eff/dN ≈ −0.017 over the *full*
observable window (~50 e-folds), not a cliff at the end. The on/off superposition rule cannot supply
that. The only natural place a smooth, sustained decline could come from is the **smooth decline of the
background SSV / DP-Sea density during inflation** governing the boost *continuously* — i.e. the boost
factor itself is a smooth function H = H(SSV) (or the ZBW injection amplitude σ = σ(SSV)) that eases off
as the medium thins, rather than an on/off switch tied to occupancy ≥ 2.

That relocates the roll-off mechanism from the *unstacking exit* to a *smooth H(SSV) dependence* — a
well-posed next target. But it is NOT derived, and matching −0.017/e-fold would require the SSV-
dependence to have a specific gentle form. So this is a redirect, not a rescue: **n_s remains
unpredicted, and we now know the obvious mechanism (graceful-exit unstacking) is the wrong source.**

## Honest status of the early-universe sector after this brick

- Gaussianity (CLT) — solid (0738).
- Amplitude A_s — one tuning (owed; 0738).
- Horizon — early high c_eff (0738).
- Δc / LPI — survives, reduced to the Z₀-geometric question (0739/0740).
- **Tilt n_s — FOUND PROBLEM.** Simplest first-principles roll-off predicts the excluded HZ value.
  Tilt must come from a smooth H(SSV)/σ(SSV) decline during inflation; not yet derived; the value is
  not predicted and the simplest version is in tension.

This is the sharpest open problem in the sector and a genuine candidate vulnerability — it should be
weighed honestly, not papered over. The construction is not dead (the tilt-from-smooth-SSV path is
open), but "CPP predicts n_s = 0.965" is **not** currently supportable.

## Pointers

- Supersedes the optimistic roll-off framing in `brick4_branch_v_adoption_and_toy_spec.md` §4–§5.
- Toy + verify: `.../early_universe/scripts/0741_rolloff_law.py`.
- Reasoning: `series_relativity/development/reasoning/0741_rolloff_law.md`.
- Next candidate target (if pursued): a smooth H(SSV) / σ(SSV) roll-off during the constant-H phase —
  derive the SSV-dependence and test whether any natural form gives a sustained ~−0.017/e-fold.
