# Capotauro — Flagship Paper Folder

**Status: v1.0 SHIPPED (Session 122 close, 16 May 2026, Patch 0415)**

This folder contains the *Capotauro* flagship paper of the CPP corpus, closing OPEN-SM-4 sub-claim (c) — the chirality matrix element $|M| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ on the tribimaximal-aligned $K_3$-doublet of charged-lepton substrate states — at conditional theorem closure level under ten foundational inputs (FI-C-1 through FI-C-10) plus four CPP axioms (A1, A3, A4, A7; A3 substrate orientation field and A7 substrate-stress framework most load-bearing per the Picture B substrate-orientation-field framework). The primary empirical prediction $\Delta p_{LR} = |M| \approx 0.0394$ is validated within 2% of the empirical anchor $\sim 0.04$ inferred from the cosmological baryon asymmetry $\eta_B = (6.12 \pm 0.04) \times 10^{-10}$ via the standard leptogenesis back-derivation.

The paper is the third flagship paper to ship at v1.0 in the CPP corpus (after SS-9 Session 32, SF-4 Session 54, SF-2 Session 83), and the first flagship paper outside the SF-N numerical convention — the THEO-CAP-N naming convention for the Capotauro theorem chain reflects its flagship-paper-pending status preserved through v1.0 SHIP, recording that the paper's primary programme-level theorem (**THEO-CAP-1**, Composite Capotauro Wigner-Eckart Theorem) was registered as theorem #62 in the SF-Line section of `theorem-registry.md` at Session 103 Patch 0397, ahead of its own flagship-paper publication. This is the first programme-level theorem registered ahead of its own flagship paper in the CPP corpus and establishes the methodological pattern for theorem-registry registration from closure-trajectory sub-sketches when four conditions are met: (i) eight-step rigorous proof, (ii) end-to-end numerical verification to machine precision, (iii) primary empirical prediction validated against observation, (iv) honest scope-limitation framing for re-scoped sub-problems.

## Contents

| Path | Description |
|------|-------------|
| `capotauro.tex` | Main paper source, v1.0 SHIPPED (Session 122 Patch 0415); 1149 lines; 46 pages compiled at v0.9 (601 KB PDF at v0.9; v1.0 SHIP is version-bump-only with no content change so PDF page count and KB size are preserved relative to v0.9). 6 theorem-family environments: Theorem 5.1 Composite Capotauro Wigner-Eckart Theorem (the central result) + Definition 2.1 substrate primitive chirality magnitude + Remark 2.2 primitive-feature framing vs SSB mathematical equivalence + Lemmas 4.2/5.2/5.3 (D₆-irrep selection rule, K3-amplitude factor $|M_{K_3}| = \chi$ from cross-product structure of unique A₂ generator, cage-shell averaging factor $|M_\perp| = 1/6$ from Schur orthogonality with $V_\text{cage} = |D_6| = 12$ via $d_E/V_\text{cage} = 2/12$). |
| `sketches/` | Working development documents from the closure trajectory and beyond. See `documentation_suite/changelog-capotauro.md` for the version archaeology of each. Currently 4 documents: `capotauro_outline.md` (327 lines, Session 104 Patch 0398, original paper outline); `Capotauro_chi_phi_closure.md` (681 lines, parent sketch covering FI-C-9 + FI-C-10 closure trajectory Sessions 87-102); `Capotauro_subclaim_c_wigner_eckart.md` (2146 lines, sub-claim (c) detailed eight-step closure with Theorem 18.1 + §22 v1.0 closure narrative); `Capotauro_chiral_mechanism_candidate.md` (296 lines, Session 121 Patch 0414, Reading C geometric-chirality candidate for sub-claim (b) "substrate chirality mechanism candidate derivation" — primitive 4D direction $\hat{n}$ producing direction-correlated edge-length variation at $\phi^{-3}$ scale; Tier-4 Layer 1/Layer 2 epistemic status; Layer 3 closure trajectory tracked at `OPEN-FI-C-9-FP-MECHANISM` in `Research_Frontier.md`). |
| `documentation_suite/` | Documentation suite for the paper. Currently `changelog-capotauro.md` only (Patch 0415 updated with v1.0 SHIP version section + Patch 0415 register row + Last-updated footer Session 122). Remaining four-tier files (`handover-capotauro.md`, `development-capotauro.md`, `transcript-capotauro.md`, `reasoning-capotauro.md`) + 7 standalone companion files (`mechanism-capotauro.md`, `glossary-capotauro.md`, `phenomena-capotauro.md`, `philosophy-capotauro.md`, `development-capotauro.md`, `reviews-capotauro.md`, `keywords-capotauro.md`) planned in Patches 0416+ across Sessions 123+ per `templates/paper_completion_checklist.md`. |
| `reviews/` | Review archive. 5 review files at v1.0 SHIP: ChatGPT round-1/round-2/round-3 (`chatgpt_v0.6_session_113.md`, `chatgpt_v0.7_session_117.md`, `chatgpt_v0.8_session_119.md`) + CoPilot round-1 (`copilot_v0.8_session_119.md`) + Grok round-1 (`grok_v0.8_session_119.md`). Cross-reviewer convergence on SHIP-readiness achieved at v0.8 Session 119 Patch 0412 with all three reviewers reaching SHIP-ready verdicts. |

