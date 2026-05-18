# Capotauro Transcript Document — Per-Session Transactions

**Paper**: `flagship_papers/capotauro/capotauro.tex` (v1.0 SHIPPED Session 122 Patch 0415)
**Purpose**: Compact per-session transaction log capturing the patch-by-patch development trajectory from closure-trajectory opening through v1.0 SHIP and post-SHIP doc-suite catch-up.
**Companion**: `development-capotauro.md` (per-session vignettes, Patch 0416B); `reasoning-capotauro.md` (Tier 4 verbatim reasoning, pending Patch 0416D); `handover-capotauro.md` (Session 122 close §15 Step H, retroactively recorded Patch 0416).

**Format**: One section per session. Each section lists the session number, patch number(s), one-line description of work done, and key artifact references.

---

## Session 86 — Closure trajectory opening (Patch 0376)

**Patch 0376**: Parent sketch creation + three-sub-claim decomposition.
- Created `flagship_papers/capotauro/sketches/Capotauro_chi_phi_closure.md`
- Three sub-claims registered: (a) Capotauro nucleation event derivation, (b) substrate chirality magnitude mechanism candidate derivation, (c) substrate-to-K3-doublet matrix element derivation
- Sub-claim (c) identified as v1.0 closure target

## Session 86 (continued) — Foundational findings C-1 through C-3 (Patches 0377–0378)

**Patches 0377–0378**: Foundational re-grounding work.
- C-1: original $\chi \approx \phi^{-1}$ conjecture failed geometric consistency check
- C-2: magnitude mismatch with empirical anchor surfaced
- C-3 (Patch 0378): OP-SM-4 archive's $\chi = \phi^{-2}$ derivation contained one-step arithmetic error (lost factor $1/\phi$); corrected value $\chi = \phi^{-3} \approx 0.236$ derived from edge-to-first-non-edge-distance ratio in 600-cell
- $\chi = \phi^{-3}$ becomes substrate chirality magnitude registered as FI-C-9

## Session 87 — Findings C-4 through C-8 (Patches 0379–0381)

**Patches 0379–0381**: Closure trajectory framework crystallization.
- C-4/5/6: structural alignment findings
- C-7 (Patch 0379): Grok's $\Delta p_{LR} \approx 0.04$ target adopted; substrate-to-observable transmission factor $T = V/2 = 6$ identified at numerical-signpost level
- C-8 (Patch 0381): Picture A (foundational substrate-vacuum) + Picture B (transmission mechanism) + Picture C (group-theoretic skeleton) decomposition adopted as load-bearing role assignment

## Session 88 — Theorem 8.1 anti-diagonal parity structure (Patch 0382)

**Patch 0382**: Sub-sub-claim (c.1a) closed at theorem level.
- K3-doublet matrix of $\hat{C}_\chi$ rigorously anti-diagonal in TBM-aligned basis under FI-C-3 + substrate-vacuum chirality input
- Five-step proof gathering FI-C-3 perpendicular wavefunctions + substrate-vacuum ansatz + K3-stabilizer $S_3$ action + ζ-parity assignment
- $M_{11} = M_{22} = 0$ with $M_{12} \neq 0$ established

## Session 89 — D_6 stabilizer corrigendum (Patch 0383)

**Patch 0383**: σ-orientation-reversing verification flag discharged + corrigendum.
- K3 stabilizer structure: $D_6 = S_3 \times Z_2$ with cell-swap $\zeta$ having $\det = -1$ (corrected from earlier informal $\det = +1$)
- Chirality-preserving subgroup: $S_3' = \langle r, \sigma_1 \zeta \rangle$ (corrected from $C_6$)
- ζ-ODD operators (not ζ-EVEN) are chirality observable carriers
- Three independent computational routes confirm: matrix-element computation + orbit analysis + character verification

## Session 90 — D_6 character theory obstruction (Patch 0384)

**Patch 0384**: (c.4.G2) closure attempt via $D_6$ character theory; obstruction surfaced.
- Under uniform ζ-parity in K3-doublet basis: all σ_1-ODD matrix elements forced to zero by combined σ_1 + σ_1ζ selection rules
- Pure ζ-uniform K3-doublet wavefunctions cannot host Capotauro mechanism
- Obstruction registered; resolution path opened toward FI-C-3 extension

