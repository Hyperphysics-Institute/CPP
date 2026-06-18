# CPP Repository Index

Directory-by-directory map of the entire repository.
**Last updated:** 26 May 2026 (Patch 0586 Session 144 close, **Series Umbrella (SU) section restructure**: SSCA papers (Capotauro v1.0+v2.0, Chirality Continuum, F.1 Dynamical Substrate Law) extracted from `flagship_papers/` section and re-placed under new `## series_umbrella/` section corresponding to the Patch 0571d SU establishment + SSCA migration. New section added between flagship_papers and series_strong; flagship_papers section now contains only SF-line entries (SF-1 through SF-7) plus the migrated SSCA entries' new home is series_umbrella/series_substrate_chirality_arc/. The new section also adds entries for `README-SU.md` + `README-SSCA.md` + `manifestation_inventory.md` SU governance documents not previously indexed.) Earlier: 25 May 2026 (Patch 0577 Session 143; gap-fill audit on F.1 dynamical_substrate_law/ subfolder representation — added entries for `layer3_promotion/` Layer 3 promotion arc artifacts + `phase_7B_content_pack.md` Phase 7B execution scaffolding (Patch 0573) + `development-transcripts/` curated transcripts directory (Patch 0572i). These three were created after Patch 0572h initial INDEX entry registration and were missing.) Earlier: 24 May 2026 (Patch 0572h Session 143; added F.1 dynamical_substrate_law/ entry to flagship_papers section for the first F-line flagship v1.0 SHIP)
**Earlier last updated:** 11 April 2026

For paper IDs and status, see [`paper_catalog.md`](paper_catalog.md).
For what is proved vs open, see [`research_frontier.md`](research_frontier.md) (open problems) and [`theorem-registry.md`](theorem-registry.md) (proved results).

---

## Top-Level Files

| File | Purpose |
|------|---------|
| [`README.md`](README.md) | Repository overview, theory summary, 8 registered papers |
| [`INDEX.md`](INDEX.md) | This file — directory map |
| [`paper_catalog.md`](paper_catalog.md) | Master list of all papers with IDs, files, and status |
| [`research_frontier.md`](research_frontier.md) | **The dashboard** — all open problems, conjectures, propositions with status |
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
| [`quarks/`](flagship_papers/quarks/) | **SF-3 [v1.0 SHIPPED Session 161, 14 June 2026, Patch 1505]** — The Quark Sector from 600-Cell Geometry (masses + $\alpha_s$ + Koide phase + generation count from a single $m_e$ calibration); synthesis/reframing of SM-7/8/9/10 + SS-1/2 + SM-6 (no new derivation); $m_c$ demoted to derived; Proposition 5.1 (phase–mass bookkeeping separation); CKM inherited-open (OPEN-FP-3-CKM). Four review rounds, Grok SHIP all four + ChatGPT/Copilot REVISE→SHIP. Includes `sf-3_quarks.tex`, `code/1500_verify_sf3_core.py`, `code/sf-3_reproduce.ipynb` (executed reproducibility notebook — asserts every headline number against the paper), `documentation_suite/` (changelog + reasoning), `review/` (four review sets) |
| [`neutrinos/`](flagship_papers/neutrinos/) | **SF-4 [v2.0 SHIPPED Session 60]** — Neutrino Sector Unification from 600-Cell Geometry; cage-shell mass formula + Picture A axiomatic closure; v1.0 partial-closure (Session 54 patch 0314) → v2.0 Picture A axiomatic closure (Session 60 patch 0321) |
| [`neutrinos/sf-4_neutrinos.tex`](flagship_papers/neutrinos/sf-4_neutrinos.tex) | **SF-4 v4.0 SHIPPED (Session 72, patch 0333)**: 2296 lines source; flagship neutrino-sector paper with OPEN-FP-SF-4-1 + OPEN-FP-SF-4-2 + SM-5 op:nu_id RESOLVED via cross-sector closure campaign Sessions 68–72 (patches 0329–0333) on top of v3.0 OPEN-FP-SF-4-1 RESOLVED (patches 0316–0327); 25-entry bibliography; 5 theorems including new Theorem thm:k3_cage_shell_coupling Composite K3-Cage-Shell Coupling Theorem added at v4.0. **FIRST CROSS-SECTOR CLOSURE IN CPP** — single derivation chain simultaneously resolves OPEN-FP-SF-4-2 and SM-5 op:nu_id |
| [`neutrinos/sf-4_neutrinos.pdf`](flagship_papers/neutrinos/sf-4_neutrinos.pdf) | **SF-4 v4.0 SHIPPED compiled PDF (Session 72, patch 0333)**: 48 pages, 603 KB |
| [`neutrinos/documentation_suite/`](flagship_papers/neutrinos/documentation_suite/) | **SF-4 four-tier documentation suite at v2.0 ship**: handover-SF-4 (Session 60 v2.0 SHIP close) + development-SF-4 (Vignettes 1–24 Sessions 37–60) + transcript-SF-4 (per-session transactions Sessions 37–60) + reasoning-SF-4 (Tier 4 verbatim reasoning + pointer to working sketch document) |
| [`neutrinos/sf-4_outline.md`](flagship_papers/neutrinos/sf-4_outline.md) | SF-4 v0.1 outline document (Session 44, patch 0304): section-by-section structure, predictions table, falsifier set, drafting plan |
| [`neutrinos/sketches/`](flagship_papers/neutrinos/sketches/) | SF-4 staging + closure documents. Currently: `SF-4_neutrino_sector_audit.md` (Session 37), `SF-4_mechanism_selected.md` (Session 39), `SF-4_suppression_derivation.md` (Sessions 40–41 OPEN-FP-SF-4-1 v1.0 partial closure), `SF-4_k3_cage_shell_consistency.md` (Sessions 42–43 OPEN-FP-SF-4-2 PARTIAL CLOSURE), **`SF-4_picture_A_axiomatic_closure.md` (Sessions 55–60, 1106 lines, Tier-4 closure source for Picture A v2.0)**, **`SF-4_alpha_exponent_closure.md` (Sessions 62–65, 1184 lines, Tier-4 closure source for α-exponent residual v3.0)**, **`SF-4_open_fp_sf_4_2_closure.md` (Sessions 68–71, 750 lines, Tier-4 closure source for OPEN-FP-SF-4-2 + SM-5 op:nu_id cross-sector closure v4.0)** |
| [`strong/`](flagship_papers/strong/) | **SF-5 [v1.0 SHIPPED Session 161, 15 June 2026, Patches 1520→1521]** — Strong-Sector Unification from 600-Cell Geometry (SU(3) + the eight gluons + confinement + string tension 926.5 MeV/fm + $\alpha_s = 5/(8\phi)$ + the alpha-cluster binding cascade from the tetrahedral cage, single $m_e$ calibration); synthesis/reframing of SS-1b/1c/1d, SS-2, SS-3, SS-4, SS-5, SS-7, SS-9, SM-7, SM-8 (no new derivation). Gluon-counting decision: lead the theorem-level SS-1c octet, demote CONJ-SS-Gluon-4Vertex to a flagged conjecture; glueball mass inherited-open (OPEN-FP-5-GLUEBALL). 4/4 panel SHIP (ChatGPT/Grok/Gemini/Copilot). Includes `sf-5_strong.tex`, `code/1520_verify_sf5_core.py`, `documentation_suite/` (10 four-tier files), `review/` (four review sets + cycle synthesis), `reasoning/` (1520, 1521), `phase_7B_content_pack.md`; anthology chapter at `book_project/chapters/SF-5_the_octet_was_in_the_tetrahedron.md` |
| [`electromagnetism/`](flagship_papers/electromagnetism/) | **SF-6 (NEW S41)** — Electromagnetism Unified: classical Maxwell + special-relativistic photon kinematics + QED phenomena from eDP-sea polarization; cross-domain bridge synthesizing EW-1 through EW-5 + SR-1 + QM-1 through QM-6 |
| [`unification/`](flagship_papers/unification/) | **SF-7 (renumbered S41 from SF-5)** — Standard Model Grand Unification — Hierarchy Without Hierarchy; synthesis on top of SF-1 through SF-6. Contains original Track-1 hierarchy outline as source material |

See [`research_priorities.md`](research_priorities.md) for the strategic frame.

---

## [`series_umbrella/`](series_umbrella/) — Problem-Arc Papers (SU)

Series Umbrella container for *problem-arc-organized* paper groupings. Established 26 May 2026 (Session 144 Patch 0571d). Organized along the **problem-arc axis** (not phenomenology-sector axis); papers under SU sit in sub-umbrellas (`series_<arc-name>/`) when they share a stable problem-arc identity, or directly under `series_umbrella/<paper-name>/` when not yet grouped. SU is a peer container to the union of phenomenology-sector series at /CPP/ root; the third paper-container kind alongside sector series (`series_<sector>/`) and sector flagship (`flagship_papers/<sector>/`). See `series_umbrella/README-SU.md` for full programme-philosophy README + `templates/operating_system.md` §15.13 for the regrouping audit discipline.

| File / Folder | Description |
|------|-------------|
| [`README-SU.md`](series_umbrella/README-SU.md) | Full SU programme-philosophy README (~200 lines): two-axis taxonomy rationale (phenomenology-sector vs problem-arc); what SU contains (sub-umbrellas + ungrouped papers); accumulate-then-group workflow; regrouping audit discipline (threshold count ≥ 3 ungrouped papers; fires at paper-completion-state Patches touching SU); naming conventions; three paper-container kinds at programme level; future evolution patterns |
| [`series_substrate_chirality_arc/`](series_umbrella/series_substrate_chirality_arc/) | **Substrate-Chirality Arc (SSCA)** — first sub-umbrella established Patch 0571d. Groups three flagship papers organized under OPEN-SD-CHIR-PRIMITIVE umbrella problem (5 named observable manifestations of substrate's primitive chirality). Three of five manifestations closed: (i) K3-doublet mass-mixing via Capotauro v1.0 THEO-CAP-1; (ii) electroweak V−A coupling via Capotauro v2.0 + Chirality Continuum THEO-CHIR-CONT-2 substrate-level + Layer 4 EFT; (iv) thermodynamic causal arrow via F.1 THEO-DSL-3 at sketch-document Layer 3. Two open: (iii) electromagnetic-handedness; (v) cosmological-vacuum asymmetry — both F.2/F.3 candidate territory with no current closure-trajectory machinery |
| [`series_substrate_chirality_arc/README-SSCA.md`](series_umbrella/series_substrate_chirality_arc/README-SSCA.md) | SSCA arc-level overview (~100 lines): umbrella structure; three arc papers with v1.0 SHIP dates and closing theorems; closure status table; methodology cross-references (umbrella registration, ex ante joint-paper format, sketch-document L3 umbrella with publication-grade L3 building blocks, four-artifact hardened-theorem sequence); future-trajectory candidates |
| [`series_substrate_chirality_arc/manifestation_inventory.md`](series_umbrella/series_substrate_chirality_arc/manifestation_inventory.md) | Canonical OPEN-SD-CHIR-PRIMITIVE five-manifestation tracker (~120 lines) with per-manifestation closure status, closing paper, closing theorem, rigor level, and (for open manifestations iii + v) expected closure-trajectory machinery notes. Consolidates manifestation-tracking content previously split between `research_frontier.md` umbrella entry + `frontier_sectors/SD.md` + F.1 §9 in-body inventory |
| [`capotauro/`](series_umbrella/series_substrate_chirality_arc/capotauro/) | **Capotauro [v1.0 SHIPPED Session 122 Patch 0415 + v2.0 v1.0 SHIPPED Session 135 Patch 0479]** — Substrate-Vacuum Chirality on the K3-Doublet (v1.0) extended at v2.0 to Three-Way Cross-Sector Unification with FI-C-RC-1 + FI-C-RC-2 Substrate-Foundational Inputs. v1.0 closes OPEN-SM-4 sub-claim (c) via THEO-CAP-1 ($|M| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ on K3-doublet) within 2% of leptogenesis back-derived empirical anchor. v2.0 extends to three-way cross-sector unification $|M^{K3}| = |M^W| = |M^{qDP}| = \chi/6$ via THEO-CAP-1 + THEO-SD-CHIR-1 (W-bracelet) + THEO-SD-CHIR-2 (qDP/eDP); same magnitude through three structurally distinct mechanisms. **Third flagship paper to v1.0** after SS-9 / SF-4 / SF-2; **first flagship outside SF-N convention**; **first flagship to undergo substantive v2.0 extension** (vs polish/reviewer-feedback revision). Three-reviewer convergence on v2.0 v1.0 SHIP-acceptable achieved at v0.9 / v0.9.1 (Grok Patch 0476 + CoPilot Patch 0475 + ChatGPT round-2 revised Patch 0474) |
| [`capotauro/capotauro.tex`](series_umbrella/series_substrate_chirality_arc/capotauro/capotauro.tex) | **Capotauro v1.0 SHIPPED + v2.0 v1.0 SHIPPED (Session 135 Patch 0479)**: v2.0 source 97 pages PDF; 3 programme-level theorems at full Layer 3 rigor (THEO-CAP-1 K3-doublet + THEO-SD-CHIR-1 W-bracelet + THEO-SD-CHIR-2 qDP/eDP); 12 foundational inputs (FI-C-1 through FI-C-10 from v1.0 + FI-C-RC-1 primitive 4D direction $\hat{n}$ + FI-C-RC-2 vertex-aligned reading) + 4 CPP axioms (A1, A2, A4, A7); master programme-architecture Figure 1 at §3.5; §13.6 dynamical engine subsection registering Layer 1 dynamical-substrate-law work as explicitly open; 11-route falsifier set including 2 cross-sector substrate-handle predictions; new §15 Methods Catalogue Cross-Reference section listing 19 entries. **v1.0 SHIPPED state preserved historically**: 1149 lines source v1.0; 46 pages PDF v0.9 (v1.0 version-bump-only); 10 v1.0 foundational inputs; primitive-feature framing for FI-C-9 substrate chirality magnitude $|\chi| = \phi^{-3}$ adopted at v0.9 Patch 0413 per CPP core methodological principle that mathematical descriptions are not physical mechanisms |
| [`capotauro/sketches/`](series_umbrella/series_substrate_chirality_arc/capotauro/sketches/) | Capotauro staging + closure documents. Currently: `capotauro_outline.md` (327 lines, Session 104 Patch 0398), **`Capotauro_chi_phi_closure.md` (681 lines, parent sketch covering FI-C-9 + FI-C-10 closure trajectory Sessions 87-102)**, **`Capotauro_subclaim_c_wigner_eckart.md` (2146 lines, sub-claim (c) detailed eight-step closure with Theorem 18.1 + §22 v1.0 closure narrative)**, **`Capotauro_chiral_mechanism_candidate.md` (296 lines, Session 121 Patch 0414 Reading C geometric-chirality candidate for sub-claim (b) substrate chirality mechanism candidate derivation — primitive 4D direction $\hat{n}$ producing direction-correlated edge-length variation at $\phi^{-3}$ scale; Tier-4 Layer 1/Layer 2 epistemic status; Layer 3 closure trajectory tracked at OPEN-FI-C-9-FP-MECHANISM)** |
| [`capotauro/documentation_suite/`](series_umbrella/series_substrate_chirality_arc/capotauro/documentation_suite/) | Capotauro documentation suite at v2.0 v1.0 SHIPPED (Session 135 Patches 0481b + 0481d-0481j). 10-file companion suite all at v2.0 v1.0 SHIPPED status markers (Patch 0481b) + substantive v2.0 content (Patches 0481d-0481j): changelog-capotauro.md + development-capotauro.md (Tier-3 vignettes 36-40 for Session 135) + glossary-capotauro.md (12 new v2.0 terms) + keywords-capotauro.md (v2.0-era keyword set) + mechanism-capotauro.md (v2.0 cross-sector unification additions) + phenomena-capotauro.md (11-route falsifier set + 2 cross-sector substrate-handle predictions) + philosophy-capotauro.md (Layer 1 dynamical engine epistemology + constrained-closure-and-inheritance reframing) + reasoning-capotauro.md (Tier-4 verbatim reasoning §19-§23 for Session 135) + reviews-capotauro.md (Part 3 v2.0 review rounds — eight letters across seven review patches) + transcript-capotauro.md (per-patch transactions Patches 0466-0481e) |
| [`capotauro/reviews/`](series_umbrella/series_substrate_chirality_arc/capotauro/reviews/) | Capotauro review archive. 5 review files at v1.0 SHIP: `chatgpt_v0.6_session_113.md` (ChatGPT round-1) + `chatgpt_v0.7_session_117.md` (ChatGPT round-2) + `chatgpt_v0.8_session_119.md` (ChatGPT round-3 SHIP-ready verdict) + `copilot_v0.8_session_119.md` (CoPilot round-1 SHIP-ready verdict) + `grok_v0.8_session_119.md` (Grok round-1 SHIP-ready verdict) — cross-reviewer convergence on SHIP-readiness achieved at v0.8 Patch 0412 Session 119 |
| [`chirality_continuum/`](series_umbrella/series_substrate_chirality_arc/chirality_continuum/) | **Chirality Continuum [v1.0 SHIPPED Session 137 Patch 0509, 20 May 2026]** — Joint Layer 4 EFT Cross-Sector Closure of OPEN-FP-SF-2-CHIR (Electroweak V–A Coupling) and SM-2 v2.0+ (Quark Chiral-Polarity-Bias) from substrate handle $\|M\| = \chi/6$. Sixth flagship paper to v1.0 in the CPP corpus after SS-9 / SF-4 / SF-2 / Capotauro v1.0 / Capotauro v2.0; second flagship outside the SF-N numerical convention (joint-paper format under OPEN-SD-CHIR-PRIMITIVE umbrella; THEO-CHIR-CONT-N theorem-naming convention). Second Layer 4 cross-sector closure in CPP after SF-4 v4.0 (10 May 2026); first with ex ante joint-paper format adoption at viability decision gate (Patch 0484). **OSF deposit pending** under existing JXE8D DOI; public posting (Zenodo + arXiv) at Thomas's discretion. **First flagship paper in CPP programme history to achieve three-reviewer convergence on SHIP-acceptable verdict at first reviewer round each** (ChatGPT round-2 + Grok round-1 + CoPilot round-1; previous flagships required multi-round cycles) |
| [`chirality_continuum/chirality_continuum.tex`](series_umbrella/series_substrate_chirality_arc/chirality_continuum/chirality_continuum.tex) | **Chirality Continuum v1.0 SHIPPED (Session 137 Patch 0509)**: 1265 lines source; 38 pages 659 KB PDF compiled clean; 3 programme-level theorems THEO-CHIR-CONT-1 (Substrate-Handle-to-Effective-Coupling Bridge; sector-agnostic; theorem #65 SD section) + THEO-CHIR-CONT-2 (SF-2 W-bracelet V–A coupling Layer 4 EFT closure; theorem #66) + THEO-CHIR-CONT-3 (SM-2 qDP/eDP chiral-polarity-bias Layer 4 EFT closure; theorem #67); 4 programme-level methods catalogued METH-CHIR-CONT-1+2+3+4 (Sector-Agnostic Substrate Wigner-Eckart Datum + Continuum-Limit Projection Map $\Phi$ via Wilson-Fisher Block-Spin + Topological Substrate Quantity + Topological-Projection Argument); 15 foundational inputs FI-CHIR-CONT-1 through FI-CHIR-CONT-15 inherited from Capotauro v2.0 + SF-2 v1.0 + SM-2 v1.0; cross-sector convergence at observable scale §6.5 as structural prediction of joint-paper format (ChatGPT round-2 "proto-theoretical-architecture moment"); Capotauro Falsifier 6 three operative thresholds activated; OPEN-FP-SF-2-CHIR LAYER 4 CLOSURE COMPLETE via THEO-CHIR-CONT-2; SM-2 v2.0+ chiral-polarity-bias EFT continuum-limit JOINTLY CLOSED via THEO-CHIR-CONT-3 |
| [`chirality_continuum/documentation_suite/`](series_umbrella/series_substrate_chirality_arc/chirality_continuum/documentation_suite/) | Chirality continuum 8-file documentation suite at v1.0 SHIP (Session 137 Patch 0511; flat layout per established companion-suite convention): changelog-chirality_continuum.md (full version archaeology Patches 0482–0509) + development-chirality_continuum.md (Tier-3 vignettes capturing 28-patch closure trajectory) + glossary-chirality_continuum.md (13 chirality continuum terms) + keywords-chirality_continuum.md (search-engine-discoverability keyword set) + mechanism-chirality_continuum.md (substrate-handle-to-effective-coupling bridge mechanism narrative) + phenomena-chirality_continuum.md (Capotauro Falsifier 6 three operative thresholds + cross-sector convergence at observable scale falsifier framing) + philosophy-chirality_continuum.md (topological-projection argument as standard-QFT-grade closure technique + joint-paper format as cross-framework methodology) + reviews-chirality_continuum.md (three-reviewer convergence at first reviewer round each — first in CPP programme history) |
| [`chirality_continuum/code/`](series_umbrella/series_substrate_chirality_arc/chirality_continuum/code/) | Chirality continuum verification notebook suite (Session 137 Patch 0515; Python stdlib only). Five standalone notebooks numerically validate paper claims at Section B of `templates/paper_completion_checklist.md` verification points B1–B5: `B1_verify_chi6_substrate_handle.py` ($\chi/6 = \phi^{-3}/6 \approx 0.0394$ + BAU back-derivation comparison + Falsifier 6 (C) check) + `B2_verify_michel_rho_va.py` (Michel $\rho = 3/4$ via V-A four-fermion kinematics + 1-loop QED + PDG 2024 + Falsifier 6 (A) check) + `B3_verify_chirality_helicity_coincidence.py` ($P_L^{\text{helicity}}(v) = (1+v)/2 \to 100\%$ LH at massless limit + multi-particle scales + Falsifier 6 (B) check) + `B4_verify_cross_sector_convergence.py` (single primary observable Δp_LR via two channels converge within $O((\chi/6)^3) \sim 6 \times 10^{-5}$) + `B5_verify_capotauro_falsifier_6.py` (three-threshold cascade test with current experimental data + future-collider projections). All five report PASS under current data; README.md indexes the suite |
| [`chirality_continuum/chirality_continuum_outline.md`](series_umbrella/series_substrate_chirality_arc/chirality_continuum/chirality_continuum_outline.md) | Chirality continuum v0.1 outline document (Session 137 Patches 0482–0484): section-by-section structure, foundational inputs registration, viability decision gate analysis (joint-paper format vs separate single-sector papers), drafting plan. Patch 0484 viability decision: PROCEED with joint-paper format; saves estimated 4–11 sessions across §A + §B + §C trajectory vs Venue (b) fallback |
| [`dynamical_substrate_law/`](series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/) | **F.1 [v1.0 SHIPPED Session 142 Patch 0570, 24 May 2026]** — The Dynamical Substrate Law: Substrate-Locality of DI-Bit Currents at Vertex-Aligned Reading C in the 600-Cell. **First F-line flagship v1.0 SHIP in CPP corpus** (seventh flagship paper to v1.0 overall after SS-9 / SF-4 / SF-2 / Capotauro v1.0 / Capotauro v2.0 / Chirality Continuum; third flagship outside the SF-N numerical convention). Closes OPEN-SD-CHIR-PRIMITIVE manifestation (iv) thermodynamic causal arrow at **sketch-document Layer 3** via Theorem 7.1 substrate-locality umbrella with closed-form first-order DI-bit current $\vec{j}_{DI}^{\text{net}}(\vhost) = (6\delta/\phi^2)\,\hat{n} + \mathcal{O}(\delta^2)$. Three publication-grade Layer 3 trio inputs (Theorems 5.1 + 5.2 + 6.1 + Corollary 6.2); five Open Problems registered (OPEN-FP-F1-1 through OPEN-FP-F1-5) + OPEN-FP-F1-6 prose-density tightening registered separately at Patch 0569e from R6 follow-up. Three-reviewer convergence at v1.0 SHIP: Grok R1 EXPLICIT v1.0 SHIP-acceptable + Copilot R1 implicit SHIP-acceptable with tier-ranked recommendations + ChatGPT R1→R6 monotonic improvement to strongest-positive verdict ("substantially more credible, rigorous, and publishable than all earlier versions"); R6 diagnostic resolution identified TikZ-rendering processing artifact resolved via PDF upload protocol. Three programme-level conventions extended at this SHIP: Variant (b) `\date{}` line scope-subtitle pattern; PDF-upload-default reviewer engagement protocol; `.gitignore` exception pattern for flagship paper SHIP PDFs |
| [`dynamical_substrate_law/dynamical_substrate_law.tex`](series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/dynamical_substrate_law.tex) | **F.1 v1.0 SHIPPED (Session 142 Patch 0570)**: 1240 lines source; ten sections including §5 first-shell geometric identities (Theorems 5.1 + 5.2 + Lemma 5.2.1 + Capotauro v2.0 §3 spatial-sector parallel cross-reference) + §6 perturbation-theory propagation rule (Lemmas 6.1.1 + 6.2.1 + 6.3.1 + Theorem 6.1 + Corollary 6.2 + five-class exclusion enumeration) + §7 substrate-locality umbrella theorem (Theorem 7.1 sketch-document Layer 3 with three-step assembly at §7.3) + §8 Layer 3 stack with Figure 8.1 TikZ dependency-graph + §9 five Open Problems + §10 conclusion with anti-erasure discipline operationalised at three concrete points |
| [`dynamical_substrate_law/dynamical_substrate_law.pdf`](series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/dynamical_substrate_law.pdf) | **F.1 v1.0 SHIPPED compiled PDF (Session 142 Patch 0570)**: 33 pages, 489 KB, MD5 `49e56be92a3ccc126ce09210b5898794`; first flagship paper PDF committed deliberately at v1.0 SHIP per the `.gitignore` exception pattern `!flagship_papers/*/*.pdf` adopted at Patch 0570 apply-fix |
| [`dynamical_substrate_law/documentation_suite/`](series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/documentation_suite/) | F.1 documentation suite at v1.0 SHIPPED (Phase 7A doc-suite production sub-arc Patches 0572 + 0572a–g, Session 143 24 May 2026). 10-file suite: **7 SHIP-time companion files** — `changelog-dynamical-substrate-law.md` (canonical version archaeology per docsuite.md §11) + `keywords-dynamical-substrate-law.md` (Primary + Secondary + Cross-paper-reference + Discovery-aid Keywords + PACS/MSC/arXiv codes + Elevator Pitch + SEO Notes + Registry Entries) + `reviews-dynamical-substrate-law.md` (Part 1 Formal reviews across the 6-round ChatGPT cycle + Copilot R1 + Grok R1 + Part 2 FAQ 13 entries across Methodology + Scope + Falsifiability + SM Relationship + Future Work) + `mechanism-dynamical-substrate-law.md` (8-step physical mechanism narrative + mathematical-correspondence table 12 entries + failure-modes 6 entries + cross-paper consistency) + `glossary-dynamical-substrate-law.md` (~46 entries across Constants + Structural + Mechanism + Methodology + Status Labels) + `phenomena-dynamical-substrate-law.md` (PHEN-E + PHEN-P 8 zero-parameter structural predictions + PHEN-V 4 consilience + PHEN-F 10-falsifier inventory + PHEN-O out-of-scope + PHEN-X cross-sector consistency + structural-consistency-driven swarm-validation contribution) + `philosophy-dynamical-substrate-law.md` (paper-type declaration clause-by-clause analysis + Layer classification table + certainty levels + 10-falsifier threshold table + Honest assessment IS/IS-NOT/Weakest-link triad + methodological observations consolidating anti-erasure + calibration + diagnostic resolution + reviewer-pause cycle + 5 programme-level convention candidates) + **3 Tier files** — `transcript-dynamical-substrate-law.md` (Tier 2 transaction pointer-map; Transactions 001–072) + `development-dynamical-substrate-law.md` (Tier 3 vignette-style narrative; Vignettes 01–55) + `reasoning-dynamical-substrate-law.md` (Tier 4 verbatim Opus reasoning; §§01–67) |
| [`dynamical_substrate_law/code/`](series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/code/) | F.1 verification scripts (Python stdlib + NumPy only) + INDEX.md doubling as B1–B5 verification notebooks audit document (Patch 0572g). Five scripts: `verify_phase1.py` (Net DI-bit current at host vertex; 4 identities verified including substrate-locality umbrella closed-form result $\vec{j}_{DI}^{\text{net}} = (6\delta/\phi^2)\hat{n}$; B3 directly executed at audit time — PASS) + `verify_b1q2_curl_content.py` (B.1.q2 discrete curl vanishing at host vertex via 30 host-first-shell side-face trapezoidal circulations; the K3-base protection identity Capotauro shares) + `verify_b1q4_first_shell_current_sum.py` (B.1.q4 first-shell-vertex current magnitude $2 r_0 \delta \sqrt{7-\phi}$ uniform + sum $24/\sqrt{7-\phi}$) + `verify_phase3.py` + `verify_phase4.py` (foundations-work artifacts; thermodynamic-arrow emergence beyond paper-body scope per §10 explicit disclaimer) |
| [`dynamical_substrate_law/hardened_theorems/`](series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/hardened_theorems/) | F.1 publication-grade Layer 3 hardened-theorem trio supplying §5 + §6 body content as direct integration inputs. Three artifacts at 741 lines LaTeX combined: `perturbation_locality.tex` (Patch 0550; underpinning §6) + `first_shell_perpendicularity.tex` (Patch 0551; underpinning §5.4 Theorem 5.2) + `host_first_shell_projection.tex` (Patch 0552; underpinning §5.3 Theorem 5.1). Each with explicit hypothesis tracking + five-class exclusion enumeration. The hardened-theorems trio convention is corpus-establishing for F-line flagship trajectories |
| [`dynamical_substrate_law/reviews/`](series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/reviews/) | F.1 review archive. 9 review letters at v1.0 SHIP archived across Patches 0568–0569e: `copilot_v0.9_session_142.md` (Copilot R1 implicit SHIP-acceptable with Tier 1/2/3 ranked recommendations) + `grok_v0.9_session_142.md` (Grok R1 explicit v1.0 SHIP-acceptable + 4 minor polish items) + `chatgpt_v0.9_session_142.md` (ChatGPT R1 strong pre-v1.0 internal flagship draft with 2 hardening steps pending) + `chatgpt_v0.9v2_session_142.md` (ChatGPT R2 substantial improvement) + `chatgpt_v0.9v3_session_142.md` (ChatGPT R3 credible flagship framework theorem paper) + `chatgpt_v0.9v4_session_142.md` (ChatGPT R4 recurring R3 recommendations diagnostic-framing) + `chatgpt_v0.9v4_session_142_round5.md` (ChatGPT R5 recurring-pattern documentation) + `chatgpt_v0.9v5_session_142_round6.md` (ChatGPT R6 strongest-positive verdict + diagnostic resolution TikZ-rendering processing artifact confirmed via PDF upload + 2 new follow-up items) + `synthesis_v0.9_to_v1.0_session_142.md` (Round 1 synthesis with 12-item classification: 1 MUST-ADDRESS + 4 SHOULD-ADDRESS + 5 CAN-DEFER + 2 DECLINED) |
| [`dynamical_substrate_law/reviewer_pause/`](series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/reviewer_pause/) | F.1 reviewer-pause cycle artifacts (canonical worked example for `templates/operating_system.md` §17 + `templates/paper_completion_checklist.md` Reviewer-Pause Cycle Precondition for Flagship-Paper-Trajectory Work added Patch 0539a). 4 artifacts: Phase 2 foundations work + Layer 3 promotion checkpoints + feedback records covering Patches 0531–0537 (Phase 2 closure) → 0538 (calibration response) → 0539 (status upgrade) → 0540–0546 (Layer 3 promotion). Reference example for future F-line flagship trajectories (F.2, F.3, …) |
| [`dynamical_substrate_law/sketches/`](series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/) | F.1 working sketches (Tier-4 reasoning capture). 4 sketches: `F1_phase2_foundations_work.md` (Phase 2 sub-question closure load-bearing arc) + `F1_subquestion_pcd_orientation_link.md` (sub-question scoping sketch) + `F1_layer3_promotion_scoping.md` (Layer 3 promotion work scoping) + `F1_flagship_paper_assembly_scoping.md` (paper-assembly trajectory scoping immediately preceding Patch 0554 skeleton) |
| [`dynamical_substrate_law/layer3_promotion/`](series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/layer3_promotion/) | F.1 Layer 3 promotion arc artifacts captured during the closure trajectory prior to flagship paper assembly. 5 sub-question files: `F1_layer3_b1d_substrate_locality_temporal_extension.md` (B.1.d substrate-locality temporal extension) + `F1_layer3_b1q1_matter_state_independent_derivation.md` (B.1.q1 matter-state-independent derivation) + `F1_layer3_b1q2_full_4d_curl_schur_decomposition.md` (B.1.q2 full 4D curl via Schur decomposition on the 30 host-first-shell side-face 2-form basis) + `F1_layer3_b1q3_perturbation_theory_propagation.md` (B.1.q3 perturbation-theory propagation rule precursor to Theorem 6.1) + `F1_layer3_b1q4_algebraic_derivation.md` (B.1.q4 first-shell-vertex current sum identity foundations work). Tier-4 reasoning preservation for the Layer 3 promotion arc; reference example for future F-line flagship trajectories following the reviewer-pause cycle methodology |
| [`dynamical_substrate_law/development-transcripts/`](series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/development-transcripts/) | F.1 curated transcripts directory (created Patch 0572i, Session 143 Phase 7A FINAL item; closes Phase 7A doc-suite production sub-arc). Currently holds `F1_transcript_session_143_phase_7a_opus.md` (curated Phase 7A doc-suite production transcript covering Patches 0572 → 0572a–0572i) + `README.md` index. The curated-transcripts subfolder convention extends the per-paper subfolder discipline beyond the documentation_suite four-tier structure with venue-specific transcript curation for cross-session readability |
| [`dynamical_substrate_law/phase_7B_content_pack.md`](series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/phase_7B_content_pack.md) | F.1 Phase 7B execution scaffolding (Patch 0573, Session 143; ~460 lines). Pre-stages all 11 programme-level registry insertion blocks with anti-collision anchors + sanity checks + per-registry Landing status tracking (`PENDING` → `LANDED at Patch 05NN` flipped per Phase 7B patch). Enables lightweight-bootup-mode for Phase 7B sessions (Patches 0574–0584+) per `bootup.md` §3.5; subsequent sessions read content pack + ONE target registry rather than full priority-read + paper + doc suite. Same-session register-and-resolve resolution of OPEN-ORG-020 Phase 7B context-overflow failure mode (third such pattern in CPP corpus history after OPEN-ORG-013/014/008). Lifecycle: retired or archived after Phase 7C closes (post-OSF deposit). Reference implementation templates content pack creation for future flagship paper v1.0 SHIP Phase 7B transitions |

---

## [`series_strong/`](series_strong/) — Strong Sector (SS)

The SU(3) derivation from 600-cell tetrahedral geometry, uniqueness proof, nucleon structure, string tension, deuteron binding, deuteron observables scoping, alpha-cluster regime, and interstitial-neutron 2E/V scaling. **SS-1 registered on OSF. SS-2, SS-3, SS-4, SS-5, SS-6, SS-8 pending. SS-7 has existing OSF DOI from v0.1; v1.2 update pending.**

| File | Description |
|------|-------------|
| `SS-1_strong_sector_from_600cell_lattice.tex/.pdf` | **SS-1** (v2) — 9 theorems |
| `papers/SS-1f_su3_hop_realization.tex` | **SS-1f** (v1.0) — SU(3) hop realisation: colour = baryon-tetrahedron vertex occupancy, gluon = a charge-driven ZBW/SSV vertex hop (Prop 6.1 torus result); SU(3)-foundations companion |
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
| `papers/SR-2_spin_bit_axiom_quadrupole_formula.tex` | **SR-2** — spin-bit axiom (A3′) / derived Einstein quadrupole formula; closes op:einstein (a) (v1.0 SHIPPED) |
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

## [`series_phenomena/`](series_phenomena/) — Empirical Phenomena Explained from CPP Axioms

**Established 31 May 2026 (Patch 0700).** Home of record for any empirical phenomenon CPP derives, at any maturity (sketch → gated conjecture → shipped). Phenomena mature in place; not migrated on completion. See [`series_phenomena/README.md`](series_phenomena/README.md) for the three-container boundary rule.

### [`series_phenomena/cosmology/early_universe/`](series_phenomena/cosmology/early_universe/) — EU-1 (SHIPPED v1.0)

| File | Description |
|------|-------------|
| `EU-1/EU-1_primordial_spectral_index.tex` | **EU-1** — primordial scalar spectral index $n_s = 1 - 2/N_* \approx 0.9649$ from substrate inflation (A1 indistinguishability → ZBW-bath ZRP → $\delta N$ tilt); zero-new-axiom, framework-conditional. First cosmology-sector paper to ship. |
| `EU-1/documentation_suite/changelog-EU-1.md` | Version archaeology (v0.1 → v1.0). |
| `EU-1/review/` | Self-contained review package + `reviews-EU-1.md` (3/3 SHIP). |
| `scripts/0781_eu1_numerics.py` | Verification (ALL PASS). |
| `reasoning/0781…`, `0783…` | Per-patch Tier-4 reasoning fragments. |

**Predictions:** PRED-C-96 ($n_s$, §1), PRED-O-34 ($\alpha_s$, §2). **No THEO.** Open residual: OPEN-EU-1.
**Doc-suite:** full suite shipped (Patch 0789) — changelog + development + reviews + keywords + transcript + mechanism + phenomena + philosophy + glossary + verification + osf-deposit. OSF upload pending (metadata prepared).

### [`series_phenomena/cosmology/dark_matter/`](series_phenomena/cosmology/dark_matter/) — gated conjecture

Far-frontier dark-matter arc (qDP/hTetra-clouds-as-DM, CONJ-COSMO-1); `reasoning/` + `scripts/` only, pre-paper (falsification-first). Frontier home: `frontier_sectors/CONJ.md`.

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

**Master dashboard:** See [`research_frontier.md`](research_frontier.md) for the complete register (84 entries across all sectors).

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
