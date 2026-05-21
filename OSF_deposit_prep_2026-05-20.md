# OSF Deposit Prep — Session 137 Close

**Date prepared**: 20 May 2026
**Window**: Session 137 close
**Author of prep**: Opus (Claude)
**Action owner**: Thomas Lee Abshier, ND
**Target deposits**: Capotauro v1.0 + Capotauro v2.0 v1.0 + Chirality Continuum v1.0
**Parent project**: Hyperphysics Institute / Conscious Point Physics, OSF DOI 10.17605/OSF.IO/JXE8D

---

## How to use this document

Each paper has a section with deposit-ready materials. Sit down at the OSF web interface, create a new component under the Hyperphysics Institute / CPP parent project for each paper, and paste the materials section-by-section into the OSF fields. Each paper section is self-contained — no cross-referencing needed during the deposit action.

**Order of deposits recommended**: Capotauro v1.0 first (oldest; sets the cross-link target for v2.0), then Capotauro v2.0 (links forward from v1.0), then Chirality Continuum v1.0 (links forward from Capotauro v2.0). This matches the substantive dependency chain.

**OSF deposit workflow per component**:
1. Create new component under parent project JXE8D
2. Title: paste **Component Title** field below
3. Description: paste **OSF Description** field
4. Tags: paste **Tags** list
5. Contributors: Thomas Lee Abshier, ND (Hyperphysics Institute)
6. License: CC-BY 4.0 (matches existing CPP component licenses per SM-6 + SM-7 convention)
7. Upload files per **Files to Upload** list
8. Mint component DOI (OSF auto-mints; record the DOI here after deposit)
9. Set component visibility to Public

**Parallel Zenodo deposit** (if desired): each section also includes Zenodo-format metadata. Zenodo accepts DOI-minted on deposit; cross-link to OSF DOI in Zenodo "Related Identifiers" field. arXiv submission abstract candidates are also included for each paper.

**Post-deposit action items** (track separately):
- Update `paper_catalog.md` row "OSF pending" → "Registered on OSF" with component DOI
- Update `INDEX.md` entries with component DOI cross-links
- Update `research_frontier.md` deposit-status markers

---

# 1. Capotauro v1.0

## Component Title (OSF "Title" field)

```
Capotauro: Substrate-Vacuum Chirality on the K3-Doublet (v1.0)
```

## OSF Description (OSF "Description" field; ~400 words)

The Capotauro paper closes sub-claim (c) of OPEN-SM-4 — the foundational open problem of Conscious Point Physics' substrate-vacuum chirality sector — by deriving the matrix element that governs parity violation acting on charged leptons. The derivation produces |M| = χ/6 = φ⁻³/6 ≈ 0.0394 at zero free parameters, where χ = φ⁻³ ≈ 0.236 is the substrate's primitive chirality magnitude (a foundational input at v1.0; derived from a perturbative-distance-ratio constraint on n̂-induced edge perturbations of the 600-cell lattice) and 1/6 = d_Γ/V_cage is the cage-shell averaging factor set by the orbit count of the icosahedral stabilizer on the K3 doublet. The empirical anchor is leptogenesis CP-asymmetry Δp_LR ≈ 0.04, back-derived from the observed cosmological baryon asymmetry through standard sphaleron-equilibration kinematics; the framework prediction matches within 2%.

The closure is a conditional theorem (THEO-CAP-1, the Composite Capotauro Wigner-Eckart Theorem) on a 10-foundational-input stack (FI-C-1 through FI-C-10) and 4 CPP axioms (A1, A3, A4, A7). The decomposition of OPEN-SM-4 into three sub-claims — (a) cosmological-event derivation, (b) primitive chirality magnitude derivation, (c) observable-translation derivation — is part of the contribution: it identifies (c) as the sub-claim that does not depend on substrate-dynamics machinery the framework has not yet built, and shows that closing (c) requires only the substrate's primitive chirality magnitude taken as given, the K3-doublet basis structure, and the icosahedral stabilizer's orbit-counting on cage shells.

The paper is the third CPP flagship to ship at v1.0 (after SS-9 and SF-4 v4.4) and the first flagship to ship outside the SF-N numerical convention. The THEO-CAP-N theorem-naming convention reflects the flagship-paper-pending status preserved through v1.0 ship. The companion paper Capotauro v2.0 (separate OSF component) extends the v1.0 single-sector closure to a three-way substrate-level cross-sector unification (K3 doublet + W-bracelet + qDP/eDP), all sharing the same substrate-handle magnitude χ/6.

