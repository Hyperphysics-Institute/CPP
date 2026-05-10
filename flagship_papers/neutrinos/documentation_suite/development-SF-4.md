# SF-4 Development Document — Session-by-Session Vignettes

**Paper**: `flagship_papers/neutrinos/sf-4_neutrinos.tex` (v1.0 SHIPPED Session 54)
**Purpose**: Per-session development arc covering Sessions 37–54 (audit phase through v1.0 SHIP).
**Companion**: `transcript-SF-4.md` (per-session transactions); `reasoning-SF-4.md` (Tier 4 verbatim reasoning); `handover-SF-4.md` (Session 54 v1.0 SHIP close).

---

## Vignette 1 — Session 37 (audit phase, patch 0294)

The SF-line architectural decision at Session 36 (patch 0293) split the original "Sector Foundations" plan into a 5-paper SF-line architecture covering all 17 SM particles. Of those five, SF-4 (neutrino sector) was identified as the heavy-lift paper — the only one requiring substantive new derivation work, since the existing SM-5 corpus delivered TBM mixing angles at zeroth order but mass values, $\delta_{CP}$, and ordering were all open.

Session 37 conducted the audit. Document: `sketches/SF-4_neutrino_sector_audit.md`.

Key audit findings:
1. Eight observable parameters in scope: 3 masses + 3 mixing angles + $\delta_{CP}$ + hierarchy ordering
2. Pre-formalism material analysis surfaced two distinct mechanism candidates ($\sigma = 120^{-d}$ entropy suppression vs cage-radius scaling); both had specific identifiable problems
3. Five mechanism candidates for current-formalism derivation (Cross-comparison matrix in audit §5)
4. K3 integration identified as non-negotiable: any mechanism must produce 3 mass eigenstates aligning with K3 eigenmodes at zeroth order to preserve SM-5's PMNS derivation (Audit Constraints K1/K2/K3)
5. Q3 calibration architecture: single-calibration ($m_e$) preserved by Candidates A and C; threatened by B/D/E
6. $\delta_{CP}$ posture identified as a separate decision: route (i) derive, (ii) register-as-open, (iii) register-as-falsifier

The audit was the foundation for the subsequent mechanism-selection work.

## Vignette 2 — Session 38 (architectural rest, patch 0295)

A falsifier check followed the audit, ruling out Candidate B (cage-radius scaling) cleanly. Candidate C (cage-shell $V^\alpha$ scaling) emerged as the strongest prior at $\alpha = 2$ with the assignment $V \in \{4, 12, 30\}$:
- $m_2/m_1 = 9.00$ vs observed 8.66 (4% match)
- $m_3/m_1 = 56.25$ vs observed 50.9 (11% match)

The folder `flagship_papers/neutrinos/` was established as SF-4's per-paper home. The Q3 audit document migrated from the original Track-1 location (`hierarchy_problem/sketches/`) to the SF-4-dedicated home.

## Vignette 3 — Session 39 (mechanism selection, patch 0298)

Mechanism-selection session formalized Candidate C ($\alpha = 2$) as the SF-4 mechanism. Document: `sketches/SF-4_mechanism_selected.md`.

The decision document covered:
- Why Candidate C: matches K3 + Q3 + delivers a parameter-free mass-ratio prediction
- Why $\alpha = 2$: matches the pair-count $V^2$ component of the SM-9 decomposition $V^{7/3} = V^2 \cdot V^{1/3}$, with the linear-cage-dimension factor $V^{1/3}$ absent for unbound modes
- The two open sub-derivations identified: OPEN-FP-SF-4-1 (suppression mechanism for absolute scale) and OPEN-FP-SF-4-2 (K3-Cage-Shell Consistency at vertex-by-vertex level)
- $\delta_{CP}$ posture: route (ii) selected (defer to SF-2 EW-sector flagship)

Two open problems registered in `Research_Frontier.md`:
- OPEN-FP-SF-4-1: Suppression mechanism Picture A formalization from CPP axioms A1–A11
- OPEN-FP-SF-4-2: Vertex-by-vertex K3-coupling theorem; tied to SM-5 antibonding-doublet open problem

## Vignette 4 — Sessions 40–41 (OPEN-FP-SF-4-1 partial closure, patches 0299–0300)

Session 40 (patch 0299): Suppression mechanism leading-order derivation work. The walk-dimension framework $\sigma = N^{-d}$ gives $\sigma_\nu = z^{-2 d_{\mathrm{eff}}}$ with integer channel enumeration $d_{\mathrm{eff}} = 5$ (3 spatial + 1 ZBW phase + 1 orientation). Per-channel suppression $z^{-2}$ from initial physical-picture analysis. Combined: $\sigma_\nu = 12^{-10} \approx 1.62 \times 10^{-11}$, matching empirical at 2%.

