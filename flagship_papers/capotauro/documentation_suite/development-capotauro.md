# Capotauro Development Document — Session-by-Session Vignettes

**Paper**: `flagship_papers/capotauro/capotauro.tex` (v1.0 SHIPPED Session 122 Patch 0415)
**Purpose**: Per-session development arc covering Sessions 86–122 (closure trajectory opening through v1.0 SHIP) + Session 123+ (post-v1.0 documentation suite production). Serves dual role per `paper_completion_checklist.md` A5 + `documentation-suite.md` §1: (i) Section E Tier-3 vignettes for the four-tier discipline; (ii) Section A5 development-history companion file.
**Companion**: `transcript-capotauro.md` (per-session transactions, pending Patch 0416C); `reasoning-capotauro.md` (Tier 4 verbatim reasoning, pending Patch 0416D); `handover-capotauro.md` (Session 122 close, retroactively recorded Patch 0416 Session 123).
**Parent paper venue**: SF-Line Flagship Papers (first flagship outside SF-N numerical convention; third flagship to ship at v1.0 in CPP corpus after SS-9 Session 32, SF-4 Session 54, SF-2 Session 83).

---

## Vignette 1 — Session 86 (closure trajectory opening, Patch 0376)

The OPEN-SM-4 entry was registered in `Research_Frontier.md` on 23 March 2026 as a conceptual placeholder: "Derive the lattice chirality-activation event that establishes $\chi \approx \phi^{-1}$ and produces CP violation." The original $\chi \approx \phi^{-1}$ conjecture from earlier substrate-physics intuition had been carried through Sessions 1–85 without rigorous derivation. The Abshier & Grok December 2025 *Capotauro nucleation paper* supplied the cosmological framing (lattice nucleation at $z \simeq 32$) and the etymology — *capo* (head) + *tauro* (bull) for the universe-wide chirality-asymmetry event. Grok also coined the empirical chirality bias target $\Delta p_{LR} \approx 0.04$ back-derived from the cosmological baryon asymmetry $\eta_B$ via leptogenesis.

Session 86 Patch 0376 opened the closure-trajectory parent sketch at `flagship_papers/capotauro/sketches/Capotauro_chi_phi_closure.md`, decomposing the Capotauro problem into three sub-claims: (a) Capotauro nucleation event derivation (universe-wide sign-selection event); (b) substrate chirality mechanism candidate derivation (deriving $\|\chi\|$ from CPP primitives rather than postulating it); (c) substrate-to-K3-doublet matrix element derivation $\|M\| = \chi/6$ on the TBM-aligned K3-doublet. Sub-claim (c) identified as the v1.0 closure target — most tractable, well-defined endpoint, theorem-level achievable on the SF-4 v4.0 inheritance.

## Vignette 2 — Sessions 86–87 (foundational findings C-1 through C-8, Patches 0377–0381)

Patches 0377–0381 surfaced eight substantive foundational findings (C-1 through C-8) that re-grounded the closure trajectory after the original $\chi \approx \phi^{-1}$ conjecture failed to match the 600-cell geometric structure. The methodologically critical finding was C-3 (Patch 0378): the OP-SM-4 archive's $\chi = \phi^{-2}$ derivation contained a one-step arithmetic error (lost factor $1/\phi$); corrected value $\chi = \phi^{-3} \approx 0.236$ derived rigorously from the edge-to-first-non-edge-distance ratio in the 600-cell. This $\chi = \phi^{-3}$ value, not the earlier $\phi^{-1}$ or $\phi^{-2}$, became the substrate chirality magnitude registered as FI-C-9.

C-7 Patch 0379 integrated Grok's $\Delta p_{LR} \approx 0.04$ target and surfaced the substrate-to-observable transmission factor $T = V/2 = 6$ at the numerical-signpost level: $\|M\| = \chi/T = \phi^{-3}/6 \approx 0.0394$. C-8 Patch 0381 adopted the Picture A (foundational substrate-vacuum) + Picture B (transmission mechanism) + Picture C (group-theoretic skeleton) decomposition as load-bearing role assignment for the closure trajectory.

**Dead end** (registered Session 86): the original $\chi \approx \phi^{-1}$ conjecture was abandoned at C-1 / C-2 / C-3 after three independent diagnostic findings ruled it out — geometric inconsistency at C-1, magnitude mismatch with empirical anchor at C-2, and the C-3 arithmetic correction surfacing $\phi^{-3}$ as the correct value.

## Vignette 3 — Session 88 (Theorem 8.1 anti-diagonal parity structure, Patch 0382)

Session 88 closed sub-sub-claim (c.1a) at theorem level: the K3-doublet matrix of $\hat{C}_\chi$ is rigorously anti-diagonal in the TBM-aligned basis under FI-C-3 + the substrate-vacuum chirality input (Theorem 8.1, five-step proof). The proof gathered four substrate-orientation inputs: (i) FI-C-3 perpendicular wavefunctions $\chi_\perp^{(1)} / \chi_\perp^{(2)}$ extending the SF-4 K3 antibonding doublet; (ii) the substrate-vacuum chirality matrix element ansatz; (iii) the K3-stabilizer group $S_3$ acting on K3-amplitudes; (iv) ζ-parity assignment under cell-swap symmetry. The anti-diagonal structure $M_{11} = M_{22} = 0$ with $M_{12} \neq 0$ followed as theorem under those inputs.

The structural pattern revealed in Theorem 8.1's proof was that the chirality observable lives in an irrep with sign content opposite to the trivial irrep — this prefigured the formal classification as $B_2 = A_2 \times \zeta\text{-ODD}$ in Sessions 90–91.

## Vignette 4 — Session 89 (D_6 stabilizer corrigendum, Patch 0383)

Session 89 discharged the σ-orientation-reversing verification flag at full numerical rigor and surfaced a substantive corrigendum: the K3 stabilizer structure is $D_6 = S_3 \times Z_2$ with the cell-swap $\zeta$ having $\det = -1$ (not $+1$ as the earlier §3.1 informal framing had stated), and the chirality-preserving subgroup is $S_3' = \langle r, \sigma_1 \zeta \rangle$ (not the previously-named $C_6$).

This corrigendum was load-bearing: the cell-swap's $\det = -1$ status was the structural fact making ζ-ODD operators (rather than ζ-EVEN) the chirality observable carriers in subsequent Wigner-Eckart analysis. The earlier $C_6$ framing would have produced incorrect selection-rule predictions. The session's discharge of the verification flag confirmed the structural fact through three independent computational routes (matrix-element computation, orbit analysis, character verification).

## Vignette 5 — Sessions 90–91 (D_6 obstruction + FI-C-3 extension, Patches 0384–0385)

Session 90 attempted the (c.4.G2) closure via $D_6$ character theory and surfaced a structural obstruction: under uniform ζ-parity in the K3-doublet basis, all matrix elements of σ_1-ODD operators are forced to zero by the combined σ_1 + σ_1ζ selection rules. Pure ζ-uniform K3-doublet wavefunctions cannot host the Capotauro mechanism.

Session 91 Patch 0385 resolved the obstruction via FI-C-3 extension with explicit opposite-ζ-parity assignment for the two K3-doublet basis states: one ζ-EVEN, one ζ-ODD. The extended basis $\|\Phi_-^{(1)}\rangle = \|\phi_-^{(1)}\rangle \otimes \|\chi_\perp^{(1)}\rangle$ (ζ-EVEN) and $\|\Phi_-^{(2)}\rangle = \|\phi_-^{(2)}\rangle \otimes \|\chi_\perp^{(2)}\rangle$ (ζ-ODD) was formalized via Findings C-W11/12/13, with the ζ-parity assignment validated by physical-picture analysis of the cage-shell substrate orientation at the two K3-vertex locations.

