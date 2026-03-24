# CPP Open Problems Registry

**GitHub:** `CPP/open_problems/`  
**Last updated:** 23 March 2026  
**Maintainer:** Thomas Lee Abshier, Hyperphysics Institute

---

## Purpose

This directory is the central research frontier for Conscious Point
Physics.  Every open problem in the programme is registered here with
its current status, evidence base, suggested approach, and connections
to other problems.

A problem moves from **OPEN** → **PARTIAL** → **SOLVED** as work
progresses.  When solved, the status line is updated and a link to the
resolving paper is added.  No problem file is ever deleted — the
history of what was tried and why it failed is as valuable as the
final solution.

---

## How to use this directory

- **Finding a problem to work on:** scan the master table below,
  filter by priority and status.
- **Starting work on a problem:** read the `.md` file in full before
  beginning — it records what has already been tried.
- **Reporting progress:** update the `.md` file with new findings,
  even partial ones.  Stage numbers in
  `development_strong_series.md` and equivalent development logs
  are the canonical provenance trail.
- **Solving a problem:** add the resolving paper reference and change
  status to SOLVED.  Update any downstream problems that were waiting
  on this one.

---

## Master Problem Table

### OP-SS — Strong Sector (10 problems)

| ID | Title | Priority | Status |
|---|---|---|---|
| [OP-SS-1](OP-SS/OP-SS-1_quark_mass_formula.md) | Quark mass formula $M_q(n_\text{layers})$ | HIGHEST | PARTIAL |
| [OP-SS-2](OP-SS/OP-SS-2_three_generations.md) | Three SM generations from cage geometry | HIGH | OPEN |
| [OP-SS-3](OP-SS/OP-SS-3_chiral_condensate.md) | Chiral condensate $\langle\bar{q}q\rangle$ from ZBW | MEDIUM | OPEN |
| [OP-SS-4](OP-SS/OP-SS-4_two_loop_beta.md) | Two-loop $\beta_1$ from CPP dynamics | MEDIUM | OPEN |
| [OP-SS-5](OP-SS/OP-SS-5_string_tension.md) | String tension $\sigma$ from sea\_strength | HIGH | PARTIAL |
| [OP-SS-6](OP-SS/OP-SS-6_glueball_mass.md) | Glueball mass from tetrahedral hDP loop | MEDIUM | OPEN |
| [OP-SS-7](OP-SS/OP-SS-7_lambda_qcd.md) | $\Lambda_\text{QCD}$ from PSR saturation | MEDIUM | OPEN |
| [OP-SS-8](OP-SS/OP-SS-8_nucleon_magnetic_moments.md) | Nucleon magnetic moments from ZBW | HIGH | OPEN |
| [OP-SS-9](OP-SS/OP-SS-9_charge_quantisation.md) | Prove $\delta = 1/3$ from 600-cell geometry | HIGH | OPEN |
| [OP-SS-10](OP-SS/OP-SS-10_nuclear_binding.md) | Nuclear binding energy from qDP insertion | HIGH | OPEN |

### OP-EW — Electroweak Sector (6 problems)

| ID | Title | Priority | Status |
|---|---|---|---|
| [OP-EW-1](OP-EW/OP-EW-1_eta_derivation.md) | Derive $\eta \sim 10^{-17}$ (Planck-to-weak) | HIGHEST | OPEN |
| [OP-EW-2](OP-EW/OP-EW-2_unified_mass_formula.md) | Unified boson mass formula | HIGH | OPEN |
| [OP-EW-3](OP-EW/OP-EW-3_loop_density.md) | Loop density 4D projection factor | MEDIUM | OPEN |
| [OP-EW-4](OP-EW/OP-EW-4_mass_ratios_eigenvalues.md) | Boson mass ratios from eigenvalue ratios | HIGH | OPEN |
| [OP-EW-5](OP-EW/OP-EW-5_W0_virtual.md) | W$^0$ virtual particle: quantitative properties | MEDIUM | OPEN |
| [OP-EW-6](OP-EW/OP-EW-6_chirality.md) | Chirality from eigenvalue-weighted phase bias | MEDIUM | OPEN |

### OP-SD — Foundations / Superdeterminism (5 problems)

