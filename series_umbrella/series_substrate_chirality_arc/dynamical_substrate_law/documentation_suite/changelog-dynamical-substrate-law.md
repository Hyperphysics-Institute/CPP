# Changelog: F.1 Dynamical Substrate Law flagship paper

**Paper**: The Dynamical Substrate Law: Substrate-Locality of DI-Bit Currents at Vertex-Aligned Reading C in the 600-Cell
**Source**: `flagship_papers/dynamical_substrate_law/dynamical_substrate_law.tex`
**Programme registration**: THEO-DSL-1 + THEO-DSL-2 + THEO-DSL-3 candidate IDs (Session 142 Patch 0570 v1.0 SHIP; theorem-registry update DEFERRED to Phase 7B Patch 0573-ish per handover §6 Step E)
**OPEN-SD-CHIR-PRIMITIVE manifestation (iv) status at registration**: CLOSED at sketch-document Layer 3 via Theorem 7.1 substrate-locality umbrella. Trio inputs (Theorems 5.1 + 5.2 + 6.1 + Corollary 6.2) at publication-grade Layer 3; umbrella itself at sketch-document Layer 3 with explicit anti-erasure of Layer distinction per ChatGPT R1-R6 convergent guidance.
**F.1 sub-question status at registration**: SHIPPED at v1.0 with strongest-positive cross-reviewer convergent verdict (Grok R1 explicit + Copilot R1 implicit + ChatGPT R6 strongest-positive). The question *"Does CPP imply substrate-locality of DI-bit currents at vertex-aligned Reading C?"* has its v1.0 SHIPPED answer at the post-Patch-0570 `.tex` source + frozen PDF.
**Maintainer**: Thomas Lee Abshier ND, Hyperphysics Institute

This file is the canonical version archaeology for the F.1 Dynamical Substrate Law flagship paper. Each `dynamical_substrate_law.tex` patch updating the paper source adds an entry below. Substantive detail lives in the patch commit messages, the Tier 4 reasoning file `reasoning-dynamical-substrate-law.md`, and the per-transaction lab-notebook entries in `transcript-dynamical-substrate-law.md` and `development-dynamical-substrate-law.md`; this file is the curated narrative for researchers tracing the closure trajectory.

The `.tex` source itself carries the v1.0 SHIP CHANGELOG comment block at the head of the file (lines ~13–90) preserved at v1.0 for archival completeness. Subsequent patches will update this `.md` file as the canonical version archaeology per the convention codified Patch 0408 (Session 115) + Patch 0409 (Session 116); programme-internal version archaeology belongs alongside development/transcript/reasoning files in the documentation suite, not solely in the paper source.

This is **F.1, the first F-line flagship v1.0 SHIP in CPP corpus history.** The Capotauro paper at `flagship_papers/capotauro/capotauro.tex` was the precedent flagship trajectory for the F-line framework (Capotauro v2.0 v1.0 SHIPPED at Session 135 Patch 0479, 19 May 2026); F.1 is the first paper in the F-line flagship series proper.

---

## Post-v1.0 SHIP — Hardened-theorem artifact additions

### Patch 0571 — 25 May 2026 (Session 143): G1 publication-grade hardening (OPEN-FP-F1-3 RESOLVED)

**OPEN-FP-F1-3 RESOLVED.** First post-v1.0-SHIP substantive physics Patch on the F.1 trajectory, executed per ChatGPT R1–R6 + Copilot R1 convergent verdict that G1 publication-grade hardening was the "single highest-value next action" after v1.0 SHIP. The patch adds the fourth and final F.1 Layer 3 hardened-theorem artifact at `flagship_papers/dynamical_substrate_law/hardened_theorems/first_shell_inner_product_primitive.tex` (320 lines LaTeX; 9-page PDF, ~312 KB; clean three-pass compile with zero warnings/errors).

**Theorem hardened.** Identity G1 (first-shell inner-product primitive): under (H1) vertex-aligned Reading C with $\hat{n} = v_{\text{host}}$, (H2) 600-cell unit-vertex normalisation $|v|=1$, and (H3) icosahedral residual symmetry $H_3 = I_h$ at the host vertex, every first-shell vertex $v_i$ of $v_{\text{host}}$ satisfies $v_i \cdot v_{\text{host}} = \phi/2$ uniformly across $i \in \{1, \ldots, 12\}$.

