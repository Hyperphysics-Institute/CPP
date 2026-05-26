# Capotauro v2.0 v0.1 — Cross-References Inventory

**Status**: scoping document, Patch 0444 (Session 134 / first v0.1 drafting session).
**Companion to**: `series_umbrella/series_substrate_chirality_arc/capotauro/capotauro_v2_outline.md` (Patch 0442, the scoping anchor) and the eventual v2.0 v0.1 `capotauro.tex`.
**Purpose**: enumerate every cross-reference touched by the v1.0 → v2.0 rewrite, so subsequent drafting patches (§2 reframe, §3 substrate-locality, §5 W-bracelet, §6 qDP/eDP, §7 predictions, §9 Q7 scoping, §10 discussion) can be composed without label collisions, dangling `\ref{}`s, or omitted back-references from preserved v1.0 content into new cross-sector content.

The inventory is intentionally exhaustive rather than terse — it is the working surface a future-window session loads alongside `capotauro_v2_outline.md` when picking up the §3-§10 drafting arc. The outline tells *what to write*; this file tells *what each new section must cite and what every preserved section must back-reference*.

---

## 1. v1.0 section structure → v2.0 section structure mapping

The v1.0 paper currently has 11 `\section{}` blocks; v2.0 expands to 12 (one new section for the substrate-locality theorem, one new section per cross-sector manifestation, one new Q7 scoping section; `\section{$\sin^2\theta_{13}$ Posture}` from v1.0 absorbed into v2.0 §7 predictions framing). The mapping:

| v1.0 § | Title | v2.0 § | Status | Notes |
|---|---|---|---|---|
| §1 | Introduction and Strategic Frame | §1 | REWRITTEN | Programme positioning extended; Reading C trajectory narrative; OPEN-SD-CHIR-PRIMITIVE umbrella positioning |
| §2 | Substrate-Vacuum Chirality as Primitive Feature | §2 | REFRAMED | Operation A → Operation B; FI-C-RC-1 + FI-C-RC-2 registered; three converging arguments; v1.0 §2.1-§2.6 subsection map preserved with reframing |
| — | (new) | §3 | NEW | Substrate-Locality Theorem (Finding C-W39); local-$I_h$-preservation at $v_{\text{host}}$; $\chi \equiv \epsilon$ identification |
| §3 | The K3-Doublet and the Chirality Observable | §4 | PRESERVED | Renumbered §3 → §4; framed as "one sector of three" under umbrella; cross-references updated |
| §4 | The $D_6$ Stabilizer and Wigner-Eckart Framework | §4 (cont.) | PRESERVED | Folded as §4 continuation (subsection-level promotion); content unchanged; cross-references updated. **Alternative**: keep as separate §4.b — decision deferred to §4 drafting patch |
| §5 | The Composite Capotauro Wigner-Eckart Theorem | §4 (cont.) | PRESERVED | Theorem 5.1 (`thm:composite_cap_we`) preserved at exact wording; THEO-CAP-1 statement preserved; eight-step proof preserved; cross-references updated |
| §6 | Primary Empirical Prediction: $\Delta p_{LR} = \chi/6$ | §4 (cont.) or §7 (predictions) | PRESERVED | Decision deferred to §7 drafting patch; if folded into §7 master predictions table the v1.0 §6 standalone framing retires |
| §7 | $\sin^2\theta_{13}$ Posture: Re-scoped to SF-2 v2.0+ | §7 (cont.) or §10 (Discussion) | ABSORBED | Currently a standalone section; absorbed into v2.0 §7 master predictions or §10 cross-sector programme-pattern discussion. Content preserved |
| — | (new) | §5 | NEW | W-Bracelet Sector: Cross-Sector Unification with K3-Doublet (THEO-SD-CHIR-1, Findings C-W40 + C-W41 + C-W42 + C-W43) |
| — | (new) | §6 | NEW | qDP/eDP Sector: Three-Way Cross-Sector Unification (THEO-SD-CHIR-2, Findings C-W44 + C-W45 + C-W46) |
| — | (new) | §7 | NEW/REWRITTEN | Empirical Predictions and Cross-Sector Implications (master table; absorbs v1.0 §6 + v1.0 §7 content) |
| §8 | Cumulative Falsifier Set | §8 | EXTENDED | v1.0 falsifiers preserved; new cross-sector falsifiers added from THEO-SD-CHIR-1 + THEO-SD-CHIR-2 + umbrella unification claim |
| §9 | Open Theorem-Level Work | §9 (or absorbed) | REWRITTEN/ABSORBED | v1.0 §9 sub-claims (a)/(b)/FI-C-10 framing absorbed; v2.0 §9 becomes "Q7 Cosmological-Nucleation Scoping" per outline §3 §9 |
| §10 | Discussion | §10 | REWRITTEN | Programme-level pattern observations extended; cross-sector unification framework; reading C closure trajectory methodological observations; future-window targets |
| §11 | Foundational Input Summary | §11 (or appendix) | EXTENDED | FI-C-1 through FI-C-10 preserved; FI-C-RC-1 + FI-C-RC-2 added; v1.0 axiom-accounting preserved with A2 added (4 → 5 axioms? or A1+A2+A4+A7 per outline §0 abstract) |

