# **OPEN-BAND-CONV-1 EXECUTED — THE COMPARATOR IS COMPUTED, AND IT IS ~4–9× SMALLER THAN THE TRANSPLANTED BAND, NOT 130–963× SMALLER**: F_MAP = 1.39e-04 (β = 0.05), 5.97e-04 (β = 0.10), 8.22e-04 (β = 0.20) from the MEASURED 72-bin map — **so the single admissible arm, the β = 0.10 rung at 9.14e-04, is IN-BAND at 1.53×**, where 3176's assumed-parity bounds had placed it 45–340× ABOVE; the frozen aggregate reading is NOT declared, because only ONE arm is admissible and the rule requires a majority — **and the β = 0.20 comparator fired the prereg's own UNSTABLE falsifier, for an informative reason: the six geometries split into TWO CLASSES differing ~5× (A ≈ 2.3e-4 vs B ≈ 4.5e-5 at β = 0.05), so "floor 1" is a SYSTEMATIC class spread, not statistical noise, and a single scalar comparator conflates two physically distinct geometries**

**Patch 3186 (22 Aug 2026). Executes `openbandconv1_prereg.md`
(Patch 3185, committed BEFORE this computation ran — the freeze is in
the git history). Container only; no engine legs, no Kila6 time.**

## §1 — The comparator, at full fidelity

| β | F_MAP | floor 1 (geometry SE) | floor 2 (archive se) | ratio | sign | §3 verdict |
|---|---|---|---|---|---|---|
| 0.05 | **1.3905e-04** | 4.20e-05 | 8.58e-05 | 2.04 | STABLE | **USABLE** |
| 0.10 | **5.9711e-04** | 1.96e-04 | 6.86e-05 | 2.86 | STABLE | **USABLE** |
| 0.20 | 8.2175e-04 | 2.18e-04 | 4.96e-05 | **4.39** | STABLE | **UNSTABLE** ⇒ no comparison |

360 of 432 pairs fall inside the binned domain; the remaining 72 take
zero increment, per §2.2 (assuming otherwise would re-import the very
error 3176 caught).

**The transplanted band 0.026·β exceeds F_MAP by 9.3× (0.05), 4.4×
(0.10), 6.3× (0.20).** 3176's assumed-parity bounds gave ≥130×–963×
— they were bounds under a *guessed* profile, and the measured
profile lands far above the odd-parity cancellation they feared. **The
audit's direction was right; its magnitude was wrong by one to two
orders, and the correction runs against the worker's own earlier
number.**

## §2 — The re-comparison the prereg permits

Admissible only at β whose comparator passed §3, against arms with a
measurement excluding zero:
- **β = 0.10 rung, measured 9.14e-04 vs band [2.99e-04, 1.19e-03]:
  ratio 1.53× ⇒ IN-BAND.**
- β = 0.15 rung: no map at that β ⇒ no comparison.
- β = 0.20 rung: comparator UNSTABLE ⇒ no comparison (frozen).
- β = 0.05 rung: CI spans zero (Phase 1 underpower) ⇒ nothing
  admissible to compare.

**AGGREGATE READING: NOT DECLARED.** §4 requires a majority of arms;
exactly one is admissible. **ANOMALY-DISSOLVES is not claimed on a
sample of one** — though the single admissible arm points that way,
and the worker's §5 pre-declaration (INVERTS or DISSOLVES) is
therefore **partially borne out but NOT scored**, since no aggregate
reading exists to score it against.

## §3 — The finding inside the falsifier

The per-geometry values are not scattered — they are **bimodal**:
(β = 0.05) +2.33e-04, +2.33e-04, +2.33e-04, +4.49e-05, +4.54e-05,
+4.50e-05. Three class-A geometries agree to three digits; three
class-B geometries agree to three digits; **the two classes differ by
~5×.** The same split appears at every β.

So "floor 1" was never a statistical error bar — **it is a systematic
class difference**, and the β = 0.20 UNSTABLE verdict fired because
that systematic exceeded the archive's statistical floor by 4.4×.
**The frozen falsifier did its job and taught us something: a single
scalar comparator conflates two physically distinct Sea geometries.**
The honest successor is a **class-resolved comparator** (F_MAP^A,
F_MAP^B), which would very likely be stable at every β — **but that
requires its own freeze and its own arm-matching, and is NOT applied
here.** The β = 0.20 comparison stays refused.

## §4 — What this does and does not move

- **DISP-I3 is NOT re-adjudicated here.** Its basis remains in
  question (3176), and this patch supplies a comparator that is
  valid at two βs and class-conflated at all of them.
- **COEFFICIENT-OVERPREDICTED stays SUSPENDED** (3176), per §6 of the
  prereg. Note without adopting it: against F_MAP the measured
  response is ~1.5× above, not 3.5× below — the direction of the
  original finding remains inverted, but no counter-claim is minted
  on one arm.
- **The strategy's S1 is DISCHARGED in substance:** the comparator
  exists, is computable from archived data, and is far closer to the
  measurements than either the transplanted band or the audit's
  bounds suggested.
- **S3's gate is now clear on both prerequisites** (S1 here, S2 at
  3183/3184) — but the class-split finding above is the first thing
  any S3 design must absorb.
- Kila6 untouched; the β-ladder outranks all of this.
