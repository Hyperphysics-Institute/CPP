# FA-SG-R1 LEG L2 RECORD — registered-arena restriction/prediction test, statistics and tolerances committed BEFORE the comparison ran: structural-class prediction 3-of-4 (S1 FAIL as committed — the diameter-matched compact arena does not stagger), envelope-consistency S2 FAIL at the committed tolerance on both metrics — reported adverse-direction, in full, with diagnosis; no direct-ℓ construction on I1 found (stronger form not available)

**Patch 2687, 21 July 2026. Executing charter §2 R1-L2 under the frozen
[ADJ] (restriction/prediction operationalization; comparison statistic
and tolerance committed before the comparison ran — the commitments are
in the verify-script header, written and fixed before any I1 residual
was computed). Verify: `code/2687_r1_l2_restriction.py`. Nothing renamed
after results. 79.5% not in scope.**

## §1 — The committed statistics (fixed pre-comparison)

**S1 (structural class):** screening locality (ℓ ≪ arena) predicts every
compact arena of I1's proportions is sign-oscillating with no clean decay
regime (classifier: neg-frac ≥ 0.25 AND no constant-sign monotone
|f̄·r| shell run ≥ 0.3 fm). Predicted OSC/NO-REGIME for: I1 chord metric,
I1 geodesic metric, compact-FCC diameter-matched (r ≤ 0.60 fm), and
compact-FCC count-matched (r ≤ 1.00 fm). PASS iff all four.

**S2 (envelope consistency):** per metric, I1 shell means, I6-normalized;
residual against the extended-instrument envelope (FCC R=9, ℓ_ext =
0.0885 fm); tolerance T = 1.25× the extended instrument's OWN max shell
modulation about its fitted envelope over [0.36, 1.2] fm (self-calibrated,
computed before any I1 residual: T = 2.07 log units). PASS iff ≥ 6 of 8
shells within T, none over 1.6T.

**S3:** screening-locality diagnostic (reported, no pass/fail).

## §2 — Results as committed

**S1: FAIL (3 of 4 match).** I1 chord (neg 0.723, run 0.261 fm): OSC ✓.
I1 geodesic (neg 0.597, run 0.000): OSC ✓. Count-matched compact FCC
(135 sites, max pair 0.963 fm; neg 0.448): OSC ✓. **Diameter-matched
compact FCC (19 sites, max pair 0.515 fm): neg-frac = 0.000 — entirely
positive field, no staggering — prediction WRONG on this arena.**

**S2: FAIL on both metrics.** Chord: 3/8 shells within T, worst |Δ| =
4.58 (> 1.6T = 3.31). Geodesic: 1/5 within T, worst 11.66.

**S3 diagnostic:** compact solves vs the full-arena field on the same
sites — diameter-matched median relative deviation 0.023 (the 19-site
field IS the full field locally); count-matched 0.203.

**Stronger-form determination:** no construction permitting a direct ℓ
readout on I1 was found — 8 chord shells spanning < 2 envelope decades
against ~1-decade staggering modulation cannot host a fit window. The
[ADJ]'s fallback operationalization stands as executed.

## §3 — Diagnosis (same font as the result; interpretations are the panel's)

1. **The S1 miss is a site-count effect, and it is itself a finding:**
   staggering requires sufficient multiple-scattering feedback. A
   diameter-matched 3D ball holds 19 sites where the 4D I1 holds 120 —
   the S3 diagnostic shows its field is simply the local (near-source,
   positive) patch of the extended solution. The count-matched arena —
   the better-matched restriction — reproduces I1's class. The committed
   statistic counted both; FAIL stands as committed.
2. **The S2 misses are dominated by geometry mismatch the tolerance did
   not absorb:** the tolerance was self-calibrated on the 3D instrument's
   own modulation; I1's 4D compact shell structure (populations 12→1,
   antipodal closure, single-vertex normalization shell at 1.178 fm)
   deviates beyond it. The geodesic-metric comparison additionally
   stretches distances (path metric vs the 3D chord-space ℓ_ext),
   inflating far-shell residuals — visible in the 11.66 worst case.
3. **What survives:** I1's qualitative class (sign-oscillating,
   no-clean-regime, positive-definite operator) is exactly what the
   extended solution predicts for a ~120-site compact arena — the
   2671 READOUT-INCONCLUSIVE verdict is CONFIRMED as the expected
   behaviour, not an anomaly. What does NOT survive is quantitative
   envelope consistency at the committed tolerance.

**Leg verdict for the class machinery: L2 NOT-CONSISTENT (as committed).**
This bars R1-PASS (charter §5) and is carried adverse-direction to the
packet, alongside the disclosure that the [ADJ] operationalization itself
(diameter- vs count-matching; 3D tolerance against 4D geometry) is
votable at the returns. **Fence audit:** clean. Next leg: L4.
Reasoning: `reasoning/2687.md`.
