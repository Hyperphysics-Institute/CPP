# A_i Is Not Independent of ∇ × V_i — INDEPENDENCE Resolved

**Patch:** 4179. **Lane:** EW/GR. **Session:** 234.
**Resolves:** TODO-4178-INDEPENDENCE — the single question A3′'s channel rested on.
**Verify:** `series_standard_model/code/4179_independence.py`.

---

## 1. The decomposition that settles it

Any axial field splits (Helmholtz) as **A = ∇ × (something) + ∇φ_A**.

- The **first** piece is exactly what **∇ × V_i** already supplies.
- The **second** is longitudinal, and its potential **φ_A is a pseudoscalar** — because A is axial
  and ∇ is polar.

> **So A_i's only independent content is a pseudoscalar potential.**

## 2. And a pseudoscalar is exactly what 4172 excluded

4172 §§1–3: the channels are the pieces of the matter source, and **T_μν contains no pseudoscalar**
— which is *why* A_u, the l = 0 odd irrep, is absent from the packet on principle.

**A_i's independent part needs the very source the source principle rules out.** Its transverse part
duplicates ∇ × V_i; its longitudinal part cannot be sourced. **Either way it carries nothing new
that matter can excite.**

## 3. The degree-of-freedom count, on CPP's own shell

For a plane wave, (∇ × V)(k) = i k × V(k), rank **2 of 3** — the component along k is annihilated.
Checked over 2000 random k: min 2, max 2.

**And the lattice does not change it.** Building the discrete curl on the actual 12-neighbour
icosahedral stencil and testing 2000 random k: **rank > 2 in 0 of 2000.** Same as the continuum.

So **∇ × V_i supplies two of A_i's three components at every wavevector**, and the missing one is
the longitudinal, pseudoscalar mode.

## 4. Verdict

> **A_i is not independent of ∇ × V_i in any part that matter can excite.**

**The one remaining loophole, and it is not attractive.** A longitudinal mode can carry *free*
radiation with no source. But a longitudinal mode of a propagating field is the classic
ghost/non-dynamical case — **precisely the second exposure Patch 4174 named and nobody has
examined.** So the loophole, if taken, converts A3′'s channel from *redundant* to *carrying a mode
that is probably a ghost*. **Neither is a case for keeping it as written.**

## 5. What this does not touch — stated again because it keeps mattering

**A1′'s carried attribute is the ZBW circulation's *sense*: a sign, not a field.** It is not a
component of any vector field and is not obtainable from ∇ × V_i. b needs it (4165). **A1′ is
unaffected by every result in this arc and remains load-bearing and cheap.**

## 6. Where this leaves the founder's ruling

The founder kept A3′ on realism: *"if the argument describes reality."* Following that criterion to
its end:

- the **empirical** support was near-empty (4155, 4165, 4170, 4175);
- the **structural** support fails on CPP's own ZBW radius — spin here is resolved circulation, hence
  orbital, hence already in V_i (4178);
- and the **independence** support fails too — the axial content is ∇ × V_i up to an unsourceable
  longitudinal mode (this patch).

**Every support the channel has been given has now been tested and none holds.** That is a
recommendation to restate or retire A3′'s amendment, and **it is the founder's call, not mine.** The
recommendation is not "χ₄ is wrong" — A1′ carries χ₄'s physics intact.

## 7. PD-008 — the convenient branch, marked

The founder ruled to keep the channel one patch ago. The convenient branch was to run this check,
find the loophole, and report it as *"independence is possible via the longitudinal mode"* — true in
letter, and it would have let the ruling stand. **I have instead said what the longitudinal mode
probably is.** I have also stated in §6 that every support has failed, which is the strongest claim I
have made about the amendment all session, and I want it read alongside §5: **the part of χ₄ that
does the physics is untouched.**

## 8. Status

TODO-4178-INDEPENDENCE **resolved: not independent.** No verdict moved — nothing here contradicts
data. χ₄ provisionally adopted. **F5 remains the blocker.**