| ID | Title | Priority | Status |
|---|---|---|---|
| [OP-SD-1](OP-SD/OP-SD-1_K0_derivation.md) | Explicit $K_0(\lambda)$ from single-CP integral | HIGH | OPEN |
| [OP-SD-2](OP-SD/OP-SD-2_interpolation_proof.md) | Non-perturbative proof of interpolation conjecture | HIGH | OPEN |
| [OP-SD-3](OP-SD/OP-SD-3_amplitudes_A5_A3.md) | Amplitudes $A_5 = \phi^{-3}/(2\pi)$, $A_3/A_5$ | HIGH | OPEN |
| [OP-SD-4](OP-SD/OP-SD-4_multiqubit_K.md) | Many-body $K$ for entangled multi-qubit states | MEDIUM | OPEN |
| [OP-SD-5](OP-SD/OP-SD-5_apparatus_SSV.md) | Apparatus DP Sea anisotropy $\delta_0$ from SSV | MEDIUM | OPEN |

### OP-GLOBAL — Cross-Series (2 problems)

| ID | Title | Priority | Status |
|---|---|---|---|
| [OP-G-1](OP-GLOBAL/OP-G-1_three_generations_global.md) | Three SM generations: quarks + leptons unified | HIGHEST | OPEN |
| [OP-G-2](OP-GLOBAL/OP-G-2_SM_unification.md) | Full SM from single 600-cell: all parameters | HIGHEST | OPEN |

---

## Dependency Graph

```
OP-SS-9 (δ=1/3)  ──────────────────────────────────────────► OP-G-2
OP-SS-5 (σ)  ────► OP-SS-7 (Λ_QCD) ──────────────────────► OP-G-2
                ├── OP-SS-10 (nuclear)
                └── OP-SS-6 (glueball)
OP-SS-1 (M_q) ───► OP-SS-3 (chiral) ──────────────────────► OP-G-1
              └──► OP-SS-2 (generations) ──────────────────► OP-G-1
OP-SS-8 (μ_N) ──────────────────────────────────────────────► OP-G-2
OP-SS-4 (β₁)  ──────────────────────────────────────────────► OP-G-2

OP-EW-1 (η)   ──────────────────────────────────────────────► OP-G-2
OP-EW-2 (masses) ──► OP-EW-4 (ratios) ─────────────────────► OP-G-2

OP-SD-1 (K₀)  ──► OP-SD-2 (interp.) ──► OP-SD-3 (A₅, A₃)
```

---

## Recommended Attack Order

Problems are ordered by: (a) fewest prerequisites, (b) most tractable
with current CPP tools, (c) highest leverage on downstream problems.

1. **OP-SS-9** — Pure group theory; no new physics.  Closes the
   charge quantisation question that underlies both strong and EW sectors.
2. **OP-SS-5** — One dimensional-analysis step from established mechanism.
3. **OP-SS-8** — Clear SU(6) + ZBW derivation path.
4. **OP-SS-1** — Mechanism established; find the ZBW-frequency kernel.
5. **OP-SD-1** — Resolves the superdeterminism amplitude conjecture.
6. **OP-SS-3** — ZBW notebooks give the starting point.
7. **OP-SS-10** — Needs OP-SS-5 as prerequisite.
8. **OP-SS-6** — Extend $f_\text{geom}$ formula to cell-level loops.
9. **OP-EW-1** — The hardest single problem; requires new scaling argument.
10. **OP-G-1/G-2** — Capstone; emerges when all sector problems converge.

---

## Series Cross-Reference

| Series | Development log | Open problem IDs |
|---|---|---|
| QM (2040a–f) | `series_QM/development_qm_series.md` | (to be catalogued) |
| Electroweak | `series_electroweak/development_ew_series.md` | OP-EW-1 – OP-EW-6 |
| Strong | `series_strong/development_strong_series.md` | OP-SS-1 – OP-SS-10 |
| Foundations | `series_foundations/` | OP-SD-1 – OP-SD-5 |
| Nuclear | `series_nuclear/` (future) | OP-SS-10 feeds here |
| Leptons | `series_leptons/` (future) | OP-SS-1, OP-G-1 feed here |
