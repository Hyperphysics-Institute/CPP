# Reasoning capture — Patch 0744: deriving p — reduces to smooth-exit vs cliff

*Session 154. The decisive p-derivation. Writeup: `series_relativity/development/derive_p_finding.md`.
Toy: `.../scripts/0744_derive_p.py`. NO THEO.*

## The reduction

δN: ζ = δN = (1/3)(δn̄/n̄). P ~ H_eff² at crossing ⇒ n_s − 1 = 2 d ln H_eff/dN. So p is fixed by how
H_eff depends on the superposition state — computable from the boost rule, not free.

## An error I caught (and what it taught)

My first toy placed the observable pivot at N_rem=3 (3 e-folds before end) instead of N_rem≈57
(observable modes cross EARLY, ~57 e-folds before end). That made the log case read 0.333. Fixed the
pivot (N = N_star − 57 ≈ 3.5, where ln n̄ ≈ 171, N_rem = 57). With the correct pivot the log coupling
gives 0.9649 exactly. Lesson logged: always evaluate at N_rem≈57 (early crossing), not near the end.

## Result (corrected)

- depth-independent (literal per-GP axiom): H_eff const → cliff in f → n_s = 1.0000, EXCLUDED (=0741).
- log of occupancy (H_eff ∝ ln n̄ ∝ N_rem, smooth wind-down): n_s = 0.9649 = canonical 1 − 2/N_*. p=2.
- linear (per-CP): H_eff ∝ n̄ → n_s = −5, EXCLUDED.

## Honest verdict (neither rigged up nor over-pessimistic)

p does NOT cleanly derive to 2. The spectrum reduces to a single fork: does the graceful exit track
the smooth mean DEPTH ln(n̄) ∝ e-folds-remaining (→ 0.9649, canonical slow-roll) or the cliffing
FRACTION f (→ excluded n_s=1)? The bare on/off axiom is fraction-based (cliff) → excluded. The data
value = the smooth depth-tracking exit. Plausibly favorable (real graceful exits are smooth; mean depth
declines smoothly unlike f; H∝N_rem is the textbook 1−2/N form) but NOT derived (bare axiom is
fraction-based; the depth-log coupling is not shown). So 0.965 is NOT yet a prediction.

Temptation resisted: the log coupling gives EXACTLY 0.9649, which is seductive. I did not declare it a
prediction — the bare axiom gives the cliff/excluded value, and I have not derived that H_eff tracks
depth rather than fraction. Reported as "plausibly favorable, single computation away," not "predicted."

## What would close it
Show H_eff tracks mean depth ln(n̄) (smooth, ∝N_rem) not fraction f (cliff). Then n_s = 1 − 2/N_* =
0.965 is a zero-parameter prediction (N_* already CP-count-fixed). If H_eff is genuinely fraction-based,
CPP predicts excluded n_s=1 and the tilt is a real vulnerability.

## Net arc
0738 tuning → 0741 cliff/excluded → 0742 n_s=1−p/N_* (N_* CP-fixed, p free) → 0744 p reduced to the
depth-vs-fraction fork (smooth→0.965, cliff→excluded). The spectrum thread is one well-posed,
plausibly-favorable computation from closing or failing.

## Conventions
NO THEO (model-structure result; no prediction registered since p not derived). Verify script bundled.
Clear of chirality. PCD = Perceive/Compute/Displace.

## Pointer
- THE gating computation: does H_eff track mean superposition depth ln(n̄) or fraction f? Decides
  whether n_s=0.965 is a CPP prediction or CPP predicts the excluded n_s=1.
