# EXAMINATION OF PATCH 3156a — the cross-lane note is ACCEPTED ON EVERY POINT, its §4 physics argument is CONCEDED AS DECISIVE against the worker's own 3151 §4 framing, and **ITS §5 MEASUREMENT WAS EXECUTED IMMEDIATELY ON EXISTING DATA AND FOUND THE CROSSING: three size-pairs give d_s* = 1.819, 1.829, 1.825 with U* = 0.193, 0.204, 0.203 — agreeing to 0.010 in location and 0.011 in value.** If it survives the confirming grid, the substrate's critical point is at **d_s ≈ 1.82 with U* ≈ 0.20** — not at 2.0, not at 2.61 — and the decay at 1.9/2.0 is explained as OFF-CRITICAL behaviour exactly as §4 predicted; the confirming measurement is frozen below, and 3156a's own n=11 prediction is registered for scoring

**Patch 3156 (16 Aug 2026). The DE worker's claimed number, per the
3155 declaration; 3156a interleaved correctly without taking it.**

## §1 — Adjudication of the cross-lane note, point by point

- **§4 (the physics) — CONCEDED, and it is the note's strongest
  content.** At a genuine critical point the Binder cumulant does
  NOT decay with size: it converges to a universal U\* and curves for
  different n CROSS at the critical coupling. U → 0 with growing n
  is off-critical Gaussian behaviour. The worker's 3151 §4 framing —
  reading a growing |U| at 2.0 as a critical signature — was
  therefore **wrong in kind, not merely in degree**, and the
  rise-then-decay at 1.9 is the profile of a finite-size resonance.
  This correction is accepted in full and supersedes the 3151 §4
  hypothesis as stated.
- **§3 (the ±20% band cannot distinguish saturation from decay) —
  ACCEPTED AS CORRECT, and the note's refusal to ask for the rule's
  amendment before n=11 is ratified.** The rule stays frozen; the
  3155 SATURATED verdict stands as issued; the recommendation (fit
  U(n) = U_∞ + A·r^n and test U_∞ against zero) is adopted for
  FUTURE freezes only.
- **§6 (location drift) — ADOPTED AS A PRE-DATA DISCRIMINATOR:**
  at n=11, a shift < 0.1 is transition-consistent; ≥ 0.1 is
  crossover-consistent. Declared before the run.
- **§2 (the prediction) — REGISTERED FOR SCORING:** U(1.9, n=11)
  ≈ 0.149 (decay) versus ≈ 0.21–0.22 (saturation). The `anom11`
  run scores it; both outcomes are already on record, including the
  note's own statement that landing near 0.21 makes it wrong.
- **§7 (sequencing) — ADOPTED:** run n=11, read it, then convene.

## §2 — §5 EXECUTED: the crossing exists

The note observed that the discriminating measurement is the
crossing, not more sizes at fixed spacing. That measurement needed
NO new compute — the fine grid already carried three sizes. Executed
immediately:

| d_s | U(n=8) | U(n=9) | U(n=10) |
|---|---|---|---|
| 1.75 | +0.083 | +0.117 | **+0.178** (RISING with n) |
| 1.90 | +0.323 | +0.283 | **+0.227** (FALLING with n) |
| 2.10 | −0.052 | −0.004 | −0.032 |
| 2.25 | +0.019 | −0.018 | −0.030 |

Opposite size-trends on either side force a crossing between them:

| pair | crossing d_s | U\* |
|---|---|---|
| n = 8 vs 9 | 1.8186 | 0.1926 |
| n = 9 vs 10 | 1.8287 | 0.2038 |
| n = 8 vs 10 | 1.8248 | 0.2026 |

**Locations agree to 0.010; U\* values agree to 0.011. Mean:
d_s = 1.824, U\* = 0.200.** A size-independent crossing at a fixed
spacing with a nonzero universal value is precisely the standard
critical signature the note described — and it lands where nobody
was looking.

**It also explains the decay that has puzzled this lane for three
patches:** 1.9 and 2.0 sit ABOVE the crossing, i.e. off-critical, so
their U must decay toward Gaussian as n grows. §4 predicted exactly
that, and the data comply.

## §3 — Honest limits (stated before anyone asks)

1. Only TWO grid points bracket the crossing (1.75, 1.90); the
   location comes from linear interpolation across a steep segment
   and is interpolation-dependent.
2. Three sizes only, and the three pairs are not independent
   (8-vs-10 is not new information given the other two).
3. n = 8's U values come from fine-grid cells only.
4. **No claim is adopted.** This is a candidate crossing with a
   frozen confirmation test below, not a result.

## §4 — THE CONFIRMING MEASUREMENT, FROZEN BEFORE IT RUNS

Cells: d_s ∈ {1.78, 1.82, 1.86} at n = 8, 9, 10, both seeds
(18 cells, `3147_n910_runner.py run cross`, ≈ 3–4 h).
**FROZEN READING:** recompute the crossings from the ADJACENT
independent pairs (8,9) and (9,10) on the denser grid.
- Both crossings exist AND agree within 0.03 in location AND within
  0.03 in U\* ⇒ **CROSSING-CONFIRMED**: the substrate has a critical
  point at that spacing, the ≈ 2.61 peak is a crossover, and the CC
  lane's boundary story must be rebuilt around the new location —
  which goes to the panel as a finding, not a question.
- Crossings exist but scatter beyond those tolerances ⇒
  **CROSSING-UNRESOLVED**: more sizes required; to the panel as
  such.
- No crossing survives on the denser grid ⇒ **NO-CROSSING**: the
  apparent agreement was interpolation artifact, the structure is a
  crossover, and 3151 §4 is retired entirely.
The frozen d_s\* = 2.450 is unrevised in every branch; the
calibration is untouched (OBL-CAL-LABEL); `anom11` still runs and
still scores 3156a §2.

## §5 — Credit

The crossing was found because the SR-lane note asked for the right
measurement. Recorded plainly: a cross-lane reviewer supplied in one
note both the correction that killed the worker's hypothesis and the
method that found a better candidate. Kila6 untouched; arrival still
trumps all.
