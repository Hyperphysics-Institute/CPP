# EXECUTION RECORD — AUTOMATON MOVING-SOURCE LW TEST

**Patch 2886. Bands frozen at Patch 2885, committed BEFORE this run; the
ordering is verifiable in `git log`.**

# VERDICT: **INCONCLUSIVE** — on two independent pre-registered grounds.

**The worker predicted NON-LW in the prereg (§2) and the raw numbers point
that way. The frozen criteria do not permit the claim. Reported as
inconclusive.**

---

## §1 — RESULT

Engine: committed `2802_automaton2_engine.py`, functions only. M = 48,
R = 4 (the ratified G1 configuration). Relay propagation speed **measured
from the kernel itself rather than assumed**: mean euclidean front radius
**c_lat = 4.0384 units/Moment** over a 266-site front.

Discriminant **A = (x_aim − x_src)/(β·r)**. LW ⟹ A → 0. Fully retarded
⟹ A → −1.

| β | r = 4 | r = 6 | r = 8 |
|---|---|---|---|
| 0.10 | −0.3907 | −1.6668 | −2.6548 |
| 0.20 | −0.3420 | −1.9677 | −1.3872 |
| 0.40 | −0.3522 | −1.3223 | −0.4607 |

Mean A = **−1.1716**. Spread/mean = **0.675**.

## §2 — WHY INCONCLUSIVE, AGAINST THE FROZEN BANDS

**FAILURE 1 — LINEARITY.** The prereg froze: *"A must be approximately
β-independent (spread < 30% of the mean)… forces INCONCLUSIVE regardless
of the value of A."* Measured spread is **67.5%**, more than double the
declared limit.

**FAILURE 2 — THE RETARDED BAND IS NOT MET.** The prereg required
**A < −0.50 at every tested β, at ≥ 2 of 3 radii.** At β = 0.10 and
β = 0.20 that holds (2 of 3 each). **At β = 0.40 only 1 of 3 radii
qualifies** (r = 6 alone). The band fails on its own terms.

**What is nonetheless factually true, and is NOT a verdict:** all twelve
measurements are negative, and the closest approach to the LW band
(|A| < 0.15) is −0.342 — more than twice the band edge. **Per the frozen
linearity clause this does NOT license concluding non-LW**, because a
β-dependent artifact can produce a consistent sign while carrying no
information about structure. **That clause was written precisely to
prevent the worker from banking this pattern, and it is doing its job.**

## §3 — OBSTACLE DIAGNOSED

The r = 4 column is strikingly **stable** across a 4× range in β
(−0.391, −0.342, −0.352 — spread ≈ 6%). The r = 6 and r = 8 columns
scatter by a factor of ~2 and drive the entire linearity failure.
**The instability is radius-dependent, not β-dependent in origin.** Three
candidate causes, in order of suspicion:

1. **Periodic wrap-around contamination.** M = 48. At β = 0.40 the source
   advances 1.615 units/Moment over 40 Moments ≈ 65 units, **traversing
   more than one box length**, so the test points at r = 8 are plausibly
   sampling periodic images of the source and of its own wake. This would
   hit large r hardest and β = 0.40 hardest — **exactly the observed
   pattern.**
2. **Integer rounding of test points.** Field values are read at
   `round(p) % M`; the true test point sits at fractional offsets
   r/√2 = 2.83, 4.24, 5.66. The rounding error is a fixed lattice
   fraction, so it degrades the aim-point extrapolation differently at
   each radius.
3. **Fore/aft averaging.** The run averages test points placed both ahead
   of and behind the source. Those two placements have different
   systematics under retardation and should not have been pooled.

## §4 — WHAT WOULD RESOLVE IT (not run here)

- **M = 96 or larger**, so no test point is within a box length of an
  image, and a motion phase short enough that the source does not wrap.
- **Trilinear interpolation of the field at test points**, matching the
  trilinear deposition already used for the source, removing cause 2.
- **Report fore and aft separately** rather than pooled, removing cause 3.
- Re-freeze bands unchanged and re-run. **The bands are NOT to be
  widened**; the prereg forbids re-banding after an inconclusive result.

## §5 — STANDING

**CONJ-FP-1 Condition B remains OPEN.** It is neither confirmed nor
refuted, and the substrate-viability escalation of Patch 2884 — that an
LW-like relay would forbid coasting entirely — **remains live and
unresolved.**

Nothing here touches the dark-matter ledger: 1B OPEN; PR7 PARTIAL; six of
seven; B7 holds DM-1/DM-2/DM-3; Candidate (B) 79.5%.
