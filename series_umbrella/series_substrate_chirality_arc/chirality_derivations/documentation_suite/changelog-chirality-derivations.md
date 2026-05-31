# Changelog — Chirality Derivations

Patch history of the chirality-derivations sub-corpus. Newest first. Version history of each
`.tex` is in its own internal CHANGELOG header; this is the sub-corpus-level patch log.

---

**Patch 0670 (Session 151, 30 May 2026) — cross-sector hygiene.**
Corrected the stale OPEN-SM-4 one-line in `frontier_sectors/SM.md` (χ "≈ φ⁻¹" → φ⁻³) — the
documentation root cause of the apparent χ tension and of BRIDGE-1 falsifier B4. Isolated from
0669 for independent apply. No mechanism content changed.

**Patch 0669 (Session 151, 30 May 2026) — B-ii magnitude anchors scoped + χ φ⁻¹-vs-φ⁻³ reconciled.**
`sketches/chir_bii_magnitude_anchors_scoping.md` + `code/verify_bii_chi_normalization.py` (all
checks pass). B-ii-P (Δp_LR = χ/6 = φ⁻³/6 ≈ 0.0394) load-bearing/shipped (CAP-1); B-ii-T (δ_CP)
signpost only, gated behind B-iii. χ "tension" resolved as a **non-tension** (φ⁻³ live; φ⁻¹ the
retired dead-end *and* the first-shell distance χ is built from). BRIDGE-1 falsifier B4 reclassified
(documentation; sub-claim-(b) hook). No verdict move.

**Patch 0668 (Session 151, 30 May 2026) — B-iii capacity engine scoped.**
`sketches/chir_biii_capacity_landau_scoping.md` + `code/verify_biii_landau_reduction.py` (all
checks pass). Capacity ⟺ **sign(μ²)** of a ℤ₂-even Landau V(η) in the det-coset order parameter
(μ²<0 ⇒ chiral double-well ⇒ V3→V1); EWSB-identification ⟺ substrate μ² = Higgs μ² (CONJ-CHIR-1).
ℤ₂-even *form* reachable now; *sign of μ²* gated behind F.1 §14.17. Structural reduction only; no
verdict move.

**Patch 0665 (Session 150, 30 May 2026) — THEO-CHIR-BRIDGE-1 review cycle CLOSED 3/3 → v1.1.**
All three reviewers CONFIRMED at Layer-2.5 (ℤ₂-match forced/sound, P2 sound); two honest-cap
calibrations (discharge conditional on P2 / "skeleton identified, bridge not built"; summary-
discipline Remark). First live use of the dispatch-protocol delivery-mode fallback.
`review/reviews-CHIR-BRIDGE.md`.

