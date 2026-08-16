# n = 10 COMPLETE — FROZEN VERDICT: **REMAINS-OPEN** (two independent triggers) — and THREE findings that reframe the question: (1) the step REVERSED SIGN (−0.0027, −0.0074, **+0.0059**): the tail is OSCILLATING about ≈ 2.6128, i.e. sitting at the instrument's resolution floor rather than drifting — the "residual drift" reading of n = 9 is retired by its own successor; (2) **Q5 CONFOUNDING IS CONFIRMED AND LARGE:** the global data collapse moves from d_c = 2.675 to 1.810 when the d_s ∈ [1.7, 2.3] anomaly region is excluded — a shift of **0.865**, seventeen times the 0.05 threshold declared in 3148; (3) **THE BINDER SIGNAL LIVES AT d_s = 2.0, NOT AT THE PEAK:** U = −0.24 there at n = 10, SAME SIGN BOTH SEEDS, ~5× its n = 9 magnitude and GROWING WITH SIZE, while remaining ≈ 0 everywhere else — a size-growing non-Gaussian (heavy-tailed, intermittent) fluctuation signature at the anomaly, which is the classic mark of a critical point and is ABSENT at the 2.61 peak we have been extrapolating for eight sizes

**Patch 3151 (15 Aug 2026). Executes the frozen verdict rule
(3147 §3 as amended 3148) on eight sizes. Venue: VideoCPU, 16 cells,
8 workers, seed agreement ≤ 0.0007.**

## §1 — The verdict, in the frozen words

Peak sequence: 3.420, 3.338, 3.106, 2.649, 2.617, 2.6143, 2.6069,
**2.6128**. Steps: −0.082, −0.232, −0.457, −0.032, −0.0027,
−0.0074, **+0.0059**.

E1 = 2.6128. Primary convergence test **PASS**; strict test (≤ 0.005
twice) **FAIL** ⇒ tests DISAGREE ⇒ per the 3148 amendment,
**REMAINS-OPEN**. Live estimators E1 = 2.613 and E3 = 2.675 (spread
0.062, inside the 0.10 gate; D_res would have been 2.644), E2 VOID
per 3150. **VERDICT: REMAINS-OPEN.** The frozen d_s* = 2.450 stands
unrevised; the calibration is untouched (OBL-CAL-LABEL). Recorded
without adjustment: had only the primary test governed, D_res =
2.644 would have given |2.644 − 2.450| = 0.194 > 0.182 —
STANDS-QUANTIFIED. The stricter rule adopted from DeepSeek's return
is what prevented a verdict here, exactly as a conservative
amendment should.

## §2 — Finding 1: the tail OSCILLATES; the drift reading is retired

The n = 8 → 9 step was −0.0074, prompting the 3150 flag that drift
might have resumed. The n = 9 → 10 step is **+0.0059 — opposite
sign**. Three sizes now scatter about a common value with no
directional tendency (mean of n = 7…10: 2.6128, full spread 0.010).
**The "residual drift" reading is retired by its own successor;**
the "instrument resolution floor" reading stands. This is what
running the extra size was for, and the answer arrived against the
worry rather than for it.

## §3 — Finding 2: the anomaly CONFOUNDS the collapse (Q5 answered)

Global data collapse over n ≥ 6: **d_c = 2.675 (ν = 0.72)** with all
cells; **d_c = 1.810 (ν = 0.94)** excluding d_s ∈ [1.7, 2.3].
**Shift 0.865 — seventeen times the 0.05 threshold declared in
3148.** Q5's CONFOUNDING option (Copilot's minority answer) is
CONFIRMED by measurement: the anomaly region dominates the global
fit, and any collapse-based estimate that includes it is unsafe.
The two collapse values bracket both candidate features rather than
agreeing — a further sign that ONE scaling family does not describe
this data, as the panel suspected.

## §4 — Finding 3: the critical signature is at d_s = 2.0, not at the peak

Binder cumulant at n = 10 by spacing: **2.0 → −0.241** (seeds −0.277,
−0.204 — same sign, agreeing); 1.5 → +0.136; 2.5 → +0.017;
3.0 → +0.012; ≈ 0 elsewhere. At n = 9 the 2.0 value was −0.038;
**at n = 10 it is −0.241: roughly fivefold growth in one size step,
with both seeds agreeing in sign for the first time.**

Interpretation, stated as a HYPOTHESIS and adopted nowhere:
U ≈ 0 is Gaussian; U < 0 is heavy-tailed/intermittent. A
fluctuation signature that is absent everywhere else, present at one
spacing, and GROWING WITH SYSTEM SIZE is the classic behavior of a
genuine critical region — and it sits at d_s ≈ 2.0, not at the
≈ 2.61 susceptibility peak the programme has extrapolated across
eight sizes. Together with §3, this raises a possibility the corpus
must now confront honestly: **the peak locator may have been
tracking a smooth crossover all along, while the actual transition
sits near 2.0** — where f_b also dips monotonically deeper with
every size (0.232, 0.186, 0.165, 0.156, 0.152, 0.153 for
n = 5…10). Note without comment that the frozen 2.450 lies between
the two candidate features.

## §5 — Disposition (economy rule applied)

The frozen verdict sends this to the panel — but the panel's OWN
mandated diagnostic (`run anom`: the fine grid {1.75, 1.90, 2.10,
2.25} at n = 8, 9) has not yet run, and §3–§4 make it the decisive
measurement rather than a side check. **Dispatching before running a
diagnostic the panel already ordered would waste the round.** The
anomaly map runs first; then CONV-022 assembles with the verdict,
these three findings, and the anomaly's size-scaling — bundled with
the Route C round per WORKFLOW-REVIEW-ECONOMY. Kila6 untouched;
arrival still trumps all.