**Three structural advances over the Patch 0541 §3.1 sketch-document Layer 3 derivation:**
1. **Dihedral-angle calculation as standalone lemma** (Lemma 3.1): the central angle 36° between adjacent 600-cell vertices, with $\cos(\pi/5) = \phi/2$, is now derived rigorously from the Chebyshev minimal polynomial of $\cos(\pi/5)$ — specifically, $16x^5 - 20x^3 + 5x + 1 = (x+1)(4x^2 - 2x - 1)^2 = 0$ with $x = \cos(\pi/5) \neq -1$ giving $x = (1+\sqrt{5})/4 = \phi/2$.
2. **Icosahedral residual symmetry $H_3 = I_h$ as separately-derived structural input (H3)**: the previously implicit symmetry hypothesis is now made explicit, with the derivation chain Capotauro v2.0 FI-C-RC-2 + Patch 0419 Finding C-W37 cited as the structural-input source. Lemma 2.4 (icosahedral transitivity) lifts the per-pair inner product to uniformity across all 12 first-shell vertices via the orbit–stabilizer theorem applied to $\Hthree$ acting on the first-shell icosahedron.
3. **Five-class exclusion enumeration (E1–E5)** registering the polytope-theoretic primitives taken as given: (E1) Layer 4 derivation of the 600-cell substrate from CPP A1–A11; (E2) non-vertex-aligned Reading C variants; (E3) Identity G2 (icosahedral first-shell structure) imported at sketch-document Layer 3; (E4) higher-shell inner-product primitives; (E5) the 600-cell short-edge chord length $1/\phi$ taken as polytope-theoretic input.

**Programme-state changes at Patch 0571.**
1. **OPEN-FP-F1-3 RESOLVED.** First of the six post-v1.0-SHIP F.1 Open Problems closed; closure recorded in `research_frontier.md` §4 Recently Resolved and in `frontier_sectors/FP.md` status field.
2. **Shared exclusion class E1 of Patches 0551 + 0552 CLOSED** (Corollary 3.2 of the new artifact). F.1 Theorems 5.1 (host-to-first-shell uniform projection) and 5.2 (first-shell-to-first-shell perpendicularity) upgrade from publication-grade Layer 3 *conditional on G1* to publication-grade Layer 3 *unconditional*.
3. **F.1 Theorem 7.1 (substrate-locality umbrella) conditionality strengthened** (Corollary 3.3). The G1-conditional clause is discharged; remaining conditionality reduces to (a) the umbrella's own sketch-document Layer 3 status; (b) framework-axiom status of Mechanism A (registered as OPEN-FP-F1-2); (c) the $\mathcal{O}(\delta^1)$ restriction (OPEN-FP-F1-1).
4. **F.1 Layer 3 hardened-theorem sequence complete at four artifacts** (Patches 0550 + 0551 + 0552 + 0571): perturbation-theory propagation rule + shell-locality (0550); first-shell-to-first-shell perpendicularity (0551); host-to-first-shell uniform projection (0552); G1 first-shell inner-product primitive (this Patch). Combined LaTeX: ~1060 lines; combined PDFs: ~30 pages across four artifacts.
5. **First F-line post-v1.0-SHIP substantive physics Patch landed** without Phase 7B/7C completion — the Session 142 close handover (planned narratively as Patch 0571 in `reasoning-dynamical-substrate-law.md` §65) and Session 143 Phase 7A doc-suite production sub-arc (planned narratively as Patches 0572–0572i) remain as forward-looking trajectory plans drafted in the documentation suite but not yet committed to git history. Patch 0571 narrative-numbering question is flagged for maintainer disposition (renumbering of either the planned-but-uncommitted Patch 0571 narrative or the present Patch 0571 G1 hardening; the present `.tex` artifact carries the Patch 0571 label per maintainer instruction).