**Open structural decisions during drafting** (parked for §4/§7 drafting patches):
- Whether v1.0 §3 + §4 + §5 (K3-doublet + $D_6$ + composite theorem) consolidate into single v2.0 §4 or remain three subsections of v2.0 §4. Default: consolidate, since v1.0 §3-§5 already form a single derivation chain.
- Whether v1.0 §6 ($\Delta p_{LR}$ prediction) lives in v2.0 §4 (with composite theorem) or v2.0 §7 (master predictions table). Default: §7, to consolidate three sector predictions in one table.
- Whether v1.0 §7 ($\sin^2\theta_{13}$ re-scope) lives in v2.0 §7 (predictions) or v2.0 §10 (discussion). Default: §10 programme-pattern discussion.

## 2. v1.0 label preservation table

The v1.0 `.tex` defines 104 `\label{}` entries. Preservation status under v2.0:

### 2.1 Section labels preserved unchanged (no re-target)

These remain in v2.0 with same `\label{}` and same target content; only their containing `\section{}` numbering may shift (LaTeX handles renumbering automatically — `\ref{sec:k3_doublet}` will resolve to whatever section number v2.0 ends up assigning):

| Label | v1.0 location | v2.0 retention rationale |
|---|---|---|
| `sec:introduction` | §1 | section preserved (rewritten content, same heading concept) |
| `sec:cap_problem`, `sec:what_delivers`, `sec:what_not`, `sec:position`, `sec:cross_sector`, `sec:strict_c`, `sec:roadmap` | §1 subsections | introduction subsection structure preserved |
| `sec:substrate_vacuum` | §2 | section preserved (reframed content, same heading concept) |
| `sec:order_parameter`, `sec:fi_c9_direct_falsifiers`, `sec:chi_resolution`, `sec:chi_constraint`, `sec:chi_scales`, `sec:chi_reductio`, `sec:chi_forward`, `sec:chi_falsifier`, `sec:empirical_anchor` | §2 subsections | preserved (light edits per §2 reframe patch 0445) |
| `sec:k3_doublet`, `sec:k3_base`, `sec:k3_tbm_basis`, `sec:perpendicular_wavefunction`, `sec:chirality_observable`, `sec:full_basis` | §3 (becomes v2.0 §4 K3-doublet sector) | preserved unchanged |
| `sec:d6_we`, `sec:k3_stabilizer`, `sec:s3_prime`, `sec:d6_irreps`, `sec:wigner_eckart_d6` | §4 (becomes v2.0 §4 cont.) | preserved unchanged |
| `sec:composite_we`, `sec:theorem_statement`, `sec:proof_overview`, `sec:k3_amplitude_factor`, `sec:cage_shell_factor`, `sec:cage_shell_factor_motivation`, `sec:cage_shell_factor_lemma`, `sec:composite_product`, `sec:numerical_verification`, `sec:nontriviality`, `sec:nontriviality_caveats` | §5 (becomes v2.0 §4 cont.) | preserved unchanged |
| `sec:dplr`, `sec:dplr_definition`, `sec:dplr_predicted`, `sec:dplr_observed`, `sec:dplr_agreement`, `sec:dplr_what_2_percent_means`, `sec:dplr_observable`, `sec:experimental_signature`, `sec:constraint_vs_fitting` | §6 (folds into v2.0 §7 predictions OR stays in v2.0 §4 cont.) | preserved unchanged |
| `sec:sin2theta13`, `sec:rescoping_decision`, `sec:scaling_tension`, `sec:gamma_observation`, `sec:gamma_guiding`, `sec:scope_limitation_honesty` | §7 (folds into v2.0 §7 or §10) | preserved unchanged |
| `sec:falsifier`, `sec:falsifier_framework`, `sec:falsifier_empirical`, `sec:falsifier_cross_sector`, `sec:falsifier_absences`, `sec:falsifier_modular` | §8 | preserved; new sibling subsections added in v2.0 |
| `sec:open_work`, `sec:open_subclaim_a`, `sec:open_subclaim_b`, `sec:open_fi_c10`, `sec:open_q11`, `sec:open_experimental_route` | §9 (rewritten as Q7 scoping) | preserved; sub-claim (b) framing absorbed into v2.0 §9 Q7 scoping |
| `sec:discussion`, `sec:methodological_observations`, `sec:cross_sector_inheritance`, `sec:cross_sector_implications`, `sec:programme_pattern`, `sec:templates_future`, `sec:outlook`, `sec:roadmap_v2`, `sec:alternatives`, `sec:probabilistic_rarity` | §10 | preserved; new programme-pattern subsections added |
| `sec:fi_summary`, `sec:ten_fis`, `sec:fi_axiom_accounting`, `sec:four_axioms`, `sec:dof_enumeration`, `sec:sf4_inheritance_section`, `sec:sigma1_odd_correction` | §11 | preserved; FI-C-RC-1 + FI-C-RC-2 added; axiom-accounting potentially expanded A1+A3+A4+A7 → A1+A2+A4+A7 (per outline §0; A2 most-load-bearing under Picture B substrate-orientation-field framework) |

