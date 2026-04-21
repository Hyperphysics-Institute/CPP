# CPP Future Projects

**Location:** `/CPP/future_projects.md`
**Purpose:** Prioritised list of next papers, infrastructure work, and long-term goals.
**Last updated:** 21 April 2026 (SS-7 v1.2 completed and reclassified; SS-8 retargeted to OPEN-SS-23 as new NEXT PRIORITY; OPEN-SS-24 and OPEN-SS-25 registered)

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

### Project 0b: SS-5 — Light-Nuclei Binding from Open-Vertex Cascade — **v6 POLISH COMPLETE 18 April 2026**
**Status:** ✅ v6 published-ready 18 April 2026 (Opus + ChatGPT + Copilot reviewers, independent Opus v4 stress-test completed). Compiles cleanly at 19 pages; all 15 bibliography entries cited inline. Documentation suite at v6 header currency (7 files); development transcript created (`SS-5_development_transcript.md`, 259 lines).
**Result:** Cascade formula $B(A,Z) = (A-1) n_{np} M_0/\varphi - n_{pp}\alpha_{em}\hbar c/(1.2 A^{1/3}) - (n_{pp}+n_{nn}) M_0/\varphi^3 + \delta_{A,4} M_0/\varphi$. Four zero-parameter quantitative predictions: $B_d = 2.342$ MeV (+5.3%), $B(^3\mathrm{H}) = 8.474$ MeV (−0.09%), $B(^3\mathrm{He}) = 7.642$ MeV (−1.0%), $B(^4\mathrm{He}) = 27.904$ MeV (−1.4%). Three structural unboundness predictions: $^5$He ($S_n = -0.89$ MeV), $^5$Li ($S_p = -1.97$ MeV), $^8$Be (−92 keV), all confirmed. Registered as CONJ-SS-11 with honest conjecture status on the (A-1) multiplicity and Pauli coefficient (OPEN-SS-19). Resolves OPEN-SS-10 across A=2,3,4. v5→v6 added four Copilot "Remark X" inserts + ChatGPT A=3 stress-test sentence; all inline citations added; Rod Nave fabricated-dedication error caught and corrected.
**Remaining:** Grok numerical verification of v6; Sonnet hostile-reviewer pass; reviews-SS-5.md Parts 3 (v4 stress-test) and 4 (Copilot review) bodies to be appended; OSF registration after review cycle completes.

### Project 0c: SS-6 — Deuteron Observables Beyond Binding (Scoping) — **v0.1 COMPLETE 18 April 2026**
**Status:** ✅ v0.1 scoping draft complete 18 April 2026. 12 pages, clean compile, all 10 references cited inline. Companion documentation suite pending (7 files).
**Result:** Three-category classification of deuteron observables by CPP derivability. Category A (bipyramid-geometric): binding, J^P, I — all derived in SS-5. Category B (bipyramid-via-$V_{SR}$): $a_{np}$, $r_0$, singlet virtual state — require OPEN-SS-20. Category C (orbital-dominated): $Q_d$, $r_d$, $P_D$, $\mu_d$ — require OPEN-SS-21. Key finding: rigid-bipyramid intrinsic $Q_d^{\mathrm{int}} = -0.22$ fm$^2$ (oblate) has wrong sign vs observed $+0.286$ fm$^2$ (prolate) — reveals $Q_d$ is orbital-dominated, not bipyramid-dominated. Zero-range Bethe-Peierls gives $a_{np} = 1/\kappa = 4.32$ fm from $B_d$ alone ($-20\%$ vs observed 5.425 fm). Registers OPEN-SS-20 ($V_{SR}(r)$ shape), OPEN-SS-21 (orbital wavefunction), PROP-SS-6-1 ($Q_d$ orbital-dominated), PROP-SS-6-2 (zero-range $a_{np}$).
**Remaining:** Companion documentation suite (mechanism, phenomena, glossary, keywords, philosophy, development, reviews); Grok/Copilot/Sonnet review; OSF registration.
**Significance:** Sharpens SS-5's claims by classifying what the bipyramid does and does not predict. Honest scoping rather than attempting additional bipyramid-based derivations where the orbital regime dominates.