46 pages compiled (601 KB PDF). 1149 lines source. Six theorem-family environments. 11-route falsifier inventory. Cross-reviewer convergence on ship-ready verdict achieved at v0.8 (ChatGPT round-3 + CoPilot round-1 + Grok round-1 ship-ready verdicts).

## Tags

```
conscious-point-physics, 600-cell, substrate-chirality, K3-doublet, parity-violation, weak-interaction, leptogenesis, Wigner-Eckart, golden-ratio, zero-parameter-prediction, CPP, derivational-physics, capotauro, OPEN-SM-4
```

## Files to Upload

| File | Source path | Role |
|------|-------------|------|
| `capotauro_v1.0.pdf` | (compiled from `flagship_papers/capotauro/capotauro.tex` at v1.0 commit) | Primary deposit artifact |
| `capotauro_v1.0.tex` | `flagship_papers/capotauro/capotauro.tex` at v1.0 commit (Patch 0415) | LaTeX source |
| `cpp_references.bib` | `bibliography/cpp_references.bib` at v1.0 commit | Bibliography |
| `mechanism-capotauro.md` | `flagship_papers/capotauro/documentation_suite/mechanism-capotauro.md` | Companion: substrate mechanism narrative |
| `phenomena-capotauro.md` | `flagship_papers/capotauro/documentation_suite/phenomena-capotauro.md` | Companion: empirical anchors |
| `philosophy-capotauro.md` | `flagship_papers/capotauro/documentation_suite/philosophy-capotauro.md` | Companion: epistemology |

**Compile note**: PDF must be compiled fresh on ClearPC per Binary Artifact Workflow before deposit. Use two-pass pdflatex (cross-references resolve on pass 2). Verify 46 pages compiled / 601 KB output before upload.

## arXiv Submission Abstract Candidate (250 words)

```
We close sub-claim (c) of OPEN-SM-4 — the foundational open problem governing parity-
violation observables in Conscious Point Physics' substrate-vacuum chirality sector — by
deriving the matrix element |M| = χ/6 = φ⁻³/6 ≈ 0.0394 at zero free parameters between
opposite-parity K3-doublet substrate states. The substrate's primitive chirality magnitude
χ = φ⁻³ enters as a foundational input (v1.0); the cage-shell averaging factor 1/6 = d_Γ/V_cage
follows from the orbit count of the icosahedral stabilizer on the K3 doublet. The empirical
anchor is leptogenesis CP-asymmetry Δp_LR ≈ 0.04 back-derived from the cosmological baryon
asymmetry via standard sphaleron-equilibration kinematics; the framework prediction matches
within 2%. The closure is a conditional theorem (Composite Capotauro Wigner-Eckart Theorem)
on a 10-foundational-input stack and 4 CPP axioms. OPEN-SM-4 sub-claims (a) cosmological-
event and (b) primitive-magnitude derivation remain open; the decomposition framework
identifies these as separable from sub-claim (c) and not blocking the present closure. The
paper is the third CPP flagship at v1.0 and the first outside the SF-N family/sector
numerical convention. A companion paper (Capotauro v2.0) extends the present single-sector
closure to a three-way substrate-level cross-sector unification across K3-doublet,
W-bracelet, and qDP/eDP sectors; a downstream paper (Chirality Continuum v1.0) closes the
Layer 4 effective-field-theory bridge from substrate to observable scales for two of the
three sectors.
```

## arXiv Categories (recommended)

```
Primary: hep-ph (high-energy physics phenomenology)
Cross-listed: hep-th (high-energy physics theory), gr-qc (general relativity / quantum cosmology, for leptogenesis anchor)
```

## Zenodo Metadata Equivalent

- **Title**: Capotauro: Substrate-Vacuum Chirality on the K3-Doublet (v1.0)
- **Authors**: Abshier, Thomas Lee (Hyperphysics Institute)
- **Description**: (use OSF Description text above)
- **Keywords**: (use Tags list above)
- **License**: Creative Commons Attribution 4.0 International (CC-BY 4.0)
- **Related identifiers**: OSF parent project DOI 10.17605/OSF.IO/JXE8D ("isPartOf"); Capotauro v2.0 OSF component DOI ("isPreviousVersionOf"); Chirality Continuum v1.0 OSF component DOI ("hasPart")
- **Resource type**: Publication / Working paper

