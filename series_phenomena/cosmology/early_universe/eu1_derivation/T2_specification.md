# T-2 — the O(α) ZRP correction coefficient: the clean local problem, specified so it is not lost

**Patch 3848, Session 183, 9 Sep 2026. Lane: EU.** Written at the founder's request ("document the clean local problem so we don't forget it"), on the session where the amplitude arc closed negative and T-2 became the lane's principal live work. **This is a specification, not a derivation.** Nothing computed, nothing adopted, no constant minted (PD-007).

## §1 Why this document exists
For fifteen patches the lane has worked the amplitude, and T-2 has been carried as "unblocked fallback" in every handover without ever being described beyond a single charter line. With C-4 withdrawn (3847) and the amplitude sector empty, T-2 is no longer a fallback — it is the substantial EU work that remains. A one-line entry is not enough to resume from, and the founder asked for it to be written down properly.

**T-2 is also, and unusually for this lane, entirely self-contained**: EU-local, needing nothing from CHIR, nothing from the Capotauro flagship, no founder picture, and no cross-lane sanction.

## §2 The problem, stated
From the charter (§2, frozen at 3811):

> **T-2 The ZRP correction coefficient.** The O(α) occupation-dependence coefficient in the PCD→ZRP reduction (0774/0775), currently bounded by the paper's 0.1α–10α table (Δn_s from 5×10⁻⁵ to 4×10⁻³). **Deliverable: the coefficient, or a derived bound tighter than 10α.**

In plainer terms. EU-1's tilt rests on μ ∝ ln n̄, which holds because the substrate relaxes to the indistinguishable Gibbs state. That relaxation is established through the PCD → symmetric-constant-rate-ZRP reduction (0774/0775) plus the ZRP H-theorem (LEMMA-NS-HTHEOREM, 0772). The reduction is exact at leading order, but the SSV occupation-dependence enters at O(α) and its coefficient has never been computed — only bracketed.

## §3 What is at stake, quantitatively
The bracket is the paper's own, and it is wide:

| coefficient | Δn_s | as a fraction of σ_Planck (0.0042) |
|---|---|---|
| 0.1α | 5×10⁻⁵ | 0.012σ |
| α | ~5×10⁻⁴ | 0.12σ |
| 10α | 4×10⁻³ | 0.95σ |

At the low end the correction is invisible. **At the high end it is nearly a full Planck sigma** — which would make it the dominant theory uncertainty on PRED-C-96 and would matter for any future comparison against a sharper measurement. The paper currently quotes ~5×10⁻⁴ as its theory error, i.e. it implicitly assumes the middle of the bracket without having derived it.

**So T-2's value is not that it might change n_s — it is that it converts EU-1's stated theory error from an assumption into a result.** For a prediction whose whole claim is zero-parameter agreement to four digits, that is not cosmetic.

## §4 Inputs, all EU-local and all on file
- **0774** — `scripts/0774_zrp_derivation_corrections.py` and `reasoning/0774_zrp_derivation.md`: the PCD→ZRP reduction with corrections.
- **0775** — the leg-1 consensus status on that reduction.
- **0772** — `scripts/0772_zrp_htheorem.py`, LEMMA-NS-ZRP-DERIVE / LEMMA-NS-HTHEOREM.
- **0749** — the A1 counting result μ = kT ln n̄.
- The paper's own table (EU-1 §, the 0.1α–10α bracket).
- ~~α as it enters here is the SSV occupation-dependence parameter of the reduction, **not** the fine-structure constant.~~ **CORRECTED at 3850:** α here **is** the fine-structure constant, and exactly so — 0766 gives Γ = q²/(a·kT) with a = l_P, so at kT = E_Pl, Γ = q²/(ℏc) = α. The warning above pointed the wrong way and is withdrawn.

## §5 Worker expectation on record (charter §5 E-3, unchanged)
> "the coefficient is order-one times α; the table's 0.1α–10α bracket will narrow to ~[0.5α, 2α] without changing the count."

Recorded before any work, per the charter's discipline. **Note that E-2 (the quadrupole expectation) and the "three-for-three" bookkeeping were both wrong and were withdrawn at 3820 and 3831.** E-3 should be treated as a prior to be tested, not as a preview of the answer.

## §6 Method sketch (not prescriptive)
Keep the SSV correction to first order in the 0774/0775 reduction and carry it through to the occupation dependence of the hop rate, then to μ(n̄). The H-theorem (0772) fixes the equilibrium; what is wanted is the first correction to the *rate's* occupation dependence, since that is what shifts p away from exactly 2 in μ ∝ p·ln n̄ and hence shifts n_s − 1 = −2/N_rem.

Estimated one to two sessions (charter §4 W-4).

## §7 Bars
Charter §3 bars apply unchanged: no working backward from Planck's n_s to the coefficient (PD-007 — it is an output or it is nothing); LOCAL to the EU lane; no panel round until there is a result.

**One bar specific to T-2:** a *bound* is an acceptable deliverable and should not be presented as a coefficient. The charter asks for "the coefficient, **or** a derived bound tighter than 10α," and a tighter honest bound is a real contribution.

## §8 Standing
- **T-2 is the lane's principal live work** following C-4's withdrawal (3847).
- Fully EU-local; no cross-lane dependency, no founder question, no sanction needed.
- Deliverable: the O(α) coefficient, or a bound tighter than 10α.
- Converts EU-1's quoted ~5×10⁻⁴ theory error from an assumption into a derived quantity.
- Not started. Inputs §4; expectation §5; bars §7.
