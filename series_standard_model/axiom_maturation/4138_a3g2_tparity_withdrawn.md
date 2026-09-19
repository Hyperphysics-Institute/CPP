# A3G-2's T-Parity Protection Is Withdrawn — Its Own Script Printed the Refutation

**Patch:** 4138. **Lane:** EW. **Session:** 234.
**Withdraws:** the T-parity argument recorded for TEST-A3G-2 (Patch 4125).
**Found while working:** TODO-4137-FILTERTABLE.
**Verify:** `series_standard_model/code/4138_a3g2_tparity_error.py`.

---

## 1. The error

4125 recorded, and four later patches cited:

> *"The spin-dependent forces that torsion balances and comagnetometers actually bound are the
> T-odd ones — monopole-dipole A·r̂ and spin-velocity A·v. χ₄'s b is T-even (F6) and the response
> is linear in b (B3), so a T-even carrier cannot source a T-odd potential. **A3G-2 PASSES.**"*

Its own verify script, `code/4125_a3g2_spin_dependent_force.py`, sets
`T = {'A': -1, 'V': -1, 'r': +1, 'v': -1}` and prints, in its own output table:

```
A.v        spin-velocity  Axv               -1  +1   chi_4 CAN source (matches b: P-odd, T-even)
```

**T = +1. T-even.** The prose two paragraphs below the table asserts the opposite. The table was
printed and not read. A second row, (A × v)·r̂, is also recorded as T = −1 in the 4125 document
and computes to T = +1.

## 2. And the finding needs no new input — it follows from F6

This is not my parity convention against 4125's. It is 4125 against itself, and against F6:

- **F6** (from CPT, Patch 4085): b = A·V is **T-even**.
- **A** is the ZBW spin (Patch 4112 — the spin half of ⟨L̂ + 2Ŝ⟩), so **A is T-odd**.
- Therefore **V is T-odd** — which is also what V *is* physically: the displacement per Moment
  (`master_glossary`, A1′ division of labor). 4125's own dict says so.
- Then **A·v — the same contraction, the same parities — is T-even too.**

**A·v and A·V are not two different objects. b IS a spin-velocity pseudoscalar.** So "comagnetometers
bound A·v, and χ₄ cannot source it" is self-refuting: the bounded object and the carrier are the
same invariant. To make A·v T-odd you would need A·V T-odd as well — that is, **not-F6**. F6 and
A3G-2's stated protection cannot both hold.

## 3. What survives, checked term by term

- **A3G-3 STANDS.** Its protection is that an EDM is P-odd **and T-odd**: EDM ~ A·E with E
  T-even gives A·E at P−1, T−1. Genuinely T-odd. Untouched.
- **A3G-2's monopole-dipole row STANDS.** A·r̂ with r̂ T-even is genuinely T-odd.
- **A3G-2's spin-velocity row FAILS.** That is the row the comagnetometer bound actually bites on.

## 4. What this does and does not establish

**Does:** the argument recorded for A3G-2's pass is invalid. **A3G-2 returns to UNRUN, not
FAILED.** Firing it requires showing the predicted spin-velocity coupling *exceeds* the
comagnetometer bound, and I have not shown that. Filed as **TODO-4138-A3G2MAG**.

**One candidate rescue, and note where it routes.** If the filter table holds and only the
*transient bracelet* channel reads b, there is no **long-range** spin-dependent potential between
separated masses at all — and comagnetometer bounds constrain long-range couplings. That would
save A3G-2 on structure rather than on T-parity. It is a candidate, not a closure, and it is
conditional on **the very filter table TODO-4137-FILTERTABLE was opened to derive.** The table now
carries five results.

## 5. Correction to Patch 4136, made here

4136 listed four SPINORIENT routes and closed three, with **A·v** among the two closed by F6 + B3.
That closure goes. But the count was wrong in a way that cushions the loss: **routes 2 and 4 were
never distinct** — A·v and A·V are the same invariant, as §2 shows. So SPINORIENT has **three**
distinct routes, not four: A·r̂ (closed, T-odd), (A·V)² (closed by the even-exponent argument,
independently of F6/B3), and A·V (open, and conditionally bounded at 4137 via BINENERGY).

**Substance unchanged: one open route, conditionally bounded.** The arithmetic was wrong, not the
position. I record it that way rather than as a silent renumbering.

## 6. What this says about the session's own diagnosis

4136 reported the headline as *premise concentration* — F6 + B3 carrying a third result. That
diagnosis was wrong, and in an instructive direction. **F6 is fine.** The problem was never that
F6 carried too much weight; it is that a step was recorded as *following from* F6 which in fact
**contradicts** F6. Concentration would have been a fragility. This was an error, sitting inside
the concentration, and concentration-counting would never have found it — only recomputing the
table did.

**Suite status drops: four of nine stand, not five.** (A3G-1 no fire; A3G-3, A3G-7 pass; A3G-9
negative. A3G-2 back to unrun; A3G-8 withdrawn at 4128; A3G-4/5/6 unrun.)

## 7. PD-008 — the convenient branch, marked

Overwhelmingly convenient to leave alone: A3G-2 was recorded as passing, three sessions had cited
it, and I found the defect while working an unrelated item. Nothing forced me to open a script
whose conclusion I had already used twice today. The inconvenient branch is the true one, and the
cost is that a falsifier the founder authorised at 4115 is back on the board unrun.

**The lesson that generalises, and it is worth the next window's attention:** the failure was not
a wrong premise but a *computed table whose prose summary inverted it*. Reasoning capture caught
nothing because the capture was of the prose. **Any patch whose conclusion rests on a script's
classification table should reproduce the table's rows in the document, not paraphrase them.**
Filed as **TODO-4138-TABLEPROSE**.

## 8. Status

χ₄ **provisionally adopted** — and now with one fewer falsifier passed than the record showed.
Nothing here fires it; A3G-2 is unrun, not failed. No verdict moved. **F5 remains the blocker.**
