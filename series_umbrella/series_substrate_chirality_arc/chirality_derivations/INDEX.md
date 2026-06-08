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

## Continuity note

The label jump `0694 → 1100 → 0902 → 0903…` is intentional. 1100 was produced under the parallel-development system (Round 1); the arc subsequently moved to the 09xx block per the per-arc numbering discussion. Labels are not rewritten (rewriting shared history for a cosmetic label is not worth the breakage). Follow the arc by this index, not by sorting labels.

**Current arc state (from CHIR.md):** spatial verdict **V3** (FI-C-9 the one irreducible primitive; V2 excluded at axiom level; upgrade pinned to V1) · temporal verdict **W3** (upgrade pinned to W1) · the V3→V1 engine (1d-β-ii) is gated on the F.1 §14.17 effective action (where the 1100 NESS/μ² route bottoms out).
