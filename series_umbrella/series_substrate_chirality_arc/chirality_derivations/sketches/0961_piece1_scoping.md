# 0961 — Scoping piece 1: the symmetry route is closed, the natural candidates clear comfortably, and the real work is the η-identity

**Patch:** 0961, 13 Sep 2026. **Lane:** chirality (09xx). **Type:** scoping sketch — **no claim registered, no verdict moved, nothing enacted.** **Founder instruction, 13 Sep:** *"yes, please scope out the work."*

**Piece 1**, now the sole live conditionality on THEO-CHIR-CAPACITY-1 after Patch 0960: *the dynamical η is pointwise non-degenerate* — at every vertex, the local handedness observable genuinely reads several incident edges rather than collapsing onto one. Formally `p(v) = 1/Σ_e (c^v_e)⁴ ≥ 4` with `Σ_e (c^v_e)² = 1`.

---

## 1. Three findings from the scoping computation

### (a) Both natural candidates clear the floor, with margin

| candidate for the dynamical η's weights | p(v) range over all 120 vertices | vs floor of 4 |
|---|---|---|
| **sign weights** `sign det[d̂, n̂, r̂₁, r̂₂]` (the 0821 canonical observable) | **12.000 everywhere**, all three frames | 3× the floor — the maximum possible on 12 edges |
| **magnitude weights** `\|det[d̂, n̂, r̂₁, r̂₂]\|` | **[5.333, 12.000]**, all three frames | worst case 33% above the floor |

To reach `p = 4` at all, a single edge must carry **~70% of the total weight norm**. At 50% concentration `p` is still 8.8; at 60%, 6.0.

### (b) The stated worry points the wrong way

Patch 0924 named the concern as the dynamical η *"degenerating at n̂-extremal vertices."* It does the opposite. The n̂-extremal vertices are the **best** case: at the poles (`v·n̂ = ±1`) the vertex stabiliser is the full local I_h of order 120, acting transitively on all 12 edges, so `p = 12` exactly. For the magnitude-weighted candidate the minimum sits at the **equatorial** shell (`v·n̂ = 0`), not at the poles.

### (c) **The symmetry route is closed — and this is the finding that matters**

The obvious proof strategy is: the vertex stabiliser inside Stab(n̂) acts on that vertex's 12 edges, symmetry forces equal weights within each orbit, and the orbit structure bounds `p` from below. **It does not work.** Orbit structure per n̂-shell:

| `v·n̂` | shell size | `\|Stab_v\|` | edge orbits | symmetry-forced floor on p |
|---|---|---|---|---|
| ±1.000 | 1 | 120 | [12] | **12** |
| ±0.809 | 12 | 10 | **[1, 1, 5, 5]** | **1** |
| ±0.500 | 20 | 6 | [3, 3, 3, 3] | 3 |
| ±0.309 | 12 | 10 | **[1, 1, 5, 5]** | **1** |
| 0.000 | 30 | 4 | [2, 2, 2, 2, 4] | 2 |

**Four of the nine shells — the 48 vertices at `v·n̂ = ±0.809` and `±0.309` — carry singleton edge orbits.** A Stab_v-covariant observable is free to put all its weight on a singleton, giving `p = 1`: fully degenerate. Symmetry permits exactly the collapse piece 1 needs to rule out, and permits it at the near-polar shells, which is roughly where 0924 feared it.

**So piece 1 cannot be closed by a symmetry argument.** That route is now eliminated rather than untried, which is the main value of this scope.

## 2. What piece 1 actually requires

It is the **η-identity problem**: not "is some admissible observable non-degenerate" (trivially yes — CAPACITY-1 already quantifies over the whole non-degenerate class), but **"which observable does the substrate's dynamics single out, and what are its weights?"**

CAPACITY-1 holds for every observable in the non-degenerate class. Piece 1 asks whether the physically realised η is in that class. Since symmetry does not force it, the weights must be **derived from the dynamics** — the PCD cycle, the det-coset structure, and whatever fixes the reading radius and the per-edge weighting.

## 3. Routes, with honest cost

**Route A — derive the dynamical η's weights from the PCD cycle.** The real route. If the derived weights are sign-like or determinant-magnitude-like, piece 1 closes immediately with the margins in §1(a). **Cost: a genuine research task, not a computation.** It needs a statement of what the substrate's own handedness reading *is* — plausibly one session to determine whether that statement already exists in the corpus (the det-coset construction may already fix it), and several more if it does not. **This is where I would start, and the first step is cheap: search whether the det-coset order parameter's weights are already pinned somewhere in the sub-corpus.**

**Route B — symmetry bound.** **CLOSED** by §1(c). Do not attempt.

**Route C — the banked fallback, already written.** Patch **0925** drafted `CAPACITY-1B`, the narrowed theorem that is **unconditional on piece 1**: *over the class of pointwise non-degenerate observables, η does not condense* — stated as an explicit domain of quantification rather than an assertion about the substrate. It is drafted, not registered, and it was banked precisely for this situation. Registering it would give an unconditional-on-piece-1 result at the cost of the stronger headline. **Cost: one patch plus a panel** — and under R-2 that is a fresh campaign, not free.

**Route D — a weaker sufficient condition.** Rather than deriving the weights exactly, find a property the dynamics plainly has that forbids ~70% single-edge concentration. The concentration required to fail is extreme, so a crude bound might suffice. **Cost: unknown until Route A's first step tells us what constrains the weights at all.** Speculative; listed because it is cheap to notice if Route A surfaces a partial constraint.

## 4. Recommendation

**One session on Route A's first step only:** determine whether the corpus already fixes the dynamical η's weights, and report. That is a search-and-read task with a definite end, and it decides everything downstream — if the weights are already pinned and look like either candidate in §1(a), piece 1 closes almost immediately; if they are not pinned, piece 1 is a research programme and Route C becomes the sensible fallback.

**What I would not do:** open Route A blind as an open-ended derivation. The honest scope is that piece 1 is *not* a day's work by any route now known, and that the single cheap step which could make it one is the corpus search.

**Answer to the founder's question — a day or a year?** Neither, on current evidence: **it is one session to find out.** The symmetry shortcut is gone, the natural candidates look healthy but are not established as *the* dynamical η, and a banked fallback exists if the derivation proves long.

## 5. Disposition

- **Scoping only.** No claim registered, no verdict moved, CAPACITY-1 untouched, piece 1 still open and still the live conditionality.
- **Recorded for the next window:** Route B is eliminated; §1(a) margins and §1(c) orbit table are reusable; Route C is drafted at 0925 and needs only a panel.
- **Note on 0924's framing:** the "n̂-extremal degeneration" worry is misdirected — the poles are maximally non-degenerate. The singleton-orbit shells (`±0.809`, `±0.309`) are the actual exposure, and they are near-polar rather than extremal. Worth correcting if 1B is ever fired.
