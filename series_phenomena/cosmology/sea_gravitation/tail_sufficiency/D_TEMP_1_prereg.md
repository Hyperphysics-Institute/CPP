# PREREGISTRATION — **D-TEMP-1: MEASURE p = d ln n_eq / d ln T, THE ONE NUMBER THAT FIXES w** — with a FULL DISCLOSURE that the worker has already seen a two-point estimate in existing data, so this run is NOT blind and is scored accordingly

**Patch 3414, 23 August 2026. Frozen before the campaign runs.**

## §1 — The temperature knob, identified

The instrument's dynamics are **overdamped**: X ← X + F each Moment,
with no velocity state. In overdamped Langevin dynamics the noise
amplitude IS the temperature: **T ∝ σ_n².** So the knob has existed
all along — **INV-SENS (3131) simply never turned it far enough.**

**Why INV-SENS saw nothing:** 3181 measured a SELF-GENERATED ambient
field at σ_amb ≈ 0.27 that persists at ZERO drive. Across
σ_n ∈ [0.05, 0.45] the injected term never dominates that floor, so
the TOTAL kinetic scale barely moved — **the Sea was never actually
heated.** That is a defect in the earlier range, not evidence of
temperature-insensitivity.

## §2 — What is measured

At fixed spacing d_s = 4.636, n = 5, seeds {5, 11}: the equilibrium
**bound-entity concentration proxy n_eq ∝ f_b** (bound pairs per unit
volume at fixed d_s), across **σ_n ∈ {0.15, 0.30, 0.60, 1.20}** — a
**64× range in T**, deliberately spanning from below to well above the
0.27 floor.
**p ≡ d ln f_b / d ln T = 2 · d ln f_b / d ln σ**, by least squares in
log-log, reported **twice**: over all four points, and over the upper
three (σ ≥ 0.30) where the injected term dominates the floor.

## §3 — FROZEN READINGS

**w = −1 + p/3**, then:
- **PHANTOM** iff w < −1.005 (ρ_Λ rises as the universe cools)
- **LAMBDA-LIKE** iff |w + 1| ≤ 0.005
- **QUINTESSENCE** iff w > −0.995 (the DESI-preferred direction)
Reported in every branch: both p estimates, their difference (a
linearity check), and the implied w to three decimals.

## §4 — DISCLOSURE: THIS RUN IS NOT BLIND

**The worker has already seen two relevant numbers.** D-TAIL-1's power
gate (3193) measured f_b = 0.44479 at σ = 0.30 and 0.40608 at
σ = 0.45. **That pair implies d ln f_b/d ln σ ≈ −0.22, hence
p ≈ −0.11 and w ≈ −1.04 — PHANTOM, and OPPOSITE to the founder's
stated sign** (hotter ⇒ denser ⇒ p > 0).

**Consequences, declared now:**
1. **The worker's expectation (PHANTOM) cannot be scored as a
   prediction** — it is an extrapolation of data already in hand.
2. **What this run genuinely tests is the RANGE and the LINEARITY:**
   whether p holds over 64× in T rather than 2.25×, and whether the
   two estimates in §2 agree. **A p that changes sign or magnitude
   across the range would falsify the two-point extrapolation.**
3. **The reading thresholds are set from observational relevance**
   (±0.005 in w is far below current sensitivity), **not from the
   anticipated value.**

## §5 — Hazard, stated plainly

**If p < 0, the founder's stated sign is WRONG and the mechanism
predicts PHANTOM — the same side as the retired HDE overlay and the
OPPOSITE side from the DESI-preferred w₀.** That would remove the one
directional advantage identified at 3413 and leave CPP's native
prediction pointing where the data disfavour.
**If p > 0**, the founder's sign is confirmed and CPP has a
distinguishing prediction in the preferred direction.
**Either outcome is decisive for the lane**, and the proxy caveat in
§6 applies to both.

## §6 — The proxy caveat (load-bearing, stated before the result)

f_b counts **bound PAIRS at fixed lattice spacing**; the founder's
n_eq counts **DP ENTITIES** (aggregates: 2DP pairs, ribbons, amorphous
clusters). **These are not the same quantity**, and the instrument
models no aggregates. **Whatever this run returns, it constrains the
pair-level proxy, and its transfer to entity-level concentration is
an assumption the corpus has not tested.** Nothing here may be quoted
as an entity-level result.