### Project 0d: SS-7 — Alpha-Cluster Regime and 3N−6 Edge Formula — **v1.2 COMPLETE 21 April 2026**
**Status:** ✅ v1.2 published-ready 21 April 2026 (Opus + ChatGPT + Copilot + Grok reviewers, symmetric-honesty correction cycle completed in 24 hours). 25 pages; clean compile; documentation suite at v1.2 header currency (7 files); PH-OPEN-SS-22.md retirement narrative written.
**Result:** Zero-parameter formula $B(N_\alpha) = N_\alpha B_\alpha + (3N_\alpha - 6) B_\text{pair}$ with $B_\alpha = 28.296$ MeV and $B_\text{pair} = M_0/\varphi = 2.342$ MeV, both from SS-5. Twelve concurrent zero-parameter predictions across strict $N{=}Z$ alpha-chain nuclei at $N_\alpha \in [3, 14]$ (${}^{12}$C through ${}^{56}$Ni) all within ±1.5%, RMS 0.80%. Widest deviation ${}^{20}$Ne at +1.19%. ⁸Be near-threshold unbound derived in-formula via single-edge Coulomb cancellation; inversion gives $R_{\alpha\alpha} = 2.37$ fm (consistency parameter, not forward prediction). Theorem 2.1 registered as THEO-SS-12 (simplicial polytope edge count = $3N_\alpha - 6$ from Euler's formula). Partially resolves OPEN-SS-18. Hostile-geometry stress test (ChatGPT re-review contribution) establishes edge-count dominance: simplicial rule outperforms lower-edge alternatives in all five tested cases at single-$B_\text{pair}$ sensitivity.
**OPEN-SS-22 retirement (first in CPP programme record):** v1.1's empirical anchor (−2% residual plateau at $N_\alpha = 12, 13, 14$) was an isotope-selection artifact — v1.1 used non-$N{=}Z$ isotopes (${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe, each $N-Z=+4$); strict $N{=}Z$ counterparts (${}^{48}$Cr, ${}^{52}$Fe, ${}^{56}$Ni) show no plateau. Three-reviewer convergence (ChatGPT, Copilot, Grok with Benjamin/Lucas/Harper) on "isotope-selection artifact, retirement correct." Physics content split: DP-sea Coulomb screening → new OPEN-SS-25; neutron-excess empirical signal (~2 MeV/neutron) absorbed into existing OPEN-SS-23; structural-onset hypothesis itself retired, no replacement needed.
**Registry cascade completed:** theory-overview.md, axiom-registry.md (if applicable), theorem-registry.md (THEO-SS-12), master_glossary.md (SS-7 v1.2 terms section), Research_Frontier.md (OPEN-SS-22 retired, OPEN-SS-25 registered), predictions.md (PRED-C-42 through PRED-C-53), paper_catalog.md, founders_vision.md, CPP_the_theory.md (new Part VI), problem_histories/PH-OPEN-SS-22.md. Bibliography entry pending.
**Remaining:** OSF registration for v1.2 (update DOI JXE8D); development transcript for v1.2 cycle (registration→retirement 24h arc).
**Significance:** Third predictive nuclear sector after SS-5 ($A \leq 4$ cascade) and SS-6 (deuteron observables scoping). 12 independent zero-parameter predictions — densest single-paper star shot to date under the swarm-validation doctrine. First retired open problem establishes the OPEN → RETIRED status transition in the programme record.

### Project 0e: SS-8 — Neutron-Excess Extension of Alpha-Chain Formula (OPEN-SS-23) — **NEW NEXT PRIORITY**
**Status:** Registered as primary target 21 April 2026 following SS-7 v1.2 retirement of OPEN-SS-22 and absorption of the ~2 MeV-per-neutron signal into OPEN-SS-23. SS-8 Phase 1 exploration (AME 2020 alpha-chain map) already produced the isotope-selection catch that drove OPEN-SS-22 retirement.
**Goal:** Extend the SS-7 3N−6 alpha-chain formula to non-N=Z nuclei: (i) neutron-excess even-even isotopes at alpha-chain $N_\alpha$ values (${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe at $\Delta N = +4$ as the immediate cases; ${}^{48}$Ca at $\Delta N = +8$ as a stress test); (ii) odd-A nuclei with single extra nucleons bound to alpha cores (${}^7$Li, ${}^9$Be, ${}^{11}$B, ${}^{13}$C); (iii) non-alpha-clustered structures (${}^6$Li ≈ ${}^4$He + d, ${}^{14}$N, ${}^{18}$O). Preliminary ${}^6$Li inspection gives a residual alpha-deuteron binding of 1.47 MeV ≈ $2B_\text{pair}/3 \approx 1.56$ MeV, suggestive of an incomplete K₃ face at the alpha-d contact.
**Success criterion:** The stability valley from ${}^{40}$K through ${}^{208}$Pb reproduced within CPP residual precision; the ~2 MeV-per-extra-neutron pattern derived from first principles rather than calibrated.
**Effort:** 3–5 sessions
**Significance:** Completes the nuclear-chart coverage that OPEN-SS-22 was originally intended to anchor. Under the swarm-validation doctrine this extends star shots to the dominant portion of the nuclear chart (all isotopes, all mass numbers 6–208). The neutron-excess physics is the actual content; the icosahedral-closure hypothesis was a misread of where the physics lived.
**Dependencies:** SS-5 v6, SS-7 v1.2, OPEN-SS-24 (simplicial contact structure; not blocking — SS-8 can proceed with C4 hypothesis), OPEN-SS-25 (DP-sea screening; may need to be addressed for neutron-excess Coulomb).

### Project 0f: Simplicial Contact Structure from CPP Primitives (OPEN-SS-24)
**Status:** Registered 21 April 2026 as spin-off from SS-7 v1.2 theorem-vs-hypothesis split. Would convert SS-7 assumption C4 (alpha clusters arrange as simplicial polytopes) from hypothesis to theorem.
**Goal:** Derive simplicial polytope connectivity from CPP lattice primitives. Three physical intuitions registered in SS-7: (i) triangular faces follow from C1–C2 rigid-tetrahedral base-to-base contact; (ii) simplicial maximises contact reinforcement (thermodynamic selection at fixed $N_\alpha$); (iii) convexity follows from rigid-packing constraints on non-interpenetrating tetrahedra. These need to become quantitative constraints.
**Effort:** 2–3 sessions (mathematical, potentially self-contained)
**Significance:** Would complete the theorem-status of SS-7's central result (from "theorem conditional on C4" to "theorem unconditionally"). A candidate SS-9 paper.
**Dependencies:** SS-2 (lattice-scale grounding), SS-5 (contact-face mechanism), SS-7 (statement of hypothesis).

### Project 0g: DP-Sea Screening of Alpha-Alpha Coulomb (OPEN-SS-25)
**Status:** Registered 21 April 2026 as spin-off from SS-7 v1.2. The Coulomb-free SS-7 formula fits within 1.5% despite each alpha carrying $Z = 2$ — adding full vacuum Coulomb at $R_{\alpha\alpha} = 2.37$ fm (~2.4 MeV per contact) would produce substantial over-subtraction at $N_\alpha \geq 3$, yet ${}^8$Be itself is consistent with full Coulomb. The contrast implies DP-sea screening that requires at least one additional alpha neighbour.
**Goal:** Derive the DP-sea reorganisation that produces the effective $V_C^{\text{eff}}$ reduction from CPP primitives. Must reproduce ${}^8$Be full-Coulomb limit at $N_\alpha = 2$ (isolated contact) and the effective-near-zero Coulomb implied by the Table 1 agreement at $N_\alpha = 3$–$14$ (embedded contacts).
**Effort:** 2–4 sessions
**Significance:** Addresses a quantitative puzzle in SS-7's numerical agreement. Progress here could also inform Coulomb handling in SS-8's neutron-excess extension.
**Dependencies:** DP Sea description (founders_vision §3 — still [to be filled]), SS-2 (lattice-scale), SS-7 (statement of puzzle).

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
- [x] SS-5 v6: Light-nuclei binding from open-vertex cascade (18 April 2026)
- [x] SS-6 v0.1: Deuteron observables scoping (18 April 2026)
- [x] SS-7 v1.2: Alpha-cluster regime and 3N−6 edge formula; 12 concurrent zero-parameter predictions; OPEN-SS-22 retired as first retired open problem in CPP programme record (21 April 2026)
- [x] PH-OPEN-SS-22.md: First retired-open-problem narrative in CPP programme record (21 April 2026)

---

*This document is updated as projects are completed or new ones are identified.*