**Patch 0664 (Session 150) — BRIDGE-1 multi-AI review cycle OPENED** (first use of the "initiate
review protocol" command).

**Patch 0663 (Session 150, 30 May 2026) — THEO-CHIR-BRIDGE-1 (B-i of the CHIR↔EW bridge).**
`theo_chir_bridge_1.tex` + `code/verify_bridge_1_z2_match.py`. A Layer-2.5 structural correspondence
(NOT a derivation): the OPEN-SM-4 activation ℤ₂ = the STATUS-2 quotient ℤ₂ = one det-coset object
(kinematic, conditional on premise P2) + the P/T-face dictionary. CONJ-CHIR-1 kinematic half
discharged, dynamical half isolated as B-iii. No verdict move.

**Patch 0662 (Session 150, 30 May 2026) — CHIR↔electroweak bridge SCOPED.**
`sketches/chir_ew_bridge_scoping.md`; unifies OPEN-CHIR-1d-β-v ∪ OPEN-CHIR-3 (co-owned with
OPEN-SM-4); decomposition B-i/B-ii/B-iii/B-iv; the ℤ₂-match lead. NEW conjecture **CONJ-CHIR-1**
(substrate chiral-vacuum transition = Capotauro activation = EWSB).

**Patch 0661 (Session 150, 30 May 2026) — THEO-CHIR-TARROW-1 review cycle CLOSED 3/3 → v1.1**
(ChatGPT + Grok + Copilot CONFIRMED; sector-paired CPT phrasing + CPT-logic Remark + the T-even
invariant set enumerated). `review/reviews-CHIR-TARROW.md`.

**Patch 0660 (Session 150, 30 May 2026) — review-dispatch protocol** (workflow infrastructure; no
chirality physics). NEW `templates/review_dispatch_protocol.md` + OS §1/§5 — the canonical "initiate
review protocol" command, the review-side analog of the §15 handover.

**Patch 0659 (Session 150) — TARROW-1 multi-AI review cycle OPENED.**

**Patch 0658 (Session 150, 30 May 2026) — THEO-CHIR-TARROW-1 (the T-arrow sign(δ) status, OPEN-CHIR-2a).**
`theo_chir_tarrow_1.tex` + `code/verify_tarrow_1_arrow_status.py`. Instantiates the STATUS-1
partition on the temporal axis: sign(δ) is **W3**, upgrade pinned to **W1**. The T-even-geometry
lemma (no T-odd geometric quantity → disanalogy with parity) + the CPT unification (spatial V2- and
temporal W2-reopeners are the same SM CP/T object). Closes the status capstone's temporal half.

**Patches 0657 + 0657a (Session 149 close) — handover** (status capstone closed; 0657a itemizes the
v1.1 reviewer microcorrections). No physics.

**Patch 0656 (Session 149, 29 May 2026) — STATUS-1 + STATUS-2 review cycle CLOSED 3/3 → v1.1**
(all CONFIRMED at Layer-2.5; capstone endorsed; ChatGPT: STATUS-2's V2-exclusion is what makes the
pair a falsifiable constraint, not relabeling). `review/reviews-CHIR-STATUS.md`.

**Patch 0655 (Session 149) — STATUS-1 + STATUS-2 multi-AI review cycle OPENED.**

**Patch 0654 (Session 149, 29 May 2026) — THEO-CHIR-STATUS-2.**
`theo_chir_status_2.tex` + `code/verify_status_2_breaking_chain.py`. The chiral-vacuum breaking
chain H₄ → H₄⁺ (order 14400 → 7200, index-2 ℤ₂; order parameter sign(n̂) = FI-C-9); axiom-level
V2-exclusion ⇒ the emergence upgrade pinned to exactly **V1** (emergent mechanism, contingent sign).
Verdict stays V3.

**Patch 0653 (Session 149, 29 May 2026) — THEO-CHIR-STATUS-1 + OPEN-CHIR-1d-β ID reserved.**
`theo_chir_status_1.tex` + `code/verify_status_1_verdict_partition.py`. Formalizes the verdict space
{V1,V2,V3} (proved exhaustive); current rigor **V3** (FI-C-9 = the one currently-identified
irreducible chirality primitive); names the V1 upgrade condition (1d-β-ii).

**Patch 0652 (Session 149, 29 May 2026) — OPEN-CHIR-1d-β scoped (the FI-C-9 emergence question; the status crux).**
`sketches/chir_open_1d_beta_fi_c_9_emergence_scoping.md`. Decomposes 1d-β into i–v; the
capacity-vs-value distinction; current-rigor verdict V3, achievable upgrade V1.

**Patch 0651 (Session 149, 29 May 2026) — THEO-CHIR-MERGE-2 review cycle CLOSED 3/3 → v1.2**
(ChatGPT CONFIRMED: verdict M1-χ conditional on MERGE-α). `review/reviews-CHIR-MERGE-2.md`.

**Patch 0650 (Session 149) — MERGE-2 v1.1 ChatGPT re-review request issued** (toward formal cycle
close).

**Patch 0649 (Session 149, 29 May 2026) — THEO-CHIR-MERGE-2 review integrated → v1.1** (calibration,
no falsifier; verdict M1-χ stands, now conditional on MERGE-α).

**Patch 0648 (Session 149) — THEO-CHIR-MERGE-2 multi-AI review cycle OPENED.**

**Patch 0647 (Session 149, 29 May 2026) — THEO-CHIR-MERGE-2.**
`theo_chir_merge_2.tex` + `code/verify_merge_2_parity_decomposition.py`. OPEN-CHIR-MERGE MERGE-β
advanced M3 → M1-χ (chirality-count half resolved); OPEN-FP-F1-2 sub-target L4-D delivered.

**Patch 0646 (Session 149, 29 May 2026) — OPEN-FP-F1-2 scoped** (Layer-4 axiomatic derivation of
Mechanism A from A1–A11; the shared gate for MERGE-β and OPEN-CHIR-2a). Cross-sector scope; no
chirality theorem.

**Patch 0645 (Session 148 close) — handover** (CHIR audit-downstream derivation arc complete). No
physics.

**Patch 0644 (Session 148, 29 May 2026) — THEO-CHIR-MERGE-1.**
`theo_chir_merge_1.tex` + `code/verify_merge_current_sign.py`. OPEN-CHIR-MERGE partially resolved
(unified-chirality-sign; the primitive-count capstone — is σ_cycle = sign(n̂)?).

**Patch 0643 (Session 148, 29 May 2026) — OPEN-CHIR-MERGE scoped** (the unified-chirality-sign
question; the E19/E20 merge). `sketches/theo_chir_merge_1_scope.md`.

**Patch 0641 (Session 148, 29 May 2026) — documentation-suite consolidation.**
This consolidation: `README.md` (folder index) + `documentation_suite/` (mechanism, development,
reasoning-index, keywords, glossary, phenomena, changelog) synthesized from the Tier-4 verbatim
reasoning fragments at the three-derivations milestone. No physics changed. The per-patch
`reasoning/*.md` fragments remain the canonical record.

**Patch 0640 — THEO-CHIR-CAP-1 v1.0 (E19, capture handedness).**
Resolves the deepest unregistered audit entry. capture handedness = `ζ` (registered involution)
× `σ_capture`, with `σ_capture = sign(n̂) = FI-C-9` (verdict R1, from the SD-CHIR sign
bookkeeping). No independent third primitive; **E19 emergent (provisional)**. R3 refuted; R2
(E19/E20 merge) left as hypothesis; FI-C-9 consumed not eliminated. + `code/verify_capture_
involution.py` (all checks pass). 1c/2d duplication collapsed onto 1c.

**Patch 0639 — OPEN-CHIR-1c/2d (E19) scope sketch.**
`sketches/theo_chir_cap_1_scope.md`. The involution×sign decomposition; the no-false-reduction
discipline; the R1/R2/R3 outcomes; replacing Grok's unregistered seed with the registered ζ
structure. THEO-CHIR-CAP-1 reserved.

**Patch 0638 — THEO-CHIR-CHI-1 v1.0 (E21 / sub-gap 1d-α).**
A locality criterion (symmetric bias of the two nearest 600-cell shells) uniquely selects
`χ = φ⁻³`; `1/√5`, `5−2√5` excluded as non-local. **1d-α closed** (Layer 2/2.5); answers "why
exponent −3". + `code/verify_chi_phi3_ratio.py` (all checks pass). E21 stays emergent (P)
(1d-β open). [Build note: a stray patch file swept in by `git add -A` was caught and removed
pre-delivery.]

**Patch 0637 — OPEN-CHIR-1d (E21) scope sketch.**
`sketches/theo_chir_chi_magnitude_1_scope.md`. `χ = φ⁻³` is FI-C-9 (input) with value-derivation
Finding C-3; corrected the audit's CONT-1.3 note (CONT-1.3 is inheritance, not derivation);
decomposed into 1d-α (ratio, near-term) + 1d-β (dynamics, deep). THEO-CHIR-CHI-1 reserved.

**Patch 0636 — THEO-CHIR-PCD-ORIENTATION-1 v1.0 (E20).**
First downstream theorem. `ω_PCD = σ_cycle·n̂`, a product of two registered primitives; Scenario B
refuted; **E20 emergent (provisional)** (viability/Layer 2.5). Primitive-count, robust to the
three open F.1 commitments. Precondition cleared (σ_cycle ← A1+A4, not the F.1 "A5").

**Patch 0635 — THEO-CHIR-PCD-ORIENTATION-1 scope sketch + AUDIT-1 cycle close.**
`sketches/theo_chir_pcd_orientation_1_scope.md`. AUDIT-1 review cycle closed 3/3 on v1.1; the
audit `.tex` frozen. (The `chirality_derivations/` folder was created at this patch.)

---

**Upstream (audit, in `chirality_audit/`):** Patch 0632 THEO-CHIR-AUDIT-1 registered (the 27-entry
catalogue); Patches 0633–0634 the multi-AI review cycle (v1.0→v1.1 label calibration; no
falsifier). These predate this folder; their reasoning fragments are in `chirality_audit/reasoning/`.

**Open frontier (unchanged by this sub-corpus):** FI-C-9 elimination (1d-β); the symmetric-bias
form assumption (CHI-1 F2); the E19/E20 merge (whether `σ_cycle = sign(n̂)`).
