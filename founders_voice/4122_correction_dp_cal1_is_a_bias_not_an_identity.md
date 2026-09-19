# 4122 — Founder correction: DP-CAL-1 is a strong bias, not an exact constraint

**Date:** 18 Sep 2026. **Session:** 233. **Patch:** 4122.
**Source:** Thomas's response to the TEST-A3G-1 result (Patch 4121).

**Founder's verbatim:**

> "Note: vacuum-state magnetism should not be exactly zero on a finite scale because of charge
> motion (the origin and essence of inertia/momentum/KE). The helical bit's orientation will be
> most strongly biased antiparallel by its pair, but it will not be exact because of the
> influence of the Di-bits from the DP Sea."

**What it corrects.** Patch 4121 (and DP-CAL-1 as recorded at 4107) treated antiparallel
alignment as an **exact** constraint, giving exactly zero summed axial channel. The founder
rules it is a **strong bias with a residual**: the pair dominates the orientation, the sea's
DI-bits perturb it, and vacuum magnetism is therefore **not exactly zero at finite scale**.

**Consequence.** F2 stops being a binary (exact cancellation vs 2q) and becomes a **bounded**
quantity — see Patch 4122's document. This is a strengthening: a bound is testable where an
identity is not.
