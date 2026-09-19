# b Needs Covariance, Not Invariance — TODO-4140-BIVECTOR Closed as Misconceived

**Patch:** 4143. **Lane:** EW. **Session:** 234.
**Closes:** TODO-4140-BIVECTOR — **as misconceived, not solved.**
**Withdraws:** 4140's bivector construction as a *target*; 4142 §5's relocation of it.
**Verify:** `series_standard_model/code/4143_covariance_not_invariance.py`.

---

## 1. The mistake I have been making for four patches

4139 found an absolute-frame residual in b and called it a crisis. 4140 tried to remove it by
making b an **exact Lorentz invariant** (the bivector construction). 4141 and 4142 then spent two
patches hunting the bivector partner that construction needs.

None of it was necessary, and the target was unattainable in principle:

> **Helicity is not Lorentz-invariant for a massive particle.** It never has been, in any theory.
> Boost past a massive particle and its helicity reverses. The Standard Model has exactly this
> property and nobody regards it as a defect.

Computed on collinear boosts, where the little-group element is trivial and there is no Wigner
rotation to omit: a nucleon at 0.3c has its momentum reversed by any boost above β = 0.3; at
0.999c, above β = 0.999; a photon requires β > 1 and so is never reversed. That is the whole of
the massive/massless distinction, and it is why the corpus's own OPEN-FP-SF-2-CHIR closes V−A
chirality *at the massless helicity limit* and not generally.

## 2. What the comagnetometer actually forbids

Not frame-dependence. It forbids an energy term

  E_spin = κ (Ŝ · n̂_cosmic)

with **n̂_cosmic a fixed direction in space** — that is what modulates at the sidereal frequency as
the lab rotates under it. It requires a preferred direction to exist in the dynamics.

A covariant theory has no such direction available: every vector in the energy is built from the
local state — local momentum, local field, local spin — and the lab's rotation moves all of them
together. Nothing modulates.

**Frame-dependence and a preferred-frame signature are different things, and 4139 conflated them.**

## 3. Which is exactly what the ruling says

> *"The summation yields a Lorentz-modified **local** reference-frame velocity … resulting in no
> absolute-frame signature."*

b = A · SSV_net^disp is then built from two **local** quantities. It is frame-dependent, like every
helicity in physics, and carries no fixed cosmic direction. No sidereal term. The comagnetometer
bound is not approached, let alone exceeded — and no exact invariance is required to get there.

## 4. Consequences — four of my own patches withdrawn or downgraded

| | |
|---|---|
| **4139** absolute-frame alarm | already withdrawn at 4140; now also *understood* — it presumed the CP reads an absolute velocity, which the ruling denies and covariance makes unnecessary |
| **4140** bivector construction | **withdrawn as the wrong target**, not merely unproven: exact invariance of a spin–momentum pseudoscalar is unattainable for a massive particle in any theory |
| **4141** objection to 4140 | correct, and now moot along with its target — but its **by-product stands** |
| **4142** relocation to the CP's attributes | **withdrawn.** I flagged "more natural home" for the next window to check; checked, and the question it relocated should not have been asked |

**What survives the arc, and it is the real yield:** the **SSV_net role split** (4142 §§1–3) — two
objects under one name, settled by GR-1a's own force equation, with the corpus audit registered as
TODO-4142-SSVAUDIT. That stands independently of everything above and would not have been found
without the detour.

## 5. Status

**A3G-2 PASSES** — on exactly the same footing as every other CPP result that relies on SR-1's
emergent Lorentz covariance. No weaker and no stronger. If SR-1's covariance fails, A3G-2 reopens
along with a large part of the corpus; that is the honest scope of the claim, and it is a far
better-grounded pass than the 4125 T-parity argument it replaces.

**Suite: five of nine** — back where the session-start record had it, but for a sound reason
instead of an inverted table. χ₄ provisionally adopted. **F5 remains the blocker.**

## 6. PD-008 — the convenient branch, marked

There is no convenient branch here; there is only a long one and a short one, and I took the long
one first. The honest accounting is that patches 4139–4142 chased a requirement that a first-year
result about massive-particle helicity rules out, and I did not stop to ask whether invariance was
the right target until the fourth patch. The founder's ruling said "no absolute-frame signature" —
which is covariance — and I read it as "b is invariant," which is stronger and false. **The
generalisable lesson: when a ruling states an absence, check what exactly is absent before building
machinery to guarantee it.** Filed with TODO-4138-TABLEPROSE as a second instance of the same
discipline — the gap between what was established and what got written down.
