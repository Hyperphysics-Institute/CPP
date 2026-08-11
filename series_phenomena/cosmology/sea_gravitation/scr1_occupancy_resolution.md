# SCR-1 RESOLVED — PAIR DENSITY / OCCUPANCY: φ₁ = 0.4844 (dynamic-matching cycle average), plus a ~2% truncation erratum on the 3067 C₄

**Patch 3071 (11 Aug 2026). The first of the four frozen counting
questions (3068 §3; D-COMP-WEIGHT added at 3070). Forward-resolved
from the automaton and the registered founder picture; no reference
to the band appears anywhere in this derivation. Verify:
`scripts/3071_scr1_occupancy.py` (convergence PASS; the 3067
committed value reproduced exactly under its own convention).**

## §1 — The frozen question

The 3068 forward assembly's lattice sum C₄ = Σ 1/r⁴ took **one pair
per FCC site**. The founder's registered picture (3059 ruling,
quoted at 3067) is **every GP a CP**, with a DP's two CPs occupying
**adjacent GPs**. Which counting does the corpus force, and what is
the resulting factor on ρ_Λ?

## §2 — Corpus-forced inputs (nothing new assumed)

1. **3059 (founder, registered):** CPs each on their own GP ⇒ a DP =
   two CPs on adjacent GPs. The emitting dipole's location is the
   **nn-edge midpoint**, not a site.
2. **Full occupancy (founder picture per the 3068 SCR-1 text):**
   every GP hosts one CP ⇒ N_pairs = N_sites/2 (each CP in exactly
   one pair at any Moment).
3. **FQ-1 (founder, 3068):** partner switching every ZBW cycle ⇒ the
   matching is **dynamic**; the cycle-averaged pair-centre
   distribution is the object that enters the arrival sum.
4. **z = 12 FCC at nn = l_P** (corpus-forced, 3067).

## §3 — Resolution

The cycle-averaged dynamic matching, mean-field: each site sits in
exactly one of its 12 nn edges ⇒ every edge midpoint carries
occupation weight 1/12. (Charge eligibility — only +/− edges pair —
halves the eligible edges and doubles the conditional weight; the
product is unchanged.) The receiving CP's own pairing is the edge
incident to the origin ⇒ excluded as self. Correlation corrections
(the origin's partner is unavailable to its other edges; the
remaining 11 neighbours re-weight slightly) are O(1/z) class and are
bracketed by the ordered extreme below.

Computed by direct summation over a sphere with the exact analytic
tail (4π·density/R for a 1/r⁴ sum):

| Quantity | Value | Note |
|---|---|---|
| C₄ per the 3067 convention (±40 cube, no tail) | **24.8225** | reproduced exactly |
| C₄ converged (one pair per site, infinite lattice) | **25.3382** | the 3067 cube truncation undercounts by ×1.0208 |
| S₄ mean-field dynamic matching | **12.2736** | the ADOPTED cycle average |
| S₄ ordered parallel matching (bracket) | 9.8251 | maximal-correlation extreme |
| **φ₁ = S₄(pairs)/C₄(converged)** | **0.4844** | bracket [0.388, 0.484] |
| far-field density ratio | 0.5000 | pairs = sites/2, as it must |

Near-field detail: the nearest non-self pair centres sit at √3/2 ≈
0.866 (midpoints of edges between the origin's mutual-nn
neighbours), closer than the nearest site at 1.0 — this is why φ₁ =
0.4844 rather than exactly 1/2. The two matching extremes differ by
×1.25; the mean-field value is adopted as the FQ-1-mandated dynamic
average, the bracket recorded.

## §4 — The two SCR-1 outputs, stated with direction

- **φ₁ = 0.4844** multiplies ρ_Λ (√φ₁ = 0.696 multiplies c_Li).
  **Direction: AWAY from the band** — this factor alone deepens the
  3068 shortfall by ~×2. Recorded plainly; the scrutiny was frozen
  precisely so that its answers bind whichever way they point.
