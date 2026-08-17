# PRE-REGISTERED PREDICTION FOR n=11 — filed CROSS-LANE before the run (Patch 3156a)

**Filed by the SR-lane worker into the DE lane at founder direction
(16 Aug 2026), under CONV-022.** Number `3156a` uses the alpha-suffix
convention (Patch 0481M precedent) **deliberately, not as collision recovery**:
Patch 3155 declared "Next patch: 3156," so 3156 is claimed by the DE worker.
This note interleaves without taking it.

**Status of this note: ADVISORY. It mandates nothing.** The DE worker and any
panel retain full authority over the lane. Nothing here asks for the frozen
n=11 rule to be changed — see §3, which argues the opposite.

**Read before the n=11 spot-check is interpreted.**

---

## §1 — The numbers on record

U(1.9) by size, from Patches 3153–3155:

| n | U(1.9) | decrement | fractional step |
|---|---|---|---|
| 7 | +0.001 | — | — |
| 8 | +0.323 | — (onset) | — |
| 9 | +0.283 | −0.040 | −12.4% |
| 10 | +0.227 | −0.056 | −19.8% |

**The decrements are growing by a factor of 1.40 per step** (0.056 / 0.040).
That is accelerating decay, not approach to a plateau.

## §2 — The prediction, declared before the run

Propagating the 1.40 decrement ratio:

| n | predicted U(1.9) under ACCELERATING DECAY | under GENUINE SATURATION |
|---|---|---|
| 11 | **≈ 0.149** (decrement 0.078, step **−34.5%**) | ≈ 0.21–0.22 (decrement shrinking) |
| 12 | ≈ 0.039 | ≈ 0.21 |
| 13 | **zero crossing between n=12 and n=13** | ≈ 0.21 |

**The two hypotheses are cleanly separable at n=11.** A −34.5% step falls
*outside* the frozen ±20% band and reads NON-MONOTONIC under the existing rule;
saturation reads SATURATED. One point decides it.

**If U(11) lands near 0.149, this note is confirmed. If it lands near 0.21–0.22,
this note is wrong and the saturation reading is strengthened by a prediction
that failed against it.** Both outcomes are declared here in advance.

## §3 — The methodological point — and why the rule must NOT be changed now

The ±20% fractional-step band **cannot in principle distinguish saturation from
decay**, because these are different questions. Saturation asks whether a
sequence converges to a *nonzero* limit. A step-size threshold asks only whether
the latest change was *small*. A quantity decaying geometrically toward zero
produces small fractional steps at every stage and will keep reading SATURATED
until it reaches zero. The rule is therefore biased toward the verdict it
returned at 3155.

**This is not a request to change the rule before n=11.** Amending a frozen
criterion after seeing the data it was frozen against destroys the value of
freezing it, and the 3155 verdict was reported with exemplary honesty — a
0.23-percentage-point margin called a coin-on-edge, and the fixed-location claim
withdrawn by the worker against its own prior patch. The bias is real and the
verdict still stands as issued.

**Recommendation for FUTURE freezes only:** replace the fractional-step band
with a convergence test — fit U(n) = U_∞ + A·r^n and ask whether U_∞ is
distinguishable from zero at the achieved precision. That tests the actual
question.

## §4 — The physics argument, which is stronger than the extrapolation

At a genuine critical point the Binder cumulant does **not** decay with system
size. It converges to a universal fixed value U\*, and curves for different n
**cross at the critical coupling** — that crossing is the standard signature.
U → 0 with growing n is the *off-critical, Gaussian* behaviour.

The observed sequence at d_s = 1.9 — absent at n=7, spiking at n=8, then
declining monotonically at 9 and 10 — is not the profile of a critical point. A
rise-then-decay is the profile of a finite-size resonance or commensuration
effect that peaks when the system size matches some length and washes out as the
system grows past it.

**This predicts the decay continues, and it is why §2 favours decay over
saturation.**

## §5 — A better measurement than more n at fixed d_s

If d_s = 1.9 is off-critical, adding sizes there measures the approach to zero
and little else. The discriminating measurement is **the crossing**: across the
d_s grid, look for a spacing at which U(n) is *size-independent* — where the
n=8, 9, 10 curves intersect. That location, if it exists, is the critical
spacing; if no crossing exists anywhere on the grid, there is no critical point
in the window and the structure is crossover, which settles the question the
programme has been circling since 3151.

Offered for the DE worker's and the panel's consideration; not a mandate.

## §6 — On the location drift 2.0 → 2.1

The 3155 withdrawal of the fixed-location claim was correct. But it should
**not** be over-read as evidence against a transition: pseudo-critical locations
genuinely do drift with system size, scaling as n^(−1/ν). What distinguishes a
transition from a crossover is that the drift *shrinks toward an asymptote*
rather than wandering. One step cannot tell which.

**Discriminator at n=11: the SIZE of the next shift, not its direction.**
A shift smaller than 0.1 is transition-consistent; a shift of 0.1 or larger is
crossover-consistent.

## §7 — Note on the proposed panel

A panel convened *after* this note is on record adjudicates a falsifiable claim
with a number attached, rather than an impression. Recommended sequencing: run
n=11, read it against §2 and §6, **then** convene. The panel is materially
better informed for costing one run.

---

*Filed under PD-006. Physics-picture authority remains the founder's; lane
authority remains the DE worker's.*
