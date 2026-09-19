# Does Whatever Reads b Reach the Internal Energy? — TODO-4136-BINENERGY

**Patch:** 4137. **Lane:** EW/SS. **Session:** 234.
**Answers:** TODO-4136-BINENERGY — **conditionally**, and the condition is the limit of the result.
**Verify:** `series_standard_model/code/4137_binenergy.py`.

---

## 1. The question

4136 closed three of the four routes by which the A_i channel could break R-F3-ISO. The fourth —
an **A·V** term (b itself) in a structure's internal energy — is P-odd and **T-even**, so
T-parity cannot touch it, and excluding it by assumption is circular, since such a term *is*
hadronic parity violation. It sits upstream of F3, A3G-2 and A3G-3 alike, which is why it was
taken before the cage-moment refinement.

## 2. The structural step, and it is the only CPP-internal content here

The corpus's filter table (`chirality_axiom_maturation` §2aa) says exactly one channel reads b
linearly:

| interaction | partner | ⟨b⟩ | reads b? |
|---|---|---|---|
| weak (W bracelet) | **free** | ≠ 0 | **linear in b** |
| EM (sea exchange) | confined | 0 | magnitude only |
| strong (cage hop) | confined | 0 | cage SSV dominates |

If that holds, a P-odd term in a *nucleon's* internal energy cannot come from the strong or EM
channel at all. It has to pass through **bracelet formation** — and is therefore routed through
the weak scale rather than left free. That routing is the whole of this patch's contribution.

## 3. The size — imported, not derived, and I checked

Weak-channel suppression at the hadronic scale: G_F m_π² = **2.27×10⁻⁷**, G_F f_π² = 1.98×10⁻⁷.
The textbook hadronic-PV scale, as it must be.

**Is that a CPP prediction? No.** SF-2 derives the *ratio* m_Z/m_W = 1.1405 at zero parameters
against 1.1344 observed — but m_W itself is **calibrated via η_W** (SF-2 scorecard: *"m_W =
80.377 GeV (calibrated via η_W)"*). The weak scale is an input to CPP, not an output. So the
10⁻⁷ is imported. What is CPP-internal is only the channel argument in §2.

## 4. And the comparison does not have slack

4136's bound was ε ≤ 1×10⁻⁷ / |W| = **8.6×10⁻⁸**. The weak-channel estimate is 2.27×10⁻⁷ — a
**factor 2.6 on the wrong side of the bound it has to respect.**

With O(1) coefficients unknown on both sides that is agreement at order of magnitude, and I am
not going to dress it up as more. What it does say is worth stating in both directions:

- the unknown coefficient **cannot be much larger than 1** — a real, if weak, constraint;
- there is **no room for a CPP-extra P-odd contribution** on top of the weak admixture, which
  already accounts for the observed hadronic PV.

## 5. The caveat that bounds the whole result

**The filter table is not established corpus.** Its own status line reads *"Status: CONDITIONAL"*
and records the founder's response as *"I have no explanation"* (session 233). It is a worker
proposal. Every step above inherits that conditionality: BINENERGY is answered **conditional on
the filter table**, not outright, and nothing here upgrades the table. If the table is wrong —
if the strong channel reads b after all — route 4 reopens with nothing bounding it.

## 6. What this is worth, and what it is not

**Worth:** route 4 moves from *unbounded and circular* to *bounded by a channel argument,
conditional on the filter table*. That is a genuine improvement on 4136's position.

**Not:** a derivation. The 10⁻⁷ is imported through a calibrated m_W; the O(1) coefficient is
unknown; the estimate sits a factor 2.6 on the wrong side; and the channel argument is itself
conditional. **R-F3-ISO is therefore not independently secured**, and F3 continues to rest on the
same empirical bound it is trying to explain. Anyone reading the last four patches as "F3 is
derived" is reading them wrong: F3 is *better characterised* than at session start, and the thing
it rests on has moved from an unanswered picture question to a named requirement with a partly
bounded failure mode. That is progress, not closure.

## 7. PD-008 — the convenient branch, marked

The convenient result was the consilience: *the 10⁻⁷ that R-F3-ISO needs as a bound is the same
10⁻⁷ the weak channel supplies — CPP produces its own protection.* That sentence is available and
would read well. **It is not independent evidence:** the observed hadronic-PV bound and G_F m_π²
are the *same empirical fact* approached from two sides, and the weak scale is calibrated rather
than predicted. I record the routing as structure and the number as imported, separately, and the
next window should check that I kept them apart.

## 8. Status

F3 unchanged, better characterised, not closed. **TODO-4136-BINENERGY answered conditionally**;
the residual is filed as **TODO-4137-FILTERTABLE** — the filter table is load-bearing for F3,
A3G-2, A3G-3 and now BINENERGY, and it is a conditional worker proposal the founder has declined
to endorse. Upgrading or refuting it is now the lane's highest-leverage item. No verdict moved.
χ₄ provisionally adopted. **F5 remains the blocker.**
