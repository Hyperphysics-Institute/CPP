# The Register Contains Its Own CP — 4165 Repaired, and a Bound on the Founder's Mixing

**Patch:** 4166. **Lane:** EW. **Session:** 234.
**Corrects:** Patch 4165 §2 (the premise, not the verdict).
**Verify:** `series_standard_model/code/4166_register_composition.py`.

---

## 1. The correction is right, and it removes 4165's argument

4165 §2 asserted that a GP's resident CP does not send itself a DI-bit, so its own A is absent from
its own GP's register. **The founder's objection is decisive: the GP must know its resident CP's
attributes or it could not imprint them on outgoing DI-bits — and then a charge could not radiate
its presence at all.** EM would not work. The register is **(own CP) + (arrivals)**. 4165 §2 is
withdrawn.

## 2. The verdict survives, on a better argument: dilution

In an unpolarised sea the arrivals sum to a random vector of magnitude ~√N while A_CP is a single
unit contribution. So the register's correlation with the CP's own spin is **diluted by the
neighbour count**:

| N arrivals | corr(register, own spin) | V−A would be |
|---|---|---|
| 4 | 0.259 | 25.9% |
| **12** | **0.154** | **15.3%** |
| 60 | 0.069 | 6.9% |
| 600 | 0.022 | 2.2% |

**If b read the register's axial content, V−A would be ~15% of maximal at the generic N = 12, not
100%.** The measured coupling is maximal. **So b reads the CP's own A.**

4165's verdict stands; 4165's reason does not. And the replacement is stronger — it does not depend
on any claim about what the register contains, only on the arithmetic of mixing one signal with
twelve random ones.

## 3. The founder's mixing proposal, and the bound it must respect

> *"the two add, the environmental axial vector and the CP axial vector mix in some proportion, and
> that is the axial vector carried by the CP to its next location after the V_i displacement."*

This is a **spin-evolution rule**: A_next = normalise((1−ε)A + ε·A_env). In an unpolarised sea A_env
is random, so the rule produces **spin relaxation** — and spin relaxation is measured to
extraordinary precision.

Random-walk estimate: angular variance accumulates as ε²n, coherence lost when ε²n ~ 1.

| experiment | t (s) | tolerance | n Moments | ε ≤ |
|---|---|---|---|---|
| muon g−2 storage ring | 10⁻⁵ | 10⁻¹⁰ | 1.9×10³⁸ | 7×10⁻²⁵ |
| neutron polarimetry flight | 10⁻¹ | 10⁻³ | 1.9×10⁴² | 2×10⁻²³ |
| electron spin, Penning trap | 10³ | 10⁻⁶ | 1.9×10⁴⁶ | 7×10⁻²⁷ |

**The environmental mixing fraction is bounded below ~10⁻²⁴ per Moment.** The proposal is allowed —
but only at a level where the CP's own A is conserved to some twenty-four decimal places each
Moment. **The environment cannot meaningfully rotate a spin on the Moment timescale.**

## 4. What the proposal buys

- **It repairs 4165** without changing its answer, on a premise the founder supplied rather than one
  I mis-assumed.
- **It gives the A_i register a second job** — which is exactly what TODO-4165-CHANNELJOB was
  asking. The register is the **environmental term in the spin-evolution rule**. Thin, but real,
  and better than "magnetism only."
- **It makes spin relaxation a CPP observable with a number attached.** Any measured
  spin-relaxation rate *not* accounted for by known mechanisms would bound ε **from below** — so the
  rule is falsifiable, not merely permitted.

## 5. What I have not done

The ε bound is a **random-walk estimate, not a derivation** from the corpus's own DI-bit statistics:
I assumed A_env is random and **uncorrelated Moment to Moment**. If environmental axials are
*correlated* over many Moments — which a nearby polarised medium would make them — the walk becomes
ballistic and the bound tightens by a further √n, i.e. by up to nineteen orders. **That is the case
worth computing next, and it is where a real prediction would live**: a spin in a polarised medium
should relax faster than one in vacuum by a calculable factor. Filed as **TODO-4166-MIXING**.

## 6. PD-008 — the convenient branch, marked

The convenient response to a founder correction that removes my argument is to find a replacement
argument and present the whole thing as a refinement. §2 *is* a replacement argument and I think it
is right, but §1 says plainly that the original was wrong and why. The genuinely inconvenient part
is §5: the bound I computed is the *loose* version, and the tight version — correlated environments
— is the one that could actually fire against the proposal I have just endorsed.

## 7. Status

TODO-4165-CHANNELJOB **partially answered** (the register has a second job). No verdict moved.
χ₄ provisionally adopted. **F5 remains the blocker.**
