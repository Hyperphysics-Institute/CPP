# SF-4: Neutrino Sector Unification from 600-Cell Geometry

**Status:** **v3.0 SHIPPED Session 66** (10 May 2026, patch 0327). **OPEN-FP-SF-4-1 RESOLVED at all four sub-goals**: Picture A axiomatic closure (Sessions 55–60 patches 0316–0321, v2.0) plus α-exponent residual closure (Sessions 62–66 patches 0323–0327, v3.0). The full mass formula $m_{\nu_i} = M_0 \cdot V_{\nu_i}^2 \cdot \sigma_\nu$ at leading order is now rigorously derived from CPP axioms plus foundational inputs: Picture A delivers $\sigma_\nu = (1/z^2)^5 = 1/z^{10} \approx 1.62 \times 10^{-11}$ from A1–A11 + three foundational inputs (3D embedding, neutrino identification, spin-orbital 2:1 frequency convention); α-exponent residual delivers Theorem 3.1 — $m_\text{unbound} = M_0 \cdot V^2 \cdot \sigma_\nu$ at leading order in V — from A1, A2, A4, A6', A7, A9 plus four foundational inputs (FI-α-1 SM-9-inheritance for $V^{7/3}$; FI-α-2 cage-cooperative SSV reinforcement; FI-α-3 neutrino identification [shared with Picture A]; FI-α-4 rigid-cage operational definition with central-anchor condition); the bound-mode formula's $V^{7/3} = V^2 \cdot V^{1/3}$ reduces to $V^2$ alone with $V^{1/3} \to 1$ in the unbound regime. Substantive content (§0–§11) frozen at v3.0; documentation suite ACTIVE post-ship per SS-9 lesson learned. **Forward work flows through OPEN-FP-SF-4-2 cross-sector closure with SM-5 antibonding-doublet (now structurally identified as dominant residual source for ν_3 per Finding α-7 empirical residual decomposition), anthology chapter, TATWD integration, SF-2 EW-flagship closure for $\delta_{CP}$, JUNO peer-review bibliography update, and public posting v3.0 at Thomas's discretion.** Earlier campaign history: audit phase complete (Session 37, patch 0294); mechanism selected (Session 39, patch 0298); both substantive sub-derivations at PARTIAL CLOSURE — OPEN-FP-SF-4-1 (Session 41 patch 0300) and OPEN-FP-SF-4-2 (Session 43 patch 0303); outline established Session 44 patch 0304; v0.1 .tex shipped Session 45 patch 0305; v0.2 §4 Session 46 patch 0306; v0.3 §5 Session 47 patch 0307; v0.4 §6-§11 Session 48 patch 0308; v0.5 integration polish + first PDF Session 49 patch 0309; v0.6 ChatGPT pass 1 Session 50 patch 0310; v0.7 ChatGPT pass 2 Session 51 patch 0311; v0.8 Grok + Copilot Session 52 patch 0312; v0.9 ChatGPT pass 3 Session 53 patch 0313; **v1.0 SHIP Session 54 patch 0314**; OPEN-FP-SF-4-1 Picture A axiomatic closure campaign Sessions 55–60 patches 0316–0321 with working sketch document `sketches/SF-4_picture_A_axiomatic_closure.md` (1106 lines, Tier-4 closure source for Picture A); **v2.0 SHIP Session 60 patch 0321** integrating Picture A closure into paper (42 pages, 559 KB); OPEN-FP-SF-4-1 α-exponent residual closure campaign Sessions 62–66 patches 0323–0327 with working sketch document `sketches/SF-4_alpha_exponent_closure.md` (1184 lines, Tier-4 closure source for α-exponent residual); **v3.0 SHIP Session 66 patch 0327** integrating α-exponent residual closure into paper (45 pages, 579 KB); Session 67 patch 0328 programme-level registration completing OPEN-FP-SF-4-1 RESOLVED.
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
- **`sf-4_neutrinos.tex`** — **v1.0 SHIPPED (Session 54, patch 0314)**: 1850+ lines source; FROZEN at v1.0
- **`sf-4_neutrinos.pdf`** — **v1.0 SHIPPED compiled PDF (Session 54, patch 0314)**: 40 pages, 537 KB
- `documentation_suite/handover-SF-4.md` — Session 54 v1.0 SHIP close handover (~250 lines)
- `documentation_suite/development-SF-4.md` — 17 vignettes covering Sessions 37–54 (~280 lines)
- `documentation_suite/transcript-SF-4.md` — per-session transactions log (~200 lines)
- `documentation_suite/reasoning-SF-4.md` — Tier 4 verbatim reasoning across 7 sections (~360 lines)
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