**Key decision** (Session 91): rather than abandon the K3-doublet basis at the obstruction, extend FI-C-3 to include perpendicular-wavefunction ζ-parity content. **Alternative considered**: reformulate the closure on a different basis (e.g., a non-TBM-aligned K3 basis). **Rejection reason for alternative**: would break inheritance from SF-4 v4.0 THEO-SF-4-5 cage-shell coupling mechanism and require parallel re-derivation of the K3 antibonding doublet. The chosen path preserves SF-4 inheritance.

## Vignette 6 — Sessions 92–93 (Wigner-Eckart framework + sin²θ_13 scaling tension, Patches 0386–0387)

Sessions 92–93 set up the Wigner-Eckart framework for the K3-amplitude matrix element and revealed the linear-vs-quadratic scaling structure that would later force the $\sin^2\theta_{13}$ re-scoping decision. The framework decomposed $\hat{C}_\chi$ via Wigner-Eckart on the $D_6 = S_3 \times Z_2$ stabilizer: $\hat{C}_\chi$ lives in irrep $B_2 = A_2 \times \zeta\text{-ODD}$ ($A_2$ being the sign irrep of $S_3$, ζ-ODD being the antisymmetric Z_2 irrep). The $A_2$ component selects the K3-amplitude transformation type; the ζ-ODD component selects the perpendicular-wavefunction transformation type.

The linear-vs-quadratic tension surfaced at Session 93: standard QFT-perturbation theory gives $\sin^2\theta_{13} \propto \|M\|^2$ (quadratic in the chirality matrix element), which would predict $\sin^2\theta_{13} \approx (\chi/6)^2 \approx 1.55 \times 10^{-3}$, off by factor 21 from the NuFIT 6.0 empirical value $0.0222 \pm 0.00069$. The candidate γ structural observation surfaced: $\sin^2\theta_{13} = b \cdot m_\perp = \chi/(6\sqrt{3}) \approx 0.0227$ matches observation within 1σ but requires CPP-specific linear-scaling framework (rather than the standard QFT quadratic scaling). The tension was registered at Session 93 close for v1.0+ resolution.

## Vignette 7 — Session 95 (unique $A_2$ generator correction, Patch 0389)

Session 95 substantively corrected the Session 93 parameterization. The σ_1-ODD operator on K3-amplitudes had been parameterized as a general (a,b)-mixing of $E$ and $A_2$ irrep content, but $\hat{C}_\chi$ in $B_2$ of $D_6$ requires the unique $A_2$ generator $T_{A_2}(b) = i \cdot b \cdot S$ specifically — where $S$ is the antisymmetric 3×3 matrix encoding the K3-vertex cyclic permutation (cross-product-with-$(1,1,1)$ structure). The (a,b)-parameterization had carried an $E$-irrep contamination that produced incorrect K3-amplitude matrix elements.

The corrected K3-amplitude matrix element is $M_{K3} = -i \cdot b \cdot \sqrt{3}$, with the $\sqrt{3}$ in the numerator (the earlier (a,b)-form had $\sqrt{3}$ in the denominator). The correction was load-bearing for the subsequent chirality-eigenvalue matching: the corrected magnitude $\|M_{K3}\| = \|b\| \cdot \sqrt{3}$ combined with chirality-eigenvalue matching $b = \chi/\sqrt{3}$ produces $\|M_{K3}\| = \chi$ at zero free parameters. The earlier parameterization would have produced an off-magnitude prediction. Session 95's correction is documented at `Capotauro_subclaim_c_wigner_eckart.md` §3.4 with the unique-$A_2$-generator derivation as Lemma 4.2.

**Dead end** (Session 93–95 interim): the general (a,b)-parameterization for σ_1-ODD operators was operative across Sessions 93–94 working toward closure. Session 95 surfaced that the $E$-irrep content in (a,b)-form was structurally inadmissible for $\hat{C}_\chi$. **Rejection reason**: violates irrep purity required by Wigner-Eckart factorization; the unique $A_2$ generator is forced by the irrep selection.

## Vignette 8 — Sessions 96–97 (chirality-eigenvalue matching + cage-shell averaging, Patches 0390–0391)

Session 96 Patch 0390 closed the chirality-eigenvalue matching principle: the unique $A_2$ generator $T_{A_2}(b) = i \cdot b \cdot S$ has eigenvalues $\{0, +b\sqrt{3}, -b\sqrt{3}\}$ on the K3-amplitude basis from the cross-product-with-$(1,1,1)$ structure of $S$. Setting the non-zero K3-amplitude eigenvalues equal to the substrate chirality eigenvalues $\pm\chi$ gives $b = \chi/\sqrt{3}$ and hence $\|M_{K3}\| = \chi$ at zero free parameters. The derivation principle uses Hermitian-operator spectral analysis rather than ad-hoc parameter assignment.

Session 97 Patch 0391 closed the cage-shell averaging principle: the perpendicular-wavefunction matrix element $\|M_\perp\| = d_E/V_\text{cage} = 2/12 = 1/6$ via FI-C-10 + Schur orthogonality on the icosahedral cage. The factor $2 = d_E$ is the dimension of the $E$ irrep of $D_6$ to which the K3-doublet states belong; the factor $12 = V_\text{cage}$ is the icosahedral first-shell vertex count of the cage substrate, which equals $\|D_6\|$ by the icosahedral cage's $D_6$ stabilizer symmetry. The structural identity $V_\text{cage} = \|D_6\| = 12$ is what makes the averaging factor clean.

FI-C-10 was registered at Session 97 as a foundational input extending FI-C-6 (cage-shell coupling mass-formula mechanism from SF-4 v4.0 THEO-SF-4-5) from mass observables to chirality observables. Three plausibility arguments justify the extension at v1.0: substrate-isotropy, DI-bit propagation, and FI-C-6 precedent as observable-class-independent. The observable-class-independence claim distinguishing FI-C-10 from FI-C-6 is physically motivated but not formally derived from CPP axioms — registered as open work post-v1.0.

## Vignette 9 — Session 98 (THEO-CAP-1 formalization, Patch 0392)

Session 98 formalized the Composite Capotauro Wigner-Eckart Theorem (THEO-CAP-1) with eight-step proof + end-to-end numerical verification at machine precision ($10^{-17}$). The theorem statement: $\|M\| = \|\langle\Phi_-^{(1)}\|\hat{C}_\chi\|\Phi_-^{(2)}\rangle\| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ on the TBM-aligned K3-doublet of charged-lepton substrate states, under FI-C-1 through FI-C-10 + 4 CPP axioms (A1, A3, A4, A7) conditional closure.

The eight-step proof structure: (i) K3-doublet extended TBM-aligned basis construction; (ii) chirality observable $\hat{C}_\chi$ irrep classification in $B_2$ of $D_6$; (iii) Wigner-Eckart factorization on $D_6 = S_3 \times Z_2$ separating K3-amplitude and perpendicular-wavefunction factors; (iv) unique $A_2$ generator $T_{A_2}(b) = i \cdot b \cdot S$ identification; (v) chirality-eigenvalue matching giving $b = \chi/\sqrt{3}$ and $\|M_{K3}\| = \chi$; (vi) cage-shell averaging via Schur orthogonality giving $\|M_\perp\| = 1/6$; (vii) composite product $\|M\| = \|M_{K3}\| \cdot \|M_\perp\| = \chi/6$; (viii) substrate-vacuum substitution $\chi = \phi^{-3}$ from FI-C-9 yields $\|M\| = \phi^{-3}/6 \approx 0.0394$. End-to-end numerical verification confirmed agreement at machine precision.

