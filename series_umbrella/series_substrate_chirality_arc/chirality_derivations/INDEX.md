# Chirality Determination Arc — Patch Index

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/INDEX.md`
**Purpose:** A flat, chronological list of the chirality-determination arc's patches so the arc can be **followed in development order regardless of patch label**. Patch labels are *not* monotonic across this arc: the sequence ran 0635→0694, then jumped to **1100** (parallel-development Round 1, window W1), and now **continues in the 09xx block from 0902**. Git history is the source of truth for ordering; this index is the human-readable through-line. Labels at 1100 and in 08xx/09xx are intentional and not rewritten (cosmetic; see CONV-002 / lease-board notes).

**Maintenance:** append each new arc patch here (label · one line) when it lands. Topic-organized detail lives in `frontier_sectors/CHIR.md`; this file is purely the ordered table of contents.

## Sequence

| Patch | What |
|-------|------|
| 0635 | THEO-CHIR-AUDIT-1 cycle closed (3/3, v1.1) + PCD-ORIENTATION-1 scoped |
| 0636 | THEO-CHIR-PCD-ORIENTATION-1 registered — n̂→ω_PCD primitive-count theorem |
| 0637 | OPEN-CHIR-1d / E21 (χ=φ⁻³ magnitude) scoped — THEO-CHIR-CHI-1 reserved |
| 0638 | THEO-CHIR-CHI-1 registered — χ=φ⁻³ as locality-selected bias of two nearest shells (1d-α closed) |
| 0639 | OPEN-CHIR-1c/2d / E19 (capture handedness) scoped — THEO-CHIR-CAP-1 reserved |
| 0640 | THEO-CHIR-CAP-1 registered — capture handedness = involution × FI-C-9 sign (E19 emergent) |
| 0641 | chirality-derivations doc-suite consolidation (governance) |
| 0643 | OPEN-CHIR-MERGE scoped — the unified-chirality-sign question |
| 0644 | THEO-CHIR-MERGE-1 registered — OPEN-CHIR-MERGE partially resolved |
| 0647 | THEO-CHIR-MERGE-2 registered — MERGE-β advanced M3→M1-χ (chirality-count decoupled) |
| 0648 | MERGE-2 multi-AI review cycle opened |
| 0649 | MERGE-2 review integrated — v1.1, no falsifier |
| 0650 | MERGE-2 v1.1 ChatGPT re-review request |
| 0651 | MERGE-2 review cycle CLOSED 3/3 — v1.2 (M1-χ confirmed) |
| 0652 | OPEN-CHIR-1d-β scoped — the FI-C-9 emergence question (the primitive/emergent-status crux) |
| 0653 | THEO-CHIR-STATUS-1 registered — verdict structure {V1,V2,V3}; current rigor V3 |
| 0654 | THEO-CHIR-STATUS-2 registered — H₄→H₄⁺ breaking chain + axiom-level V2-exclusion → upgrade pinned to V1 |
| 0655 | STATUS-1 + STATUS-2 review cycle opened |
| 0656 | STATUS-1 + STATUS-2 review cycle CLOSED 3/3 — v1.1 |
| 0658 | THEO-CHIR-TARROW-1 — the T-arrow sign(δ) status (OPEN-CHIR-2a); W3, upgrade pinned to W1 |
| 0659 | TARROW-1 review cycle opened |
| 0661 | TARROW-1 review cycle CLOSED 3/3 — v1.1 |
| 0662 | CHIR↔electroweak bridge scoped — OPEN-CHIR-3 ∪ 1d-β-v; CONJ-CHIR-1 |
| 0663 | THEO-CHIR-BRIDGE-1 — B-i of the bridge (ℤ₂-match + P/T-face dictionary) |
| 0664 | BRIDGE-1 review cycle opened |
| 0665 | BRIDGE-1 review cycle CLOSED 3/3 — v1.1 |
| 0668 | B-iii capacity engine scoped — capacity ⇔ sign(μ²) of the ℤ₂-even Landau V(η) |
| 0669 | B-ii magnitude anchors scoped + χ φ⁻¹-vs-φ⁻³ reconciliation RESOLVED |
| 0671 | Session 151 close handover — bridge reachable faces mapped (B-i closed) |
| 0675 | doc-suite consolidation backfill (0643–0670) |
| 0679 | B-iii: scope a sign(μ²) route via Vafa–Witten reflection-positivity |
| 0680 | THEO-CHIR-VW-1 — V2-exclusion ⇔ Vafa–Witten no-go (the sign(μ²) route) |
| 0681 | VW-1 review cycle opened |
| 0682 | VW-1 review cycle CLOSED 3/3 — v1.1 (no verdict move) |
| 0683 | VW-a (H1) probe — reflection positivity sharpened to an OS criterion; H1 anchored |
| 0684 | SUSC opened — sign bit = mass channel = §14.17-gated; sign(μ²) route fully mapped |
| 0685 | THEO-CHIR-VW-2 — δ=0 reflection-positivity anchor + OS reduction of H1 to VW-a-4 |
| 0686 | VW-2 review cycle opened |
| 0687 | VW-2 review cycle CLOSED 3/3 — v1.1 (Q1-driven restatement) |
| 0688 | deep engine (1d-β-ii / §14.17) decomposed — first reachable gate = the O(δ²) curl |
| 0689 | O(δ³) Kolmogorov computation — detailed balance VIOLATED at third order (no verdict move) |
| 0690 | THEO-CHIR-TARROW-2 registered — a derived substrate T-asymmetry mechanism (candidate W3→W1) |
| 0691 | TARROW-2 review cycle opened |
| 0692 | TARROW-2 review cycle CLOSED 3/3 — v1.1; W3→W1 conditional on Mechanism A (first verdict-move candidate) |
| 0693 | Session 152 close handover — O(δ³) engine + TARROW-2 W3→W1-conditional |
| 0694 | Session 153 — construct + validate the Mechanism-A NESS stationary measure (Priority-1 setup) |
| **1100** | *[parallel Round 1, W1]* η-susceptibility symmetric-part form: χ_sym = N/m² (zero-mode dominated) ⇒ sign(μ²) = sign(m²); bottoms out at the (H-NESS) gap — no verdict move |
| **0902** | *[this file]* arc patch index created; **arc continues in the 09xx block from 0903** |
| **0903** | **DETERMINATION ARC CLOSED AT CURRENT RIGOR** — consolidation capstone (`chirality_determination_closure.md`): emergent to one primitive FI-C-9 + T-arrow; V3/W3; V2/W2 axiom-excluded; residual unified to OPEN-SM-4 by CPT. Deep V3→V1 (1d-β-ii, §14.17-gated) stays open. No new claim; count unchanged. |
| **0904** | chirality-lane review of DM-window Patch 0813 (`review/0904_…`): favorable-branch *conditional* input; framing correction (μ²>0 = unbroken = V3/primitive, not emergent); off-criticality assumed from product base = unclosed §14.17 gate. No verdict move. |
| **0905** | addendum to 0904: cross-lane resolution (DM lane retracted inverted label, 0815) + gate sharpening (0814 shows real NESS departs from product base → finite-χ must be recomputed on the real measure; reopens, does not flip). No verdict move. |
| **0906** | **DESCRIPTIVE** (`sign_nhat_primitive_and_axiom_entry.md`): what `sign(n̂)` is and where chirality enters — NOT an axiom; a Foundational Input (`n̂`=FI-C-RC-1, magnitude χ=φ⁻³=FI-C-9) actualized as the edge pattern `ε(ê·n̂)` on the achiral 600-cell, derivation open (OPEN-FI-C-9-FP-MECHANISM/1d-β-ii). No verdict, no count change. |
| **0907** | **GO/NO-GO + verdict spec** (`sketches/sec1417_chir_theorem_gonogo_and_verdict_spec.md`): "chirality as a theorem" is an openable bounded season; §14.17 gate reduced (VW-1→H1; 0818 reframe H1 = `sign(K_c−K_lift)`, K_c=1/12). Verdict criterion: K_lift<K_c ⇒ THEO-CHIR-CAPACITY-1 (primitive); K_lift>K_c ⇒ V1. Chirality-lane completeness residual = clear the O(δ³) current. DG-3 gate + lane division recorded. No verdict, no count change. |
| **0908** | assessment of K_lift (Patch 0819) (`review/0908_klift_assessment.md`): real reduction — verdict compressed to the **η-identity** (m; crossover m≈8). Registry m=12 edge → 0.64 → primitive (margin better than 0.64 since true K_c > mean-field 1/12), but the knife-edge is *which* effective η. Caution: "effective η = 0906 edge pattern" is an UNPROVEN cross-lane identification (must be derived, not assumed). O(δ³) current check (0907 §3) still open. Endorses the coarse-graining probe with two asks. No verdict move. |
| **0909** | assessment of coarse-graining probe (Patch 0820) (`review/0909_coarsegrain_assessment.md`): both 0908 asks substantially met — η-identity now **doubly-grounded** (0820 geometric canonicity + review-closed CHI-1 locality both select the 12-neighbour vertex figure); MC gives \|K_lift\|/K_c≈0.65→primitive; bias-shift cleared. Residuals (sharp, not walls): dynamical=geometric η (core), O(δ³) current-ordering (plausibly negligible, unproven), frustrated-AFM/true K_c. **Did NOT bottom out at PCD** → season looks closable toward THEO-CHIR-CAPACITY-1 without PCD. Well-grounded primitive **lean**, no verdict; DG-3 unmet. |
| **0910** | **DG-3 review scaffold** (`review/dg3_capacity_1_review_scaffold.md`): prepared (not live) swarm-review package for THEO-CHIR-CAPACITY-1 (V3 confirmed / V1 excluded). Precise claim + framing guard (μ²>0 ⇒ primitive, not emergent); three conditions C1 (dynamical=geometric η) / C2 (no current-induced ordering) / C3 (off-critical at correct AFM K_c), each slotted to an F.1 residual; Q1–Q5 review set; pass criteria + consequences (resolve OPEN-CHIR-1d-β as V1-excluded). **Fires only when C1–C3 close.** No verdict, no review run, no count change. |
| **0911** | assessment of residual closures 0821/0822 + DG-3 readiness (`review/0911_residual_closures_dg3_readiness.md`): **C1 discharged** (locality clean; no candidate mode orders, refutes 0819 crossover — caveat: worst-mode value swung 1.95→~0→0.50, Q1 must confirm) · **C2 discharged at physical bias** (current O(δ³), T-parity O(δ⁶)-suppressed; load-bearing arg is T-parity not div J=0) · **C3 NOT discharged** — all margins use the *ferromagnetic* K_c=1/12 but the coupling is *antiferromagnetic*; need the AFM-frustrated K_c (1/\|λ_min\|+frustration). **Ruling: HOLD DG-3 until residual 3 quantified.** Decisive residual closed without PCD; primitive looks set to pass. No verdict. |
| **0912** | **DG-3 SWARM PACKAGE — LIVE** (`review/dg3_capacity1_swarm_presentation.md`): all three conditions discharged (C3 closed by 0823 — true uniform K_c≈0.09–0.10, exact margin 42–47%, AFM suppresses uniform mode; the 0911 hold released). CONV-001 paste-block for ChatGPT/Grok/Copilot: CAPACITY-1 claim (V3 confirmed / V1 excluded; primitive, uniform-mode-scoped) + C1/C2/C3 evidence & caveats + Q1–Q5 + standing Mechanism-A conditionality. Pass = 3/3 confirm → enact (register CAPACITY-1, resolve OPEN-CHIR-1d-β V1-excluded). No verdict moved by this patch. |
| **0913** | folds the 0825 reconciliation into the 0912 package before firing: replaces "staggered orthogonal" (the soft spot — a staggered order *does* break the det-coset ℤ₂) with **"both channels cleared"** — |K_lift|≈0.053 below **both** the uniform (≈0.095) and staggered (≈0.27 = 1/\|λ_min\|, λ_min=−3.708) thresholds → η disordered in every mode → primitive, sign-independently. **Conservative headline ≈44%** (uniform, worst-case sign) + favorable ≈80% (staggered, AFM). C3/scope/Q3 updated; preempts the package's own Q3. **Verdict unchanged (primitive, robust); package now ready to fire.** No verdict moved. |
| **0914** | **DG-3 review results — RESTATE, NOT a pass; CAPACITY-1 NOT enacted** (`review/0914_dg3_review_results_RESTATE.md`). Final tally (Grok added 0915): **1 CONFIRM (Grok) / 2 RESTATE (ChatGPT, Copilot)**. **Convergent falsifier (Q1):** C1's mode-scan is a *sample* — "η disordered in every mode" overreaches without a closure that all admissible η lie in the tested local class; Grok's lone CONFIRM asserts this rather than proving it, so it does not discharge the falsifier. **Path A** (recommended): eigenmode-completeness + locality-bounded λ_max≤12 ⇒ \|K_lift\|·λ_max<1 clears all modes (the ≈44% margin *is* the exhaustive bound); F.1 to formalize. **Path B:** narrow to "V1 excluded within the local-η regime at the physical bias." Fixable: Q3 (link 0824/0825, annotate 0823's superseded "not V1"), Q4 (both modes), Q2 ("physical bias" scope limit). Q5 confirmed by all; framing guard drew no inversion flag. **No verdict moved**; V3/W3 stand; OPEN-CHIR-1d-β OPEN. |
| **0915** | records Grok's DG-3 review into 0914 (CONFIRM all five; "passes") and adjudicates it: a 1-CONFIRM/2-RESTATE split is **not a pass**; Grok's CONFIRM rests on the nn-only correlator showing the *tested* η is local but does **not** engage the sample-vs-complete gap the two RESTATEs raise, so it asserts rather than discharges the Q1 falsifier. Disposition **unchanged** — CAPACITY-1 NOT enacted; Path A/B + Q2/Q3/Q4 fixes then re-fire. Notes that Path A (λ_max≤12 eigenmode closure) is the rigorous form of Grok's intuition. No verdict moved. |
| **0916** | **Path A closure spec** (`review/0916_pathA_capacity1_closure_spec.md`): converts C1 from a *sampled* mode-scan into an *exhaustive* bound to discharge Q1, on two axes — (1) **eigenmode completeness**: real-symmetric M_eff has a complete eigenbasis, so `\|K_lift\|·a_max < 1` clears every mode (a_max = spectral radius = \|K_lift\|/K_c = 0.64<1); (2) **worst-case observable**: Gershgorin row-sum ⇒ the m=12 vertex figure (most engaged neighbours) maximizes a_max, so more-local η is *strictly* more sub-critical (explains 0821's m=4<m=12; overturns 0819). Hands the F.1 window **L-CAP-A** (diagonalize full M_eff, confirm a_max<1/\|K_lift\|≈18.9 incl. 2nd shell; confirm m=12 worst-case). On confirm → reframe C1 + Q2/Q3/Q4 fixes + re-fire. **No verdict moved**; conditional on Mechanism A. |
| **0917** | **Path A spec-review results + refined L-CAP-A** (`review/0917_pathA_specreview_refined_LCAPA.md`). Axis 1 **confirmed** (both reviewers: eigenmode completeness exhausts "which mode" for a fixed observable). Axis 2 **RESTATE — ChatGPT's falsifier valid**: Gershgorin gives only an *upper* bound, so "m=12 max row-sum (12) ⇒ m=12 worst-case" fails — actual a_max(M(12))=0.64≠12, a more-local observable could exceed 0.64 (Review-1's CONFIRM repeated the conflation). **Refined:** add unit-variance normalization (\|M_ij\|≤1); replace the Gershgorin step with **L-CAP-A(ii)′** = an *observable-monotonicity theorem* (M(m′) a sub-weighting of M(12), no sign-coherence enhancement ⇒ ρ(M(m′))≤ρ(M(12))) to be **proven**. **Deeper read:** Axis 2 *is* the η-identity (3rd surfacing) — proving it either closes Path A or localizes the irreducible residual to the PCD-layer node (then Path B). Q3 fix validated (0824 link). **No verdict moved.** |
| **0918** | **L-CAP-A computation assessment** (`review/0918_LCAPA_computation_assessment.md`). The F.1 computation (their Patch 1200): **Axis 1 ESTABLISHED** (full M_eff diagonalization, a_max≈0.644<1 incl. d=2 shell; vertex-transitive ⇒ Gershgorin tight for the fixed m=12 operator). **Axis 2 NOT established** — F.1 re-ran the *original 0916 Gershgorin* argument (cited 0916/0821/0824/0823 but **not 0917**, so missed the refinement); that step was refuted by ChatGPT and orders operators by row-sum upper bounds, which is invalid. **Sharpened route:** Axis 2 closes iff `\|C(m′)\|≤0.053` entrywise ∀ admissible m′ ⇒ ρ(M(m′))≤ρ(\|M(12)\|)≈0.644<1 by **Perron–Frobenius** (not Gershgorin); this one structural fact **is the η-identity**. **Path A NOT closed; no re-fire.** Re-hand to F.1 with 0917+0918. No verdict moved. |

## Continuity note

The label jump `0694 → 1100 → 0902 → 0903…` is intentional. 1100 was produced under the parallel-development system (Round 1); the arc subsequently moved to the 09xx block per the per-arc numbering discussion. Labels are not rewritten (rewriting shared history for a cosmetic label is not worth the breakage). Follow the arc by this index, not by sorting labels.

**Current arc state (from CHIR.md):** spatial verdict **V3** (FI-C-9 the one irreducible primitive; V2 excluded at axiom level; upgrade pinned to V1) · temporal verdict **W3** (upgrade pinned to W1) · the V3→V1 engine (1d-β-ii) is gated on the F.1 §14.17 effective action (where the 1100 NESS/μ² route bottoms out).
