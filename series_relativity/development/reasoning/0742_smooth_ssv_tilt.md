# Reasoning capture — Patch 0742: tilt recovered, n_s = 1 − p/N_* (coupling to e-folds-remaining)

*SR-1 rederivation pass, Session 154. Recovery from the 0741 found-problem. Writeup:
`series_relativity/development/smooth_ssv_tilt_finding.md`. Toy: `.../scripts/0742_smooth_ssv_tilt.py`.
NO THEO.*

## The diagnostic that led to the fix

0741's failure was specific: the available rates were 3/e-fold (density, too fast) and 0-then-∞
(on/off fraction). The data need a sustained −0.018/e-fold. The ONLY variable declining ~170× slower
than the density but never zero is the LOG of the density — which equals e-folds-remaining
N_rem = (1/3)ln n̄, with d ln N_rem/dN = −1/N_rem ≈ −0.018 at N_rem≈57. That is the natural variable.

## Why coupling to N_rem is principled, not fishing

The δN formalism: the curvature perturbation ζ = δN (fluctuation in the number of e-folds). So the
frozen power depends on the e-fold structure (N_rem), not the instantaneous density. Coupling to N_rem
is the generic structure of inflationary perturbations. ⇒ P ∝ N_rem^p ⇒ n_s = 1 − p/N_*, the standard
slow-roll form.

## What is CPP-specific vs generic (kept straight)

- GENERIC: the n_s = 1 − p/N form (many inflation models give it).
- CPP-SPECIFIC and real: N_* ≈ 60 is FIXED by the CP count (N_* = (1/3)ln(N_CP/N_GP), the same N_CP
  that set the e-folds in Brick #4 C). In standard inflation N_* is partly free (reheating); here it is
  pinned by the initial stacking depth.
- p=0 recovers 0741 (the on/off case = Harrison-Zel'dovich, excluded) — a good consistency check that
  the new model contains the old as a limit.

## Results (no tuning): p=0→1.000(excluded); p=1→0.9835; p=2→0.9670 (Planck 0.9649±0.0042); p=3→0.9505.
Running |α_s|≲6e-4, inside Planck's ±0.0067. n_s flat across the window (Δ~0.006), unlike 0741's cliff.

## The honesty boundary (did NOT overclaim)

This is a STRUCTURAL recovery, NOT a parameter-free prediction. The δN formalism fixes the VARIABLE
(N_rem) but NOT the power p. p is set by how the frozen ZBW source amplitude scales with
e-folds-remaining — underived. p=2 matches and is the simplest large-field value (m²φ²), but the data
REQUIRE p=2; CPP does not yet PREDICT it. p=1 would give 0.984 (~4σ off). So "CPP predicts 0.965" is
still NOT supportable — the gap is now a single integer, down from a free function. I checked the δN
route and confirmed it does NOT by itself fix p (a scale-invariant source gives p=0); p needs the
source-scaling, which is the owed computation. Stated this explicitly rather than letting p=2's match
imply a prediction.

## Net arc (0738→0741→0742)

0738: n_s a tuning (optimistic). 0741: simplest dynamics give EXCLUDED n_s=1 (found problem). 0742:
coupling to the right variable (e-folds-remaining) gives n_s=1−p/N_* with N_* fixed by CP count; tension
resolved; n_s predicted up to one integer p; p=2 hits Planck. Remaining: derive p.

## Conventions
NO THEO (model-structure result + conditional numerical evidence; p underived so no prediction
registered). Verify script bundled. Clear of chirality. PCD = Perceive/Compute/Displace.

## Pointer
- THE gating computation now: derive p = exponent of frozen ZBW power vs e-folds-remaining (≈ vs
  log-density / superposition depth). p=2 ⇒ n_s=0.965 becomes a real prediction; p=1 ⇒ 0.984, ~4σ
  tension. One-number calc, not a free function.
