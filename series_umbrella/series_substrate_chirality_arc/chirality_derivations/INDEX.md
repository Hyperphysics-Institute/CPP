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

## Continuity note

The label jump `0694 → 1100 → 0902 → 0903…` is intentional. 1100 was produced under the parallel-development system (Round 1); the arc subsequently moved to the 09xx block per the per-arc numbering discussion. Labels are not rewritten (rewriting shared history for a cosmetic label is not worth the breakage). Follow the arc by this index, not by sorting labels.

**Current arc state (from CHIR.md):** spatial verdict **V3** (FI-C-9 the one irreducible primitive; V2 excluded at axiom level; upgrade pinned to V1) · temporal verdict **W3** (upgrade pinned to W1) · the V3→V1 engine (1d-β-ii) is gated on the F.1 §14.17 effective action (where the 1100 NESS/μ² route bottoms out).
