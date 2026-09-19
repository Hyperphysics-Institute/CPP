# TODO-4111-BCONFLICT Resolved — No Double-Count; Option B Supplies a Missing Half

**Patch:** 4112. **Lane:** EW (SS cross-lane). **Discharges:** TODO-4111-BCONFLICT.
**Verify:** `series_standard_model/code/4112_bconflict_resolution.py`.
**Verdict: NO CONFLICT. The risk inverts into Option B's second-largest payoff.**

---

## 1. The worry, as filed at 4111

SF-6 derives **B as the curl of a polar displacement** (Patches 4069/4070). Option B adds an
**independent axial channel A_i** to the same broadcast. Two axial objects in one packet
looked like a double-count, and I filed it as the thing to settle before the axiom question
could be put.

## 2. The corpus already names both, in one operator

**OPEN-SS-8** (Nucleon Magnetic Moments, HIGH priority) states its own solution route:

> *"Compute **⟨L̂ + 2Ŝ⟩**_ZBW for u,d quarks from cage geometry; apply SU(6) formula."*

That is the orbital-plus-spin magnetic moment operator with the g = 2 factor on Ŝ written out.
The two axial objects are not duplicates — they are **the two terms of an operator the corpus
has had registered all along**:

| term | supplied by | status today |
|---|---|---|
| ⟨L̂⟩ — orbital magnetism | SF-6's ∇×V | **present** |
| 2⟨Ŝ⟩ — spin magnetism | Option B's A_i | **MISSING** |

## 3. And for the nucleon, orbital contributes exactly nothing

The proton and neutron are ground-state baryons: **L = 0**. So ⟨L̂⟩ = 0 and **100% of the
nucleon magnetic moment is the spin term**. A curl-of-displacement channel cannot supply any
of it — orbital-only predicts μ_p = μ_n = 0.

The spin-only SU(6) result reproduces the observed ratio:

- SU(6): μ_p/μ_n = **−1.500**
- observed: 2.793/(−1.913) = **−1.460**
- agreement **2.7%**, with no free parameter

This is the classic SU(6) success and it is *purely* a spin result. **There is no choice of
orbital dynamics that yields −1.46 from L = 0.**

## 4. Verdict

> **No double-count. SF-6's ∇×V and Option B's A_i are the orbital and spin halves of
> ⟨L̂ + 2Ŝ⟩. Both are required; only one currently exists.**

The 4111 risk inverts. Option B does not threaten SF-6's magnetism — it supplies the half that
**OPEN-SS-8** (HIGH priority) and **PRED-O-14** (a registered prediction, still "to derive")
are both blocked on, and the only half that contributes for the nucleon ground state.

What survives from the 4111 concern is a **naming requirement, not a conflict**: SF-6 results
that refer to "the axial part of the lattice state" must say whether they mean ∇×V or A. That
is an editorial obligation at adoption time, not a physics obstacle.

## 5. Side finding — a registry error worth correcting

**OPEN-SS-8 lists "Dependencies: None blocking."** That is wrong. It is blocked on a spin
attribute CPP does not have — the founder's own words at 4107: *"we had not assigned a spin to
any CP, whether ZBW or not."* The entry has carried a HIGH priority and an empty dependency
field while being unreachable in principle. Corrected in `frontier_sectors/SS.md`, and filed
as **TODO-4112-SS8DEP**.

This is the same failure shape the lane hit at 4102: an item whose stated route quietly
presupposes something the corpus lacks, carried forward because nothing downstream contradicts
it.

## 6. Status

**TODO-4111-BCONFLICT: CLOSED, no conflict.** The axiom question can now be put to the founder
without this outstanding. Remaining unchecked at 4111: AP-5's saturation budget versus +33%
broadcast content.

No verdict moved. Nothing adopted. **F5 still untouched and still χ₄'s blocker.**
