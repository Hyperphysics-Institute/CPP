# TEST-A3G-8 — Passes. And B3 is now the amendment's single point of failure.

**Patch:** 4127. **Lane:** EW/QM. **Verify:** `series_standard_model/code/4127_a3g8_two_slot.py`.

---

## 1. The tension the test had to resolve

Patch 4098 got exactly **two** slots per spatial mode because χ₄'s b is binary. But A_i is a
**continuous** axial vector — its state space is S², not {+1, −1}. If two CPs at one GP are
distinguishable by their A *direction*, strict exclusion should not apply to them, and Pauli
doubling would become **Pauli unbounded**.

## 2. Resolution

The χ₄ response is **linear in b** (B3, Patch 4076), and b = sign(A·V). So the only function of
A that any interaction reads is **the sign of A·V**. A is continuous; the observable built from
it is binary.

Demonstrated: 200,000 continuous A directions collapse to exactly **2** distinct values of b,
balanced 50/50. Same-b pairs separated by up to ~180° in A produce **identical** responses —
indistinguishable to every interaction the axiom provides, hence the same quantum state, hence
strictly excluded.

> **Slot count is set by b, not by A. 120 spatial modes × 2 = 240 fermionic states —
> reproducing Patch 4098 exactly, now from the axiom rather than the bit.**

**A3G-8 PASSES.**

## 3. The finding that matters more than the pass

That resolution works **only** because the response reads nothing about A beyond sign(A·V).
That is **B3** doing the work. And B3 is now doing it in three places:

| test | rests on |
|---|---|
| A3G-2 (spin-dependent force) | **B3** + F6 |
| A3G-3 (EM parity) | **B3** + F6 |
| A3G-8 (two-slot/Pauli) | **B3** |

At 4125 I flagged that F6 carried two of the three falsifiers. **B3 is worse: it is the common
factor in all three of these results.** Six tests run, but the architecture underneath is far
less redundant than the count suggests.

**And B3's failure mode is the most severe in the suite.** If any interaction ever reads A's
*direction* rather than just sign(A·V), then same-b CPs become distinguishable, strict exclusion
fails, and Pauli doubling becomes unbounded. That does not merely refute the amendment — **it
breaks fermions.**

## 4. What follows

**B3 is now the single most load-bearing premise in the amendment, and its own support has not
been re-examined since Patch 4076.** It was established there as an answer to a founder
question, before A_i existed as an axiom attribute. Whether an argument for linearity in a
*binary bit* carries over to linearity in a quantity derived from a *continuous vector* is
exactly the sort of step this session has repeatedly found to fail when checked.

Filed as **TODO-4127-B3AUDIT**, and I would put it ahead of the remaining consistency tests
(A3G-4/5/6). Those test whether the amendment fits; this tests whether the three passes already
recorded are real.

## 5. Suite status

**Six of nine run.** A3G-1 does not fire; A3G-2, A3G-3, A3G-7, A3G-8 pass; A3G-9 answered
negatively. A3G-4/5/6 unrun.

Still not a clean win per the 4093 standard — and the concentration found here is a reason to
be *more* cautious about the passes, not less.

χ₄ remains provisionally adopted. No verdict moved. **F5 remains the blocker.**
