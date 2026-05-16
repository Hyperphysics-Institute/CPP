# Changelog: Capotauro flagship paper

**Paper**: The Capotauro Mechanism: Chirality on the K3-Doublet from Substrate-Vacuum Broken-Symmetry Physics
**Source**: `flagship_papers/capotauro/capotauro.tex`
**Programme registration**: THEO-CAP-1 (Session 103 Patch 0397, theorem #62 in `theorem-registry.md`)
**OPEN-SM-4 status at registration**: PARTIAL CLOSURE — sub-claim (c) v1.0 closed; sub-claims (a) and (b) remain open
**Maintainer**: Thomas Lee Abshier ND, Hyperphysics Institute

This file is the canonical version archaeology for the Capotauro paper. Each `capotauro.tex` patch updating the paper source adds a one-line summary entry below. Substantive detail lives in the patch commit messages; this file is the curated narrative for researchers tracing the closure trajectory.

The `.tex` source itself carries only its current title block (title + author + version + date). Paper-level CHANGELOG comment blocks and visible PDF-rendered version-history paragraphs were removed at Patch 0408 (Session 115) per the convention that programme-internal version archaeology belongs alongside development/transcript/reasoning files in the documentation suite, not in the paper source.

---

## Version 1.0 (SHIPPED) — 16 May 2026 (Session 122, Patch 0415)

**Capotauro paper v1.0 SHIPPED** as the third flagship paper to ship at v1.0 in the CPP corpus after SS-9 (Session 32), SF-4 (Session 54), and SF-2 (Session 83); first flagship paper outside the SF-N numerical convention — the THEO-CAP-N naming for the Capotauro theorem chain reflects its flagship-paper-pending status preserved through v1.0 SHIP, recording that the paper's primary programme-level theorem (THEO-CAP-1) was registered Session 103 Patch 0397 ahead of its own paper publication, the first such registration pattern in the CPP corpus.

**Substantive content unchanged from v0.9 (Patch 0413)**: v1.0 SHIP is version-bump-only at the paper level. Title block updated from `Version 0.9 --- 16 May 2026` to `Version 1.0 (SHIPPED) --- 16 May 2026`; all other paper content preserved. The paper body already references v1.0 throughout via the closure trajectory's forward-targeting language (the "what is out of scope at v1.0" enumeration in the abstract, the "v1.0" qualifier on foundational input postulates, the v1.0 / v2.0+ scope-deferral language in the open-work sections), reflecting that the closure trajectory across Sessions 87–102 already targeted v1.0 SHIP as its endpoint. The version-bump-only character of this SHIP confirms that the v0.9 cross-reviewer convergence on SHIP-readiness (ChatGPT round-3 + CoPilot round-1 + Grok round-1; archived at Patch 0412 Session 119) was the correct SHIP signal.

**Programme-level changes at v1.0 SHIP** (Patch 0415 across multiple registry files; .tex source itself version-bump-only):

- `Research_Frontier.md` OPEN-SM-4 status field updated to reflect v1.0 SHIP via the Capotauro paper; the PARTIAL CLOSURE status is preserved (sub-claim (c) closed at v1.0 SHIP; sub-claims (a) and (b) remain open).
- `Research_Frontier.md` NEW `OPEN-FI-C-9-FP-MECHANISM` entry registered in the FP section, capturing the Reading C geometric-chirality candidate mechanism (working sketch `sketches/Capotauro_chiral_mechanism_candidate.md` from Patch 0414) as the sub-claim (b) Layer-3 closure target. FP-section problem count advances 8 → 9.
- `theorem-registry.md` Last-updated header updated noting THEO-CAP-1 paper-level confirmation at v1.0 SHIP (theorem registered Session 103 Patch 0397 ahead of paper publication; v1.0 SHIP confirms the registered theorem now has its flagship-paper venue). Summary Statistics SF-Line row UNCHANGED at 10 theorems + 7 propositions + 1 lemma (THEO-CAP-1 already counted); Total theorem count UNCHANGED at 62.
- `paper_catalog.md` SF-Line section updated with new Capotauro row at v1.0 SHIPPED + Capotauro documentation paragraph.
- `INDEX.md` flagship_papers section updated with Capotauro entries at v1.0 SHIPPED.
- NEW `flagship_papers/capotauro/README.md` — paper-level README at v1.0 SHIPPED transition (parallel to the README pattern at `flagship_papers/neutrinos/README.md` and `flagship_papers/electroweak/README.md`).
- This file (`documentation_suite/changelog-capotauro.md`) updated with this v1.0 SHIP version section + Patch 0415 register row + Last-updated footer updated to Session 122 Patch 0415.

**Out-of-scope at v1.0 (registered as open work for v2.0+ closure trajectory)**:

- Sub-claim (a) — Capotauro nucleation event (universe-wide sign-selection event downstream of sub-claim (b) magnitude mechanism). Tracked at `Research_Frontier.md` OPEN-SM-4.
- Sub-claim (b) — substrate chirality mechanism candidate derivation. Tracked at `Research_Frontier.md` OPEN-FI-C-9-FP-MECHANISM (NEW this patch); Reading C geometric-chirality candidate (primitive 4D direction $\hat{n}$) at Tier-4 Layer 1 / Layer 2 epistemic status with working sketch from Patch 0414; estimated 10–20 sessions to Layer 3 closure trajectory completion.
- FI-C-10 cage-shell observable-class-independence claim first-principles derivation. Tracked at `Research_Frontier.md` (separate open work entry distinct from OPEN-FI-C-9-FP-MECHANISM).
- PMNS reactor mixing angle $\sin^2\theta_{13}$ re-scoped to SF-2 v2.0+ (linear-vs-quadratic scaling tension surfaced Session 100; wavefunction-level coupling hypothesis ruled out Session 101; candidate γ structural observation $\sin^2\theta_{13} = b \cdot m_\perp \approx 0.0227$ matches observation within 1σ but lacks rigorous derivation).
- $\delta_{CP}$ and $\eta_B$ — downstream observables from $|M| = \chi/6$ via PMNS perturbation machinery beyond the Capotauro mechanism's direct scope; future Capotauro sub-claim work.

**Forward queue post-Session 122 close**:

- Patches 0416+ documentation suite production across estimated 7–15 sessions per `templates/paper_completion_checklist.md` Section A (7 companion documentation files: `mechanism-capotauro.md`, `glossary-capotauro.md`, `phenomena-capotauro.md`, `philosophy-capotauro.md`, `development-capotauro.md`, `reviews-capotauro.md`, `keywords-capotauro.md`) + Section B verification notebooks + Section C registry updates beyond v1.0 SHIP baseline + Section D navigation updates beyond v1.0 SHIP baseline + Section E development transcripts (`handover-capotauro.md`, `development-capotauro.md`, `transcript-capotauro.md`, `reasoning-capotauro.md`) + Section F OSF registration (DOI `10.17605/OSF.IO/JXE8D`; Thomas/Isak timing decision per existing programme practice) + Section G repository commit + Section H final verification.
- Sub-claim (b) Reading C closure trajectory Q1 group-theoretic verification of the $\Hfour$ stabilizer of $\hat{n}$ $\cong$ $\Ifour$ claim — first sub-step toward Layer 3 closure, estimated 1–3 sessions.
- Anthology chapter at Rovelli/SciAm register parallel to SS-7 / SS-8 / SS-9 / SF-4 chapters (~5000–6000 words).
- TATWD integration to `CPP_the_theory.md` at v1.0 SHIP — Capotauro mechanism integrated into the master theory narrative with OPEN-SM-4 sub-claim (c) closed and OPEN-FI-C-9-FP-MECHANISM as sub-claim (b) closure-trajectory pointer.
- SF-4 v4.5+ integration per Grok Session 119 suggested next steps (paste Theorem 5.1 + $\Delta p_{LR} = \chi/6$ into SF-4 Capotauro section; update SF-4 predictions table for $\delta_{CP}$ substrate-level handle; open `SF-4_deltaCP_capotauro_integration.md` sketch).
- ClearPC PDF compile + public posting (Zenodo + arXiv) at Thomas's discretion via the Binary Artifact Workflow established at SF-4 Patch 0339.

After v1.0 SHIP: the `.tex` source enters the post-SHIP regime in which substantive modifications are deferred to external-feedback-driven v1.x or to a v2.0+ programme advance (e.g., Reading C closure retiring FI-C-9 from foundational postulate). Documentation suite production continues in Patches 0416+ per the convention that documentation suite is ACTIVE post-v1.0 while the `.tex` source freezes (Lesson 6 from SF-4 v1.0 SHIP Session 54).

---

## Version 0.8 — 16 May 2026 (Session 118, Patch 0411)

**v0.8 substantive expositional polish from ChatGPT v0.7 round-2 review (Patch 0411, Session 118)**

ChatGPT v0.7 round-2 review (archived at `reviews/chatgpt_v0.7_session_117.md` per Patch 0410) was overall strongly positive ("v0.7 is meaningfully better than v0.6. Not incrementally better — structurally better.") and identified five high-leverage v0.8 items. All five addressed in Patch 0411 in a single coherent expositional-polish pass with no new physics content (refinement of presentation of physics content already in the paper):

- **Item #5 (highest-value v0.8 addition)** — NEW §1.7 "Derivation roadmap" with TikZ figure showing the structural composition flow from H₄ → I₄ chirality breaking through χ = φ⁻³ (FI-C-9) → T_{A_2}(b) chirality-eigenvalue matching → |M_{K_3}| = χ (K3-amplitude factor) → |M_⊥| = d_E/V_cage = 1/6 (FI-C-10 cage-shell averaging) → |M| = χ/6 ≈ 0.0394 (composition) → Δp_LR (primary prediction). Green boxes = substrate-physics foundational inputs; blue boxes = derivation-level structural composition steps; orange box = observable. Figure also makes load-bearing assumptions visible (two green boxes are postulates with first-principles closure deferred to sub-claim (a)+(b) v2.0+ work; FI-C-10 box is foundational input with first-principles closure registered separately). Required adding `arrows.meta` and `shapes.geometric` to TikZ libraries in preamble. Substantially improves new-reader accessibility per ChatGPT's specific request.
- **Item #4** — Cross-reference paragraph added to §1.2 (What this paper delivers) explicitly noting that χ/6 ≈ 0.0394 is not parameter-selected to match empirical anchor 0.04 (three structural inputs independently fixed; zero free parameters) and cross-referencing §6.6 nontriviality argument. Makes the structural-constraint argument discoverable from the introduction for new readers who jump to §1 only. No new content (§6.6 unchanged from Patch 0407).
- **Item #1 (bounded; full closure deferred to v2.0+)** — §5.4 FI-C-10 motivation strengthened with new Argument 3: SF-4 v4.0 precedent for cage-shell mass-observable extension via FI-C-6 (Composite K3-Cage-Shell Coupling Theorem THEO-SF-4-5). Same averaging factor d_E/V_cage = 1/6 emerges from same cage geometry and irrep structure for the mass observable at theorem level; FI-C-10 extends to chirality observable via observable-class-independence claim (narrower than "Schur orthogonality on cage produces physical averaging factor" in general). Strengthens FI-C-10 plausibility on three grounds: established mechanism not new construction; same numerical factor from same structural setup; only observable-class-independence claim requires first-principles closure work. What-establishes/what-does-not-establish caveats updated to include the FI-C-6 precedent in the establishes list.
- **Item #2** — §6.1.1 rewritten with compact "what would experimentalists measure?" opening paragraph followed by enumerated-not-multi-paragraph four-route summary. New opening establishes the observable's substrate-level identity (off-diagonal matrix element of B₂-irrep chirality operator Ĉ_χ between K3-doublet basis states on icosahedral cage) and its phenomenological connection (parity-violation asymmetry between left-handed and right-handed K3-doublet eigenstates) along with the technical obstacle (K3-doublet structure averaged out in conventional flavor-basis observables). Four routes (direct K3-doublet inaccessible, indirect via precision electroweak HL-LHC/FCC-ee, indirect via precision PMNS JUNO/DUNE through Q11 closure in SF-2 v2.0+, cosmological back-derivation refinement Planck-class/CMB-S4) presented in compact enumerated form rather than four multi-paragraph route entries. Net more digestible while preserving all four route descriptions.
- **Item #3** — §10 Discussion compressed: §10.3 and §10.4 methodological observations (first-programme-level-theorem-registered-ahead-of-paper-publication and Tier-4-reasoning-recovery-as-enabler) merged into single §10.3 with both observations presented as flowing-prose subparagraphs rather than separate subsections with enumerated lists. §10 intro paragraph updated from "Five topics" to "Four topics" to match the new structure. Substantive content preserved (both observations remain accessible to programme-internal readers); presentation tightened.

Source grew 1112 → 1158 lines (+46 net). Theorem environments unchanged at 6. pdflatex two-pass clean: 44 pages, 566 KB.

After v0.8 ship: paper routes to CoPilot + Grok for parallel review per restored programme practice (.tex source + framework specification); ChatGPT round-3 not required unless v0.8 introduces substantive new physics content (it does not under the disposition).

---

## Version 0.7 — 16 May 2026 (Sessions 114–115, Patches 0407 + 0408)

**v0.7 Group A — substantive physics incorporation from ChatGPT v0.6 review (Patch 0407, Session 114)**

ChatGPT v0.6 review (archived at `reviews/chatgpt_v0.6_session_113.md` per Patch 0405) identified four physics-rigor items addressed in Patch 0407:

- **Item 4 (highest leverage)** — NEW §6.6 "Why this prediction is structurally constrained" (~135 lines new content across six subsections). Enumerates framework degrees of freedom (substrate-vacuum order parameter |χ| = φ⁻³ via FI-C-9, cage-shell averaging factor |M_⊥| = d_E/V_cage = 2/12 = 1/6 via FI-C-10, substrate-physics parameter b = χ/√3 via chirality-eigenvalue matching). Shows three structural inputs compose to |M| = χ/6 with zero free parameters. Enumerates alternative outcomes (different cages → |M| = χ/12, χ/30, χ/60; different irrep content → different averaging factor; different order-parameter scale → predictions off by factor 1.6–2.6). Probabilistic-rarity argument: ~60 accessible (V_cage, d_E, |χ|) triples in framework's natural range; only one produces |M| within ±10% of empirical anchor. Converts χ/6 ↔ 0.04 match from "looks like fitting" to "structurally restricted."
- **Item 3** — §2.3 rewritten with forward-from-broken-symmetry-physics argumentation across five subsubsections. Replaced retrospective Session 87 reframing narrative with forward argument: perturbativity constraint on order parameter (broken phase must preserve geometric structure at zeroth order) → candidate scales φ⁻¹/φ⁻²/φ⁻³ enumeration → reductio for φ⁻¹ (edge-length scale, macroscopic distortion) and φ⁻² (substantial fraction of edge-length, still macroscopic) → φ⁻³ is first viable scale → three falsification modes registered.
- **Item 2** — §5.4 new physical motivation subsections before Lemma 5.3 (~100 lines). Two complementary arguments for FI-C-10's cage-shell averaging: Argument 1 substrate-isotropy + irrep averaging (A4-based) — Schur orthogonality IS mathematical expression of "no preferred direction within an irrep"; Argument 2 DI-bit propagation paths + path-averaging (A3-based) — propagation paths average over D₆ symmetry group giving same 1/6 factor. Numerical identity V_cage = |D₆| = 12 explained as same isotropy structure from two starting points. Explicit caveats: establishes plausibility + consistency with two CPP axioms; does NOT establish first-principles derivation from A1–A11 (sub-claim work §9.4) or uniqueness at theorem level.
- **Item 5** — §6.1.1 NEW experimental-signature subsection (~75 lines) enumerating four candidate routes for direct/indirect Δp_LR measurement (parity-violation K3-doublet-mediated weak processes, indirect inference from precision electroweak, cross-sector inference from precision PMNS, cosmological back-derivation refinement). New §9.5 open work item registers experimental-signature identification with three closure-route candidates spanning ~10–40 sessions.

Source grew 1188 → 1492 lines (+304 net). Theorem environments unchanged at 6. pdflatex two-pass clean: 44 pages, 518 KB.

**v0.7 Group B — writing/style + title-block cleanup (Patch 0408, Session 115)**

ChatGPT v0.6 review writing/style items addressed in Patch 0408:

- **Item 1** — Sharpened conditional-closure framing in §1.1 ("conditional theorem closure paper" stance made explicit and load-bearing in the opening paragraphs).
- **Item 6** — Compressed §1.5 (cross-sector entanglement) and §1.6 (strict-C inheritance) — left §1.1–§1.4 informative, tightened the bookkeeping subsections.
- **Item 7** — Moved inline Session/Patch metadata references to footnotes throughout §1–§8 body prose so the new-reader experience is not interrupted by programme-internal provenance markers. Bookkeeping sections (§9 open work, §10 discussion methodological observations, §11 FI summary) keep inline references where they are content rather than provenance metadata.
- **Item 8** — Compressed §9 closure-route candidate prose (removed estimated-timeline parenthetical clauses; tightened sub-claim (a)/(b)/Q11/FI-C-10/experimental subsections). Tightened §10.3/§10.4 methodological observations.

Also in Patch 0408 (not from ChatGPT review but flagged by the same review and by Thomas in Session 115 conversation):

- **Title block cleaned** — Removed visible version-history paragraph from `{\normalsize ...}` block under `{\Large Version 0.7}`. Title page now renders just title + author + Version 0.7 + date. New readers reach the abstract without ambush by version archaeology.
- **Source comment CHANGELOG block removed** — Deleted ~145 lines of `% Version 0.X -- ...` comments from top of `capotauro.tex`. Source file is significantly shorter and immediately readable.
- **This file** — Created at `flagship_papers/capotauro/documentation_suite/changelog-capotauro.md` as the canonical version archaeology going forward. v0.1–v0.7 history extracted from the removed source comments + title block paragraph.

After v0.7 ship: paper goes to ChatGPT for round-2 review (per sequential-reviewer protocol confirmed Session 113 conversation) before CoPilot + Grok reviewer round.

---

## Version 0.6 — 16 May 2026 (Session 112, Patch 0404)

Integration polish + first PDF compile pass. Fixed undefined macro `\sigmanu` defined in preamble (was used in §10.1 without definition). Verified clean two-pass pdflatex compile with all cross-references resolved and zero fatal errors. Known cosmetic remainder: hyperref "Token not allowed in PDF string" warnings for math-content section titles affect only PDF bookmark labels (the rendered PDF is correct); deferred to v0.7 polish. All eleven sections (§1 introduction through §11 FI summary) at full v0.5 draft quality from prior patches. Output: 35 pages, 481 KB.

---

## Version 0.5 — 16 May 2026 (Session 111, Patch 0403)

Expanded §9 Open Theorem-Level Work, §10 Discussion, and §11 Foundational Input Summary subsections. §9 expansion: sub-claim (a) Capotauro nucleation event (3 closure-route candidates: substrate-thermodynamic transition, coeval-with-substrate primitive, W⁰ centroid-event); sub-claim (b) substrate-vacuum symmetry-breaking dynamics (3 closure-route candidates: substrate orientation field dynamics, SS-corpus cross-sector closure, spontaneous-symmetry-breaking vs postulated-initial-bias resolution); Q11 sin²θ_13 derivation re-scoped to SF-2 v2.0+ (3 SF-2 v2.0+ closure-route candidates: candidate γ rigorous derivation, alternative-mechanism path, honest-acceptance-as-coincidence path); FI-C-10 first-principles verification (3 closure-route candidates: A3+A4 substrate-dynamics derivation, FI-C-6 + extension structural argument, Schur orthogonality + substrate-isotropy derivation); Roadmap to v2.0+. §10 expansion: programme-level pattern (integer counts and substrate primitives at 1–2% across SS-7/SM-9/SF-4/Capotauro); cross-sector implications across five CPP sectors; methodological observation on first programme-level theorem registered ahead of paper publication; methodological observation on Tier 4 reasoning recovery as enabler; outlook on 2026–2032+ experimental landscape (JUNO, HL-LHC, CMB μ-distortion, direct parity-violation, η_B refinement). §11 expansion: full ten-input FI summary (FI-C-1 through FI-C-10) with source paper + rigor level + falsifier mapping.

---

## Version 0.4 — 16 May 2026 (Session 110, Patch 0402)

Expanded §6 Primary Empirical Prediction Δp_LR = χ/6, §7 sin²θ_13 Posture (re-scoped to SF-2 v2.0+), and §8 Cumulative Falsifier Set subsections. §6 expansion: Δp_LR observed value (leptogenesis back-derived from η_B); Δp_LR predicted value from THEO-CAP-1 with eight-step verification chain; what 2% agreement means in three honest framings (structural-numerical consistency vs precision lab test; back-derivation framework as source of uncertainty; future direct-measurement falsifier). §7 expansion: Sessions 99–101 trajectory and candidate γ observation; the linear-vs-quadratic scaling tension surfaced (standard PMNS perturbation predicts |M|²~0.001, off by factor ~21); attempts considered and ruled out; Session 101 Patch 0395 re-scoping decision; candidate γ registered as numerical conjecture pending SF-2 v2.0+ closure. §8 expansion: empirical falsifier (Δp_LR outside ±2% of χ/6 ≈ 0.0394); framework-level falsifiers (FI-C-3 K3-doublet basis falsification; FI-C-9 substrate-vacuum order parameter falsification; FI-C-10 cage-shell averaging falsification; cross-sector falsifier on SF-2 W⁰ catalyst framework parameters).

---

## Version 0.3 — 16 May 2026 (Sessions 108–109, Patch 0401)

Expanded §4 D₆ Stabilizer and Wigner-Eckart Framework + §5 Composite Capotauro Wigner-Eckart Theorem. §4 expansion: K3 stabilizer D₆ = S₃ × ℤ₂ derivation; chirality-preserving subgroup S₃' ⊂ D₆ identification (Session 89 Finding C-W7 correction from naive C₆ framing); irreducible representations of D₆ with character table; Wigner-Eckart on D₆ general formula; σ₁-ODD operator parameterization correction (Session 95 Patch 0389 — naive (a,b)-parameterization captures both A₂ and E irrep components; C_χ ∈ B₂ of D₆ requires K3-amplitude in A₂ specifically). §5 expansion: Theorem 18.1 (Composite Capotauro Wigner-Eckart Theorem) statement; eight-step proof overview; K3-amplitude factor (chirality-eigenvalue matching principle: |M_K3| = χ); cage-shell averaging factor (cage-shell averaging principle: |M_⊥| = 1/6); composition |M| = |M_K3| · |M_⊥| = χ/6; structural-numerical agreement χ/6 = φ⁻³/6 ≈ 0.0394 with observed Δp_LR ≈ 0.04 within 2%.

---

## Version 0.2 — 16 May 2026 (Session 107, Patch 0400)

Expanded §2 Substrate-Vacuum Broken-Symmetry Physics + §3 K3-Doublet and Chirality Observable. §2 expansion: H₄ → I₄ chirality ℤ₂ symmetry breaking at the 600-cell substrate level; order parameter |χ| = φ⁻³ registered as foundational input FI-C-9 (Session 87 Patch 0381); chi inconsistency resolution at φ⁻³ via natural distance-ratio bias of broken phase (forward argument added at v0.7); empirical anchor and cosmological context (leptogenesis back-derived Δp_LR ≈ 0.04 from η_B). §3 expansion: K3 base structure and four-cage taxonomy (FI-C-2 inherited from SM-1); K3-doublet TBM-aligned basis (FI-C-3 inherited from SF-4 v4.0 Composite K3-Cage-Shell Coupling Theorem); perpendicular wavefunction structure χ₊, χ₋ (Session 91 Patch 0385 extension to FI-C-3); chirality observable C_χ definition (B₂ of D₆ irrep, σ₁ζ-EVEN pairing convention via Session 91 Finding C-W12); full K3-doublet basis states for matrix element.

---

## Version 0.1 — 16 May 2026 (Session 105, Patch 0399)

Initial .tex source from Session 104 Patch 0398 outline. Paper structure across 11 sections: §1 Introduction and Strategic Frame; §2 Substrate-Vacuum Broken-Symmetry Physics; §3 K3-Doublet and Chirality Observable; §4 D₆ Stabilizer and Wigner-Eckart Framework; §5 Composite Capotauro Wigner-Eckart Theorem; §6 Primary Empirical Prediction Δp_LR = χ/6; §7 sin²θ_13 Posture (Re-scoped to SF-2 v2.0+); §8 Cumulative Falsifier Set; §9 Open Theorem-Level Work; §10 Discussion; §11 Foundational Input Summary. Preamble + bibliography + section skeleton; substantive content per section deferred to v0.2–v0.7. v0.1 anchors the paper structure and bibliography (~14 internal CPP references + ~5 external physics references). Theorem-registry anchor: THEO-CAP-1 registered Session 103 Patch 0397 in `theorem-registry.md`.

---

## Working sketches (source-of-truth Tier 4 reasoning)

The substantive physics content captured in v0.1–v0.7 paper text was developed across Sessions 87–102 in two working sketches:

- **Parent sketch**: `flagship_papers/capotauro/sketches/Capotauro_chi_phi_closure.md` (681 lines) — the overall closure-trajectory framework, FI-C-1 through FI-C-10 enumeration, eight-step proof outline at the strategic level, and Session 87 Patch 0381 reframing decision at φ⁻³.
- **Sub-claim (c) working sketch**: `flagship_papers/capotauro/sketches/Capotauro_subclaim_c_wigner_eckart.md` (2146 lines) — the detailed Wigner-Eckart derivation, the K3-doublet basis structure, the σ₁-ODD operator parameterization correction, the wavefunction-spread arguments, and Theorem 18.1 statement + proof. The v0.x paper text is the publication-grade form of this sketch.

Both sketches remain canonical Tier 4 reasoning sources; the .tex paper is the external-audience packaging.

---

## Patch register

| Patch | Session | Version | Type | Summary |
|:---:|:---:|:---:|:---|:---|
| 0397 | 103 | — | Programme | THEO-CAP-1 registered in `theorem-registry.md` (first SF-Line theorem registered ahead of own flagship paper) |
| 0398 | 104 | — | Paper | `capotauro_outline.md` created (327 lines) |
| 0399 | 105 | v0.1 | Paper | `capotauro.tex` initial .tex source + preamble + section skeleton + bibliography |
| 0400 | 107 | v0.2 | Paper | §2 substrate-vacuum + §3 K3-doublet content expansion |
| 0401 | 108–109 | v0.3 | Paper | §4 D₆ Wigner-Eckart + §5 composite WE theorem content expansion |
| 0402 | 110 | v0.4 | Paper | §6 Δp_LR + §7 sin²θ_13 posture + §8 falsifier set content expansion |
| 0403 | 111 | v0.5 | Paper | §9 open work + §10 discussion + §11 FI summary content expansion |
| 0404 | 112 | v0.6 | Paper | Integration polish + first PDF compile (35 pages, 481 KB) |
| 0405 | 113 | — | Review | ChatGPT v0.6 review archived at `reviews/chatgpt_v0.6_session_113.md` |
| 0406 | 113 | — | Programme | Programme-infrastructure Grok-suspension-warning cleanup (out-of-scope but timed in session) |
| 0407 | 114 | v0.7 (Group A) | Paper | Substantive physics rework: §6.6 nontriviality + §2.3 forward argument + §5.4 motivation + §6.1.1 experimental + §9.5 experimental open work |
| 0408 | 115 | v0.7 (Group B) | Paper | Writing/style + title-block cleanup + this changelog file creation + ships v0.7 PDF for ChatGPT round-2 |
| 0409 | 116 | — | Programme | Programme-infrastructure standardization of changelog-architecture convention (codifies Patch 0408 reference implementation as programme-wide rule across `operating_system.md` + `paper-formatting.md` + `documentation-suite.md` + `paper_production_workflow.md` + `paper_completion_checklist.md` + `bootup.md`; forward-only migration policy) |
| 0410 | 117 | — | Review | ChatGPT v0.7 round-2 review archived at `reviews/chatgpt_v0.7_session_117.md` (overall strongly positive; four remaining issues mapped to v0.8 disposition table) |
| 0411 | 118 | v0.8 | Paper | Substantive expositional polish — all five ChatGPT v0.7 items: NEW §1.7 derivation-flow TikZ figure + §1.2 cross-reference to §6.6 + §5.4 FI-C-6 precedent argument for FI-C-10 + §6.1.1 tightening + §10 methodological observations merged into single subsection |
| 0412 | 119 | — | Review | Three v0.8 reviews archived in parallel: ChatGPT round-3 at `reviews/chatgpt_v0.8_session_119.md` (mature conditional-theorem flagship paper; 4 problems carry-over from v0.7, 5 v0.9 items, 2 are discoverability gaps), CoPilot round-1 at `reviews/copilot_v0.8_session_119.md` (extremely close to v1.0 ship-ready; 5 tightening items, includes `gandolfi_2025` citation veridicality verification flag), Grok round-1 at `reviews/grok_v0.8_session_119.md` (Ship as v1.0; 4 minor polish items, 2025 Grok co-authorship footnote concern, higher-n undershoot quantification); strong cross-reviewer convergence on ship-readiness with light v0.9 polish pass |
| 0413 | 120 | v0.9 | Paper | v0.9 polish + foundational framing reframe: §2 reframed from "Substrate-Vacuum Broken-Symmetry Physics" to "Substrate-Vacuum Chirality as Primitive Feature" per CPP-core-principle methodological commitment that mathematical descriptions are not physical mechanisms; SSB framing demoted to mathematical-equivalence alternative in Remark 2.2; sub-claim (b) renamed from "symmetry-breaking dynamics derivation" to "substrate chirality mechanism candidate derivation" with geometric-chirality candidate (preferred 4D direction) registered + working sketch `Capotauro_chiral_mechanism_candidate.md` bibliography entry added; sub-claim (a) clarified as universe-wide sign-selection event downstream of sub-claim (b) magnitude mechanism; gandolfi_2025 citation removed (unverified, web_search confirmed no matching paper) + §2.4 empirical-anchor paragraph rewritten; 8 ADDRESS items + 2 DISCOVERABILITY items from v0.8 cross-reviewer disposition: author-line 2025 Grok co-authorship footnote (Grok #1), §2.3.4 higher-n undershoot quantification φ⁻⁴≈39% + φ⁻⁵≈63% (Grok #2), §1.7 TikZ arrow label refinement (Grok #3), NEW §2.3 "Falsifying FI-C-9 directly" subsection (CoPilot #4), §3 chirality-observable C_χ physical-meaning paragraph (CoPilot #2), §5.4 intuition-for-1/6 paragraph (CoPilot #3) + Arguments 1-3 ~20% compression (CoPilot #1), §6 CEERS paragraph removed (CoPilot #5a), §10 + §9.6 Roadmap further 15-20% compression (ChatGPT #4), §1.2 + §1.7 cross-reference (ChatGPT discoverability), residual broken-symmetry-language cleanup throughout abstract + plain-English summary + §5 + §6 + §8 + §9 + §13; 1149 lines (-9 from v0.8); 46 pages 601 KB; theorem count unchanged at 6; pdflatex two-pass compile VERIFIED CLEAN |
| 0414 | 121 | — | Sketch | NEW working sketch `sketches/Capotauro_chiral_mechanism_candidate.md` (296 lines) developing Reading C as the candidate physical mechanism for FI-C-9's primitive chirality: a primitive 4D direction n̂ in the substrate's ambient 4D space produces direction-correlated edge-length variation in the 600-cell lattice at the φ⁻³ scale; the H₄ → I₄ algebraic structure is the structural consequence of n̂ being primitive, not the outcome of a dynamical event; the chirality magnitude |χ| = φ⁻³ is derived rather than postulated, via the perturbative-distance-ratio constraint applied to the n̂-perturbation; new structural prediction of fractional chirality retention across observable classes (mass observables retain O(χ²) ≈ 0.6%; chirality observables retain full χ/6 ≈ 4%; intermediate observables retain calculable fractions); five open questions registered for sub-claim (b) closure trajectory (group-theoretic verification of H₄ → I₄ stabilizer claim; perturbative-distance-ratio sharpening under Reading C; cross-sector consistency with SF-2 W bracelet and SM-2 qDP/eDP asymmetry; sub-claim (a) cosmological-timing interaction). Tier-4 reasoning capture at Layer 1 / Layer 2 epistemic status (physical intuition + structural mathematical sketching), not Layer 3 (formal theorem closure). The sketch is the working development of the v0.9 paper's §9.2 sub-claim (b) "substrate chirality mechanism candidate derivation"; v2.0+ paper trigger is the closure of Question 1 (group-theoretic verification) at minimum. 2 files changed +298 / -1. |
| 0415 | 122 | **v1.0 (SHIPPED)** | Paper | **Capotauro paper v1.0 SHIPPED** as the third flagship paper to ship at v1.0 after SS-9 / SF-4 / SF-2; first flagship paper outside the SF-N numerical convention. Substantive paper content unchanged from v0.9 (Patch 0413); `capotauro.tex` title block updated `Version 0.9 --- 16 May 2026` → `Version 1.0 (SHIPPED) --- 16 May 2026` (all other paper content preserved; the paper body already references v1.0 throughout via the closure trajectory's forward-targeting language). Programme-level changes across registry files: (1) `Research_Frontier.md` OPEN-SM-4 status field updated noting v1.0 SHIP (PARTIAL CLOSURE status preserved; sub-claims (a) and (b) remain open); (2) `Research_Frontier.md` NEW OPEN-FI-C-9-FP-MECHANISM entry registered in FP section (Reading C geometric-chirality candidate at Tier-4 Layer 1/2 sketch level; Layer 3 closure trajectory estimated 10-20 sessions); FP-section problem count 8 → 9; (3) `theorem-registry.md` Last-updated header updated noting THEO-CAP-1 paper-level confirmation at v1.0 SHIP (theorem registered Session 103 Patch 0397 ahead of paper publication; v1.0 SHIP confirms registered theorem now has flagship-paper venue); Summary Statistics SF-Line row UNCHANGED at 10 theorems + 7 propositions + 1 lemma; Total theorem count UNCHANGED at 62; (4) `paper_catalog.md` SF-Line section updated with new Capotauro row at v1.0 SHIPPED + Capotauro documentation paragraph; (5) `INDEX.md` flagship_papers section updated with Capotauro entry at v1.0 SHIPPED; (6) NEW `flagship_papers/capotauro/README.md` paper-level README at v1.0 SHIPPED transition (parallel to README pattern at `flagship_papers/neutrinos/README.md` and `flagship_papers/electroweak/README.md`); (7) this changelog file v1.0 SHIP version section added + Patch 0415 register row (this row) + Last-updated footer updated. Cross-reviewer convergence on SHIP-readiness achieved at v0.8 Session 119 Patch 0412 (ChatGPT round-3 + CoPilot round-1 + Grok round-1 SHIP-ready verdicts); v0.9 polish Patch 0413 incorporated 8 ADDRESS + 2 DISCOVERABILITY items + foundational framing reframe of §2 from SSB to primitive-feature framing. **Out-of-scope at v1.0**: sub-claim (a) Capotauro nucleation event; sub-claim (b) substrate chirality mechanism candidate derivation (tracked at OPEN-FI-C-9-FP-MECHANISM); FI-C-10 first-principles derivation; PMNS reactor mixing angle sin²θ_13 re-scoped to SF-2 v2.0+; δ_CP and η_B downstream sub-claim work. **Forward queue post-Session 122 close**: Patches 0416+ documentation suite production (7 companion files + verification notebooks + transcripts + OSF deposit + arXiv submission per `templates/paper_completion_checklist.md`); sub-claim (b) Q1 group-theoretic verification next substrate-physics session (1-3 sessions estimated); anthology chapter at Rovelli/SciAm register; TATWD integration to `CPP_the_theory.md`; SF-4 v4.5+ Capotauro integration per Grok Session 119 next steps; ClearPC PDF compile + public posting at Thomas's discretion. |

---

*Last updated: Session 122, Patch 0415 (16 May 2026) — Capotauro paper v1.0 SHIPPED*