**Files in this Patch.**
1. NEW — `flagship_papers/dynamical_substrate_law/hardened_theorems/first_shell_inner_product_primitive.tex` (320 lines).
2. NEW — `flagship_papers/dynamical_substrate_law/hardened_theorems/first_shell_inner_product_primitive.pdf` (9 pages, compiled three-pass clean from the .tex).
3. APPEND — this changelog entry to `documentation_suite/changelog-dynamical-substrate-law.md`.
4. EDIT — `frontier_sectors/FP.md` to mark OPEN-FP-F1-3 RESOLVED.
5. EDIT — `research_frontier.md` Last-updated header + §4 Recently Resolved entry + problem counts.

**Post-Patch-0571 trajectory.** Two highest-priority remaining F.1 substrate-locality programme targets: **OPEN-FP-F1-1** (extension to $\mathcal{O}(\delta^2)$ via second-shell inner-product primitives) and **OPEN-FP-F1-2** (Layer 4 axiomatic derivation of Mechanism A from CPP primitive axioms A1–A11). Both are independent of OPEN-FP-F1-3 and may be pursued in either order. Other open F.1-trajectory items: OPEN-FP-F1-4 (Sector-5 schema instantiation), OPEN-FP-F1-5 (non-vertex-aligned Reading C variants), OPEN-FP-F1-6 (prose-density tightening / F.1-condensed companion paper).

**Calibration discipline at Patch 0571.** No theorem statements of F.1 v1.0 paper source modified; no proofs of F.1 v1.0 paper source modified; no Open Problems of F.1 v1.0 paper source modified; no existing `hardened_theorems/*.tex` source artifacts modified (Patches 0550 + 0551 + 0552 unchanged on disk); no bibliography body of F.1 v1.0 paper source modified; no abstract / §1–§10 substantive content rewrites. The hardened-theorem artifact is purely additive within `hardened_theorems/`. The five-Open-Problem in-body commitment of F.1 v1.0 §9 is preserved end-to-end; OPEN-FP-F1-3's status transition (OPEN → RESOLVED) is recorded in the frontier registry layer only, not in the F.1 v1.0 paper source.

---

## Version 1.0 SHIPPED — 24 May 2026 (Session 142, Patch 0570)

**F.1 Dynamical Substrate Law SHIPPED as v1.0 release after six-round ChatGPT reviewer cycle converged on strongest-positive verdict, with explicit Grok and Copilot Round 1 SHIP-acceptable sign-offs.** Title block `\date{}` line bumped from `Version 0.9 (pre-v1.0; awaiting reviewer engagement), 23 May 2026` to `Version 1.0 --- 24 May 2026` + italicized scope-framing subtitle. Author email updated to `drthomas@protonmail.com` at Patch 0569a. The v1.0 SHIP is **the first F-line flagship v1.0 ship in CPP corpus history.**

**Three-reviewer convergence at v0.9 / Rounds 1–6:**

- **Grok Round 1 sign-off** (Patch 0568 archival): explicit "v1.0 SHIP-acceptable" verdict.
- **Copilot Round 1 sign-off** (Patch 0568 archival): implicit SHIP-acceptable with tier-ranked recommendations (1 MUST-ADDRESS + 4 SHOULD-ADDRESS + 5 CAN-DEFER + 2 DECLINED items classified in Round 1 synthesis at Patch 0568).
- **ChatGPT six-round trajectory** (Patches 0568 → 0569e, monotonic verdict improvement):
  - R1: "NOT yet publication-grade flagship overall"
  - R2: "substantially improved; reviewer-ready as disciplined pre-v1.0 framework paper"
  - R3: verdict matrix YES for "reviewer-ready as flagship framework preprint"
  - R4: "genuinely stable in identity; credible flagship framework theorem paper"
  - R5: "intellectually stable for long-term foundational programme"
  - **R6**: *"v5 is substantially more credible, rigorous, and publishable than all earlier versions; first version that feels architecturally stable, epistemically disciplined, mathematically centered, structurally self-aware."* (strongest-positive)

