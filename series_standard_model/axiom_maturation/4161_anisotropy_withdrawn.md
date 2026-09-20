# The Anisotropy Falsifier Is Withdrawn — It Was My Modelling Error

**Patch:** 4161. **Lane:** EW. **Session:** 234.
**Withdraws:** Patch 4160's falsifier, and Patch 4159's "distinctive signature" — the same error
with opposite sign.
**Verify:** `series_standard_model/code/4161_anisotropy_withdrawn.py`.

---

## 1. The error

4159 and 4160 computed ⟨b⟩ by substituting **the twelve edge directions** for û in b = sign(A·V).
**The 12-edge rule quantises the *displacement*, not V.** c03, verbatim:

> *"The 12-edge selection rule chooses the lattice edge i\* that maximizes **e_i · SSV_net**."*

V is **prior to the selection and continuous**; the edge is chosen *from* it. And the amendment
evaluates b on V — 4120: *"b ~ A·V is derived, not postulated"*, with V the GP's summed register.

**So b never sees the twelve directions. It sees their sum.** Escape (b) of Patch 4160 §6 is not
"cheap and contradicts c03" — I had it backwards. It is simply correct, and my framing of it as a
contradiction was part of the same mistake.

## 2. The sum is isotropic, and exactly so at second order

| arrivals N | spread of ⟨b⟩ over spin-axis directions |
|---|---|
| 1 | 0.5034 |
| 2 | 0.1127 |
| 4 | 0.0106 |
| 12 | 0.0084 |
| 60 | 0.0093 |

At N = 1 the CP reads a single arrival and the lattice shows through — that is 4160's staircase, and
it is the N = 1 row of a table whose physical case is N ≥ 12. **By N = 12 the spread is at the
sampling floor.**

The reason is the same 5-design property 4160 used to explain why *nobody had noticed*:

  (1/12) Σ e_i e_iᵀ = **(1/3)·I exactly** — off-diagonals 2.5×10⁻¹⁸, diagonal spread 0.

A sum with independent weights over a set whose second-moment tensor is proportional to the identity
is isotropic at second order **by construction**. 4160 had the design property in hand and drew the
opposite conclusion from it, because it was looking at a single direction rather than at a sum.

## 3. This also settles 4158's premise, on the third attempt

4158 assumed an isotropic measure. 4159 showed the χ draft's double rotation does not supply it and
fell back on orientation-averaging. 4160 showed there is nothing to average over. **The real answer
was simpler than all three:** V's direction is isotropic because V is a **sum over a spherical
5-design**. No orbit argument, no ensemble argument.

## 4. What stands and what falls

| | |
|---|---|
| **Patch 4160's falsifier** | **FALLS entirely.** No sidereal modulation is predicted. |
| **Patch 4159's "first distinctive empirical signature"** | **FALLS.** Same error, opposite sign. |
| Patch 4158's ⟨b⟩ = (v/c)cos θ | **STANDS**, now on a third and finally sound premise |
| Patch 4159's negative result on the χ draft's double rotation | **STANDS** — it just was not needed |

**Net effect on the amendment: back to Patch 4155 §4's position — A_i has no distinctive empirical
signature.** Two patches of excitement and alarm cancelled, and the honest ledger is that 4159 and
4160 were both wrong, in opposite directions, for one reason.

## 5. The residual, which is real but small

V is isotropic at second order exactly and deviates at degree 6 — the 5-design's limit. **A CP that
reads only one arrival per Moment would see the lattice** (the N = 1 row). Whether any physical
regime is arrival-starved — very low DP-sea density, or the first Moment after a creation event — is
**not examined here**, and it is the one place the anisotropy could still live. Filed as
**TODO-4161-STARVED**.

## 6. PD-008 — the convenient branch, marked

There was no convenient branch available in either direction, which is itself worth noting: 4160's
falsifier was maximally inconvenient and I raised it; this withdrawal is convenient and I am
publishing it in the same session. **What the pair shows is that the inconvenient-branch discipline
does not substitute for getting the model right.** I checked at 4160 which escapes would *cost*
what, and did not check which was *true* — the corpus sentence that settles it (c03's "chooses the
lattice edge that maximizes e_i · SSV_net") was quoted in my own Patch 4155 and I read past it
twice.

## 7. Status

TODO-4160-ANISOTROPY **closed as withdrawn**. TODO-4159-CRYSTAL **closed** — its premise is gone.
No verdict moved. χ₄ provisionally adopted, with no distinctive signature. **F5 is again the
blocker.**