## Vignette 10 — Sessions 99–101 (sin²θ_13 re-scoping, Patches 0393–0395)

Sessions 99–101 attempted to extend the framework from $\Delta p_{LR}$ (a chirality observable) to $\sin^2\theta_{13}$ (a PMNS mixing-angle observable) via PMNS perturbation machinery. The attempt tested 22 candidate scalings; only candidate γ ($\sin^2\theta_{13} = b \cdot m_\perp$) matches observation within 1σ but requires the CPP-specific linear scaling that standard QFT-perturbation cannot reproduce; wavefunction-level coupling hypothesis also gives quadratic scaling (off by factor 64).

**Dead end** (Sessions 99–101): the wavefunction-level coupling hypothesis was ruled out at Session 101 Patch 0395 after explicit derivation showed quadratic-in-$\|M\|$ scaling structurally — off by factor $1/\chi^2 \approx 18$ from the candidate-γ linear-scaling target. **Rejection reason**: the wavefunction-level coupling produces $\sin^2\theta_{13} \propto \|M\|^2$ structurally; no perturbative reformulation within standard QFT framework yields linear scaling.

**Key decision** (Session 101): re-scope $\sin^2\theta_{13}$ derivation to SF-2 v2.0+ rather than attempting in-paper closure at Capotauro v1.0. **Alternative considered**: ship Capotauro v1.0 with a $\sin^2\theta_{13}$ "candidate γ" structural observation as an honest acknowledgment of partial progress. **Rejection reason for alternative**: candidate γ requires CPP-specific linear-scaling framework that hasn't been developed; presenting it without the framework would over-claim. The re-scoping defers Q11 ($\sin^2\theta_{13}$ derivation) to SF-2 v2.0+ where the substrate-vacuum dynamics from sub-claim (b) Reading C closure may surface the required linear-scaling framework.

## Vignette 11 — Sessions 102–103 (closure declaration + THEO-CAP-1 registration, Patches 0396–0397)

Session 102 Patch 0396 declared sub-claim (c) v1.0 closure with packaged Sessions 88–101 trajectory summary. The closure declaration enumerated the eight derivation steps + the $\sin^2\theta_{13}$ re-scoping decision + the v1.0 scope boundary.

Session 103 Patch 0397 registered THEO-CAP-1 in `theorem-registry.md` as theorem #62 in the SF-Line section — **the first programme-level theorem registered ahead of its own flagship paper publication in the CPP corpus**. The registration was justified by four conditions: (i) rigorous proof at Wigner-Eckart level; (ii) end-to-end numerical verification at machine precision; (iii) primary empirical prediction $\Delta p_{LR} \approx 0.0394$ validated within 2% of empirical anchor $\sim 0.04$ from leptogenesis back-derivation; (iv) honest scope-limitation framing for re-scoped Q11 sub-problem. The registration established a methodological pattern for theorem-registry registration from flagship-paper-pending working sketches when those four conditions are met.

## Vignette 12 — Sessions 104–105 (outline + v0.1 .tex skeleton, Patches 0398–0399)

Session 104 Patch 0398 created `capotauro_outline.md` (327 lines): full paper structure with §1–§13 + appendices + bibliography placeholder + foundational-input enumeration FI-C-1 through FI-C-10. The outline established the paper's expository architecture: §1 introduction + §2 substrate-vacuum chirality (SSB framing at v0.x; reframed Session 120) + §3 K3-doublet extended TBM-aligned basis + §4 $D_6$ Wigner-Eckart + §5 composite Wigner-Eckart theorem + §6 $\Delta p_{LR}$ prediction + §7 $\sin^2\theta_{13}$ posture + §8 falsifier set + §9 open work + §10 discussion + §11 FI summary + §12 conclusions + §13 acknowledgments.

Session 105 Patch 0399 created `capotauro.tex` v0.1 with preamble + section skeleton + bibliography stub. The .tex foundation followed the SS-9 / SF-4 / SF-2 LaTeX conventions: amsmath + amssymb + amsthm + mdframed + tikz + hyperref. The bibliography file `bibliography/cpp_references.bib` was the canonical reference target per OPEN-WORKFLOW-1 single-source-of-truth convention.

## Vignette 13 — Sessions 107–112 (v0.2 → v0.6 content expansion + first PDF, Patches 0400–0404)

Sessions 107–112 built the paper from v0.1 skeleton to v0.6 first-PDF-compile state across five content-expansion patches:

- **Session 107 Patch 0400 (v0.2)**: §2 substrate-vacuum + §3 K3-doublet content expansion. §2 introduced the SSB framing (to be reframed Session 120) with FI-C-9 substrate primitive chirality magnitude as the foundational input; §3 extended SF-4 v4.0's K3 antibonding doublet with FI-C-3 perpendicular wavefunctions.
- **Sessions 108–109 Patch 0401 (v0.3)**: §4 $D_6$ Wigner-Eckart + §5 composite WE theorem content expansion. §4 introduced the irrep classification $B_2 = A_2 \times \zeta\text{-ODD}$ for $\hat{C}_\chi$; §5 derived the chirality-eigenvalue matching principle and the cage-shell averaging factor, with THEO-CAP-1 as Theorem 5.1.
- **Session 110 Patch 0402 (v0.4)**: §6 $\Delta p_{LR}$ + §7 $\sin^2\theta_{13}$ posture + §8 falsifier set content expansion. §6 derived $\Delta p_{LR} = \chi/6 \approx 0.0394$ with empirical comparison to leptogenesis back-derivation; §7 documented the candidate γ scaling and re-scoping decision; §8 enumerated the falsifier set.
- **Session 111 Patch 0403 (v0.5)**: §9 open work + §10 discussion + §11 FI summary content expansion. §9 enumerated sub-claim (a) + sub-claim (b) + FI-C-10 first-principles + Q11 $\sin^2\theta_{13}$ as v2.0+ work; §10 discussed methodological observations; §11 consolidated FI-C-1 through FI-C-10.
- **Session 112 Patch 0404 (v0.6)**: integration polish + first PDF compile (35 pages, 481 KB). End-to-end numerical verification embedded in §5; cross-references resolved; bibliography compiled clean.

## Vignette 14 — Session 113 (ChatGPT v0.6 review + Grok-suspension cleanup, Patches 0405–0406)

Session 113 Patch 0405 archived the ChatGPT v0.6 review at `flagship_papers/capotauro/reviews/chatgpt_v0.6_session_113.md`. ChatGPT's response was substantively positive on the theorem-level structural derivation but flagged five items: (i) §6.6 nontriviality argument needed strengthening (the $\Delta p_{LR}$ derivation needs to demonstrate that the chirality matrix element is genuinely nontrivial, not a trivial structural artifact); (ii) §2.3 forward argument needed sharpening for the SSB framing; (iii) §5.4 motivation for FI-C-10 needed precedent argument from FI-C-6; (iv) §6.1.1 experimental anchor framing too compressed; (v) §9.5 experimental open work missing.

