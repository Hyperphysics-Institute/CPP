# Changelog: Capotauro flagship paper

**Paper**: The Capotauro Mechanism: Chirality on the K3-Doublet from Substrate-Vacuum Broken-Symmetry Physics
**Source**: `flagship_papers/capotauro/capotauro.tex`
**Programme registration**: THEO-CAP-1 (Session 103 Patch 0397, theorem #62 in `theorem-registry.md`)
**OPEN-SM-4 status at registration**: PARTIAL CLOSURE — sub-claim (c) v1.0 closed; sub-claims (a) and (b) remain open
**Maintainer**: Thomas Lee Abshier ND, Hyperphysics Institute

This file is the canonical version archaeology for the Capotauro paper. Each `capotauro.tex` patch updating the paper source adds a one-line summary entry below. Substantive detail lives in the patch commit messages; this file is the curated narrative for researchers tracing the closure trajectory.

The `.tex` source itself carries only its current title block (title + author + version + date). Paper-level CHANGELOG comment blocks and visible PDF-rendered version-history paragraphs were removed at Patch 0408 (Session 115) per the convention that programme-internal version archaeology belongs alongside development/transcript/reasoning files in the documentation suite, not in the paper source.

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

---

*Last updated: Session 117, Patch 0410 (16 May 2026)*
