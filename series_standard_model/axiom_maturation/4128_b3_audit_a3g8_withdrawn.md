# B3 Audit — A3G-8 WITHDRAWN. The amendment needs A_i quantized.

**Patch:** 4128. **Lane:** EW/QM. **Discharges:** TODO-4127-B3AUDIT.
**Withdraws:** TEST-A3G-8 (Patch 4127, mine, one turn old).
**Verify:** `series_standard_model/code/4128_b3_audit.py`.

---

## 1. What B3 actually says

B3 (Patch 4076), verbatim: *"Let a process rate be R(b). Parity violation appears in
observables **iff R depends on b linearly**… The response must be odd — linear — in the spin
bit."*

**B3 is a necessary condition for parity violation.** It says: to get V−A, the *parity-violating*
response must be odd in b. It does **not** say no interaction may read anything else about A.

## 2. What A3G-8 needed it to say

A3G-8 concluded *"the only function of A that any interaction reads is sign(A·V)"* — hence
same-b CPs are indistinguishable, hence strict exclusion, hence exactly two slots.

That is far stronger than B3 licenses. **B3 constrains the P-odd sector only. It is silent on
P-even couplings.**

## 3. And a P-even coupling that reads A already exists — established by my own A3G-2

Patch 4125 established that **A₁·A₂ is P-even, T-even, and is ordinary magnetic dipole-dipole** —
a real coupling the amendment supplies the carrier for. It depends on the **directions** of A₁
and A₂, not on sign(A·V).

> So two CPs sharing b but differing in A **are** distinguishable — by their mutual magnetic
> dipole interaction. They are not in the same quantum state, and strict exclusion does not
> apply.

**A3G-8's resolution fails. The two-slot result does not follow from the amendment as written.**

## 4. Why real QM gets two slots and this does not

In QM an electron's spin direction is continuous, yet Pauli gives exactly two states per orbital
— because spin-½ lives in a **two-dimensional Hilbert space**. The continuum of directions is a
continuum of *superpositions* of two basis states, not a continuum of independent states.

| | state space |
|---|---|
| classical axial 3-vector (what the amendment states) | S² — a continuum |
| spin-½ (what Pauli doubling needs) | **2** |

These are different objects, and only the second gives Pauli doubling.

## 5. Verdict and consequence

- **A3G-8: WITHDRAWN.**
- **The amendment needs an addition: A_i must be QUANTIZED** — a two-state spin-½ object, not a
  classical axial vector. That requirement is **not presently in A1′/A3′/AP-4** and must be
  added for Pauli doubling to hold. Filed as **TODO-4128-QUANTIZE**.
- **A3G-2 and A3G-3 STAND.** They used B3 only for the T-parity argument — that a T-even carrier
  cannot source a T-odd term at linear order — which is exactly what B3 licenses.

The concentration I flagged at 4127 was real, and it broke in **exactly one** of the three
places: the one where I had stretched B3 beyond its own statement.

## 6. Note

This is the fifth self-correction this session, and the second in two patches. The cause is the
same each time — a premise assumed to say more than it says, or tested on a configuration other
than the corpus's own. That the audit I recommended *found its own target* is the process
working; that the target was my patch from one turn earlier is worth the next window knowing.

**Suite status: five of nine stand** (A3G-1 no fire; A3G-2, A3G-3, A3G-7 pass; A3G-9 negative).
A3G-4/5/6 unrun. χ₄ remains provisionally adopted — but its QM payoff is now **conditional on
TODO-4128-QUANTIZE**, not delivered.

No verdict moved. F5 remains the blocker.
