# The Lattice Has a Global Orientation, and b Can See It — a Falsifier-Class Problem

**Patch:** 4160. **Lane:** EW. **Session:** 234.
**From:** TODO-4159-CRYSTAL link 2. **Reopens:** Patch 4143's isotropy argument.
**Verify:** `series_standard_model/code/4160_lattice_anisotropy.py`.

---

## 1. Link 2 answered, and the answer is worse than "no"

Link 2 asked whether the substrate lattice's orientation is tied to a material crystal's. **No** —
the 600-cell's spacing is l_P ~ 1.6×10⁻³⁵ m against a crystal's ~10⁻¹⁰ m, twenty-five orders apart.
A material crystal cannot orient the substrate.

**But the substrate does not need orienting. It already has a global orientation.** Every GP has the
same twelve neighbours pointing the same twelve ways, everywhere. So Patch 4159's
orientation-averaging — the thing that rescued ⟨b⟩ = (v/c)cos θ — **is not available. There is
nothing to average over.**

## 2. The corpus's own no-preferred-direction argument proves something weaker than it says

`founders_vision.md`: *"The 600-cell is the same in every direction at every vertex — each GP has
the same twelve neighbours arranged the same way. So when a CP displaces, it has no built-in bias
toward any neighbour."*

That establishes **vertex-transitivity**. It does **not** establish **directional isotropy**: the
twelve neighbours point in twelve specific directions, and their being the same at every vertex is
precisely **a global orientation**, not the absence of one. The sentence slides from "no vertex is
special" to "no direction is special," and only the first is proved.

## 3. Why nobody has caught it: the 12-set is a spherical 5-design

| observable | spread over spin-axis directions |
|---|---|
| polynomial moment, degree 2 | 3.9×10⁻¹⁶ |
| polynomial moment, degree 4 | 5.0×10⁻¹⁶ |
| polynomial moment, degree 6 | 4.7×10⁻² |

Degrees 2 and 4 are direction-independent **to machine precision** — the lattice is *exactly*
isotropic to them. Degree 6 breaks, as a 5-design must.

**Every observable CPP has tested is a low-degree polynomial.** That is why SR-1's emergent Lorentz
invariance has held for everything asked of it: the lattice really is isotropic to all of it.

## 4. But b is sign-valued, and sign() is not a polynomial

| β | mean over directions | min | max | **spread** |
|---|---|---|---|---|
| 0.1 | 0.1002 | 0.0000 | 0.3333 | **0.333** |
| 0.2 | 0.2002 | 0.0000 | 0.5000 | **0.500** |
| 0.5 | 0.5001 | 0.3333 | 0.8333 | **0.500** |
| 0.9 | 0.9001 | 0.8333 | 1.0000 | **0.167** |

The **mean** over directions is β — 4158's law survives as an average. The **spread is 17–50% of
full polarisation, depending on direction.**

> **b is the first observable in CPP that can see the lattice's anisotropy, because it is the first
> that is not a low-degree polynomial. The amendment introduced it.**

## 5. What that predicts — and it is a problem, not a result

The lattice orientation is a global constant; a laboratory direction sweeps relative to it as the
Earth rotates. So beta-decay longitudinal polarisation should show a **sidereal modulation with
icosahedral structure, of amplitude tens of percent at β ≈ 0.2–0.7.**

**This is falsifier-class.** Beta polarimetry dates from 1957, and Lorentz-violation searches bound
spin-direction sidereal effects at ~10⁻³³ GeV — the same He-3/Xe-129 comagnetometer bound used at
Patch 4139. **A tens-of-percent modulation would have been seen a lifetime ago.**

**It also reopens Patch 4143.** 4143 dismissed the preferred-frame alarm on the grounds that "a
covariant theory has no fixed cosmic direction." A globally oriented lattice **is** a fixed cosmic
direction. 4143's argument holds for polynomial observables — which, per §3, is everything CPP had
tested. It does not hold for b.

## 6. The escapes, and what each costs

- **(a) b is read only after averaging over Moments in which cage orientation decorrelates from the
  lattice.** But the cage *occupies* lattice vertices, so its orientation is lattice-locked by
  construction. Hard.
- **(b) The 12-edge selection and the b-evaluation happen at different stages**, so b is not
  restricted to the twelve directions when it is evaluated. **Cheapest**, but contradicts c03/GR-1b
  as written.
- **(c) b enters observables only through low-degree polynomials in b.** Contradicts B3, which says
  the response is *linear* in b — and linear-in-a-sign is exactly the non-polynomial case.
- **(d) The lattice has domains smaller than a laboratory.** Nothing in the corpus proposes them,
  and they would carry their own signatures.

I do not know which is right. **(b)** is cheapest, **(d)** most speculative. What I am confident of:
**as the corpus stands, {12-edge selection + b = sign(A·V) + B3 linearity + a globally oriented
lattice} predicts an effect that is not observed.**

## 7. PD-008 — the convenient branch, marked

The convenient branch was large and I want it named precisely. Patch 4159 presented the staircase as
**the amendment's first distinctive empirical signature** — the thing Patch 4155 said it lacked, and
the best news of the session. Pressing link 2 turns the same computation from a prediction into a
**contradiction with existing data**, because the orientation-averaging that made it a prediction is
unavailable once the lattice's global orientation is taken seriously. I could have left link 2 as
"three unverified links" and moved on; nothing forced this.

The second declined branch: escape (b) is cheap, plausible, and would dissolve the whole thing in a
sentence. I have listed it as a candidate rather than adopting it, because adopting an escape I
cannot derive is how a falsifier becomes a footnote.

## 8. Status

**This is the most serious open issue in the lane, ahead of F5.** Registered as
**TODO-4160-ANISOTROPY**. It does not fire a verdict by itself — an escape may exist — but it should
be treated as a live falsifier for χ₄ and, through SR-1's isotropy claim, as a question about the
substrate itself rather than only the amendment. No verdict moved. χ₄ provisionally adopted.
