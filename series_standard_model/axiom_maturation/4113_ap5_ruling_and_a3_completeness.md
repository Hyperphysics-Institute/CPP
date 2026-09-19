# Two Rulings Under PD-006 — AP-5 Saturation, and A3′'s Parity-Blind Completeness

**Patch:** 4113. **Lane:** EW. **Founder:** *"I have no way of ruling on this. You'll have to
make this judgment as per PD-006 or 007 or 008."*
**Verify:** `series_standard_model/code/4113_a3_parity_blindness_verify.py`.
**Discharges:** the AP-5 item left unchecked at 4111.

---

## RULING 1 — AP-5's saturation budget is arrival-count based. Option B does not breach it.

**What AP-5 governs, in its own words:** *"the case where more [DI-bits] **arrive** in one
Moment than [the GP] can **act on**."* Its derived quantity is a **depth**, ⌈1.5 v⌉, tied to v.
D1 **clips** the acted-on displacement; D3 **relays the packet whole**; D4 **stores** the held
sector in registers.

**The judgment.** A fourth irrep changes **what each DI-bit carries**, not **how many arrive**.
Arrival count is set by the PSR shell population — geometric, and unchanged by packet content.
**No saturation threshold is crossed. AP-5 is not violated by Option B.**

**The honest residual, because this is a ruling and not a clean bill.** AP-5 quantifies **no
per-content cost at all**. D3's whole-relay and D4's register storage would each carry 33% more
content per Moment, and there is nothing in AP-5 to measure that against. The correct finding
is therefore **not "free" but "unbudgeted"**: AP-5 cannot be violated by Option B because AP-5
does not constrain content size. If a future result makes per-content cost matter, this ruling
does not protect it. Filed as **TODO-4113-CONTENTCOST**.

---

## RULING 2 — A3′'s completeness claim is parity-blind, and the omitted irrep is exactly what χ₄ needs

Reading A3′ closely for the AP-5 question turned up something larger. A3′ states LSP′ is

> *"the complete set of rotationally protected irreps of the lattice point group
> (**A ⊕ T₁ ⊕ H = 1+3+5 = 9 dynamical components**)"*

That is the decomposition of {scalar, vector, symmetric rank-2} under the **rotation** group I.

**Verified computationally** (|I| = 60, |I_h| = 120, both built explicitly):

| | χ_polar vs χ_axial |
|---|---|
| on the **proper** group I | **identical**, max difference 4.4×10⁻¹⁶ |
| on the **full** group I_h | **inequivalent irreps**, overlap exactly 0; each irreducible (self-overlap 1.0000) |

**A rotation-only enumeration cannot distinguish a polar vector from an axial one.** Under the
full point group — the actual symmetry of the icosahedral lattice, its 60 improper elements
included — they are *different irreps*: polar = T₁_u, axial = T₁_g. **A3′ carries T₁_u only.**

> **Option B's A_i is precisely the T₁_g channel A3′ omits. The amendment is not an arbitrary
> addition — it COMPLETES A3′ with respect to the full point group.**

A3′'s word "complete" is true for rotations and false for I_h. That is not an error in A3′ so
much as an unstated scope: it enumerated what rotations protect, and parity was never in view.

## Why this matters for the decision

It changes the character of what would be put to the founder. The question is no longer *"shall
we bolt a new channel onto a ratified axiom?"* but:

> *"A3′ claims completeness over the lattice point group but enumerates only the rotation
> group's irreps. Under the full group one irrep — the axial vector T₁_g — is missing. Shall
> A3′ be completed?"*

That is a smaller and better-posed question, and it explains why χ₄ kept needing something
that felt both absent and natural: the channel it wants is the one the completeness claim
skipped.

## Status

Both items the 4111 scoping left open are now closed or filed. **The axiom question is ready to
be put**, with:

- form: Option B, matched across A1′/A3′/AP-4 (Patch 4111)
- magnetism conflict: none — orbital and spin halves of ⟨L̂ + 2Ŝ⟩ (Patch 4112)
- AP-5: not breached, unbudgeted (Ruling 1 above)
- character: a **completion** of A3′, not an addition (Ruling 2 above)

No verdict moved. Nothing adopted. **F5 remains χ₄'s blocker and none of this touches it.**
