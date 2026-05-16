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

## [`flagship_papers/`](flagship_papers/) — Cross-Cutting Apex Papers

Cross-cutting papers that solve named unsolved problems in physics, make forced-choice prospective predictions, or provide cross-domain unification. Established Session 37 (patch 0293); reorganized at Session 38 (patch 0295) into the Option-3 four-family + unification SF-line architecture; **revised at Session 41 (patch 0301) to 7-paper architecture** — six family/sector flagship papers (SF-1 through SF-6) plus a grand unification synthesis (SF-7).

| File / Folder | Description |
|------|-------------|
| [`README.md`](flagship_papers/README.md) | Architecture overview, inclusion criterion, SF-line table, current status |
| [`SF-line_switch_log.md`](flagship_papers/SF-line_switch_log.md) | Family-switch protocol + log; serial SF-line work with derivation-logic-driven switches between families |
| [`charged_leptons/`](flagship_papers/charged_leptons/) | **SF-1** — Charged Lepton Mass Spectrum from K3 + 600-Cell Geometry; planned, primarily reframing of SM-3/4/6 |
| [`electroweak/`](flagship_papers/electroweak/) | **SF-2** — Electroweak Cage-Boson Unification (W±/W⁰/Z/H from 600-Cell Geometry); **v1.0 SHIPPED Session 83 close 14 May 2026 Patch 0368** (main paper + Companion joint SHIP); three-reviewer convergence (ChatGPT structural-architecture validation + Copilot SHIP-ready + Grok *"flagship-series work at its strongest, SHIP at v1.0"*); 24-patch campaign Sessions 81-83 (Patches 0345-0368); W⁰ catalyst framework externally validated as central original contribution; mass-degeneracy structural prediction $m_{W^0} = m_{W^\pm}$ confirmed at parametric-scaling level by sensitivity-scan $\Delta T \approx 0$; six OPEN-FP-SF-2-* problems systematically registered; PD-004 publication-pathway captured + operating-system version-discipline rule codified + W⁰ neutrino scattering sketch captured at Patch 0367; ClearPC PDF compile pending; documentation suite Patches 0370-0375 forward queue (registers freeze, Tier-4 reasoning, development+transcript, 7-file companion suite, anthology chapter, TATWD integration) |
| [`quarks/`](flagship_papers/quarks/) | **SF-3** — Quark Sector Unification from 600-Cell Distance Shells; planned, primarily reframing of SM-7/8/9/10 |
| [`neutrinos/`](flagship_papers/neutrinos/) | **SF-4 [v2.0 SHIPPED Session 60]** — Neutrino Sector Unification from 600-Cell Geometry; cage-shell mass formula + Picture A axiomatic closure; v1.0 partial-closure (Session 54 patch 0314) → v2.0 Picture A axiomatic closure (Session 60 patch 0321) |
| [`neutrinos/sf-4_neutrinos.tex`](flagship_papers/neutrinos/sf-4_neutrinos.tex) | **SF-4 v4.0 SHIPPED (Session 72, patch 0333)**: 2296 lines source; flagship neutrino-sector paper with OPEN-FP-SF-4-1 + OPEN-FP-SF-4-2 + SM-5 op:nu_id RESOLVED via cross-sector closure campaign Sessions 68–72 (patches 0329–0333) on top of v3.0 OPEN-FP-SF-4-1 RESOLVED (patches 0316–0327); 25-entry bibliography; 5 theorems including new Theorem thm:k3_cage_shell_coupling Composite K3-Cage-Shell Coupling Theorem added at v4.0. **FIRST CROSS-SECTOR CLOSURE IN CPP** — single derivation chain simultaneously resolves OPEN-FP-SF-4-2 and SM-5 op:nu_id |
| [`neutrinos/sf-4_neutrinos.pdf`](flagship_papers/neutrinos/sf-4_neutrinos.pdf) | **SF-4 v4.0 SHIPPED compiled PDF (Session 72, patch 0333)**: 48 pages, 603 KB |
| [`neutrinos/documentation_suite/`](flagship_papers/neutrinos/documentation_suite/) | **SF-4 four-tier documentation suite at v2.0 ship**: handover-SF-4 (Session 60 v2.0 SHIP close) + development-SF-4 (Vignettes 1–24 Sessions 37–60) + transcript-SF-4 (per-session transactions Sessions 37–60) + reasoning-SF-4 (Tier 4 verbatim reasoning + pointer to working sketch document) |
| [`neutrinos/sf-4_outline.md`](flagship_papers/neutrinos/sf-4_outline.md) | SF-4 v0.1 outline document (Session 44, patch 0304): section-by-section structure, predictions table, falsifier set, drafting plan |
| [`neutrinos/sketches/`](flagship_papers/neutrinos/sketches/) | SF-4 staging + closure documents. Currently: `SF-4_neutrino_sector_audit.md` (Session 37), `SF-4_mechanism_selected.md` (Session 39), `SF-4_suppression_derivation.md` (Sessions 40–41 OPEN-FP-SF-4-1 v1.0 partial closure), `SF-4_k3_cage_shell_consistency.md` (Sessions 42–43 OPEN-FP-SF-4-2 PARTIAL CLOSURE), **`SF-4_picture_A_axiomatic_closure.md` (Sessions 55–60, 1106 lines, Tier-4 closure source for Picture A v2.0)**, **`SF-4_alpha_exponent_closure.md` (Sessions 62–65, 1184 lines, Tier-4 closure source for α-exponent residual v3.0)**, **`SF-4_open_fp_sf_4_2_closure.md` (Sessions 68–71, 750 lines, Tier-4 closure source for OPEN-FP-SF-4-2 + SM-5 op:nu_id cross-sector closure v4.0)** |
| [`capotauro/`](flagship_papers/capotauro/) | **Capotauro [v1.0 SHIPPED Session 122 close 16 May 2026 Patch 0415]** — Substrate-Vacuum Chirality as Primitive Feature: Composite Wigner-Eckart Closure of the K3-Doublet Chirality Matrix Element; conditional theorem closure paper closing OPEN-SM-4 sub-claim (c) via THEO-CAP-1 ($|M| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ on K3-doublet); primary empirical prediction $\Delta p_{LR} \approx 0.0394$ validated within 2% of leptogenesis back-derived $\sim 0.04$. **Third flagship paper to ship at v1.0** after SS-9 / SF-4 / SF-2; **first flagship paper outside the SF-N numerical convention**. v1.0 SHIP at Patch 0415 is version-bump-only from v0.9 Patch 0413; cross-reviewer convergence on SHIP-readiness achieved at v0.8 Session 119 Patch 0412 (ChatGPT round-3 + CoPilot round-1 + Grok round-1 SHIP-ready verdicts) |
| [`capotauro/capotauro.tex`](flagship_papers/capotauro/capotauro.tex) | **Capotauro v1.0 SHIPPED (Session 122 Patch 0415)**: 1149 lines source; 46 pages compiled at v0.9 (601 KB PDF at v0.9; v1.0 SHIP is version-bump-only with no content change); 6 theorem-family environments (Theorem 5.1 composite Wigner-Eckart + Definition 2.1 + Remark 2.2 + Lemmas 4.2/5.2/5.3); 10 foundational inputs FI-C-1 through FI-C-10 + 4 CPP axioms (A1+A3+A4+A7); primitive-feature framing for FI-C-9 substrate chirality magnitude $|\chi| = \phi^{-3}$ adopted at v0.9 Patch 0413 per CPP core methodological principle that mathematical descriptions are not physical mechanisms |
| [`capotauro/sketches/`](flagship_papers/capotauro/sketches/) | Capotauro staging + closure documents. Currently: `capotauro_outline.md` (327 lines, Session 104 Patch 0398), **`Capotauro_chi_phi_closure.md` (681 lines, parent sketch covering FI-C-9 + FI-C-10 closure trajectory Sessions 87-102)**, **`Capotauro_subclaim_c_wigner_eckart.md` (2146 lines, sub-claim (c) detailed eight-step closure with Theorem 18.1 + §22 v1.0 closure narrative)**, **`Capotauro_chiral_mechanism_candidate.md` (296 lines, Session 121 Patch 0414 Reading C geometric-chirality candidate for sub-claim (b) substrate chirality mechanism candidate derivation — primitive 4D direction $\hat{n}$ producing direction-correlated edge-length variation at $\phi^{-3}$ scale; Tier-4 Layer 1/Layer 2 epistemic status; Layer 3 closure trajectory tracked at OPEN-FI-C-9-FP-MECHANISM)** |
| [`capotauro/documentation_suite/`](flagship_papers/capotauro/documentation_suite/) | Capotauro documentation suite (Patch 0415 close). Currently: `changelog-capotauro.md` (Patch 0415 updated with v1.0 SHIP version section + Patch 0415 register row + Last-updated footer Session 122). Remaining four-tier files (handover-capotauro.md, development-capotauro.md, transcript-capotauro.md, reasoning-capotauro.md) + 7 standalone companion files (mechanism, glossary, phenomena, philosophy, development, reviews, keywords) planned Patches 0416+ across Sessions 123+ per `templates/paper_completion_checklist.md` |
| [`capotauro/reviews/`](flagship_papers/capotauro/reviews/) | Capotauro review archive. 5 review files at v1.0 SHIP: `chatgpt_v0.6_session_113.md` (ChatGPT round-1) + `chatgpt_v0.7_session_117.md` (ChatGPT round-2) + `chatgpt_v0.8_session_119.md` (ChatGPT round-3 SHIP-ready verdict) + `copilot_v0.8_session_119.md` (CoPilot round-1 SHIP-ready verdict) + `grok_v0.8_session_119.md` (Grok round-1 SHIP-ready verdict) — cross-reviewer convergence on SHIP-readiness achieved at v0.8 Patch 0412 Session 119 |
| [`strong/`](flagship_papers/strong/) | **SF-5 (NEW S41)** — Strong-Sector Unification: gluon counting from 4-tetrahedral-vertex bonding (CONJ-SS-Gluon-4Vertex), glueballs (OPEN-SS-6), confinement, hadron spectrum from SS-1 through SS-9+ corpus |
| [`electromagnetism/`](flagship_papers/electromagnetism/) | **SF-6 (NEW S41)** — Electromagnetism Unified: classical Maxwell + special-relativistic photon kinematics + QED phenomena from eDP-sea polarization; cross-domain bridge synthesizing EW-1 through EW-5 + SR-1 + QM-1 through QM-6 |
| [`unification/`](flagship_papers/unification/) | **SF-7 (renumbered S41 from SF-5)** — Standard Model Grand Unification — Hierarchy Without Hierarchy; synthesis on top of SF-1 through SF-6. Contains original Track-1 hierarchy outline as source material |

