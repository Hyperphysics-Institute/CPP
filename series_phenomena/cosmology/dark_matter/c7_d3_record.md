# C7-D3 execution record — VERDICT D3-NO-PLATEAU (dt-stable, both phases): the dance estimator's object is NOT local curvature on this ladder — while the static curvature EXISTS, is small (−259), and is plateau-perfect, with the dance number visibly decaying toward it as the offset term dies

**Patch 2652, 20 July 2026.** Execution under `c7_discriminant_campaign_prereg.md`
(2649) §4 ONLY — third arc, frozen order complete. Verify: `code/2652_c7_d3.py`,
stages guardtest | cleanroom | static | dance | tc | resample | read, all run
(operationalization declared in the script header BEFORE any cell, nucleus1
precedent; dance/tc checkpointed per the runtime rider). Per the composite-only
rule this reading registers; the composite adjudication is Patch 2653.

## 1. Controls and J4 apparatus — ALL PASS

- **Guard-trigger tests:** x=0 assert, antisymmetry zero-denominator, n<2
  leave-one-out — all fire clean.
- **Clean-room classifier (DeepSeek's condition, 2648):** written from the
  registered prose, no code copied; **24/24 cell-by-cell agreement** across the
  full D1 store (3 TC × 2 dt × 4 modes) and **BRANCH N reproduced** on the 2635
  registered table. The inherited classifier is not an implementation accident.
- **Exact internal estimator pair (the declared same-object test):** static
  λ_U (closed-form potential, energy form) vs λ_F (ssv_vectors generalized
  force, force form) agree to ≤ 0.8% across the full ladder with antisymmetry
  residuals at machine precision. **D3-ESTIMATOR-SPLIT does NOT fire.**

## 2. The static level (registered data)

λ_static ≈ **−258.9 to −262.9**, IDENTICAL at both phases, ratio-flat to 1%
across the full 16× ladder — a textbook plateau. The m2 static softened-Coulomb
curvature of the frozen scaffold exists, is well-defined, and is SMALL.
**Scope fence (pre-empting a reviewer misread):** this is a frozen-scaffold
static-potential number; dynamical stability is a different, separately
registered question (the NUCLEUS-1 certification class) and NO stability
sentence of any kind rides on this value.

## 3. The dance level (TC = 60, both phases, both dt)

```
lam_E(x):  x=0.01        0.02       0.04      0.08     0.16
 dt50 ph0:  -1,449,267  -152,169   -98,988  -26,818   -3,314   (all adjacencies [outside])
 dt50 ph90: -1,321,802  -379,269   -77,083   -8,535   -2,375   (all [outside])
 dt25 ph0:  -1,738,225  -167,171  -108,081  -23,266   -3,001   (all [outside])
 dt25 ph90: -1,827,400  -414,091  -130,582  -12,684   -2,893   (all [outside])
```

**No adjacency at any phase or dt falls in the declared plateau band [0.8,
1.25]** — λ_E varies by THREE ORDERS OF MAGNITUDE down the ladder. ±x
agreement FAILS at multiple rungs (one-sided c+ and c− disagree in SIGN, e.g.
−424,531 vs +120,192 at x=0.02 ph0 dt50). TC subset drifts 3–13% (disclosed).
Resampling on the registered D1 members: leave-one-out sign-stable at both dt
(disclosed; this condition alone passing cannot rescue the others).

**Frozen reading: D3-NO-PLATEAU** — "the object is not local curvature on this
ladder; the invalid-regime reading hardens" (2649 §4 verbatim).

## 4. Observation registered without claim — the three-arc closure

λ_E·x² (the raw symmetric energy excess) is ≈ **−72 to −165 MeV across the
entire 16× ladder** — the amplitude-independent offset of D2 (−71…−93 band),
now seen from the third independent direction. And the dance λ_E decays toward
the static −259 as x grows (−3,314 → the offset/x² term dying into the true
curvature floor): the estimator reads offset/x² where it was built to read
curvature. Three arcs, one mechanism, each prediction WRITTEN BEFORE the arc
that tested it ran (2650 §3; 2651 §3.1). The composite record owns any
adjudication sentence.

## 5. Standing

D3 DISCHARGED at D3-NO-PLATEAU. All three arcs complete; **composite
adjudication at Patch 2653** per the frozen rule. Fences held; 2513/2635
unedited; C7 untouched at this patch; 79.5% untouched. Reasoning:
`reasoning/2652.md`.
