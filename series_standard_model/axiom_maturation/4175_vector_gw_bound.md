# The A_i Channel's First Numerical Bound — and the Choice It Forces

**Patch:** 4175. **Lane:** EW/GR. **Session:** 234.
**Discharges:** TODO-4174-VECTORGW.
**Verify:** `series_standard_model/code/4175_vector_gw_bound.py`.

---

## 1. Why the bound is weak: astrophysical spin density is tiny

A_i is sourced by **intrinsic** spin density, not orbital angular momentum. Bulk neutron matter is
essentially unpolarised, so the source carries the polarisation fraction P. For a body of mass M,
radius R, angular frequency ω:

  S/(M R²ω) = (M/m_n)ħP/(M R²ω) = **ħP/(m_n R²ω)**

For a neutron star at R = 10⁴ m, ω = 10⁴ rad/s: **6.3×10⁻²⁰ × P.** Even at P = 1. A magnetar's
P ~ 10⁻³ gives 6×10⁻²³.

With LIGO/Virgo/KAGRA bounding the non-tensor amplitude fraction at ≲10%:

> **κ_A / κ_grav ≤ 1.6×10¹⁸**

## 2. A dimensional error I made and caught — recorded, not fixed silently

My first draft compared this against an anomalous **spin–spin force** bound and concluded the
spin–spin test was fifteen orders tighter. **The comparison was meaningless.** It set
κ_A ħ²/(4π) [J·m³] beside κ_grav = 16πG/c⁴ [m/J] — different units, m³/(J s²) against m/J — so the
"× κ_grav" in that draft was not a number at all.

**What exposed it:** the script's own comparison line printed *"the spin–spin bound is 7×10⁻³⁵ times
tighter"* while the prose above it said fifteen orders the other way. That is **D-11 firing on my own
draft**, one patch after D-11 was enacted, and it is the first time this session the discipline
caught something before it shipped rather than after.

**Why it cannot be repaired here.** To get A_i's **static** potential between two spins — what a
torsion balance bounds — one needs A_i's **field equation**, and there isn't one.
**TODO-4172-SOURCEEQ is open precisely because A3′ never wrote it.** So the missing source clause
blocks the static test; only the **radiative** test is available.

## 3. So the GW bound stands alone, and 4174's nomination was right

**κ_A / κ_grav ≤ 1.6×10¹⁸.** Dimensionally consistent because A_i and Q_ij feed propagating channels
of the *same packet*: the amplitude ratio is (κ_A/κ_grav) × (spin source / mass-quadrupole source),
and the suppression factor carries the dimensions.

**This is the first numerical bound the A_i channel has ever carried.** It converts
TODO-4172-SOURCEEQ from *"the coefficient is unknown"* to *"the coefficient is bounded above."* It
is weak — eighteen orders of room — and a weak bound is not nothing when the prior state was none.

## 4. The choice it forces, and this is the session's sharpest statement about χ₄

- **If κ_A is the gravitational value** — the natural zero-parameter choice, and what 4173 wanted —
  A_i's vector-mode contribution sits **10¹⁸ below the LIGO bound** and is unobservable by this
  route too.
- **If κ_A is large enough to be observable**, it is a **new parameter**, and the programme's
  zero-parameter claim takes the hit 4172 warned of.

> **The amendment cannot have both: zero parameters, or observability.**

And unlike everything else this session concluded about A_i, **this does not depend on any
identification I proposed.** It follows from A3′'s own structure — a propagating channel, a spin
source, and a coupling that is either fixed or free.

## 5. PD-008 — the convenient branch, marked

Two. First, §2: the error was mine, it was in an unshipped draft, and deleting it would have cost
nothing and shown nothing. It is recorded because the *mechanism that caught it* is worth more than
the embarrassment — D-11, one patch old, working as intended. Second, §3 vindicates 4174's
nomination, which is my own previous patch; I have said so plainly rather than burying it, but the
next window should note that I was the one who both nominated and vindicated it, and that §1 shows
the handle is far weaker than 4174's language implied.

## 6. Status

TODO-4174-VECTORGW discharged. **TODO-4172-SOURCEEQ remains open and is now the binding constraint
on every other test** — the static spin–spin route is unavailable until A_i has a field equation.
No verdict moved. χ₄ provisionally adopted. **F5 remains the blocker.**