See [`research_priorities.md`](research_priorities.md) for the strategic frame.

---

## [`series_strong/`](series_strong/) — Strong Sector (SS)

The SU(3) derivation from 600-cell tetrahedral geometry, uniqueness proof, nucleon structure, string tension, deuteron binding, deuteron observables scoping, alpha-cluster regime, and interstitial-neutron 2E/V scaling. **SS-1 registered on OSF. SS-2, SS-3, SS-4, SS-5, SS-6, SS-8 pending. SS-7 has existing OSF DOI from v0.1; v1.2 update pending.**

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
| `SS-8/SS-8_interstitial_neutron_2EV_scaling.tex/.pdf` | **SS-8** (v1.0) — Interstitial-neutron binding and the 2E/V scaling law on the alpha-polytope; 42 conditional zero-parameter predictions (12 primary at $N_\text{ex}=2$ across $N_\alpha \in [3,14]$ + 30 secondary at $N_\text{ex} \in [3,8]$); two sub-1% agreements at the most symmetric polytopes (²⁶Mg octahedron, ⁴²Ca gyroelongated square bipyramid); D1–D3 conditional theorems registered; opens OPEN-SS-26, OPEN-SS-27, OPEN-SS-28; partially resolves OPEN-SS-23. Per-paper subfolder per §11 convention. |
| `cpp_strong_series.bib` | Bibliography |