### 2.2 Section labels reframed at content level (`\label` preserved, content reframed)

| Label | v1.0 location | v2.0 reframe |
|---|---|---|
| `sec:h4_i4` | §2.2 (currently "The $H_4$ structure and the $I_4$ substrate symmetry") | REFRAMED in Patch 0445: heading changes to "The $H_4 \to H_3 = I_h$ vertex-aligned reduction"; content rewritten to Operation B framing per Q1' resolution. Label preserved to keep all inbound `\ref{sec:h4_i4}` cross-references (currently 1 inbound from §2.5.1 line 260) resolving |

### 2.3 New section labels to register in v2.0

The new content sections require fresh `\label{}` entries. Proposed naming:

| New label | v2.0 location | Content |
|---|---|---|
| `sec:vertex_aligned_reading_c` | new §2.2.1 or §2.X | Three converging arguments for vertex-alignment (Finding C-W37) |
| `sec:fi_c_rc_inputs` | new §2 sub | Registration of FI-C-RC-1 + FI-C-RC-2 |
| `sec:substrate_locality` | new §3 | Substrate-Locality Theorem (Finding C-W39) |
| `thm:local_ih_preservation` | new §3 | Local-$I_h$-Preservation Theorem statement |
| `sec:chi_epsilon_identification` | new §3 sub | $\chi \equiv \epsilon$ identification at substrate level |
| `sec:w_bracelet_sector` | new §5 | W-Bracelet Sector header |
| `sec:substrate_locality_unification` | new §5.1 | Substrate-Locality Unification (Finding C-W40) |
| `sec:w_cage_shell_factor` | new §5.2 | Cage-shell factor identity on $D_6$ (Finding C-W41) |
| `sec:w_pairing_convention` | new §5.3 | $\zeta^W$ identification (Finding C-W43) |
| `thm:theo_sd_chir_1` | new §5.4 | THEO-SD-CHIR-1 statement |
| `sec:qdp_edp_sector` | new §6 | qDP/eDP Sector header |
| `sec:linear_orbital_zbw` | new §6.1 | Linear-vs-Orbital ZBW characterization (Finding C-W44) |
| `sec:qdp_cage_shell_layer2` | new §6.2 | Q6 Step 2 Layer 2 with Q6-PAIRING (Finding C-W45) |
| `sec:qdp_pairing_convention` | new §6.3 | $\zeta^{qDP}$ combined-$CP$ identification (Finding C-W46) |
| `thm:theo_sd_chir_2` | new §6.4 | THEO-SD-CHIR-2 statement |
| `sec:three_way_unification` | new §6.5 or §7 | Three-way magnitude unification corollary |
| `tab:manifestation_comparison` | new §6 or §7 | Manifestation comparison table per sketch §20.11 |
| `sec:cross_sector_predictions` | new §7 | Master predictions table |
| `sec:q7_scoping` | new §9 | Q7 sub-questions Q7.1-Q7.4 decomposition |
| `sec:q7_1_substrate_physics`, `sec:q7_2_cosmological_timing`, `sec:q7_3_baryogenesis`, `sec:q7_4_falsifiers` | new §9 sub | individual Q7 sub-question framings |
| `sec:cross_sector_unification_framework` | new §10 sub | Programme-pattern discussion |
| `sec:three_step_closure_pattern` | new §10 sub | Three-step closure pattern as umbrella structural invariant |
| `sec:magnitude_vs_mechanism_unification` | new §10 sub | Magnitude-level vs mechanism-level unification distinction |
| `sec:future_window_targets` | new §10 sub | Manifestations (iv)+(v) + Capotauro v3.0+ pointers |

