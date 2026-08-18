# DE LANE RESUMED — THE f_b FIRST-MOMENT n-SCALING MEASUREMENT

**Patch 3166, 17 August 2026. VideoCPU. Economy-rule disposition: NO PANEL
ROUND** — this measurement was **already specified by the panel** at CONV-022
and its execution is a §2.3 standing item, not a new question.

---

## §1 — WHY THIS IS A RESUMPTION, NOT A REVIVAL

CONV-022 Q6 went 4–1 THE LANE YIELDS. **Q7 records what the yield was for:**
*"record the outcome, archive, release the machine to the dark-matter
campaign."* The yield was a RESOURCE decision, not a scientific one. **Route C
completed on 17 Aug 2026 and the machine contention that motivated the yield no
longer exists.**

CONV-022 Q3 split (PHYSICAL-FEATURE ×2, UNDETERMINED ×2, FINITE-SIZE ×1) ⇒
UNDETERMINED-BY-SPLIT. **Both UNDETERMINED seats named the SAME decisive
measurement**, and the adjudication §3 records it, together with its own verdict
rule:

> measure the n-scaling of the f_b minimum's **location and depth** across sizes
> (and, per Gemini, the anomaly's own susceptibility from first-moment
> variance). A stable limiting location and depth ⇒ PHYSICAL-FEATURE; systematic
> drift toward a size-dependent endpoint ⇒ FINITE-SIZE-EFFECT. **Not launched:**
> Q6 yields the lane... **This is the first item if the lane is ever resumed.**

This patch launches exactly that, with the panel's own verdict rule frozen
verbatim. **No new question is asked and no new statistic is invented.**

## §2 — COMPATIBILITY WITH THE BINDER RETIREMENT (Q2, RESOURCE-BINDING)

CONV-022 Q2 went 3–2 ABANDON-BINDER: the fourth-moment route is **RETIRED
CORPUS-WIDE and unrevivable without a fresh round.** This measurement is
**FIRST-MOMENT ONLY** — f_b's minimum location, its depth, and the variance of
f_b itself. **No Binder cumulant is computed, reported, or referenced as
evidence anywhere in this campaign.** The adjudication §3 explicitly notes the
specified measurement is "compatible with the Binder retirement because it is
FIRST-MOMENT ONLY."

## §3 — WHY THE FIRST MOMENT CAN DECIDE WHAT THE FOURTH COULD NOT

The precision gap is the whole reason the panel chose this statistic:

| | Binder U (RETIRED) | f_b (this campaign) |
|---|---|---|
| moment | fourth | first |
| seed-to-seed scatter, SAME runs | **0.037** mean, 0.103 max | **0.001–0.01** |
| signal the verdict rests on | size-to-size differences ≈ 0.05 | depth change 0.232 → 0.146 = **0.086** |
| signal / noise | **≈ 1.4** | **≈ 9–86** |

The retired route was asked to resolve differences at its own noise floor. The
first moment carries the same physics at 10–60× the precision, measured in the
identical runs.

**A cross-lane note, recorded because the parallel is exact and was not noticed
at the time.** The DM lane's S3-C failure (Patches 3160–3165) has the same
structure: a verdict built on a statistic sitting at its resolution floor, while
a first-moment statistic of far better precision was available in the same data.
DM required that to be discovered; **DE had it identified and the bad route
retired by the panel a day earlier.** The lanes converged on the same
methodological error independently, which is itself evidence the error is
systemic rather than incidental — recorded as a programme finding.

## §4 — THE MEASUREMENT (frozen before the run)

**Instrument:** unchanged. `scripts/3120_ds_indep_campaign.py` via the existing
`scripts/3147_n910_runner.py` cell structure. **Bit-identity of every prior
output key must be regression-verified before any new cell is accepted**
(the 3147/3152 precedent). No dynamics parameter changes.

**Cells:** sizes **n ∈ {7, 8, 9, 10, 11}** — five sizes, the full range already
banked plus n = 11 — over the fine grid **d_s ∈ {1.9, 2.0, 2.1, 2.2, 2.3}**
bracketing the drifted minimum, **both seeds {5, 11}**. Existing cells are
REUSED where already computed (the runner is checkpointed); only missing cells
run.

**Statistics, per (n, seed):**
1. `loc(n)` — the d_s at which f_b attains its minimum, by parabolic
   interpolation on the three lowest grid points (declared now, not chosen
   later).
2. `depth(n)` — f_b at that minimum.
3. `var_fb(n)` — first-moment variance of f_b at the minimum cell (Gemini's
   susceptibility proxy).

Seed agreement reported for all three. **Any quantity whose seed-to-seed
difference exceeds 20% of its size-to-size change is declared UNDERPOWERED and
may not carry a verdict in any direction** (the §9 claim-hygiene rule, and the
gate whose absence caused the Binder failure).

## §5 — FROZEN READINGS (the panel's rule, verbatim)

- **PHYSICAL-FEATURE** — `loc(n)` and `depth(n)` both approach stable limiting
  values across the five sizes (final-step change ≤ 20% of the preceding step,
  in the same direction, for both quantities).
- **FINITE-SIZE-EFFECT** — either quantity drifts systematically toward a
  size-dependent endpoint with no sign of a limit (monotone, non-decelerating
  steps).
- **UNDETERMINED-PERSISTS** — the two quantities disagree (one stabilizes, one
  drifts), or any contributing quantity is UNDERPOWERED.

**Prior knowledge disclosed (anti-extraction):** the location has ALREADY
drifted once, 2.0 → 2.1 at n = 10, and the depth has deepened monotonically
0.232 → 0.186 → 0.165 → 0.156 → 0.146 across n = 5…10. **The worker therefore
expects FINITE-SIZE-EFFECT to be the more likely reading and records that
expectation BEFORE the run.** A PHYSICAL-FEATURE return would be the surprise.

## §6 — EXHAUSTION TRIGGER

UNDETERMINED-PERSISTS only. PHYSICAL-FEATURE and FINITE-SIZE-EFFECT are both
determinate and ride into the next natural bundle (§5 of the economy protocol),
not a dedicated round.

## §7 — WHAT THIS PATCH MAY NOT DO

It may not revive the Binder route in any form. It may not revise the frozen
d_s* = 2.450 (CONV-022: revision requires its own dedicated round). It may not
touch the calibration (OBL-CAL-LABEL in force). It does not re-open Q1's
SUSTAINED-QUANTIFIED challenger value 2.644.

## §8 — Execution

`python scripts/3147_n910_runner.py run fb` on VideoCPU (24 logical cores),
then `analyze`. Checkpointed, resumable, overnight-safe. Estimated ≈ 6–9 h for
the missing cells; most of n = 7–10 is already banked.
