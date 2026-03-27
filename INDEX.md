# CPP Repository Index

Directory-by-directory map of the entire repository.  
**Last updated:** 27 March 2026

For paper IDs and status, see [`paper_catalog.md`](paper_catalog.md).  
For what is proved vs open, see [`postulates_and_theorems.md`](postulates_and_theorems.md).

---

## Top-Level Files

| File | Purpose |
|------|---------|
| [`README.md`](README.md) | Repository overview, theory summary, submission status |
| [`INDEX.md`](INDEX.md) | This file — directory map |
| [`paper_catalog.md`](paper_catalog.md) | Master list of all papers with IDs, files, and status |
| [`postulates_and_theorems.md`](postulates_and_theorems.md) | Registry of postulates, theorems, conjectures, and falsified claims |
| `LICENSE` / `LICENSE-CC-BY-4.0.md` | License files |

---

## [`series_strong/`](series_strong/) — Strong Sector (SS)

The SU(3) derivation from 600-cell tetrahedral geometry. **Paper SS-1 is submission-ready.**

| File | Description | Paper ID |
|------|-------------|----------|
| `cpp_ss_unified_v2.tex` | **Unified submission package** — 9 theorems, 8 open problems | **SS-1** |
| `cpp_ss1_overview_v1.tex` | Companion: cage geometry and eigenvalue bridge | |
| `cpp_ss2_su3_algebra_v1.tex` | Companion: T^a = λ^a/2 exact proof | |
| `cpp_ss3_gluons_v1.tex` | Companion: eight gluons as hDP structures | |
| `cpp_ss4_confinement_v1.tex` | Companion: confinement and β-function | |
| `cpp_ss5_hadrons_v1.tex` | Companion: hadron spectrum | |
| `cpp_ss_unified_v1.tex` | Earlier unified version (superseded by v2) | |
| `cpp_strong_series.bib` | Bibliography | |
| `mc_su3_algebra.py` | Monte Carlo verification script — 33/33 checks pass | |
| `mc_su3_algebra.ipynb` | Same verification as Jupyter notebook | |
| `mc_su3_algebra_executed.ipynb` | Pre-executed notebook with outputs | |
| `development_strong_series.md` | Session-by-session development log | |

### [`series_strong/notebooks/`](series_strong/notebooks/) — 14 derivation notebooks

| Notebook | Topic |
|----------|-------|
| `chain_fraying_dynamics.ipynb` | qDP chain bow, string tension, central breaking |
| `confinement_dynamics.ipynb` | Cornell potential, confinement radius |
| `cpp_benchmark.ipynb` | Full benchmark: DP energies, decay constant τ |
| `fractional_charges_overlap.ipynb` | Quark charges from hDP overlap |
| `full_benchmark_table.ipynb` | Complete benchmark comparison table |
| `hadron_spectrum.ipynb` | GMO relations, Ω⁻, quarkonium |
| `jet_multiplicity_lattice.ipynb` | Jet fragmentation predictions |
| `magnetic_moments_zbw.ipynb` | Nucleon magnetic moments (mechanism correct, values not yet derived) |
| `nested_cage_masses.ipynb` | Cage mass model (partially falsified by PS-1) |
| `nucleon_NBT_bonding.ipynb` | Nuclear binding via NBT mechanism |
| `strong_modes_probabilistic.ipynb` | Probabilistic strong mode analysis |
| `zbw_magnetic_effects.ipynb` | ZBW Lorentz forces on qDP chains |
| `parameters_600cell.py` | Shared constants file |
| `README.md` | Notebook descriptions |

### [`series_strong/figures/`](series_strong/figures/)

`cpp_ss_running_coupling.png` · `cpp_ss_verification_summary.png`

---

## [`series_standard_model/`](series_standard_model/) — Standard Model Emergence (SM)

The main SM emergence programme. Papers SM-1 through SM-5 plus 27 topic subdirectories.  
Has its own [`INDEX.md`](series_standard_model/INDEX.md) and [`README.md`](series_standard_model/README.md).

### [`series_standard_model/papers/`](series_standard_model/papers/) — Authoritative paper files

