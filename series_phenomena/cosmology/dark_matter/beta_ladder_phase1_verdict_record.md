# THE β-LADDER PHASE 1 — VERDICT RECORD

**Patch 3175, 21 August 2026. Kila6.** Executes `beta_ladder_prereg.md`
v2 (§8, Patch 3174) to completion. Readings were frozen before any leg
ran; nothing below was selected after the data existed.

---

## §1 — CAMPAIGN INTEGRITY (checked BEFORE any statistic, prereg §5.3)

**GATE PASS — all 16 duplicate pairs BIT-IDENTICAL across a machine
restart.** Element-exact float64 equality of the full `F` and `AB` arrays
(pairs {0, 127} × {step, ctrl} × all four rungs). `--analyze` refuses
without this and did not run until it passed.

**MemTest86: 4 passes, 0 errors (18 Aug 2026).** Prereg §5.4 acceptance
condition SATISFIED — **this campaign is NOT provisional** and carries no
downstream provisional label.

Execution: 1,024 evidentiary legs + 16 duplicates, ~60 h wall on 32
workers, per-leg 6,070–8,133 s. One mid-campaign interruption; leg-atomic
checkpointing resumed at pair 0016 with no repeats and no gaps.

## §2 — THE MEASUREMENT

| β | m | sust_B | 99% CI | k = s/β | k/0.026 |
|---|---|---|---|---|---|
| 0.05 | 128 | 2.2686e-04 | [−1.467e-04, 5.958e-04] | 4.5371e-03 | 0.17 |
| 0.10 | 128 | 9.1406e-04 | [4.701e-04, 1.369e-03] | 9.1406e-03 | 0.35 |
| 0.15 | 128 | 1.1222e-03 | [7.267e-04, 1.517e-03] | 7.4810e-03 | 0.29 |
| 0.20 | 128 | 1.4379e-03 | [1.065e-03, 1.816e-03] | 7.1894e-03 | 0.28 |

Ratio `s(0.20)/s(0.05)` = 6.338, 99% CI **[−222.095, 187.758]** —
contains 1.0 AND contains 4.0.

Through-origin fit: **k_hat = 7.3701e-03** (prediction 2.600e-02); every
rung's 99% CI contains `k_hat·β` (True at all four rungs).

Required N from measured scatter: **≈ 685 pairs/rung**.

## §3 — FROZEN READING: **BETA-UNRESOLVED**

Per prereg §3, BETA-UNRESOLVED is the reading when the ratio's CI
contains both 1.0 and 4.0. It does. **The primary question — does the
sustained response scale with β — is NOT declared in either direction.**

