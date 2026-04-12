# CPP Repository Index

Directory-by-directory map of the entire repository.
**Last updated:** 11 April 2026

For paper IDs and status, see [`paper_catalog.md`](paper_catalog.md).
For what is proved vs open, see [`postulates_and_theorems.md`](postulates_and_theorems.md).

---

## Top-Level Files

| File | Purpose |
|------|---------|
| [`README.md`](README.md) | Repository overview, theory summary, 8 registered papers |
| [`INDEX.md`](INDEX.md) | This file — directory map |
| [`paper_catalog.md`](paper_catalog.md) | Master list of all papers with IDs, files, and status |
| [`postulates_and_theorems.md`](postulates_and_theorems.md) | 6 axioms, theorems, corollaries, conjectures |
| [`predictions.md`](predictions.md) | Every quantitative prediction with status labels |
| [`propositions.md`](propositions.md) | Physically motivated claims not yet proved as theorems |
| [`nomenclature.md`](nomenclature.md) | ID code legend (AXIM, THEO, PROP, CORL, CONJ, etc.) |
| [`solution_candidates.md`](solution_candidates.md) | Candidate solutions for registered open problems |
| `LICENSE` / `LICENSE-CC-BY-4.0.md` | License files |

---

## [`templates/`](templates/) — Formatting Standards

| File | Purpose |
|------|---------|
| [`paper-formatting.md`](templates/paper-formatting.md) | Master formatting standard for all CPP papers (16 sections, checklist) |
| [`documentation-suite.md`](templates/documentation-suite.md) | Template for the 8 documentation files per paper |

---

## [`bibliography/`](bibliography/) — Site-Wide Bibliography

| File | Purpose |
|------|---------|
| [`cpp_references.bib`](bibliography/cpp_references.bib) | Aggregated BibTeX from all local paper `.bib` files |

---

## [`series_strong/`](series_strong/) — Strong Sector (SS)

The SU(3) derivation from 600-cell tetrahedral geometry. **SS-1 registered on OSF.**

| File | Description |
|------|-------------|
| `SS-1_strong_sector_from_600cell_lattice.tex/.pdf` | **SS-1** (v2) — 9 theorems |
| `SS-1a` through `SS-1e` companion papers | Cage geometry, SU(3) proof, gluons, confinement, hadrons |
| `cpp_strong_series.bib` | Bibliography |

**Documentation:** `mechanism-SS-1.md`, `glossary-SS-1.md`, `phenomena-SS-1.md`, `reviews-SS-1.md`, `FAQ-SS-1.md`, `philosophy-SS-1.md`, `development-SS-1.md`, `keywords-SS-1.md`

**Notebooks:** 12 notebooks in `notebooks/` (confinement, hadron spectrum, magnetic moments, etc.)

---

## [`series_standard_model/`](series_standard_model/) — Standard Model Emergence (SM)

Papers SM-1 through SM-11. **SM-1 through SM-7 registered on OSF. SM-8 through SM-11 pending.**

### [`series_standard_model/papers/`](series_standard_model/papers/) — Papers and documentation

| File | Paper ID | Version | Status |
|------|----------|---------|--------|
| `SM-1_binding_mechanisms_and_cage_stability.tex/.pdf` | **SM-1** | v6 | Registered |
| `SM-2_mass_generation_geometric_hierarchies.tex/.pdf` | **SM-2** | v30 | Registered |
| `SM-3_k3_spectral_theorem_koide_formula.tex/.pdf` | **SM-3** | v5 | Registered |
| `SM-4_charged_lepton_masses_from_k3.tex/.pdf` | **SM-4** | v5 | Registered |
| `SM-5_tribimaximal_neutrino_mixing_from_k3.tex/.pdf` | **SM-5** | v1 | Registered |
| `SM-6_lepton_mass_spectrum.tex/.pdf` | **SM-6** | v3 | Registered |
| `SM-7_heavy_quark_mass_spectrum.tex/.pdf` | **SM-7** | v2.2 | Registered |
| `SM-8_quark_generation_600cell_shells.tex/.pdf/.bib` | **SM-8** | v4.1 | OSF pending |
| `SM-9_scaling_exponent.tex/.pdf/.bib` | **SM-9** | v2.2 | OSF pending |
| `SM-10_chain_network_FEM.tex/.pdf/.bib` | **SM-10** | v0.1 | OSF pending |
| `SM-11_lattice_scale_nucleon_structure.tex/.pdf` | **SM-11** | v1.0 | OSF pending |

**Documentation per paper:** 7 files × 11 papers. Reviews include FAQ (SM-8 onwards).

**Development transcripts:**
- `SM-9_SM-10_development_transcript_opus.md`
- `SM-10_FEM_computational_journey_transcript.md`
- `SM-11_development_transcript_opus.md`

### [`series_standard_model/figures/`](series_standard_model/figures/)

| Directory | Content |
|-----------|---------|
| `figures-SM-6/` | 4 figures for SM-6 (.svg, .png, .pdf) |