| File | Paper ID | Status |
|------|----------|--------|
| `paper_1_binding-mechanisms_and_cage_stability.tex` | **SM-1** | Submission-ready |
| `paper_1b_reconstruction_1_of_original_CPP_mass_calculations.tex` | SM-TN-1 | Ready |
| `paper_1c_reconstruction_2_bridge_original_to_600_cell.tex` | SM-TN-2 | Needs correction |
| `paper_2_mass_generation_from_geometric_hierarchies_and_cage_complexity.tex` | **SM-2** (v30) | Submission-ready |
| `paper_3_k3_spectral_theorem_koide_formula.tex` | **SM-3** (v5) | Submission-ready |
| `paper_4_charged_lepton_masses_from_k3_spectral_theorem.tex` | **SM-4** | Submission-ready |
| `paper_5_tribimaximal_neutrino_mixing_zeroth_order_pmns_from_k3_cage_base.tex` | **SM-5** | Submission-ready |
| `development_p3-koide-spectral.md` | | Sessions A–H development log |
| `development_p3_koide_spectral.md` | | Alternate log file |
| `development_p3_transcript.md` | | Session transcript |

### [`series_standard_model/notebooks/`](series_standard_model/notebooks/)

| File | Description |
|------|-------------|
| `ps1_quark_mass_ladder.ipynb` | PS-1: exact 600-cell shell volumes, all mass mechanisms tested |
| `ps1_quark_mass_ladder_verifiable.py` | Standalone verification script |

### Topic Directories — Paper 1 series

| Directory | Content |
|-----------|---------|
| `p1-binding-mechanisms/` | Cage stability, SSV force law, electron binding example |
| `p1-dipole-sea/` | DP Sea structure, ZBW preview |
| `p1-ontology/` | Consciousness as CP primitive, historical context |

### Topic Directories — Paper 2 series (22 directories)

| Directory | Content |
|-----------|---------|
| `p2-mass-breakdown-and-validation/` | Mass contribution tables, iterative solve, PDG comparison |
| `p2-dp-types-and-composition/` | DP types (eDP, qDP, hDP-A/B), composition gradients |
| `p2-zwb-spectrum-and-oscillation/` | ZBW modes (d=0,1,3), orbital/linear/unbound mechanics |
| `p2-alpha-em-derivation/` | Fine structure constant from golden angle |
| `p2-sin2theta-w-derivation/` | Weinberg angle derivation |
| `p2-boson-structures/` | W (ribbon), Z (icosa cage), Higgs (dodeca cloud) |
| `p2-electroweak-unification/` | EW scale, sin²θ_W, unified couplings |
| `p2-electron-g-2-precision/` | Anomalous magnetic moment, loop corrections |
| `p2-charge-screening-and-asymmetries/` | Fractional charges, 1/φ² → 1/3, Capotauro bias, antimatter |
| `p2-neutrino-masses-and-suppression/` | Unbound ZBW, σ = 120⁻³, neutrino spectrum |
| `p2-neutrino-mixing-angles/` | PMNS angles, δ_CP, Capotauro phase, lattice subgroups |
| `p2-gravitational-and-cosmological-constants/` | G and Λ derivations, simulation notebooks |
| `p2-dark-matter-relic-density/` | DM candidates, relic density, cosmological model |
| `p2-cosmological-constant-refinement/` | Λ refinement, DM comparison |
| `p2-full-cosmology/` | Big Bang to Capotauro, inflation, structure formation, CMB |
| `p2-scalar-spectral-index/` | Scalar spectral index mechanism |
| `p2-structure-formation-mc/` | Structure formation Monte Carlo |
| `p2-quantum-gravity-consistency/` | GR emergence, UV completeness |
| `p2-precision-and-predictive-power/` | Framework predictive assessment |
| `p2-glossary-and-ontology/` | Full glossary of all CPP terms |

### Cross-Cutting Support

| Directory/File | Content |
|----------------|---------|
| `cpp-zbw-mixing-fractions/` | ZBW mixing notebooks (lepton + quark), sensitivity analysis |
| `suppression/` | Five suppression mechanisms (σ, φ, VEV, α, g-2) with derivation notebooks |
| `potential_solutions.md` | Candidate mechanisms for registered open problems |

