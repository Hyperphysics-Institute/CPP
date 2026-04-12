# CPP Future Projects

**Location:** `/CPP/future_projects.md`
**Purpose:** Prioritised list of next papers, infrastructure work, and long-term goals.
**Last updated:** 11 April 2026

---

## Near-Term Papers (ready to write)

### Project 1: SM-10 GPU FEM Implementation — **#1 PRIORITY**
**Status:** Phase 1-2 (CPU proof-of-concept) complete; Phase 3 (GPU) pending
**Goal:** Implement DP-level chain dynamics on GPU (CUDA/JAX). Derive cascade rates f₀ from local pairing rules. Validate Shell 3 relay mechanism. Target: first-principles quark mass derivation.
**Effort:** Multiple sessions
**Dependencies:** SM-8 v4.1 (cage hierarchy), SM-9 v2.2 (pair model), SM-10 v0.1 (proposal), Isak (GPU infrastructure), Claude Code

### Project 1b: SM-12 — Deuteron Binding from Open-Vertex Model
**Status:** Proposed — uses SS-2 proton/neutron structures
**Goal:** Predict deuteron binding energy from open-vertex nuclear force mechanism
**Dependencies:** SS-2

### Project 1c: Derive σ from Lattice Mode Spectrum
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
