# Problem History: OPEN-SM-4 — Capotauro mechanism for chirality and parity violation

**Created:** 16 May 2026 (registered at Capotauro v1.0 SHIP retroactive doc-suite catch-up, Session 123 Patch 0416A; problem itself active since March 2026)
**Status:** OPEN (PARTIAL CLOSURE) — sub-claim (c) CLOSED at v1.0 SHIP Session 122 Patch 0415 via THEO-CAP-1; sub-claims (a) + (b) OPEN
**Research_Frontier.md entry:** OPEN-SM-4
**Target paper:** Capotauro v1.0 SHIPPED (sub-claim (c)); Capotauro v2.0+ (sub-claim (b) closure trigger via Reading C Q1+); future paper (sub-claim (a) Capotauro nucleation event downstream of sub-claim (b))
**Parent paper:** Capotauro v1.0 SHIPPED 16 May 2026 (Session 122 close, Patch 0415) at `flagship_papers/capotauro/capotauro.tex`

---

## The Problem

Derive from CPP substrate primitives the chiral asymmetry of the universe — the empirically observed parity violation in weak-interaction processes, the right-hand-rule structure of the ExB law at all charge-magnitude / DP-density / velocity scales, the V-A coupling structure of W± gauge bosons, and the matter-antimatter asymmetry ratio $\eta_B = (6.12 \pm 0.04) \times 10^{-10}$ from cosmological leptogenesis. The substrate-level chirality must be reconciled with the 600-cell's intrinsic geometric symmetry (the polytope has full $H_4$ symmetry of order 14400, with equally many left-handed and right-handed enantiomorphs at every vertex and at every scale).

### Three sub-claims

The Capotauro mechanism decomposes the problem into three sub-claims, registered with the following status at Session 123:

**Sub-claim (a)** — Capotauro nucleation event derivation. The universe-wide sign-selection event determining which of the two equivalent enantiomorphs of the substrate vacuum is realized in our universe. Distinct from the magnitude mechanism (sub-claim b); the magnitude can be derived independently of the sign-selection. Cosmological framing from Abshier & Grok December 2025 Capotauro nucleation paper (lattice nucleation at $z \simeq 32$). **OPEN.**

**Sub-claim (b)** — substrate chirality mechanism candidate derivation. The first-principles derivation of the substrate's primitive chirality magnitude $\|\chi\| = \phi^{-3}$ from more primitive CPP axioms, rather than postulating $\phi^{-3}$ as a foundational input. Tracked separately at `Research_Frontier.md` OPEN-FI-C-9-FP-MECHANISM with Reading C geometric-chirality candidate registered Session 121 Patch 0414 at working sketch `flagship_papers/capotauro/sketches/Capotauro_chiral_mechanism_candidate.md`. **OPEN.**

**Sub-claim (c)** — substrate-to-K3-doublet matrix element derivation $\|M\| = \chi/6$ on the TBM-aligned K3-doublet of charged-lepton substrate states. Given the substrate chirality magnitude $\|\chi\|$ as foundational input (FI-C-9), derive the chirality matrix element on the K3-doublet at theorem level. **CLOSED at v1.0 SHIP Session 122 Patch 0415 via THEO-CAP-1 Composite Capotauro Wigner-Eckart Theorem.**

### Closure route at v1.0 SHIP (sub-claim (c))

The Capotauro paper v1.0 closes sub-claim (c) at conditional theorem level via THEO-CAP-1: $\|M\| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ on the TBM-aligned K3-doublet, gathering eight ingredients across Sessions 88–97 of the closure trajectory: (i) the anti-diagonal Theorem 8.1 parity-structure result via the $D_6$-stabilizer + extended FI-C-3 perpendicular wavefunctions + ζ-parity assignment; (ii) the unique $A_2$ generator $T_{A_2}(b) = i \cdot b \cdot S$ of σ_1-ODD Hermitian operators on K3-amplitudes (Patch 0389 Session 95 correction to the earlier (a,b)-parameterization); (iii) the chirality-eigenvalue matching principle giving $b = \chi/\sqrt{3}$ and $\|M_{K3}\| = \chi$ (Patch 0390 Session 96); (iv) the cage-shell averaging principle giving $\|M_\perp\| = d_E/V_\text{cage} = 2/12 = 1/6$ via FI-C-10 + Schur orthogonality on the icosahedral cage (Patch 0391 Session 97); (v) composite product $\|M\| = \|M_{K3}\| \cdot \|M_\perp\| = \chi/6$ at theorem level (Patch 0392 Session 98); (vi) substrate-vacuum substitution $\chi = \phi^{-3}$ from FI-C-9 yields $\|M\| = \phi^{-3}/6 \approx 0.0394$. Primary empirical prediction $\Delta p_{LR} \approx 0.0394$ validated within 2% of empirical anchor $\sim 0.04$ from leptogenesis back-derivation.

