# CPP Repository Index

Directory-by-directory map of the entire repository.  
**Last updated:** 31 March 2026

For paper IDs and status, see [`paper_catalog.md`](paper_catalog.md).  
For what is proved vs open, see [`postulates_and_theorems.md`](postulates_and_theorems.md).

---

## Top-Level Files

| File | Purpose |
|------|---------|
| [`README.md`](README.md) | Repository overview, theory summary, 7 submission-ready papers |
| [`INDEX.md`](INDEX.md) | This file — directory map |
| [`paper_catalog.md`](paper_catalog.md) | Master list of all papers with IDs, files, and status |
| [`postulates_and_theorems.md`](postulates_and_theorems.md) | 6 axioms, theorems, corollaries, falsified claims |
| [`predictions.md`](predictions.md) | Every quantitative prediction with status labels |
| [`propositions.md`](propositions.md) | Physically motivated claims not yet proved as theorems |
| [`nomenclature.md`](nomenclature.md) | ID code legend (AXIM, THEO, PROP, CORL, CONJ, etc.) |
| [`solution_candidates.md`](solution_candidates.md) | Candidate solutions for registered open problems |
| `LICENSE` / `LICENSE-CC-BY-4.0.md` | License files |

---

## [`series_strong/`](series_strong/) — Strong Sector (SS)

The SU(3) derivation from 600-cell tetrahedral geometry. **Paper SS-1 is submission-ready.**

| File | Description | Paper ID |
|------|-------------|----------|
| `SS-1_strong_sector_from_600cell_lattice.tex` | **Unified submission package** (v2) — 9 theorems | **SS-1** |
| `SS-1_strong_sector_from_600cell_lattice.pdf` | Compiled PDF | |
| `SS-1a_cage_geometry_eigenvalue_bridge.tex` | Companion: cage geometry and eigenvalue bridge | |
| `SS-1b_su3_algebra_exact_proof.tex` | Companion: T^a = λ^a/2 exact proof | |
| `SS-1c_eight_gluons_hdp_structures.tex` | Companion: eight gluons as hDP structures | |
| `SS-1d_confinement_beta_function.tex` | Companion: confinement and β-function | |
| `SS-1e_hadron_spectrum.tex` | Companion: hadron spectrum | |
| `cpp_strong_series.bib` | Bibliography | |
| `development_strong_series.md` | Session-by-session development log | |

**Documentation files:** `mechanism-SS-1.md`, `glossary-SS-1.md`, `phenomena-SS-1.md`, `reviews-SS-1.md`, `philosophy-SS-1.md`, `development-SS-1.md`

### [`series_strong/notebooks/`](series_strong/notebooks/) — Derivation notebooks

| Notebook | Topic |
|----------|-------|
| `chain_fraying_dynamics.ipynb` | qDP chain bow, string tension, central breaking |
| `confinement_dynamics.ipynb` | Cornell potential, confinement radius |
| `cpp_benchmark.ipynb` | Full benchmark: DP energies, decay constant τ |
| `fractional_charges_overlap.ipynb` | Quark charges from hDP overlap |
| `full_benchmark_table.ipynb` | Complete benchmark comparison table |
| `hadron_spectrum.ipynb` | GMO relations, Ω⁻, quarkonium |
| `jet_multiplicity_lattice.ipynb` | Jet fragmentation predictions |
| `magnetic_moments_zbw.ipynb` | Nucleon magnetic moments |
| `nested_cage_masses.ipynb` | Cage mass model (partially falsified by PS-1) |
| `nucleon_NBT_bonding.ipynb` | Nuclear binding via NBT mechanism |
| `strong_modes_probabilistic.ipynb` | Probabilistic strong mode analysis |
| `zbw_magnetic_effects.ipynb` | ZBW Lorentz forces on qDP chains |

---

## [`series_standard_model/`](series_standard_model/) — Standard Model Emergence (SM)

Papers SM-1 through SM-5 plus topic subdirectories. **All 5 papers submission-ready.**

### [`series_standard_model/papers/`](series_standard_model/papers/) — Paper files and documentation

| File | Paper ID | Status |
|------|----------|--------|
| `SM-1_binding_mechanisms_and_cage_stability.tex` (v6) | **SM-1** | **Submission-ready** |
| `SM-2_mass_generation_geometric_hierarchies.tex` (v30) | **SM-2** | **Submission-ready** |
| `SM-3_k3_spectral_theorem_koide_formula.tex` (v5) | **SM-3** | **Submission-ready** |
| `SM-4_charged_lepton_masses_from_k3.tex` (v5) | **SM-4** | **Submission-ready** |
| `SM-5_tribimaximal_neutrino_mixing_from_k3.tex` (v1) | **SM-5** | **Submission-ready** |
| `SM-TN-2_bridge_original_to_600cell.tex` | SM-TN-2 | Needs correction |

**Documentation files per paper:** `mechanism-SM-N.md`, `glossary-SM-N.md`, `phenomena-SM-N.md`, `reviews-SM-N.md`, `philosophy-SM-N.md`, `development-SM-N.md` — 30 files total, all complete.

### Topic subdirectories

27 topic directories (`p1-binding-mechanisms/`, `p1-dipole-sea/`, `p1-ontology/`, `p2-mass-breakdown-and-validation/`, `p2-alpha-em-derivation/`, `p2-sin2theta-w-derivation/`, `p2-neutrino-mixing-angles/`, etc.) containing supporting derivations, notebooks, and analysis.

---

## [`series_relativity/`](series_relativity/) — Special Relativity (SR)

**Paper SR-1 is submission-ready (v17).**

