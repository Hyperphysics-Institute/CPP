# CPP Open Problems Registry

**GitHub:** `CPP/open_problems/`
**Last updated:** 29 March 2026
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

### OP-SS — Strong Sector (14 problems)

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
| [OP-SS-9](OP-SS/OP-SS-9_charge_quantisation.md) | Prove $\delta = 1/3$ from 600-cell geometry | HIGH | ✅ SOLVED (29 Mar 2026) |
| [OP-SS-10](OP-SS/OP-SS-10_nuclear_binding.md) | Nuclear binding energy from qDP insertion | HIGH | OPEN |
| [OP-SS-11](OP-SS/OP-SS-11_su3_operator_uniqueness.md) | Uniqueness of SU(3) operator mapping | HIGH | OPEN |
| [OP-SS-12](OP-SS/OP-SS-12_w_bracelet_polarity_inversion.md) | W bracelet polarity inversion from CPP | HIGH | OPEN |
| [OP-SS-13](OP-SS/OP-SS-13_zbw_delta_quantitative.md) | ZBW mechanism quantitative agreement with $\delta=1/3$ | MEDIUM | OPEN |
| [OP-SS-14](OP-SS/OP-SS-14_deconfinement_temperature.md) | QCD deconfinement temperature from CPP | MEDIUM | OPEN |

### OP-SM — Standard Model Emergence (7 problems)

| ID | Title | Priority | Status |
|---|---|---|---|
| [OP-SM-1](OP-SM/OP-SM-1_k_constant_derivation.md) | Derive $k \approx 0.0185$ from 600-cell geometry | HIGHEST | ✅ SOLVED (23 Mar 2026) |
| [OP-SM-2](OP-SM/OP-SM-2_k_vs_sea_strength.md) | Reconcile $k = 0.0185$ with sea\_strength $= 0.185$ | HIGH | ✅ SOLVED (23 Mar 2026) |
| [OP-SM-3](OP-SM/OP-SM-3_epsilon_correction.md) | $\epsilon$ correction factor | MEDIUM | OPEN |
| [OP-SM-4](OP-SM/OP-SM-4_capotauro_mechanism.md) | Capotauro mechanism for TBM corrections | HIGH | OPEN |
| [OP-SM-5](OP-SM/OP-SM-5_pmns_mixing_angles.md) | PMNS mixing angle corrections beyond TBM | HIGH | OPEN |
| [OP-SM-6](OP-SM/OP-SM-6_cosmological_constant.md) | Cosmological constant from CPP vacuum | HIGH | OPEN |
| [OP-SM-7](OP-SM/OP-SM-7_koide_derivation.md) | Koide phase $\theta = 132.73°$ derivation | HIGHEST | OPEN |

### OP-SR — Special Relativity (8 problems)

| ID | Title | Priority | Status |
|---|---|---|---|
| [OP-SR-1](OP-SR/OP-SR-1_psr_reduction_formula.md) | PSR reduction formula from first principles | HIGH | OPEN |
| [OP-SR-2](OP-SR/OP-SR-2_k_constant.md) | Derive $k = l_P^3/E_P$ prefactor geometrically | HIGH | OPEN |
| [OP-SR-3](OP-SR/OP-SR-3_ssv_definition.md) | SSV definition from DP density | MEDIUM | OPEN |
| [OP-SR-4](OP-SR/OP-SR-4_full_einstein_equations.md) | Full Einstein field equations from SSV | HIGH | OPEN |
| [OP-SR-5](OP-SR/OP-SR-5_cosmological_constant.md) | Cosmological constant from holographic vacuum | MEDIUM | OPEN |
| [OP-SR-6](OP-SR/OP-SR-6_big_bang.md) | Big Bang as initial 600-cell state | MEDIUM | OPEN |
| [OP-SR-7](OP-SR/OP-SR-7_gp_exclusion.md) | Grid Point exclusion principle | MEDIUM | OPEN |
| [OP-SR-8](OP-SR/OP-SR-8_equivalence_principle.md) | Equivalence principle from SSV geometry | HIGH | OPEN |