(Final label names locked at drafting time per author preference; the above are proposed defaults consistent with v1.0 naming conventions.)

## 3. Cross-references to UPDATE inside preserved v1.0 content

Cross-references where the *content of the reference* changes even though the label resolves to a preserved location. These need editor attention during the §4-§10 preservation pass:

### 3.1 Inside preserved K3-doublet derivation chain (v1.0 §3-§5, v2.0 §4)

- v1.0 line 152 §1 derivation roadmap: refers to §2.X for substrate primitive chirality input. **v2.0**: also point to new §3 substrate-locality theorem (FI-C-9 sourced from §2's $\hat{n}$ + §3's $\chi \equiv \epsilon$ identification).
- v1.0 line 372 §3.4 (`sec:chirality_observable`): mentions FI-C-9 from §2. **v2.0**: add cross-link to §3 substrate-locality theorem identifying $\chi$ at substrate level.
- v1.0 line 455 §5 introduction: gathers substrate-physics inputs from §2 (FI-C-9). **v2.0**: gathers from §2 + §3 (substrate-locality identification).
- v1.0 line 485 step S8: substitutes FI-C-9 magnitude. **v2.0**: same substitution but FI-C-9 framed as v2.0 derivation via Reading C, not just v1.0 postulate.
- v1.0 line 504 §5.2 chirality-eigenvalue matching: identifies eigenvalues $\pm\chi$ from FI-C-9. **v2.0**: add cross-link to §3 substrate-locality theorem.
- v1.0 line 528 §5.4 Schur orthogonality on icosahedral cage: notes $\chi$ is global substrate property. **v2.0**: cross-link to §3 (local-$I_h$-preservation ensures the cage's $V_{\text{cage}}=12$ symmetric structure that Schur orthogonality requires).
- v1.0 line 583 §5.4 numerical verification: substitutes $|\chi| = \phi^{-3}$. **v2.0**: same.

### 3.2 Inside preserved sub-claim (b) discussion (v1.0 §9, absorbed/rewritten in v2.0)

- v1.0 line 886-891 §9.2 (`sec:open_subclaim_b`): describes geometric-chirality candidate working sketch. **v2.0**: the geometric-chirality candidate is no longer "candidate" — it is the working framework adopted in v2.0 §2 (FI-C-RC-1) + §3 (substrate-locality theorem). The sub-claim (b) framing is partially closed under v2.0: vertex-aligned Reading C resolved at Layer 2; first-principles magnitude derivation of $|\chi| = \phi^{-3}$ from CPP primitives remains open (FI-C-9 retained as foundational input). v2.0 §9 Q7 scoping absorbs the remaining sub-claim (b) content.
- v1.0 line 960-965 §9.4 v2.0+ decision point: notes mechanism candidate closure as v2.0 gate. **v2.0**: this section becomes the §9 Q7 scoping section + §10 discussion. The "v2.0 incorporates the mechanism-derivation chapter" forward-targeting language is *fulfilled by v2.0 §2 + §3* and rewritten to point forward to Q7 substantive work + manifestations (iv)+(v) closures.

### 3.3 Inside preserved cumulative falsifier set (v1.0 §8, v2.0 §8 extended)

- v1.0 falsifiers structured around FI-C-9 + FI-C-10 + composite theorem. **v2.0**: add cross-sector falsifiers from THEO-SD-CHIR-1 + THEO-SD-CHIR-2 + umbrella three-way unification claim per outline §3 §8.

## 4. Cross-document references inventory

References *outside* `capotauro.tex` that v2.0 acquires or updates. Critical for the §3-§10 drafting patches.

### 4.1 To `theorem-registry.md`

- THEO-CAP-1 (theorem #62, registered Patch 0397 Session 103): preserved at exact wording per outline §2.2; cross-linked from §4 K3-doublet composite theorem and §5/§6 cross-sector unification statements.
- THEO-SD-CHIR-1 (theorem #63, registered Patch 0434 Session 132 close): cross-linked from §5 W-bracelet sector main theorem statement.
- THEO-SD-CHIR-2 (theorem #64, registered Patch 0440 Session 133): cross-linked from §6 qDP/eDP sector main theorem statement.
- Lemma supporting structure: v1.0 paper's three lemmas (`lem:spectral_S`, `lem:k3_factor`, `lem:cage_shell`) preserved. v2.0 may add Lemma `lem:local_ih_preservation` in §3 if drafted at lemma level rather than as theorem-of-record.

### 4.2 To `research_frontier.md`

- OPEN-SM-4 (sub-claim (c) PARTIAL CLOSURE at v1.0): v2.0 confirms sub-claim (c) closure; sub-claim (b) status updated to PARTIAL CLOSURE under Reading C trajectory (Layer 2 vertex-alignment via three converging arguments; Layer 3 first-principles magnitude derivation remains open).
- OPEN-SD-CHIR-PRIMITIVE (umbrella, registered Patch 0422 Session 127): v2.0 delivers three-manifestation triangle closure (i)+(ii)+(iii); manifestations (iv)+(v) deferred.
- OPEN-FI-C-9-FP-MECHANISM: v2.0 status update — Reading C vertex-aligned at Layer 2; magnitude derivation from CPP primitives remains open as future-window work (folded into Q7 scoping or retained as separate FP-level entry, decision deferred to v2.0 v1.0 SHIP).
- OPEN-FP-SF-2-CHIR: substrate-physics handle $|M^W| = \chi/6$ delivered at substrate level from THEO-SD-CHIR-1; Layer 4 EFT continuum-limit closure (75% finite-mass → 100% massless-limit) registered as separate SF-2 v2.0+ work.

### 4.3 To `sketches/Capotauro_chiral_mechanism_candidate.md`

The working sketch is the canonical Tier 4 substantive content for v2.0's new sections. Section pointers:

| v2.0 section | Sketch section | Substance |
|---|---|---|
| §2 reframe | §2.1-§2.5 | Reading C primitive 4D direction $\hat{n}$ and edge-perturbation formula |
| §2 reframe (cross-sector arguments) | §11.4 | Q1' resolution / three converging arguments for vertex-alignment |
| §3 substrate-locality theorem | §13 | Finding C-W39; local-$I_h$-preservation theorem; $\chi \equiv \epsilon$ identification |
| §5 W-bracelet substrate-locality | §14 | Finding C-W40; Substrate-Locality Unification |
| §5 W-bracelet cage-shell factor | §15 | Finding C-W41; $|M_\perp^W| = 2/12 = 1/6$ |
| §5 W-bracelet pairing convention | §17 | Finding C-W43; $\zeta^W$ = icosahedral-center inversion; $E_2 \oplus E_1$ matter-doublet basis |
| §6 qDP/eDP substrate-locality | §18 | Finding C-W44; Linear ZBW = 1-vertex; Orbital ZBW = trivial subset |
| §6 qDP/eDP cage-shell factor Layer 2 | §19 | Finding C-W45; vanishing under naive framing; antipodal-pair $D_{5d}$ refinement |
| §6 qDP/eDP pairing convention | §20 | Finding C-W46; $\zeta^{qDP}$ = combined-$CP$; $A_{1g} \oplus A_{2u}$ matter-doublet basis |
| §6 three-way unification corollary | §20.14 + §20.11 | Three-way magnitude unification; manifestation comparison table |
| §9 Q7 scoping | §21 | Q7.1-Q7.4 sub-question decomposition; three candidate framings per sub-question |

### 4.4 To SM-2 v1.0

The qDP/eDP characterization in v2.0 §6 inherits from SM-2 v1.0:
- §5 (qDP/eDP general framework)
- §6 (Linear-vs-Orbital ZBW distinction)
- Glossary (Linear ZBW + Orbital ZBW definitions)

Bibliography entry for SM-2 v1.0 must be present in `bibliography/cpp_references.bib`; v2.0 §6 narrative text must explicitly reference SM-2's ZBW characterization at first introduction.

### 4.5 To SF-2 v1.0

The W-bracelet substrate object in v2.0 §5 inherits from SF-2 v1.0:
- Theorem 4.2 (W-bracelet $D_6$ stabilizer)
- §5/§6/§7 W-bracelet geometry on 600-cell first shell
- The 10 Petrie-polygon hexagons-per-host-vertex correspondence (Finding C-W36, Patch 0418)

### 4.6 To SF-4 v1.0+

The K3-doublet TBM-aligned basis (FI-C-3) inherits from SF-4 at theorem level. v1.0 §3 already cites SF-4 inheritance; v2.0 §4 preserves this. SF-4 Capotauro-integration paragraph (Grok Session 119 suggested next step from changelog) is downstream of v2.0 v1.0 SHIP and not v0.1 scope.

## 5. FI-C-N foundational input enumeration

The v1.0 paper registers FI-C-1 through FI-C-10. v2.0 adds two Reading-C-specific foundational inputs:

| FI ID | Statement | Status in v2.0 |
|---|---|---|
| FI-C-1 | K3-doublet identification (charged-lepton substrate states) | preserved |
| FI-C-2 | K3-base + four-cage taxonomy | preserved |
| FI-C-3 | TBM-aligned basis from SF-4 inheritance | preserved |
| FI-C-4 | Perpendicular-wavefunction structure | preserved |
| FI-C-5 | Chirality observable $\hat{C}_\chi$ in $B_2$ irrep | preserved |
| FI-C-6 | $D_6 = S_3 \times \mathbb{Z}_2$ stabilizer | preserved |
| FI-C-7 | Chirality-eigenvalue matching principle | preserved |
| FI-C-8 | Cage-shell averaging via Schur orthogonality | preserved |
| FI-C-9 | Substrate primitive chirality magnitude $|\chi| = \phi^{-3}$ | retained as foundational input; v2.0 §3 identifies $\chi \equiv \epsilon$ with magnitude derivation via perturbative-distance-ratio constraint preserved at structural-argument level |
| FI-C-10 | Cage-shell extension to chirality observables | preserved |
| **FI-C-RC-1** (NEW) | Substrate has a primitive 4D direction $\hat{n}$ as foundational feature of substrate existence-state | registered v2.0 §2 reframe (Patch 0445) |
| **FI-C-RC-2** (NEW) | Vertex-aligned reading: $\hat{n}$ aligns with a 600-cell vertex direction $v_{\text{host}}$, per Q1' resolution by three converging arguments (paper-internal hosting, cross-sector SF-2 W-bracelet, SM-1 first-shell icosahedron preservation) | registered v2.0 §2 reframe (Patch 0445), Layer 2 |

Axiom accounting: v1.0 declared closure conditional on 4 CPP axioms (A1, A3, A4, A7). Outline §0 abstract identifies v2.0 axiom dependencies as A1, A2, A4, A7 with A1+A7 most load-bearing under Picture B substrate-orientation-field framework. The A3 → A2 substitution traces to: A3 (rule-content for CP interactions) is consumed by the chirality observable's $B_2$-irrep identification (preserved); A2 (Grid Point existence/locality) becomes load-bearing under Reading C because the substrate's primitive 4D direction $\hat{n}$ is defined relative to the 4D ambient where GPs sit (FI-C-RC-1 is meaningful only given GP-substrate ambient). Final axiom dependency list locked at v2.0 §11 drafting patch.

## 6. Findings inventory

| Finding | Source patch | v2.0 section | Status |
|---|---|---|---|
| C-W23 | (pre-Reading-C) | §4 K3-doublet (preserved) | chirality-eigenvalue matching principle, v1.0 |
| C-W35 | Patch 0417 | §2 reframe | face-aligned Reading C structural coincidence; preserved as sub-result within vertex-aligned (Finding C-W37 §11.4 reconciliation) |
| C-W36 | Patch 0418 | §2 reframe | W-bracelet centroid coincidence with 600-cell vertex directions (vertex-aligned); one of three converging arguments for FI-C-RC-2 |
| C-W37 | Patch 0419 | §2 reframe | Q1' resolution toward vertex-aligned Reading C at Layer 2; FI-C-RC-2 registered |
| C-W38 | Patch 0423 | (SUPERSEDED) | not registered in v2.0; §13 §12 correction narrative preserved per `founders_voice/004` discipline |
| C-W39 | Patch 0424 | §3 NEW | Substrate-Locality Theorem; $\chi \equiv \epsilon$ identification |
| C-W40 | Patch 0425 | §5.1 NEW | Substrate-Locality Unification (K3 ↔ W) |
| C-W41 | Patch 0427 | §5.2 NEW | W-bracelet cage-shell factor identity $1/6$ |
| C-W42 | Patch 0428 | §5.3 NEW | Q5-PAIRING registered (Layer 2 conservative) |
| C-W43 | Patch 0429 | §5.3 NEW | Q5-PAIRING resolved; $\zeta^W$ = icosahedral-center inversion; composite $|M^W| = \chi/6$ at Layer 3 |
| C-W44 | Patch 0437 | §6.1 NEW | Linear/Orbital ZBW substrate-level identification |
| C-W45 | Patch 0438 | §6.2 NEW | Q6 Step 2 Layer 2 + Q6-PAIRING |
| C-W46 | Patch 0439 | §6.3 NEW | Q6-PAIRING resolved; $\zeta^{qDP}$ = combined-$CP$; composite $|M^{qDP}| = \chi/6$ at Layer 3 |

## 7. Bibliography extension needs

`bibliography/cpp_references.bib` entries currently cited from v1.0 capotauro.tex are preserved. New entries needed for v2.0:

- `abshier_theo_sd_chir_1` — pointer to `theorem-registry.md` THEO-SD-CHIR-1 entry (Patch 0434)
- `abshier_theo_sd_chir_2` — pointer to `theorem-registry.md` THEO-SD-CHIR-2 entry (Patch 0440)
- `abshier_open_sd_chir_primitive` — pointer to `research_frontier.md` OPEN-SD-CHIR-PRIMITIVE umbrella entry (Patch 0422)
- `abshier_capotauro_chiral_mechanism_sketch` — already cited in v1.0; v2.0 cross-references sketch §13-§21 specifically (verify @misc entry's `note` field points to current sketch state at 1874 lines through §21)
- `abshier_sm_2_v1_0` — SM-2 v1.0 paper (if not already in bibliography from other papers)
- `abshier_sf_2_v1_0` — SF-2 v1.0 paper (verify already in bibliography)
- Patch-history pointers: bibliography entries for Patches 0417, 0419, 0422-0429, 0434, 0437-0442 may be added as @misc entries with `note` fields if specific patch-level claims are referenced (optional; v1.0 paper used this pattern for Patches 0381, 0396, 0397).

## 8. Open structural decisions parked for drafting

These are decisions that don't need resolution at the cross-references inventory stage but will surface during §3-§10 drafting:

1. **§3 status: Theorem vs Section.** The Local-$I_h$-Preservation result of Finding C-W39 is theorem-grade content (proof at sketch §13.3). v2.0 §3 could either be a full `\section{}` with embedded `\begin{theorem}` block, or a subsection of §2 with the theorem inline. Recommended: full §3 section. The substrate-locality theorem is structurally foundational to §4-§6 and deserves section-level visibility.

2. **§4 consolidation depth.** v1.0 §3+§4+§5 form a single derivation chain. v2.0 §4 could either consolidate (single section with subsections) or preserve the three-section structure. Recommended: consolidate to single §4 with explicit subsection structure; this clarifies "§4 = one sector of three" framing.

3. **§7 vs §4 prediction placement.** $\Delta p_{LR} = \chi/6$ derivation (currently v1.0 §6) could either stay in §4 (K3-doublet sector) or move to §7 (cross-sector predictions table). Recommended: move to §7 to consolidate three-sector predictions table.

4. **§9 absorption of sub-claim (a)/(b)/FI-C-10 framing.** v1.0 §9 has dedicated subsections for sub-claim (a), sub-claim (b), FI-C-10. v2.0 §9 becomes Q7 cosmological-nucleation scoping. Sub-claim (b) is partially closed by v2.0 §2 + §3; sub-claim (a) becomes Q7 sub-question Q7.2 timing + Q7.3 baryogenesis bridge; FI-C-10 remains open future work. Recommended: rewrite v1.0 §9 entirely as v2.0 §9 Q7 scoping; preserve sub-claim (a)/(b)/FI-C-10 framing language in §10 discussion or §11 foundational input summary.

5. **§11 axiom-accounting expansion.** v1.0 axiom-accounting is conditional on 4 axioms (A1, A3, A4, A7). v2.0 outline says A1, A2, A4, A7. Decision: drop A3, add A2, retain A4+A7, or expand to 5 axioms total. Decision deferred to v2.0 §11 drafting patch with reviewer input.

6. **Manifestation comparison table placement.** Sketch §20.11 references a three-way manifestation comparison table. Either §6.5 (qDP/eDP sector closing) or §7 (master predictions). Recommended: §7, alongside the predictions table.

## 9. Drafting order recommendation

Per outline §4.1 the v0.1 drafting arc is Sessions 1-2 (this and one more). Within Patch 0445 (§2 reframe), this inventory enables clean §2 drafting without label collisions. Subsequent Sessions 3-4 drafting should proceed in this order, by inventory dependency:

1. **§3 NEW Substrate-Locality Theorem** — depends on §2 reframe (FI-C-RC-1 registration). Provides §3's $\chi \equiv \epsilon$ identification that §4-§6 cross-link forward to.
2. **§4 K3-doublet sector preservation pass** — light edits per §3.1 above (cross-link forward to §3); content preserved.
3. **§5 W-bracelet NEW** — depends on §3 (substrate-locality) + §4 (K3-doublet cage-shell factor template).
4. **§6 qDP/eDP NEW** — depends on §5 (parallel structure) + SM-2 v1.0 §5+§6+Glossary inheritance.
5. **§7 Predictions rewrite** — depends on §4+§5+§6 (three sector predictions).
6. **§8 Falsifiers extension** — depends on §5+§6 (cross-sector falsifier additions).
7. **§9 Q7 Scoping NEW** — depends on outline §3 §9 + sketch §21.
8. **§10 Discussion rewrite** — depends on all of §1-§9 (programme-pattern observations).
9. **§11 FI summary extension** — depends on §2 reframe (FI-C-RC-1+RC-2 registration). Possible at any time post-§2.

The §1 introduction rewrite + §0 abstract rewrite are best done last after §3-§10 stabilize, so cross-references to specific results are correct at first draft.

---

**End of cross-references inventory.** Total: ~285 lines. Companion to `capotauro_v2_outline.md` (Patch 0442). Provides label-preservation table, new-label registry, cross-document reference map, FI-C-N + Findings + Theorems inventory, bibliography extension list, and open structural decisions parked for drafting patches. v0.1 §2 reframe (Patch 0445) proceeds against this inventory.
