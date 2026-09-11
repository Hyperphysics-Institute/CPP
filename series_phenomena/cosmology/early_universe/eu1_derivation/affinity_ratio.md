# The affinity ratio computed — **the structure derives the founder's asymmetry from charge content alone**, and the ratio comes out **2.70 against a predicted 2.76**. **But the circularity check kills any end-to-end amplitude claim: H is A_s-normalised.** This is a **consistency check, not a derivation** — and it is the **third chained near-miss in three sessions**, which is recorded as grounds for suspicion

**Patch 3902, Session 210, 11 Sep 2026. Lane: EU.** Worked under 3901's hazard discipline: **structure and couplings written down before any ratio was formed.** Verify `scripts/3902_affinity_ratio.py` (10/10). Reasoning `reasoning/3902_affinity_ratio.md`. **Nothing adopted; no constant minted; C-5 not reported as working; the amplitude is NOT derived**; PRED-C-96 untouched; 3710 not retired.

## §1 Step A — the structure, from charge content, before any numbers (verify T1, T2)
- **qCP carries both polar (electric) charge and strong charge.**
- **eCP carries only polar charge.**
- **The strong channel requires *both* partners to carry strong charge.**

Therefore:

| pairing | strong channel | coupling |
|---|---|---|
| Q-dominant ↔ Q-dominant | **open** | **α_s** |
| Q-dominant ↔ E-dominant | closed | α |
| E-dominant ↔ E-dominant | closed | α |

> **E-dominant couples at α whatever its partner — it is INDIFFERENT.**
> **Q-dominant reaches α_s only with its own kind — it DISCRIMINATES.**

**That is exactly the founder's asymmetry from 3894, derived rather than posited.** It is the strongest thing in this patch: his walk-and-talk described a behaviour, and the charge content produces it without being asked to.

## §2 Step B — both couplings fixed before the ratio (verify T3)
The 3901 hazard discipline required this, and it was followed:

- **α = 0.007297.**
- **α_s(M_Pl) = 0.01970**, from standard one-loop QCD running: n_f = 6, Λ = 0.2 GeV, b₀ = (33−2n_f)/12π = 0.557, ln(M_Pl²/Λ²) = 91.1. **No CPP input and no free choice.**

## §3 Steps C and D — the model, the ratio, the comparison (verify T4, T5)
Re-stacking opposes unstacking; in the **re-stacking-dominated limit** f ~ 1/A, so

> **f_E/f_Q = A_Q/A_E = α_s/α = 2.70.**

**3900 predicted 2.76, band [1.7, 6.5]. Computed 2.70 — 2.2% from centre, well inside the band.**

## §4 The circularity check — and it is the point of this patch (verify T6, T7, T8, T9)
**Before writing any of the above up as a success I checked where H comes from, and the answer changes what can be claimed.**

> **H_inf here is an A_s-normalised value.** The corpus carries H ≤ 4.7×10¹³ GeV as a bound, and the standard relation A_s = H²/(8π²ε M_Pl²) fixes H **from the observed amplitude**.

> **So computing ζ end-to-end from H would be circular. That claim is not made, and must not be made.**

**What can be said:** with δ_patch = ln(α_s/α) = 0.993 computed **independently**, the required correlation length is **139.0 PSR** against the derived **1/α = 137.0** — **1.4%**.

**And the observation enters only weakly.** Since ℓ_req ∝ R_H·ζ^{2/3} and R_H ∝ ζ^{−1/2}:

> **ℓ_req ∝ ζ^{1/6}.** A **10× error in ζ_obs moves ℓ_req by only 1.5×** (×0.1 → 95 PSR; ×1 → 139; ×10 → 204).

> ### **VERDICT: a consistency check, not a derivation.**
> Not trivially circular — the sixth-power dependence is weak. **But not observation-free either. The amplitude is NOT derived end-to-end and must not be reported as such.**

## §5 The meta-warning — the most useful line here (verify T10)
> **This is the third consecutive session in which a computed number has landed near a required one:** 1/α at 3898, the O(1) saturation argument at 3900, α_s/α here.

**Three in a row is either a framework that works or a worker pattern-matching systematically.** I cannot tell which from the inside, and neither can the record unless it says so.

**The discriminator is independence, and they are not independent.** They are **one chain**: 3898's brake fed 3900's prediction, and this patch tests that prediction. **One chain, one observational input (A_s, entering at the sixth power), two couplings (α, α_s).**

> **A reader should weigh this as one result, not three.**

## §6 What is genuinely new, stated narrowly
1. **The founder's affinity asymmetry is derived from charge content** (§1). Independent of everything else here, and not observation-dependent at all.
2. **The ratio α_s/α = 2.70 sits inside the predicted band** — a consistency check with weak observation-dependence.
3. **The end-to-end amplitude claim is refuted before it was made** (§4), which is the patch's most important content.

## §6b THE MODEL CAVEAT CLOSED (Patch 3910)

§6 warned that **f ~ 1/A is the re-stacking-dominated limit** and that **in the opposite limit f_E/f_Q → 1 and the chain fails**. **Settled at 3910, by f itself:** f(start) = 1/n₀ and ln f is linear in N_rem (3892), so **ln f(pivot) = −0.884 ln n₀** ⇒ **f(pivot) = 5×10⁻⁶ to 6×10⁻²²** across plausible n₀ — **deeply re-stacking-dominated, so f ~ 1/A HOLDS, independent of the stack number.** The crossover to the failing limit sits at **N_rem ≈ 0.8–3.2**, the last one to three e-folds, while observed modes exit at **N_rem ≈ 50–60**. **Both limits are traversed, as the count law requires — the transition is what ends the unstacking.** See `f_model_limit.md`.

## §7 Standing
- **Structure derived:** Q-Q → α_s; Q-E, E-E → α. **Reproduces the founder's asymmetry from charge content.**
- **Couplings fixed before the ratio** (3901 discipline honoured): α = 0.007297; α_s(M_Pl) = 0.01970 from standard running.
- **f_E/f_Q = α_s/α = 2.70** vs predicted **2.76**, band [1.7, 6.5]. **Inside.**
- **ℓ_req = 139.0 vs ℓ_sat = 137.0 — 1.4%**, with ζ entering at the **sixth power**.
- **THE AMPLITUDE IS NOT DERIVED.** H is A_s-normalised; end-to-end is circular; **consistency check only.**
- **Model caveat:** f ~ 1/A is the re-stacking-dominated limit; other limits give f_E/f_Q → 1.
- **Identification caveat:** CPP's strong coupling = SM α_s run to M_Pl is **assumed, not established.**
- **Meta-warning: three chained near-misses in three sessions. Weigh as one result.**
- **Debt (6), adiabaticity, untouched.** PRED-C-96, T-1, T-2, the count law: unaffected.