The R6 strongest-positive verdict was diagnostic-resolved at Patch 0569e: the recurring R3/R4/R5 reviewer-driven-recommendations pattern (all 4 recommendations already implemented at Patch 0569b) was identified as a **TikZ-rendering processing artifact** — ChatGPT reading raw `.tex` source where `\begin{tikzpicture}...\end{tikzpicture}` code does not render as visualized figure. Resolution: switch to PDF upload protocol for ChatGPT reviewer engagement (codified as one of three programme-level conventions at this SHIP; see below).

**SHIP-cycle reviewer-engagement protocol patches** (Patches 0568–0569e + 0570):

- Patch 0568 Round 1 archival + synthesis (Copilot + ChatGPT + Grok letters; tier-ranked classification).
- Patch 0569 Round 1 multi-edit response (8 atomic LaTeX edits implementing 5 reviewer-cycle items): thermodynamic-arrow framing triple-coverage at abstract + §1.1 + §10 + executive summary; §7.3 Step 3 representation-theoretic justification.
- Patch 0569a Round 2 (4 atomic edits): author email update + §1.2 "substrate-locality component required for Scenario A closure" + Lemma 6.3.1 unperturbed-step clarification + §7.4 "structural rather than editorial" hardening note.
- Patch 0569b Round 3 (5 atomic edits): Scenario A closure language extension to 3 anchors + §1 executive summary bold declarative + Figure 8.1 TikZ dependency-graph in §8.2.
- Patches 0569c–0569e Rounds 4–6 archival + diagnostic-framing + recurring-pattern documentation + diagnostic resolution (NO `.tex` edits at these Patches; reviewer-engagement-cycle diagnostic work only).
- **Patch 0570 (this SHIP patch)**: Variant (b) selected over Variant (a) (G1-hardening-first) per multi-round cross-reviewer convergent verdict + ChatGPT R3–R6 scope-framing convergence + CPP corpus convention. Two atomic `.tex` edits: Edit 1 `\date{}` line v1.0 SHIP update + italicized scope-framing subtitle; Edit 2 CHANGELOG comment block update from pre-v1.0 to comprehensive v1.0 SHIP block. V1.0 PDF committed as frozen reference at `flagship_papers/dynamical_substrate_law/dynamical_substrate_law.pdf` (33 pages, 489 KB, MD5 `49e56be92a3ccc126ce09210b5898794`). `.gitignore` exception `!flagship_papers/*/*.pdf` added during apply-fix to enable v1.0 SHIP PDF + future flagship SHIP PDFs.

**v1.0 SHIP-state content summary:**

- **Three publication-grade Layer 3 theorems**: Theorem 5.1 (host-to-first-shell uniform projection, conditional on G1), Theorem 5.2 (first-shell-to-first-shell perpendicularity, conditional on G1), Theorem 6.1 (perturbation-theory propagation rule) + Corollary 6.2 (shell-locality at O(δ¹)). Supporting Lemmas 5.2.1, 6.1.1, 6.2.1, 6.3.1 + imported Lemma "G1 first-shell inner-product primitive" at sketch-document Layer 3.
- **One sketch-document Layer 3 umbrella theorem**: Theorem 7.1 substrate-locality of DI-bit currents at vertex-aligned Reading C. Anti-erasure discipline operationalized at three concrete points in §10. The umbrella's non-publication-grade status is preserved transparently in the scope-framing subtitle and at §7.4 "structural rather than editorial" hardening note.
- **Three hardened-theorem artifacts at `hardened_theorems/`**: Patches 0550 + 0551 + 0552 (741 lines LaTeX combined; publication-grade Layer 3 trio supplying §5 + §6 body content as direct integration inputs).
- **Five Open Problems registered**: OPEN-FP-F1-1 (extension to O(δ²)), OPEN-FP-F1-2 (Layer 4 axiomatic derivation of Mechanism A), OPEN-FP-F1-3 (G1 publication-grade hardening), OPEN-FP-F1-4 (Sector-5 schema instantiation), OPEN-FP-F1-5 (non-vertex-aligned Reading C variants). Anti-priorities sustained: NO Open Problems modified during SHIP-cycle calibration response.
- **Mechanism A as framework axiom**: propagation-rate asymmetry $r(\hat{e}) = r_0(1 + \delta\,\hat{e}\cdot\hat{n})$ + framework-local current construction at $\mathcal{O}(\delta^1)$ taken as Layer 3 framework input. Layer 4 axiomatic derivation deferred to OPEN-FP-F1-2.
- **OPEN-SD-CHIR-PRIMITIVE umbrella manifestation (iv)**: closed at sketch-document Layer 3 via Theorem 7.1; joins Capotauro v2.0's spatial-sector manifestations (i)–(iii) (parity violation, neutrino chirality structure, weak isospin assignment). Manifestation (v) registered as OPEN-FP-F1-4 (Sector-5 schema, candidate domains include thermal-equilibrium gauge fixing + symmetry-restoration dynamics + cosmological-arrow alignment).
- **Cross-reference to Capotauro v2.0 §3 spatial-sector parallel**: §5.6 establishes the methodological parallel between F.1's vertex-aligned Reading C first-shell identities and Capotauro v2.0's spatial-sector substrate physics.