---

## The Journey

### Pre-v0.1 (Sessions 1-85)

The OPEN-SM-4 entry was registered in `Research_Frontier.md` on 23 March 2026 as a conceptual placeholder: "Derive the lattice chirality-activation event that establishes $\chi \approx \phi^{-1}$ and produces CP violation." The original conjectured magnitude $\chi \approx \phi^{-1}$ from earlier substrate-physics intuition was carried through Sessions 1-85 without rigorous derivation. The Abshier & Grok December 2025 Capotauro nucleation paper supplied the cosmological framing ($z \simeq 32$ lattice nucleation epoch) and the etymology (*capo* + *tauro* = "head bull event"). Grok also coined the empirical chirality bias target $\Delta p_{LR} \approx 0.04$ back-derived from $\eta_B$ via leptogenesis.

### Session 86 (Patches 0376–0381): closure trajectory opening

Patch 0376 Session 84 opened the closure-trajectory sketch at `flagship_papers/capotauro/sketches/Capotauro_chi_phi_closure.md` (parent sketch covering all three sub-claims with sub-claim (c) as the v1.0 closure target). Sessions 85–87 surfaced four substantive findings: (C-1, C-2) the original $\chi \approx \phi^{-1}$ value did not match the 600-cell geometric structure; (C-3 Patch 0378) the OP-SM-4 archive's $\chi = \phi^{-2}$ derivation contained a one-step arithmetic error (lost factor $1/\phi$); corrected value $\chi = \phi^{-3} \approx 0.236$ derived from the edge-to-first-non-edge-distance ratio in the 600-cell; (C-7 Patch 0379) integration of Grok's $\Delta p_{LR} \approx 0.04$ target gave substrate-to-observable transmission factor $T = V/2 = 6$ at the numerical-signpost level; (C-8 Patch 0381) Picture A foundational + Picture B transmission + Picture C group-theoretic skeleton decomposition adopted as load-bearing role assignment.

### Sessions 88–97 (Patches 0382–0391): sub-claim (c) closure trajectory

Session 88 Patch 0382 closed sub-sub-claim (c.1a) at theorem level: the K3-doublet matrix of $\hat{C}_\chi$ is rigorously anti-diagonal in the TBM-aligned basis under FI-C-3 + the broken-symmetry vacuum input (Theorem 8.1, five-step proof). Session 89 Patch 0383 discharged the σ-orientation-reversing verification flag at full numerical rigor and surfaced the corrigendum that the K3 stabilizer structure is $D_6 = S_3 \times Z_2$ with the cell-swap $\zeta$ having $\det = -1$ (not $+1$ as earlier hypothesized), and the chirality-preserving subgroup is $S_3' = \langle r, \sigma_1 \zeta \rangle$ (not $C_6$ as the §3.1 informal framing had). Session 90 Patch 0384 attempted the (c.4.G2) closure via $D_6$ character theory and surfaced a structural obstruction: under uniform ζ-parity in the K3-doublet basis, all matrix elements forced to zero by the combined σ_1 + σ_1ζ selection rules. Resolution at Session 91 Patch 0385: FI-C-3 extension with explicit opposite-ζ-parity assignment for the two K3-doublet basis states (one ζ-EVEN, one ζ-ODD), formalized via Findings C-W11/12/13. Sessions 92–93 Patches 0386–0387 set up the Wigner-Eckart framework and revealed the linear-vs-quadratic scaling structure: standard QFT-perturbation gives $\sin^2\theta_{13} \propto \|M\|^2$ off by factor 21, while the candidate γ structural observation $\sin^2\theta_{13} = b \cdot m_\perp = \chi/(6\sqrt{3}) \approx 0.0227$ matches NuFIT 6.0 empirical $0.0222 \pm 0.00069$ within 1σ but requires CPP-specific linear-scaling framework. Session 95 Patch 0389 substantively corrected the Session 93 parameterization: the σ_1-ODD operator on K3-amplitudes used a general (a,b) parameterization mixing $E$ + $A_2$ irrep content, but $\hat{C}_\chi$ in $B_2$ of $D_6$ requires the unique $A_2$ generator $T_{A_2}(b) = i \cdot b \cdot S$ specifically — corrected $M_{K3} = -i \cdot b \cdot \sqrt{3}$ with the $\sqrt{3}$ in the numerator. Sessions 96 + 97 Patches 0390 + 0391 closed the two derivation principles at theorem level: chirality-eigenvalue matching giving $b = \chi/\sqrt{3}$ (so $\|M_{K3}\| = \chi$); and cage-shell averaging giving $\|M_\perp\| = d_E/V_\text{cage} = 2/12 = 1/6$ via FI-C-10 + Schur orthogonality with $V_\text{cage} = \|D_6\| = 12$.