## Conditional theorem closure structure

The paper is a **conditional theorem closure paper** per the conditional-closure framework established by SF-4 v4.x and SF-2 v1.0 (`templates/conditional_closure_framework.md`). The discipline distinguishes theorem-level claims that hold rigorously under explicit foundational-input assumptions from claims at structural-argument or empirical-anchor level. The Capotauro paper's substantive content sits in the rigorous-derivation category once the ten foundational inputs FI-C-1 through FI-C-10 are accepted; first-principles closure of the foundational inputs themselves is registered as open work and deferred to v2.0+.

The four foundational inputs whose first-principles closure is the deepest open work (in priority order):

- **FI-C-9 substrate primitive chirality magnitude $|\chi| = \phi^{-3}$** — tracked at `Research_Frontier.md` as `OPEN-FI-C-9-FP-MECHANISM` (NEW at Patch 0415); Reading C geometric-chirality candidate (primitive 4D direction $\hat{n}$ producing direction-correlated edge-length variation at $\phi^{-3}$ scale) registered at Patch 0414 with working sketch `sketches/Capotauro_chiral_mechanism_candidate.md`; Tier-4 Layer 1/Layer 2 epistemic status; Layer 3 closure trajectory estimated 10–20 sessions to completion; Layer 3 closure of Q1 (group-theoretic verification of the $H_4$ stabilizer of $\hat{n} \cong I_4$ claim) is the first sub-step and triggers Capotauro v2.0+ at minimum.

- **FI-C-10 cage-shell extension to chirality observables** — registered at Session 97 Patch 0391 as a new foundational input. The observable-class-independence claim distinguishing FI-C-10 from FI-C-6 (the established mass-observable cage-shell mechanism inherited from SF-4 v3.0) is physically motivated but not formally derived from CPP axioms A1–A11. Three plausibility arguments are presented in §5.4 of the paper (FI-C-6 precedent, Schur orthogonality, observable-class structural similarity). First-principles closure registered as separate open work entry.

- **FI-C-3 K3 antibonding-doublet structure + TBM-aligned basis at theorem level** — inherited from SF-4 v4.0 Composite K3-Cage-Shell Coupling Theorem (THEO-SF-4-5); the perpendicular wavefunction structure $|\chi_\pm\rangle$ as $\zeta$-parity-decomposed substrate orientation field is extended in Session 91 of the Capotauro closure trajectory.

- **FI-C-4, FI-C-5 cage geometries** — inherited from SF-2 v1.0 (W bracelet $D_6$ stabilizer; Z icosahedral + H dodecahedral cages).

The remaining FIs (FI-C-1 600-cell chiral structure; FI-C-2 K3 base + four-cage taxonomy from SM-1; FI-C-6 cage-shell mass formula; FI-C-7 DP species taxonomy from SM-2; FI-C-8 empirical SM phase data) inherit from the broader SM corpus.

## Programme-level state at v1.0 SHIP

