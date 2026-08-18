# THE β-LADDER CALIBRATION CAMPAIGN — FROZEN BEFORE ANY LEG RUNS

**Patch 3167, 17 August 2026. Kila6. Economy-rule disposition: NO PANEL ROUND**
(§3 — repairing a defective instrument with a known, principled remedy; §4
pre-commitment applied in full). **This campaign also serves as Kila6's hardware
stress test, and §5 exists because of that.**

---

## §1 — WHAT THIS CAMPAIGN IS FOR

Patch 3165 returned **H-ESTABLISHMENT-MIXED** on the existing legs: neither
H-HORIZON nor H-BETA could be eliminated, and the frozen reading named the
successor requirement directly — *"lengthen AK's horizon AND vary β
independently."* That is what this campaign does, and it is the first Route C
work requiring new compute.

**The open question.** Under the corrected Route B recipe (Patch 3164) four
isolation arms detect a sustained response clustered at 5.50e-4 – 1.084e-3,
while AK — at **6× the drive and 4× the pairs**, with the tightest CI of any arm
— returns −1.56e-4 with its interval spanning zero. Either the response needs
longer than AK's 68-Moment horizon to become detectable, or it does not scale
with β at all. **These are separable only by varying β at a FIXED, adequate
horizon**, which no existing arm does.

**What it also tests.** MEAS-1 §4.1 defines the sustained motion response as
`0.026·β` — a PREDICTION from the 2918 decomposition, never an empirical
calibration. Seven arms across two campaigns and two codebases have now measured
0.55–1.63e-3 against a prediction of 2.6e-3 at β = 0.10. **This campaign
measures the coefficient directly, and therefore tests a CPP prediction rather
than merely repairing an instrument.**

## §2 — DESIGN (frozen)

**Geometry FIXED at the a2/AK configuration** so β is the only varying quantity:
`x_half = 28.0`, `Δ = +6`, `x_src0 = −24.0`, `L = 48.0` — identical to both arms,
removing geometry as a confound.

**Horizon T_END = 264 for EVERY rung.** Justification, recorded now: a0p
(T_END = 264) first detects at 30 Moments post-step and a0 at 78; 264 gives
`t_post = 72`, `base = 48`, and a LATE window at 216:264 sitting **192 Moments
post-step** — nearly triple the longest isolation-arm first-detection time and
2.8× AK's entire horizon. **AK's horizon deficiency is thereby removed by
construction at every rung, including the β = 0.60 rung that reproduces AK.**

**β ladder: {0.10, 0.20, 0.40, 0.60}.** The 0.10 rung reproduces a2's drive; the
0.60 rung reproduces AK's. Four rungs give three independent scaling ratios.

**N = 128 pairs per rung** (matching the isolation arms, so per-rung precision is
directly comparable to the Route C values already in hand).

**Total: 4 rungs × 128 pairs × 2 branches = 1024 legs.** At the measured
~7,400 s/leg for this geometry class, ≈ 2,100 CPU-h ≈ **2.8 days** at 32 workers.

**Statistic: the corrected Route B recipe, verbatim from Patch 3164** —
`sust_B = D[LATE] − D[PRE(12:24)]`, SIGNED, bootstrap over pairs, 10000
resamples, seed 30530811, `det = signed CI excludes 0`. No new statistic is
introduced by this campaign.

## §3 — FROZEN READINGS

Let `s(β)` be the measured sustained response at each rung, with 99% CIs.

- **BETA-LINEAR** — `s(β)` is consistent with proportionality to β across all
  four rungs (a through-origin linear fit's 99% band contains every rung, and
  `s(0.60)/s(0.10)` has a CI containing 6.0 and excluding 1.0). The band's
  `β/0.10` scaling is VINDICATED, and AK's null was a horizon artifact.
- **BETA-FLAT** — `s(β)` shows no significant dependence on β (the ratio's CI
  contains 1.0 and excludes 6.0). **The band's β scaling is FALSIFIED**, every
  AK-class S3-C reading in the corpus inherits the error, and the tree item 1
  requirement that AK pass an β-scaled band was never satisfiable.
- **BETA-SUBLINEAR** — the ratio's CI excludes both 1.0 and 6.0. The response
  scales, but not as β; the exponent is reported with its CI and no band is
  re-sited on it here.
