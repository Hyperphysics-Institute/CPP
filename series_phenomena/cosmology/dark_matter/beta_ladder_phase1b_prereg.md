# PREREGISTRATION — β-LADDER PHASE 1B: THE β = 0.05 UNDERPOWER CLOSURE

**Patch 3180, 22 August 2026. Kila6. FROZEN BEFORE ANY PHASE 1B LEG
EXISTS.** Chartered by `kila6_dm_strategy_3177.md` §5.3 ("worthwhile
regardless, since the scaling arc never touched the invalid band; runs
whenever Kila6 is free; not blocked by S1"). Executes under the
strategy's own rule that each stage needs its own preregistration.

---

## §1 — WHAT THIS CAMPAIGN IS FOR, AND WHAT IT MAY NOT TOUCH

Phase 1 (Patch 3175) returned **BETA-UNRESOLVED** for one identified
reason: the β = 0.05 rung's own 99% CI spanned zero
([−1.467e-04, 5.958e-04]), so the frozen ratio `s(0.20)/s(0.05)` admitted
a zero denominator and its interval diverged to [−222, +188]. The
analyzer's own required-N estimate from the measured scatter was
**≈ 685 pairs/rung**.

**Phase 1B raises N at β = 0.05 from 128 to 685 and re-reads the frozen
Phase 1 readings. Nothing else changes.**

**Explicitly OUT OF SCOPE, frozen:**
- **The ratio endpoints stay `s(0.20)/s(0.05)`** with reference values
  1.0 and 4.0. Phase 1's record named re-siting them as forbidden
  extraction; that prohibition binds this campaign too. A ratio built on
  `s(0.20)/s(0.10)` — which existing data would already resolve — is NOT
  computed, NOT reported, and NOT used.
- **The statistic is unchanged**: the 3164 Route B recipe verbatim,
  `sust_B = D[LATE(216:264)] − D[PRE(12:24)]`, SIGNED, bootstrap 10000,
  seed 30530811.
- **The β = 0.10, 0.15, 0.20 rungs are NOT re-run and NOT extended.**
  Their m stays 128. Phase 1's legs for those rungs are reused byte-for-
  byte.
- **THE COEFFICIENT READING IS SUSPENDED.** Patch 3176 established that
  `SUST_REF = 0.026·β` is a polarization amplitude transplanted into a
  force comparison with an implied conversion factor of 1, while the
  computed factor is ≤ 0.008 or exactly 0 by profile. **The comparator is
  VOID pending OPEN-BAND-CONV-1.** This campaign fires no
  COEFFICIENT-OVERPREDICTED flag and makes no coefficient claim in either
  direction; `--analyze` prints the k column as diagnostic arithmetic
  with the void label attached. The 3175 coefficient finding remains
  RETRACTED, not revived by more data.
- **No tree movement.** DISP-I3 stands until re-adjudicated; item 1B
  OPEN; Candidate (B) 79.5%; the frozen tree is not re-run.

## §2 — DESIGN (frozen)

- **Rung extended:** β = 0.05 only. Pairs **128 … 684** added (557 new
  pairs × 2 branches = **1,114 new evidentiary legs**).
- **Seed table extension, verified:** `SEEDS = default_rng(31670817)
  .integers(1e6, 1e7, size=685)`. Numpy draws sequentially, so the first
  128 entries are **bit-identical** to the Phase 1 `size=128` table —
  verified before freezing (`prefix identical: True`, 685 unique seeds).
  Phase 1's β = 0.05 legs therefore remain valid members of the extended
  ensemble and are NOT recomputed.
- **Geometry, horizon, engine: unchanged.** x_half = 28.0,
  x_src0 = −24.0, T_STEP = 24, T_END = 264, the committed 3055 `run_leg`,
  the 2902 engine, BLAS pinned to 1 thread.
- **Cost:** 1,114 legs × ~7,700 s ÷ 32 workers ≈ **74.5 h ≈ 3.1 days**.
- **Mixed-m disclosure:** the ratio will compare a rung at m = 685
  against a rung at m = 128. This is legitimate because the analyzer
  already bootstraps each rung independently over its own pairs; it is
  recorded here so no reader discovers it in the output. The β = 0.20
  rung's precision is unchanged and is not the binding constraint — its
  CI already excludes zero comfortably.

## §3 — CORRUPTION GUARD (unchanged in kind, new in membership)

- **Duplicate set, FROZEN:** pairs **{128, 684}** × branches
  {step, ctrl} at β = 0.05 = **4 legs**, second copies produced by
  `--run-duplicates-1b` in an invocation separated from `--run-1b` by at
  least one machine restart.
- **Bit-identity:** element-exact float64 equality of the full `F` and
  `AB` arrays. **Any mismatch VOIDS Phase 1B entirely** — no partial
  rescue. Phase 1's own gate result stands independently and is not
  disturbed by a Phase 1B void.
- `--analyze-1b` **REFUSES** unless `duplicates_1b_verified.json` reads
  PASS.
- MemTest86 (4 passes, 0 errors, 18 Aug 2026) already satisfies the §5.4
  acceptance condition; Phase 1B is not provisional. **Core Temp must
  remain uninstalled for the duration** (H-CORETEMP, `kila6_hardware_log.md`)
  — a second clean multi-day run is the registered test of that
  hypothesis, and running Core Temp would forfeit it.

## §4 — FROZEN READINGS (mechanically identical to Phase 1 §3)

Computed once, at N = 685, after the gate passes:

- **BETA-LINEAR** — through-origin fit consistent with all four rungs
  AND ratio 99% CI contains 4.0 excluding 1.0.
- **BETA-FLAT** — ratio CI contains 1.0 excluding 4.0.
- **BETA-SUBLINEAR** — ratio CI excludes both; log-log exponent reported,
  no band re-sited.
- **BETA-UNRESOLVED** — ratio CI contains both. **If this returns again:
  report the new required-N estimate and STOP.** No further extension may
  be launched without a fresh preregistration. Optional stopping —
  running until the interval happens to fall the wanted way — is
  forbidden, and this clause exists to make that explicit before the data
  can tempt anyone.

**Pre-declared expectation, recorded before any Phase 1B leg runs:** the
worker expects **BETA-LINEAR**. This REVERSES the Phase 1 pre-declaration
(BETA-FLAT or SUBLINEAR) and the reversal is recorded as a reversal: the
Phase 1 through-origin fit passed at k_hat = 7.37e-03 consistent with all
four rungs, and the three upper rungs rose monotonically. The worker's
earlier expectation was wrong and is not carried forward pretending
otherwise. **A BETA-FLAT return would now be the surprise.**

## §5 — HAZARD DIRECTION (stated, unchanged)

BETA-LINEAR does not rescue Candidate (B) and is not sought for that
purpose. It establishes that the instrument's sustained response scales
with drive — an instrument property. What the arm's magnitude means
cannot be judged until OPEN-BAND-CONV-1 supplies a valid comparator; the
3176 audit removed the old one. **A scaling result with no valid
comparator is an instrument fact, not a physics verdict**, and this
prereg forbids reporting it as more.

## §6 — EXECUTION (Kila6)

```
cd ~/Documents/GitHub/CPP/series_phenomena/cosmology/dark_matter
python code/3167_beta_ladder_driver.py --calibrate-1b     # arithmetic only
python code/3167_beta_ladder_driver.py --run-1b           # ~3.1 days, resumable
#   ---- machine restart ----
python code/3167_beta_ladder_driver.py --run-duplicates-1b
python code/3167_beta_ladder_driver.py --verify-duplicates-1b
python code/3167_beta_ladder_driver.py --analyze-1b
```

No analysis of any kind may be run against partial Phase 1B data. The
driver enforces this: `--analyze-1b` refuses unless all 1,370 β = 0.05
legs (685 pairs × 2 branches) are present AND the duplicate gate reads
PASS.
