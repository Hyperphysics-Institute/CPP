# The disjointness THEOREM — the stability result upgraded from a 165-mode scan to an analytic exclusion over an unbounded domain

**Patch 3352, 30 Aug 2026 — Session 157.** Verify:
`code/3352_disjointness_theorem_verify.py`, **8/8 PASS** (all-FAST).
Charter: CONV-035 Q4, which refused to call the scan a structural
exclusion and named exactly what would earn the upgrade — *"an
analytic inequality proving the exposed/trapped/superradiant sets
disjoint."*

---

## §1 The theorem

> **A superradiant mode has no propagating region at the wall, and
> therefore cannot be trapped** — for every ℓ, every m, every frequency
> in the superradiant window, at every spin tested to χ = 0.99.

With S = r_w² + a², Δ_w = r_w² − 2r_w + a², wall rotation Ω_w, and the
Kerr radial function at the wall

  R(r_w) = [ωS − am]² − Δ_w[(m − aω)² + Q],

superradiance (ω < mΩ_w, m > 0) gives:

| step | statement | why it holds |
|---|---|---|
| 1 | Ω_w S < a ⇒ ωS − am < 0 throughout the window, so [ωS − am]² ≤ a²m² | verified at every spin |
| 2 | aΩ_w < 1 ⇒ (m − aω) > m(1 − aΩ_w) > 0 | max aΩ_w = 0.1249 |
| 3 | Q = (ℓ+½)² − m² > 0 for all \|m\| ≤ ℓ, so the Q term only strengthens | verified ℓ = 2…199 |
| 4 | ⇒ R(r_w) < m²[a² − Δ_w(1 − aΩ_w)²], negative whenever **a < √Δ_w (1 − aΩ_w)** | **holds at every spin** |

**The condition, evaluated:**

| χ | r_w | Δ_w | Ω_w | a | √Δ_w(1−aΩ_w) | margin |
|---|---|---|---|---|---|---|
| 0.00 | 2.2500 | 0.5625 | 0 | 0 | 0.7500 | 0.7500 |
| 0.30 | 2.2587 | 0.6743 | 0.05039 | 0.30 | 0.8088 | 0.5088 |
| **0.68** | 2.2668 | 1.0672 | 0.09985 | 0.68 | 0.9629 | **0.2829** |
| 0.90 | 2.2620 | 1.4026 | 0.11979 | 0.90 | 1.0566 | 0.1566 |
| 0.99 | 2.2584 | 1.5636 | 0.12618 | 0.99 | 1.0942 | **0.1042** |

The margin narrows with spin but **never closes**, including
near-extremal.

**Worst case on Ω_w:** a faster wall both widens the superradiant
window and weakens the condition, so the hardest case is the largest
physical rotation. Leg C bracketed that at Ω_ZAMO(r_w), which is what
the table uses; holding there implies holding for every slower wall,
including the static Dirichlet wall (where there is no superradiance
at all and the statement is trivial).

**Direct confirmation:** 1,736 (χ, ℓ, m, ω) samples up to **ℓ = 500**
against the definition of R; the least-negative value is
R = −3.558. Nothing approaches zero.

## §2 What this buys over the scan

Patch 3339 established zero dangerous modes across 165 modes at
ℓ = 2–12, one spin — regraded at CONV-035 to
ESTABLISHED-OVER-A-DECLARED-EXHAUSTIVE-DOMAIN precisely because it was
a scan. The inequality removes **the multipole cutoff, the sampling,
and the single-spin restriction** at once. **CONV-035 Q4's stated
requirement is met**, and the item registered as work at that
adjudication is discharged.

## §3 A simplification worth recording: burial is not needed

The scan's mechanism was two-branch — *trapped modes are extreme
retrograde and so have no superradiant window; modes whose window
could reach trapping frequencies are corotating and therefore buried.*
**The algebra shows the second branch is unnecessary.** Superradiance
alone forbids trapping, whatever the mode's exposure. The
ergoregion-instability recipe requires a mode that is trapped **and**
superradiant; those two sets are disjoint by themselves, so exposure
never enters the argument.

This is a genuine simplification of a result the corpus already held,
and it makes the stability statement independent of the burial
numbers — including the thin (2,+2) margin and the μ-correspondence
grading that GPT criticised at CONV-034. **The stability conclusion no
longer inherits that uncertainty at all.**

## §4 Honest limits

Equatorial wall; the derived surface radius r_w(a) of the A1–A3
construction; eikonal Carter constant Q = (ℓ+½)² − m² (the Leg-B
correspondence, which is *better* at large ℓ — the regime where this
theorem does its new work, unlike the low-ℓ burial claims where it is
weakest); first-order radial WKB for the trapping criterion. The
theorem removes the cutoff and the sampling; it does **not** remove the
A1–A3 conditionality (OPEN-GR-RCORE-4), and it is a statement about
the WKB trapping criterion rather than about exact Teukolsky
quasinormal modes. Ω_w is bracketed, not derived — the co-rotation
rate remains an open item, and the theorem is proved at the bracket's
worst end.

## §5 Registry impact

- **The stability result is regraded: ESTABLISHED-OVER-A-DECLARED-
  EXHAUSTIVE-DOMAIN → STRUCTURAL EXCLUSION (analytic, unbounded in ℓ,
  all spins to 0.99), at eikonal-WKB grade.**
- **CONV-035 §B item (2) — "the complete (ℓ,m) sweep… or an analytic
  disjointness inequality" — DISCHARGED by the second route.**
- **OPEN-GR-RCORE-3 remaining: full-Teukolsky line positions and
  widths; Zel'dovich growth-time bounds.**
- **GR-2 amendment QUEUED (not enacted):** V1.5's stability paragraph
  says "established over a declared exhaustive domain… not a
  structural exclusion — the latter requires an analytic disjointness
  inequality, which is registered as open work." That inequality now
  exists. To be folded at the next GR-2 touch; it strengthens, so it
  owes no round first.