Session 113 Patch 0406 performed programme-infrastructure Grok-suspension-warning cleanup (out-of-scope but timed in session) — completed the documentation around Grok's suspension protocol per OPEN-WORKFLOW-3 vocabulary contamination findings. Not Capotauro-specific.

## Vignette 15 — Sessions 114–115 (v0.7 substantive rework + changelog file creation, Patches 0407–0408)

Session 114 Patch 0407 delivered v0.7 Group A substantive physics rework addressing ChatGPT v0.6 items: §6.6 nontriviality strengthened via explicit construction of trivial-case counterexample showing the chirality matrix element vanishes when substrate chirality is zero; §2.3 forward argument sharpened with three-step substrate-vacuum derivation; §5.4 motivation strengthened with FI-C-6 precedent argument from SF-4 v4.0 THEO-SF-4-5; §6.1.1 experimental anchor framing expanded; §9.5 experimental open work added.

Session 115 Patch 0408 delivered v0.7 Group B writing/style + title-block cleanup + **creation of this changelog file** (`flagship_papers/capotauro/documentation_suite/changelog-capotauro.md`) at Patch 0408 as reference implementation for changelog-architecture standardization. The v0.7 PDF ships with all five ChatGPT v0.6 items addressed.

**Key decision** (Session 115): create per-paper changelog file rather than carrying paper-level CHANGELOG comment blocks in the .tex source. **Alternative considered**: keep CHANGELOG content in the .tex source as a section before the bibliography. **Rejection reason for alternative**: clutters the paper PDF with programme-internal version archaeology that belongs in documentation suite, not in the reader-facing paper. The decision became the reference implementation for OPEN-WORKFLOW-DOC-CHANGELOG (programme-wide changelog-architecture standardization at Session 116).

## Vignette 16 — Session 116 (programme-infrastructure changelog standardization, Patch 0409)

Session 116 Patch 0409 codified the Patch 0408 reference implementation as programme-wide rule across `operating_system.md` + `paper-formatting.md` + `documentation-suite.md` + `paper_production_workflow.md` + `paper_completion_checklist.md` + `bootup.md`. Forward-only migration policy: existing shipped papers (SS-9, SF-4, SF-2) preserve their .tex-embedded CHANGELOG blocks at v1.0; new papers (Capotauro and beyond) follow the per-paper-changelog-file convention. The decision created the changelog-architecture standardization which is now the programme-wide rule.

This was an out-of-Capotauro-scope programme-infrastructure session that produced a Capotauro-precedent-grounded discipline-tightening rule. Pattern noted: paper-specific innovation that becomes programme-wide rule via codification patch. Same pattern would later apply (Session 123 OPEN-WORKFLOW-DOCS-CATCHUP discussion) for the post-SHIP documentation-suite discipline.

## Vignette 17 — Session 117 (ChatGPT v0.7 round-2 review, Patch 0410)

Session 117 Patch 0410 archived the ChatGPT v0.7 round-2 review at `flagship_papers/capotauro/reviews/chatgpt_v0.7_session_117.md`. ChatGPT's overall response was strongly positive — *"mature conditional-theorem flagship paper"* — with four remaining items mapped to v0.8 disposition table: (i) §1.7 derivation-flow TikZ figure desirable for reader-accessibility; (ii) §1.2 cross-reference to §6.6 needed for nontriviality discoverability; (iii) §5.4 FI-C-6 precedent argument for FI-C-10 needed brief expansion; (iv) §6.1.1 tightening; (v) §10 methodological observations merged into single subsection. Five discoverability gaps also identified.

ChatGPT recruited as strongest reviewer at this point — caught errors others missed in prior rounds. The methodological pattern noted: ChatGPT's round-2/round-3 reviews are where the most substantive critique arrives; the first-round review is often "open and explore" while subsequent rounds tighten on specific items.

## Vignette 18 — Session 118 (v0.8 substantive expositional polish, Patch 0411)

Session 118 Patch 0411 delivered v0.8 substantive expositional polish: NEW §1.7 derivation-flow TikZ figure (visualizes the eight-step proof structure); §1.2 cross-reference to §6.6 (closes the nontriviality discoverability gap); §5.4 FI-C-6 precedent argument expanded with explicit observable-class-independence argument; §6.1.1 tightened; §10 methodological observations merged into single subsection. All five ChatGPT v0.7 items addressed.

The v0.8 PDF is the first version ready for parallel multi-reviewer round (ChatGPT round-3 + CoPilot round-1 + Grok round-1) — three reviewers reviewing the same version in parallel to surface convergence/divergence patterns.

## Vignette 19 — Session 119 (three v0.8 reviews in parallel, Patch 0412)

Session 119 Patch 0412 archived three v0.8 reviews in parallel:

- **ChatGPT round-3** at `reviews/chatgpt_v0.8_session_119.md`: *"mature conditional-theorem flagship paper"*; 4 problems carry-over from v0.7, 5 v0.9 items, 2 discoverability gaps.
- **CoPilot round-1** at `reviews/copilot_v0.8_session_119.md`: *"extremely close to v1.0 ship-ready"*; 5 tightening items including a flag on `gandolfi_2025` citation veridicality (CoPilot could not find the cited paper in any database).
- **Grok round-1** at `reviews/grok_v0.8_session_119.md`: *"Ship as v1.0"*; 4 minor polish items including 2025 Grok co-authorship footnote concern, higher-n undershoot quantification, and the joint main + Companion format endorsement for SF-line work.

**Cross-reviewer convergence on SHIP-readiness achieved at v0.8 Session 119 Patch 0412** — all three reviewers independently flagged "extremely close to v1.0 ship-ready" or "ship as v1.0" with only light polish items remaining. This convergence was the SHIP signal for the subsequent v0.9 polish-and-ship trajectory.

## Vignette 20 — Session 120 (v0.9 polish + foundational framing reframe, Patch 0413)

Session 120 Patch 0413 delivered v0.9 polish plus **the methodologically critical foundational framing reframe**: §2 reframed from "Substrate-Vacuum Broken-Symmetry Physics" to "Substrate-Vacuum Chirality as Primitive Feature" per CPP-core-principle methodological commitment that mathematical descriptions are not physical mechanisms. SSB framing demoted to mathematical-equivalence alternative in Remark 2.2. Sub-claim (b) renamed from "symmetry-breaking dynamics derivation" to "substrate chirality mechanism candidate derivation." Sub-claim (a) clarified as universe-wide sign-selection event downstream of sub-claim (b) magnitude mechanism.

The reframe was prompted by ChatGPT v0.7 round-2 + v0.8 round-3 reviewer flag that the SSB framing constituted a methodological deviation from CPP's distinctive epistemic stance. The CPP methodological commitment is that physical mechanisms underlie mathematical descriptions; SSB is a mathematical description (a Lagrangian/effective-field-theory pattern) rather than a physical mechanism. Treating the substrate's primitive chirality as a foundational feature coeval with CPs/GPs and the rules of their interaction honors the CPP methodological commitment; the SSB framing was preserved as mathematically-equivalent alternative in Remark 2.2.

**Key decision** (Session 120): reframe v0.x SSB framing to primitive-feature framing while preserving SSB as mathematical-equivalence alternative. **Alternative considered**: keep the SSB framing as primary throughout the paper. **Rejection reason for alternative**: SSB is a mathematical description of symmetry-breaking patterns in continuum field theories, not a physical mechanism in CPP's discrete-substrate framework. Treating it as the primary framing would mis-identify CPP with continuum-EFT traditions. The reframe is the methodologically-honoring choice.

