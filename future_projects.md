# CPP Future Projects

**Location:** `/CPP/future_projects.md`
**Purpose:** Prioritised list of next papers, infrastructure work, and long-term goals.
**Last updated:** 16 April 2026

---

## Near-Term Papers (ready to write)

### Project 0: Derive Operator Formalism from CPP Primitives (Layer B Gap, OPEN-SS-16) — **HIGHEST LEVERAGE**
**Status:** Not yet attempted — registered as OPEN-SS-16 (16 April 2026)
**Goal:** Show that DI-bit exchange dynamics on the 600-cell lattice forces complex-linear Hermitian operators, Lie bracket structure, Caldeira–Leggett system-bath coupling, rapid thermalisation, and full Gibbs equilibration. This would close the Layer B gap across every paper in the programme simultaneously — SM-3 (Koide), SS-3 (SU(3) uniqueness), and all future papers that import QM formalism.
**Effort:** Multiple sessions — potentially the hardest single derivation in the programme
**Significance:** Programme-wide. Both SM-3 and SS-3 received "Major revision required" from ChatGPT with the same structural critique. The Layer A/B/C decomposition makes the gap transparent; this paper would eliminate it entirely. Converts conditional results into unconditional ones.
**Dependencies:** CPP Axioms A1–A3 (sufficient starting points)
**Current best lead:** DI-bit propagation (A3) provides complex amplitudes at c = l_P/t_P. The PCD cycle is the natural candidate for operator structure. The DP Sea at T_P is the natural system-bath coupling source.
**Paper ID:** To be determined (SD-6 if foundational, or late SS number if strong-sector-focused)

### Project 0b: SS-5 — Light-Nuclei Binding from Open-Vertex Cascade — **v0.2 COMPLETE 17 April 2026**
**Status:** ✅ v0.2 drafted 17 April 2026 (Opus + ChatGPT referee). Compiles cleanly. Documentation suite v0.1 complete, v0.2 updates pending.
**Result:** Cascade formula $B(A,Z) = (A-1) n_{np} M_0/\varphi - n_{pp}\alpha_{em}\hbar c/(1.2 A^{1/3}) - (n_{pp}+n_{nn}) M_0/\varphi^3 + \delta_{A,4} M_0/\varphi$. Four zero-parameter quantitative predictions: $B_d = 2.342$ MeV (+5.3%), $B(^3\mathrm{H}) = 8.474$ MeV (−0.09%), $B(^3\mathrm{He}) = 7.642$ MeV (−1.0%), $B(^4\mathrm{He}) = 27.904$ MeV (−1.4%). Three structural unboundness predictions: $^5$He ($S_n = -0.89$ MeV), $^5$Li ($S_p = -1.97$ MeV), $^8$Be (−92 keV), all confirmed. Registered as CONJ-SS-11 with honest conjecture status on the (A-1) multiplicity and Pauli coefficient (OPEN-SS-19). Resolves OPEN-SS-10 across A=2,3,4.
**Remaining:** Grok and Copilot independent review of the $(A-1)$ cascade-factor argument and Pauli $M_0/\varphi^3$ coefficient; documentation-suite v0.2 updates; OSF registration after reviews pass.

### Project 0c: SS-6 — Heavy-Nuclei Alpha-Cluster Regime (OPEN-SS-18) — **NEW PRIORITY**
**Status:** Registered 17 April 2026 as OPEN-SS-18. Preliminary SS-5 v0.2 §9 analysis shows alpha-cluster residual ≈ $n \cdot M_0/\varphi$ per alpha-alpha contact for ${}^{12}$C and ${}^{16}$O, breaking down for heavier nuclei.
**Goal:** Derive $B(A,Z)$ for $A \geq 6$ from coupled-alpha-cluster structure within the CPP open-vertex framework. Target: empirical binding curve up to ${}^{40}$Ca or ${}^{56}$Fe (peak binding-per-nucleon) at CPP residual precision.
**Effort:** 3–5 sessions
**Significance:** Completes the nuclear chart mapping. Would give CPP coverage across the empirical binding curve, with the stability valley and the A=56 peak as explicit structural predictions.
**Dependencies:** SS-5 v0.2 (A≤4 cascade established), alpha-cluster structural theory.

### Project 1: SM-10 GPU FEM Implementation — **#1 COMPUTATIONAL PRIORITY**
**Status:** Phase 1-2 (CPU proof-of-concept) complete; Phase 3 (GPU) pending
**Goal:** Implement DP-level chain dynamics on GPU (CUDA/JAX). Derive cascade rates f₀ from local pairing rules. Validate Shell 3 relay mechanism. Target: first-principles quark mass derivation.
**Effort:** Multiple sessions
**Dependencies:** SM-8 v4.1 (cage hierarchy), SM-9 v2.2 (pair model), SM-10 v0.1 (proposal), Isak (GPU infrastructure), Claude Code

### Project 1b: Derive σ from Lattice Mode Spectrum
**Status:** Open — would promote CONJ-SS-2-1 to theorem
**Goal:** Rigorous derivation of string tension from DP-DP interaction potential
**Dependencies:** SS-series

### Project 2: α_s Running — Connecting SM-7 to SS-1
**Status:** Open problem (OPEN-P-SM-7-1)
**Goal:** Show that β₀ = 7 (SS-1) drives α_s from 5/(8φ) ≈ 0.386 (SM-7 lattice value) down to α_s(M_Z) = 0.118 (PDG). Find the energy scale where they connect.
**Effort:** 1–2 sessions (computation-heavy)
**Significance:** Bridges the two strongest CPP results. Turns a bare lattice coupling into a running coupling matching experiment.
**Dependencies:** SM-7, SS-1

