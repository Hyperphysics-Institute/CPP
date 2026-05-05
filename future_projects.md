# CPP Future Projects

**Location:** `/CPP/future_projects.md`
**Purpose:** Prioritised list of next papers, infrastructure work, and long-term goals.
**Last updated:** 5 May 2026 (Session 13 close: OPEN-SS-35 closure programme through Session 13 captured — 7 programme-level negative results ruled out, 1 qualitative cross-paradigm consilience claim achieved, 1 Decoupling Theorem established, R2 substantively bracketed; Phase 3B IRREP-selective decomposition registered as Session 14 Priority 1 with three sharply constrained quantitative targets)

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

### Project 0e: SS-8 — Interstitial-Neutron Binding and the 2E/V Scaling Law on the Alpha-Polytope — **v1.0 COMPLETE 25 April 2026**
**Status:** ✅ v1.0 published-ready 25 April 2026 (multi-AI Round 1 + Round 2 review cycles complete: Opus, ChatGPT, Copilot, Grok). 1184 lines / paper at v1.0 in `series_strong/papers/SS-8/SS-8_interstitial_neutron_2EV_scaling.tex`. Per-paper subfolder structure complete (reviews/, letters/, sketches/, scripts/, founders_voice/, documentation_suite/ all populated). 5 Python verification scripts in `scripts/`. Round 1 + Round 2 reviewer correspondence preserved verbatim (10 review files + 5 letters).
**Result:** Conditional zero-parameter scaling law $\Delta_1(N_\alpha) = (6 - 12/N_\alpha)\,B_\text{pair}$ for single-neutron interstitial binding in alpha-cluster nuclei, where $B_\text{pair} = M_0/\varphi = 2.342$ MeV is the third-scale recurrence of the SS-5 K₃-mode quantum and $2E/V = 6 - 12/N_\alpha$ follows from Euler's formula on simplicial 3-polytopes. **42 conditional zero-parameter predictions:** 12 primary at $N_\text{ex} = 2$ across $N_\alpha \in [3, 14]$ + 30 secondary at $N_\text{ex} \in [3, 8]$. Two sub-1% agreements at the most symmetric polytopes: ${}^{26}$Mg (octahedron at $N_\alpha = 6$, $-0.2\%$) and ${}^{42}$Ca (gyroelongated square bipyramid at $N_\alpha = 10$, $-1.0\%$). 11 of 12 within 15% in the bulk regime; 5 of 6 even-$N_\alpha$ validation rows within 10%. **3 paper-level conditional theorems registered:** D1 (proximity-binding / vertex localization), D2 (K₃-edge coupling at host vertex), D3 (bulk-regime averaging). D1 promoted to a conditional theorem under two functionally independent sufficient premises (Level-1 algebraic and Level-2 functional independence established; Level-3 physical-principle independence open). Registers OPEN-SS-26 (D1 derivation from SSV minimization, Level-3 PARTIAL), OPEN-SS-27 (D2 K₃-edge coupling derivation via A6′ extension), OPEN-SS-28 (D3 bulk-regime averaging derivation + residual decomposition). Partially resolves OPEN-SS-23 (non-N=Z extension restricted to $N_\text{ex} \leq 8$, $N_\alpha \in [3, 14]$).
**Registry cascade completed (patches 0024–0026):** predictions.md (PRED-C-54 through PRED-C-95 added; cumulative swarm-tally section established at 103 entries; ratio 11.4×); axiom-registry.md (cross-referenced; entry #14 reframed from accommodation to derivation per audit follow-up). Documentation suite (mechanism-/glossary-/phenomena-/philosophy-/reviews-/keywords-/FAQ-) pending (Session 2 of paper-completion checklist). Theorem-registry, paper_catalog, README/INDEX, master_glossary updates in progress (this patch / patch 0027).
**Significance:** Completes the SS-5 → SS-7 → SS-8 cascade across three nuclear scales. Demonstrates the K₃-mode quantum's third recurrence at the interstitial-alpha contact scale (Pattern 6 in axiom-registry.md). Adds 42 conditional empirical correspondences to the cumulative CPP swarm — the densest single-paper contribution to date. Establishes the conditional-theorem-with-independence-tiers methodology (D1's Level-1+2 promotion under functionally independent realizations).
**Remaining for SS-8 v1.0 archive close:** Documentation suite (7 companion files), problem_histories/PH-OPEN-SS-27.md and PH-OPEN-SS-28.md, OSF registration. None blocking SS-9 drafting.

### Project 0f: SS-9 selection — **DEFERRED, candidate slate below**
**Status:** SS-8 v1.0 completion (25 April 2026) closes the OPEN-SS-22 → OPEN-SS-23 retargeting arc. SS-9 selection deferred pending Thomas review of candidates.

