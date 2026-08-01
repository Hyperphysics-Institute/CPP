# PRE-REGISTRATION — HYBRID CURVATURE PIPELINE (STAGE 1: RESPONSE FIELD; STAGE 2: ANALYTIC DRESSED DRIVE)

**Patch 2913. Committed and presented BEFORE any Stage-1 field is
analysed for β-structure and BEFORE any Stage-2 number exists.
Implements restructure item (2) of the 2908 analysis. This is the route
to the renounced curvature question.**

## §0 — DESIGN RULING (worker decision under PD-006, correctable)

The founder's arcs question (does the fore/aft disparity live in arc
displacement or partly in "charging state") is answered from his own
31-Jul one-primitive ruling: at the primitive level a CP's only state is
position; SSV is recomputed each Moment from arriving DI-bits, never
stored. The displacement/dipole configuration is therefore the COMPLETE
substrate carrier. The pipeline tabulates the full vector response —
axial induced dipole, radial induced dipole, and pair-centre drift — so
no emergent reading of "charging" is discarded. Founder correction
invited; recorded per CONV-009 class when it arrives.

## §1 — STAGE 1: MEASURED RESPONSE FIELD

Instrumented mobile legs (small domain, gated kernel, procedure of the
sign round): seeds {1,2,3} × classes {A,B} × β {0.05, 0.10, 0.20},
matched windows, T_eq = 40. Per Moment in the window, per pair, in
co-moving coordinates ξ = x_pair − x_source(t), ρ:

- axial induced dipole p_x(ξ, ρ) (baseline exactly 0 by construction —
  initial dipoles are radial);
- radial induced dipole δp_ρ(ξ, ρ) (baseline d₀ + jitter, known);
- pair-centre axial drift u_x(ξ, ρ).

Binned: ξ in 24 bins of width 1 on [−12, 12]; ρ in {[1,3), [3,5),
[5,8]}. Ensemble-averaged over legs at fixed β.

**Frozen linear-response test:** the collapse residual
R = ‖p_x(·;β)/β − p̄₁(·)‖ / ‖p̄₁‖ (norm over bins with ≥ 200 samples,
p̄₁ the β-pooled estimate) must satisfy R < 0.25 at every β for the
linear extraction to proceed; otherwise Stage 2 must model the β³ term
explicitly and says so.

## §2 — STAGE 2: ANALYTIC DRESSED DRIVE (deterministic)

Given the measured p̄₁ (and drift field), compute the steady-state
retarded drive on the source from the co-moving response pattern: each
virtual pair at absolute position carries the pattern evaluated at its
retarded co-moving coordinate; the sum is the 2884-class doubly-retarded
integral with the MEASURED source term. Extract
D_hyb(β)/β = k_h(1 − c_hyb β²) over a fine β grid (no chatter anywhere
in Stage 2; c_hyb is scale-invariant in p̄₁, sensitive only to its
shape).

**Uncertainty:** propagate binwise Stage-1 standard errors through the
integral by 200-fold bootstrap; report c_hyb ± σ_c.

## §3 — FROZEN BANDS FOR c_hyb (inherited, committed before any number)

| outcome | criterion |
|---|---|
| **CANCELLATION (provisional)** | \|c_hyb\| < 0.05 with σ_c ≤ 0.05 |
| **RETAINED (provisional)** | c_hyb ∈ [0.10, 0.30] with σ_c ≤ 0.05 |
| **INTERMEDIATE** | c_hyb ∈ [0.05, 0.10) with σ_c ≤ 0.05 — neither band; reported as measured |
| **INCONCLUSIVE** | σ_c > 0.05, collapse test failed without a modelled β³ term, or any §1 gate unmet |

Provisional status: any banded outcome requires a domain variation of
Stage 1 (the 1.3× configuration) before promotion, pre-registered
subsequently. **Context frozen with the bands:** the static-Sea
kinematic value is c = 1/5 exactly (Patch 2900); CANCELLATION means the
measured entrainment shape suffices to null it; RETAINED means it does
not and the B1 conflict stands at substrate level.

**Worker expectation, seventh declaration: CANCELLATION — still resting
on the 2900 steady-state argument alone; the sign result does not bear
on it.**
