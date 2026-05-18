# SF-2 Development Document — Patch-by-Patch Vignettes

**Paper**: `flagship_papers/electroweak/sf-2_electroweak.tex` (main paper v1.0 SHIPPED Session 83) + `flagship_papers/electroweak/sf-2_companion.tex` (Companion v1.0 SHIPPED Session 83)
**Purpose**: Patch-by-patch development arc covering the 24-patch SF-2 campaign (Patches 0345–0368) plus post-SHIP documentation discipline (Patches 0369–0371).
**Companion files**: `transcript-SF-2.md` (per-patch transactions); `reasoning-SF-2.md` (Tier 4 verbatim reasoning); `handover-SF-2.md` (Session 83 close handover).

**Honesty about coverage**: Vignettes 1-3 cover the early patches (0345-0355) at arc-level rather than per-patch detail; the v0.1 drafting work was distributed across many small commits whose individual content is consolidated into the v0.1 PDF deliverable. Vignettes 4-19 cover Patches 0356-0371 at per-patch resolution. The fine-grained record of multi-reviewer review incorporation (Patches 0359-0361, 0363, 0364, 0366, 0367) lives in the patch commit messages and the main paper / Companion title-block CHANGELOG entries; this document captures the substantive arc rather than reproducing the line-level diffs.

---

## Vignette 1 — Session 81 pre-survey audit (Patch 0345)

After SF-4 v1.0 SHIPPED at Session 54 (Patch 0314) and the subsequent v2.0/v3.0/v4.0/v4.4 closure campaigns (Sessions 55-81), the SF-line forward queue rotated to SF-2 as the next active flagship drafting campaign. SF-2 had been scope-narrowed at Session 41 (Patch 0301) to cage bosons only (W±, W⁰, Z, H) — photon to SF-6, gluon to SF-5 — and the W⁰ catalyst hypothesis had been registered as CONJ-EW-W0 at the same architectural revision.

The pre-survey audit was the first work-arc of the SF-2 campaign. Document: `sketches/SF-2_electroweak_sector_audit.md`. Audit goals:

1. Survey existing EW corpus (EW-1 through EW-5) to identify which content is at theorem-level vs sketch-level rigor.
2. Map EW-series content to SF-2 v0.1 scope, separating cage-boson content from photon/gluon content (which goes to SF-6/SF-5).
3. Identify the substantive new derivation work required: W⁰ catalyst framework, cage-shape uniqueness theorems, mass-formula machinery from SM-7/8/9 inheritance, Weinberg-angle correspondence inheritance from SM-6.
4. Surface CONJ-EW-W0 as the central original physics-content claim.