- **THEO-CAP-1 status: confirmed at paper-level v1.0 SHIP** (registered Session 103 Patch 0397; paper-level confirmation Session 122 Patch 0415).
- **OPEN-SM-4 status: OPEN (PARTIAL CLOSURE)** — sub-claim (c) v1.0 SHIPPED via Capotauro paper v1.0; sub-claim (a) Capotauro nucleation event remains open; sub-claim (b) substrate chirality mechanism candidate derivation tracked at new `OPEN-FI-C-9-FP-MECHANISM` entry.
- **Primary empirical prediction $\Delta p_{LR} \approx 0.0394$** validated within 2% of leptogenesis back-derived empirical anchor $\sim 0.04$.
- **Q11 sin²θ_13 derivation re-scoped to SF-2 v2.0+** (Session 101 Patch 0395; linear-vs-quadratic scaling tension surfaced Session 100; wavefunction-level coupling hypothesis ruled out Session 101; candidate γ structural observation $\sin^2\theta_{13} = b \cdot m_\perp \approx 0.0227$ matches observation within 1σ but lacks rigorous derivation).
- **34 findings registered (C-W1 through C-W34)** across the 16-session closure trajectory Sessions 87–102.

## Forward queue post-Session 122 close

- **Patches 0416+** documentation suite production for the Capotauro paper across estimated 7–15 sessions per `templates/paper_completion_checklist.md` Section A (7 companion documentation files: mechanism, glossary, phenomena, philosophy, development, reviews, keywords) + Section B verification notebooks + Section C registry updates beyond v1.0 SHIP baseline + Section D navigation updates beyond v1.0 SHIP baseline + Section E development transcripts (`handover-capotauro.md`, `development-capotauro.md`, `transcript-capotauro.md`, `reasoning-capotauro.md`) + Section F OSF registration (DOI `10.17605/OSF.IO/JXE8D`) + Section G repository commit + Section H final verification. Documentation suite is ACTIVE post-v1.0; only the `.tex` source freezes per Lesson 6 from SF-4 v1.0 SHIP Session 54 handover.

- **Sub-claim (b) Reading C closure trajectory** Q1 group-theoretic verification of the $H_4$ stabilizer of $\hat{n} \cong I_4$ claim — first sub-step toward Layer 3 closure, estimated 1–3 sessions; subsequent Q3/Q4 perturbative-distance-ratio sharpening (3–5 sessions); Q5/Q6 cross-sector consistency checks with SF-2 W bracelet and SM-2 qDP/eDP (5–10 sessions); Layer 3 closure trajectory total estimate 10–20 sessions; Capotauro v2.0+ trigger is closure of Q1 at minimum.

- **Anthology chapter** at the Rovelli/SciAm register parallel to the SS-7 / SS-8 / SS-9 / SF-4 chapters in `book_project/chapters/` (~5000–6000 words).

- **TATWD integration** to `CPP_the_theory.md` at v1.0 SHIP — Capotauro mechanism integrated into the master theory narrative with OPEN-SM-4 sub-claim (c) closed and OPEN-FI-C-9-FP-MECHANISM as sub-claim (b) closure-trajectory pointer.

- **SF-4 v4.5+ Capotauro integration** per Grok Session 119 suggested next steps (paste Theorem 5.1 + $\Delta p_{LR} = \chi/6$ into the SF-4 Capotauro section; update SF-4 predictions table for the $\delta_{CP}$ substrate-level handle; open `SF-4_deltaCP_capotauro_integration.md` sketch).

- **Public posting** of v1.0 SHIPPED PDF (Zenodo + arXiv) at Thomas's discretion via the Binary Artifact Workflow established at SF-4 Patch 0339.

## Cross-references

- Programme-level theorem: `theorem-registry.md` THEO-CAP-1 (theorem #62 in SF-Line section).
- Open-problem registry: `Research_Frontier.md` OPEN-SM-4 (PARTIAL CLOSURE) + new OPEN-FI-C-9-FP-MECHANISM in FP section.
- Paper catalog: `paper_catalog.md` SF-Line Flagship Papers section (Capotauro row).
- Version archaeology: `documentation_suite/changelog-capotauro.md`.
- Closure trajectory Tier-4 reasoning: working sketches in `sketches/` (`Capotauro_chi_phi_closure.md` parent; `Capotauro_subclaim_c_wigner_eckart.md` sub-claim (c) detailed; `Capotauro_chiral_mechanism_candidate.md` sub-claim (b) candidate).
- Cross-reviewer convergence at v0.8: `reviews/` (ChatGPT round-3 + CoPilot round-1 + Grok round-1).

---

**Status footer**: v1.0 SHIPPED Session 122 close, 16 May 2026, Patch 0415. Documentation suite ACTIVE post-v1.0; `.tex` source frozen at v1.0 unless external feedback or programme advance triggers v1.x or v2.0+ revision.