**The cause is the pre-disclosed underpower, and it is diagnosed, not
excused.** The β = 0.05 rung's own CI spans zero
([−1.467e-04, 5.958e-04]); the ratio's denominator therefore admits zero
and the ratio's interval diverges to ±200. The v2 amendment §8 recorded
this exact risk before launch ("at β = 0.05 the expected signal
approaches the resolution floor at N = 128"). The disclosed hazard fired.

**Stated as observation, NOT as a reading, and NOT substituted for one:**

- The three upper rungs each DETECT (every CI excludes zero) and the
  response rises monotonically 9.14e-04 → 1.12e-03 → 1.44e-03.
- The through-origin fit's limb of the BETA-LINEAR criterion PASSED: a
  strict proportional law at k_hat = 7.37e-03 is consistent with all four
  rungs simultaneously. **BETA-LINEAR required BOTH limbs; the ratio limb
  failed on power, so the reading is UNRESOLVED and stays UNRESOLVED.**
  The worker declines to promote a half-satisfied criterion.
- Direction of the residual: the worker's pre-declared expectation was
  BETA-FLAT or BETA-SUBLINEAR. What the data show is neither flat nor
  declared — **the pre-declared expectation is NOT confirmed here**, and
  the fit limb points away from it. Recorded because it cuts against the
  worker.

**Remedy, costed, NOT launched:** N ≈ 685 at β = 0.05 alone is 1,114
additional legs ≈ 74.5 h ≈ 3.1 days on Kila6; the full ladder at N = 685
is ≈ 12.4 days. **Re-siting the ratio endpoints (e.g. to
s(0.20)/s(0.10), which the existing data would resolve) is FORBIDDEN
here** — the endpoints were frozen before the data and changing them now
would be extraction of the exact kind the protocol exists to prevent. Any
successor must freeze its endpoints before its own testing data exists.

**AK is NOT withdrawn.** BETA-FLAT did not return, so the tree item-1
consequence in §4 does not fire. DISP-I3 stands; item 1B remains OPEN;
the frozen tree is not re-run (prereg §4).

## §4 — **COEFFICIENT-OVERPREDICTED** (fired — then **SUSPENDED at Patch 3176**)

> **SUSPENSION NOTICE (Patch 3176, 22 Aug 2026).** The band this section
> compares against (`SUST_REF` = 0.026·β) has been traced to a
> **polarization amplitude** (Sea-pair dipole moment `p = plus − minus`,
> 2914 line 41) transplanted into a **force** band as though the
> conversion factor were 1. The computed factor is |F_CONV| ≤ 0.008 for
> a uniform profile and **exactly 0** for the odd profile the 2918
> record reports. Against any corrected band the measured response is
> 45×–340× ABOVE, not 3.5× below: **the finding below fails in magnitude
> and inverts in direction.** Nothing in this section may be cited or
> dispatched. No counter-claim is minted either — an invalidated
> comparator supports no verdict in either direction. See
> `band_provenance_audit_3176.md`; successor OPEN-BAND-CONV-1.
> §1–§3 and §5 of this record are UNAFFECTED.


**Every rung's 99% CI excludes 0.026·β.** Measured k clusters at
7.19e-03 – 9.14e-03 (through-origin k_hat = 7.37e-03) against the 2918
decomposition's predicted 0.026 — an overprediction of **≈ 3.5×**.

Provenance of the confrontation, stated in full:

1. Route B (3028-era): 3 arms, 2 of 3 out of band.
2. Route C corrected (3164/3165): 5 arms clustered 0.55–1.63e-03 against
   a 2.6e-03 prediction at β = 0.10.
3. **This campaign:** 4 rungs, a fourfold drive lever, the founder's
   inside-the-Sea geometry, a horizon 2.8× AK's, and a passed
   bit-identity gate on memory-tested hardware.

Three campaigns, three codebases, one direction. The earlier candidate
account (≈ 0.010·β, offered and not adopted at 3165) is corroborated and
sharpened to ≈ 0.0074·β. **REGISTERED, NOT ADOPTED** (prereg §3):
adopting a corrected coefficient requires its own round.

**LIM-ISOLATED-DP applies here and is the reason adoption would be
premature** (`founders_voice/founder_ruling_inside_sea_dp_entities_2026-08-18.md`
§4.4): every current Sea instrument builds isolated, independently
jittered dipoles, while the founder's registered picture has the Sea
aggregated into DP entities with free charge between them. A coefficient
discrepancy therefore indicts **either** the 2918 derivation **or** the
isolated-DP idealization, and this campaign cannot separate them. The
scaling readings are robust to a level error in the medium's response;
the absolute coefficient reading is fidelity-limited.

## §5 — DISPOSITION (worker recommendation; founder decides)

The coefficient finding meets the review-economy §2.1 threshold on its
own terms (a thrice-failed zero-parameter prediction is a closed
confrontation, not an instrument repair). The worker's recommendation is
to dispatch it bundled with the standing DM disposition **with
LIM-ISOLATED-DP disclosed in the dispatch**, and to let the panel rule on
whether the limitation blocks adoption — rather than the worker deciding
that question unilaterally by holding the finding back.

The competing course, equally defensible and preferred if the founder
judges entity structure likely to move a coefficient by ≈ 3.5×: hold the
coefficient finding until the entity-aware instrument (D-JITTER-1
pipeline, fed by measured f_b) can separate the two indictments.

**No disposition is produced by this record. Nothing moves the ledger.**