### Sessions 98–101 (Patches 0392–0395): theorem formalization + sin²θ_13 re-scoping

Session 98 Patch 0392 formalized the Composite Capotauro Wigner-Eckart Theorem (THEO-CAP-1) with eight-step proof + end-to-end numerical verification at machine precision ($10^{-17}$). Sessions 99–101 attempted to extend the framework from $\Delta p_{LR}$ to $\sin^2\theta_{13}$ via PMNS perturbation machinery: 22 candidate scalings tested, only candidate γ ($\sin^2\theta_{13} = b \cdot m_\perp$) matches observation within 1σ but requires linear scaling that standard QFT-perturbation cannot reproduce; wavefunction-level coupling hypothesis also gives quadratic scaling (off by factor 64); Q11 sin²θ_13 derivation re-scoped to SF-2 v2.0+ at Session 101 Patch 0395.

### Sessions 102–103 (Patches 0396–0397): sub-claim (c) v1.0 closure declaration + theorem registration

Session 102 Patch 0396 declared sub-claim (c) v1.0 closure with packaged Sessions 88–101 trajectory summary; Session 103 Patch 0397 registered THEO-CAP-1 in `theorem-registry.md` as theorem #62 in the SF-Line section — the first programme-level theorem registered ahead of its own flagship paper publication in the CPP corpus. Methodological pattern established: theorem-registry registration from flagship-paper-pending working sketch is appropriate when four conditions are met (rigorous proof; end-to-end numerical verification; primary empirical prediction validated; honest scope-limitation framing for re-scoped sub-problems).

### Sessions 104–122 (Patches 0398–0415): paper production + v1.0 SHIP

Sessions 104–122 produced the v1.0 paper via the standard v0.1 → v1.0 trajectory: outline (104), v0.1 foundation (105), v0.2 § substrate-vacuum + K3-doublet (107), v0.3 § Wigner-Eckart + theorem (108-109), v0.4 § predictions + falsifier (110), v0.5 § open work + discussion + FI summary (111), v0.6 polish + first PDF compile (112), v0.7 Group A substantive physics + Group B writing/style + title-block cleanup + changelog architecture standardization (113-115), v0.8 expositional polish (118), v0.9 polish + **foundational framing reframe from SSB to primitive-feature framing** (120, the methodologically critical Session 120 reframe per CPP core principle that mathematical descriptions are not physical mechanisms — replaces the v0.x "spontaneous symmetry breaking" language with primitive-substrate-feature framing while preserving SSB as mathematical-equivalence alternative in Remark 2.2), Reading C mechanism candidate sketch (121), and v1.0 SHIP via title-block bump only (122). Cross-reviewer convergence on SHIP-readiness achieved at v0.8 Session 119 Patch 0412 (ChatGPT round-3 + CoPilot round-1 + Grok round-1 SHIP-ready verdicts).

---

## Outcome at v1.0 SHIP (Session 122 Patch 0415)

**Sub-claim (c) CLOSED** at conditional theorem level via THEO-CAP-1 (Composite Capotauro Wigner-Eckart Theorem); primary empirical prediction $\Delta p_{LR} \approx 0.0394$ validated within 2% of empirical anchor $\sim 0.04$ from leptogenesis back-derivation; the Capotauro paper is the third flagship paper to ship at v1.0 in the CPP corpus (after SS-9, SF-4, SF-2) and the first flagship outside the SF-N numerical convention. **Sub-claims (a) and (b) remain OPEN.** OPEN-SM-4 advances OPEN → OPEN (PARTIAL CLOSURE) but NOT OPEN → CLOSED.