---

## [`series_relativity/`](series_relativity/) — Special Relativity (SR)

Lorentz factor from lattice dynamics, the coupling constant k, and the α_geom resolution. **Paper SR-1 is submission-ready.**

| File/Directory | Description | Paper ID |
|----------------|-------------|----------|
| `main_special_relativity_emergence/` | **SR-1 paper (v17)**, figures, development log, notebooks | **SR-1** |
| `companion_papers/` | **22 companion papers** (c01–c22), see below | |
| `600-cell-monte-carlo-k-fit.py` | Monte Carlo k-fit code | |
| `600cell_k_alpha_geom_consistency_fix.py` | α_geom numerical verification | |
| `600cell_monte_carlo_voronoi_k_fit.py` | Voronoi-based Monte Carlo | |
| `k_prefactor_resolution.md` | α_geom correction documentation (v16 → v17) | |
| `lattice-derived_coupling_constant_k.md` | Coupling constant derivation history (v1–v4) | |

### [`series_relativity/companion_papers/`](series_relativity/companion_papers/) — 22 companions

| Directory | Topic |
|-----------|-------|
| `c01_absolute_moment_postulate/` | Discrete time structure |
| `c02_dipole_stiffness_C/` | Dipole stiffness and α_geom derivation |
| `c03_born_rule/` | Born rule from CPP |
| `c04_ZBW_hbar_mass_units/` | ZBW, ℏ, and mass units |
| `c05_newtonian_gravity_from_SSV/` | Newtonian gravity from SSV gradients |
| `c06_DP_chaining_as_mass_and_EM_substrate/` | DP chaining as mass and EM substrate |
| `c07_weak_field_GR/` | Weak-field general relativity |
| `c08_strong-field_GR.tex` | Strong-field GR |
| `c09_gravitational_wave_echoes/` | Gravitational wave echoes |
| `c10_Hawking_Radiation_and_the_Planck_Remnant/` | Hawking radiation |
| `c11_Kerr_metric_from_rotational_SSV/` | Kerr metric from rotational SSV |
| `c12_Kerr-Newman_charged_rotating_BH/` | Kerr-Newman solution |
| `c13_superradiance/` | Superradiance |
| `c14_quark_confinement_qDP_chaining/` | Quark confinement from qDP chaining |
| `c15_color_charge_as_emergent/` | Color charge from cage geometry |
| `c20_Spin_I_emergent_Spin-Captured_DPs/` | Spin I: emergent from captured DPs |
| `c21_Spin_II_standing_wave_subharmonics/` | Spin II: standing wave subharmonics |
| `c22_Spin_III_600-cell_Voronoi_eigenvalue/` | Spin III: Voronoi eigenvalue spectrum |
| `research/` | Supporting research material |

---

## [`series_electroweak/`](series_electroweak/) — Electroweak Sector (EW)

W, Z, Higgs bosons and electroweak unification. **Needs consolidation before submission.**

| File | Description | Paper ID |
|------|-------------|----------|
| `cpp_ew1_intro_v2.tex` | EW introduction | EW-1 |
| `cpp_ew2_W_v2.tex` | W boson from CPP | EW-2 |
| `cpp_ew3_Z_v2.tex` | Z boson from CPP | EW-3 |
| `cpp_ew4_Higgs_v2.tex` | Higgs boson from CPP | EW-4 |
| `cpp_ew5_unification_v2.tex` | EW unification | EW-5 |
| `mc_weinberg_unification.py` / `.ipynb` | Monte Carlo: Weinberg angle verification | |
| `mc_weinberg_unification_executed.ipynb` | Pre-executed notebook | |
| `development_EW_Claude.md` | Claude development log | |
| `development_ew_series.md` | EW series development log | |

*Note: OP-EW-1 through OP-EW-6 must be closed before EW submission.*

---

## [`series_quantum_mechanics/`](series_quantum_mechanics/) — QM Foundations

Derivation of quantum mechanics from CPP primitives. **Needs review.**