## Session 91 — FI-C-3 extension with opposite-ζ-parity (Patch 0385)

**Patch 0385**: Obstruction resolved via extended foundational input.
- FI-C-3 extended: $\|\Phi_-^{(1)}\rangle = \|\phi_-^{(1)}\rangle \otimes \|\chi_\perp^{(1)}\rangle$ (ζ-EVEN); $\|\Phi_-^{(2)}\rangle = \|\phi_-^{(2)}\rangle \otimes \|\chi_\perp^{(2)}\rangle$ (ζ-ODD)
- Findings C-W11/12/13 register the opposite-ζ-parity formalization
- Key decision: extend FI-C-3 rather than abandon TBM-aligned K3-doublet basis (preserves SF-4 v4.0 inheritance)
- ζ-parity assignment validated by physical-picture analysis of cage-shell substrate orientation at K3-vertex locations

## Sessions 92–93 — Wigner-Eckart framework + sin²θ_13 scaling tension (Patches 0386–0387)

**Patch 0386** (Session 92): Wigner-Eckart framework setup on $D_6 = S_3 \times Z_2$.
- $\hat{C}_\chi$ irrep classification: $B_2 = A_2 \times \zeta\text{-ODD}$
- $A_2$ component selects K3-amplitude transformation type
- ζ-ODD component selects perpendicular-wavefunction transformation type

**Patch 0387** (Session 93): Linear-vs-quadratic sin²θ_13 scaling tension surfaced.
- Standard QFT-perturbation: $\sin^2\theta_{13} \propto \|M\|^2$ (quadratic in chirality matrix element) gives $\approx 1.55 \times 10^{-3}$, off by factor 21 from NuFIT 6.0 empirical
- Candidate γ structural observation: $\sin^2\theta_{13} = b \cdot m_\perp = \chi/(6\sqrt{3}) \approx 0.0227$ matches observation within 1σ
- Linear vs quadratic scaling tension registered for v1.0+ resolution

## Session 94 — Operator parameterization scoping (Patch 0388)

**Patch 0388**: σ_1-ODD operator parameterization survey on K3-amplitudes.
- General (a,b)-parameterization carrying $E$ and $A_2$ irrep content surveyed
- Initial K3-amplitude matrix element computed under (a,b)-parameterization
- Result later corrected at Session 95 (E-irrep contamination identified as inadmissible)

## Session 95 — Unique A_2 generator correction (Patch 0389)

**Patch 0389**: Session 93–94 parameterization substantively corrected.
- $\hat{C}_\chi$ in $B_2$ of $D_6$ requires the unique $A_2$ generator $T_{A_2}(b) = i \cdot b \cdot S$
- $S$ = antisymmetric 3×3 matrix encoding K3-vertex cyclic permutation (cross-product-with-$(1,1,1)$ structure)
- Corrected K3-amplitude matrix element: $M_{K3} = -i \cdot b \cdot \sqrt{3}$ ($\sqrt{3}$ in numerator)
- (a,b)-parameterization rejected: $E$-irrep contamination structurally inadmissible
- Documented at `Capotauro_subclaim_c_wigner_eckart.md` §3.4 with derivation as Lemma 4.2

## Session 96 — Chirality-eigenvalue matching closure (Patch 0390)

**Patch 0390**: Chirality-eigenvalue matching principle closed at theorem level.
- $T_{A_2}(b) = i \cdot b \cdot S$ eigenvalues on K3-amplitude basis: $\{0, +b\sqrt{3}, -b\sqrt{3}\}$ from cross-product-with-$(1,1,1)$ structure
- Setting non-zero eigenvalues equal to substrate chirality eigenvalues $\pm\chi$: $b = \chi/\sqrt{3}$
- $\|M_{K3}\| = \chi$ at zero free parameters
- Derivation principle: Hermitian-operator spectral analysis (not ad-hoc parameter assignment)

## Session 97 — Cage-shell averaging closure + FI-C-10 registration (Patch 0391)