Session 41 (patch 0300): Three convergent CPP physical pictures all give per-channel suppression $\sigma_{\mathrm{channel}} = 1/z^2$:
- **Picture A**: Two-sided DI-bit exchange — both sides need to align for channel coherence; probability $1/z \cdot 1/z = 1/z^2$
- **Picture B**: Two ZBW half-cycles per moment; alignment required at both half-cycles; probability $(1/z)^2$
- **Picture C**: Edge-straddling coherent state across nearest-neighbor pair; coherent population $\sim 1/z^2$

OPEN-FP-SF-4-1 status: PARTIAL CLOSURE (structural-physical picture established with quantitative prediction in hand at 2% empirical match; theorem-level closure from CPP axioms registered for v1.0+ work).

## Vignette 5 — Session 41 (architectural revision, patch 0301)

Mid-Session 41, the user surfaced two CPP physical-content claims that prompted SF-line architectural revision:
- **W⁰ as bracelet/open-config catalyst substrate** (CPP-novel particle prediction) — registered as CONJ-EW-W0
- **No-8-gluons claim** — SU(3) octet as phenomenological dressing of smaller substrate structure (4 baryon tetrahedral vertices) — registered as CONJ-SS-Gluon-4Vertex

The architectural revision: 5-paper → 7-paper SF-line. SF-2 narrowed to cage bosons only; new SF-5 (strong sector) added; new SF-6 (electromagnetism) added; SF-5-original renumbered SF-7 (grand unification synthesis). Architectural patches 0301 landed the README + Research_Frontier registrations + transcript §16 documenting the decision.

The SF-line transcript file (`flagship_papers/SF-line_development_transcript.md`) was created with §1–§16 covering Sessions 37–41 architectural conversations.

## Vignette 6 — Sessions 42–43 (OPEN-FP-SF-4-2 partial closure, patches 0302–0303)

K3-Cage-Shell Consistency Theorem development work. Document: `sketches/SF-4_k3_cage_shell_consistency.md`.

Session 42 work: Mass-basis-vs-flavor-basis clarification (the load-bearing observation). The cage-shell V assignment is in mass basis (K3-eigenmode basis from SM-5) not flavor basis (K3 vertex basis); flavor-basis reading would force PMNS = identity contradicting observation. Numerical zeroth-order consistency exact: $\hat{V}^2_{\mathrm{flavor}}$ matrix has exact $\mu\tau$-exchange symmetry whose eigenvectors are exactly TBM directions.

Session 43 work: Route C structural closure at SM-5-inheritance level. Direct 600-cell distance-shell computation:
- V values $\{4, 12, 30\}$ verified as the available cage shells from any 600-cell vertex
- V = 20 exclusion forced by SM-1 particle-type taxonomy (assigned to bottom quark + Higgs)
- $\nu_2 \leftrightarrow V = 12$ forced by full-$S_3$-symmetric bonding mode + $S_3 \subset H_3$ symmetry-hierarchy
- Antibonding doublet split V=4 / V=30 via wavefunction-spread / $\mu\tau$-symmetry-character argument, inheriting SM-5's existing open problem

OPEN-FP-SF-4-2 status: PARTIAL CLOSURE (structural-physical picture at SM-5-inheritance level; theorem-level vertex-by-vertex coupling tied to SM-5 antibonding-doublet open problem).

## Vignette 7 — Session 44 (v0.1 outline, patch 0304)