**Documentation:** SS-1: `mechanism-SS-1.md`, `glossary-SS-1.md`, `phenomena-SS-1.md`, `reviews-SS-1.md`, `FAQ-SS-1.md`, `philosophy-SS-1.md`, `development-SS-1.md`, `keywords-SS-1.md`
SS-2: `mechanism-SS-2.md`, `glossary-SS-2.md`, `phenomena-SS-2.md`, `philosophy-SS-2.md`, `development-SS-2.md`, `reviews-SS-2.md`, `keywords-SS-2.md`
SS-3: `mechanism-SS-3.md`, `glossary-SS-3.md`, `phenomena-SS-3.md`, `philosophy-SS-3.md`, `development-SS-3.md`, `reviews-SS-3.md`, `keywords-SS-3.md`, `FAQ-SS-3.md`
SS-4: documentation suite pending
SS-5: 7 doc-suite files in `series_strong/papers/SS-5/documentation_suite/` (mechanism, glossary, phenomena, philosophy, keywords, development, reviews — all at v6 header currency); plus `transcript-SS-5.md` (renamed from `SS-5_development_transcript.md` during patch 0019 migration)
SS-6: documentation suite pending
SS-7: 8 doc-suite files in `series_strong/papers/SS-7/documentation_suite/` (mechanism, glossary, phenomena, philosophy, keywords, development, reviews, lay-summary — all at v1.2 header currency); plus `transcript-SS-7.md` (renamed from `SS-7_development_transcript.md` during patch 0020 migration), `SS-7_v1.2_transcript.md` (v1.2 cycle addendum), `handover-SS-7.md` (renamed from `SS-7_v1.2_handover.md`), and `SS-7_OSF_registration_status.md` (v1.1 status doc; v1.2 update pending)
SS-8: 3 session-continuity files in `series_strong/papers/SS-8/documentation_suite/` (`handover-SS-8.md`, `development-SS-8.md`, `transcript-SS-8.md`); 0 of 7 companion documentation files (mechanism, glossary, phenomena, philosophy, reviews, keywords, FAQ) — pending. 5 Python verification scripts in `scripts/`. 4 sketch files in `sketches/`. 5 founders-voice notes in `founders_voice/`. 10 reviewer correspondence files in `reviews/` (Round 1 + Round 2). 5 letters in `letters/`.

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