| File/Directory | Description | Paper ID |
|----------------|-------------|----------|
| `main_special_relativity_emergence/SR-1_special_relativity_emergence.tex` | **SR-1 paper** (v17) | **SR-1** |
| `companion_papers/` | **22 companion papers** (c01–c22) | |
| `600cell_k_alpha_geom_consistency_fix.py` | α_geom numerical verification | |
| `k_prefactor_resolution.md` | α_geom correction documentation (v16 → v17) | |
| `lattice-derived_coupling_constant_k.md` | Coupling constant derivation history | |

---

## [`series_electroweak/`](series_electroweak/) — Electroweak Sector (EW)

W, Z, Higgs bosons and electroweak unification. **Needs consolidation before submission.**

| File | Description | Paper ID |
|------|-------------|----------|
| `EW-1_electroweak_introduction.tex` | EW introduction | EW-1 |
| `EW-2_w_boson_from_cpp.tex` | W boson from CPP | EW-2 |
| `EW-3_z_boson_from_cpp.tex` | Z boson from CPP | EW-3 |
| `EW-4_higgs_boson_from_cpp.tex` | Higgs boson from CPP | EW-4 |
| `EW-5_electroweak_unification.tex` | EW unification | EW-5 |

**Documentation:** 6 files per paper (EW-1 through EW-5) complete — 30 files total.

*OPEN-P-EW-1 through OPEN-P-EW-6 must be closed before EW submission.*

---

## [`series_quantum_mechanics/`](series_quantum_mechanics/) — QM Foundations

Derivation of quantum mechanics from CPP primitives. **Needs review.**

| Directory | ID | Topic |
|-----------|----|-------|
| `QM-1_schrodinger_emergence/` | QM-1 | Schrödinger equation |
| `QM-2_superposition/` | QM-2 | Superposition from lattice |
| `QM-3_bell_entanglement/` | QM-3 | Bell inequality, entanglement |
| `QM-4_measurement_problem/` | QM-4 | Measurement problem |
| `QM-5_qft_emergence/` | QM-5 | QFT emergence |
| `QM-6_capstone/` | QM-6 | QM capstone |

**Documentation:** 6 files per paper (QM-1 through QM-6) — mechanism, phenomena, philosophy, reviews, development complete; glossary complete for QM-1.

---

## [`series_foundations/`](series_foundations/) — Foundational Papers

Superdeterminism, DP Sea physics, vacuum energy.

### [`series_foundations/series_superdeterminism/`](series_foundations/series_superdeterminism/)

| File | Description | Paper ID |
|------|-------------|----------|
| `SD-1_nexus_superdeterminism.tex` (v1) | Nexus superdeterminism | SD-1 |
| `SD-2_h4_angular_structure.tex` (v1) | H4 angular structure | SD-2 |
| `SD-3_apparatus_model.tex` (v1) | Apparatus model | SD-3 |
| `SD-4_nexus_correlation_function.tex` (v1) | Nexus correlation function | SD-4 |
| `SD-5_k0_derivation.tex` (v0) | K0 derivation (research agenda) | SD-5 |

**Documentation:** 6 files per paper (SD-1 through SD-5) complete — 30 files total. Revised 31 March 2026.

### Other foundations files

| File/Directory | Description |
|----------------|-------------|
| `TN-SR-1_vacuum_energy_holographic_suppression.tex` | Vacuum energy technical note |
| `dp-sea-polarization/` | DP Sea polarization physics |
| `dp_sea_composition/` | DP Sea composition |
| `shared/` | Shared resources |

---

## [`series_nuclear/`](series_nuclear/) — Nuclear Physics

| Directory | Content |
|-----------|---------|
| `cpp5014a_gs_derivation/` | Ground state derivation |
| `cpp5014b_delta_gs_exact/` | Delta ground state exact |
| `cpp5014c_O17_magnetic_moment/` | O-17 magnetic moment |

Nuclear binding is registered as OPEN-P-SS-10.

---

## [`series_experimental_phenomena/`](series_experimental_phenomena/) — Experimental Connections

| Directory | Content |
|-----------|---------|
| `600-cell_electron_g-2/` | Electron anomalous magnetic moment analysis |
| `swarm-analysis-chiral_evidence/` | Multi-scale 600-cell fingerprint evidence |

---

## [`series_synthesis/`](series_synthesis/) — Cross-Series Synthesis

| File | Description | Paper ID |
|------|-------------|----------|
| `QM-1_qm_synthesis.tex` | QM synthesis paper | QM-1 |

---

## [`open_problems/`](open_problems/) — Open Problems Register

| Directory | Series | Count |
|-----------|--------|-------|
| `OP-SS/` | Strong sector | 14 |
| `OP-SM/` | Standard Model | 10 |
| `OP-SR/` | Special relativity | 8 |
| `OP-EW/` | Electroweak | 6 |
| `OP-QM/` | Quantum mechanics | 7+ |
| `OP-SD/` | Superdeterminism | 5 |
| `OP-GLOBAL/` | Cross-series | 2 |

**Total registered open problems: 50+**

---

## [`archive/`](archive/) — Superseded Material

| Content | Description |
|---------|-------------|
| `SM-TN-1_reconstruction_original_mass_calculations.tex/.pdf` | Original mass calculation reconstruction |
| `SS-1_strong_sector_v1_superseded.tex` | Earlier strong sector version |
| `legacy_structure/` | Pre-reorganisation directory structure |

---

*See [`README.md`](README.md) for the narrative overview.*  
*See [`paper_catalog.md`](paper_catalog.md) for the complete paper list with IDs.*