**Patch 0391**: Cage-shell averaging principle closed; FI-C-10 registered.
- $\|M_\perp\| = d_E/V_\text{cage} = 2/12 = 1/6$ via FI-C-10 + Schur orthogonality
- $d_E = 2$: dimension of $E$ irrep of $D_6$
- $V_\text{cage} = 12$: icosahedral first-shell vertex count = $\|D_6\|$ (cage's $D_6$ stabilizer symmetry)
- FI-C-10 extends FI-C-6 (cage-shell coupling mass-formula from SF-4 v4.0 THEO-SF-4-5) from mass observables to chirality observables
- Three plausibility arguments justify the extension: substrate-isotropy, DI-bit propagation, FI-C-6 precedent
- Observable-class-independence claim physically motivated, not formally derived (registered as separate open work)

## Session 98 — THEO-CAP-1 formalization (Patch 0392)

**Patch 0392**: Composite Capotauro Wigner-Eckart Theorem formalized.
- Theorem statement: $\|M\| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ on TBM-aligned K3-doublet
- Eight-step proof: (i) extended basis construction; (ii) $\hat{C}_\chi$ irrep classification; (iii) Wigner-Eckart factorization; (iv) unique $A_2$ generator; (v) chirality-eigenvalue matching ($\|M_{K3}\| = \chi$); (vi) cage-shell averaging ($\|M_\perp\| = 1/6$); (vii) composite product; (viii) substrate substitution $\chi = \phi^{-3}$
- End-to-end numerical verification at machine precision ($10^{-17}$)
- Conditional on FI-C-1 through FI-C-10 + 4 CPP axioms (A1, A3, A4, A7)

## Sessions 99–100 — sin²θ_13 candidate scaling enumeration (Patches 0393–0394)

**Patch 0393** (Session 99): 22 candidate scalings for $\sin^2\theta_{13}$ tested.
- Only candidate γ ($\sin^2\theta_{13} = b \cdot m_\perp$) matches observation within 1σ
- All others ruled out by magnitude or scaling-form mismatch

**Patch 0394** (Session 100): PMNS perturbation machinery analysis.
- Standard QFT-perturbation: structurally produces quadratic scaling
- Candidate γ requires CPP-specific linear-scaling framework (not standard QFT)
- Linear-vs-quadratic tension confirmed as structural, not artifactual

## Session 101 — Wavefunction coupling ruled out + sin²θ_13 re-scoping (Patch 0395)

**Patch 0395**: Wavefunction-level coupling hypothesis explicitly derived; ruled out.
- Wavefunction-level coupling produces $\sin^2\theta_{13} \propto \|M\|^2$ structurally (quadratic)
- Off by factor $1/\chi^2 \approx 18$ from candidate-γ linear-scaling target
- Hypothesis ruled out; no perturbative reformulation within standard QFT yields linear scaling
- Key decision: re-scope Q11 $\sin^2\theta_{13}$ derivation to SF-2 v2.0+ rather than over-claim in-paper closure
- Sub-claim (b) Reading C closure trajectory may surface required CPP-specific linear-scaling framework

## Session 102 — Sub-claim (c) closure declaration (Patch 0396)

**Patch 0396**: v1.0 closure declaration with packaged trajectory summary.
- Sessions 88–101 closure trajectory enumerated as eight derivation steps + sin²θ_13 re-scoping decision
- v1.0 scope boundary articulated: sub-claim (c) CLOSED; sub-claims (a), (b) OPEN; Q11 re-scoped
- Closure declaration becomes the canonical referent for THEO-CAP-1 registration

## Session 103 — THEO-CAP-1 registration ahead of paper publication (Patch 0397)

**Patch 0397**: THEO-CAP-1 registered in `theorem-registry.md` as theorem #62 SF-Line section.
- **First programme-level theorem registered ahead of its own flagship paper publication in CPP corpus**
- Four-condition methodological pattern established for theorem-registry registration from flagship-paper-pending working sketch: rigorous proof + end-to-end numerical verification + primary empirical prediction validated + honest scope-limitation framing for re-scoped sub-problems
- Paper-level confirmation deferred to v1.0 SHIP at Session 122

## Session 104 — Outline (Patch 0398)

**Patch 0398**: `flagship_papers/capotauro/capotauro_outline.md` created (327 lines).
- Full paper structure: §1 intro + §2 substrate-vacuum + §3 K3-doublet + §4 $D_6$ Wigner-Eckart + §5 composite WE theorem + §6 Δp_LR + §7 sin²θ_13 + §8 falsifier + §9 open work + §10 discussion + §11 FI summary + §12 conclusions + §13 acknowledgments
- Foundational input enumeration FI-C-1 through FI-C-10 codified

## Session 105 — v0.1 .tex skeleton (Patch 0399)

**Patch 0399**: `flagship_papers/capotauro/capotauro.tex` v0.1 initial source created.
- Preamble + section skeleton + bibliography stub
- LaTeX conventions matching SS-9 / SF-4 / SF-2 (amsmath + amssymb + amsthm + mdframed + tikz + hyperref)
- Bibliography target: `bibliography/cpp_references.bib` (single source of truth per OPEN-WORKFLOW-1)

## Session 107 — v0.2 content expansion (Patch 0400)

**Patch 0400**: §2 substrate-vacuum + §3 K3-doublet content expansion.
- §2: SSB framing introduced (to be reframed Session 120); FI-C-9 as foundational input
- §3: SF-4 v4.0 K3 antibonding doublet extended with FI-C-3 perpendicular wavefunctions

## Sessions 108–109 — v0.3 content expansion (Patch 0401)

**Patch 0401**: §4 $D_6$ Wigner-Eckart + §5 composite WE theorem.
- §4: Irrep classification $B_2 = A_2 \times \zeta\text{-ODD}$ for $\hat{C}_\chi$
- §5: Chirality-eigenvalue matching + cage-shell averaging derivations; THEO-CAP-1 as Theorem 5.1

## Session 110 — v0.4 content expansion (Patch 0402)

**Patch 0402**: §6 Δp_LR + §7 sin²θ_13 + §8 falsifier set.
- §6: $\Delta p_{LR} = \chi/6 \approx 0.0394$ derivation + empirical comparison to leptogenesis back-derivation
- §7: Candidate γ structural observation + re-scoping decision
- §8: Falsifier set enumeration

## Session 111 — v0.5 content expansion (Patch 0403)

**Patch 0403**: §9 open work + §10 discussion + §11 FI summary.
- §9: Sub-claim (a) + sub-claim (b) + FI-C-10 first-principles + Q11 sin²θ_13 as v2.0+ work
- §10: Methodological observations
- §11: FI-C-1 through FI-C-10 consolidated

## Session 112 — v0.6 polish + first PDF (Patch 0404)

**Patch 0404**: Integration polish + first PDF compile.
- End-to-end numerical verification embedded in §5
- Cross-references resolved; bibliography clean
- First PDF: 35 pages, 481 KB

## Session 113 — ChatGPT v0.6 review + Grok-suspension cleanup (Patches 0405–0406)

**Patch 0405**: ChatGPT v0.6 review archived at `flagship_papers/capotauro/reviews/chatgpt_v0.6_session_113.md`.
- Substantively positive on theorem-level structural derivation
- Five items flagged for v0.7 disposition: §6.6 nontriviality, §2.3 forward argument, §5.4 FI-C-6 precedent, §6.1.1 experimental, §9.5 experimental open work

**Patch 0406**: Programme-infrastructure Grok-suspension-warning cleanup (out-of-Capotauro scope).
- OPEN-WORKFLOW-3 vocabulary contamination protocol documentation completed

## Session 114 — v0.7 Group A substantive rework (Patch 0407)

**Patch 0407**: All five ChatGPT v0.6 items addressed via Group A rework.
- §6.6 nontriviality strengthened (explicit trivial-case counterexample construction)
- §2.3 forward argument sharpened (three-step substrate-vacuum derivation)
- §5.4 FI-C-6 precedent argument added
- §6.1.1 experimental anchor framing expanded
- §9.5 experimental open work section added

## Session 115 — v0.7 Group B + changelog file creation (Patch 0408)

**Patch 0408**: Writing/style polish + title-block cleanup + changelog file creation.
- v0.7 PDF shipped with all five ChatGPT v0.6 items addressed
- **Created** `flagship_papers/capotauro/documentation_suite/changelog-capotauro.md` as reference implementation
- Key decision: per-paper changelog file rather than .tex-embedded CHANGELOG blocks

## Session 116 — Changelog-architecture programme-wide standardization (Patch 0409)

**Patch 0409**: Patch 0408 reference implementation codified as programme-wide rule.
- Updates across `operating_system.md` + `paper-formatting.md` + `documentation-suite.md` + `paper_production_workflow.md` + `paper_completion_checklist.md` + `bootup.md`
- Forward-only migration policy: SS-9 / SF-4 / SF-2 preserve .tex-embedded CHANGELOG; new papers (Capotauro+) use per-paper changelog file convention

## Session 117 — ChatGPT v0.7 round-2 review (Patch 0410)

**Patch 0410**: ChatGPT v0.7 round-2 review archived at `reviews/chatgpt_v0.7_session_117.md`.
- *"mature conditional-theorem flagship paper"* — overall strongly positive
- 4 remaining items + 5 discoverability gaps mapped to v0.8 disposition
- ChatGPT recruited as strongest reviewer at this point (round-2/round-3 deliver most substantive critique)

## Session 118 — v0.8 substantive expositional polish (Patch 0411)

**Patch 0411**: All five ChatGPT v0.7 items addressed.
- NEW §1.7 derivation-flow TikZ figure (visualizes eight-step proof)
- §1.2 cross-reference to §6.6 (closes nontriviality discoverability gap)
- §5.4 FI-C-6 precedent argument expanded with observable-class-independence
- §6.1.1 tightened
- §10 methodological observations merged into single subsection

## Session 119 — Three v0.8 reviews in parallel (Patch 0412)

**Patch 0412**: Cross-reviewer convergence on SHIP-readiness achieved.
- ChatGPT round-3 at `reviews/chatgpt_v0.8_session_119.md`: *"mature conditional-theorem flagship paper"*; 4 carry-over + 5 v0.9 items + 2 discoverability gaps
- CoPilot round-1 at `reviews/copilot_v0.8_session_119.md`: *"extremely close to v1.0 ship-ready"*; 5 tightening items including `gandolfi_2025` citation veridicality flag
- Grok round-1 at `reviews/grok_v0.8_session_119.md`: *"Ship as v1.0"*; 4 minor polish items; joint main + Companion format endorsement for SF-line work
- Cross-reviewer convergence triggers v0.9 polish-and-ship trajectory

## Session 120 — v0.9 polish + foundational framing reframe (Patch 0413)

**Patch 0413**: Methodologically critical foundational framing reframe.
- §2 reframed: *"Substrate-Vacuum Broken-Symmetry Physics"* → *"Substrate-Vacuum Chirality as Primitive Feature"*
- CPP-core-principle methodological commitment: mathematical descriptions are not physical mechanisms
- SSB framing demoted to mathematical-equivalence alternative in Remark 2.2
- Sub-claim (b) renamed: "symmetry-breaking dynamics derivation" → "substrate chirality mechanism candidate derivation"
- Sub-claim (a) clarified as universe-wide sign-selection event downstream of sub-claim (b)
- `gandolfi_2025` citation removed (web_search verification failed via arXiv + Scholar + ADS); §2.4 empirical-anchor paragraph rewritten using only verified leptogenesis-back-derivation chain
- 8 ADDRESS items + 2 DISCOVERABILITY items from v0.8 cross-reviewer disposition
- 1149 lines (-9 from v0.8); 46 pages 601 KB; pdflatex two-pass compile VERIFIED CLEAN

## Session 121 — Reading C mechanism candidate sketch (Patch 0414)

**Patch 0414**: NEW `flagship_papers/capotauro/sketches/Capotauro_chiral_mechanism_candidate.md` (296 lines).
- Reading C: primitive 4D direction $\hat{n}$ in substrate's ambient 4D space produces direction-correlated edge-length variation in 600-cell lattice at $\phi^{-3}$ scale
- $H_4 \to I_4$ algebraic structure is structural consequence of $\hat{n}$ being primitive
- Chirality magnitude $\|\chi\| = \phi^{-3}$ **derived** rather than postulated via perturbative-distance-ratio constraint
- New structural prediction: fractional chirality retention across observable classes (mass $\approx 0.6\%$; chirality $\approx 4\%$)
- Five Layer 3 closure-trajectory questions registered: Q1 group-theoretic verification of $H_4 \to I_4$ stabilizer + Q3/Q4 perturbative-distance-ratio sharpening + Q5/Q6 cross-sector consistency
- Tier-4 Layer 1 / Layer 2 epistemic status (physical intuition + structural mathematical sketching)
- Registered at `Research_Frontier.md` OPEN-FI-C-9-FP-MECHANISM (Layer 3 closure trajectory; estimated 10–20 sessions)

## Session 122 — v1.0 SHIPPED via title-block bump (Patch 0415)

**Patch 0415**: **Capotauro paper v1.0 SHIPPED**.
- Title block: `Version 0.9 --- 16 May 2026` → `Version 1.0 (SHIPPED) --- 16 May 2026`
- Substantive paper content unchanged from v0.9 (Patch 0413); version-bump-only SHIP
- Programme-level changes: (1) `Research_Frontier.md` OPEN-SM-4 PARTIAL CLOSURE; (2) NEW OPEN-FI-C-9-FP-MECHANISM entry; (3) `theorem-registry.md` THEO-CAP-1 paper-level confirmation; (4) `paper_catalog.md` SF-Line Capotauro row + Documentation paragraph; (5) `INDEX.md` flagship_papers entries; (6) NEW `flagship_papers/capotauro/README.md`
- **Third flagship paper to ship at v1.0 in CPP corpus** (after SS-9, SF-4, SF-2)
- **First flagship paper outside SF-N numerical convention**
- Commit message's "All registers UNCHANGED at programme level" framing missed 3 drift items (predictions.md PRED-O entry + master_glossary.md Capotauro section + problem_histories/PH-OPEN-SM-4.md) — caught and fixed retroactively at Patch 0416A

## Session 123 — Retroactive handover + registry drift fix (Patches 0416 + 0416A)

**Patch 0416**: Retroactive §15 Step H handover for Session 122 close.
- Previous context window closed mid-conversation during post-SHIP discipline-tightening discussion; no Step H handover artifact produced at Session 122 close
- NEW `flagship_papers/capotauro/documentation_suite/handover-capotauro.md` (63 lines, §15 Step H paste-ready format)
- NEW `session_logs/2026-05-16_session_log.md` (Template B retrospective synthesis variant)
- §15 Step E per-registry audit surfaced 3 drift items the Patch 0415 commit message's bundled "registers updated" framing missed

**Patch 0416A**: Registry drift fix.
- `predictions.md` NEW PRED-O-25 entry for $\Delta p_{LR} = \chi/6 \approx 0.0394$ + Capotauro row in §6 Predictions by Paper + Last-updated header update
- `master_glossary.md` NEW "Capotauro v1.0 substrate-vacuum chirality framework terms" section appended with 12 entries (Capotauro mechanism + FI-C-9 + FI-C-10 + K3-doublet basis + $\hat{C}_\chi$ + matching principle + averaging factor + THEO-CAP-1 + $\Delta p_{LR}$ + $\hat{n}$ Reading C + sub-claim taxonomy + primitive-feature vs SSB)
- NEW `problem_histories/PH-OPEN-SM-4.md` (~120 lines) with canonical problem-history narrative
- First letter-suffix patch in post-SHIP Capotauro doc-suite catch-up arc
- Key decisions registered: parallel-window workflow (letter-suffix docs-arc 0416A+ vs integer physics-arc 0417+) + OPEN-WORKFLOW-DOCS-CATCHUP deferred to post-Section-A completion per discipline-tightening-after-precedent principle

## Session 123 (continued) — Section E doc-suite production (Patches 0416B–D)

**Patch 0416B**: NEW `flagship_papers/capotauro/documentation_suite/development-capotauro.md` (252 lines).
- Section E Tier-3 vignettes + Section A5 development-history dual-role file
- 24 vignettes covering Sessions 86–123 closure trajectory through v1.0 SHIP and post-SHIP doc-suite catch-up
- Cumulative campaign metrics + Contributor roles + Transcript references sections

**Patch 0416C** (this patch): NEW `flagship_papers/capotauro/documentation_suite/transcript-capotauro.md` (this file).
- Section E Tier-2 per-session transaction log
- Per-session sections covering Sessions 86–123 with patch numbers + one-line summaries + artifact references
- Compact pointer-map format following SF-4 / SS-9 convention

**Patch 0416D** (pending): NEW `flagship_papers/capotauro/documentation_suite/reasoning-capotauro.md` (planned).
- Section E Tier-4 verbatim reasoning narrative
- Per SF-4 v4.0 convention: may be pointer file to three working sketches at `sketches/` as canonical Tier-4 source

---

## Forward queue post-Patch 0416C

- **Patch 0416D**: `reasoning-capotauro.md` (Section E Tier-4 reasoning narrative)
- **Patches 0416E–J**: Section A 6 standalone companions (mechanism + glossary + phenomena + philosophy + reviews + keywords)
- **Patch 0416K**: anthology chapter at Rovelli/SciAm register (~5000–6000 words)
- **Patch 0416L**: TATWD integration to `CPP_the_theory.md`
- **Patch 0416M**: OPEN-WORKFLOW-DOCS-CATCHUP registration in `todolist.md`

**Parallel-window forward-physics arc** (separate context window, integer patches 0417+): sub-claim (b) Reading C Q1 group-theoretic verification of $H_4$ stabilizer of $\hat{n} \cong I_4$ claim (estimated 1–3 sessions; first sub-step toward Layer 3 closure; closure triggers Capotauro v2.0+ at minimum).

---

## Sessions 127–130 (17 May 2026) — Reading C closure arc continuation

**Note:** Patches 0417–0421 (Sessions 124–126, 16 May 2026) were the Reading C Layer 2/3 trajectory opening (Q1, Q2 closure + Q1' resolution toward vertex-aligned Reading C + closure-trajectory handover consolidation). Per-patch transcript entries for 0417–0421 are a pre-existing pointer-map gap to be filled at next opportunity; the consolidated narrative is at `Patch 0421` handover doc (commit `8acdb63`). The entries below cover Patches 0422–0426 (Sessions 127–130 + this handover).

**Patch 0422 (Session 127):** Programme-level umbrella registration **OPEN-SD-CHIR-PRIMITIVE** in SD section above OPEN-FI-C-9-FP-MECHANISM and OPEN-FP-SF-2-CHIR; five-manifestation scope. NEW `founders_voice/005_chirality_is_primitive.md` (~180 lines) verbatim recovery of Session 120 founder's-confrontation reasoning. Research_Frontier.md problem counts updated (93 → 94 entries, 58 → 59 open). Commit `a4f8656`.
- → `Research_Frontier.md` §OPEN-SD-CHIR-PRIMITIVE (NEW)
- → `flagship_papers/capotauro/founders_voice/005_chirality_is_primitive.md` (NEW, ~180 lines)
- → Tier 4: `reasoning-capotauro.md` §8 (Session 127 reasoning at Patch 0426)

**Patch 0423 (Session 128):** Q3 ε-χ relationship Layer 2 attempt. Sketch §12 added with f_geom · f_irrep two-factor structure; Finding C-W38 registered. **NOTE: §12 subsequently superseded by §13 in Patch 0424; C-W38 superseded by C-W39. The §12 content is preserved in the sketch for audit-trail per founders_voice/004 discipline.** Commit `ffe293c`.
- → `flagship_papers/capotauro/sketches/Capotauro_chiral_mechanism_candidate.md` §12 (preserved as superseded)
- → `Research_Frontier.md` §OPEN-FI-C-9-FP-MECHANISM (Finding C-W38, later superseded)
- → Tier 4: `reasoning-capotauro.md` §9 (Session 128 reasoning + supersession note at Patch 0426)

**Patch 0424 (Session 129):** Q3 §12 4D correction + Q4 dissolution. Under proper 4D analysis the K3-base edges are tangent to $\hat n$ identically — first-order edge-length perturbations vanish for the entire first shell under vertex-aligned Reading C. **Finding C-W39** (NEW; supersedes C-W38): local I_h preservation under vertex-aligned Reading C; χ ≡ ε at substrate level. Q3 CLOSED at Layer 3 by direct identification. Q4 DISSOLVED (the f_irrep Wigner-Eckart computation was an artifact of the §12 geometric error). Capotauro v1.0 paper §10's |M| = χ/6 prediction preserved exactly. Layer 3 closure trajectory revised 7–17 → 5–12 sessions. Commit `653637c`.
- → `flagship_papers/capotauro/sketches/Capotauro_chiral_mechanism_candidate.md` §13 (correction)
- → `Research_Frontier.md` §OPEN-FI-C-9-FP-MECHANISM (Finding C-W39 supersedes C-W38; Q3 closed; Q4 dissolved)
- → Tier 4: `reasoning-capotauro.md` §10 (Session 129 reasoning at Patch 0426)

**Patch 0425 (Session 130):** Q5 (cross-sector consistency with SF-2 W bracelet) CLOSED at Layer 2 via Substrate-Locality Unification theorem. Sketch §14 (~93 lines, v2 framing — v1 sign-coherence draft deleted in-session). The §13.3 local-I_h-preservation theorem applies uniformly to any subset of first-shell vertices, hence covers both K3-base (OPEN-FI-C-9) and W-bracelet (OPEN-FP-SF-2) substrate objects. **Finding C-W40** (NEW): Substrate-Locality Unification under vertex-aligned Reading C — first explicit cross-sector unification result under OPEN-SD-CHIR-PRIMITIVE umbrella. K3-doublet's d_E/V_cage = 2/12 = 1/6 cage-shell factor (paper §10) yielding χ/6; W-bracelet's analog factor on Petrie-polygon D_6 sub-stabilizer is Q5 Layer 3 target (2–4 sessions). Sketch grows 904 → 997 lines (+93 net). Commit `b1b17b5`.
- → `flagship_papers/capotauro/sketches/Capotauro_chiral_mechanism_candidate.md` §14 (Q5 Layer 2 closure)
- → `Research_Frontier.md` §OPEN-FI-C-9-FP-MECHANISM (Finding C-W40 registered; Q5 Layer 2 closed)
- → Tier 4: `reasoning-capotauro.md` §11 (Session 130 reasoning + v1/v2 §14 cleanup decision at Patch 0426)

**Patch 0426 (Session 130 close):** Session-close handover protocol — Sessions 127–130 Reading C closure arc handover per `templates/operating_system.md` §15. Step A (per-session logs), Step B (this transcript update), Step C (development vignettes), Step D (Tier 4 reasoning §8–§11), Step E (Organizational_Frontier OPEN-ORG-015 + future_projects Q5/Q6/Q7), Step G (paste-truncation workflow item registered as OPEN-ORG-015), Step H (this `handover-capotauro.md` overwrite). Steps F + several Step E sub-items marked N/A with audit rationale.
- → `session_logs/2026-05-17_session_127_log.md` through `_130_log.md` (NEW, 4 files)
- → `flagship_papers/capotauro/documentation_suite/development-capotauro.md` (Sessions 127–130 vignettes appended)
- → `flagship_papers/capotauro/documentation_suite/reasoning-capotauro.md` §8–§11 (appended)
- → `flagship_papers/capotauro/documentation_suite/handover-capotauro.md` (overwrite with Session 130 close handover)
- → `Organizational_Frontier.md` OPEN-ORG-015 (NEW, paste-truncation workflow)
- → `future_projects.md` (Q5 Layer 3 + Q6 + Q7 entries appended)

---

## Forward queue post-Patch 0426

**Priority 1 (next session):** Q5 Layer 3 closure — W-bracelet Schur-orthogonality cage-shell factor on Petrie-polygon D_6 ⊂ H_3 sub-stabilizer + SF-2 V-A coupling matching at massless helicity limit + Wigner-Eckart H_3 → D_6 branching consistency. Estimated 2–4 sessions; piece (a) likely single-session.

**Priority 2:** Q6 (SM-2 qDP/eDP) — Finding C-W40 framework application if qDP/eDP characterizable as first-shell-vertex substrate object. Estimated 3–5 sessions.

**Priority 3:** Q7 (cosmological-timing question) — scoping not yet started.

**Pre-existing pointer-map gap:** Patches 0417–0421 (Sessions 124–126) per-patch transcript entries to be filled at next opportunity (consolidated narrative at Patch 0421 handover doc, commit `8acdb63`).

---

*Maintainer: Dr. Thomas Lee Abshier ND, Hyperphysics Institute. Last updated: 17 May 2026 (Session 130 Patch 0426 handover — appended Sessions 127–130 Reading C closure arc Patches 0422–0426 transaction entries).*
