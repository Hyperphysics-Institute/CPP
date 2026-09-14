# 0964 — R-1 hostile pass on piece 1: all three checks clear, one reviewer trap found in our own corpus

**Patch:** 0964, 13 Sep 2026. **Lane:** chirality (09xx). **Verify:** `chirality_derivations/code/0964_piece1_hostile_pass.py` (6/6). **Type:** R-1 pre-dispatch hostile pass. **No claim registered, no verdict moved, piece 1 still formally open.**

This is R-1 (Patch 0959) being applied for the first time: run the tests an adversarial reviewer would demand **before** dispatching, rather than discovering them mid-campaign as happened through CONV-047/048.

---

## Check 1 — does anything in the corpus produce non-unit weights?

**No.** Searched every η construction in the sub-corpus. All three — 0819, 0820, 0821 — weight each edge by `sign det[d̂, n̂, r̂₁, r̂₂]`. Unit magnitude throughout.

**0820 already states the conclusion**, which 0963 did not surface. Its coarse-graining note §(1) and §(3):

> *"(1) The CANONICAL local enantiomorph = orientation of the WHOLE vertex figure (icosahedron of 12 neighbours) — a SYMMETRIC function reading all 12 incident edges with equal weight. Reading-weight participation ratio = 12 (uniform) ⇒ m_eff = 12, by construction."*
>
> *"(3) The Mechanism-A bias (delta e.n) shifts edge MEANS (the tilt…) but leaves the reading WEIGHTS uniform ⇒ m_eff stays 12 for small delta… **So the bias polarises but does NOT concentrate the reading.**"*

That last sentence is the answer to the question 0963 left open — *can the dynamics concentrate the weights?* — and it was already on file. **The tilt enters the edge variables' means, not the reading weights.** Piece 1's central worry was addressed at 0820 and never connected to CAPACITY-1's conditionality.

## Check 2 — can the construction lose support to a vanishing determinant?

A sign weight is zero when the edge direction lies in `span{n̂, r̂₁, r̂₂}`, so support could in principle drop below the floor. Tested:

| frames | minimum support over all 120 vertices | p (unit weights) |
|---|---|---|
| 200 random frames | **11 of 12** | 11 |
| adversarial frames along lattice edge directions | **7 of 12** | 7 |

Even choosing frames deliberately aligned with lattice directions — where degeneracies concentrate — support never falls below 7. **Clears the floor of 4 with margin in every case tested.**

## Check 3 — the singleton-orbit worry from 0961

Patch 0961 found that four of the nine n̂-shells have edge orbits `[1, 1, 5, 5]` under the vertex stabiliser, so a covariant observable could in principle sit entirely on a singleton and reach `p = 1`. Enumerating the achievable covariant supports:

| `v·n̂` | orbits | achievable supports | min ≥ 4 |
|---|---|---|---|
| ±1.000 | [12] | 12 | **12** |
| ±0.809 | [1,1,5,5] | 1, 2, 5, 6, 7, 10, 11, 12 | **5** |
| ±0.500 | [3,3,3,3] | 3, 6, 9, 12 | **6** |
| ±0.309 | [1,1,5,5] | 1, 2, 5, 6, 7, 10, 11, 12 | **5** |
| 0.000 | [2,2,2,2,4] | 2, 4, 6, 8, 10, 12 | **4** |

**A bonus the enumeration gives:** on the singleton-orbit shells, supports **3 and 4 are not achievable at all**. The orbit structure jumps from 2 to 5. So the smallest admissible reading on exactly the shells 0961 flagged as the exposure is **5, not 4** — those shells clear with room. **Only the equatorial shell is tight, at exactly 4.**

So the 0961 worry resolves in our favour, and for a reason 0961 could not have seen: the singleton orbits are there, but an observable sitting on them has support 1 or 2, which the dimensional argument excludes outright as not a handedness observable at all.

## The reviewer trap — found in our own corpus

**0820 §(2) says: *"A 4-edge det reads only 4 (⇒ emergent)"*.**

Read cold, that contradicts the floor: it asserts that a 4-edge reading gives *emergence*, while CAPACITY-1's floor admits `p = 4` as sufficient for *non*-emergence.

**It is not a contradiction — it is a superseded statement.** 0820's "emergent" verdict came from 0819's mean-field `K_lift` comparison, whose crossover sits at `m_read ≈ 8`. That scan was **replaced** by 0828's refined-chord bound — a proof over the whole class rather than a mode scan — under which `p ≥ 4 ⇒ z* ≤ 0.5 ⇒ ρ(M) ≤ κ(0.5) = 2/3 < 1`. The live bound clears `p = 4`; the superseded estimate did not.

**The assembly patch must say this explicitly.** A reviewer who reads 0820 — and they will, since it is where the uniform-weight claim lives — will hit §(2) and read it as our own corpus contradicting our own floor. Left unaddressed, this is the single most likely falsifier vote in the next dispatch.

## Disposition

- **All three R-1 checks clear.** Piece 1's assembly is not obstructed by anything the hostile pass could find.
- **Two findings strengthen the case beyond 0963:** 0820 §(3) already establishes that the bias does not concentrate the reading; and the singleton-orbit shells admit no reading of support 3 or 4, so they clear at 5.
- **One finding must be handled in the assembly patch:** the superseded 0820 §(2) statement, explicitly reconciled against 0828.
- **Next:** the assembly patch — statements (a) unit weights from the det-coset construction, (b) participation = support, (c) the 4-D orientation floor — with the 0820 §(2) reconciliation stated up front, then a panel under R-2 as a fresh campaign with its effort bound written at dispatch.
- **No claim registered. No verdict moved. CAPACITY-1 untouched. Piece 1 still open.**
