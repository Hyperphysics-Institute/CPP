# THE CROSSING TEST RETURNS **CROSSING-UNRESOLVED** (frozen words) — location agreement PASSES (1.865 vs 1.881, within 0.016) but U\* agreement FAILS (0.096 vs 0.181, apart by 0.085 — nearly triple the 0.03 tolerance); **AND THE DENSER GRID REFUTES PATCH 3156's OWN ESTIMATE: U rises with size at 1.75, 1.78, 1.82 AND 1.86, falling only at 1.90, so the crossing lies between 1.86 and 1.90 — not at the 1.824 that linear interpolation across a steep segment produced**; the disqualifying limitation named in 3156 §3.1 was the correct one, and it disqualified the number

**Patch 3157 (16 Aug 2026). Executes `3156_crosslane_examination_and_crossing.md`
§4 exactly. Venue: VideoCPU, 18 cells, seed agreement DEGRADED (see §3).**

## §1 — The measurement

| d_s | U(n=8) | U(n=9) | U(n=10) |
|---|---|---|---|
| 1.75 | +0.083 | +0.117 | +0.178 |
| 1.78 | +0.091 | +0.141 | +0.184 |
| 1.82 | +0.097 | +0.168 | +0.207 |
| 1.86 | +0.066 | +0.071 | +0.131 |
| 1.90 | +0.323 | +0.283 | +0.227 |

Crossings, adjacent independent pairs: (8,9) → d_s = 1.865,
U\* = 0.096; (9,10) → d_s = 1.881, U\* = 0.181.
**Location agreement 0.016 (PASS); U\* agreement 0.085 (FAIL).**
The frozen rule required both. **VERDICT: CROSSING-UNRESOLVED —
more sizes required; to the panel as such.**

## §2 — Patch 3156's estimate is REFUTED by its own confirming test

3156 §3.1 named the disqualifying limitation explicitly: only two
grid points bracketed the crossing, so the location came from linear
interpolation across a steep segment. That limitation is exactly
what went wrong. The denser grid shows U RISING with size at 1.75,
1.78, 1.82 AND 1.86 — the fall appears only at 1.90 — so the
crossing sits between 1.86 and 1.90, and **the 1.824 candidate is
withdrawn.** The three-pair agreement to 0.010 that made it look
strong was an artifact of interpolating the same steep segment three
times: agreement among estimates sharing a common error is not
independent confirmation. Recorded as a methodological lesson, not
just a retraction.

## §3 — The deeper finding: the Binder noise floor is comparable to the signal

Seed-to-seed differences across the nine new cells: mean 0.037,
max 0.103 — an order of magnitude worse than the 0.001–0.01
agreement that f_b shows in the same runs. This is expected and
should have been quantified before the estimator was trusted: the
Binder cumulant is a FOURTH-moment quantity, whose estimator
variance goes as ≈ 2.67/N_eff, and our 1000-Moment window of a
strongly autocorrelated series carries far fewer effective samples
than Moments.

**Consequence, stated plainly: size-to-size differences of ≈ 0.05 —
the very differences the crossing analysis is built on — sit AT the
noise floor.** What survives the floor is the large structure: the
+0.32 spike at 1.90 is ≈ 5σ and real; the n = 11 excursion at 2.0
(+0.46 with seeds 0.090 apart) is NOT resolvable and is now formally
flagged pending the stationarity check.

## §4 — What this costs and what it buys

The Binder route is not dead, but it is **undersampled, not
undersized**: adding sizes cannot fix a variance problem. The fix is
sampling — longer windows (T scaled with system size, since
relaxation time grows with n) and/or more seeds, which are
embarrassingly parallel and cheaper per unit of variance reduction
than new sizes. Rough scaling: halving the SE needs 4× the samples.
**No such campaign is launched here.** It is a real cost, the CC
lane is already YIELDED, and Kila6's Route C lands in ~2 days — so
this goes to CONV-022 as a costed option for the panel to prioritize
against everything else, rather than as a unilateral compute
commitment.

## §5 — Standing state of the d_s ≈ 2 question

- The f_b feature (minimum, deepening, location 2.0 → 2.1 → 2.1) is
  robust: f_b agrees across seeds to ≈ 0.001 at every size and is
  NOT affected by §3's variance problem.
- The Binder-based critical reading — 3151 §4, revised by 3156 §1,
  candidate-located by 3156 §2 — is now **UNRESOLVED at the
  achievable precision**, with its location candidate withdrawn.
- The ≈ 2.61 susceptibility peak and the frozen d_s\* = 2.450 are
  untouched by all of this; the calibration is untouched
  (OBL-CAL-LABEL).
- 3156a's n = 11 prediction was scored and REFUTED (U(1.9) held at
  +0.2295 vs the predicted 0.149); its §6 location discriminator
  returned TRANSITION-CONSISTENT (zero shift). Both recorded.

Everything above rides into CONV-022 with the Route C verdict.
Kila6 untouched; arrival still trumps all.
