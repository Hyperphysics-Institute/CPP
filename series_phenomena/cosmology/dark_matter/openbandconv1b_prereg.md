# PREREGISTRATION — **OPEN-BAND-CONV-1b: THE GEOMETRY MISMATCH IN THE WORKER'S OWN 3186 RE-COMPARISON**, and the comparator recomputed on the geometry the campaign arms ACTUALLY USED

**Patch 3187, 22 August 2026. Container. Frozen before recomputation.**

## §1 — The defect, found by the worker one patch after publishing it

3186 compared the β-ladder's measured response against F_MAP computed
on the **2914 symmetric Sea** (`build_sea_sym`, classes A and B,
seeds 4/5/6). **The β-ladder does not use that geometry.** Its driver
(`code/3167_beta_ladder_driver.py` line 138) builds
`build_sea_jittered` — a lattice-filled shell (SPACING grid over
ρ ∈ RHO, x ∈ ±X_HALF = ±28), radial orientation, separations
D0 + uniform(JIT_LO, JIT_HI), per-leg seeds.

**So 3186 §2's "IN-BAND at 1.53×" compared a jittered-Sea measurement
against a symmetric-Sea comparator.** This is the SAME defect class as
the original band transplant (3176): a quantity computed in one
configuration applied to another as though the configurations were
interchangeable. **The worker introduced it while correcting the
original instance of it, and is recording it before anyone else finds
it.** 3186's §1 comparator values are unaffected as *symmetric-Sea*
quantities; only the §2 arm re-comparison is compromised.

**Corroborating evidence that geometry matters here, from 3186
itself:** classes A and B differ by ~5× in F_MAP. If two variants of
the SAME builder differ fivefold, a different builder entirely cannot
be assumed equivalent.

## §2 — Method (frozen)

Recompute F_MAP on `build_sea_jittered` at the campaign's own
parameters (X_HALF = 28.0, the driver's SPACING/RHO/JIT constants,
source at X_SRC0 = −24.0 rather than the origin — the campaign's
actual source placement), for **six independent geometry seeds** drawn
from the driver's own SEEDS array. Same measured 72-bin a1 map, same
per-pair bin lookup by (ξ = centre_x − source_x, ρ), same zero
increment outside the binned domain, same engine force law, same exact
two-member sum.

**DECLARED ASSUMPTION, stated because it cannot be tested here:** the
a1 response profile was MEASURED in the symmetric Sea and is here
APPLIED to the jittered Sea, bin by bin. Whether that profile
transfers between geometries is unknown; this patch tests the
*conversion*, not the *transfer*. **If the two geometries give
materially different F_MAP, the transfer assumption becomes the
dominant open uncertainty and must be named as such in every
downstream use.**

## §3 — Frozen statistic, floor, falsifier

- **Statistic:** F_JIT(β) for β ∈ {0.05, 0.10, 0.20}, mean over six
  seeds, engine force units.
- **Floors, both reported:** across-seed SE, and the archive's
  per-bin `se` propagated as at 3186.
- **Falsifier:** floors disagreeing by > 3×, or sign unstable across
  seeds ⇒ **UNSTABLE**, no arm comparison at that β. (Identical rule
  to 3185 §3 — deliberately unchanged, so the two geometries are
  judged by the same standard.)

## §4 — Frozen readings

Per β whose comparator is USABLE, the matched arm is IN-BAND iff
|measured| ∈ [F_JIT/2, 2·F_JIT]; else ABOVE/BELOW with ratio quoted.
Aggregate over admissible arms only, and **the aggregate reading is
declared ONLY if at least three arms are admissible** — the sample-of-
one refusal at 3186 §2 is hereby generalized into a standing minimum,
so that a favourable single arm can never carry an aggregate verdict.

**Additionally frozen: 3186 §2's IN-BAND result is WITHDRAWN as an
arm comparison regardless of what this patch returns** — it compared
mismatched geometries and cannot be repaired by a later number
agreeing with it.

## §5 — Hazard direction (declared)

If F_JIT ≈ F_MAP, 3186's arithmetic survives its own geometry error
and the β = 0.10 arm is IN-BAND on a valid comparison. If F_JIT
differs materially, the corrected comparator changes again and the
anomaly's status changes with it. **Worker's pre-declared
expectation: F_JIT will differ from F_MAP by more than 2×**, because
the jittered Sea is far larger (x ∈ ±28 vs the 2914 shell), the
source sits at −24 rather than at the centre, and A-vs-B already
showed 5× sensitivity. Recorded before the number exists; the
worker's last three pre-declarations scored WRONG, NOT-CONFIRMED, and
UNSCORED.