**Candidate slate (in priority order by my read; Thomas's call):**

1. **OPEN-SS-24 — First-principles derivation of C4 simplicial connectivity from CPP primitives.** *Highest-leverage by far.* Closing this converts 54 of 55 conditional D-N predictions (12 SS-7 alpha-chain bindings + 42 SS-8 interstitial bindings) to unconditional. The single-largest swarm-count promotion available. Effort: 2–3 sessions, mathematical, potentially self-contained. Three physical intuitions already registered in SS-7. **Recommendation: this is the high-leverage SS-9 if the math is tractable.**

2. **OPEN-SS-23 remainder — Non-N=Z and odd-A extension beyond what SS-8 covered.** *Quicker but less impactful.* SS-8 covered $N_\text{ex} \in [2, 8]$ at $N_\alpha \in [3, 14]$; remainder is odd-A nuclei (single extra nucleons bound to alpha cores) and non-alpha-clustered structures (${}^6$Li, ${}^{14}$N, ${}^{18}$O). Effort: 2–4 sessions. Significance: extends nuclear-chart coverage but doesn't close the conditional-theorem chain.

3. **OPEN-SS-26 Level-3 — D1 vertex localization from CPP primitives, completing the Level-3 independence gap.** *Targeted spin-off from SS-8.* Effort: 1–2 sessions. Significance: promotes SS-8's D1 from conditional theorem to unconditional theorem, but the 42 SS-8 predictions stay conditional on C1–C4 + D2 + D3 even after this closes — so leverage is smaller than OPEN-SS-24.

4. **OPEN-SS-27 — D2 K₃-edge coupling via A6′ extension.** Effort: 2 sessions. Significance: as #3 (targeted spin-off, modest leverage).

5. **OPEN-SS-28 — D3 bulk-regime averaging derivation + residual decomposition.** Effort: 2 sessions. Significance: would tighten SS-8's secondary 30 predictions from 8–15% to under 5%, but doesn't promote any conditional D-N to unconditional.

6. **DP-sea Coulomb screening (OPEN-SS-25).** Effort: 1–2 sessions. Significance: addresses a quantitative puzzle in SS-7's numerical agreement but doesn't add new predictions; leverage is mostly defensive.

7. **Charge quantisation post-mortem paper.** PH-THEO-SS-9 already documents the proof; could anchor an SS-9 that draws out the unification with the K₃ spectral theorem (both K = 2/3 and δ = 1/3 emerge from the same K₃ graph — the deepest two CPP lepton results share one geometric source). Significance: high pedagogical value, modest research leverage.

**My recommendation: OPEN-SS-24** — the leverage on the swarm count is unmatched. Pivot to OPEN-SS-23 remainder if OPEN-SS-24's math turns out to be intractable in a 2–3 session window.

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

## Session-level priority queue (cross-session backlog)

**Purpose:** Track high-leverage moves that have been identified but deferred to keep individual sessions focused. Updated 5 May 2026 Session 13 close (Phase 3B IRREP-selective decomposition registered with sharp quantitative targets; OPEN-SS-35 closure programme has produced 7 programme-level negative results, 1 qualitative cross-paradigm consilience claim, and 1 Decoupling Theorem since Session 5).

### Active queue (next-session ready)

**(A.1) Phase 3B — IRREP-selective Hessian decomposition (next-session priority).**
*Priority:* HIGH (sharply constrained falsifier rather than qualitative search; closure of R2 if successful). *Scope:* Multi-session by scope (3–5 sessions), but Phase 3B-A is single-session-tractable. *Trigger:* Session 13 Phase 3A established constructive bracketing — empirical peak softening $-33.6\%$ at $N_\alpha = 10$ lies between Phase 2 lower bound $-4.6\%$ and Phase 3A upper bound $-85\%$; empirical is $\sim 40\%$ of upper bound; mode space contains sufficient amplitude, selection is the bottleneck. *Quantitative targets from the bracketing:* (a) $\sim 40\%$ of full-mode-space softening at J-solid mid-range $N_\alpha = 7$–$10$ (belt-localized fraction $\sim 0.4$); (b) near-zero at regular polytopes $T_d$, $I_h$ (no belt IRREP, projection vanishes); (c) $O_h \ll D_{2d}$ ratio at $N_\alpha = 6$ (Reading-A vs Reading-B/C discriminator). Targets turn Phase 3B from qualitative search into sharp falsifier. *Registered:* 5 May 2026 Session 13 Phase 3A close, OPEN-SS-35 paragraph in `Research_Frontier.md`. *Companion:* `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_unification_phase3a.md` §6.

**(A.2) OPEN-SS-35 closure programme — broader continuation.**
*Priority:* HIGH (largest cross-paradigm consilience target the programme has identified). *Scope:* Multi-session, possibly multi-paper. *State at Session 13 close:* First qualitative cross-paradigm consilience claim achieved Session 9 (empirical magic-number sequence reproduced from CPP first-principles via $\hbar\omega^*$ and $V_{\rm SO}$). Decoupling Theorem established Session 12 (A-scaling closure and gap-strength closure are independent open problems; closure of one does not advance the other). 7 programme-level negative results ruled out (Routes D, B-γ, 1b, Path (i), R1, Phase 2 model (a), Phase 3A naive full-Hessian). R2 substantively bracketed — Phase 3B IRREP-selective is the only remaining R2 closure realization untested. *Best lead at registration:* CPP analog of spin-orbit coupling from 600-cell coordination + ZBW phase structure. Pattern-6 K$_3$ scale-recurrence at the nucleon-shell-organization scale. *Registered:* 2 May 2026 Session 4 follow-up 3rd sub-arc, OPEN-SS-35 entry in `Research_Frontier.md`. *Companion sketches:* SS-9 sketches OPEN-SS-35 sub-question (a) Ascaling and sub-question (b) Balpha layer1/2/3, plus the OPEN-SS-32 ↔ U-shape unification phase 1/2/3a.

### Completed and removed from queue

- ✅ **2 May 2026:** PRED-O-19 verification at ${}^{84}$Mo, ${}^{88}$Ru, ${}^{100}$Sn (Kimura+2025, Mougeot+2021). Two direct hits + one regime-termination deviation at registered falsification route. Patches 0066–0072.
- ✅ **2 May 2026:** OPEN-SS-34 Level-1 derivation under H1–H4. Three target derivations (T1, T2, T3) + $\sqrt{3}$ refinement (T4). OPEN-SS-35 and OPEN-SS-36 registered as deepest dependencies. Patches 0073–0079.
- ✅ **2 May 2026:** OPEN-SS-36 derivation attempt with self-correction. Constant-$\sqrt{3}$ retired; refined closure+shell decomposition replaces it. OPEN-SS-36 closure now identified as dependent on OPEN-SS-35. Patches 0080–0087.
- ✅ **2 May 2026 (Session 5 Phase 1):** AME 2020 lookup for ${}^{92}$Pd and ${}^{96}$Cd. Both extrapolation-matches at <0.5% precision. PRED-C-77 and PRED-C-78 added to swarm at extrapolation level. Empirical $B_{\rm slip}$ sequence acceleration toward ${}^{100}$Sn confirmed, reinforcing 4th sub-arc closure+shell decomposition framing.
- ✅ **2 May 2026 (Sessions 5-9):** OPEN-SS-35 sub-question (a) A-scaling Level-1 partial closure (harmonic-oscillator mean-field from K$_3$ contacts; Pattern-6 K$_3$ scale-recurrence reaches 7 confirmed instances). Sub-question (b) Route B-α layer 1 closure (Fermi velocity from CPP primitives, Session 8). Layer 3 partial closure with first qualitative cross-paradigm consilience claim (Session 9). Patches through ~0125.
- ✅ **2 May 2026 (Sessions 10-11):** Route 1b $V_{\rm SO}$ refinement saturation result (Session 10). Path (i) cluster-surface Thomas-form spin-orbit RULED OUT (Session 11 Phase 1) — fourth programme-level negative result, $K_3$ Gaussian-modulated mean field framework fundamentally insufficient for magic-strength gap closure.
- ✅ **4 May 2026 (Session 12):** R1 ($R_\alpha$ scale-dependence as A-scaling closure) RULED OUT — fifth programme-level negative result. Three independent grounds (wrong sign, U-shape pattern shape-driven not radius-driven, Decoupling Theorem). U-shape diagnostic registered with forward pointer to OPEN-SS-32 J-solid regime.
- ✅ **4–5 May 2026 (Session 13 Phases 1, 2, 3A):** OPEN-SS-32 ↔ U-shape unification investigation. Phase 1 prior-art read refined patch-0149 cross-link from "coincides exactly" to "qualitative six-of-eight with octahedron $N_\alpha=6$ as discriminator"; three admissible readings (A, B, C) registered. Phase 2 uniform-scaling radial-breathing model (a) RULED OUT — sixth programme-level negative result (factor 7.4 magnitude undershoot, monotonic vs U-shape pattern, wrong endpoint signs). Phase 3A naive full-Hessian RULED OUT — seventh programme-level negative result (flat $-85\pm1\%$ pattern, factor 2.5 overshoot, $O_h \approx D_{2d}$ selection failure). **Constructive bracketing established:** empirical $-33.6\%$ peak between $-4.6\%$ (Phase 2) and $-85\%$ (Phase 3A); empirical $\sim 40\%$ of upper bound; selection is the bottleneck, not amplitude. Phase 3B sharply constrained as falsifier. Patches 0152–0168.

---

*This document is updated as projects are completed or new ones are identified.*
