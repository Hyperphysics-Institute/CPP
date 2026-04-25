# CPP Repository Index

Directory-by-directory map of the entire repository.
**Last updated:** 11 April 2026

For paper IDs and status, see [`paper_catalog.md`](paper_catalog.md).
For what is proved vs open, see [`Research_Frontier.md`](Research_Frontier.md) (open problems) and [`theorem-registry.md`](theorem-registry.md) (proved results).

---

## Top-Level Files

| File | Purpose |
|------|---------|
| [`README.md`](README.md) | Repository overview, theory summary, 8 registered papers |
| [`INDEX.md`](INDEX.md) | This file — directory map |
| [`paper_catalog.md`](paper_catalog.md) | Master list of all papers with IDs, files, and status |
| [`Research_Frontier.md`](Research_Frontier.md) | **The dashboard** — all open problems, conjectures, propositions with status |
| [`theorem-registry.md`](theorem-registry.md) | All proved theorems by series, with axiom dependencies |
| [`axiom-registry.md`](axiom-registry.md) | All axioms with tiers, usage, and prediction tracking |
| [`predictions.md`](predictions.md) | Every quantitative prediction with status labels |
| [`nomenclature.md`](nomenclature.md) | ID code legend (AXIM, THEO, PROP, CORL, CONJ, etc.) |
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

The SU(3) derivation from 600-cell tetrahedral geometry, uniqueness proof, nucleon structure, string tension, deuteron binding, deuteron observables scoping, and alpha-cluster regime. **SS-1 registered on OSF. SS-2, SS-3, SS-4, SS-5, SS-6 pending. SS-7 has existing OSF DOI from v0.1; v1.2 update pending.**

| File | Description |
|------|-------------|
| `SS-1_strong_sector_from_600cell_lattice.tex/.pdf` | **SS-1** (v2) — 9 theorems |
| `SS-1a` through `SS-1e` companion papers | Cage geometry, SU(3) proof, gluons, confinement, hadrons |
| `SS-2_lattice_scale_nucleon_structure.tex/.pdf` | **SS-2** (v1.0) — Lattice grounding, nucleon structure |
| `SS-3_su3_uniqueness.tex/.pdf` | **SS-3** (v1.3) — SU(3) uniqueness from tetrahedral cage |
| `SS-3_su3_uniqueness.py` | Numerical verification (5 checks) |
| `SS-4_string_tension.tex/.pdf` | **SS-4** (v0.1) — String tension from face-mode multiplicity, $\sigma = M_0 z^2/(\varphi\,l_\text{edge}) = 926.5$ MeV/fm |
| `SS-5/SS-5_light_nuclei_open_vertex_cascade.tex/.pdf` | **SS-5** (v6) — Light-nuclei binding via open-vertex cascade; $B_d, B_{^3H}, B_{^3He}, B_{^4He}$ at $\leq 5.3\%$ error, zero params; $^5$He, $^5$Li, $^8$Be unbound predictions. Per-paper subfolder per §11 convention. |
| `SS-6/SS-6_deuteron_observables_beyond_binding.tex/.pdf` | **SS-6** (v0.2) — Deuteron observables beyond binding (scoping): rigid-bipyramid intrinsic $Q_d$ oblate (reveals $Q_d$ orbital-dominated); zero-range $a_{np} = 1/\kappa = 4.32$ fm from $B_d$ alone. Per-paper subfolder per §11 convention. |
| `SS-7/SS-7_alpha_cluster_edge_formula.tex/.pdf` | **SS-7** (v1.2) — Alpha-cluster regime and the 3N−6 edge formula for medium-mass nuclei; 12 concurrent zero-parameter N=Z alpha-chain predictions at $N_\alpha \in [3,14]$, RMS 0.80%; retires OPEN-SS-22, registers OPEN-SS-25. Per-paper subfolder per §11 convention. |
| `cpp_strong_series.bib` | Bibliography |

