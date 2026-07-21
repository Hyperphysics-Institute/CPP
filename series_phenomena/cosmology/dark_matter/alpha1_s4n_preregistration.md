# ALPHA-1 S4-N PREREGISTRATION (FROZEN) — direct numerical confirmation of the S4-analytic monotonic-screening verdict: two-species point-charge Sea at the closed parameters (θ = 35.15 MeV, q = e, n_CP = 58.64 /fm³, Γ = 0.2251), Metropolis Monte Carlo, pass conditions committed HERE before any run

**Patch 2708, 21 July 2026. Founder direction (21 July): hardening step
before panel review. Method, ensembles, observables, and pass/fail
frozen pre-run; adverse outcomes report in full, nothing renamed.
Verify script: `code/2709_alpha1_s4n_simulation.py` (seeded,
deterministic). 79.5% not in scope.**

## §1 — System (all inputs registered/closed upstream; zero tuned)

Two species, equal numbers, charges ±q with q² = α_EM ħc =
1.43996 MeV·fm (0764 anchor); density n_CP = 2√2/d_DP³ = 58.636 /fm³;
temperature θ = 35.1495 MeV (TH-1); cubic periodic box; minimum-image
Coulomb truncated-and-shifted at L/2 (disclosed approximation, valid
because κL ≳ 10 ≫ 1 screens interactions well inside the box; the
Ewald upgrade is offered to the seats). Short-distance regularization
v(r) = ±q²/√(r² + a_s²) standing in for the GP-scale exclusion
(commitment 3); a_s is a ROBUSTNESS AXIS, not a parameter:
a_s ∈ {0.02, 0.04, 0.08} fm, all ≪ d_DP — the physical claim under
test includes insensitivity of the screening-scale physics to a_s.

## §2 — Ensembles (frozen)

Main: N = 686 (343 per species), a_s = 0.04 fm, seed 20260721;
500 equilibration + 2000 sampling sweeps, g(r) accumulated every 5.
Robustness: N = 432, a_s = 0.02 and 0.08 fm, seeds 20260722/3;
300 + 1200 sweeps each. Box sizes follow from N and n_CP
(L = 2.27 fm / 1.94 fm; κL = 12.5 / 10.7).

## §3 — Observables and pass conditions (frozen)

Charge-correlation profile about a tagged charge:
ρ_z(r) = shell average of Σ (sign-weighted, opposite-normalized)
neighbour charges — the numerical analog of the screened response.

- **P1 (monotonic decay):** beyond r > 2a_s and out to r = 3/κ_D =
  0.546 fm, the shell-averaged ρ_z(r) has NO statistically significant
  sign alternation (no shell of opposite sign exceeding 2σ of its own
  shell noise) in the main run.
- **P2 (scale):** log-linear fit of |ρ_z(r)·r| over r ∈ [0.10, 0.45] fm
  yields κ_fit ∈ [0.75, 1.25] × κ_D (κ_D = 5.494 /fm).
- **P3 (robustness):** the P1 character (monotonic vs oscillatory) is
  identical across both robustness runs; κ_fit stays within
  [0.6, 1.4] × κ_D on both.

**S4-N PASS = P1 ∧ P2 ∧ P3** → the S4-analytic verdict (monotonic,
ℓ_phys = d_DP/2) is numerically confirmed and the consolidated packet
assembles on founder dispatch. **Any sign-alternating profile beyond
noise** → layering present at Γ = 0.2251 → the S4-analytic verdict is
WRONG, D3 reverts to UNDECIDED-leaning-PHYSICAL, reported
adverse-direction in full. Partial failures (e.g., P2 miss with P1
pass) report as committed with diagnosis.