- **BETA-UNRESOLVED** — the ratio's CI contains both. Underpowered at N = 128;
  the required N is computed from the measured scatter and reported.

**Coefficient reading, reported alongside and NOT used to re-site any band:**
`k_measured = s(β)/β` per rung, against the 2918 prediction `k = 0.026`. A
cluster of `k_measured` excluding 0.026 at 99% across rungs is recorded as
**COEFFICIENT-OVERPREDICTED**, with the measured value and its CI. **This is a
finding about CPP's own prediction and it is registered, not adopted** — adopting
it would require its own round.

## §4 — ANTI-EXTRACTION AND THE DIRECTION OF THE HAZARD

**Prior knowledge disclosed:** the worker expects BETA-FLAT or BETA-SUBLINEAR,
because a2 (β = 0.10, s = 7.71e-4) and AK (β = 0.60, s = −1.56e-4) already
differ by 6× in drive with no corresponding difference in response. **That
expectation is recorded before the run and a BETA-LINEAR return would be the
surprise.**

**The hazard direction is unchanged and restated.** If BETA-FLAT returns, AK's
S3-C failure is an instrument artifact, AK's reading is withdrawn from the item-1
test, tree item 1 may cease to fire — and **item 2 then evaluates against S1-C's
SIGNIFICANT result at a2 (Δ = +6), firing DISP-T: the falsifier, against
Candidate (B), requirement 7.** Every outcome of this campaign that repairs the
instrument moves toward convicting the programme's leading dark-matter
candidate. GPT's CONV-024 symmetry condition is satisfied by arithmetic, not by
argument.

**This campaign does NOT re-run the frozen tree.** A restored S3-C plus a fired
DISP-T is a §2.1 WIN trigger (a closed falsifier campaign) and gets its own
round, assembled by the worker and pasted once.

## §5 — HARDWARE-CORRUPTION GUARD (MANDATORY — Kila6 is unvalidated)

Kila6 has suffered eight unclean shutdowns in 48 hours, cause unresolved, with
**memory never tested**. The Route C integrity sweep verified that files parse
and pair; **it did NOT and could not verify that the arithmetic was correct.** A
memory fault produces silently wrong floats that pass every structural check.

**Therefore, frozen as a campaign requirement:**

1. **Duplicate-seed set.** 16 legs (4 per rung) are designated DUPLICATES and
   run TWICE, in separate invocations separated by at least one machine restart.
   Their `F` arrays must be **BIT-IDENTICAL** across runs.
2. **Bit-identity is a HARD GATE.** Any duplicate pair that is not bit-identical
   **VOIDS THE ENTIRE CAMPAIGN.** No partial rescue, no "exclude the bad leg" —
   a machine that computes non-reproducibly cannot be trusted for any leg,
   including ones whose duplicates happened to match.
3. **The gate is checked BEFORE any statistic is computed.** The analysis refuses
   to report `s(β)` until every duplicate pair has verified.
4. **MemTest86, four passes minimum, is REQUIRED before the campaign is
   accepted** — it may run before or after, but a campaign whose duplicates pass
   while memory is untested is provisional and must be labelled so in any
   downstream use.

Cost of the guard: 16 extra legs ≈ 33 CPU-h ≈ **1.6% of runtime.** It is the
cheapest possible insurance against the one failure mode that would silently
corrupt the physics.

## §6 — RESTART TOLERANCE

Leg-level checkpointing is retained; the campaign resumes after any halt with
only in-flight legs lost. Run under the auto-restart loop. **Machine repairs
(RAM swaps, PSU swap, port changes) are PERMITTED mid-campaign** — the duplicate
gate is precisely what makes that safe, since a hardware change that altered
arithmetic would break bit-identity and void the campaign rather than
contaminate it silently. **Log every hardware change with its timestamp in
`kila6_hardware_log.md`** so any post-hoc question about which legs ran on which
configuration is answerable.

## §7 — Execution

`code/3167_beta_ladder_driver.py --run` (to be written on approval of this
prereg), then `--verify-duplicates`, then `--analyze`. The analyze step refuses
to run if `--verify-duplicates` has not passed.
