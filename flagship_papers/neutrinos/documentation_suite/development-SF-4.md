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

## Vignettes 18–24: Sessions 55–60 OPEN-FP-SF-4-1 Picture A axiomatic closure campaign

After SF-4 v1.0 SHIPPED at Session 54 (partial closure flagship paper), the OPEN-FP-SF-4-1 Picture A axiomatic closure campaign began at Session 55 and ran through Session 60 (six sessions, six patches 0316–0321). The campaign delivered Picture A axiomatic closure at theorem level and integrated the closure into the SF-4 paper as v2.0 SHIPPED.

### Vignette 18: Session 55 — Working sketch document established (patch 0316)

The OPEN-FP-SF-4-1 closure campaign opened at Session 55 with the establishment of the working sketch document `flagship_papers/neutrinos/sketches/SF-4_picture_A_axiomatic_closure.md`. The document organized the closure target into four sub-claims plus the d_eff = 5 channel count: sub-claim (a) substrate independence, sub-claim (b) AND-of-factors across channels, sub-claim (c) equilibrium uniform marginal, and the d_eff = 5 first-principles channel enumeration. Session 55 delivered §0–§7 of the document (476 lines): firewall, setup, sub-claim decomposition, deep analysis of sub-claim (a), and sketches for (b)/(c)/d_eff. Three findings registered (Findings 1–3); sub-claim (a) reached "Outcome 2" status at Session 55 close — close but not closed, with $\sim 42\%$ correction pending κ_1 refinement.

### Vignette 19: Session 56 — Sub-claim (a) closes at theorem level (patch 0317)

Session 56 closed sub-claim (a) at theorem level via a key insight: the $\kappa_1$ correction in the substrate independence proof is bounded by the timescale separation between the orbital ZBW frequency $\omega = mc^2/\hbar$ and the Planck frequency $\omega_P = m_P c^2/\hbar$. For all sub-Planck modes (every SM particle), the per-moment phase advance ratio $m/m_P$ bounds the mode-substrate coupling at probability level: $\kappa_1 \le 2m/m_P$. Combined with A6' edge-sector substrate-substrate independence (which gives $\kappa_2 \le 1/z$), the joint correction $\kappa_1 \cdot \kappa_2 \le 2m/(m_P z)$ is utterly negligible: $\sim 3 \times 10^{-17}$ for top quark, $\sim 10^{-31}$ for neutrinos. The Session 55 §3.4 structural error (1/√z per-branch amplitude misidentified as mode-substrate coupling rather than wavefunction normalization) was identified and corrected. Findings 2 closes (outcome 1, not outcome 2); Findings 4 (the 2% empirical residual is downstream effects, not Picture A corrections) and 5 (κ_1 ~ m/m_P provides cross-sector support for bound/unbound boundary) registered.

### Vignette 20: Session 57 — V1 sanity check confirmed + sub-claim (b) at theorem level (patch 0318)

Session 57 ran the (V1) sanity check raised at Session 56: does the cage-cooperative SSV reinforcement reading of bound modes (per SM-7/SM-8/SM-9) survive the Picture A closure framework? The reading pass confirmed: bound modes have effective per-link energies amplified by $V^{7/3}/N_\text{links}$ via cage cooperation (e.g., 166× for top quark via SM-8 Shell 3 gap z=12 multiplier), but unbound modes lack confinement volume so per-chain frequency is exactly $mc^2/\hbar$ — exactly as the §8.3 timescale argument requires. (V2) and (V3) verification flags also resolved favorably. Sub-claim (b) AND-of-factors closed at theorem level via A6' edge-sector decomposition of substrate state $(\rho, \phi, \vec{O})$ into independent gauge sectors, with sub-leading $O(\alpha_\text{EM}) \sim 1\%$ cross-correlations per pair. Findings 6 (channel decomposition is most load-bearing remaining) and 7 (amplitude AND structure refined into amplitude × ANDing) registered.

### Vignette 21: Session 58 — Sub-claim (c) closes at theorem level (patch 0319)

