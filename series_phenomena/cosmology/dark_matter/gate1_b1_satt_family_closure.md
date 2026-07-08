# S_ATT(N) resolved by family closure — and the correction chain that made the answer trustworthy (Patch 2337, 8 July 2026)

**What this patch is:** founder-gated follow-up 1 executed — and the cross-check it
required caught a truncation bias in the 2336 measurement, which is corrected here with
its blast radius measured. **Verify:** `code/2337_satt_family_closure.py` (5/5;
Rutherford-validated, three-point MC-validated). **NO VERDICT MOVED.**

## 1. The correction chain (in the order it happened)

Building the family closure required an independent transport computation — the
classical deflection integral for the registered screened residual. It disagreed with
the 2336 MC at 200 km/s by ×4.3: far too large for rod structure. Diagnosis, confirmed
at the source: **the shared MC protocol (inherited from 1870/1871) terminates at
closest approach** — rods at ∓Z0 closing at v_rel with budget 2Z0/DTV run out of time
exactly when the separation reaches zero. For long-range attractive swing-bys, whose
deflection accrues over ~100 fm of *exit* path, this truncates the encounter and
reports spurious near-forward deflections.

**Fix:** finish-mode — integrate until every pair is separated >120 fm and receding
(residual tail bend ≲1% of ⟨1−cosθ⟩), persistent orbiters random-phased (physically:
phase-mixed multi-revolution engagements; the integral, which resolves them exactly,
agrees). **Blast radius, measured:** the registered 1870/1871 *repulsive floor* was
probed under finish-mode at 50 and 1500 km/s — **it stands within its own MC noise**
(ratios 0.67±0.20 and 1.38±0.49 vs stored). The bias is specific to the attraction runs.
One finish-mode run (1150) was invalidated by a freeze-threshold artifact, removed from
the record, and the 1150/1500 corrected totals taken from the validated integral plus
the registered floor.

## 2. The corrected curve and windows (supersedes 2336 §2)

σ_T/m (finish-mode MC; integral cross-validated at every attraction-dominated point):
**12.63±2.16 (30) | 8.78±1.13 (50) | 2.65±0.41 (200) | ≈0.06 (1150) | 0.062±0.019
(1500) cm²/g.** Windows: **dSph FAIL ×1.6** (3.4σ below the 20 edge); **pin OVER ×1.76**
(3.4σ above 5); **LSB consistent with its top edge** (2.65 vs 2.5, 0.4σ); group ≈0.06
(F1 falsifier character intact: predicted ≈0.06 vs Sagunski 0.5±0.2); **cluster PASS
×2.1** (margin narrows from ×6.8). Ratio bars: r1 = 1.44 (≥4 required — **FAIL**, the
sole shape failure); r2 = 3.31 (≤7.14 — now **PASSES**). The near-miss sharpens again:
the killed candidate fails the suite *only* at the dwarf pair, by ×1.6–1.8, in opposite
directions — which is exactly the r1 steepness bar and nothing else.

## 3. The family closure (the follow-up's answer)

For V = −(S/r)e^(−r/R_s) at CM energy E, classical transport collapses onto **one
dimensionless function**: σ_T = R_s²·F(ε), ε = S/(E·R_s). Every S(N) law, every E_c,
every N, every R_s moves along the same curve; the velocity ratios fix the ε ratios.
F was computed by deflection integral (Rutherford reproduced to 0.9%; Born wing slope
1.68 ≈ 2 minus log corrections; validated against the corrected MC at three points).

**Result:** the joint bar test is empty at every ε. F has exactly one convex feature —
the **classical orbiting onset**, where local r1 peaks at 5.11, steep enough for the
dSph/pin bar in isolation — but the onset is too localized: placing ε₅₀ there puts the
16× r2 interval on the pre-onset wing (rise ~10²), and off the onset F is log-concave
(where r1 ≥ 4 provably forces r2 ≥ 42.9). The exhaustive windows+floor scan (N treated
exactly as a free shift) finds **zero passing points out to R_s = 120 fm** — four times
beyond the registered band. **S_ATT(N) is RESOLVED-moot classically:** no registration
of any N-scaling can pass the suite, because the failure lives in the transport
function itself, not in the unknown strength.

## 4. What this hands to 2338

The classical orbiting onset is the blunt shadow of a quantum resonance: the same
attractive-well physics, smeared by winding geometry. A quantum resonance is
energy-sharp and **not** bounded by the geometry that kills the classical step — and
λ_dB = 336–560 fm ≫ R_s at dwarf velocities means the quantum computation is the
physical one anyway. Follow-up 2 is now precisely shaped: does the registered potential
(or any point in the OPEN-SS-43 band) place a resonance that lifts σ(30)/σ(50) past 4
without disturbing 200-and-above — and if only a tuned point does, how much tuning?

## 5. Ledger

2336 texture corrected a second time (curve, windows, bars as §2; 2324 flat-relic
sentence stays superseded; the ×486 dynamic-range figure revises to ×204). Registered
1870/1871 floor probed and **standing**. S_ATT(N) follow-up RESOLVED-moot (classical);
OPEN-SS-43's dwarf-magnitude clause inherits the family closure (the reverse-engineered
E_c cannot be tuned into the suite). NO VERDICT MOVED: G4 = KILL-on-suite-conditional
stands, its elastic flank now closed at family level with the single named quantum
remainder (2338, next).
