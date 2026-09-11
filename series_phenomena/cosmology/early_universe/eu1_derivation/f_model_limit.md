# C-5's last in-lane caveat closed — **the re-stacking-dominated limit holds at the pivot**, because f(pivot) ≪ 1 for any large stack number, and **the crossover to the failing limit sits in the last one to three e-folds**, long after every observable mode has left the horizon. **Independent of n₀. The lane's own work on C-5 is finished**

**Patch 3910, Session 214, 11 Sep 2026. Lane: EU.** Closes the 3902 §7 model caveat. Verify `scripts/3910_f_model_limit.py` (10/10). Reasoning `reasoning/3910_f_model_limit.md`. **Nothing adopted; C-5 not reported as working; the amplitude remains κ\*-gated (3906)**; PRED-C-96 untouched; 3710 not retired.

## §1 The caveat, and why it was load-bearing (verify T1)
3902 §7 recorded it as a caveat rather than burying it: **f ~ 1/A is the re-stacking-dominated limit** of the two-rate steady state

> **f = R_out/(R_out + R_in)**, with **R_in ∝ A** (the affinity).

- **R_in ≫ R_out** ⇒ f ≈ R_out/R_in ∝ **1/A** — the limit used, giving f_E/f_Q = α_s/α.
- **R_out ≫ R_in** ⇒ f ≈ **1, independent of A** ⇒ **f_E/f_Q → 1** ⇒ **C-5's amplitude chain fails.**

**Which limit holds was untested, and it decides the candidate.**

## §2 It is settled by f itself — no new assumption (verify T2, T3, T4, T5)
**The quantity that decides the limit was already derived at 3892.** f(start) = **1/n₀** (one occupied GP per n₀ CPs), and **ln f is linear in N_rem.** So with N_tot = 64.47 and the pivot at N_rem = 57:

> **ln f(pivot) = −(N_piv/N_tot)·ln n₀ = −0.884 ln n₀.**

| n₀ | f(pivot) |
|---|---|
| 10⁶ | 5.0×10⁻⁶ |
| 10¹² | 2.5×10⁻¹¹ |
| 10²⁴ | 6.0×10⁻²² |

> **f(pivot) ≪ 1 for any large n₀ ⇒ deeply re-stacking-dominated ⇒ f ~ 1/A HOLDS.**

**The limit used at 3902 is the correct one, and the validation is independent of the stack number** — **fifth session running that n₀ has been carried rather than chosen.**

## §3 And the crossover is far from the observable window (verify T6, T7, T8)
Solving f = 0.5 for the transition into the failing regime:

| n₀ | crossover N_rem |
|---|---|
| 10⁶ | 3.2 |
| 10¹² | 1.6 |
| 10²⁴ | 0.8 |

> **The last one to three e-folds. Every observed mode exits at N_rem ≈ 50–60 — more than an order of magnitude away.**

**And the system does pass through both limits — it must**, since 3892 requires f → 1 at the end for the count law to close. **That is a feature, not a problem:** the transition to unstacking-dominated is what *ends* the unstacking, and it happens **after** the observable window has been laid down.

## §4 What this closes, and what it does not (verify T9, T10)
> **C-5's last in-lane caveat is closed. The lane's own work on C-5 is finished.**

**The two remaining items are not EU-local:**
1. **The SM-sector conserved-charge check** — gates the 3908 adiabaticity pass. Cross-lane; needs sanction.
2. **The H ∝ μ assignment** — foundational, and the reason the normalisation is κ\*-gated (3906).

**This closes a caveat, not a debt.** The headline does not move:

> **A source with the right spectrum — Gaussian, scale-free, conditionally adiabatic, with a derived microphysics — and a normalisation not derivable as the framework stands.**

## §5 Standing
- **3902's model caveat CLOSED.** The re-stacking-dominated limit holds at the pivot.
- **f(pivot) ≪ 1 for any large n₀** (5×10⁻⁶ to 6×10⁻²²) — **validation independent of the stack number.**
- **Crossover to the failing limit at N_rem ≈ 0.8–3.2** — the last one to three e-folds, far outside the observable window.
- **Both limits are traversed, as the count law requires** — the transition ends the unstacking and is a feature.
- **The lane's own work on C-5 is finished.** Remaining items are cross-lane (SM-sector check) and foundational (H ∝ μ).
- **The headline is unchanged.** PRED-C-96, T-1, T-2, the count law: unaffected.