### [`series_standard_model/notebooks/`](series_standard_model/notebooks/)

| Notebook | Topic |
|----------|-------|
| `nb01_SM6_verification.py/.ipynb` | SM-6 numerical verification (10/10 steps pass) |
| `ps1_quark_mass_ladder.ipynb` | Quark mass ladder |
| `SM-11_lattice_scale_nucleon.py` | SM-11 lattice scale and nucleon structure verification |

### [`series_standard_model/cpp-zbw-mixing-fractions/`](series_standard_model/cpp-zbw-mixing-fractions/)

ZBW mixing fraction computations (lepton and quark notebooks + source).

---

## [`series_relativity/`](series_relativity/) — Special Relativity (SR)

**SR-1 registered on OSF (v17).**

| File/Directory | Description |
|----------------|-------------|
| `main_special_relativity_emergence/SR-1_special_relativity_emergence.tex/.pdf` | **SR-1** paper |
| `companion_papers/` | **22 companion papers** (c01–c22) |

**Documentation:** `reviews-SR-1.md`, `FAQ-SR-1.md`, etc.

---

## [`series_electroweak/`](series_electroweak/) — Electroweak Sector (EW)

W, Z, Higgs bosons and electroweak unification.

| File | Paper ID |
|------|----------|
| `EW-1_electroweak_introduction.tex` | EW-1 |
| `EW-2_w_boson_from_cpp.tex` | EW-2 |
| `EW-3_z_boson_from_cpp.tex` | EW-3 |
| `EW-4_higgs_boson_from_cpp.tex` | EW-4 |
| `EW-5_electroweak_unification.tex` | EW-5 |

**Documentation:** 8 files per paper (EW-1 through EW-5) — 40 files total.

### [`series_electroweak/development/`](series_electroweak/development/)

| File | Content |
|------|---------|
| `development-EW-Weinberg-Koide-session-20260401.md` | Full 12-section session log from the Weinberg/Koide derivation (1 Apr 2026) |
| `development_EW_Claude.md` | Earlier EW development history |

### [`series_electroweak/notebooks/`](series_electroweak/notebooks/)

Monte Carlo Weinberg angle unification code.

---

## [`series_quantum_mechanics/`](series_quantum_mechanics/) — QM Foundations

Derivation of quantum mechanics from CPP primitives.

| Paper ID | Topic |
|----------|-------|
| QM-1 | Schrödinger equation emergence |
| QM-2 | Superposition from lattice |
| QM-3 | Bell inequality, entanglement |
| QM-4 | Measurement problem |
| QM-5 | QFT emergence |
| QM-6 | QM capstone |

**Documentation:** 8 files per paper (QM-1 through QM-6) — 48 files total.

---

## [`series_foundations/`](series_foundations/) — Foundational Papers

### [`series_foundations/series_superdeterminism/`](series_foundations/series_superdeterminism/)

| Paper ID | Topic | Version |
|----------|-------|---------|
| SD-1 | Nexus superdeterminism | v1 |
| SD-2 | H4 angular structure | v1 |
| SD-3 | Apparatus model | v1 |
| SD-4 | Nexus correlation function | v1 |
| SD-5 | K0 derivation (research agenda) | v0 |

**Documentation:** 8 files per paper — 40 files total.

### Other foundations files

DP Sea polarization, composition, vacuum energy.

---

## [`open_problems/`](open_problems/) — Open Problems Register

| Series | Count |
|--------|-------|
| Strong sector (OP-SS) | 14 |
| Standard Model (OP-SM) | 10 |
| Special relativity (OP-SR) | 8 |
| Electroweak (OP-EW) | 6 |
| Quantum mechanics (OP-QM) | 7+ |
| Superdeterminism (OP-SD) | 5 |
| Cross-series (OP-GLOBAL) | 2 |

**Total registered open problems: 50+**

Also contains conjecture files: `CONJ-EW-1_weinberg_angle.md`, `CONJ-SM-6_koide_phase.md`.

---

## [`archive/`](archive/) — Superseded and Exploratory Material

| Directory | Content |
|-----------|---------|
| `grok-exploratory-SM/` | 23 exploratory topic folders (p1-*, p2-*, p3-*, suppression/) — unvetted |
| `grok-exploratory-nuclear/` | Nuclear physics stubs (3 files) — unvetted |
| `grok-exploratory-experimental/` | g-2 analysis, swarm analysis (154 files) — unvetted |
| `legacy_structure/` | Pre-reorganisation directory structure |
| `SM-TN-1_reconstruction_original_mass_calculations.tex/.pdf` | Original mass calculation |
| `SS-1_strong_sector_v1_superseded.tex` | Earlier strong sector version |

*Archived material has NOT been through the formal review process. It may contain useful raw material for future papers.*

---

*See [`README.md`](README.md) for the narrative overview.*
*See [`paper_catalog.md`](paper_catalog.md) for the complete paper list with IDs.*
*See [`templates/paper-formatting.md`](templates/paper-formatting.md) for paper generation standards.*