## [`session_logs/`](session_logs/) — Cross-Paper Session Logs

Running journal for cross-paper work — sessions that touch programme-level infrastructure (registries, bootup, OS), produce policy/methodology decisions, span multiple papers, or carry post-completion addenda for prior papers. Established 26 April 2026 per the Two-Trigger Documentation Discipline (`templates/operating_system.md` §4).

| File | Topic |
|------|-------|
| `README.md` | Convention description and indexing |
| `2026-04-25_session_log.md` | Bootup stress-test (patches 0022–0023); OPEN-ORG-003 swarm-tally audit (patches 0024–0026); SS-8 v1.0 paper-completion Session 1 (patch 0027) |
| `2026-04-25_session_log_2.md` | (continuation) SS-8 v1.0 documentation suite (patch 0028) |
| `2026-04-26_session_log.md` | SS-8 v1.0 Session 2 medium-priority (patch 0029); Phase 7 Completion Gate adoption-then-repeal; Two-Trigger Discipline + Cross-Paper Session Log convention (patch 0030) |

**Per-paper continuity files** (`handover-[S]-[N].md`, `transcript-[S]-[N].md`, `development-[S]-[N].md`) live alongside each paper in `series_*/papers/[S]-[N]/documentation_suite/` per `operating_system.md` §11. The session log folder is for the cross-cutting work that doesn't fit those files.

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