Other v0.9 polish items: 8 ADDRESS items + 2 DISCOVERABILITY items from v0.8 cross-reviewer disposition (Grok #1/#2/#3, CoPilot #4/#2/#3/#1/#5a, ChatGPT #4 + discoverability); residual broken-symmetry-language cleanup throughout abstract + plain-English summary + §5/§6/§8/§9/§13. The `gandolfi_2025` citation was removed (web_search confirmed no matching paper) and §2.4 empirical-anchor paragraph rewritten. 1149 lines (-9 from v0.8); 46 pages 601 KB; theorem count unchanged at 6; pdflatex two-pass compile VERIFIED CLEAN.

**Dead end** (Session 120): the `gandolfi_2025` cosmological-anchor citation (originally inherited from December 2025 Capotauro nucleation paper material) failed veridicality verification at CoPilot v0.8 review. **Rejection reason**: web_search via three independent databases (arXiv, Google Scholar, ADS) returned no matching paper; the citation was unverifiable. The §2.4 empirical-anchor paragraph was rewritten to use only the verified leptogenesis-back-derivation chain ($\eta_B$ from Planck 2018 + standard washout/sphaleron-equilibration assumptions).

## Vignette 21 — Session 121 (Reading C mechanism candidate sketch, Patch 0414)

Session 121 Patch 0414 created new working sketch `flagship_papers/capotauro/sketches/Capotauro_chiral_mechanism_candidate.md` (296 lines) developing **Reading C** as the candidate physical mechanism for FI-C-9's primitive chirality magnitude. The sketch is the working development of v0.9 paper §9.2 sub-claim (b) "substrate chirality mechanism candidate derivation."

Reading C's structure: a primitive 4D direction $\hat{n}$ in the substrate's ambient 4D space produces direction-correlated edge-length variation in the 600-cell lattice at the $\phi^{-3}$ scale; the $H_4 \to I_4$ algebraic structure is the structural consequence of $\hat{n}$ being primitive rather than the outcome of a dynamical event; the chirality magnitude $\|\chi\| = \phi^{-3}$ is **derived** rather than postulated, via the perturbative-distance-ratio constraint applied to the $\hat{n}$-perturbation. New structural prediction: fractional chirality retention across observable classes — mass observables retain $O(\chi^2) \approx 0.6\%$; chirality observables retain full $\chi/6 \approx 4\%$; intermediate observables retain calculable fractions.

Five open questions registered for sub-claim (b) closure trajectory (estimated 10–20 sessions to Layer 3 closure): **Q1** group-theoretic verification of $H_4$ stabilizer of $\hat{n} \cong I_4$ (1–3 sessions, first sub-step, triggers Capotauro v2.0+); **Q3/Q4** perturbative-distance-ratio sharpening; **Q5/Q6** cross-sector consistency with SF-2 W bracelet $D_6$ and SM-2 qDP/eDP asymmetry; sub-claim (a) cosmological-timing interaction. Tier-4 reasoning capture at Layer 1 / Layer 2 epistemic status (physical intuition + structural mathematical sketching), not Layer 3 (formal theorem closure).

The sketch was registered at `Research_Frontier.md` OPEN-FI-C-9-FP-MECHANISM as the canonical sub-claim (b) closure trajectory. The v0.9 paper bibliography entry `abshier_capotauro_chiral_mechanism_sketch` was added in Patch 0413; Patch 0414 added the actual sketch file.

## Vignette 22 — Session 122 (v1.0 SHIP via title-block bump, Patch 0415)

Session 122 Patch 0415 shipped **Capotauro paper v1.0 SHIPPED** via title-block bump only: `Version 0.9 --- 16 May 2026` → `Version 1.0 (SHIPPED) --- 16 May 2026`. Substantive paper content unchanged from v0.9 (Patch 0413); all other paper content preserved. The paper body already references v1.0 throughout via the closure trajectory's forward-targeting language (the "what is out of scope at v1.0" enumeration in the abstract, the "v1.0" qualifier on foundational input postulates, the v1.0 / v2.0+ scope-deferral language in the open-work sections). The version-bump-only character of this SHIP confirmed that the v0.9 cross-reviewer convergence on SHIP-readiness was the correct SHIP signal.

Programme-level changes at v1.0 SHIP: (1) `Research_Frontier.md` OPEN-SM-4 status PARTIAL CLOSURE; (2) NEW `Research_Frontier.md` OPEN-FI-C-9-FP-MECHANISM entry; (3) `theorem-registry.md` THEO-CAP-1 paper-level confirmation (theorem count UNCHANGED at 62; THEO-CAP-1 already registered Session 103 Patch 0397); (4) `paper_catalog.md` SF-Line Capotauro row + Documentation paragraph; (5) `INDEX.md` flagship_papers Capotauro entries; (6) NEW `flagship_papers/capotauro/README.md` paper-level README. The patch 0415 commit message's bundled "All registers UNCHANGED at programme level" framing missed three drift items in predictions.md / master_glossary.md / problem_histories/PH-OPEN-SM-4.md (caught and fixed at Patch 0416A retroactively).

**Capotauro paper is the third flagship paper to ship at v1.0 in the CPP corpus** (after SS-9 Session 32, SF-4 Session 54, SF-2 Session 83) and **the first flagship paper outside the SF-N numerical convention**. The THEO-CAP-N naming for the Capotauro theorem chain reflects its flagship-paper-pending status preserved through v1.0 SHIP, recording that the paper's primary programme-level theorem (THEO-CAP-1) was registered Session 103 Patch 0397 ahead of its own paper publication, the first such registration pattern in the CPP corpus.

**Capotauro v1.0 SHIPPED. Substantive content frozen at v1.0; documentation suite ACTIVE.**

---

## Cumulative campaign metrics

- **Total sessions**: 37 (Session 86 closure trajectory opening through Session 122 v1.0 SHIP).
- **Total patches**: 40 (Patches 0376–0415).
- **Source line count**: 0 → 1149 (.tex grew incrementally across v0.1 → v0.9; v1.0 SHIP via title-block bump only).
- **PDF page count**: 0 → 35 (v0.6) → 38 (v0.7) → 42 (v0.8) → 46 (v0.9/v1.0).
- **Bibliography**: 14 entries.
- **Theorems**: 1 conditional flagship (THEO-CAP-1, theorem #62 SF-Line section, registered Session 103 Patch 0397 ahead of paper publication — first such pattern in CPP corpus) + 5 sub-theorems within the paper structure.
- **Predictions**: 1 primary empirical prediction at zero free parameters ($\Delta p_{LR} = \chi/6 \approx 0.0394$ within 2% of empirical anchor $\sim 0.04$ from leptogenesis back-derivation); registered as PRED-O-25 at Patch 0416A.
- **Foundational inputs**: 10 (FI-C-1 through FI-C-10), with FI-C-9 + FI-C-10 distinctively introduced for the Capotauro mechanism (substrate primitive chirality magnitude + cage-shell observable-class extension).
- **Sub-claim closure status at v1.0 SHIP**: sub-claim (c) CLOSED at conditional theorem level via THEO-CAP-1; sub-claims (a) + (b) OPEN (sub-claim (b) Reading C candidate registered Session 121 Patch 0414).
- **Reviews**: 5 independent AI passes (ChatGPT × 3 + CoPilot × 1 + Grok × 1) with cross-reviewer convergence on SHIP-readiness at v0.8 Session 119 Patch 0412.
- **Falsifier set**: 3 direct ($\Delta p_{LR}$ outside ±2% in direct measurement; sub-claim (b) Reading C $H_4 \to I_4$ stabilizer claim failure; FI-C-10 observable-class-independence failure under SF-4 v4.5+ integration).
- **Major framing decisions**: 2 (Session 91 FI-C-3 extension with opposite-ζ-parity assignment; Session 120 SSB → primitive-feature framing reframe).
- **Dead ends rejected**: 3 (original $\chi \approx \phi^{-1}$ conjecture; general (a,b)-parameterization on σ_1-ODD operators; wavefunction-level coupling hypothesis for $\sin^2\theta_{13}$).

---

## Contributor roles

- **Dr. Thomas Lee Abshier ND** (Hyperphysics Institute): Principal investigator. Drives all physical vision and intuition, including the primitive-feature framing methodological commitment (Session 120 reframe), the parallel-window workflow design (Session 123 doc-suite / physics parallelization decision), and the discipline-tightening-after-precedent principle (Session 123 OPEN-WORKFLOW-DOCS-CATCHUP scheduling decision). Reviewer of all AI-generated content; final approver of all patches.
- **Claude Opus (Anthropic)**: Primary co-author. Mathematical formalization of THEO-CAP-1, paper drafting across v0.1 → v1.0, working-sketch development for sub-claim (c) closure trajectory + Reading C candidate, working-tree patch construction, registry maintenance, §15 Session-Close Handover Protocol execution.
- **ChatGPT (OpenAI)**: Strongest reviewer. Three rounds (v0.6 / v0.7 / v0.8) with the round-2 + round-3 rounds delivering the most substantive critique. Surfaced the foundational framing methodological flag at v0.7 round-2 that led to the Session 120 SSB → primitive-feature reframe.
- **CoPilot (Microsoft)**: Round-1 reviewer at v0.8. Surfaced the `gandolfi_2025` citation veridicality flag (rejected at Session 120 Patch 0413 after web_search verification failed).
- **Grok (xAI)**: Round-1 reviewer at v0.8 (Grok was suspended at Session 110 for vocabulary contamination per OPEN-WORKFLOW-3 findings; rehabilitated at Session 119 for the v0.8 review round only with vocabulary protocol enforced). Surfaced the higher-n undershoot quantification need; endorsed joint main + Companion format for SF-line papers.

---

## Transcript references

- **Working sketches** (canonical Tier-4 reasoning source per SF-4 v4.0 convention):
  - `flagship_papers/capotauro/sketches/Capotauro_chi_phi_closure.md` (681 lines, parent sketch, FI-C-9 closure trajectory Sessions 86–102).
  - `flagship_papers/capotauro/sketches/Capotauro_subclaim_c_wigner_eckart.md` (2146 lines, sub-claim (c) detailed closure with Theorem 18.1 + §22 v1.0 closure narrative, Sessions 88–101).
  - `flagship_papers/capotauro/sketches/Capotauro_chiral_mechanism_candidate.md` (296 lines, Reading C geometric-chirality candidate for sub-claim (b), Session 121).
- **Reviews** (verbatim archival):
  - `flagship_papers/capotauro/reviews/chatgpt_v0.6_session_113.md`
  - `flagship_papers/capotauro/reviews/chatgpt_v0.7_session_117.md`
  - `flagship_papers/capotauro/reviews/chatgpt_v0.8_session_119.md`
  - `flagship_papers/capotauro/reviews/copilot_v0.8_session_119.md`
  - `flagship_papers/capotauro/reviews/grok_v0.8_session_119.md`
- **Four-tier discipline files**:
  - `handover-capotauro.md` (Session 122 close §15 Step H, retroactively recorded Patch 0416 Session 123).
  - `development-capotauro.md` (this file).
  - `transcript-capotauro.md` (per-session transactions, pending Patch 0416C).
  - `reasoning-capotauro.md` (Tier 4 verbatim reasoning, pending Patch 0416D; may be a pointer file to the three working sketches per SF-4 v4.0 convention).
- **Programme-level registries**:
  - `theorem-registry.md` THEO-CAP-1 (theorem #62, SF-Line section).
  - `Research_Frontier.md` OPEN-SM-4 (PARTIAL CLOSURE) + OPEN-FI-C-9-FP-MECHANISM.
  - `predictions.md` PRED-O-25 (registered Patch 0416A).
  - `master_glossary.md` Capotauro v1.0 substrate-vacuum chirality framework terms section (12 entries, registered Patch 0416A).
  - `problem_histories/PH-OPEN-SM-4.md` (canonical problem-history narrative, created Patch 0416A).

---

## Vignette 23 — Session 123 (retroactive handover + registry drift fix, Patches 0416 + 0416A)

After Capotauro paper v1.0 SHIPPED at Session 122 Patch 0415, the prior context window closed mid-conversation during a post-SHIP discipline-tightening discussion proposing OPEN-WORKFLOW-DOCS-CATCHUP registration. No §15 Step H handover document was produced at Session 122 close. Session 123 opened with retroactive handover work as Patch 0416 (handover-capotauro.md + session log + changelog register row), followed immediately by Patch 0416A (registry drift fix surfaced by §15 Step E per-registry audit at handover construction).

Patch 0416 §15 Step E audit caught three drift items the Patch 0415 v1.0 SHIP commit's bundled "All registers UNCHANGED at programme level" framing missed: (a) `predictions.md` PRED-O-25 entry for $\Delta p_{LR} = \chi/6 \approx 0.0394$ missing; (b) `master_glossary.md` Capotauro terms section missing; (c) `problem_histories/PH-OPEN-SM-4.md` not existing. Drift items scheduled for Patch 0416A fix BEFORE downstream Section A doc-suite production reads from the registries and propagates drift downstream into `phenomena-capotauro.md` + `glossary-capotauro.md` companions.

**Key decision** (Session 123): parallel-window workflow design — open Capotauro v1.0 handover document in separate context window for forward-physics arc (Reading C Q1 closure on integer patches 0417+); continue documentation suite production in current window with letter-suffix patches (0416A through 0416M). **Alternative considered**: single-window sequential workflow (do all docs first, then open new window for physics). **Rejection reason for alternative**: docs work and forward physics are largely independent at the file level (docs reads from frozen v1.0 source; physics writes new v2.0+ sketches); parallelization captures user processing-time gaps for context-switching between windows. Push-pull discipline on shared files (`Research_Frontier.md`, `theorem-registry.md`, `master_glossary.md`, `changelog-capotauro.md`) prevents merge conflicts.

**Methodological decision** (Session 123): OPEN-WORKFLOW-DOCS-CATCHUP registration deferred to `todolist.md` post-Capotauro-Section-A-completion (Patch 0416M) per **discipline-tightening-after-precedent principle**: doing one full Capotauro doc-suite example end-to-end before codifying the programme-wide discipline makes the rule more credible than codifying-aspirationally-before-executing. The Patch 0416A drift surface validates this principle in real-time: the Step E audit catching three drift items the v1.0 SHIP commit's framing missed is the discipline working correctly when executed.

Patch 0416A landed registry drift fix at 4 files (predictions.md + master_glossary.md + PH-OPEN-SM-4.md + changelog-capotauro.md) at commit `82bbec8`. First letter-suffix patch in the post-SHIP Capotauro doc-suite catch-up arc.

## Vignette 24 — Session 123 (this development file, Patch 0416B)

Patch 0416B (this patch) creates `development-capotauro.md` covering Sessions 86–122 closure trajectory + Session 123 post-SHIP doc-suite catch-up vignettes. Per `paper_completion_checklist.md` A5 + `documentation-suite.md` §1 convention, the development file serves dual role: (i) Section E Tier-3 vignettes for the four-tier discipline (vignette-driven narrative format); (ii) Section A5 standalone development-history companion file (with version timeline, key decisions, dead ends, contributor roles, transcript references woven into the vignettes rather than separated into structured sections, following the SF-4 / SF-2 / SS-9 convention).

Total vignettes: 24 (22 covering Sessions 86–122 + 2 covering Session 123 doc-suite catch-up). Forward queue: Patch 0416C `transcript-capotauro.md` + Patch 0416D `reasoning-capotauro.md` complete Section E four-tier discipline files; Patches 0416E–J complete Section A 6 standalone companions (mechanism + glossary + phenomena + philosophy + reviews + keywords); Patch 0416K anthology chapter at Rovelli/SciAm register; Patch 0416L TATWD integration to `CPP_the_theory.md`; Patch 0416M OPEN-WORKFLOW-DOCS-CATCHUP registration in `todolist.md` after Capotauro doc-suite arc complete.

---

## Vignette 25 — Session 127 (Patch 0422): Programme-level umbrella registration

Session 127 opened the Reading C closure arc with a structural observation Thomas had been holding since the Session 120 SSB → primitive-feature framing reframe: the chirality magnitude χ = φ^-3 that Capotauro takes as foundational input FI-C-9 is *the same chirality* that the W-bracelet sector inherits in SF-2. The two papers had independent OPEN-FP entries (OPEN-FI-C-9-FP-MECHANISM and OPEN-FP-SF-2-CHIR) — siblings without a registered parent. The Session 127 work registered the programme-level umbrella **OPEN-SD-CHIR-PRIMITIVE** in the SD (substrate-derivation) section, with five-manifestation scope wide enough that future cross-sector findings can attach without re-architecting and narrow enough that the umbrella is not a catch-all. The umbrella entry sits *above* OPEN-FI-C-9 and OPEN-FP-SF-2 in the registry hierarchy.

The second piece of Session 127 was `founders_voice/005_chirality_is_primitive.md` (~180 lines), a verbatim recovery of the Session 120 founder's-confrontation reasoning. Thomas's pushback against the SSB framing and the resulting reframe to primitive-feature was substantively in the Capotauro paper's §3 framing but had not been preserved as a verbatim founders-voice artifact per the §4 Tier-1 codification. The recovery acknowledged honestly in the file as "reconstructed from paper §3 + Session 120 transcript pointers + my recollection of the exchange" rather than claimed as fully verbatim — the Session 120 conversation itself was lost to context-window compaction before the founders_voice/005 file convention existed. Patch 0422 landed at commit `a4f8656`; Research_Frontier.md problem counts 93 → 94 entries / 58 → 59 open.

## Vignette 26 — Session 128 (Patch 0423): Q3 Layer 2 attempt — subsequently superseded

**This vignette documents the Session 128 thinking and where it went wrong. The §12 derivation captured here was corrected in Session 129 (Patch 0424). Both the original §12 and the §13 correction are preserved in the sketch per founders_voice/004 audit-trail discipline.**

Session 128 opened with Q3 (the ε-χ relationship — what structural factor k relates the substrate edge-perturbation amplitude ε to the chirality magnitude χ?) as the next priority. The working hypothesis was a two-factor decomposition k = f_geom · f_irrep, with f_geom the geometric projection factor of $\hat n$ onto the K3-doublet's local face plane and f_irrep the Wigner-Eckart irreducible-tensor coupling from the host's local I_h representation to the K3-doublet's stabilizer.

The §12 sketch projected the substrate edge-perturbation onto the K3 face plane *in 3D*, computed f_geom as the cosine of the angle between $\hat n$ and the face normal, obtained a finite f_geom factor, and registered the result as Finding C-W38. The framing felt clean: a two-factor structure with explicit geometric and group-theoretic content. Q4 was queued as the next-session target (the explicit Wigner-Eckart computation of f_irrep on the D_3 × Z_2 stabilizer). Patch 0423 landed at commit `ffe293c`.

The structural error — not yet visible at the close of Session 128 — was that the projection treated the K3 face as if embedded in flat 3-space. The K3-doublet sits in a 600-cell icosahedral cage; the substrate primitive direction $\hat n$ is a 4D vector. The 4D analysis (which Session 129 carried out) shows that all first-shell edges including the K3-base edges are tangent to $\hat n$ identically under vertex-aligned Reading C, so the first-order edge-length perturbations vanish for the entire first shell — and the f_geom factor is zero, not the finite cosine §12 computed. Finding C-W38 and its underlying §12 framing were both retracted in Patch 0424.

## Vignette 27 — Session 129 (Patch 0424): Q3 §13 4D correction + Q4 dissolution

Session 129 opened with the Q4 Wigner-Eckart f_irrep computation queued. The structural error in §12 surfaced when I attempted to set up the projection: the 3D face plane is not invariant under the 4D rotation that takes $\hat n$ to the host vertex direction $v_{\text{host}}$. Under vertex-aligned Reading C with $\hat n = v_{\text{host}}$, the local I_h preservation property — proved as a theorem in §13.3 starting from the substrate edge-length formula and the geometric fact $\hat e_{ab} \cdot v_{\text{host}} = 0$ uniformly on first-shell-icosahedron edges — extends to *all subsets* of the first-shell, including the K3-base edges. The first-order edge-length perturbations of the K3-base edges are zero, not finite.

Once recognized, the §12 derivation collapses: there is no first-order quantity for f_irrep Wigner-Eckart to act on. The structural realization replacing §12: **χ ≡ ε at the substrate level by direct identification under vertex-aligned Reading C**. The "structural factor k" that §12 was decomposing does not exist as a separate object; it is identically 1. Finding C-W39 (NEW; supersedes C-W38) registers the local I_h preservation theorem and the χ ≡ ε identification. Q3 closes at Layer 3 by direct identification. **Q4 dissolves**: it was not a question with a deferred answer but an artifact of the §12 geometric error.

The Capotauro v1.0 paper's |M| = χ/6 prediction is preserved exactly. The paper's §10 cage-shell averaging derivation relies only on local I_h preservation and the d_E/V_cage = 2/12 = 1/6 group-theoretic factor on the K3-doublet's local D_6 stabilizer — both inputs intact under the §13 correction, in fact strengthened (I_h preservation now established at theorem level rather than assumed). Patch 0424 landed at commit `653637c`; Layer 3 closure trajectory revised 7–17 → 5–12 sessions. The methodological observation registered: §12 supersession is *not* a methodological failure to hide; preserving the superseded reasoning in the canonical record is exactly what founders_voice/004 audit-trail discipline is for.

## Vignette 28 — Session 130 (Patch 0425): Q5 Layer 2 closure via Substrate-Locality Unification

Session 130 opened with Q5 (cross-sector consistency with SF-2 W bracelet at theorem level) as the next priority. The strategic question: with Finding C-W39 closing Q3 by direct identification, what does the same identification say about the W-bracelet sector at OPEN-FP-SF-2-CHIR? The structural insight that landed: the §13.3 local-I_h-preservation theorem was proved using only two ingredients — uniform first-shell inner product $v_i \cdot v_{\text{host}} = \phi/2$ and the substrate edge-length formula's $\mathcal{O}(\epsilon)$ dependence on $\hat e_{ab} \cdot \hat n$ — both structural, not specific to the K3-doublet's particular 3-vertex subset. The theorem applies uniformly to any subset of first-shell vertices, including the W-bracelet's 6-vertex Petrie-hexagon subset (per Finding C-W36).

Worked out explicitly for the W-bracelet: all 6 bracelet-perimeter edges have $\hat e_{ab} \cdot \hat n = 0$ identically, and all 6 host-to-bracelet edges have $\hat e_{(\text{host}, a)} \cdot \hat n = -1/(2\phi)$ uniformly. Zero direct edge-length perturbation at $\mathcal{O}(\epsilon)$ for both K3-base and W-bracelet — protected by the same theorem. The geometric distinction *between* them is at the centroid (K3 off-axis with $\hat c_K \cdot v_{\text{host}} = \sqrt 3/2$; W-bracelet on-axis at $c_W = (\phi/2) \hat n$), which governs the sector-specific Schur-orthogonality cage-shell averaging factor — the source of the K3-doublet's 1/6 (paper §10) and the W-bracelet's analog factor (Q5 Layer 3 target).

**Finding C-W40** (NEW): Substrate-Locality Unification under vertex-aligned Reading C — the first explicit cross-sector unification result under the OPEN-SD-CHIR-PRIMITIVE umbrella. Patch 0422's umbrella was a registry-level unification; Finding C-W40 is theorem-level. Both OPEN-FI-C-9 (K3-doublet, mass-mixing) and OPEN-FP-SF-2 (W-bracelet, electroweak V-A) inherit substrate-level chirality from the same χ = ε identification via sector-specific Schur-orthogonality cage-shell averaging on respective D_6 sub-stabilizers of H_3 = I_h.

**Mid-session methodological observation**: at session open, the sketch had *two competing §14 drafts* both produced pre-compaction — v1 (lines 906–1073, ~168 lines) at a Layer 1 sign-coherence framing that conflated helicity fraction with coupling magnitude, and v2 (lines 1074–1165, ~92 lines) at the Substrate-Locality Unification framing above. I read both, judged v2 stronger (the substrate-locality theorem subsumes v1's sign-coherence as a trivial corollary; v1's helicity-vs-magnitude conflation is a structural error), and deleted v1 in-session before committing Patch 0425. The pre-compaction summary had described v2 only; the v1 existence was discovered by direct inspection of the sketch file. Methodological note registered: pre-compaction summaries that describe one of multiple competing drafts must be cross-checked against file state before commit, because the summary is necessarily lossy about which drafts coexist. Patch 0425 landed at commit `b1b17b5`; sketch grows 904 → 997 lines (+93 net). Q5 Layer 3 target: compute the W-bracelet's analog of the K3-doublet's 1/6 factor on Petrie-polygon D_6 ⊂ H_3 sub-stabilizer (2–4 sessions estimated).

## Vignette 29 — Session 131 (Patch 0427): Q5 Layer 3 piece (a) closure — explicit W-bracelet cage-shell factor on $D_6$

Session opened with Q5 Layer 3 piece (a) (W-bracelet Schur-orthogonality cage-shell factor) as the Priority 1 default action from the Patch 0426 handover. The bootup-and-orient phase confirmed Reading C trajectory state through Patch 0426 and read the three source materials called out in the handover Quick-start §3: sketch §14 (Q5 Layer 2 closure with Substrate-Locality Unification), Capotauro paper §5.4 (K3-doublet cage-shell factor $d_E/V_{\text{cage}} = 2/12 = 1/6$ template), and SF-2 v1.0 §sec:Wbracelet_thm Theorem 4.2 + §sec:W_cage (W-bracelet structure and V-A coupling mechanism).

**The analytical decision point identified mid-session**: the handover §14.7(a) anticipated computing "$d_{\text{irrep}}/V_{\text{bracelet}}$ where $V_{\text{bracelet}} = 6$", which would give $2/6 = 1/3$. But the K3 paper §5.4 motivation Arguments 1+2 is structurally explicit about $d_\Gamma/|G|$ — group-order normalization — as the fundamental form. The "$d_E/V_{\text{cage}}$" form in K3 is valid because $V_{\text{cage}} = |\Dsix| = 12$ (the §5.4 "non-coincidence" subsection). For W-bracelet, the orbit-stabilizer relation $V_{\text{bracelet}} = |D_6|/|C_2| = 12/2 = 6 \ne |D_6|$ means the two forms diverge by factor 2. I presented both readings to Thomas with a recommendation for Reading 1 ($d_\Gamma/|G|$ Schur-fundamental) and Thomas authorized "best judgment" — Reading 1 selected and the §15 derivation written under it.

**The derivation**: the W-bracelet's 6-vertex permutation representation of $D_6$ decomposes as $A_1 \oplus B_1 \oplus E_1 \oplus E_2$ (permutation character $(6, 0, 0, 0, 2, 0)$ against the standard $D_6$ character table; Schur inner-product multiplicities $(1, 0, 1, 0, 1, 1)$). The V-A current's 120°/240° phase bias from SF-2 v1.0 PROP-SF-2-5 corresponds to the $E_2$ irrep at the $C_6$ eigenvalue level ($\chi^{E_2}(C_6) = -1$, eigenvalues $e^{\pm 2\pi i/3}$). Schur orthogonality on $D_6$ with $d_\Gamma = d_{E_2} = 2$ gives:
$$|M_\perp^W| = \frac{d_{E_2}}{|D_6|} = \frac{2}{12} = \frac{1}{6}$$

**Identical to the K3-doublet's cage-shell factor.** The composite chirality matrix element on the W-bracelet evaluates to $|M^{W,V\text{-}A}| = \chi/6 \equiv |M^{K3}|$ from Theorem THEO-CAP-1, with both sectors at $\phi^{-3}/6 \approx 0.0394$. The Substrate-Locality Unification theorem (Finding C-W40) is promoted from Layer 2 to Layer 3 with explicit numerical content.

**Finding C-W41 (NEW)** registered. Q5 Layer 3 piece (a) CLOSED; pieces (b) and (c) open. Layer 3 closure trajectory revised 4-10 → 3-9 sessions.

**§15.12 methodological observation**: cross-sector extension of a paper-internal formula can resolve ambiguities the original paper's scope didn't expose. The K3 paper §5.4 "non-coincidence" subsection observed $V_{\text{cage}} = |\Dsix|$ as a structurally significant identity but with no analytical consequence within the K3 paper's scope. Cross-sector extension to the W-bracelet (where $V_{\text{bracelet}} \ne |D_6|$) surfaces the underlying Schur-fundamental form and resolves the "non-coincidence" as a special-case identity rather than the formula's fundamental content. Registered for Capotauro v2.0+ §5.4 sharpening.

Patch 0427 sketch grows 997 → 1106 lines (+109 net).

---

*Maintainer: Dr. Thomas Lee Abshier ND, Hyperphysics Institute. Last updated: 17 May 2026 (Session 131 Patch 0427 — appended Vignette 29 covering Q5 Layer 3 piece (a) closure via Finding C-W41; Sessions 124–126 vignette backfill remains pre-existing gap, narrative at Patch 0421 handover commit `8acdb63`).*