### OP-EW — Electroweak Sector (6 problems)

| ID | Title | Priority | Status |
|---|---|---|---|
| [OP-EW-1](OP-EW/OP-EW-1_eta_derivation.md) | Derive $\eta \sim 10^{-17}$ (Planck-to-weak) | HIGHEST | OPEN |
| [OP-EW-2](OP-EW/OP-EW-2_unified_mass_formula.md) | Unified boson mass formula | HIGH | OPEN |
| [OP-EW-3](OP-EW/OP-EW-3_loop_density.md) | Loop density 4D projection factor | MEDIUM | OPEN |
| [OP-EW-4](OP-EW/OP-EW-4_mass_ratios_eigenvalues.md) | Boson mass ratios from eigenvalue ratios | HIGH | OPEN |
| [OP-EW-5](OP-EW/OP-EW-5_W0_virtual.md) | W$^0$ virtual particle: quantitative properties | MEDIUM | OPEN |
| [OP-EW-6](OP-EW/OP-EW-6_chirality.md) | Chirality from eigenvalue-weighted phase bias | MEDIUM | OPEN |

### OP-QM — Quantum Mechanics (7 problems)

| ID | Title | Priority | Status |
|---|---|---|---|
| [OP-QM-1](OP-QM/OP-QM-1_born_rule.md) | Born rule from CPP statistics | HIGH | OPEN |
| [OP-QM-2](OP-QM/OP-QM-2_schrodinger_derivation.md) | Schrödinger equation from ZBW diffusion | HIGH | OPEN |
| [OP-QM-3](OP-QM/OP-QM-3_spin_pauli_exclusion.md) | Spin and Pauli exclusion from cage geometry | HIGH | OPEN |
| [OP-QM-4](OP-QM/OP-QM-4_decoherence_timescale.md) | Decoherence timescale from Nexus coupling | MEDIUM | OPEN |
| [OP-QM-5](OP-QM/OP-QM-5_entanglement_threshold.md) | Entanglement threshold distance | MEDIUM | OPEN |
| [OP-QM-6](OP-QM/OP-QM-6_discrete_spectra.md) | Discrete spectra from lattice quantisation | MEDIUM | OPEN |
| [OP-QM-7](OP-QM/OP-QM-7_qft_second_quantization.md) | QFT second quantisation from CPP | HIGH | OPEN |

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

## Recently Resolved (29 March 2026 Session)

| ID | Resolution | Resolving paper |
|---|---|---|
| OP-SS-9 | $\delta = 1/3$ proved from C₃ symmetry + cage completeness | SM-1 Theorem 1 (v6) |

## Previously Resolved (23 March 2026)

| ID | Resolution | Resolving paper |
|---|---|---|
| OP-SM-1 | $k_{\rm SM} = \alpha_{\rm geom}/(12\varphi^2) \approx 0.01781$ | SS-1 §8 + SR-1 companion |
| OP-SM-2 | sea\_strength $= 10 \times k_{\rm SM}$ (factor $N_{\rm lattice}/z = 120/12$) | SS-1 §8 |

---

## Conjectures Register

See [conjectures-SS.md](conjectures-SS.md) for:
- **CJ-SS-1:** W₀ bracelet locally-linear coupling face (registered 29 Mar 2026)
- **CJ-SS-2:** Universal qCP polarity switching in quark flavor transitions (registered 29 Mar 2026)
- **Candidate Postulate P-SS-1:** 2:1 ZBW orbital frequency ratio for quarks

---

## Dependency Graph

