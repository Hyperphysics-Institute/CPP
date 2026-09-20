# Does the A_i Channel Earn Its Place? — CHANNELJOB Pressed

**Patch:** 4171. **Lane:** EW. **Session:** 234.
**Answers:** TODO-4165-CHANNELJOB.
**Verify:** `series_standard_model/code/4171_completeness_audit.py`.

---

## 1. The amendment has two supports, and this session weakened the first

The empirical case for A_i is now clear and it is thin. Its identified jobs:

- **sourcing A₁·A₂** — ordinary long-range magnetic dipole–dipole, which the corpus already had (4125);
- **the environmental term in the spin-evolution rule** (the founder's proposal, 4166) — **bounded at
  ε ≤ 5×10⁻⁴⁷ per Moment** (4170).

Neither is a distinctive prediction. And b — the one construction that would have been distinctive —
**does not read the register at all** (4165, 4166, corrected 4168). So the empirical support is
near-empty.

That leaves the **structural** case from 4120: A_i *completes* A3′ over the full point group I_h.

## 2. The structural case is sound in form

LSP′'s components with parity made explicit:

| component | indices | parity | irrep | l | dim |
|---|---|---|---|---|---|
| Φ = g_tt | none spatial | even | **A_g** | 0 | 1 |
| V_i = g_ti | one | odd | **T₁u** | 1 | 3 |
| Q_ij = g_ij | two | even | **H_g** | 2 | 5 |
| **A_i** (4120) | axial | even | **T₁g** | 1 | 3 |

The original enumeration used the **rotation** group I, under which polar and axial 3-vectors are
the same irrep T₁. Under I_h they are inequivalent. **4113's observation is correct.**

## 3. But it proves more than the amendment does

If the defect was that a rotation-only enumeration cannot see parity, the fix is to enumerate
l ≤ 2 **with both parities**:

| l | even | odd | in the packet? |
|---|---|---|---|
| 0 | A_g — Φ ✓ | **A_u (pseudoscalar)** | **NO** |
| 1 | T₁g — A_i ✓ | T₁u — V_i ✓ | both ✓ |
| 2 | H_g — Q_ij ✓ | **H_u (odd rank-2)** | **NO** |

**Two parity partners remain missing after the amendment: A_u (dim 1) and H_u (dim 5).** Neither is
added; neither is discussed. So:

- **(a)** there is a principle selecting T₁g and excluding A_u and H_u — in which case *that* is the
  argument, not completeness, and it should be stated; or
- **(b)** completeness is the argument, and **A3′ is still incomplete after the amendment**, by two
  channels.

The corpus states (a) nowhere I have found. 4113's text addresses T₁u vs T₁g specifically and says
nothing about l = 0 or l = 2.

## 4. What the missing two would be — and they are not idle

**A_u, a pseudoscalar broadcast** — the parity partner of Φ. A scalar that changes sign under
reflection: structurally an axion-like channel. **If it existed it would give a P-odd term with no
axial vector needed, competing directly with b as the source of chirality.** That is a live rival to
the amendment's own mechanism, from inside the amendment's own argument.

**H_u, an odd rank-2** — the parity partner of the radiative tensor. It would be a **parity-odd
gravitational-wave polarisation**, and those are tightly bounded by LIGO/Virgo birefringence
searches. So one missing channel competes with χ₄'s mechanism and the other is already constrained
by data.

## 5. Verdict on CHANNELJOB

**This is not a refutation of χ₄.** It is a statement that the amendment's two supports are each
weaker than they looked:

- the **empirical** support is near-empty — magnetism the corpus already had, plus an effect bounded
  at 10⁻⁴⁷;
- the **structural** support is sound in form but **incomplete in application** — the same argument
  asks for three channels, and one was added.

**Recommendation: before χ₄ is ratified beyond provisional, either state the principle that selects
T₁g alone, or add A_u and H_u and face the gravitational-wave birefringence bound on H_u.** Filed as
**TODO-4171-PARITYPARTNERS**.

## 6. PD-008 — the convenient branch, marked

The convenient branch was to leave CHANNELJOB as an open worry. It had been registered twice and
nobody was pressing it; the session had already produced enough corrections. Pressing it turns a
vague discomfort into a specific structural gap in the amendment I have spent this session
defending, and §4 is worse than the gap itself — the pseudoscalar channel the argument demands would
be a **rival** to b, not a supplement to it.

## 7. Status

TODO-4165-CHANNELJOB **answered**. No verdict moved — and this does not fire a falsifier, since
nothing here contradicts data. χ₄ **provisionally adopted**, with both supports now honestly sized.
**F5 remains the blocker.**