Programme-level changes at v1.0 SHIP: (1) `Research_Frontier.md` OPEN-SM-4 status updated to PARTIAL CLOSURE; (2) `Research_Frontier.md` NEW OPEN-FI-C-9-FP-MECHANISM entry registered (Reading C geometric-chirality candidate as Layer 3 closure trajectory); (3) `theorem-registry.md` THEO-CAP-1 paper-level confirmation; (4) `paper_catalog.md` SF-Line Capotauro row + Documentation paragraph; (5) `INDEX.md` flagship_papers entries; (6) `flagship_papers/capotauro/README.md` paper-level README created.

Documentation drift fix at Session 123 Patch 0416A (this PH file's creation): three drift items surfaced by §15 Step E per-registry audit at Patch 0416 retroactive handover construction — (a) `predictions.md` PRED-O-25 Capotauro $\Delta p_{LR}$ entry; (b) `master_glossary.md` Capotauro v1.0 substrate-vacuum chirality framework terms section (12 entries); (c) this `problem_histories/PH-OPEN-SM-4.md` file. All three drift items fixed in Patch 0416A before downstream Section A doc-suite production reads from the registries.

---

## Open work post-v1.0 SHIP (sub-claims (a) + (b) + Reading C closure trajectory)

**Sub-claim (b) Reading C closure trajectory** (Tier-4 Layer 1 / Layer 2 working sketch at `flagship_papers/capotauro/sketches/Capotauro_chiral_mechanism_candidate.md`; Layer 3 closure trajectory estimated 10–20 sessions): a primitive 4D direction $\hat{n}$ in the substrate's ambient 4D space produces direction-correlated edge-length variation in the 600-cell lattice at the $\phi^{-3}$ scale; the $H_4 \to I_4$ algebraic structure is the structural consequence of $\hat{n}$ being primitive rather than the outcome of a dynamical event; the chirality magnitude $\|\chi\| = \phi^{-3}$ is derived rather than postulated, via the perturbative-distance-ratio constraint applied to the $\hat{n}$-perturbation. Five Layer 3 closure-trajectory questions registered: **Q1** group-theoretic verification of $H_4$ stabilizer of $\hat{n} \cong I_4$ (estimated 1–3 sessions; the first sub-step; closure of Q1 triggers Capotauro v2.0+ at minimum); **Q3/Q4** perturbative-distance-ratio sharpening (3–5 sessions); **Q5/Q6** cross-sector consistency with SF-2 W bracelet $D_6$ and SM-2 qDP/eDP asymmetry (5–10 sessions); sub-claim (a) cosmological-timing interaction. Reading C predicts new structural prediction: fractional chirality retention across observable classes (mass observables retain $O(\chi^2) \approx 0.6\%$; chirality observables retain full $\chi/6 \approx 4\%$; intermediate observables retain calculable fractions).

**Sub-claim (a) Capotauro nucleation event derivation**: deferred until sub-claim (b) magnitude closure trajectory makes substantial progress. The two are structurally coupled — the nucleation event sign-selection presupposes a substrate-vacuum dynamics framework that sub-claim (b) Reading C is the candidate venue to develop. Sub-claim (a) closure paper venue TBD post-Capotauro v2.0+.

**FI-C-10 first-principles derivation**: tracked as separate open work entry; the observable-class-independence claim distinguishing FI-C-10 from FI-C-6 (cage-shell mass formula precedent at theorem level in SF-4 v4.0 THEO-SF-4-5) is physically motivated by three plausibility arguments in §5.4 of the Capotauro paper but not formally derived from CPP axioms A1–A11.

**Q11 sin²θ_13 derivation** re-scoped to SF-2 v2.0+ at Session 101 Patch 0395; the linear-vs-quadratic scaling tension requires CPP-specific perturbation framework that sub-claim (b) substrate-vacuum dynamics may surface. Candidate γ $\sin^2\theta_{13} = b \cdot m_\perp \approx 0.0227$ matches observation within 1σ but lacks rigorous derivation.

---

*Maintainer: Thomas Lee Abshier ND, Hyperphysics Institute. Last updated: 16 May 2026 (Session 123 Patch 0416A creation).*
