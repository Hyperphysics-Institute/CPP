# δ_patch worked — **the seed is irrelevant; SATURATION sets it, and that is why it is O(1) for a reason rather than by assumption.** The number needs affinity strengths not on file, so **C-5 makes a falsifiable prediction instead: E-dominant patches unstack ≈2.8× further than Q-dominant ones.** Band 1.7–6.5. **Half the gate closed; the other half is now a test**

**Patch 3900, Session 209, 11 Sep 2026. Lane: EU — first patch in the new block 3900–3999**, allocated by the founder on exhaustion of 3800–3899. Verify `scripts/3900_delta_patch.py` (10/10). Reasoning `reasoning/3900_delta_patch.md`. **Nothing adopted; no constant minted; C-5 not reported as working**; PRED-C-96 untouched; 3710 not retired.

## §1 The seed is not the source (verify T2)
The obvious guess is that δ_patch traces the scatter in SCP compositions. **It cannot.** If compositions are seeded randomly, the per-SCP spread is Poisson in n₀:

| n₀ | composition spread |
|---|---|
| 10⁶ | 10⁻³ |
| 10¹² | 10⁻⁶ |
| 10²⁴ | 10⁻¹² |

**Minute.** Had δ_patch been seed-set, C-5 would fail by many orders and the question would already be closed. **So the seed is not what makes δ_patch O(1)** — which is the first thing worth knowing about it.

## §2 Saturation sets it — and that is the reason 3898 asked for (verify T3, T4)
> **ℓ_corr is, by definition, the range over which the sorting is coherent.**

So **within one correlation volume, preferential attachment has run to completion.** Each patch ends up **wholesale** Q-dominant or **wholesale** E-dominant — **however small its seed.** The amplification *is* the mechanism; the seed only picks which way a patch falls.

> **Therefore δ_patch = |ln(f_E/f_Q)| — a log-ratio of two *saturated* unstacking fractions.**

**This discharges the qualitative half of the gate.** 3898 asked whether δ_patch is 1 *for a reason*. **The reason is saturation**, and it is structural: a log-ratio of two saturated dynamical outcomes is an O(1) number by construction, not by hope. It could not have been 10⁻⁶ and it could not have been 10⁶.

## §3 The number is not on file, and is not invented (verify T5)
Computing |ln(f_E/f_Q)| requires the **Q-to-Q and E-to-anything affinity strengths**. **D-1 finds none** — the corpus fixes the affinities qualitatively only (3894).

**So the value is not computed here and is not supplied.** Fourth session running that a parameter the corpus lacks has been carried rather than chosen.

## §4 So C-5 makes a falsifiable prediction (verify T6, T7, T8)
Combining the **independently derived** brake with the **observed** amplitude:

> ℓ_sat = 1/α = **137.0 PSR** (derived, 3898) against ℓ_req = 138.4·δ^{−2/3} (3896, from the observation)
>
> ⇒ **δ_patch = 1.015** ⇒ **f_E/f_Q = e^{1.015} = 2.76.**

> ### **C-5 predicts: E-dominant patches unstack about 2.8× further than Q-dominant ones.**

**That is a concrete statement about two rates, not a fitted parameter** — and it is physically sensible in direction: Q-dominant patches re-superimpose more readily (strong mutual affinity), so they unstack *less*.

**It is sharp enough to falsify.** Allowing ℓ_sat to differ from 1/α by 1.5× either way:

| ℓ_sat vs 1/α | f_E/f_Q |
|---|---|
| 1.5× | 1.7 |
| **1.0×** | **2.8** |
| 0.67× | 6.5 |

> **Band: f_E/f_Q ∈ [1.7, 6.5].** A computed ratio of 1.1, or 20, kills C-5.

## §5 Why this is a prediction and not a fit (verify T9)
**Nothing was tuned.** The brake came from α by an argument that made no reference to the target (3898 §2); the requirement came from the observation (3896). **Their agreement demands a specific value of a third quantity, and that quantity has an independent route to it** — the two affinity strengths.

**This is the same structure as T-2's kT_bath bound** (3850 §4): an observation constraining a quantity the theory must independently supply. That was accepted then and the logic is unchanged.

**What would make it a fit** is computing the affinities *after* seeing 2.8 and arranging them to land there. **The affinities must be derived from the SCP composition dynamics and then compared** — and whoever does it should note that they are reading this file first, which is itself a hazard.

## §5b THE PREDICTION TESTED (Patch 3902) — inside the band, but the amplitude is NOT derived

§4 predicted **f_E/f_Q ≈ 2.8, band [1.7, 6.5]**. Tested at 3902 under the hazard discipline (structure and couplings written down **first**): the strong channel needs **both** partners to carry strong charge, so **Q-Q → α_s** while **Q-E and E-E → α** — which **derives the founder's asymmetry from charge content**. With α_s(M_Pl) = 0.01970 from standard running, **f_E/f_Q = α_s/α = 2.70 — 2.2% from centre, inside the band.**

**But the circularity check matters more:** **H is A_s-normalised**, so an end-to-end ζ computation is **circular** and is not claimed. What survives is **ℓ_req = 139.0 vs ℓ_sat = 137.0 (1.4%)**, with the observation entering at the **sixth power**. **Consistency check, not derivation** — and the **third chained near-miss in three sessions, to be weighed as one result.** See `affinity_ratio.md`.

## §6 Standing
- **First patch in the new EU block 3900–3999.**
- **The seed is irrelevant** — Poisson in n₀, minute. δ_patch is not seed-set.
- **Saturation sets it: δ_patch = |ln(f_E/f_Q)|, an O(1) log-ratio of saturated outcomes.** **The qualitative half of 3898's gate is DISCHARGED — δ_patch is O(1) for a reason.**
- **The number requires affinity strengths not on file; not invented.**
- **C-5 PREDICTS f_E/f_Q ≈ 2.8, band [1.7, 6.5]** — E-dominant patches unstack ~2.8× further than Q-dominant.
- **Falsifiable:** a computed ratio outside the band kills C-5's amplitude.
- **Test named:** derive the two affinity strengths from the SCP composition dynamics, then compare.
- **Debt (6), adiabaticity vs Planck's isocurvature bound, remains untouched.**
- PRED-C-96, T-1, T-2, the count law: unaffected.