---

# 2. Capotauro v2.0 v1.0

## Component Title (OSF "Title" field)

```
Capotauro v2.0: Three-Way Cross-Sector Substrate-Level Unification of Mass-Mixing Chirality, Electroweak V−A, and Electromagnetic Handedness
```

## OSF Description (OSF "Description" field; ~450 words)

Capotauro v2.0 extends the v1.0 single-sector closure of sub-claim (c) of OPEN-SM-4 to a three-way substrate-level cross-sector unification: the same substrate-handle magnitude |M| = χ/6 = φ⁻³/6 ≈ 0.0394 is shown to govern three structurally distinct observable manifestations across three different substrate sectors. The K3-doublet sector governs mass-mixing chirality (the v1.0 closure, preserved). The W-bracelet sector governs the electroweak V−A coupling at the substrate-handle level (Theorem THEO-SD-CHIR-1). The qDP/eDP sector governs the electromagnetic-handedness chiral-polarity-bias at the substrate-handle level (Theorem THEO-SD-CHIR-2). All three sectors derive the same numerical magnitude through three different mechanisms — the v2.0 substantive contribution.

Two new Reading-C foundational inputs are introduced and registered: FI-C-RC-1 (primitive 4D direction n̂ in the substrate's ambient four-space) and FI-C-RC-2 (vertex-aligned reading n̂ = v_host at Layer 2 via three converging arguments). These ground the substrate's primitive chirality magnitude χ = φ⁻³ at a sharper epistemic position than the v1.0 free-magnitude postulate; FI-C-9 of v1.0 thus inherits its magnitude rather than postulating it. The 12-foundational-input v2.0 inventory (10 v1.0 FIs preserved + FI-C-RC-1 + FI-C-RC-2) is the operational stack for v2.0 closures.

The 11-route falsifier inventory at §13.4 extends the v1.0 5-route inventory. Each route maps a measurable observable threshold to the theorem(s) it would disconfirm via cascade backward through the substrate-handle identification. Falsifier 6 in particular (Michel ρ + massless-helicity V+A admixture + leptogenesis CP-asymmetry) anticipates the Layer 4 effective-field-theory bridge that the downstream paper Chirality Continuum v1.0 establishes; Falsifier 6 activated as operative at Chirality Continuum v1.0 ship.

The paper is the first CPP flagship to undergo a substantive v2.0 extension — not a polish or reviewer-feedback revision, but a structural extension that grounds an existing foundational input at a sharper epistemic position and extends the v1.0 single-sector closure to a multi-sector unification under an umbrella registration (OPEN-SD-CHIR-PRIMITIVE). v1.0 SHIPPED status is preserved as historical archival state.

1870 lines source. 51+ pages compiled. Three-reviewer convergence on ship-ready verdict achieved at v0.9 reviewer cycle (ChatGPT round-2 maturation confirmation + Grok round-1 ship-acceptable + CoPilot round-1 ship-acceptable). Three new theorems (THEO-CAP-1 preserved from v1.0 + THEO-SD-CHIR-1 + THEO-SD-CHIR-2); 11-route falsifier set; master architecture figure at §3.5; dynamical-engine framing at §13.6 identifying the next programme gate (Q1′+Q1′.A Layer 3 promotion of n̂ + |χ| = φ⁻³).

## Tags

```
conscious-point-physics, 600-cell, substrate-chirality, K3-doublet, W-bracelet, qDP-eDP, cross-sector-unification, OPEN-SD-CHIR-PRIMITIVE, golden-ratio, zero-parameter-prediction, CPP, parity-violation, capotauro, Reading-C, dynamical-substrate-law
```

## Files to Upload

| File | Source path | Role |
|------|-------------|------|
| `capotauro_v2.0_v1.0.pdf` | (compiled from `flagship_papers/capotauro/capotauro.tex` at v2.0 v1.0 commit Patch 0479) | Primary deposit artifact |
| `capotauro_v2.0_v1.0.tex` | `flagship_papers/capotauro/capotauro.tex` at v2.0 v1.0 commit | LaTeX source |
| `cpp_references.bib` | `bibliography/cpp_references.bib` at v2.0 v1.0 commit | Bibliography |
| `changelog-capotauro.md` | `flagship_papers/capotauro/documentation_suite/changelog-capotauro.md` | Version archaeology v1.0 → v2.0 v1.0 |
| `mechanism-capotauro.md` | `flagship_papers/capotauro/documentation_suite/mechanism-capotauro.md` | Companion: substrate mechanism (extended for v2.0) |
| `phenomena-capotauro.md` | `flagship_papers/capotauro/documentation_suite/phenomena-capotauro.md` | Companion: 11-route falsifier inventory |
| `philosophy-capotauro.md` | `flagship_papers/capotauro/documentation_suite/philosophy-capotauro.md` | Companion: epistemology of v2.0 extension |
| `capotauro_what_was_always_there.md` | `book_project/chapters/capotauro_what_was_always_there.md` | Anthology chapter at Rovelli register |

**Compile note**: PDF must be compiled fresh on ClearPC per Binary Artifact Workflow.

## arXiv Submission Abstract Candidate (250 words)

```
We extend the v1.0 single-sector closure of sub-claim (c) of OPEN-SM-4 in Conscious Point
Physics to a three-way substrate-level cross-sector unification. The same substrate-handle
magnitude |M| = χ/6 = φ⁻³/6 ≈ 0.0394 governs three structurally distinct observable
manifestations across three different substrate sectors: mass-mixing chirality on the
K3 doublet (preserved from v1.0), electroweak V−A coupling at the W-bracelet level
(THEO-SD-CHIR-1), and electromagnetic-handedness chiral-polarity-bias at the qDP/eDP level
(THEO-SD-CHIR-2). All three sectors derive the same numerical magnitude through three
different mechanisms — the substantive v2.0 contribution. Two new Reading-C foundational
inputs (FI-C-RC-1: primitive 4D direction n̂; FI-C-RC-2: vertex-aligned reading) ground
the substrate's primitive chirality magnitude χ = φ⁻³ at a sharper epistemic position than
the v1.0 free-magnitude postulate. The 11-route falsifier inventory extends the v1.0
5-route inventory; Falsifier 6 anticipates the Layer 4 effective-field-theory bridge
established in the downstream paper Chirality Continuum v1.0. The dynamical-substrate-law
gate (Q1′+Q1′.A Layer 3 promotion of n̂ + |χ| = φ⁻³ from CPP primitive axioms) is identified
in §13.6 as the next programme gate; closure would retire FI-C-RC-1 and FI-C-RC-2 from
foundational inputs to theorems. This is the first CPP flagship to undergo a substantive
v2.0 extension; v1.0 is preserved as historical archival state at a separate OSF component.
```

## arXiv Categories

```
Primary: hep-ph
Cross-listed: hep-th, gr-qc
```

## Zenodo Metadata Equivalent

- **Title**: Capotauro v2.0: Three-Way Cross-Sector Substrate-Level Unification
- **Authors**: Abshier, Thomas Lee (Hyperphysics Institute)
- **Description**: (use OSF Description text above)
- **Keywords**: (use Tags list above)
- **License**: CC-BY 4.0
- **Related identifiers**:
  - OSF parent JXE8D ("isPartOf")
  - Capotauro v1.0 OSF component DOI ("isNewVersionOf")
  - Chirality Continuum v1.0 OSF component DOI ("hasPart"; v2.0 substrate-level closures inform CC v1.0 Layer 4 bridge)
- **Resource type**: Publication / Working paper

---

# 3. Chirality Continuum v1.0

## Component Title (OSF "Title" field)

```
Chirality Continuum from Substrate to Observable EFT: Joint Layer 4 Closure of OPEN-FP-SF-2-CHIR (Electroweak V−A Coupling) and SM-2 v2.0+ (Quark Chiral-Polarity-Bias) from |M| = χ/6 (v1.0)
```

## OSF Description (OSF "Description" field; ~500 words)

The Chirality Continuum paper closes the Layer 4 effective-field-theory bridge from substrate-handle magnitude χ/6 ≈ 0.0394 to observable Standard Model scales for two of the three sectors that Capotauro v2.0 v1.0 unified at substrate level: the W-bracelet sector (electroweak V−A coupling, closing OPEN-FP-SF-2-CHIR at full Layer 4 rigor) and the qDP/eDP sector (chiral-polarity-bias, jointly closing SM-2 v2.0+). The bridge is built once at sector-agnostic level via three programme-level theorems (THEO-CHIR-CONT-1 substrate-handle-to-effective-coupling bridge; THEO-CHIR-CONT-2 W-bracelet V−A coupling closure; THEO-CHIR-CONT-3 qDP/eDP chiral-polarity-bias closure) and then applied twice.

The bridge depends on a small universal substrate-level dataset: the substrate-handle magnitude |χ|, the cage-shell averaging factor d_Γ/V_cage = 1/6, and the ζ-parity matching between sector pairing conventions and continuum-limit operators. Everything sector-specific attaches to this universal dataset after the bridge is built.

The central recognition moment of the closure trajectory is that magnitude inheritance |M^eff| = χ/6 at leading order does not require renormalization-group integration from the substrate cutoff down to electroweak scales. The substrate handle χ/6 is a topological substrate quantity (Definition 15.1.1): preserved exactly under continuum-limit projection via the standard QFT protection-of-topological-quantities principle (Adler-Bardeen anomaly coefficients exact at all loop orders; topological charges in θ-vacuum sectors; Chern-Simons levels; Atiyah-Singer index theorem; discrete symmetry parities). The topological-projection argument bypasses the substrate-dynamics machinery the framework has not yet built.

Empirical predictions: Michel ρ = 3/4 within 0.3σ of PDG 2024 (ρ_obs = 0.7497 ± 0.0010); 100% LH at massless helicity limit consistent with all LEP and LHC observables; leptogenesis CP-asymmetry Δp_LR ≈ 0.0394 within 2% of BAU back-derivation. Capotauro Falsifier 6 (anticipated at Capotauro v2.0 §13.4) activated as operative with three thresholds: (A) Michel ρ at 3×10⁻³ deviation; (B) massless-helicity V+A admixture at 3×10⁻² combined sensitivity; (C) leptogenesis Δp_LR at 0.015 deviation. Cross-sector convergence at observable scale §6.5: single primary observable (leptogenesis CP-asymmetry) validates both Layer 4 closures via different physical channels — framed as structural prediction of the joint-paper format.

The paper is the sixth CPP flagship at v1.0 in seven weeks, the second Layer 4 cross-sector closure (after SF-4 v4.0), and the first with ex ante joint-paper format adoption at the viability decision gate. It is the first CPP flagship in programme history to achieve three-reviewer convergence on ship-acceptable verdict at first reviewer round each (ChatGPT round-2 + Grok round-1 + CoPilot round-1; previous flagships required multi-round cycles).

38 pages compiled (659 KB PDF). 1265 lines source. Three theorems + four methods + 15 foundational inputs (FI-CHIR-CONT-1 through -15 inherited from Capotauro v2.0 + SF-2 v1.0 + SM-2 v1.0). The dynamical-substrate-law gate (Q1′+Q1′.A Layer 3 promotion of n̂ + |χ| = φ⁻³) is identified by all three external reviewers as the defining next programme gate.

## Tags

```
conscious-point-physics, 600-cell, chirality-continuum, substrate-handle, Layer-4-EFT, V-minus-A, Michel-parameter, leptogenesis, chiral-polarity-bias, topological-projection, Wilson-Fisher, golden-ratio, zero-parameter-prediction, CPP, OPEN-FP-SF-2-CHIR, OPEN-SD-CHIR-PRIMITIVE, joint-paper-format
```

## Files to Upload

| File | Source path | Role |
|------|-------------|------|
| `chirality_continuum_v1.0.pdf` | (compiled from `flagship_papers/chirality_continuum/chirality_continuum.tex` at v1.0 commit Patch 0509) | Primary deposit artifact |
| `chirality_continuum_v1.0.tex` | `flagship_papers/chirality_continuum/chirality_continuum.tex` at v1.0 commit | LaTeX source |
| `cpp_references.bib` | `bibliography/cpp_references.bib` at deposit-time commit | Bibliography (includes 13 new bibitems added at Patch 0516) |
| `changelog-chirality_continuum.md` | `flagship_papers/chirality_continuum/documentation_suite/changelog-chirality_continuum.md` | Full version archaeology Patches 0482–0509 |
| `mechanism-chirality_continuum.md` | `flagship_papers/chirality_continuum/documentation_suite/mechanism-chirality_continuum.md` | Companion: substrate-handle-to-effective-coupling bridge mechanism |
| `phenomena-chirality_continuum.md` | `flagship_papers/chirality_continuum/documentation_suite/phenomena-chirality_continuum.md` | Companion: Capotauro Falsifier 6 three operative thresholds |
| `philosophy-chirality_continuum.md` | `flagship_papers/chirality_continuum/documentation_suite/philosophy-chirality_continuum.md` | Companion: topological-projection argument + joint-paper format |
| `glossary-chirality_continuum.md` | `flagship_papers/chirality_continuum/documentation_suite/glossary-chirality_continuum.md` | Companion: 13 chirality continuum terms |
| `reviews-chirality_continuum.md` | `flagship_papers/chirality_continuum/documentation_suite/reviews-chirality_continuum.md` | Companion: three-reviewer convergence at first reviewer round each |
| `B1_verify_chi6_substrate_handle.py` | `flagship_papers/chirality_continuum/code/B1_verify_chi6_substrate_handle.py` | Verification notebook 1/5 |
| `B2_verify_michel_rho_va.py` | `flagship_papers/chirality_continuum/code/B2_verify_michel_rho_va.py` | Verification notebook 2/5 |
| `B3_verify_chirality_helicity_coincidence.py` | `flagship_papers/chirality_continuum/code/B3_verify_chirality_helicity_coincidence.py` | Verification notebook 3/5 |
| `B4_verify_cross_sector_convergence.py` | `flagship_papers/chirality_continuum/code/B4_verify_cross_sector_convergence.py` | Verification notebook 4/5 |
| `B5_verify_capotauro_falsifier_6.py` | `flagship_papers/chirality_continuum/code/B5_verify_capotauro_falsifier_6.py` | Verification notebook 5/5 |
| `code/README.md` | `flagship_papers/chirality_continuum/code/README.md` | Verification suite index |
| `chirality_continuum_what_held_across_the_scales.md` | `book_project/chapters/chirality_continuum_what_held_across_the_scales.md` | Anthology chapter at Rovelli register (4323 words) |

**Compile note**: PDF must be compiled fresh on ClearPC. The verification notebooks are stand-alone Python (stdlib only — no external dependencies); they can be uploaded as-is for reviewer reproducibility.

## arXiv Submission Abstract Candidate (250 words)

```
We close the Layer 4 effective-field-theory bridge from the substrate-handle magnitude
χ/6 ≈ 0.0394 of Conscious Point Physics to observable Standard Model scales for two
structurally distinct sectors simultaneously. The Wilson-Fisher block-spin continuum-limit
projection map preserves group-theoretic structure and uniquely identifies the continuum
operator (Schur's lemma + parity calculus). Magnitude inheritance |M^eff| = χ/6 at
leading order requires no renormalization-group integration: χ/6 is a topological
substrate quantity, preserved exactly under continuum-limit projection via the standard
QFT protection-of-topological-quantities principle. The bridge applies once at
sector-agnostic level then twice: closing OPEN-FP-SF-2-CHIR at full Layer 4 rigor
(electroweak V−A coupling; Michel ρ = 3/4 within 0.3σ of PDG 2024; 100% LH at massless
helicity limit) and jointly closing SM-2 v2.0+ (chiral-polarity-bias; leptogenesis
CP-asymmetry within 2% of BAU back-derivation). Cross-sector convergence at observable
scale §6.5: a single primary observable validates both closures via different physical
channels — framed as structural prediction of the joint-paper format. Capotauro Falsifier 6
activated as operative with three thresholds (Michel ρ deviation 3×10⁻³, V+A admixture
3×10⁻², leptogenesis Δp_LR deviation 0.015). The closure is a conditional theorem on 15
foundational inputs inherited from Capotauro v2.0 + SF-2 v1.0 + SM-2 v1.0; the
dynamical-substrate-law gate (Q1′+Q1′.A Layer 3 promotion of n̂ + |χ| = φ⁻³) is identified
by external reviewer convergence as the defining next programme gate. First CPP flagship
to achieve three-reviewer convergence on ship-acceptable at first reviewer round each.
```

## arXiv Categories

```
Primary: hep-ph
Cross-listed: hep-th, gr-qc, cond-mat.stat-mech (for Wilson-Fisher / RG-flow context)
```

## Zenodo Metadata Equivalent

- **Title**: Chirality Continuum from Substrate to Observable EFT
- **Authors**: Abshier, Thomas Lee (Hyperphysics Institute)
- **Description**: (use OSF Description text above)
- **Keywords**: (use Tags list above)
- **License**: CC-BY 4.0
- **Related identifiers**:
  - OSF parent JXE8D ("isPartOf")
  - Capotauro v2.0 OSF component DOI ("isDerivedFrom"; substrate-level inputs)
  - SF-2 v1.0 OSF component DOI ("isDerivedFrom"; W-bracelet sector inputs)
  - SF-4 v4.4 OSF component DOI ("references"; first cross-sector closure precedent)
- **Resource type**: Publication / Working paper

---

# Cross-cutting deposit notes

## License convention

All three components should be deposited under **Creative Commons Attribution 4.0 International (CC-BY 4.0)** to match the existing CPP component licenses (SM-6 + SM-7 already on OSF use this; SS-9 deposit recommendation in its `letters/SS-9_post_ship_OSF_arXiv_submission_guide.md` also recommends CC-BY 4.0).

## Author affiliation

All three components: **Thomas Lee Abshier, ND** as sole author, affiliation **Hyperphysics Institute** (preferred form). ORCID if available should be attached to all three.

## Component DOI cross-linking strategy

After deposit, each component will have an OSF-minted component DOI. The recommended cross-link structure:

```
Parent project JXE8D (Hyperphysics Institute / Conscious Point Physics)
├── Capotauro v1.0 [new component DOI #1]
├── Capotauro v2.0 v1.0 [new component DOI #2; isNewVersionOf #1]
├── Chirality Continuum v1.0 [new component DOI #3; isDerivedFrom #2]
├── SF-4 v4.4 [existing or pending]
├── SF-2 v1.0 [existing or pending]
├── SS-7 v1.2 [pending]
├── SS-8 v1.0 [pending]
├── SS-9 v1.0 [pending]
└── (SM-6, SM-7 already on OSF as parent-level components)
```

## arXiv submission strategy

The three papers are tightly coupled: Capotauro v1.0 establishes the substrate-handle magnitude derivation; Capotauro v2.0 extends to three-way cross-sector unification; Chirality Continuum v1.0 builds the Layer 4 bridge from Capotauro v2.0's substrate-level outputs to observable scales for two of the three sectors.

**arXiv submission recommendation**: submit all three in a tight temporal cluster (within 1–2 days), with mutual cross-references in the arXiv abstracts. This signals the cross-paper coherence at the moment of public posting.

Submission order: Capotauro v1.0 → Capotauro v2.0 → Chirality Continuum v1.0 (matches OSF deposit order; matches substantive dependency chain).

## Post-deposit administrative updates

Within 1–2 sessions after deposits land, these programme files should be updated to reflect the deposit-complete state:

- `paper_catalog.md`: change "OSF pending" entries to "Registered on OSF" with component DOIs in their respective rows. (Note: also clean up the accumulated "Last updated" mega-line headers per the refactor work, which is occurring in parallel at Patch 0520 — coordinate with that.)
- `INDEX.md`: add component DOI URLs to chirality_continuum, capotauro, capotauro v2.0 entries.
- `research_frontier.md`: deposit-status markers to "deposited" where applicable.
- `bibliography/cpp_references.bib`: update `abshier2026_chirality_continuum` and Capotauro bibitems with the minted component DOIs (and add `\href` URLs).
- `flagship_papers/README.md`: deposit status notation in the architecture history table.

These updates are NOT critical-path blocking. They can be batched at the next session opening that touches these files.

---

## Document log

- **2026-05-20 Patch 0519**: Document created at Session 137 close. Covers Capotauro v1.0 + Capotauro v2.0 v1.0 + Chirality Continuum v1.0 deposit prep. SS-7 v1.2 + SS-8 v1.0 + SS-9 v1.0 + SF-2 v1.0 + SF-4 v4.4 OSF deposits remain pending and should be prepped in a follow-on deposit-prep document at the next convenient session opening (estimated 2–4 sessions to draft those materials if Thomas wants to deposit those older flagships as well).
