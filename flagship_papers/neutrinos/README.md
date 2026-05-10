# SF-4: Neutrino Sector Unification from 600-Cell Geometry

**Status:** Active. Audit phase complete (Session 37, patch 0294); mechanism selected (Session 39, patch 0298); both substantive sub-derivations at PARTIAL CLOSURE — OPEN-FP-SF-4-1 (Session 41 patch 0300) and OPEN-FP-SF-4-2 (Session 43 patch 0303). Outline established Session 44 patch 0304. v0.1 .tex shipped Session 45 patch 0305; v0.2 §4 Session 46 patch 0306; v0.3 §5 Session 47 patch 0307; v0.4 §6-§11 Session 48 patch 0308; v0.5 integration polish + first PDF Session 49 patch 0309; v0.6 ChatGPT pass 1 corrections Session 50 patch 0310; v0.7 ChatGPT pass 2 corrections Session 51 patch 0311; v0.8 Grok + Copilot independent reviews Session 52 patch 0312. **v0.9 ChatGPT pass 3 corrections incorporated Session 53 patch 0313** — three v1.0-blocking issues fixed (JUNO uncertainty formatting; mass-ratio arithmetic consistency with explicit dual-convention presentation; JUNO bibliography arXiv:2511.14593) plus CHANGELOG bookkeeping. Reviewer's pass 3 forward-looking assessment: "After those fixes, I would be comfortable promoting SF-4 to v1.0 SHIP as a partial-closure flagship prediction paper." Five review passes complete (ChatGPT × 3 + Grok × 1 + Copilot × 1). **Paper is v1.0-promotion-ready**; next session decision is whether to do one final verification pass or promote directly to v1.0 SHIP.
**Estimated sessions to v1.0 SHIP:** 10–14 (audit done; selection + derivation campaign + writing).
**Inclusion criterion fit:** (1) named known-unknown — neutrino masses, mass hierarchy ordering, $\delta_{CP}$, the eight neutrino oscillation parameters in toto; (4) bridge to recognized mathematics — polytope theory and distance-shell structure of the 600-cell.

---

## Scope

The full eight-parameter neutrino sector — three masses (or two splittings + lightest), three mixing angles, $\delta_{CP}$, hierarchy ordering — derived from CPP first principles. The paper presents the unified neutrino sector as the apex-paper answer to: Why are neutrinos so much lighter than charged leptons? What sets the mass-squared splittings? Why tribimaximal-like mixing with specific corrections? What is the value of $\delta_{CP}$?

This is the heavy-lift SF-line paper. The audit phase (Session 37, patch 0294, document at `sketches/SF-4_neutrino_sector_audit.md`) established that the corpus is thin in the neutrino sector — SM-5 derives PMNS angles at zeroth order but mass values, $\delta_{CP}$, ordering, and TBM corrections are all open or pre-formalism. The strict-C posture (no compromise on first-principles rigor) requires substantial new derivation work.

## Source material (heavy-lift; substantial new derivation needed)

| Source paper / file | Content drawn | Status |
|---------------------|---------------|--------|
| SM-5 | Tribimaximal Neutrino Mixing from $K_3$; PMNS angles at zeroth order | Established but conditional on SM-5 ansatz A1 (neutrino mass eigenstates = $K_3$ eigenmodes) |
| SM-7/SM-8/SM-9 | Shell-distance methodology; $V^\alpha$ scaling; $M_0$ prefactor | Quark machinery; Candidate-C mechanism extends this to unbound regime |
| SM-2 §Neutrino Mass Estimates | Pre-formalism $\sigma = 120^{-3}$ entropy suppression with $N_k \in \{1,4,12\}$ | Estimates only; explicitly self-flagged as "not first-principles"; splittings off by factor 5/20 |
| `archive/grok-exploratory-SM/p2-neutrino-masses-and-suppression/` | Same $\sigma = 120^{-d}$ derivation in archived form | Archived; pre-600-cell |
| Nov 2025 viXra DUNE paper (not in repo; user-shared) | Cage-radius scaling $m \propto 1/R$ with $\lambda = \phi^{3/2}$ claim | **Falsified by audit + falsifier check (patch 0295 prep work)** — algebra error; quoted masses calibrated not derived; cage-radius spread inadequate to observed splitting span |

## Audit findings (Session 37, document in `sketches/`)

Key results from the audit document:

1. **Eight parameters in scope.** Three masses + three mixing angles + $\delta_{CP}$ + hierarchy ordering. The unified document covers all eight.
2. **Current-corpus state.** Only PMNS angles at TBM zeroth order are established (SM-5). Everything else is open.
3. **Pre-formalism material analysis.** Two distinct mechanisms in pre-formalism material ($\sigma = 120^{-d}$ entropy suppression vs cage-radius scaling); both have specific identifiable problems documented in audit §4.
4. **Five mechanism candidates** for current-formalism derivation. Cross-comparison matrix in audit §5.
5. **K3 integration is non-negotiable.** The mechanism must produce three mass eigenstates that align with $K_3$ eigenmodes at zeroth order to preserve SM-5's PMNS derivation. (Audit §6 Constraints K1/K2/K3.)
6. **Q3 calibration architecture coupled.** Single-calibration ($m_e$) is preserved by Candidates A and C; threatened by B/D/E.
7. **$\delta_{CP}$ posture is a separate decision.** Route (i) derive, (ii) register-as-open, or (iii) register-as-falsifier. To be settled in mechanism-selection session.

## Falsifier check (audit follow-up, patch 0295)

Done during the architectural-decision break:

- **Candidate B (cage-radius $m \propto 1/R^k$): falsified.** 600-cell bonded-shell radii spread is factor $\sim 3.74$ (tetrahedron 0.378 to icosidodecahedron $\sqrt{2}$). Observed neutrino mass ratios are factor $\sim 51$. No single power-law in radius fits the two splittings simultaneously ($k_{32} = 4.75$, $k_{21} = 6.24$).
- **Candidate C (shell-distance $m \propto V^\alpha$): encouraging at $\alpha = 2$.** With assignment ($\nu_e \to$ tetrahedron $V=4$; $\nu_\mu \to$ icosahedron $V=12$; $\nu_\tau \to$ icosidodecahedron $V=30$), the splitting predictions are $m_2/m_1 = 9.00$ vs observed $8.66$ (within 4%) and $m_3/m_1 = 56.25$ vs observed $50.9$ (within 11%). The integer exponent $\alpha = 2$ has a natural derivation handle: it matches the pair-count $V^2$ component of the SM-9 decomposition $V^{7/3} = V^2 \cdot V^{1/3}$, with the linear-cage-dimension factor $V^{1/3}$ absent for unbound modes.

Candidate C is now the strongest prior heading into mechanism-selection. The absolute-scale prefactor (suppression factor for the unbound regime) remains a separate first-principles question.

## Strategic role

SF-4 is the pivot paper of the SF-line: longest derivation campaign, highest scientific upside, the one paper whose ship-state determines whether SF-5 (unification) can be the no-compromise apex synthesis. The early-encouraging falsifier result for Candidate C suggests the campaign is tractable; the audit established the work scope; the mechanism-selection session sets the path.

## What this folder contains and will contain

Currently:
- `README.md` — this file
- `sf-4_outline.md` — v0.1 paper outline (Session 44, patch 0304)
- **`sf-4_neutrinos.tex`** — **v0.9 paper draft (Session 53, patch 0313)**: ChatGPT pass 3 corrections incorporated; 1850 lines source; **v1.0-promotion-ready**
- **`sf-4_neutrinos.pdf`** — **v0.9 compiled PDF (Session 53, patch 0313)**: 40 pages, 536 KB; v1.0 SHIP candidate
- `sketches/README.md` — staging-document discipline
- `sketches/SF-4_neutrino_sector_audit.md` — eight-parameter audit (Session 37, patch 0294)
- `sketches/SF-4_mechanism_selected.md` — mechanism-selection decision document (Session 39, patch 0298)
- `sketches/SF-4_suppression_derivation.md` — OPEN-FP-SF-4-1 working document (Sessions 40-41, patches 0299/0300; PARTIAL CLOSURE physical picture in hand at $\sigma = z^{-2 d_{\text{eff}}}$)
- `sketches/SF-4_k3_cage_shell_consistency.md` — OPEN-FP-SF-4-2 working document (Sessions 42-43, patches 0302/0303; PARTIAL CLOSURE: structural-physical picture established at SM-5-inheritance level)

To come:
- `sketches/SF-4_*.md` — additional sub-derivation working documents per the SS-9 staging discipline
- `documentation_suite/`, `letters/`, `founders_voice/` per SS-9 four-tier discipline as the paper develops to v0.6+ AI-review iteration

---

*Folder established at Session 38 (patch 0295) per Option-3 architecture; Q1 audit migrated from `flagship_papers/hierarchy_problem/sketches/` (the original Track 1 location) to the SF-4-dedicated home.*