Session 58 closed sub-claim (c) equilibrium uniform marginal at theorem level via the **transitive-action uniformity lemma**: any $G$-invariant probability measure on a finite set with transitive $G$-action is uniform. Applied to the icosahedral group $I_h$ acting transitively on the 12 DP-orientation options at each vertex (standard property of icosahedral symmetry), under A2 + A4 + A6' edge dynamics, any stationary distribution is $I_h$-invariant; by the lemma, uniform $1/z = 1/12$. By 600-cell vertex-transitivity, this holds at every vertex. The closure is robust across (R2)-S vs (R2)-L readings of "DP orientation". Equilibrium reachability for cosmological neutrino propagation is overwhelming ($\sim 10^{42}$ relaxation times). Finding 8 (sub-claim (c) closes via A2+A4+A6'; equilibrium does not need separate axiom) registered.

### Vignette 22: Session 59 — d_eff = 5 closes at theorem level (patch 0320)

Session 59 closed the d_eff = 5 first-principles channel enumeration at theorem level via icosahedral irrep decomposition. The substrate information transmitted per channel decomposes into icosahedral irreducible representations: $\mathbf{3}_\text{vector}$ (spatial gradient information; 3 channels for the 3 Cartesian axes) $\oplus\, \mathbf{1}$ (ZBW phase; trivial U(1) irrep; 1 channel) $\oplus\, \mathbf{3}_\text{axial}$ (orbital angular-momentum direction; reduced to 1 channel by spin-orbital 2:1 frequency-locking and icosahedral discretization). Channel-completeness verified: no color (singlets), no weak isospin per-channel for free propagation, no flavor for single mass-eigenstate, chirality locked, no separate helicity. Total: $3 + 1 + 1 = 5$. **Picture A axiomatic closure complete.** Findings 9 (foundational vs derived accounting) and 10 (icosahedral irrep cross-sector framework) registered.

### Vignette 23: Session 60 — SF-4 v2.0 SHIPPED (patch 0321)

Session 60 lands the SF-4 v2.0 .tex source revision integrating the Sessions 55–59 closure into the flagship paper. SF-4 advances from v1.0 SHIPPED (Session 54 partial closure) to v2.0 SHIPPED (Session 60 Picture A axiomatic closure achieved). 10 substantive .tex changes: title block + CHANGELOG v2.0 entry, §1.4 closure-status update, §1.5 claim status ledger σ_ν row to CLOSED at theorem level, §4.0 suppression mechanism opening updated, **§4.3.1 Picture A FULL REWRITE** with four sub-claim closures enumerated and boxed eq:sigma_nu_closed, §4.3.4 cross-comparison table v2.0 row added, §4.5 OPEN-FP-SF-4-1 status update with Picture A sub-task RESOLVED + α-exponent residual flagged, §11 OPEN-FP-SF-4-1 closing subsection rewrite, bibliography sf4_picture_A_closure bibitem added. Source: 1974 → 2101 lines. PDF: 40 → 42 pages, 537 → 559 KB. pdflatex two-pass clean.

### Vignette 24: Session 61 — programme-level registration (in progress)