- **Truncation erratum ×1.0208** on ρ_Λ: the 3067 C₄ was computed
  over a finite ±40 integer cube with no tail; the converged
  infinite-lattice value is 25.3382. This is a numerical correction
  to a frozen-definition sum, not a convention choice — direction
  toward the band, magnitude 2%, immaterial against ×1.5–10.
- Net SCR-1 package on ρ_Λ: **×0.4844** relative to the 3068
  assembly as committed (the erratum is already inside φ₁'s
  denominator being the converged C₄; applying φ₁ to the 3068
  formula with its committed C₄ = 24.8225 gives the equivalent net
  ×0.4945).

## §5 — Freeze compliance

Per the 3068 rule the factors (SCR-1, SCR-2, SCR-3, D-COMP-WEIGHT)
multiply ONCE, at the end, each with its own derivation note; no
intermediate verdict is computed here and none of the remaining
notes may condition on this one's direction. SCR-2 (per-pair vs
per-CP emission multiplicity under AP-4c) is next; note the
factorization boundary — SCR-1 has counted PAIRS; whether each pair
contributes one or two emission quanta per Moment is entirely
SCR-2's question, and no double-counting path exists between them.

---

## §6 — FOUNDER CORRECTION (Patch 3072, v1.1) — the picture refined; the resolution robust

**The founder, on reviewing the v1.0 resolution (verbatim):**

> One point per lattice site, except for when they are superimposed,
> which is the very essence/center of the ZBW mechanism.
> Superimposition is what creates the expansion effect. Given that
> ZBW is the driving force of the CC, the number of times that a DP
> is in a superimposed state, the double occupancy of GPs will be
> frequent, but it is not stable, which was my point in saying 1 CP
> per GP.

> Pairs do not swap every cycle. They only swap when they are closer
> to a new partner on the perigee than the old partner. We discussed
> this in the past, it may have been in the context of deriving
> inertia. I think the partner swapping frequency is small (smaller)
> compared to the monogamous partner fidelity. I don't know what the
> percentage would be. That was an unknown rather than a declared
> value.

**Disposition of correction 1 (superposition / double occupancy):**
changes WHERE the pair centres sit, not HOW MANY pairs there are.
The census (N_pairs = N_sites/2) is picture-invariant — superposition
is transient double occupancy by a pair's own two CPs, not a change
in the count. Geometry revision: with exactly-opposite excursions
about the superposition GP, the pair CENTRE sits ON a site for the
whole cycle (half the sites occupied per Moment) rather than at the
edge midpoint of the v1.0 static reading. Recomputed (script §D):
φ₁ = 0.4803–0.5000 under centres-on-sites (self-pair placement
bracket), vs 0.4844 under midpoints. **Adopted: φ₁ = 0.49 ± 0.01,
robust across both pictures.** Direction unchanged (away from the
band); the correction TIGHTENS the resolution.

**Disposition of correction 2 (monogamous fidelity, rare swapping):**
does not enter SCR-1 at all — a static 1/r⁴ ensemble sum depends
only on the marginal pair-position distribution, not the reshuffle
rate, and the correlation extremes were already bracketed. **The
swap fraction is hereby flagged as an SCR-3 input** (D-ETA-Z):
registered as an UNKNOWN, not a declared value, per the founder.
Preliminary read, to be tested in the SCR-3 note: swap-vs-return at
close approach redirects the NEXT cycle without materially changing
the completed cycle's ⟨δ²⟩, so the unknown fraction may drop out of
η_z entirely; if it does not, it becomes a named open input, never a
guess. Consonance noted: the founder's superposition emphasis (real
dwell at δ = 0) is precisely the content of the η_z ≤ 1 bound in
R-DELTA-ZBW — the corrected picture and the frozen parameterization
agree.

**Status: SCR-1 CLOSED at φ₁ = 0.49 ± 0.01.** The ±0.01 rides along
as an honest sub-2% band, not a dial.
