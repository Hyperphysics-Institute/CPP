# STRATEGY — THE KILA6 DM PROBLEM: WHY FIVE CAMPAIGNS FAILED AND WHAT REPLACES THEM

**Patch 3177, 22 August 2026.** Commissioned by the founder ("let me
know when you have developed a strategy for approaching the DM problem
we have been trying to solve with Kila6"). **A strategy document, not a
preregistration — nothing here is frozen and nothing may be executed on
its authority. Each stage below needs its own prereg.**

---

## §1 — THE FIRST MOVE IS NOT A CAMPAIGN

Route C's DISP-I3 signature reads: all five arms FAIL S3-C, universally
and one-directionally, every arm undershooting its band's lower edge,
across geometries x_half 16–32, horizons T_END 104–504, and drives
β ∈ {0.10, 0.60}. That pattern was treated as the arc's central
empirical fact.

**The 3176 audit removes its foundation.** The band was a polarization
amplitude transplanted into a force comparison as though the conversion
factor were 1; the computed factor is ≤ 0.008 (uniform profile) or
exactly 0 (odd profile). **A band too large by ≥ 100× manufactures
universal one-directional undershoot regardless of what the physics is
doing.**

So the honest position is not "five campaigns failed." It is: **we do
not currently know whether they failed.** The measurements exist and are
sound — bit-identity gates passed, memory tested, seeds frozen. Only the
comparator was invalid.

**Therefore stage 1 is a re-read, not a run:**

**S1 — OPEN-BAND-CONV-1, the full-fidelity conversion.** Compute the
axial source force implied by the archived a1 polarization map, under
retardation, at the actual campaign geometries. Then re-compare every
existing arm — Route B, Route C, the β-ladder's four rungs — against the
corrected comparator. **Cost: hours of container compute. No Kila6
time.** Possible outcomes, all informative: the arms were in band all
along (the anomaly dissolves and DISP-I3 must be re-adjudicated); the
arms are above band (a new one-directional signature, opposite in sign,
needing its own account); or the conversion is too uncertain to compare
at all (which retires the comparator permanently and forces stage 2).

**Nothing should run on Kila6 until S1 returns.** Spending three days
improving the precision of a measurement whose comparator is unknown is
the same error at a higher cost.

## §2 — THE INSTRUMENT DIAGNOSIS (independent of §1)

Even with a valid band, the instrument has a structural gap the founder
named directly. The Sea is built as **isolated dipoles with static
jitter**: `rng.uniform(−0.05, +0.05)` on each separation, once, at
construction. Bounded, symmetric, frozen, no tails, no dynamics.

The founder's registered picture is the opposite in three specific ways:

1. **Aggregated, not isolated** — DPs bind into entities (chains,
   ribbons, planes, rings); constituent oscillation is neighbour-coupled
   and stiffer, not independent.
2. **Dynamic populations, not frozen** — ZBW ejects CPs into inter-entity
   space; free DPs form, persist, nucleate new entities; entities
   evaporate under crowding. An equilibrium ratio, continuously
   maintained.
3. **Saltatory, not smooth** — long conservative DP-arc stretches
   punctuated by dominant chance encounters. Intermittent, heavy-tailed
   forcing.

**Why (3) matters most for a response measurement:** intermittent and
smooth driving give materially different response statistics even at
matched variance. This is a mechanism that can produce large
discrepancies, which is exactly what an under-responsive instrument
would look like.

**Corroboration the instruments produced without being told:** Phase A
found the paired Sea contributes ~2% of the fluctuation and the unbound
fraction carries essentially all of it — the decomposition the founder's
picture requires.

## §3 — STAGED CONSTRUCTION (each stage needs its own prereg)

**S2 — Intermittency first, cheaply.** D-JITTER-1 Phase B §B-4 already
tests whether the computed arrival spectrum is intermittent. **That
result gates the expense of S3.** If NEAR-GAUSSIAN returns, the smooth
surrogate is closer to right than the picture suggests and an entity Sea
is a much weaker priority. Free: it rides on VideoCPU work already
chartered.

**S3 — The entity-built Sea (the expensive step, only if S2 supports
it).** Open design questions, all needing founder rulings:
- **Entity geometry.** Chains are cheapest and most anisotropic; rings
  are the DM-relevant structure (the N=8 closed ring at 11.264 GeV is
  the standing candidate); amorphous aggregates are most realistic and
  least controlled. Recommendation: chains first as the minimal
  departure from isolated pairs, so the effect of *binding alone* is
  isolated before geometry is varied.
- **Free-DP seeding.** Static fraction (cheap, tests composition) versus
  dynamic exchange (expensive, tests the founder's equilibrium). Static
  first.
- **Cost.** An entity Sea at matched CP count costs the same per leg;
  a *dynamic* one adds a formation/dissolution step per Moment and could
  be several times slower. Budget honestly before chartering.

**S4 — Both statistics, per the founder's ruling.** Whichever Sea is
built, the response is read in the mean AND in the tails, both
pre-declared, neither selected post-hoc. In an intermittent medium the
signal may live in rare events that averaging destroys; neither the
founder nor the worker claims to know which regime dominates, and the
probe is the point.

## §4 — WHAT THIS STRATEGY DOES NOT ASSUME

It does not assume the DM candidate survives. If S1 shows the arms were
in band all along, the instrument's under-response was never real and
this entire diagnosis is wrong — which is a good reason to run S1 first.
It does not assume the founder's picture is correct; S2 can return
NEAR-GAUSSIAN and damage it. It does not assume an entity Sea will move
the coefficient; the 3176 audit's lesson is that the coefficient
comparison itself may be void.

**Standing ledger untouched: DISP-I3 stands until re-adjudicated;
six of seven; item 1B OPEN; Candidate (B) 79.5%.**

## §5 — RECOMMENDED ORDER

1. **S1** (container, hours) — re-read existing data against a valid
   comparator. **Highest value per unit cost in the whole programme
   right now.**
2. **Phase B / S2** (VideoCPU, chartered, GO given) — in parallel; the
   intermittency verdict gates S3.
3. **β = 0.05 closure** (Kila6, ~3 days) — worthwhile regardless, since
   the scaling arc never touched the invalid band. Runs whenever Kila6
   is free; not blocked by S1.
4. **S3** (Kila6, expensive) — only after S1 and S2 report.
