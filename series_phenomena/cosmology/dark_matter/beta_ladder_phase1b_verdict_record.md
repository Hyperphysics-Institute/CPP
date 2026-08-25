# β-LADDER PHASE 1B — VERDICT RECORD

**Patch 3199, 25 August 2026. Kila6.** Executes
`beta_ladder_phase1b_prereg.md` (Patch 3180) to completion. Readings were
frozen before any Phase 1B leg ran.

---

## §1 — INTEGRITY (checked before any statistic, prereg §3)

**GATE PASS — all 4 Phase 1B duplicate pairs BIT-IDENTICAL.** Pairs
{128, 684} × {step, ctrl}, element-exact float64 equality of the full `F`
and `AB` arrays.

**This gate is worth more than Phase 1's.** Its duplicates were computed
*after* an unexplained power-loss reboot of the host (25 Aug, 11:41:28).
Bit-identity therefore certifies the machine's arithmetic across a real
crash, not merely a clean restart.

Completeness verified independently before analysis: 1,114/1,114 Phase 1B
legs plus 256/256 reused Phase 1 β = 0.05 legs, every file readable, every
record carrying the full 264-Moment `F`/`AB` arrays, zero stray `.tmp`.
(Driver defect noted: `run_1b` printed CAMPAIGN COMPLETE unconditionally
rather than counting files as Phase 1's `run_all` does. Caught, verified
by hand, fixed below.)

## §2 — THE MEASUREMENT

| β | m | sust_B | 99% CI | k = s/β (VOID cmp) |
|---|---|---|---|---|
| 0.05 | **685** | 2.4627e-04 | **[7.089e-05, 4.283e-04]** | 4.9253e-03 |
| 0.10 | 128 | 9.1406e-04 | [4.783e-04, 1.348e-03] | 9.1406e-03 |
| 0.15 | 128 | 1.1222e-03 | [7.194e-04, 1.523e-03] | 7.4810e-03 |
| 0.20 | 128 | 1.4379e-03 | [1.069e-03, 1.824e-03] | 7.1894e-03 |

**The underpower is cured.** At N = 685 the β = 0.05 rung's CI excludes
zero ([7.09e-05, 4.28e-04]) where at N = 128 it spanned it
([−1.467e-04, 5.958e-04]). The ratio's denominator no longer admits zero
and its interval collapses from [−222, +188] to **[3.137, 18.883]**.

Ratio `s(0.20)/s(0.05)` = **5.839**, 99% CI [3.137, 18.883] — **excludes
1.0**, contains 4.0.

Through-origin fit **k_hat = 7.1007e-03**; every rung's 99% CI contains
`k_hat·β` at all four rungs.

## §3 — FROZEN READING: **BETA-LINEAR**

Both limbs of the frozen criterion passed: the through-origin fit is
consistent with all four rungs simultaneously, and the ratio CI contains
4.0 while excluding 1.0. **The instrument's sustained response scales
with drive strength. BETA-FLAT is excluded at 99%.**

**What is established, and what is not.** The ratio interval is wide and
right-skewed: it excludes the flat hypothesis decisively, but admits
values from 3.1 to 18.9, so it is consistent with strict proportionality
(4.0) *and* with superlinear scaling up to ~19×. **"The response
scales with β" is established. "It scales proportionally" is consistent
with the data but not pinned by it**, and this record does not claim
otherwise.

**Coefficient stability, reported as arithmetic, not as a claim:** k_hat
moved 7.3701e-03 → 7.1007e-03 (−3.7%) when the low rung's sampling rose
5.35×. Stable. It remains uninterpretable as a physical magnitude — see
§5.

## §4 — AGAINST THE WORKER: THE CONFIRMED PREDICTION IS WEAK EVIDENCE

The Phase 1B prereg pre-declared **BETA-LINEAR**, and BETA-LINEAR
returned. **That confirmation deserves less credit than it appears to,
and the record says so rather than banking it.**

The Phase 1 pre-declaration (BETA-FLAT or SUBLINEAR) was blind and it was
**wrong**. The Phase 1B pre-declaration was made *after* seeing Phase 1's
through-origin fit pass at k_hat = 7.37e-03 across all four rungs — it
was an informed update, not an independent prediction. A prediction that
merely restates what the existing data already favour tests very little.
The prereg recorded it explicitly as a reversal for this reason; that
labelling is now discharged, and the correct reading of this campaign's
pre-declaration record is: **one blind prediction made, one blind
prediction falsified, one informed update confirmed.** The programme's
prediction ledger should credit it accordingly.

## §5 — SCOPE FENCE (prereg §5, enforced)

**No coefficient claim is made.** `SUST_REF = 0.026·β` remains VOID as a
comparator (Patch 3176: a polarization amplitude transplanted into a
force band with an implied conversion factor of 1, against a computed
factor ≤ 0.008 or exactly 0 by profile). More data does not revive a void
comparator; the 3175 COEFFICIENT-OVERPREDICTED finding stays **RETRACTED**
and is not revived by this campaign. The `k` column above is diagnostic
arithmetic under a VOID label.

**Therefore BETA-LINEAR is an INSTRUMENT PROPERTY, not a physics
verdict.** It says the instrument responds proportionately to drive. It
says nothing about whether the magnitude of that response is right,
because nothing valid currently exists to compare the magnitude against.
**Magnitude waits on OPEN-BAND-CONV-1** (strategy §S1) — still the
highest value-per-cost move on the board, still container work, still
costing no machine time.

## §6 — CONSEQUENCE FOR THE STANDING BOARD

**The hazard direction held; this outcome does not rescue Candidate (B).**
BETA-FLAT would have supplied a benign account of AK's null — the band's
β-scaling was simply wrong, so AK was never expected to see anything at
β = 0.60. **BETA-LINEAR removes that escape route:** the instrument does
scale with drive, so AK's drive advantage was real, and AK's null cannot
be explained by β-scaling failure. What AK's null *does* mean remains
open, because the comparator that declared it a null is itself void.

**Ledger untouched: DISP-I3 stands until re-adjudicated; six of seven;
item 1B OPEN; Candidate (B) 79.5%. The frozen tree is not re-run.**

## §7 — WHAT PHASE 1B CLOSES AND WHAT IT LEAVES

CLOSED: the β-ladder's scaling question, at the sampling the analyzer
itself specified, on a gate that survived a host crash.

OPEN, unchanged: the magnitude question (OPEN-BAND-CONV-1); the
intermittency question (Phase B / S2 on VideoCPU); the entity-Sea
question (S3, gated on S2); DISP-I3's re-adjudication.
