# THE COMMENSURATION TEST RETURNS **PHYSICS-CONFIRMED** — the worker's own artifact diagnosis is REFUTED by the falsifier the worker froze one patch earlier: the f_b minimum sits at **exactly d_s = 2.0 under BOTH variants** (r_soft = 0.75 predicted 1.5; r_soft = 1.25 predicted 2.5), so the feature is SPACING-INTRINSIC, not an instrument coincidence; the Binder structure, however, is NOT yet adjudicated — the variant cells are n = 7 while the +0.30 spike was measured at n = 8/9, so SIZE and r_soft are CONFOUNDED in that comparison, and the control run is specified rather than a conclusion drawn

**Patch 3153 (15 Aug 2026). Executes `anomaly_commensuration_prereg.md`
§3 exactly. Venue: VideoCPU, 36 cells, seed agreement ≤ 0.002.**

## §1 — The verdict, in the frozen words

| r_soft | artifact would place the feature at | measured f_b minimum |
|---|---|---|
| 0.75 | 1.5 | **2.0** |
| 1.25 | 2.5 | **2.0** |

f_b across the grid, r_soft = 0.75: 0.247, 0.239, 0.228, 0.183,
**0.171**, 0.175, 0.256, 0.266, 0.276. At r_soft = 1.25: 0.240,
0.232, 0.223, 0.177, **0.160**, 0.175, 0.257, 0.274, 0.293.

**VERDICT: PHYSICS-CONFIRMED — the feature is spacing-intrinsic.**
The commensuration diagnosis (Patch 3152 §2) is **REFUTED**. It was
a good hypothesis: two independent instrument constants really do
coincide at exactly 2.0, and that really would have manufactured an
anomaly. It simply is not what is happening. The V-minimum survives
a ±25% change in the softening radius without moving at all.

Note the pattern of the last three patches, recorded deliberately:
3151 advanced the "critical point at 2.0" hypothesis; 3152 supplied
the argument against it and froze a falsifier that would have killed
it; 3153 reports that the falsifier fired the other way. The
hypothesis is not thereby proved — it has survived one honest
attempt at destruction, which is a different and lesser thing.

## §2 — What is NOT adjudicated (stated before anyone asks)

The Binder structure — the +0.30 spike at d_s = 1.9 and the negative
excursion at 2.0 — is **weak or absent in both variants** (1.9:
+0.044 at r_soft = 0.75, +0.014 at 1.25). That looks like an
artifact result. **It cannot be reported as one, because the
comparison is confounded:** the variant cells are n = 7, while the
spike was measured at n = 8 and n = 9. Size and softening radius
change together, so the difference cannot be attributed. The missing
cell is a **control: n = 7 at r_soft = 1.0, same nine spacings, both
seeds** (18 cells, `3152_commensuration_test.py run control`).
- If the control SHOWS the spike ⇒ the spike is r_soft-dependent
  ⇒ Binder structure is instrument-linked while the f_b minimum is
  physical (a genuinely mixed result, and the most likely one).
- If the control does NOT show it ⇒ the spike is size-dependent,
  emerging only at n ≥ 8 ⇒ it strengthens rather than weakens the
  critical-region reading of 3151 §4.
Either way the answer is one hour of compute and it is not guessed
at here.

## §3 — Standing consequences

1. **The 3151 §3 collapse confounding stands as physics, not
   artifact.** The d_c shift 2.675 → 1.810 on excluding the 2.0
   region reflects a real feature, so the global-collapse estimator
   remains unsafe on this data for a physical reason: two features
   in one window, not one scaling family.
2. **The 3151 §4 hypothesis survives its first test.** A real,
   spacing-intrinsic feature sits at d_s ≈ 2.0, distinct from the
   ≈ 2.61 susceptibility peak. Whether it is a second transition or
   a strong crossover is undetermined pending §2's control and the
   Binder question.
3. **The N216 challenge is unaffected in status** (REMAINS-OPEN per
   3151) but better characterized: the disagreement between
   estimators has a physical source now rather than a purely
   methodological one. This goes to CONV-022 with the Route C
   bundle.
4. Frozen d_s* = 2.450 unrevised; calibration untouched
   (OBL-CAL-LABEL). Kila6 untouched; arrival still trumps all.
