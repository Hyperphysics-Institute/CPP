# Founder ruling — what makes a group of DPs one entity (26 Aug 2026)

**Captured verbatim per CONV-009. Registered at Patch 3438. Context:
the comoving-build estimator needs to count DP-entities, and the
engine's existing cluster observable is threshold-defined — the same
arbitrariness that returned THRESHOLD-ARTEFACT at Patch 3419.**

---

## The question put to the founder

In the mechanism ruled at 3436 — DP-entities evaporate CPs, those CPs
bind with other CPs to form DPs, those DPs bond into new DP-entities —
what makes a DP-entity *one* entity? Is there a physical criterion
(a binding condition, a coordination number, a closure of the bond
structure) independent of where a distance cutoff is drawn, or is
entity-hood a matter of degree?

## The founder's answer, verbatim

> Good question. I've thought about that. The DP entities (which I
> think you mean) are, at a minimum, 2 qDPs forming an aggregate. I
> think a DP entity is a single entity if it is separated by a space
> that allows thermal agitation and collision.

---

## Two rules extracted

1. **Minimum size.** An entity is **at least 2 qDPs** in aggregate. A
   lone qDP is not an entity. This is a hard floor, not a threshold.

2. **Individuation by collisional separation.** Two aggregates are
   **distinct entities** when the space between them **admits thermal
   agitation and collision** — that is, when the gap is wide enough
   that thermal motion can carry constituents across it and produce
   collisions. Below that, the material is one entity.

**Why this is not the 3417 threshold.** The 3417 cluster observable
cut at fixed fractions of the lattice spacing — 0.5 d_s, 0.7 d_s,
0.9 d_s — chosen for convenience, and the three choices disagreed in
sign. The founder's criterion instead references the **thermal
excursion amplitude**, which is a measured property of the run
(set by the drive, and already instrumented in the engine through
the contact rate R_c and the pair-separation series W). The cut
becomes **derived from the dynamics rather than chosen against the
lattice.**

---

## Consequences, flagged not enacted

**(a) A candidate explanation for the 3419 artefact.** If the physical
individuation scale is the thermal excursion amplitude, then it moves
with temperature — and 3419 scanned temperature across 64× while
holding the cut at fixed fractions of d_s. Each fixed fraction would
then have been wrong in a temperature-dependent and differently-signed
way, which is the shape of the disagreement observed
(p = +0.0593 / −0.0024 / −0.0314). **This is a hypothesis with a
testable consequence, not a finding**: re-cutting the existing
`3418_entity_state.json` at a thermally-scaled criterion would either
collapse the sign disagreement or leave it standing. It is cheap
(the data exists; CONV-036 commits it) and it is **not** authorised
here. Re-opening a frozen conclusion requires its own preregistration,
and the temptation to re-cut data until the signs agree is exactly
what a prereg exists to restrain.

**(b) The volume-dependence question, open.** The comoving instrument
reads `w = −∂ln N_ent/∂ln V`. If the drive is held fixed while d_s
ramps, the thermal excursion amplitude stays fixed while gaps widen,
so more aggregates satisfy the separation criterion at larger V. The
reading of that which I believe is correct: **this is signal, not
contamination.** As the Sea dilutes, aggregates genuinely do come to
be separated by space that admits collision, and genuinely do become
distinct entities. That *is* the founder's mechanism producing new
entities under expansion. But the alternative reading — that the
thermal scale should itself track the expansion, holding the criterion
fixed in relative terms — gives a different instrument and a different
answer. **This is the one remaining fork, and it is the founder's to
settle** (see the question in §Open below).

---

## Open

**Does the thermal agitation scale itself change as the Sea dilutes,
or is it fixed while the spacing grows?** Equivalently: as space
expands, does the amount of thermal jostling available to a CP stay
the same while its neighbours recede — or does the jostling weaken in
step, so that the ratio of gap to thermal reach stays put?

If the scale is fixed and gaps widen, entity number rises with volume
and Λ can hold constant. If the ratio is preserved, entity number is
volume-invariant and Λ falls as 1/V. **The two give opposite
instruments**, so this is asked before the pilot rather than after.
