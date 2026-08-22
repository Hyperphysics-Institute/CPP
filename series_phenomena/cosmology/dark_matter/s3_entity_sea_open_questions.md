# S3 ENTITY-SEA — THE SPECIFIC QUESTIONS NEEDING FOUNDER RULINGS

**Patch 3178, 22 August 2026.** The founder asked to be told specifically
what he must answer before the entity-built Sea (strategy §3, S3) can be
prereg'd. This file is the question list. **It contains no design
decisions — only the questions, why each blocks construction, and what
the worker would default to if the founder declines to rule.**

Reminder of the gate: **S3 does not begin until S1 (the corrected
comparator) and S2 (Phase B's B-4 intermittency verdict) report.** These
questions can be answered at leisure; they are listed now so the founder
can think about them while the machines work.

---

## Q1 — WHAT BINDS AN ENTITY IN THE INSTRUMENT? *(blocks everything)*

The current instrument has no binding mechanism at all: Sea CPs move by
the PCD primitive alone, and pairing is imposed at construction by
placing two opposite charges at separation D0.

Two possible readings of the founder's picture, and they demand
different code:

- **(a) EMERGENT** — entities are what the existing force law *does*
  when CPs are dense enough. Nothing new is imposed; entities form,
  persist, and dissolve under the PCD rule alone.
- **(b) IMPOSED** — entity binding involves something the current force
  law does not contain (a short-range attraction between like-charge
  qCPs, a bond constraint, a saturation), and must be added explicitly.

**Why it blocks:** under (a) the work is a density/initialization study
and may be cheap; under (b) it is a new force law and everything
downstream depends on its form. **This is the single most
decision-blocking question in the list.**

*Worker's default if unruled:* try (a) first, since it adds no physics
and its failure would itself be informative.

## Q2 — ARE THE FOUNDER'S "DM RINGS" THE SAME OBJECT AS THE DM CANDIDATE?

The founder listed **DM rings** among DP-entity types (chains, amorphous
aggregates, ribbons, planes, elements, DM rings). The DM lane's standing
candidate (B) is the **N = 8 closed ring at 11.264 GeV** (CONV-001,
79.5% PROVISIONAL-FAVORABLE).

**Are these the same structure?** If yes, dark matter is not a separate
species but *a particular DP-entity geometry occurring in the Sea*, and
S3's ring case stops being one arbitrary option among four — it becomes
the direct simulation of the candidate. That would be a substantial
conceptual unification and would reorder the whole S3 priority list.

**Why it blocks:** it decides whether chains or rings are built first.

*Worker's default if unruled:* treat them as distinct and build chains
first (the minimal departure from isolated pairs), because assuming the
identification would smuggle in a claim the ledger has not adjudicated.

## Q3 — WHAT SETS ENTITY SIZE?

Entities need a member count. Is it set by (a) a preferred number the
substrate geometry dictates — e.g. N = 8 from the closed-ring work, or
something from the 600-cell; (b) a free parameter to be scanned; or
(c) an emergent outcome of density and temperature that must not be
imposed at all?

**Why it blocks:** (c) is only available if Q1 = EMERGENT.

*Worker's default:* scan a small ladder, N ∈ {2, 4, 8, 16}, with N = 2
reproducing the current isolated-pair Sea as the regression case.

## Q4 — IS ZBW EXPLICIT IN TIME, AND WHAT IS ITS PERIOD IN MOMENTS?

The current Sea's "jitter" is a **static** offset drawn once at
construction — a frozen surrogate for oscillation. The founder's picture
requires ZBW to be an ongoing cycle that ejects CPs.

Does S3 need **explicit time-dependent ZBW**, and if so, what sets its
period relative to a Moment? Sub-Moment (unresolvable, and only its
average enters), one Moment, or many Moments (resolvable, and then the
instrument can see the cycle)?

**Why it blocks:** intermittency — the effect S3 exists to capture —
cannot appear at all if the cycle is unresolvable in time.

*Worker's default:* many-Moment period, ~8–16 Moments, chosen so the
cycle is resolvable at the campaign horizons already in use.

## Q5 — WHAT IS THE EQUILIBRIUM FREE FRACTION, AND IS f_b THE SAME NUMBER?

Phase A used **f_b = 0.47** as the bound fraction, taken from the DE
lane's eight-size campaign. The founder's picture has an equilibrium
ratio of DP entities to free DPs set by temperature and density.

**Is f_b the entity-bound fraction, or a different quantity?** The DE
lane measured pairing, not entity membership — a DP can be paired yet
not belong to any entity. If they differ, S3 needs a second order
parameter, and Phase A's decomposition means something narrower than it
currently reads.

**Why it blocks:** it decides whether S3 can inherit a measured number
or must introduce a new free one — and a new free parameter in a
zero-parameter programme is a significant cost.

*Worker's default:* treat f_b as pairing only, introduce entity
membership as a separate scanned fraction, and state plainly that it is
not yet measured.

## Q6 — STATIC OR DYNAMIC EXCHANGE FIRST? *(cost question, deferrable)*

A static entity Sea (fixed membership, no formation or dissolution)
costs the same per leg as today. A dynamic one adds a
formation/dissolution step every Moment and may run several times
slower.

*Worker's default:* static first — it isolates the effect of binding
from the effect of exchange, and either result narrows the next step.
The founder may overrule if he judges that exchange is the essential
physics and a static entity Sea would be a misleading halfway house.

---

## LANE BLOCK REGISTRY (founder ruling, 22 Aug 2026)

| Lane | Blocks | Status |
|---|---|---|
| Cosmology (DM + DE + jitter) | **3100–3199** | 3160–3178 used; 3179–3199 free |
| Cosmology (reserved) | **3400–3499** | **RESERVED this patch**; entirely free; opens when 3199 is consumed |
| GR | **3300–3399** | in use by the GR arc |

Rules registered at Patch 3177 and restated: lane is chosen by where the
work lands, not by which session writes it; each lane's "Next patch"
pointer advances only its own counter; cross-lane work takes the number
of the lane whose claims it moves, cross-referenced in the other; the
frontier stays in DATE order, so out-of-sequence numbers stacked
together are expected, not errors. Verified free at this patch: 3400,
3401, 3450, 3499 return zero hits across the full log.
