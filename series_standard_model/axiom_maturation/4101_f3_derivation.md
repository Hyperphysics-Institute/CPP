# F3 Formal Derivation — Strong-Sector P-Evenness from Cage Antipodal Pairing

**Patch:** 4101. **Lane:** EW. **Block:** 4100–4199 (first physics patch).
**Owed since:** Patch 4096 (TODO-4096-F3), founder-endorsed at Patch 4097.
**Verify:** `series_standard_model/code/4101_f3_derivation_verify.py` (ALL CHECKS PASS).
**Status:** F3 **DERIVED** — conditional on ONE named, sharp, falsifiable requirement.

---

## 1. What was owed

Patch 4097 gave the physical mechanism on the founder's ruling: velocity is not intrinsic
to a CP, so the helicity bit is b = sign(ω · v_arcs), read off the DP arc cohort. Free
particles have a persistent cohort; confined quarks have theirs continuously severed and
re-established. The *formal* step — that the confined average is actually zero, and how
exactly zero — was owed.

## 2. The derivation

**Step 1 — the cage shells are exactly antipodally paired.** SF-2's confinement cages are
the icosahedral 12-shell (Z-cage) and dodecahedral 20-shell (H-cage). Both are exactly
centrally symmetric as point sets: every bond direction v̂ has −v̂ in the same shell, to
machine precision (12/12 and 20/20).

**Step 2 — the bits cancel pairwise, not on average.** Since sign(ω · (−v)) = −sign(ω · v),
an antipodally paired equally weighted direction set gives Σ sign(ω · v̂) = 0 for **every** ω.
Tested against 20,000 random ω per shell: the sum is **exactly zero every time**, not small.
There is no averaging step and no thermal argument — the cancellation is algebraic.

**Step 3 — equal weighting is not a parity assumption.** The obvious worry is circularity:
if equal weighting came from assuming P-even cage dynamics, the derivation would assume its
own conclusion. It does not. The icosahedral **proper** rotation group I (|I| = 60, every
determinant +1) acts transitively on both shells — 12/12 and 20/20 orbits. No improper
operation appears anywhere in the argument. Equal weighting follows from the cage's own
rotation symmetry, which is independently derived in SF-2.

**Step 4 — the free particle does not cancel.** A free particle's arc cohort is a single
persistent direction, not an antipodal set. There is nothing to cancel against: |⟨b⟩| = 1.
The *same* linear coupling therefore gives maximal violation on a free leg and exactly zero
in a cage, with no separate stipulation for the two sectors. That is the content F3 needed.

## 3. The inconvenient branch — and it is the load-bearing one

The convenient result would have been "icosahedral symmetry gives the cancellation." **That
is false, and this is the finding that matters.**

I does not contain −I. Antipodal pairing is a property of the **special symmetry-axis
orbits** — the 12-shell (C5 axes), 20-shell (C3), 30-shell (C2) — and *not* of icosahedral
symmetry generally. Six generic I-orbits were tested: **0/60 paired in every case**, leaving
a residual bit sum of 6.7–10%.

So F3 carries a sharp requirement:

> **R-F3:** the confined quark's DP arc cohort must lie along cage **bond directions**
> (the 12/20/30 symmetry-axis shells), not in generic directions.

Given R-F3, ⟨b⟩ = 0 exactly. Without it, the strong sector would show parity violation at
the ~10% level. Observed hadronic parity violation is ~10⁻⁷ and is fully accounted for by
weak admixture, so an off-shell arc cohort overshoots the bound by roughly **six orders of
magnitude**. R-F3 is not a soft modelling preference; it is load-bearing and falsifiable.

The residual scales linearly with any antipodal imbalance ε (ε = 10⁻⁵ → ⟨b⟩ = 1.8×10⁻⁶),
so the hadronic PV bound caps any intrinsic cage imbalance at ε ≲ 10⁻⁷.

## 4. Status change

F3 moves from **CONDITIONAL — founder-endorsed** (Patch 4097) to **DERIVED, conditional on
R-F3**. The conditionality is different in kind: it is no longer "no formal argument exists"
but "the formal argument exists and rests on one named physical requirement that can be
checked and can fail."

F2 (EM sector) inherits the same structure: sea DPs carry arc directions from their last
interactions, and if those are isotropic the same pairwise cancellation applies. F2 is *not*
discharged here — isotropy of the sea's arc directions is a separate claim from R-F3 and is
not established in this patch.

## 5. What is now owed

**R-F3 is a PD-006(a) founder question** — physics framed in a physical picture. Filed as
TODO-4101-F3. The question: *when a confined quark is deflected by the cage, is the new DP
arc cohort established along a cage bond direction, or can it point in a generic direction?*
The corpus (SF-6) describes arc establishment during acceleration but does not say whether
the cage's bond geometry quantizes the resulting direction.

No verdict moved. χ₄ remains NOT panel-ready (F5 still open, OPEN-SM-11).
