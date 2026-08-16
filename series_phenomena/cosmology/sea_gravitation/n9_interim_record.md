# n = 9 COMPLETE — TWO HONEST FINDINGS BEFORE n = 10: (1) **the plateau is NOT settling monotonically** — peak(9) = 2.6069, a step of −0.0074 that is nearly THREE TIMES the previous step (−0.0027): it PASSES the frozen ≤ 0.02 test but FAILS DeepSeek's strict ≤ 0.005 test, and under the 3148 amendment that disagreement is ITSELF a REMAINS-OPEN trigger — the panel's "plateaus can resume drifting" warning is now empirically live; (2) **the Binder cumulant is UNINFORMATIVE on this observable** — U ≈ 0 everywhere (the Gaussian value), seed-to-seed noise EXCEEDS the seed-averaged signal (S/N = 0.77), sign flips at 3 of 8 spacings ⇒ E2 (Binder crossings) is not viable as an estimator here, reported as an instrument finding, not a choice — and its near-zero value is itself physics: the transition shows NO symmetry-breaking/bimodal signature, consistent with the panel's crossover hypothesis

**Patch 3150 (15 Aug 2026). Interim record; the frozen verdict rule
(3147 §3, as amended 3148) executes only after n = 10. Venue:
VideoCPU, 16 cells one batch, seed agreement ≤ 0.0008.**

## §1 — The sequence, seven sizes

3.420 → 3.338 → 3.106 → 2.649 → 2.617 → 2.6143 → **2.6069**.
Steps: −0.082, −0.232, −0.457, −0.032, −0.0027, **−0.0074**.

The tail is NOT monotonically damping: the n = 8 → 9 step is 2.7×
the n = 7 → 8 step. Either the plateau has small residual drift (the
panel's stated worry, now with evidence) or the last two steps are
at the instrument's own resolution floor and the ordering is noise.
**Both readings are consistent with the data and NEITHER is
adopted** — n = 10 is the discriminator the frozen rule requires.

## §2 — The two convergence tests now DISAGREE

| test | criterion | n = 8 → 9 step | result |
|---|---|---|---|
| frozen primary (3147) | ≤ 0.02 | 0.0074 | **PASS** |
| strict (DeepSeek, 3148) | ≤ 0.005 | 0.0074 | **FAIL** |

Per the 3148 amendment — adopted before this datum existed —
**disagreement is itself a REMAINS-OPEN trigger.** Unless n = 10's
step satisfies both, the frozen verdict is REMAINS-OPEN regardless
of where the estimators land. Recorded now, before n = 10 runs, so
the rule cannot later appear to have been read off the outcome.

## §3 — E2 (Binder crossings) is not viable on this observable

Measured U = 1 − m₄/(3m₂²) on the per-Moment bound-fraction series:
values span −0.085 to +0.112, |mean| = 0.010; **mean seed-to-seed
difference 0.050 EXCEEDS the mean seed-averaged magnitude 0.039
(S/N = 0.77)**; signs flip between seeds at 3 of 8 spacings.
Crossings extracted from such curves would be noise artifacts.

**This is an instrument finding, reported before the verdict, not an
estimator choice** — the worker is not discarding an inconvenient
estimator but recording that it carries no signal, with the numbers
shown. **And the null is itself physics:** U ≈ 0 is the GAUSSIAN
value, so the bound-fraction distribution is unimodal and
Gaussian at every spacing and size measured — there is no
symmetry-breaking, two-state signature anywhere near the
transition. That is direct support for the panel's alternative
hypothesis (crossover/commensuration rather than a conventional
critical point), and it explains why critical-scaling machinery has
misbehaved from the start. Consequence: the mandated suite runs with
E1 (peak convergence) and E3 (data collapse, both with and without
the anomaly region) as the live estimators; E2 is reported VOID with
its diagnostics, and the panel is told plainly.

## §4 — Next

`run 10` (≈ 6–8 h, 8 workers) then `run anom` then `analyze`.
Frozen d_s* = 2.450 unrevised; calibration untouched
(OBL-CAL-LABEL). Kila6 Route C untouched; arrival still trumps all.
