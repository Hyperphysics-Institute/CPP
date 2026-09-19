# TEST-A3G-2 — Spin-Dependent Force. Passes. And a caveat about the suite itself.

**Patch:** 4125. **Lane:** EW. **Third and last falsifier** of the three authorized at 4115.
**Verify:** `series_standard_model/code/4125_a3g2_spin_dependent_force.py`.

---

## 1. Result

Classifying the leading spin-dependent potentials buildable from the broadcast content:

| potential | P | T | can χ₄ source it? |
|---|---|---|---|
| **A₁·A₂** (spin-spin) | +1 | +1 | P-even/T-even — **ordinary magnetic dipole-dipole**, already exists |
| (A₁·r̂)(A₂·r̂) tensor | +1 | +1 | same — ordinary |
| **A·r̂** (monopole-dipole) | −1 | **−1** | **T-ODD → cannot source** |
| **A·v** (spin-velocity) | −1 | **−1** | **T-ODD → cannot source** |
| (A × v)·r̂ | +1 | −1 | T-odd → cannot source |
| A·V | −1 | +1 | matches b — but this is the *local* bit, not a force between masses |

**The spin-dependent forces that torsion balances and comagnetometers actually bound are the
T-odd ones** — monopole-dipole A·r̂ and spin-velocity A·v. χ₄'s b is T-even (F6) and the
response is linear in b (B3), so a T-even carrier cannot source a T-odd potential.

What A_i *does* mediate — A₁·A₂ — is ordinary magnetic dipole-dipole. Measured, expected, not a
fifth force. This is consistent with Patch 4112: A_i is the spin half of ⟨L̂ + 2Ŝ⟩, supplying
the carrier for a coupling physics already has.

**A3G-2 PASSES.**

## 2. All three falsifiers are now run — and none fire

| test | result |
|---|---|
| A3G-1 vacuum magnetisation | does not fire |
| A3G-3 EM parity | passes — T-parity |
| A3G-2 spin-dependent force | passes — T-parity |

## 3. The caveat, and it matters for the adoption decision

**Two of the three pass by one and the same structural fact: F6's T-even signature for b.**

That is less independent evidence than "three falsifiers passed" sounds. If F6 is wrong, A3G-2
and A3G-3 reopen **simultaneously**. The suite's protection is concentrated, not distributed.

Two things partly offset this, and I record them without overstating:
- F6 was derived from CPT at Patch 4085 for unrelated reasons, weeks before these tests existed.
- The same P-odd/T-even signature was independently reproduced by the A·V construction at 4111.

But offsetting is not the same as independence. **The honest summary is: one load-bearing
premise carries two of the three falsifiers.**

And the **linear-order caveat (TODO-4124-QUADRATIC) applies to both of them**, not just A3G-3 —
a response quadratic in b is T-even × T-even = T-even and is excluded by neither.

## 4. Is this a "clean win"? Not yet — and per the founder's own standard that matters

The 4093 standard is *adopt only after a clean win*. What has actually been established:

- **Falsifiers: 3 run, 0 fire** — but 2 share a premise and both carry the linear-order caveat
- **Consistency tests A3G-4/5/6: UNRUN** (AP-4 division; SF-6 disambiguation sweep; F3 re-derivation)
- **Payoff tests A3G-7/8: UNRUN** — and A3G-7 (nucleon magnetic moments) is the strongest
  empirical test in the whole suite
- **A3G-9: effectively answered negatively** at 4121 (the axiom does not make DP-CAL-1 derivable)

So the suite is **one-third complete**, and the part completed is the part that can only
*fail* — passing falsifiers removes objections, it does not supply positive evidence.
**A3G-7 is where positive evidence would come from, and it has not been run.**

χ₄ remains **provisionally adopted**, which is the correct status: the falsifiers have not
withdrawn it, and the payoff tests have not yet earned full adoption.

## 5. Next

**A3G-7 (nucleon magnetic moments)** should be next — it is the only test in the suite that
can produce a number to compare against experiment (μ_p = +2.793 μ_N, μ_n = −1.913 μ_N), and
it targets a registered prediction still marked "to derive."

No verdict moved. **F5 remains the blocker.**