**Three programme-level conventions extended at F.1 v1.0 SHIP:**

1. **Variant (b) v1.0 SHIP framing with `\date{}` line scope subtitle.** Title-page scope-framing carries four claims (structurally-grounded + sketch-document Layer 3 flagship framework preprint + publication-grade hardened components + non-publication-grade umbrella theorem) at first reader contact. This is the first v1.0 SHIP in CPP corpus using `\date{}` line scope-subtitle pattern; corpus-establishing for future F-line + framework-preprint SHIPs that ship Layer 3 + sketch-document content with explicit honesty-of-scope.

2. **PDF-upload-default reviewer engagement protocol.** Going-forward protocol for ChatGPT reviewer engagement: upload the freshly-compiled PDF (not `.tex` source), especially for papers containing TikZ figures, bibliography environments, or other LaTeX content requiring compilation to render. Empirical motivation: Patch 0569e diagnostic resolution (Rounds 3–5 `.tex`-upload-driven recurring-recommendation pattern resolved to monotonic-positive verdict at Round 6 PDF upload). Extends `relationship_protocol.md` reviewer-submission protocol with upload-format-aware guidance.

3. **`.gitignore` exception pattern `!flagship_papers/*/*.pdf` for v1.0+ SHIP PDFs.** The repo-root `*.pdf` ignore rule preserves the default-don't-commit-PDFs discipline for working-draft compilation artifacts in deeper subfolders (`hardened_theorems/`, `sketches/`, etc.) but exempts flagship-paper-root PDFs that are committed deliberately at v1.0+ SHIP milestones. Corpus-establishing exception for F-line flagship trajectory; first F-line flagship PDF committed at this Patch as canonical citation target for v1.0 references.

**v2.0+ post-SHIP trajectory** (post-Phase-7 priority queue per ChatGPT R1–R6 convergent guidance):