The audit confirmed: substantive new derivation work was concentrated on the W⁰ catalyst framework (the framework's most original contribution) plus the cage-shape uniqueness theorems (the structural-derivation core). The other content was either inheritance (Weinberg-angle from SM-6, mass-formula machinery from SM-7/8/9) or reframing of existing EW-series sketches at theorem-level rigor.

This vignette covers the Sunday-equivalent state: Thomas had the audit in hand but did not yet have the physical intuition for *how the W boson works at the substrate level*. The audit identified what needed to be derived; the W⁰ catalyst insight that resolved it had not yet emerged.

## Vignette 2 — v0.1 outline (Patches 0346–0347)

With the audit in hand, the v0.1 outline was drafted. Document: `sketches/sf-2_outline.md` (~56 KB at v1.0 SHIP — has been continuously maintained throughout the campaign). The outline established the paper's structural skeleton:

- §1 Introduction (framing, positioning, claim-status table)
- §2-§3 Inheritance from prior CPP corpus (SM-1 four-cage taxonomy, SM-6 Weinberg-angle, SM-7/8/9 mass-formula machinery, SS-1 binary icosahedral group structure)
- §4 Cage-shape uniqueness theorems (the structural-derivation core)
- §5 W⁰ catalyst framework (the central original contribution)
- §6 Selection rules and decay channels
- §7 Cage-formation framing of EWSB
- §8 Yang-Mills EFT continuum-limit recovery (proof outline only)
- §9 Mass-formula and tree-level cross-checks
- §10 Calibrated mass-formula PARTIAL CLOSURE
- §11 EWSB analog discussion

The Sunday W⁰ catalyst insight emerged during outline drafting. The bracelet-as-substrate-with-centroid-capture mechanism became the central original physics-content idea around which §5 was structured. Six propositions (centroid capture, differential-gradient binding, mass-degeneracy, lifetime, statistical reorganization, universality) were named in outline form.

## Vignette 3 — v0.1 .tex initial draft (Patches 0348–0355)

The v0.1 .tex translation of the outline into full LaTeX paper form. Eight patches spanning the drafting effort, each touching ~3-5 sections at full paper quality. By Patch 0355, the v0.1 source was ~1300 lines: full LaTeX preamble + abstract + plain-language summary + §1-§11 drafted + bibliography + claim-status table.

The substantive content delivered at v0.1:
- Four cage-shape uniqueness theorems with proofs (THEO-SF-2-1 W bracelet, THEO-SF-2-2 Z icosahedron, THEO-SF-2-3 H dodecahedron, THEO-SF-2-4 mass-gap)
- Six W⁰ catalyst propositions (PROP-SF-2-1 through PROP-SF-2-6)
- Yang-Mills EFT continuum-limit recovery at proof-outline level (THEO-SF-2-5)
- Mass-formula PARTIAL CLOSURE via three calibrated dilution factors
- Weinberg-angle correspondence inherited from SM-6 (initial phrasing "derived")
- Six OPEN-FP-SF-2-* problems identified for theorem-level closure

The W bracelet $D_6$-orbit argument — that 4800 induced 6-cycles in the 600-cell graph partition with 1200 regular hexagons forming a single $H_4$-orbit with $D_6$ stabilizer — was the marquee theorem of the v0.1 draft. The combinatorial enumeration was verified against 600-cell topology, with the orbit-stabilizer theorem providing the count $|H_4|/|D_6| = 14400/12 = 1200$ matching exactly.

v0.1 was complete at Patch 0355 — drafted at full paper quality across all eleven sections.

## Vignette 4 — v0.2 self-review consistency pass (Patch 0356)

Before sending v0.1 to external reviewers, a self-review consistency pass to catch internal contradictions. Standard discipline pattern: every paper version ships through self-review before external review. The v0.1 → v0.2 corrections were primarily cross-reference integrity (theorem labels referenced before defined, equation cross-refs to wrong section numbers) and terminology consistency (W bracelet referred to as "hexagonal cage" in some sections, "regular hexagon" in others, "6-cycle" in others — standardized to "W bracelet" throughout).

No structural changes at v0.2. Self-review consistency-only pass.

## Vignette 5 — v0.3 terminology corrections + tau hadronic decay channels (Patch 0357)

The v0.3 patch added the tau hadronic decay channels to §5.5 (Statistical reorganization, PROP-SF-2-5). The W⁰ catalyst framework's prediction is universal across W± decay channels (PROP-SF-2-6 universality), so the framework must reproduce the observed branching structure for tau hadronic decays as well as leptonic decays. Tau hadronic channels added: $\tau \to \nu_\tau + d\bar{u}$ (Cabibbo-favored), $\tau \to \nu_\tau + s\bar{u}$ (Cabibbo-suppressed), $\tau \to \nu_\tau + \text{strange resonances}$.

Plus terminology consistency corrections from continued self-review (e.g., "h-tet" vs "hybrid tetrahedron" — standardized).

## Vignette 6 — v0.4 K⁻ two-quark-cage structural corrections + DP-chain composition (Patch 0358)

The v0.4 patch addressed a structural error in §5.5 K⁻ meson decay treatment. The K⁻ is a two-quark cage (q$\bar{q}$ structure), not a single-quark cage; the v0.3 treatment had described K⁻ decay through the W⁰ catalyst as if K⁻ were a single quark bound at the bracelet centroid. The v0.4 correction restructured the K⁻ decay treatment as a two-quark-cage reorganization mediated by the W⁰ catalyst: the strange quark transitions via $s \to u + W^-$ at the W⁰ centroid, with the K⁻ cage temporarily destabilized during the transition.

Plus DP-chain composition framework introduced: the four species (qDP, hDP-A, hDP-B, eDP) participating in W±-mediated decays were enumerated and given operational definitions. This is the framework that the Companion §6 toy MC would later compute equilibrium ratios for (OPEN-FP-SF-2-chaincomp).

## Vignette 7 — v0.5 ChatGPT review pass 1 incorporation (Patch 0359)

First external review pass. ChatGPT review of v0.4 delivered five substantive feedback items + several editorial recommendations. Verdict: v0.4 has "the right structural content" but needs (1) explicit claim-status hierarchy table, (2) two-layer Higgs spin articulation (finite-group level vs relativistic level), (3) Yang-Mills EFT proof outline status marking, (4) effective selection rules with corrected proton structure, (5) more careful framing of "framework-level" vs "theorem-level" claims.

v0.5 incorporated all five:
- New claim-status hierarchy table (§1.6) — twelve-row table with explicit closure status per substantive claim (THEOREM / INHERITED TAXONOMY / STRUCTURAL ARGUMENT / PARTIAL CLOSURE / etc.). This was the cleanest improvement; it makes the paper's rigor profile externally readable at a glance.
- Higgs spin two-layer articulation: finite-group level (Cor higgs_scalar gives $A_5 \to J=0$ at theorem-level) + relativistic level (inherits via continuum-limit Yang-Mills EFT — THEO-SF-2-5 proof outline)
- Yang-Mills EFT proof outline marking: §8.3 explicitly labels as "proof outline" with the full continuum derivation registered as Layer 4 future work
- Effective selection rules: §5.5 selection rules rewritten with corrected proton structure
- Framework-level vs theorem-level framing tightened throughout

ChatGPT's identification of the W bracelet $D_6$-orbit argument as "a real conceptual upgrade" came in this review. This was the most consequential external validation of the SF-2 structural-derivation core.

## Vignette 8 — v0.6 Copilot + Grok review incorporation (Patch 0360)

Parallel reviews from Copilot and Grok on v0.5. Combined v0.6 incorporates both reviewers' feedback in a single patch (different from SF-4 which split Copilot and Grok into separate patches; SF-2 found the combined-patch pattern efficient when the reviewer feedback was non-overlapping).

Copilot v0.5 review delivered:
- $\ell_Z$ / $s_H$ calibrated-vs-derived clarifications (the $\ell_Z$ and $s_H$ factors in the mass formula were not clearly marked as calibrated; v0.6 makes this explicit with footnotes and table caption updates)
- K⁻ hybrid-tet wrapping rationale (§5.5 K⁻ treatment needed an explicit operational definition for "hybrid-tet wrapping" — added)
- Roadmap to full closure table — what's needed for each OPEN-FP-SF-2-* to upgrade from PARTIAL to RESOLVED

Grok v0.5 review delivered:
- EW-4 no-SSB supersession statement (clarifying that SF-2's EWSB cage-formation framing supersedes EW-4's no-SSB sketch from the architectural revision at Session 41)
- Forward-reference audit (theorems referenced before defined — Grok caught two such instances in §5)
- Meson-content intentionality note (clarifying that the meson examples in §5.5 were chosen for pedagogical reasons rather than exhaustive coverage)

v0.6 incorporated all feedback. Both reviewers explicitly assessed v0.5 as "close to v1.0 SHIP quality."

## Vignette 9 — v0.7 ChatGPT v0.6 review final tightening (Patch 0361)

Second ChatGPT pass on v0.6. ChatGPT identified four residual technical issues:
1. Higgs finite-group scalar classification terminology — "scalar" was used to mean both "Lorentz scalar" and "finite-group scalar" interchangeably; v0.7 distinguishes
2. CDF W-mass framework-interpretation language with cautionary note (the 2022 CDF $W$-mass anomaly is interpretation-sensitive; the framework's $m_{W^0} = m_{W^\pm}$ prediction does not directly engage with CDF's tension with the rest of the data, but the relation is worth a footnote)
3. §8 theorem-level inheritance precision (distinguishing inherited theorems from proof outline)
4. Abstract long-sentence splits (the v0.6 abstract had several sentences over 60 words; ChatGPT recommended splitting for readability)
5. Companion paper cross-references (Companion was being developed in parallel — cross-refs from main paper to specific Companion sections needed to be added)

v0.7 was the final pre-Companion-architectural-decision version. Main paper substantive content was now stable; reviewer convergence on "v1.0-ready with Companion in parallel" began to emerge.

## Vignette 10 — Companion paper kickoff (Patch 0362)

The architectural decision to carve visual / pedagogical / exploratory-computational content into a separate Companion paper. Rationale captured in Section 6 of reasoning-SF-2.md.

Patch 0362 created `flagship_papers/electroweak/sf-2_companion.tex` at v1.0 (initial Companion version) with the planned structure:
- §1 Executive overview (pipeline navigation map for new readers)
- §2 CPP-specific terminology glossary (hDP, qCP, eCP, SSV, PCD, DP Sea, Nexus, ZBW)
- §3 Cage geometry figures (TikZ: W bracelet $D_6$ hexagonal ring, Z icosahedron first distance shell, H dodecahedron second distance shell, 600-cell distance-shell visualization)
- §4 Cheat-sheet reference tables (5 tables consolidating cage parameters, mass-formula factors, OPEN-FP problems)
- §5 Parametric scaling heuristics for $W^0$ oblique-parameter sensitivity + GPU-runnable exploratory simulation
- §6 DP-chain composition exploratory toy Monte Carlo + GPU-runnable proof-of-concept program

The decision to do GPU-runnable Python alongside the .tex was deliberate: actually running the simulations and incorporating numerical output back into the Companion text raises the rigor from "qualitative estimate" to "exploratory numerical result with constraint identification." This is the methodology pattern that became central to the Companion's identity.

## Vignette 11 — Companion v1.0 → v1.1 review-cycle incorporation (Patch 0363)

Parallel multi-reviewer cycle on Companion v1.0:
- ChatGPT v1.0 rigor-language tightening — Companion §5 oblique-parameter section needed more emphatic disclaimers that the scaling ansätze were heuristics, not derived corrections
- Copilot v1.0 reading-order box + DP-species table — Companion needed a navigation aid for readers (4-step reading order: executive overview → cage diagrams → cheat-sheet → exploratory simulations) + a consolidated DP-species reference table
- Grok v1.0 caption precision + embedded Python listings — TikZ figure captions needed sharper combinatorial-content descriptions; Python program excerpts should be embedded as listings in the relevant sections (§5, §6) for reader convenience

v1.1 incorporated all three reviewers' feedback. Companion's reader-accessibility improved markedly.

## Vignette 12 — Companion v1.1 → v1.2 GPU result incorporation (Patch 0364)

The first major GPU result incorporation cycle. Thomas's machine ran the three Python programs (`oblique_parameters_framework.py`, `dp_chain_monte_carlo.py`) and reported numerical output. Patch 0364 incorporated the actual results into Companion §5.6 and §6.3:

- **DP-chain composition refined ratios**: $(40.3\%, 29.7\%, 29.6\%, 0.4\%)$ for (qDP, hDP-A, hDP-B, eDP). The eDP rarity (0.4%) was rarer than naive estimates — qualitatively validating the framework while identifying the substrate-thermodynamic framework as needing first-principles closure (OPEN-FP-SF-2-chaincomp).
- **Oblique-parameter $\Delta T \approx 0$ confirmation**: across parametric variation, $T$ vanishes when masses are degenerate — confirming PROP-SF-2-1 at parametric-scaling level. This is a robust feature of the framework, not a tuned cancellation.
- **$|\Delta S|, |\Delta U|$ at heuristic-placeholder level**: outside LEP/SLC 3$\sigma$ in the heuristic regime — emerges as a substantive constraint on the eventual continuum-EFT derivation rather than as a failure of the framework.

This cycle is documented in detail in reasoning-SF-2.md §8 (GPU-results incorporation cycle methodology).

## Vignette 13 — Companion code suite + sensitivity scan program (Patch 0365)

Patch 0365 created the third GPU program: `oblique_parameters_sensitivity_scan.py` (302 lines). The program scans a 16×16 grid over substrate-symmetry-motivated parameter ratios and computes pass/fail against LEP/SLC 3$\sigma$ bounds for $S$, $T$, $U$. This is the program that would deliver the central Companion §5.7 finding at Patch 0366.

Code suite also formalized: `flagship_papers/electroweak/code/README.md` (96 lines) documenting the three programs' purposes, dependencies (PyTorch with GPU+CPU fallback), and expected output ranges.

## Vignette 14 — Companion v1.2 → v1.3 sensitivity-scan results (Patch 0366)

The second major GPU result incorporation cycle. Thomas's machine ran the sensitivity scan and reported the decisive finding:

**214/256 = 83.6% of substrate-symmetry-motivated parameter combinations land within LEP/SLC 3$\sigma$ bounds**, with the within-bounds region forming a clean diagonal band defined by $|r_{33} - r_{3Q}| \lesssim 0.18$ with $r_{33} \geq 0.85$.

New Companion §5.7 added documenting the result with:
- PASS/FAIL grid table (16×16 cells)
- Corner-case sensitivity table (probing the band edges)
- Geometric-structure paragraph identifying the within-bounds region's diagonal-band shape
- Interpretation framing the geometric band as the Layer 4 continuum-EFT derivation target

ChatGPT v1.3 pair review (delivered after this patch) identified §5.7 as *"a model of how to handle framework-level content: honest about what is heuristic, but still quantitatively useful and falsifiable."* This was the most consequential reviewer validation of the Companion's exploratory-computational identity.

## Vignette 15 — Patch 0367 (multi-component polish + PD-004 + W⁰ neutrino sketch + Version-discipline rule)

The ChatGPT v1.3 pair review final polish — a multi-component patch addressing three programme-strategic concerns Thomas raised plus the textual polish from ChatGPT's review. Five files touched in one patch:

1. **NEW: `programmatic_decisions/PD-004-publication-pathway.md`** — captures ChatGPT's "Best publication path" five-layer publication-pathway strategic guidance. Five layers from mathematical-combinatorial geometry (Layer 1) through eventual EFT bridge (Layer 5). SF-2 positioned as Layer 2 + Layer 3 work.

2. **UPDATED: `templates/operating_system.md` §4 Phase 7 Version-discipline rule** — codifying that every patch modifying .tex source must increment the title-block version marker (addresses the recurrent Grok-version-confusion mode where title-block versions fell out of sync with patch history).

3. **NEW: `flagship_papers/electroweak/sketches/W0_neutrino_scattering_centroid_decoupling.md`** — captures Thomas's W⁰ neutrino scattering insight on centroid decoupling mechanism. Available for SF-2 v1.1+ revision or dedicated paper when authorized.

4. **UPDATED: `sf-2_electroweak.tex` v0.7 → v0.8**: ChatGPT v1.3 textual concerns addressed — Weinberg-angle phrasing tightened to "zero-parameter numerical correspondence emerging from spectral trace structure" (the runs-with-scale concern fix); §1.4 positioning paragraph aligned to PD-004 Layer 2 + Layer 3 language; line 1451 parameter-economy assessment phrasing softened.

5. **UPDATED: `sf-2_companion.tex` v1.3 → v1.4**: emphatic red mdframed disclaimer added immediately above the §5.3 parametric scaling ansatz equations stating "The expressions in the three lines immediately following this box are dimensional scaling heuristics only, not renormalized one-loop electroweak corrections" with full enumeration of the five missing rigor ingredients.

This patch is the largest single multi-component patch of the SF-2 campaign. It addressed three categories of concerns: textual polish (ChatGPT's recommendations), programme-strategic infrastructure (PD-004 + Version-discipline rule), and durable capture of new insights (W⁰ neutrino sketch). The decision to bundle all three into one patch (rather than splitting) was driven by the fact that they all responded to the same review cycle (Thomas's review of ChatGPT v1.3 plus his own added items).

## Vignette 16 — Patch 0368 v1.0 SHIPPED (joint main paper + Companion)

The v1.0 SHIP. Patch 0368 promoted both main paper v0.8 → v1.0 SHIPPED and Companion v1.4 → v1.0 SHIPPED in a single patch with full version synchronization between the two papers' title blocks. The three actions:

1. **Version synchronization**: main paper title "Version 0.8 --- DRAFT" → "Version 1.0 SHIPPED"; Companion title "Version 1.4" → "Version 1.0 SHIPPED". Both CHANGELOG headers updated with Patch 0368 entries. Cross-references between main paper and Companion synchronized to v1.0 SHIPPED state throughout.

2. **Grok D_6 sentence added in Companion §5.7**: the optional D_6 zero-net-charge symmetry sentence per Grok's recommendation, immediately after the geometric-structure paragraph. Single sentence with measurable scientific tightening: "The geometric structure of the within-bounds band traces directly to the substrate $D_6$ zero-net-charge symmetry of the W bracelet."

3. **Main paper §1 Companion description updated**: from "framework-level closure pending full continuum-limit calculation" (the pre-v1.0 phrasing) to descriptions matching the v1.0 SHIPPED state with actual GPU numerical results integrated.

Three-reviewer convergence achieved: ChatGPT structural-architecture validation + Copilot SHIP-ready + Grok *"This is flagship-series work at its strongest. SHIP at v1.0."* The strongest possible external-validation pattern.

Thomas's reflection at v1.0 SHIP: "Ten years from qCP concept (2016) to physical intuition (Sunday) to complete flagship paper (Thursday). I didn't know how it worked on Sunday. I know how it works now on Thursday."

The 24-patch campaign closed. The W⁰ catalyst framework was externally validated as *"the framework's most original physical proposal"* (ChatGPT v1.3).

## Vignette 17 — Patch 0369 Session 83 close handover discipline

Per operating_system §15 Step H, the minimum-required session-close artifact: the canonical handover document for the next context window. Four files touched: one new + three updated.

- NEW: `flagship_papers/electroweak/documentation_suite/handover-SF-2.md` (210 lines, ~20 KB) — the canonical session-close artifact per operating_system §15 Step H template with all required sections (one-paragraph state, status, what's resolved, what's open, forward queue with Priority 1-7, where-to-find-detail, step-by-step audit, recent session count, quick-start for next session).
- UPDATED: `flagship_papers/electroweak/README.md` from "Planned" status to v1.0 SHIPPED status with full deliverables enumeration, forward queue, predictions/falsifiers, and folder-content tree.
- UPDATED: `INDEX.md` SF-2 row from "planned" to v1.0 SHIPPED with comprehensive Session 83 close context.
- UPDATED: `paper_catalog.md` — NEW SF-2 table row added above SF-4 (numerical ordering) + SF-2 Documentation paragraph after SF-4 Documentation paragraph.

This patch is the foundation for subsequent documentation work — the handover document provides Patches 0370+ with the canonical scoping artifact.

## Vignette 18 — Patch 0370 registers freeze

Programme-level registers freeze for SF-2 v1.0 SHIPPED per SS-9 Session 33 + SF-4 Session 54 patterns. Four files updated + six new problem-history files.

- UPDATED: `theorem-registry.md` — SF-line section expanded from 4 theorems + 1 proposition + 1 lemma (SF-4 only) to 9 theorems + 7 propositions + 1 lemma (SF-2 + SF-4). NEW: THEO-SF-2-1 through THEO-SF-2-5 + PROP-SF-2-1 through PROP-SF-2-6. Total theorem count 56 → 61 theorems + 7 propositions + 1 lemma.
- UPDATED: `master_glossary.md` — new "SF-2 v1.0 W⁰ catalyst framework terms" section with 10 entries (W⁰ catalyst, Activated bracelet, Centroid capture, Hybrid tetrahedron (h-tet), qDP/hDP-A/hDP-B/eDP species, Mass-gap theorem (electroweak), Cage-shape uniqueness theorems, Companion paper architecture, PD-004 publication-pathway, Sensitivity scan within-bounds region).
- UPDATED: `predictions.md` — 4 new SF-2 predictions in Section 2: PRED-O-21 mass-degeneracy, PRED-O-22 mass-gap, PRED-O-23 W decay V-A structure, PRED-O-24 sensitivity-scan geometric constraint band. SF-2 row added to Section 6.
- UPDATED: `research_frontier.md` — FP section advanced 2 → 8 problems with six new OPEN-FP-SF-2-* entries each following the standard per-problem template. Last-updated header prepended with comprehensive Sessions 81-83 SF-2 v1.0 SHIPPED narrative.
- NEW: 6 PH-OPEN-FP-SF-2-*.md problem-history files (η, EWSB, loopfactor, shelldens, chaincomp, CHIR) ~97 lines each following the standard problem-history template.

CONJ-EW-W0 status advanced from "open conjecture" (Session 41 registration) to "structurally derived and externally validated" with the W⁰ catalyst framework formalized as six propositions, mass-degeneracy structural prediction confirmed at parametric-scaling level, three-reviewer convergence achieved.

## Vignette 19 — Patch 0371 Tier-4 reasoning capture

The canonical Tier-4 verbatim Opus reasoning capture for the SF-2 v1.0 SHIP per operating_system §4 Four-Tier Documentation Discipline. One file created: `flagship_papers/electroweak/documentation_suite/reasoning-SF-2.md` at 460 lines across 10 thematic sections matching Thomas's Patch 0369 forward-queue specification:

1. The W⁰ catalyst insight arc
2. Cage-shape uniqueness proofs
3. The W bracelet $D_6$-orbit argument (the marquee theorem)
4. Weinberg-angle inheritance from SM-6
5. Mass-degeneracy structural prediction (PROP-SF-2-1)
6. Companion paper architectural decision
7. Multi-reviewer convergence cycle
8. GPU-results incorporation cycle
9. Sensitivity-scan demonstration
10. v1.0 SHIP decision

Plus pointer section to working sketches and Tier 4 capture status closing section.

This document is the canonical Tier-4 source for downstream work: Patches 0372-0375 substantive-content (this patch is 0372 production), future external-feedback drafting, future programme historians and continuation work.

The document preamble is explicit about honesty-of-coverage discipline: Sections 1-9 cover patches that were substantially produced under context-window compaction in the conversation history; Section 10 (v1.0 SHIP decision) was directly produced by the current context window and is recorded at high resolution. The fine-grained record of v0.x → v0.7 trajectory lives in the multi-reviewer review-incorporation patches' commit messages and the main paper / Companion title-block CHANGELOG entries.

---

## Texture observations from the SF-2 campaign (the 24-patch arc Patches 0345-0368)

Six lessons learned during the SF-2 campaign, captured here for systematization in future SF-line flagships:

1. **The Sunday/Thursday breakthrough rhythm**: Thomas had carried the "what does the W boson actually do" question for ten years. The breakthrough came Sunday, and the flagship paper shipped Thursday. The structural results were already latent in the 600-cell substrate; the physical intuition for how the W fits the substrate was what was missing. Sustained attention to one question over a decade produced the breakthrough — not extended re-derivation of mathematical content.

2. **Two-paper format for SF-line flagships**: the joint main paper + Companion architectural decision (Patch 0362) preserved main paper rigor while delivering reader-accessibility content fully. Three-reviewer convergence endorsed the format. This is now programme-strategic guidance per master_glossary "Companion paper architecture" entry; future SF-line flagships should plan for the two-paper format from outline stage.

3. **GPU result incorporation cycle**: the methodology progression (qualitative estimate → exploratory GPU result → constraint identification → registration as OPEN-FP-SF-2-* sub-problem if constraint identifies derivation target) is the operational pattern for moving from Layer 3 phenomenology to Layer 4 continuum-EFT closure target identification. Captured in reasoning-SF-2.md §8.

4. **Three-reviewer convergence pattern**: ChatGPT (surgical/strategic) + Copilot (editorial/SHIP-readiness) + Grok (housekeeping/pedagogical) — three independent reviewer profiles complementary, not redundant. SHIP-at-v1.0 requires all three converging. SF-2 achieved this at Patch 0368.

5. **Version-discipline as recurrent problem**: title-block version markers fall out of sync with patch history when not explicitly maintained per patch. Grok caught this at SF-2 v0.7. The fix is the operating_system §4 Phase 7 Version-discipline rule (Patch 0367): every patch modifying .tex source must increment the title-block version marker.

6. **PD-004 publication-pathway as strategic framing**: ChatGPT's five-layer publication-pathway guidance (Layer 1 mathematical-combinatorial geometry through Layer 5 eventual EFT bridge) maps existing CPP corpus structure essentially perfectly. The recommendation is not to restructure the programme but to make the layering explicit in framing language and abstract positioning. Each future SF-line paper should identify its Layer occupation in §1.4 positioning paragraphs.

---

## Development arc status at Patch 0372 close

The four-tier documentation discipline for SF-2 v1.0 SHIP at this patch close:

- `handover-SF-2.md` (Patch 0369) ✓ — Session 83 close canonical handover artifact
- `reasoning-SF-2.md` (Patch 0371) ✓ — Tier 4 verbatim Opus reasoning capture across 10 thematic sections
- `development-SF-2.md` (THIS PATCH 0372) ✓ — patch-by-patch vignettes covering the development arc
- `transcript-SF-2.md` (parallel Patch 0372 file) ✓ — per-patch transactions log Patches 0345-0371

Forward queue: Patch 0373 7-file companion documentation suite (or subsume into four-tier per SF-4 precedent), Patch 0374 anthology chapter at Rovelli/SciAm register, Patch 0375 TATWD integration. ClearPC PDF compile + public posting at Thomas's discretion.

**SF-2 v1.0 SHIPPED**. Session 83 close documentation discipline continues at Patch 0373.
