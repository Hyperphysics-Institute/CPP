# SR-5 Step D — Friedmann Recovery + the Two Load-Bearing Checks (CONDITIONAL CAPSTONE)

**Arc:** OPEN-SR-5 (Cosmological Sea-gravitation sector) · **Patch:** 0723 (1 June 2026) · **Sub-item:** OPEN-SR-5d
**Verify:** `scripts/0723_friedmann_recovery.py` (D1), `scripts/0723_horizon_wz.py` (D3) — all CHECKS PASS
**Status:** CONDITIONAL. The falsification-first sequence A→D is traversed with **no kill**. The cosmological sector is structurally complete and internally consistent, resting on **two named conditions** (the c08 field-equation reduction; the event-horizon selection). Not a theorem — a coherent, falsifiable structure with its gaps isolated.

Step D has three strands.

## D1 — Friedmann recovery (PASS, conditional)

Step A gave the matter-era acceleration ä/a = −(4π/3)Gρ (Milne–McCrea, pressureless). The full history needs the GR **active gravitational mass** ρ+3p/c², which c08 supplies as "T_μν from LSP density **and flux**" (flux = momentum/pressure). With that:
- radiation (w=1/3): ρ+3p/c² = 2ρ → decelerates twice as hard as matter;
- matter (w=0): ρ → decelerates;
- Λ (w=−1): ρ+3p/c² = −2ρ → **accelerates**.

Integrating the first Friedmann equation with (Ω_r, Ω_m, Ω_Λ), **the Planck-scale ground state NOT in the source sum** and Λ entering only as the Step-C residual, reproduces the standard ΛCDM H(z); the deceleration parameter crosses zero (decel→accel) at **z ≈ 0.63** (observed ~0.6–0.7). So excess-sourcing yields the *observed* expansion history. **Condition:** the c08 reduction G_μν = 8πG/c⁴·T_μν[LSP] holds with the excess as source (see D2).

## D2 — The ground-state exclusion is structurally consistent (CONDITIONAL PASS)

The Step-B forward check: does the CPP GR limit exclude ground-state vacuum energy from the gravitating source while keeping the equivalence principle for excess energy? The c08 construction makes this favorable, on four points:

1. **Source is the perturbation.** Mass-energy sources SSV via shell-broadcast (c05); the uniform Sea is the *propagation medium*, not a source. The field-equation source is the LSP **density and flux** — the mass-energy excess — so the uniform ground state is not a T_μν source. It therefore does **not** drive de Sitter expansion → the CC catastrophe is avoided by construction, not by tuning.
2. **Uniform background is curvature-free.** c08 maps |SSV|_abs → g_tt; a spatially-uniform |SSV|_abs is a constant g_tt (a coordinate rescaling), contributing zero curvature. Only *variations* (excess gradients; or the slow cosmological *time*-variation of the Sea as it dilutes) curve spacetime. The Sea's dilution time-variation **is** the Step-C residual → dynamical Λ — tying D2 to Step C.
3. **All tested GR is reproduced.** Light-bending, Schwarzschild, perihelion (c05/c07) are all *excess/gradient* regimes — untouched. CPP departs from GR **only** in the uniform-vacuum sector, which is exactly where observation demands the vacuum not gravitate at full strength.
4. **Conservation is preserved.** The ground state is covariantly constant (uniform, p=−ρ, like a bare Λg_μν), so ∇_μ(T_ground)^μν = 0; subtracting it leaves ∇_μ T_excess^μν = ∇_μ T_full^μν = 0. The Bianchi identity is respected. This is the standard CC renormalization — but with a *physical reason* (gradient-sourcing) for discarding the bare term, rather than a fine-tuned counterterm.

**Condition (the real gap):** this rests on the c08 field-equation reduction itself, which c08 states is a **conjecture** ("not proven") and calls "the central challenge... the one thing that isn't already solved." D2 shows the exclusion is *consistent and favorable* under that reduction; it does not prove the reduction. Falsifier D2-1: if the closed CPP field equation, once derived, sources curvature from absolute |SSV| rather than the LSP perturbation, the ground state gravitates and the picture breaks.

## D3 — The horizon/w(z) choice is resolved by the dynamics (PASS, opens a refined question)

Step C left the residual as a holographic-type ρ_Λ ~ 1/L² with the IR scale L undetermined (the Hubble radius gave Ω_Λ=1/3 but *constant* — the Hsu 2004 objection). The dynamics decide:
- **Hubble radius (L=1/H):** Friedmann forces Ω_Λ = const, Λ tracks the dominant component (w_eff≈0), **no** decel→accel transition — **ruled out** (Hsu).
- **Future event horizon (L=R_h, Li 2004):** Ω_Λ evolves ~0 (early) → 0.685 (now) → 1 (future), w_Λ(now) ≈ −1.02, q(now) ≈ −0.55 (accelerating) — **reproduces the observed history**.

So dynamical consistency **selects the future event horizon**, resolving Step C's ambiguity and fixing the coefficient (Li parameter c≈0.8 → Ω_Λ≈0.7, w≈−1). **Refined open question handed forward:** *why* is the CPP Sea coherence scale the event horizon rather than the Hubble radius? The event horizon's dependence on the future evolution is the known conceptual cost; CPP has not derived this from substrate causal structure. Falsifier D3-1: if CPP physics forces the Hubble/causal scale, the residual cannot be the observed dark energy.

## Arc verdict and what it unblocks

- **A survives · B delivered · C partial (scaling+coefficient derived) · D conditional (D1 PASS, D2 conditional PASS, D3 resolved).** The falsification-first sequence is traversed with **no kill**.
- **CONJ-COSMO-2 (DE↔DM unification): CONDITIONALLY SUPPORTED, not claimed.** One Sea sources both dark energy (uniform-mode residual → event-horizon-scaled Λ) and dark matter (swirl-mode → unsuppressed gradient gravity), via the single gradient-sourcing mechanism, with the standard expansion history recovered. This stands **conditional on**: (1) the c08 field-equation reduction (D2), and (2) the event-horizon selection (D3). Promoting it to a derived result requires closing both.
- **DM Steps 4–5 unblocked (conditionally).** The cosmological background (expansion history, the Sea-vs-matter source split) now *exists* as a coherent structure, so the DM arc's quantitative work (power spectrum, rotation curves) is no longer blocked on a non-existent sector — it proceeds on this conditional foundation.

## Honest caps

- Step D is a CONDITIONAL capstone, not a theorem. Two real gaps remain (c08 field equation; event-horizon selection). Neither is a kill; both are derivation targets.
- D1's "recovery" is a consistency check (excess-sourcing → standard Friedmann), not a new prediction; the CPP content is *which* energy sources it (excess, not ground state).
- The dynamical-Λ prediction (evolving w, event-horizon HDE) is a testable departure from w=−1 (current data favor w≈−1 within errors; future surveys constrain it).
- Everything downstream inherits the Step-B/D2 condition: if the closed field equation gravitates the ground state, the whole residual picture is moot.