Outline document established: `sf-4_outline.md`. 12-section structure:
- §0 Abstract
- §1 Introduction (founder's voice + claim status)
- §2 SM-5 K3-Eigenmode Foundation
- §3 Candidate-C Cage-Shell Mass Formula
- §4 Suppression Mechanism (OPEN-FP-SF-4-1)
- §5 K3-Cage-Shell Consistency Theorem (OPEN-FP-SF-4-2)
- §6 Predictions Summary
- §7 $\delta_{CP}$ Posture (Route ii)
- §8 Higher-Order Corrections (OP-SM-7d Inheritance)
- §9 Cumulative Falsifier
- §10 Open Theorem-Level Work
- §11 Discussion

The outline was used as the structural skeleton for the v0.1 .tex draft.

## Vignette 8 — Session 45 (v0.1 .tex SHIP, patch 0305)

v0.1 .tex SHIPPED. Foundation §0–§3 at full draft quality (565 lines source); derivation §4–§5 and closing §6–§11 as substantive stubs with key results stated in mdframed status boxes. Bibliography seeded with 12 internal CPP references. The paper SHIPPED with explicit "v0.1 status" markers on all stub sections, indicating the iteration plan v0.2 (§4) → v0.3 (§5) → v0.4 (§6–§11) → v0.5 (integration polish).

## Vignette 9 — Session 46 (v0.2 §4 SHIP, patch 0306)

§4 Suppression Mechanism filled to full draft quality from `sketches/SF-4_suppression_derivation.md`. Paper grew from 565 → 766 lines source. The three-pictures comparison table added (Picture A / B / C with cross-reference column). $V^{7/3} \to V^2$ structural argument given in §3.3. Combined result and predictions table (Table 4.2) added in §4.5. OPEN-FP-SF-4-1 sub-goals enumerated (4 items).

## Vignette 10 — Session 47 (v0.3 §5 SHIP, patch 0307)

§5 K3-Cage-Shell Consistency Theorem filled to full draft quality from `sketches/SF-4_k3_cage_shell_consistency.md`. Paper grew from 766 → 972 lines source. Theorem 5.1 (three clauses), Proposition 5.2 ($\mu\tau$-symmetry), Theorem 5.3 (TBM angle recovery) all formally stated. Mass-basis-vs-flavor-basis clarification with explicit proof-by-contradiction. Route C closure: §5.5.1 verified shell sequence (Table 5.1), §5.5.2 V=4 as tetrahedral subset, §5.5.3 V=20 exclusion. Three-arguments structure for K3-eigenmode-to-shell coupling. Remark 5.4 (Inheritance, not weakening). OPEN-FP-SF-4-2 sub-goals enumerated (3 items).

## Vignette 11 — Session 48 (v0.4 §6–§11 SHIP, patch 0308)

§6–§11 closing sections all filled to full draft quality. Paper grew from 972 → 1270 lines source. Master predictions table restructured with grouped categories. $\delta_{CP}$ posture full justification + four candidate handles. Higher-order corrections inheritance posture + expected effects. Cumulative Falsifier developed into 5 falsifiers (3 direct + 2 framework-level + what-is-not-predicted). Open theorem-level work catalog with forward roadmap. Discussion across programme-level pattern + cross-sector implications + outlook. 10 new external bibliography entries (NuFIT 5.3, DESI 2024, Planck 2018, JUNO design, KATRIN 2022, Project 8, DUNE TDR, Harrison-Perkins-Scott, Ma-Rajasekaran, Altarelli-Feruglio).

## Vignette 12 — Session 49 (v0.5 polish + first PDF, patch 0309)

Integration polish pass. Stale-version-number references cleaned (7 fixes across abstract / §1.4 / §4.3 / Table 4.1 / §4.5 / §5.8). Cross-section consistency verified. **First PDF compilation**: 32 pages, 498 KB. PDF and .tex shipped together per SS-9 convention.

## Vignette 13 — Session 50 (v0.6 ChatGPT pass 1, patch 0310)

ChatGPT pass 1 review on v0.5: "NOT v1.0-shippable yet" with eight specific corrections required. v0.6 incorporated all eight:
1. Mass-ratio language fix (mass-squared splitting → mass ratio in abstract + §3.4)
2. $m_{\nu_e} = m_1$ identification removed (§9.1.2 + Table 4.2)
3. Direct-mass falsifier reframed as principled-not-near-programmatic
4. NuFIT 5.3 → 6.0 update
5. JUNO timing softening to multi-year program
6. DESI/Planck bound qualified with Planck-PR4 alternative
7. Claim status ledger added as new §1.6
8. "No new ansatz" → "no new fitted parameter; new structural-coupling claim"

Plus paper-wide "derives" overclaiming audit (6 softenings).

PDF: 37 pages.

## Vignette 14 — Session 51 (v0.7 ChatGPT pass 2, patch 0311)

ChatGPT pass 2 review on v0.6: "Close to v1.0 SHIP quality" with 3 fixes:
1. Mass-ratio language fully propagated (6 relabels in §3.4 title / §3.4 lead-in / §6.1 master table category / §8 intro / §8.2 / §11.2)
2. **Direct-mass falsifier numerical-logic bug corrected**: v0.6 said "$m_\beta > 5$ meV would falsify" but predicted $m_\beta \approx 8.7$ meV makes 5 meV BELOW prediction; reframed as two-sided inconsistency
3. Cross-reference integrity verified

PDF: 38 pages.

## Vignette 15 — Session 52 (v0.8 Grok + Copilot independent reviews, patch 0312)

Two independent reviewers (Grok, Copilot) returned near-identical "close to v1.0 SHIP quality" / "very close to v1.0 SHIP quality" verdicts on v0.7. v0.8 lands ten consolidated polish edits:

1. JUNO 2025 first physics integration (sin²θ12 = 0.3092±0.0087, Δm²_21 = 7.50±0.12 ×10⁻⁵)
2. Structural-vs-statistical residual note in §3.4
3. §3.4 ratios-vs-absolute-scale conceptual separation paragraph
4. §3.3 operator-level picture for α = 2
5. §3.2 geometric-origin paragraph for V ∈ {4, 12, 30}
6. §3.2 prominent boxed mass-basis-vs-flavor-basis remark
7. §4.5 Σm_ν cosmological-bound sanity check (eq:sumcheck)
8. §9.2 partial-failure scenarios subsection (modular falsification)
9. §10.3 expanded out-of-scope (running, leptogenesis)
10. §6.1 master table category labels refined

One LaTeX math-mode bugfix during compile. PDF: 40 pages.

## Vignette 16 — Session 53 (v0.9 ChatGPT pass 3, patch 0313)

ChatGPT pass 3 review on v0.8: "Promote to v0.9, not v1.0 yet" with 3 v1.0-blocking fixes:
1. JUNO uncertainty formatting bug (dimensional misplacement in §3.4)
2. Empirical mass-ratio arithmetic consistency (v0.8 quoted m_2/m_1=8.66, m_3/m_1=50.9, m_1≈0.96 meV together which cannot all be true under any single normalization; v0.9 rewrites §3.4 with explicit dual-convention presentation)
3. JUNO bibliography update from "in preparation" → arXiv:2511.14593

Plus CHANGELOG bookkeeping ("Eight specific edits" → "Ten distinct edits").

Reviewer's forward-looking statement: *"After those fixes, I would be comfortable promoting SF-4 to v1.0 SHIP as a partial-closure flagship prediction paper."*

PDF: 40 pages, 536 KB.

## Vignette 17 — Session 54 (v1.0 SHIP, patch 0314)

**v1.0 SHIP PROMOTION.**

Five-pass review discipline complete (ChatGPT × 3 + Grok × 1 + Copilot × 1) with explicit reviewer convergence on "v1.0-promotion-ready". Session 54 SHIP mechanics:

1. Title block updated to "Version 1.0 SHIPPED"
2. theorem-registry.md: SF-line section added with THEO-SF-4-1 / PROP-SF-4-2 / THEO-SF-4-3
3. paper_catalog.md: SF-line catalog section added with SF-4 v1.0 SHIPPED row
4. Four-tier documentation suite created (handover-SF-4.md, development-SF-4.md, transcript-SF-4.md, reasoning-SF-4.md)
5. flagship_papers/SF-line_development_transcript.md §17 added covering Sessions 42–54
6. INDEX.md and flagship_papers/neutrinos/README.md transitioned to v1.0 SHIPPED status
7. Research_Frontier.md programme-state-changes captured

Programme state changes from v1.0 SHIP:
- Theorem registrations: THEO-SF-4-1, PROP-SF-4-2, THEO-SF-4-3 added (theorem count 52 → 54 + 1 proposition)
- Predictions registered: 7/8 neutrino-sector parameters at zero free parameters
- Open problems: OPEN-FP-SF-4-1 + OPEN-FP-SF-4-2 PARTIAL CLOSURE preserved
- Conjectures: CONJ-EW-W0 + CONJ-SS-Gluon-4Vertex (Session 41) preserved
- Negative-result count UNCHANGED

Post-v1.0 work queue:
- (A) HIGH PRIORITY: OPEN-FP-SF-4-1 Picture A formalization (5–10 sessions)
- (B) CROSS-SECTOR: SM-5 antibonding-doublet open problem (closure benefits both papers)
- (C) NEXT FLAGSHIP: SF-2 EW-flagship drafting (route ii closure delivers $\delta_{CP}$)
- (D) ANTHOLOGY: Rovelli-register chapter (~5000 words, 1–2 sessions)
- (E) TATWD: integration to CPP_the_theory.md (1 session)
- (F) HOUSEKEEPING: JUNO peer-reviewed publication bibliography update when arXiv:2511.14593 progresses

**SF-4 v1.0 SHIPPED. Substantive content frozen at v1.0; documentation suite ACTIVE.**

---

## Cumulative campaign metrics

- **Total sessions**: 18 (Session 37 audit through Session 54 v1.0 SHIP)
- **Total patches**: 21 (0294 audit through 0314 SHIP)
- **Source line count**: 0 → 1850+ (.tex grew incrementally across v0.1 → v1.0)
- **PDF page count**: 0 → 32 (v0.5) → 37 (v0.6) → 38 (v0.7) → 40 (v0.8/v0.9/v1.0)
- **Bibliography**: 12 internal + 10 external = 22 entries
- **Theorems**: 1 conditional (THEO-SF-4-1) + 1 proposition + 1 secondary theorem
- **Predictions**: 7 of 8 neutrino-sector parameters at zero free parameters
- **Falsifiers**: 5 (3 direct + 2 framework-level + partial-failure modular framework)
- **Reviews**: 5 independent AI passes (ChatGPT × 3 + Grok × 1 + Copilot × 1)

---

*Development document closes at Session 54 v1.0 SHIP. Future SF-4 development arc for v1.x revision (if external feedback prompts) or for OPEN-FP-SF-4-1 follow-up work continues in subsequent vignettes appended to this file.*