**Documentation:** SS-1: `mechanism-SS-1.md`, `glossary-SS-1.md`, `phenomena-SS-1.md`, `reviews-SS-1.md`, `FAQ-SS-1.md`, `philosophy-SS-1.md`, `development-SS-1.md`, `keywords-SS-1.md`
SS-2: `mechanism-SS-2.md`, `glossary-SS-2.md`, `phenomena-SS-2.md`, `philosophy-SS-2.md`, `development-SS-2.md`, `reviews-SS-2.md`, `keywords-SS-2.md`
SS-3: `mechanism-SS-3.md`, `glossary-SS-3.md`, `phenomena-SS-3.md`, `philosophy-SS-3.md`, `development-SS-3.md`, `reviews-SS-3.md`, `keywords-SS-3.md`, `FAQ-SS-3.md`
SS-4: documentation suite pending
SS-5: 7 doc-suite files in `series_strong/papers/SS-5/documentation_suite/` (mechanism, glossary, phenomena, philosophy, keywords, development, reviews — all at v6 header currency); plus `transcript-SS-5.md` (renamed from `SS-5_development_transcript.md` during patch 0019 migration)
SS-6: documentation suite pending
SS-7: 8 doc-suite files in `series_strong/papers/SS-7/documentation_suite/` (mechanism, glossary, phenomena, philosophy, keywords, development, reviews, lay-summary — all at v1.2 header currency); plus `transcript-SS-7.md` (renamed from `SS-7_development_transcript.md` during patch 0020 migration), `SS-7_v1.2_transcript.md` (v1.2 cycle addendum), `handover-SS-7.md` (renamed from `SS-7_v1.2_handover.md`), and `SS-7_OSF_registration_status.md` (v1.1 status doc; v1.2 update pending)

**Notebooks:** 12 notebooks in `notebooks/` (confinement, hadron spectrum, magnetic moments, etc.) + `SS-2_lattice_scale_nucleon.py` + `SS-3_su3_uniqueness.py`

**Development transcripts:** `SS-2_development_transcript_opus.md`, `series_strong/papers/SS-5/founders_voice/SS-5_session_bootup_prompt.md`, `series_strong/papers/SS-5/documentation_suite/transcript-SS-5.md` (renamed from `SS-5_development_transcript.md` via patch 0019)

---

## [`series_standard_model/`](series_standard_model/) — Standard Model Emergence (SM)

Papers SM-1 through SM-10. **SM-1 through SM-7 registered on OSF. SM-8 through SM-10 pending.**

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

**Documentation per paper:** 7 files × 10 papers. Reviews include FAQ (SM-8 onwards).

**Development transcripts:**
- `SM-9_SM-10_development_transcript_opus.md`
- `SM-10_FEM_computational_journey_transcript.md`

### [`series_standard_model/figures/`](series_standard_model/figures/)

| Directory | Content |
|-----------|---------|
| `figures-SM-6/` | 4 figures for SM-6 (.svg, .png, .pdf) |

### [`series_standard_model/notebooks/`](series_standard_model/notebooks/)

| Notebook | Topic |
|----------|-------|
| `nb01_SM6_verification.py/.ipynb` | SM-6 numerical verification (10/10 steps pass) |
| `ps1_quark_mass_ladder.ipynb` | Quark mass ladder |

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

## [`problem_histories/`](problem_histories/) — Problem Narratives

The full journey of each major open problem — from identification through wrong turns to resolution.

| File | Problem |
|------|---------|
| `PH-CONJ-EW-1.md` | Weinberg angle discovery |
| `PH-THEO-SM8-3.md` | Three quark generations |
| `PH-THEO-SS-9.md` | Charge quantisation δ = 1/3 |
| `PH-FALS-C-SM-2.md` | φ^(3(l-1)) falsification |
| `PH-OPEN-SM-cage-1.md` | Scaling exponent α = 2.38 |
| `PH-OPEN-SM-10-FEM.md` | FEM chain network simulation |

**Master dashboard:** See [`Research_Frontier.md`](Research_Frontier.md) for the complete register (84 entries across all sectors).

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