Session 61 is the SHIP-mechanics session for SF-4 v2.0 at the programme level: (i) Research_Frontier.md OPEN-FP-SF-4-1 entry advanced from PARTIAL CLOSURE to ADVANCED; (ii) Research_Frontier.md last-updated header prepended with Sessions 55–60 entry; (iii) paper_catalog.md SF-4 row updated to v2.0 SHIPPED; (iv) handover-SF-4.md (this document's parent) updated to Session 60 v2.0 SHIP close; (v) development-SF-4.md (this file) Vignettes 18–24 added; (vi) transcript-SF-4.md per-session transactions Sessions 55–60 added; (vii) reasoning-SF-4.md Tier 4 reasoning capture pointer to working sketch document added; (viii) INDEX.md sf-4_neutrinos.tex/.pdf rows updated to v2.0 SHIPPED; (ix) flagship_papers/neutrinos/README.md v1.0 → v2.0 transition; (x) flagship_papers/SF-line_development_transcript.md §18 added covering Sessions 55–60. After Session 61, OPEN-FP-SF-4-1 Picture A axiomatic closure is fully RESOLVED at all levels (paper, sketch, documentation suite, programme registries).

---

## Cumulative campaign metrics at v2.0

- **Total sessions**: 24 (Session 37 audit through Session 60 v2.0 SHIP)
- **Total patches**: 27 (0294 audit through 0321 v2.0 SHIP)
- **Source line count**: 0 → 1974 (v1.0) → 2101 (v2.0)
- **PDF page count**: 0 → 32 (v0.5) → 37 (v0.6) → 38 (v0.7) → 40 (v0.8/v0.9/v1.0) → 42 (v2.0)
- **Bibliography**: 12 internal + 10 external + sf4_picture_A_closure (NEW v2.0) = 23 entries
- **Theorems**: 1 conditional (THEO-SF-4-1) + 1 proposition + 1 secondary theorem (registered v1.0); + 4 sub-claim closure theorems (Picture A; pending registry promotion at Session 61)
- **Predictions**: 7 of 8 neutrino-sector parameters at zero free parameters (UNCHANGED from v1.0)
- **Falsifiers**: 5 (UNCHANGED from v1.0)
- **Reviews**: v1.0 had 5 AI passes (ChatGPT × 3 + Grok × 1 + Copilot × 1); v2.0 closure based on internal verification + sketch-document Tier-4 discipline (no external review for v2.0 closure mechanics; AI review TBD post-v2.0 if external reviewers engage)
- **Working sketch document `SF-4_picture_A_axiomatic_closure.md`**: 1106 lines, 13 sections, growing monotonically across Sessions 55–59

---

*Development document continues at Session 60 v2.0 SHIP; Session 61 wraps programme-level registration. Future SF-4 development arc for v2.x revision or for residual α-exponent sub-task closure (post-v2.0) continues in subsequent vignettes appended to this file.*


---

## Vignettes 18-25 — Sessions 55-79 (post-v1.0 SHIP campaigns)

### Vignette 18 — Sessions 55-60: v2.0 Picture A axiomatic closure (patches 0316-0321)

OPEN-FP-SF-4-1 had been registered at v1.0 SHIP as the highest-priority post-ship work: theorem-level closure of the suppression mechanism from CPP axioms A1-A11 (the v1.0 paper achieved structural-physical convergence across three pictures but not axiom-level derivation). The campaign decomposed Picture A into four sub-claims: (a) substrate independence of DI-bit send/receive across the cage boundary; (b) channel coherence as AND-of-factors; (c) equilibrium uniform marginal on DP orientations; (d) channel count d_eff = 5 from icosahedral irrep decomposition. Sessions 55-57 closed sub-claims (a)-(c) via timescale separation κ_1 ≤ 2m/m_P + A6' edge-sector independence + transitive-action uniformity lemma. Sessions 58-59 closed sub-claim (d) via icosahedral irrep decomposition 3_vector ⊕ 1 ⊕ 3_axial|_{spin-orbital-locked}. Session 60 integrated Picture A axiomatic closure into the paper at v2.0 SHIP. The working sketch document `sketches/SF-4_picture_A_axiomatic_closure.md` grew monotonically across the campaign to 1106 lines across 13 sections + 9 findings + close. OPEN-FP-SF-4-1 status: PARTIAL CLOSURE → ADVANCED (Picture A RESOLVED; α-exponent residual remains). The 2% empirical residual was identified as downstream effects (V²-vs-V^(7/3) approximation, K3 partial-binding, O(α_EM) cross-correlations), not Picture A corrections.

### Vignette 19 — Sessions 62-66: v3.0 α-exponent residual closure (patches 0323-0328)

OPEN-FP-SF-4-1's residual sub-task was theorem-level derivation of the α = 2 exponent at the bound/unbound boundary. The bound-mode cage-shell mass formula has α = 7/3; SF-4's unbound-mode formula has α = 2. The V^(1/3) factor must drop out — but why? Sessions 62-65 attacked this via four sub-claim closures: (a) cage cooperation requires rigid cage; (b) unbound 3D orbital ZBW has no rigid cage (per FI-α-3); (c) without anchor → leading two-point SSV correlator vanishes at leading order → per-link energy reduces to bare M₀; (d) bare per-link energy + combinatorial pair count V(V-1)/2 + SM-7 calibration convention → V² scaling. The load-bearing structural element identified: the central CP anchor. Bound modes have a central anchor that creates radially-peaked substrate-information density and shared reference direction → SM-9 §7.2 cascade structure delivers V^(7/3)/N_links per-link amplification. Unbound modes lack the anchor → no cascade → bare M₀ per link → α = 2. Session 65 discharged six verification flags Vα-1 through Vα-6 including Vα-3 antibonding-mode bound refinement. Session 66 integrated α-exponent closure at v3.0 SHIP. The working sketch `sketches/SF-4_alpha_exponent_closure.md` grew to 1184 lines across 13 sections + 9 findings. OPEN-FP-SF-4-1 status: ADVANCED → RESOLVED (all four v1.0 sub-goals at theorem level). Empirical residual decomposition into three sources: (A) α-exponent residual O(1/V²) for bonding modes, O(1/V) for antibonding modes; (B) K3-eigenstructure partial-binding (OPEN-FP-SF-4-2 territory); (C) O(α_EM) cross-channel correlations. ν_2 (V=12, bonding) 1.7% empirical within ≤2.7% bound; ν_3 (V=30, antibonding) 8.3% exceeds (A)+(C) bound by factor ~2, dominated by (B). This identified OPEN-FP-SF-4-2 cross-sector closure as next quantitative-residual-reduction priority.

### Vignette 20 — Sessions 68-72: v4.0 cross-sector closure (patches 0329-0334) — FIRST CROSS-SECTOR CLOSURE IN CPP

OPEN-FP-SF-4-2 (vertex-by-vertex K3-Cage-Shell Consistency at theorem level) had been tied to SM-5's op:nu_id (foundational open problem: K3-eigenmode identification from CPP interaction rules) since v1.0. Each paper's closure depended on the other — standard outcome was both remain conditional indefinitely. Session 68 attacked the joint closure directly via the perturbation analysis: the charged-lepton K3-vertex occupation at V_k breaks K3's S_3 to S_2(V_k) stabilizer. The leading rank-one perturbation ΔH = ε_L|V_k⟩⟨V_k| has zero off-diagonal element in the antibonding subspace because |φ_-^(2)⟩ has zero amplitude on V_1 (Finding β-2). Session 70 §7 closed the basis selection via standard S_3 → S_2 representation-theory branching rule 2|_{S_2} = 1_+ ⊕ 1_- uniquely yielding the TBM-aligned basis (Finding β-6) — this is what closes SM-5's op:nu_id from CPP interaction rules. Session 71 §10 discharged six verification flags Vβ-1 through Vβ-6 and consolidated FI accounting: 6 FIs (FI-K-1 through FI-K-6) all elsewhere-derived from SM-corpus and SF-4 v3.0; 4 CPP axioms (A1+A4+A7+A9, A1+A7+A9 most load-bearing). Session 72 integrated the closure into the paper at v4.0 SHIP as the Composite K3-Cage-Shell Coupling Theorem (Theorem 5.2; THEO-SF-4-5). The working sketch `sketches/SF-4_open_fp_sf_4_2_closure.md` reached 750 lines. Both OPEN-FP-SF-4-2 and SM-5 op:nu_id RESOLVED at conditional theorem closure level via single derivation chain — **first cross-sector closure in CPP**. Methodology registered as Finding β-10: cross-sector entanglement can be turned into structural advantage when the foundational inputs of one closure are sufficiently rich to determine the closure in another sector. The four-session campaign was substantially shorter than the projected effort (which had been comparable to OPEN-FP-SF-4-1) — the cross-sector entanglement that appeared as obstacle turned out to be the structural lever.

### Vignette 21 — Sessions 73-74: programme-level registration + anthology chapter (patches 0334-0335)

Session 73 (patch 0334) registered the v4.0 closure across programme-level documents: `theorem-registry.md` (3 new entries: THEO-SF-4-4, LEMMA-SF-4-1 anticipated, THEO-SF-4-5), `paper_catalog.md` (SF-4 row v3.0 → v4.0), `Research_Frontier.md` (OPEN-FP-SF-4-2 status PARTIAL CLOSURE → RESOLVED + SM-5 op:nu_id status OPEN → RESOLVED cross-sector). The registration was incomplete: theorem-registry.md did not yet receive the formal new entries (deferred to patch 0339). Session 74 (patch 0335) produced the SF-4 anthology chapter "Where Two Problems Met" at ~4630 words in Rovelli/SciAm register across 9 sections. The chapter narrates the cross-sector closure as the year's accumulating progress hitting an inflection point — two papers' open problems closing together via a single derivation chain. The Rovelli register handles the technical substance through accessible analogies (the K3 antibonding doublet as a degenerate pair lifted by external structure; the wavefunction-spread vs symmetry-character readings as two views of the same eigenstate content). Section 8 explicitly addresses what closed and what didn't: the conditional-closure framing is implicit through the FI enumeration ("six foundational inputs all elsewhere-derived").

### Vignette 22 — Session 75: v4.1 ChatGPT v4.0 review incorporation (patch 0336)

ChatGPT v4.0 review verdict: (c) "not yet v1.0 SHIP-ready, residual structural concerns". Six specific structural issues identified, all verified against source: (1) §5.6 "Argument 3" subsection still framed clause (iii) as "inherits SM-5's open problem" — directly contradicted v4.0's Theorem 5.2; (2) §11 cross-sector benefits paragraph stale; (3) Theorem 3.1 sub-claim (c) needed explicit lemma for the A4 → correlator-vanishing step; (4) pair-count normalization "absorbed into M₀" too casual; (5) "overdetermined: two independent arguments" overclaimed (wavefunction-spread + symmetry-character are co-determined by V_1-support/μτ-parity structure); (6) Theorem 5.2 clause (i) overclaimed rank-one perturbation as leading form. Plus 11 additional stale-text spots in §1.3/§1.5/§5.6/§11 that survived Session 72's incomplete v4.0 integration. v4.1 incorporated all 17 items in one patch: NEW Lemma 3.1 (No-Anchor Correlator Vanishing) added to §3.3; Theorem 5.2 clause (i) generalized to "any S_2(V_k)-invariant leading perturbation"; "overdetermined" softened throughout; stale partial-closure language rewritten as historical/superseded; pair-count normalization reframed per SM-7 convention. Specs: 2387 lines source (+91 from v4.0), 51 pages compiled, 623 KB.

### Vignette 23 — Session 76: v4.2 ChatGPT v4.1 review incorporation (patch 0337)

ChatGPT v4.1 review verdict: (b) "v1.0 SHIP-ready after the following 4 specific fixes". Substantial improvement from v4.0's (c) but four calibration items remained: (1) Lemma 3.1 "vanishes" overclaimed (actual content is O(1/V²) suppression); (2) Theorem 5.2 "uniquely / Forced by" too strong (mathematical strength is "structurally selected within the symmetry-preserving perturbative class"); (3) the conditional-vs-full closure distinction needed an explicit Remark — the paper's "RESOLVED" statements could be misread as full derivational closure when the actual claim is conditional; (4) selective terminology sweep needed for "RESOLVED" statements where conflation could occur. v4.2 incorporated all four: Lemma 3.1 renamed "Vanishing" → "Suppression" with statement matching actual proof strength; Theorem 5.2 clause (i) rewritten with explicit uniqueness scope; NEW Remark `rem:conditional_closure` added after the Composite Theorem in §5.7 making the conditional-closure framing explicit globally; selective qualifier additions in §1.4 abstract, §11 sec:open_fp_sf42 header, §11 forward roadmap. The new Remark is the canonical paper-level instantiation of what later (patch 0340) becomes programme convention. Specs: 2442 lines source (+55), TEX-ONLY per new workflow.

### Vignette 24 — Session 77: v4.3 ChatGPT v4.2 review incorporation (patch 0338); ChatGPT verdict (a) ACHIEVED

ChatGPT v4.2 review verdict: (b) "v1.0 SHIP-ready after the following 3 specific fixes". Three residual stale-text spots in §1.3/§1.4/§1.5 that survived the v4.0/v4.1/v4.2 cleanup waves: (1) §1.3 "Inherits as open" bullet still listed SM-5's K3-eigenmode-identification ansatz — but that's now resolved cross-sector at v4.0; (2) §1.4 K3-Cage-Shell deliverable still said "at SM-5-inheritance level" with "SM-5-ansatzed TBM-direction selection" — pre-v4.0 language; (3) §1.5 "full RESOLUTION" wording for OPEN-FP-SF-4-1 (v3.0) and OPEN-FP-SF-4-2 (v4.0) conflicted with the new global conditional-closure remark. v4.3 incorporated all three: §1.3 bullet split into (a) op:nu_id conditionally resolved at v4.0 + (b) OP-SM-7d still legitimately inherits-as-open; §1.4 deliverable updated to "Composite Theorem at conditional theorem-closure level"; §1.5 "full RESOLUTION" → "conditional theorem-level resolution" with explicit cross-references to rem:conditional_closure. Specs: 2503 lines source (+61). **ChatGPT v4.3 review verdict: (a) "v1.0 SHIP-ready, no further substantive edits required."** SF-4 v4.3 is SHIP-ready as a conditional theorem closure paper.

### Vignette 25 — Sessions 78-79: programme-level closeout (patches 0339-0340)

Session 78 (patch 0339) consolidated the v4.3 SHIP-ready state into programme-level registers: theorem-registry.md updated with THEO-SF-4-1 status upgrade + NEW THEO-SF-4-4 + NEW LEMMA-SF-4-1 + NEW THEO-SF-4-5 (catching up four sessions of registry drift across v3.0/v4.0/v4.1); master_glossary.md gained 8 new entries in the v4.x conditional-closure framework section; paper_catalog.md SF-4 row updated v4.0 → v4.3 SHIP-ready; anthology chapter §8 close updated to reference v4.3 + four-cycle review trajectory + explicit conditional-closure framing. Plus NEW `scripts/cpp-recompile-pdf.sh` shell script and new section in `templates/operating_system.md` documenting the Binary Artifact Workflow adopted after patch 0336's cross-machine .pdf blob friction. Session 79 (patch 0340) added two programme-level methodology documents: NEW `templates/conditional_closure_framework.md` (170 lines) generalizing SF-4 v4.2's Remark `rem:conditional_closure` to programme convention; NEW `theorem-dependency-graph.md` (120 lines) mapping inheritance relationships between all formal mathematical objects in the programme. Both documents are programme-load-bearing references but introduce no new mathematical content. The methodological observation registered: the conditional-closure framework crystallized at SF-4 v4.2 in response to external review pressure — methodological conventions tend to crystallize at specific friction points rather than being designed up-front.

---

**Closing observation across vignettes 18-25.** SF-4's post-v1.0 trajectory ran approximately 25 sessions across three closure campaigns + four review cycles + two closeout patches. The cage-shell mass formula advanced from PARTIAL CLOSURE (v1.0) through ADVANCED (v2.0) through fully RESOLVED OPEN-FP-SF-4-1 (v3.0) through cross-sector closure of OPEN-FP-SF-4-2 + SM-5 op:nu_id (v4.0) through proof-strength calibration (v4.1) through conditional-closure framing (v4.2) through final consistency sweep (v4.3) through programme-level registers freeze (v4.3 closeout, patches 0339-0340). The four-cycle ChatGPT review trajectory (c)→(b)→(b)→(a) was a methodological lesson in itself: external review at scale identifies the conditional-vs-full closure distinction as the critical interpretive lens, and that distinction is now codified at programme level for future flagship papers.