- **OPEN-FP-F1-3** — G1 publication-grade hardening (ChatGPT R1–R6 convergent "single highest-value next action"). Produces `hardened_theorems/first_shell_inner_product_primitive.tex` parallel in structure to the three existing hardened artifacts. Upgrades Theorems 5.1 + 5.2 from *publication-grade Layer 3 conditional on G1* to *publication-grade Layer 3 unconditional*; consequently upgrades Theorem 7.1's conditionality clause. Estimated 1–2 sessions.
- **OPEN-FP-F1-1** — extension to O(δ²) (substantive geometric and perturbation-theory project at higher order).
- **OPEN-FP-F1-2** — Layer 4 axiomatic derivation of Mechanism A (long-term programme target; spans multiple Patches in a dedicated trajectory).
- **OPEN-FP-F1-6** — prose-density tightening Patch (registered at Patch 0569e from ChatGPT R6 follow-up).
- **F.1-condensed companion paper trajectory** — Theorem 6.1 + Corollary 6.2 + Theorem 7.1 focused with minimal CPP interpretation (registered at Patch 0569e from ChatGPT R6 follow-up).
- **Substrate-locality umbrella publication-grade hardening Patch** (ChatGPT R6 §Remaining-Weaknesses #2 names specific structural lemmas).

**Total v1.0 development span**: Patches 0554 (skeleton) → 0570 (v1.0 SHIP). 17 patches across single extended Session 142. The 17-patch single-session-extended arc pattern (Capotauro v2.0 at Session 135 Patches 0482–0509; F.1 at Session 142 Patches 0554–0570) is the established CPP corpus norm for v1.0 SHIP arcs.

**Calibration discipline at Patches 0569 → 0569e**: no theorem statements modified, no proofs modified (Patch 0569a Edit C added clarification AFTER existing Lemma 6.3.1 proof, not within), no Open Problems modified, no `hardened_theorems/*.tex` source artifacts modified, no bibliography body modified. The five-Open-Problem commitment was preserved end-to-end across all six ChatGPT rounds + Patches 0568–0570.

**Authored by Opus, Session 142, Patch 0570, 24 May 2026.**

---

## Version 0.9 (pre-v1.0; reviewer-engagement cycle) — 24 May 2026 (Session 142, Patches 0568–0569e)

**Six-round ChatGPT reviewer cycle + Copilot + Grok Round 1 archival across Patches 0568–0569e closing v0.9 → v1.0 SHIP-cycle reviewer engagement.** This is the second-largest content block in F.1's development arc (after the 10-Patch body-content assembly at 0556–0565). Title block `\date{}` line carried the framing `Version 0.9 (pre-v1.0; awaiting reviewer engagement), 23 May 2026` throughout the cycle until Patch 0570 SHIP increment.

**v0.9 SHIP-cycle structure**:

- **Patch 0568** Round 1 archival + synthesis: three reviewer letters (Copilot + ChatGPT + Grok) archived at `reviews/`; synthesis document classifies 12 items as 1 MUST-ADDRESS + 4 SHOULD-ADDRESS + 5 CAN-DEFER + 2 DECLINED.
- **Patch 0569** Round 1 multi-edit response: 8 atomic LaTeX edits implementing 5 reviewer-cycle items. Major content addition: thermodynamic-arrow framing triple-coverage (abstract + §1.1 + §10 + executive summary) addressing Copilot MUST-ADDRESS item; §7.3 Step 3 representation-theoretic justification addressing ChatGPT SHOULD-ADDRESS item.
- **Patch 0569a** Round 2 reviewer-driven adjustments: 4 atomic edits. Notable additions: §1.2 "substrate-locality component required for Scenario A closure" clarification clause; Lemma 6.3.1 unperturbed-step clarification added AFTER existing proof (calibration discipline: no proof modifications); §7.4 "structural rather than editorial" hardening note. Author email updated to `drthomas@protonmail.com` at this Patch.
- **Patch 0569b** Round 3 reviewer-driven adjustments: 5 atomic edits. Major content addition: Figure 8.1 TikZ dependency-graph in §8.2 (Layer hierarchy stack visualization); Scenario A closure language extension to 3 anchors (abstract + §2.2 + §10); §1 executive summary bold declarative ("This paper closes the F.1 sub-question at sketch-document Layer 3...").
- **Patches 0569c–0569e** Rounds 4–6 archival + diagnostic-framing + recurring-pattern documentation + diagnostic resolution: NO `.tex` edits at these three Patches. The R3/R4/R5 recurring-recommendations pattern (4 recommendations already implemented at Patch 0569b but reappearing in R4/R5 reviewer letters) was documented at Patch 0569d as a verdict-stabilisation trajectory anomaly. Diagnostic resolution at Patch 0569e: identified as TikZ-rendering processing artifact (ChatGPT reading raw `.tex` source where `\begin{tikzpicture}...\end{tikzpicture}` code is unrendered text); resolved by switching to PDF-upload protocol at Round 6. Round 6 verdict (PDF upload): strongest-positive of the cycle.

**Programme-state changes**: NONE registered at the v0.9 → v1.0 SHIP-cycle level; all programme-state registry updates DEFERRED to Phase 7B per handover §6 Step E (Patches 0573–058N).

**Compile-readiness at end of v0.9 cycle (post-Patch-0569e)**: paper feature-complete at 31 pages; LaTeX environment balance verified; bibliography body unchanged from Patch 0566 (13 `\bibitem` entries); all `\ref`/`\eqref`/`\cite` targets resolve; theorem/lemma/corollary environments balanced.

**Anti-priorities sustained throughout the v0.9 cycle**: NO theorem statements modified, NO proofs modified, NO Open Problems modified, NO `hardened_theorems/*.tex` source artifacts modified, NO bibliography body modified, NO abstract / §1 / §2 / §3 / §4 / §5 / §6 / §7 / §8 / §9 / §10 substantive content rewrites (additive clarification edits only). The five-Open-Problem commitment preserved end-to-end.

**Authored by Opus, Session 142, Patches 0568–0569e, 24 May 2026.**

---

## Version 0.X-feature-complete (pre-SHIP-cycle final polish) — 24 May 2026 (Session 142, Patches 0566–0567)

**Bibliography body + pre-v1.0 final polish: paper reaches feature-complete state ready for v0.9 → v1.0 SHIP-cycle reviewer engagement.** Two patches:

- **Patch 0566** Bibliography body: 13 `\bibitem` entries added in `thebibliography` environment (Option B: explicit inline entries with body unchanged elsewhere). Citations span the CPP corpus (SF-4, Capotauro, SS-7, SM-8, SS-2, SS-4, SS-5, Reading C foundational sketches) + external references (Coxeter 1973 on the 600-cell; NuFit 6.0; JUNO 2025; Planck 2018).
- **Patch 0567** Pre-v1.0 final polish: three atomic edits — `\date{}` line metadata update + CHANGELOG comment block at `.tex` header + abstract Open Problem count corrected from 3 to 5 (Patches 0564 + earlier had registered all 5 Open Problems at §9 body but the abstract retained an outdated count of 3 from the skeleton draft). Title block bumped to `Version 0.9 (pre-v1.0; awaiting reviewer engagement)`.

**State at end of Patch 0567**: 31-page paper feature-complete, ready for v0.9 → v1.0 SHIP-cycle reviewer engagement at Patch 0568.

---

## Version 0.X-body-assembly (10-Patch body-content arc) — 24 May 2026 (Session 142, Patches 0556–0565)

**10-Patch body-content assembly arc: §1 introduction through §10 conclusion, including FIRST and SECOND integration patches importing hardened-theorems trio.** This is the largest content block in F.1's development arc.

- **Patch 0556** §1 Introduction and motivation: 4 subsections (corpus position + F.1 sub-question as programme gate + Sketch Layer 2 → Layer 3 trajectory recap + paper roadmap with Layer-distinction discipline).
- **Patch 0557** §2 The F.1 sub-question: substrate-mechanism derivation: 4 subsections (Manifestation (iv) of OPEN-SD-CHIR-PRIMITIVE + three closure scenarios + Scenario A: Mechanism A propagation-rate asymmetry + minimal-local-first-order realization framework).
- **Patch 0558** §3 Framework primitives: 4 subsections (CPP primitive axioms A1–A11 recap + 600-cell substrate at vertex-aligned Reading C + first-shell geometric primitives G1 and G2 + DI-bit current and Mechanism A framework).
- **Patch 0559** §4 Mechanism A as framework axiom: 3 subsections (propagation-rate asymmetry + framework local-current construction at first order in $\delta$ + Mechanism A as framework axiom Layer rigor and Layer 4 deferral).
- **Patch 0560** §5 The first-shell geometric identities (**FIRST integration Patch**, importing Patches 0551 + 0552 hardened theorems): 6 subsections including Theorem 5.1 + Theorem 5.2 + Exclusion class E1 + Capotauro v2.0 §3 spatial-sector parallel cross-reference.
- **Patch 0561** §6 The perturbation-theory propagation rule (**SECOND integration Patch**, importing Patch 0550 hardened theorem): 6 subsections including Lemmas 6.1.1 + 6.2.1 + 6.3.1 + Theorem 6.1 + Corollary 6.2 + five-class exclusion enumeration.
- **Patch 0562** §7 The substrate-locality theorem (umbrella result): 4 subsections constructing Theorem 7.1 at sketch-document Layer 3 from §5 + §6 inputs; explicit Layer-distinction status preservation at §7.4.
- **Patch 0563** §8 Layer 3 stack — status, scope, and exclusions: 2 subsections including per-theorem Layer hierarchy explicit table + Layer 4 trajectory implications + anti-erasure discipline named explicitly at §8.3.
- **Patch 0564** §9 Open higher-order questions: 5 Open Problem statements (OPEN-FP-F1-1 through OPEN-FP-F1-5) with independence analysis at §9 closing paragraph.
- **Patch 0565** §10 Conclusion: anti-erasure discipline operationalised at three concrete points; 5-Open-Problem commitment preserved end-to-end; cross-references to forward trajectory (OPEN-FP-F1-3 G1 hardening as ChatGPT R1–R6 convergent single-highest-value-next-action).

**Authored by Opus, Session 142, Patches 0556–0565, 24 May 2026.**

---

## Version 0.0 (paper skeleton) — 24 May 2026 (Session 142, Patch 0554)

**F.1 Dynamical Substrate Law paper skeleton created.** Preamble (LaTeX packages + theorem environments + custom macros) + section headers (§1–§10 placeholder structure) + title block draft + abstract draft + 5 Open Problem placeholders. No body content; assembly arc begins at Patch 0556.

**Initial title block**: `The Dynamical Substrate Law: Substrate-Locality of DI-Bit Currents at Vertex-Aligned Reading C in the 600-Cell` (preserved at v1.0 unchanged). Author block: Dr. Thomas Lee Abshier ND (Hyperphysics Institute) with AI co-authorship Claude Opus (Anthropic) primary mathematical co-author + ChatGPT (OpenAI) + Copilot (Microsoft) + Grok (xAI) review and calibration.

**Authored by Opus, Session 142, Patch 0554, 24 May 2026.**

---

## Pre-paper-assembly: foundations work + reviewer-pause cycle + Layer 3 promotion

The F.1 paper assembly arc at Patches 0554–0570 was preceded by substantial foundations work + reviewer-pause cycle + Layer 3 promotion work across earlier Patches in the F.1 sub-question trajectory. This pre-paper-assembly arc is documented in detail at:

- **Phase 2 foundations work** (load-bearing sub-question closure at sketch Layer 2): `sketches/F1_phase2_foundations_work.md`, `sketches/F1_subquestion_pcd_orientation_link.md`. Patches 0531–0537 closed seven sub-questions at sketch Layer 2.
- **Reviewer-pause cycle** (closure-milestone external review per `templates/operating_system.md` §17): `reviewer_pause/F1_reviewer_pause_checkpoint_patches_0531_0537_v1.0.md` + `reviewer_pause/F1_reviewer_pause_feedback_record_v1.0.md`. Patch 0538 calibration response; Patch 0539 status upgrade.
- **Layer 3 promotion** (substantive Layer 2 → Layer 3 promotion work): `sketches/F1_layer3_promotion_scoping.md`, `reviewer_pause/F1_layer3_reviewer_pause_checkpoint_patches_0540_0546_v1.0.md`, `reviewer_pause/F1_layer3_reviewer_pause_feedback_record_v1.0.md`.
- **Hardened theorems** (publication-grade Layer 3 trio supporting §5 + §6 of the paper): `hardened_theorems/` — three artifacts at 741 lines LaTeX combined (Patches 0550 + 0551 + 0552).
- **Flagship paper assembly scoping**: `sketches/F1_flagship_paper_assembly_scoping.md` (Patch 0553 scoping document immediately preceding paper skeleton at Patch 0554).

The reviewer-pause cycle convention itself (`templates/operating_system.md` §17 + `templates/paper_completion_checklist.md` §"Reviewer-Pause Cycle Precondition for Flagship-Paper-Trajectory Work" added Patch 0539a) was established during the F.1 trajectory and is the canonical worked example for future flagship trajectories (F.2, F.3, etc.).

---

*Changelog file created Session 143 Patch 0572 (24 May 2026) as the first SHIP-time companion documentation file in Phase 7A initiation. Per `templates/documentation-suite.md` §11 reference implementation: `flagship_papers/capotauro/documentation_suite/changelog-capotauro.md`. This file is maintained continuously from this Patch forward as the canonical version archaeology for the F.1 paper.*
