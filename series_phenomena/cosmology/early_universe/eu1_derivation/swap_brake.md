# The brake, derived — **the eDP pair-swap is electromagnetic, so its rate carries α, and ballistic growth against it saturates at ℓ = 1/α = 137 PSR.** The requirement from the observed amplitude was **138 PSR**. **But the requirement carries an O(1) ambiguity spanning 87–220, so this is CONSISTENT, not confirmed** — and the worker noticed the coincidence *before* finding the reason, which is disclosed

**Patch 3898, Session 208, 11 Sep 2026. Lane: EU.** Verify `scripts/3898_swap_brake.py` (10/10). Reasoning `reasoning/3898_swap_brake.md`. **Nothing adopted; no constant minted; C-5 still not reported as working**; PRED-C-96 untouched; 3710 not retired.

## §1 D-1 first: the rate is not on file (verify T1)
The corpus fixes the eDP swap **qualitatively only** — the founder's *"those eDPs are not faithful … pair-swap readily."* **No rate exists anywhere in the record.** So the brake had to be **derived**, which is what 3896 demanded: *derive then compare, never tune.*

## §2 The derivation — two protocol facts and one physical inference (verify T2, T3, T4)
**Build rate (protocol fact).** The hop cascade reaches the PSR within one Moment (3862, R-OUTWARD-FANOUT / D-SUBPSR-FIELD). So influence — and therefore correlation — extends at **1 PSR per Moment**. Not an estimate.

**Decay rate (the one physical inference).** **Pair-swapping is an electromagnetic process between eCPs.** Electromagnetic transition rates carry the electromagnetic coupling, so the per-Moment swap probability is

> **Γ_swap ~ α.**

**Saturation.** Ballistic growth against a constant decay rate saturates at ℓ = v/Γ: correlation reaches distance r after r Moments and survives with probability e^{−Γr}, so

> **ℓ_sat = 1/Γ_swap = 1/α = 137.0 PSR.**

**Derived with no reference to the target.**

## §3 The comparison (verify T5)
3896's requirement, computed from the **observed** amplitude: **ℓ_corr = 138.4 PSR.**

> **Derived 137.0 against required 138.4 — agreement at the 1.0% level.**

## §4 And the 1% is illusory precision — the honest limit (verify T6, T7)
**The requirement is not sharp to 1%.** It carries δ_patch = **O(1)**, not exactly 1, and ℓ_req ∝ δ^{−2/3}:

| δ_patch | required ℓ_corr |
|---|---|
| 0.5 | 220 PSR |
| **1.0** | **138 PSR** |
| 2.0 | 87 PSR |

> **1/α = 137 sits inside the 87–220 band.**
>
> **VERDICT: CONSISTENT — NOT CONFIRMED.** An independently derived brake lands within the allowed range. That is not the same as reproducing a measured number, and the 1% agreement at δ_patch = 1 should not be quoted as though it were.

## §5 The ordering, disclosed (verify T8)
**I noticed 138 ≈ 137 before I found the reason.** That is the wrong order, and recording it is the only protection against the failure mode it invites.

**The test that matters is whether the derivation would have produced α without the target in view — and it would.** The swap is an electromagnetic process; electromagnetic rates carry α; anyone asked for the per-Moment probability of an EM transition in Planck units would answer α. The reasoning is sound on its own terms.

**But the reasoning being sound does not make the order harmless**, and a reader of this file should weigh it. Both are on the record.

## §6 What would turn consistency into a result (verify T9)
> **Compute δ_patch from the dynamics.**

If δ_patch comes out 1 **for a reason** — from the affinity's strength and the composition spread — then the band collapses, the 1% becomes meaningful, and **C-5's amplitude is derived rather than accommodated.** If it comes out 0.3 or 3, the brake is merely compatible.

**That is now C-5's gate: one quantity between consistency and a result.**

## §7 Scope (verify T10)
**Nothing adopted. No constant minted. C-5 is not reported as working.** Two of three inputs are protocol facts (PSR reach, Moment cadence); one is a physical inference (EM rate ~ α). **PD-007 respected**: the brake was derived first and compared second, as 3896 required.

**And C-5 still owes adiabaticity** (Planck's isocurvature bound), untouched here.

## §6b THE GATE, HALF CLOSED (Patch 3900)

§6 made the gate *"compute δ_patch from the dynamics — if it comes out 1 for a reason."* **The reason is found: SATURATION.** ℓ_corr is by definition the range over which the sorting is coherent, so within one correlation volume preferential attachment has **run to completion** and each patch is **wholesale** Q- or E-dominant, whatever its seed. **So δ_patch = |ln(f_E/f_Q)|, a log-ratio of two saturated outcomes — O(1) by construction.** *(The seed is irrelevant: Poisson in n₀, ≤10⁻³.)*

**The qualitative half is discharged.** The **number** still needs the affinity strengths, which are **not on file**, so C-5 now makes a **falsifiable prediction** instead: **f_E/f_Q ≈ 2.8, band [1.7, 6.5]** — E-dominant patches unstack ~2.8× further than Q-dominant ones. See `delta_patch.md`.

## §8 Standing
- **The eDP swap rate is NOT on file** — derived, not read.
- **Derivation: Γ_swap ~ α (EM process) + build at 1 PSR/Moment (protocol) ⇒ ℓ_sat = 1/α = 137.0 PSR.**
- **Requirement (3896, from the observation): 138.4 PSR. Agreement 1.0%.**
- **But the requirement spans 87–220 for δ_patch ∈ [0.5, 2]. CONSISTENT, NOT CONFIRMED.**
- **Ordering disclosed:** the coincidence was noticed before the reason was found; the derivation stands independently, but the order is on the record.
- **Gate: compute δ_patch from the dynamics.** One quantity between consistency and a result.
- **Debt (5), adiabaticity, remains untouched.**
- PRED-C-96, T-1, T-2, the count law: unaffected.