| Directory | Topic |
|-----------|-------|
| `cpp2040a_schrodinger/` | Schrödinger equation emergence |
| `cpp2040b_superposition/` | Superposition from lattice dynamics |
| `cpp2040c_bell_entanglement/` | Bell inequality and entanglement |
| `cpp2040d_measurement/` | Measurement problem in CPP |
| `cpp2040e_qft/` | QFT emergence |
| `cpp2040f_capstone/` | QM capstone paper |
| `cpp_qm_series.bib` | Bibliography |
| `development/` | Development material |

---

## [`series_foundations/`](series_foundations/) — Foundational Papers

Superdeterminism, DP Sea physics, vacuum energy.

| File/Directory | Description | Paper ID |
|----------------|-------------|----------|
| `cpp_sd1_nexus_superdeterminism_v1.tex` | Nexus superdeterminism | SD-1 |
| `cpp_sd2_h4_angular_structure_v1.tex` | H4 angular structure | SD-2 |
| `cpp_sd3_apparatus_model_v1.tex` | Apparatus model | SD-3 |
| `cpp_sd4_nexus_correlation_function_v1.tex` | Nexus correlation function | SD-4 |
| `cpp_sd5_K0_derivation_v0.tex` | K0 derivation | SD-5 |
| `TN-SR-1_vacuum_energy_holographic_suppression.tex` | Vacuum energy technical note | TN-SR-1 |
| `dp-sea-polarization/` | DP Sea polarization physics | |
| `dp_sea_composition/` | DP Sea composition | |
| `shared/` | Shared resources | |
| `cpp_foundations_series.bib` | Bibliography | |

*All SD papers need review before submission.*

---

## [`series_experimental_phenomena/`](series_experimental_phenomena/) — Experimental Connections

| Directory | Content |
|-----------|---------|
| `600-cell_electron_g-2/` | Electron anomalous magnetic moment analysis |
| `swarm-analysis-chiral_evidence/` | Multi-scale 600-cell fingerprint (swarm/chiral) evidence |

---

## [`series_synthesis/`](series_synthesis/) — Cross-Series Synthesis

| File | Description | Paper ID |
|------|-------------|----------|
| `cpp_qm_synthesis_submission.tex` | QM synthesis paper | QM-1 |

---

## [`series_nuclear/`](series_nuclear/) — Nuclear Physics (Planned)

Currently empty. Nuclear binding is registered as OP-SS-10.

---

## [`open_problems/`](open_problems/) — Open Problems Register

Formal register of all unsolved problems with status tracking.

| Directory | Series | Count | Key problems |
|-----------|--------|-------|-------------|
| [`OP-SS/`](open_problems/OP-SS/) | Strong sector | 10 | Quark mass formula, string tension, chiral condensate, 2-loop β, glueball, Λ_QCD, magnetic moments, nuclear binding |
| [`OP-SM/`](open_problems/OP-SM/) | Standard Model | 10 | k derivation, ε correction, Capotauro, PMNS corrections, cosmological constant, Koide phase θ, AB loop, three generations |
| [`OP-SR/`](open_problems/OP-SR/) | Special relativity | 8 | PSR formula, k constant, SSV definition, Einstein equations, cosmological constant, Big Bang, GP exclusion, equivalence principle |
| [`OP-EW/`](open_problems/OP-EW/) | Electroweak | 6 | η derivation, unified mass formula, loop density, mass ratios, W0 virtual, chirality |
| [`OP-QM/`](open_problems/OP-QM/) | Quantum mechanics | 7 | Born rule, Schrödinger, spin/Pauli, decoherence, entanglement, discrete spectra, QFT |
| [`OP-GLOBAL/`](open_problems/OP-GLOBAL/) | Cross-series | 2 | Three generations (global), SM unification |

Also at top level: `OP-SS-1_quark_mass_ladder_ps1_analysis.md` — detailed PS-1 analysis results.

**Total registered open problems: 43**

---

## [`archive/`](archive/) — Superseded Material

| Content | Description |
|---------|-------------|
| `legacy_structure/` | Pre-reorganisation directory structure |
| `validate_all_600cell.ipynb` | Legacy 600-cell validation notebook |

---

*See [`README.md`](README.md) for the narrative overview.*  
*See [`paper_catalog.md`](paper_catalog.md) for the complete paper list with IDs.*