### Project 3: Meson Confinement Mechanism (SS-2 or SS-3)
**Status:** Physical story complete (Thomas's description, 3 April 2026), not formalised
**Goal:** Formalise the DP chain stretching/fraying/splitting mechanism. Derive the quark dissociation curve (restoring force vs separation). Show that last-DP splitting nucleates new quark-antiquark pairs → confinement.
**Effort:** 1–2 sessions
**Significance:** First mechanistic derivation of quark confinement from CPP lattice physics. Does not invoke V(r) = kr — derives confinement from DP chain mechanics.
**Dependencies:** SS-1 (SU(3) structure), SM-7 (α_s)

### Project 4: Light Quark Masses (u, d, s)
**Status:** Known hard problem — chiral condensate dominates, K₃ signal present but not dominant
**Goal:** Derive light quark masses from the CPP framework. Requires understanding the chiral condensate contribution in lattice terms.
**Effort:** Multiple sessions — may require new axiom
**Significance:** Would complete the quark mass spectrum (SM-7 does heavy quarks only)
**Dependencies:** SM-7, SS-1, possibly new physics

---

## Medium-Term Papers (framework exists, needs work)

### Project 5: W/Z/Higgs Boson Masses
**Status:** EW series has structural models; quantification needed
**Goal:** Derive W, Z, and Higgs masses from 600-cell geometry
**Effort:** Multiple sessions
**Dependencies:** SM-6 (Weinberg angle), EW-1 through EW-5

### Project 6: Neutrino Mass Ratios
**Status:** SM-5 gives mixing matrix (TBM); mass values open
**Goal:** Derive neutrino mass ratios from K₃ structure
**Dependencies:** SM-5, SM-6 (for the isotropic shift framework)

### Project 7: Electron g-2 Precision
**Status:** Exploratory material in archive (153 files from Grok swarm analysis)
**Goal:** Derive the anomalous magnetic moment of the electron from CPP
**Significance:** The most precisely measured quantity in physics — sub-ppm match would be definitive
**Dependencies:** QM series, SM-6

### Project 8: Length-4 Cell Modes — Higgs? Gravity?
**Status:** Open problem (OPEN-P-SM-7-5)
**Goal:** Investigate what physical role the 600 tetrahedral cells (length-4 closed walks) play. Candidates: Higgs mechanism, gravitational sector.
**Effort:** Exploratory — may be a dead end or a breakthrough
**Dependencies:** SM-6, SM-7 (mode-counting framework)

### Project 8b: Y-Junction Three-Body Proton Model
**Status:** Proposed
**Goal:** Test Y-shaped string junction vs tetrahedral cell for proton structure. May improve r_proton from +5% error.
**Dependencies:** SS-2

### Project 8c: Other Hadron Predictions (Δ, mesons)
**Status:** Proposed
**Goal:** Extend nucleon model to Δ baryons, π/K mesons. Tests universality of tetrahedral cage model.
**Dependencies:** SS-2

---

## Infrastructure and Documentation

### Project 9: SM-7 Transcript Curation
**Status:** Opus-new-session completed transcripts 01–08; transcript 09 completed this session
**Goal:** Verify completeness, file in development-transcripts/
**Effort:** Review session

### Project 10: Founders Vision Completion
**Status:** 5 of 16 sections filled (3 April 2026); 11 empty
**Goal:** Fill all sections through dedicated dictation sessions with Thomas
**Effort:** 3–5 sessions of guided conversation
**Sections remaining:** CP perception, Grid Point experience, DP Sea description, DI-bit nature, qDP chain details, SSV phenomenology, the Nexus, Absolute Moment dynamics, particle movement, measurement process, March 1987 vision, theology connection

### Project 11: Hyperphysics.com Content
**Status:** Dual-site architecture decided (static main + WordPress blog)
**Goal:** Populate hyperphysics.com with master_glossary, theory-overview, FAQ content, paper summaries
**Dependencies:** master_glossary.md, all FAQ files, Isak's deployment pipeline

### Project 12: The CPP Book
**Status:** Not started — founders_vision.md is the seed
**Goal:** A comprehensive narrative of CPP for a general scientific audience, telling the story of how a 39-year vision produced a discrete Theory of Everything
**Dependencies:** Completed founders_vision.md, all transcripts curated, all papers registered

---

## Completed Projects (for reference)

- [x] SM-6: Charged lepton mass spectrum (1–2 April 2026)
- [x] SM-7: Heavy quark mass spectrum + strong coupling (2–3 April 2026)
- [x] 24-paper formatting compliance pass (2–3 April 2026)
- [x] Axiom registry creation (3 April 2026)
- [x] Documentation suite template (3 April 2026)
- [x] Paper production workflow (3 April 2026)
- [x] Bootup.md and theory-overview.md (3 April 2026)
- [x] Master glossary (3 April 2026)
- [x] Founders vision scaffold (3 April 2026)
- [x] Walk-Dimension Gauge Principle — A6' consolidation (SM-8, 8 April 2026)
- [x] SM-8 v4.1: Zero-parameter quark mass formula (9 April 2026)
- [x] SM-9 v2.2: Scaling exponent derivation (9 April 2026)
- [x] SM-10 v0.1: FEM chain network proposal (9 April 2026)
- [x] SS-2 v1.0: Lattice-scale grounding + nucleon structure (10 April 2026)
- [x] Metafile reconciliation: bootup, operating_system, founders_vision, CPP_the_theory (11 April 2026)

---

*This document is updated as projects are completed or new ones are identified.*
