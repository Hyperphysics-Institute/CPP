# T-2 DELIVERED — the coefficient is **λ = α/κ**, not a free O(1)×α. The bath cannot exceed the substrate scale, so **κ ≤ 1 and λ ≥ α**: the bracket's entire lower half is excluded. At the bath clause's own reading (κ = 1) **λ = α exactly**, and the correction is a **systematic shift, not an error bar** — n_s: 0.9649 → **0.9654**. And it runs backwards into a new empirical result: the observed tilt **bounds the substrate bath temperature at kT ≳ 0.1 E_Pl**

**Patch 3850, Session 184, 9 Sep 2026. Lane: EU (fully local — no cross-lane input).** Discharges charter target **T-2**, specified at 3848. Verify `scripts/3850_t2_coefficient.py` (8/8; reuses the 0774 ZRP machinery verbatim). Reasoning `reasoning/3850_t2_coefficient.md`. Nothing adopted; **no constant minted** — κ is the bath clause's own parameter and is already a named leg of PRED-C-96. 3710 not retired.

## §1 The closure (verify T2)
T-2 asked for the O(α) occupation-dependence coefficient in the PCD→ZRP reduction, bracketed by EU-1 at 0.1α–10α. The bracket dissolves once two results already on file are put together, which nobody had done:

- **0774** deforms the ideal rate g(n) = n to g(n) = n(1 + λ(n−1)) and states λ ~ Γ, the plasma coupling.
- **0766** derives **Γ = α/κ** with κ ≡ kT_bath/E_Pl — and derives it *exactly*, because the corpus fixes a = l_P and hence, at kT = E_Pl, Γ = q²/(a·kT) = q²/(ℏc) = **α**. The fine-structure constant appears not as an order-of-magnitude stand-in but as an identity.

> **λ = α/κ.**

The coefficient was never a free O(1) multiple of α. **The 0.1α–10α bracket is κ ∈ [0.1, 10] — one parameter, not two**, and that parameter is the bath temperature.

*(This corrects 3848 §4, which stated that α here is "the SSV occupation-dependence parameter of the reduction, **not** the fine-structure constant." That was wrong: via Γ = q²/(a kT) at a = l_P it is the fine-structure constant, exactly.)*

## §2 A one-sided bound, from the bath's own definition (verify T3)
The bath in LEMMA-NS-BATH is the ZBW/substrate bath, whose clock is the substrate clock c/l_P. Its temperature therefore cannot exceed the substrate scale:

> **kT_bath ≤ E_Pl ⇒ κ ≤ 1 ⇒ λ ≥ α.**

**The bracket's entire lower half — 0.1α up to α — is excluded.** This is a genuine narrowing and it is one-sided, which the charter's expectation E-3 did not anticipate (it predicted a two-sided collapse to ~[0.5α, 2α]).

## §3 The value, and the fact that it is a shift (verify T4, T5)
At the bath clause's own Reading A (κ = 1):

> **λ = α exactly; η = 1.43×10⁻²; Δn_s = +5.0×10⁻⁴.**

And η > 0, so the correction has a **sign**. This is the part that matters:

> EU-1 quotes ~5×10⁻⁴ as a **symmetric theory uncertainty**. The derived object is a **one-sided systematic shift**: **n_s = 0.9649 → 0.9654**, which sits 0.12σ from the Planck central value.

The agreement survives comfortably. But "0.9649 ± 0.0005" and "0.9654" are different claims, and only the second is what the derivation supports. **EU-1's V1.x note is owed this correction**, and it is the first time in this arc that a derived result moves the paper's headline number rather than its scaffolding.

## §4 The result running backwards: a bound on the bath (verify T6)
Because λ = α/κ, the observed tilt constrains κ. Requiring Δn_s to stay within Planck's 1σ (0.0042) needs λ ≲ 9.7α, hence

> **κ ≳ 0.1, i.e. kT_bath ≳ 0.1 E_Pl.**

This is not a fit and does not violate PD-007 — nothing is tuned to match; an existing observation is used to *bound* a substrate parameter that the theory independently claims is of order E_Pl. **PRED-C-96's agreement with Planck is thereby converted into an empirical lower bound on the substrate bath temperature**, which the corpus did not previously have and which the bath clause can be checked against.

## §5 The structural finding (verify T7)
> **T-2's uncertainty is not independent. It is κ — the bath temperature — which is already a named conditionality leg of PRED-C-96** (the bath clause, LEMMA-NS-BATH; and its sharpening OPEN-EU-BATH-DEPTH-1, 3806).

So T-2 does not add a theory error to EU-1; it **re-expresses one already counted**. The prediction's conditionality does not grow by this work, and its three framework legs stay three. What changes is that the O(α) correction stops being an independent unknown bracketed by an order of magnitude and becomes a function of a quantity the framework already tracks.

## §6 What was delivered against the charter
Charter §2 asked for "the coefficient, **or** a derived bound tighter than 10α." Delivered:
- **the coefficient as a function**: λ = α/κ (§1);
- **a derived one-sided bound**: λ ≥ α, excluding the lower half of the bracket (§2);
- **a value at the bath clause**: λ = α, Δn_s = +5.0×10⁻⁴ (§3);
- **beyond the ask**: the shift is systematic not symmetric, moving the headline to n_s = 0.9654 (§3); an empirical bound kT_bath ≳ 0.1 E_Pl (§4); and the collapse of T-2's uncertainty onto an existing leg (§5).

**Not delivered:** κ itself. It is the bath clause's parameter and remains conditional — correctly so, since deriving it is OPEN-EU-BATH-DEPTH-1's business, not T-2's.

## §7 Standing
- **T-2 CLOSED** at the charter's stated deliverable and beyond it.
- **Owed to EU-1 at V1.x:** the headline moves from n_s = 0.9649 ± 5×10⁻⁴ to **n_s = 0.9654** (one-sided, at κ = 1), with the ± reinterpreted as κ-conditionality. **This is a change to the paper's quoted number and should not be folded in silently.**
- **3848 §4 corrected** (α *is* the fine-structure constant here).
- **E-3 partially confirmed**: right in magnitude, wrong in shape (one-sided, not two-sided).
- **New for the corpus:** kT_bath ≳ 0.1 E_Pl from the observed tilt.
- **OPEN-EU-1's remaining targets:** T-1 delivered (3820), T-2 delivered (here), T-3 closed negative (3847). **The charter's three targets are now all discharged** — two positively, one as a characterised gap.
- Unaffected: the e-fold budget (~10.5 short, VSL computation still owed); AP-4's shell clause; CONV-046's dispatch decision.