```
OP-SS-9 (δ=1/3) ✅ SOLVED ───────────────────────────────────► OP-G-2
OP-SS-13 (ZBW δ=1/3) ──────────────────────────────────────► OP-SS-9 (confirmation)
OP-SS-11 (SU3 uniqueness) ─────────────────────────────────► SS-1 Thm 1 (strengthens)
OP-SS-12 (W bracelet) ─────────────────────────────────────► OP-G-2
OP-SS-14 (deconfinement T) ──────────────────────────────── depends on OP-SS-5
OP-SS-5 (σ) ─────► OP-SS-7 (Λ_QCD) ────────────────────────► OP-G-2
                ├── OP-SS-10 (nuclear)
                ├── OP-SS-6 (glueball)
                └── OP-SS-14 (deconfinement T)
OP-SS-1 (M_q) ───► OP-SS-3 (chiral) ────────────────────────► OP-G-1
              └──► OP-SS-2 (generations) ───────────────────► OP-G-1
OP-SS-8 (μ_N) ─────────────────────────────────────────────► OP-G-2
OP-SS-4 (β₁)  ─────────────────────────────────────────────► OP-G-2

OP-SM-1 (k) ✅ SOLVED ─────────────────────────────────────► OP-G-2
OP-SM-2 (k/sea) ✅ SOLVED ─────────────────────────────────► OP-G-2
OP-SM-7 (θ_Koide) ─────────────────────────────────────────► OP-G-2

OP-EW-1 (η)   ─────────────────────────────────────────────► OP-G-2
OP-EW-2 (masses) ──► OP-EW-4 (ratios) ─────────────────────► OP-G-2

OP-SD-1 (K₀)  ──► OP-SD-2 (interp.) ──► OP-SD-3 (A₅, A₃)
```

---

## Recommended Attack Order (updated 29 March 2026)

1. **OP-SS-11** — Pure group theory; 1–2 page uniqueness argument.
   Strengthens SS-1 Theorem 1 from possibility to necessity.
2. **OP-SS-5** — One dimensional-analysis step from established mechanism.
   Prerequisite for OP-SS-14.
3. **OP-SS-13** — ZBW orbital calculation; confirms C₃ proof mechanically.
4. **OP-SS-8** — Clear SU(6) + ZBW derivation path.
5. **OP-SS-12** — Requires reading EW-2 first; high physical importance.
6. **OP-SS-1** — Mechanism established; find the ZBW-frequency kernel.
7. **OP-SD-1** — Resolves the superdeterminism amplitude conjecture.
8. **OP-SS-3** — ZBW notebooks give the starting point.
9. **OP-SS-10** — Needs OP-SS-5 as prerequisite.
10. **OP-SS-14** — Needs OP-SS-5 as prerequisite.
11. **OP-SS-6** — Extend $f_\text{geom}$ formula to cell-level loops.
12. **OP-EW-1** — The hardest single problem; requires new scaling argument.
13. **OP-G-1/G-2** — Capstone; emerges when all sector problems converge.

---

## Problem Count Summary

| Series | Total | Solved | Partial | Open |
|--------|-------|--------|---------|------|
| OP-SS (Strong) | 14 | 1 | 2 | 11 |
| OP-SM (Standard Model) | 7 | 2 | 0 | 5 |
| OP-SR (Special Relativity) | 8 | 0 | 0 | 8 |
| OP-EW (Electroweak) | 6 | 0 | 0 | 6 |
| OP-QM (Quantum Mechanics) | 7 | 0 | 0 | 7 |
| OP-SD (Foundations) | 5 | 0 | 0 | 5 |
| OP-GLOBAL | 2 | 0 | 0 | 2 |
| **Total** | **49** | **3** | **2** | **44** |

---

## Series Cross-Reference

| Series | Development log | Open problem IDs |
|---|---|---|
| QM (2040a–f) | `series_QM/development_qm_series.md` | OP-QM-1 – OP-QM-7 |
| Electroweak | `series_electroweak/development_ew_series.md` | OP-EW-1 – OP-EW-6 |
| Strong | `series_strong/development_strong_series.md` | OP-SS-1 – OP-SS-14 |
| Standard Model | `series_standard_model/development_sm_series.md` | OP-SM-1 – OP-SM-7 |
| Special Relativity | `series_relativity/development_sr_series.md` | OP-SR-1 – OP-SR-8 |
| Foundations | `series_foundations/` | OP-SD-1 – OP-SD-5 |
| Nuclear | `series_nuclear/` (future) | OP-SS-10 feeds here |

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
