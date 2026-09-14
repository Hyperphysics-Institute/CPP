# Reasoning Index — Chirality Derivations

A **pointer-map** (Tier 2) into the Tier-4 verbatim reasoning fragments. The fragments in
`reasoning/<patch>.md` are the **canonical record**, captured verbatim at patch-time per
`templates/reasoning_capture_protocol.md`. This index does not copy them; it tells you what each
holds and where the load-bearing reasoning lives. (Patches 0632 + 0634 fragments are in
`chirality_audit/reasoning/`, the audit folder, as they predate this folder.)

| Patch | Fragment | Load-bearing reasoning it holds |
|---|---|---|
| 0632 | `chirality_audit/reasoning/0632.md` | The audit rebuild after window overflow; the 27-entry classification logic; the central spatial→`n̂` reduction. |
| 0634 | `chirality_audit/reasoning/0634.md` | Integration of the 3-reviewer cycle; the emergent (E)/(P) grading decision; why no falsifier fired. |
| 0635 | `reasoning/0635.md` | AUDIT-1 cycle close (3/3 on v1.1); the THEO-CHIR-PCD-ORIENTATION-1 scoping decision (primitive-count framing). |
| 0636 | `reasoning/0636.md` | E20 resolution: why primitive-count not magnitude; the robustness argument (3 F.1 commitments reintroduce no primitive); the A5→A1+A4 reconciliation; the E19 cross-link kept distinct. |
| 0637 | `reasoning/0637.md` | E21 scope: `χ=φ⁻³` is FI-C-9 but value-derived by Finding C-3; the CONT-1.3→Finding-C-3 correction; the 1d-α/1d-β decomposition; why staged not single-closure. |
| 0638 | `reasoning/0638.md` | The distance-spectrum exploration that found the locality criterion; the two residual freedoms (bias-form assumption; 1d-β); the `git add -A` stray-patch error + fix. |
| 0639 | `reasoning/0639.md` | E19 scope: the no-false-reduction discipline; the involution×sign insight; the R1/R2/R3 outcomes kept distinct; why R1 is likely-but-unproven. |
| 0640 | `reasoning/0640.md` | The 1c-β decisive test (SD-CHIR sign bookkeeping → R1); why R2 was *left open* deliberately; the local-`I_h` script surprise; the honesty caps held. |
| 0643 | `reasoning/0643.md` | OPEN-CHIR-MERGE scope: is σ_cycle = sign(n̂)? (the E19/E20 merge); the primitive-count framing. |
| 0644 | `reasoning/0644.md` | THEO-CHIR-MERGE-1: OPEN-CHIR-MERGE partially resolved; the primitive-count capstone; the unified-sign current bookkeeping. |
| 0647 | `reasoning/0647.md` | THEO-CHIR-MERGE-2: MERGE-β advanced M3 → M1-χ (chirality-count half); the parity decomposition; OPEN-FP-F1-2 sub-target L4-D. |
| 0648 | `reasoning/0648.md` | MERGE-2 review package issued; the questions put to the reviewers. |
| 0649 | `reasoning/0649.md` | MERGE-2 review integration → v1.1; why no falsifier fired; M1-χ now conditional on MERGE-α. |
| 0650 | `reasoning/0650.md` | The MERGE-2 v1.1 ChatGPT re-review request (toward formal close). |
| 0651 | `reasoning/0651.md` | MERGE-2 cycle close 3/3 → v1.2; ChatGPT's MERGE-α conditionality confirmation. |
| 0652 | `reasoning/0652.md` | OPEN-CHIR-1d-β scope: the FI-C-9 emergence question; the i–v decomposition; the capacity-vs-value distinction. |
| 0653 | `reasoning/0653.md` | STATUS-1: the {V1,V2,V3} partition (exhaustiveness); why current rigor is V3; the 1d-β ID reservation. |
| 0654 | `reasoning/0654.md` | STATUS-2: the H₄→H₄⁺ breaking chain; the axiom-level V2-exclusion; why the upgrade pins to exactly V1. |
| 0655 | `reasoning/0655.md` | STATUS-1/2 review package; the Q1 "informative-vs-relabeling" question put to reviewers. |
| 0656 | `reasoning/0656.md` | STATUS-1/2 cycle close 3/3 → v1.1; ChatGPT's read that the V2-exclusion is the falsifiable content; the three wording calibrations. |
| 0658 | `reasoning/0658.md` | TARROW-1: the T-even-geometry lemma (no T-odd geometric quantity); the CPT unification of the V2/W2 reopeners; the W3 verdict. |
| 0659 | `reasoning/0659.md` | TARROW-1 review package issued. |
| 0661 | `reasoning/0661.md` | TARROW-1 cycle close 3/3 → v1.1; the sector-paired CPT phrasing + the T-even invariant enumeration. |
| 0662 | `reasoning/0662.md` | The bridge scoping: the B-i/B-ii/B-iii/B-iv decomposition; the ℤ₂-match lead; CONJ-CHIR-1's framing. |
| 0663 | `reasoning/0663.md` | BRIDGE-1: the ℤ₂-match (one det-coset object, kinematic, premise P2); the P/T-face dictionary; the CONJ-CHIR-1 kinematic/dynamical split. |
| 0664 | `reasoning/0664.md` | BRIDGE-1 review package (first use of the "initiate review protocol" command). |
| 0665 | `reasoning/0665.md` | BRIDGE-1 cycle close 3/3 → v1.1; the two honest-cap calibrations; the delivery-mode fallback. |
| 0668 | `reasoning/0668.md` | B-iii: capacity ⟺ sign(μ²) of the ℤ₂-even Landau V(η); why the ℤ₂-even form is forced; why the sign is §14.17-gated. |
| 0669 | `reasoning/0669.md` | B-ii: the magnitude anchors (P load-bearing, T signpost); the χ φ⁻¹-vs-φ⁻³ reconciliation as a non-tension; the B4 reclassification. |

*No-fragment patches in this range (by design):* 0645, 0657, 0657a, 0666, 0667 are session-close handovers; 0660 is the review-dispatch protocol (workflow, not physics); 0670 is cross-sector documentation hygiene. 0646 (OPEN-FP-F1-2 scope) is FP/DSL-sector — its reasoning lives in the `dynamical_substrate_law/` area, not this folder.

## Verification scripts (Tier 2/3)

| Script | Theorem | What it asserts (machine precision) |
|---|---|---|
| `code/verify_chi_phi3_ratio.py` | THEO-CHIR-CHI-1 | 600-cell built; 8 distance shells; two nearest = φ⁻¹×12 + 1×20; bias = φ⁻³; `(φ⁻¹,1)` the unique adjacent φ⁻³ pair + max adjacent bias; `1/√5`, `5−2√5` produced only by non-adjacent edge-pairings. |
| `code/verify_capture_involution.py` | THEO-CHIR-CAP-1 | `ζ^W` involution; linear part `−I` flips `n̂`; edge-perturbation field odd under `n̂→−n̂` over all 720 edges (max `φ⁻³`); first-shell↔first-shell edges tangent (local-`I_h`). |
| `code/verify_merge_current_sign.py` | THEO-CHIR-MERGE-1 | The unified-sign current bookkeeping (σ_cycle vs sign(n̂)); the primitive-count check. |
| `code/verify_merge_2_parity_decomposition.py` | THEO-CHIR-MERGE-2 | The parity decomposition behind MERGE-β M3 → M1-χ. |
| `code/verify_status_1_verdict_partition.py` | THEO-CHIR-STATUS-1 | The {V1,V2,V3} verdict partition is exhaustive; the V3 placement at current rigor. |
| `code/verify_status_2_breaking_chain.py` | THEO-CHIR-STATUS-2 | H₄→H₄⁺ index-2 (orders 14400→7200); the order parameter = sign(n̂); the axiom-level V2-exclusion. |
| `code/verify_tarrow_1_arrow_status.py` | THEO-CHIR-TARROW-1 | The substrate invariant set is T-even (no T-odd geometric quantity); the W3 arrow status. |
| `code/verify_bridge_1_z2_match.py` | THEO-CHIR-BRIDGE-1 | The OPEN-SM-4 activation ℤ₂ and the STATUS-2 quotient ℤ₂ are the same det-coset object; the P/T-face dictionary consistency. |
| `code/verify_biii_landau_reduction.py` | B-iii scope (0668) | The ℤ₂-even Landau V(η) reduction; capacity ⟺ sign(μ²); the chiral double-well at μ²<0. |
| `code/verify_bii_chi_normalization.py` | B-ii scope (0669) | χ = (1−φ⁻¹)/(1+φ⁻¹) = φ⁻³; Δp_LR = χ/6 ≈ 0.0394; φ⁻¹ vs φ⁻³ is not a live tension. |

## Provenance

All fragments are `verbatim` (captured at patch-time), not reconstructed; none carries a
`STATUS: reconstructed` header. The capture rode the patch-presentation contract per the
reasoning-capture rider (bootup §3) at each of Patches 0635–0669.

*This index was backfilled for Patches 0643–0669 at Patch 0675 (Session 152) — index/synthesis
hygiene only; the per-patch fragments themselves were captured verbatim at their own patch-times
across Sessions 148–151 and are unchanged.*

---

## Session 228 — Patches 0936–0974 (13 Sep 2026): the capture gap, stated plainly

*Added at Patch 0977 as Step D of the deferred §15 close (TODO-0974a-CAPTURE).*

**Tier-4 verbatim exists for 5 of this session's 39 patches. For the other 34 it does not, and it
cannot now be created.** Tier 4 is defined as Opus's substantive reasoning *preserved verbatim*, and
the window that held it is gone. Writing prose into a `reasoning-<patch>.md` file today would not be
recovery; it would be a fresh narration wearing the name of the canonical record — the one failure
the four-tier discipline exists to prevent, since every other tier is defined as *derived from* Tier 4.
So no such files are written. What follows is the honest substitute: a pointer-map to where each
patch's substance actually lives, all of it committed at patch time.

### Patches with patch-time verbatim capture

| Patch | Fragment | Load-bearing reasoning it holds |
|---|---|---|
| 0936 | `reasoning/0936.md` | The cross-lane E1 response to the DM lane; why the four-state question was answerable from the qDP sector. |
| 0937 | `reasoning/0937.md` | C-W46 flags F1–F3: why no pseudoscalar operator exists on the antipodal pair; the `A_u(I_h) ↓ A₁u` restriction; the inversion-referent correction. |
| 0940 | `../../dynamical_substrate_law/documentation_suite/reasoning-0940.md` | L4-B: why vertex-transitivity is invalid once `n̂` is fixed (nine shells) and `Stab(n̂)`-per-shell transitivity is the valid route. |
| 0941 | `../../dynamical_substrate_law/documentation_suite/reasoning-0941.md` | L4-C: the A6′ Perceive/Displace forcing; why `r(−ê;v)` is the reverse traversal and not a missing edge. |
| 0949 | `../../dynamical_substrate_law/documentation_suite/reasoning-0949.md` | L4-A (Fable): the reversal-odd uniqueness proof; why `A = 0` and truncation are *not* forced. |

### Patches without verbatim capture — where the substance is instead

These artifacts are finished prose, not raw reasoning, and most carry a verify script. They are
Tier-3-grade material sitting at Tier-4 addresses; the distinction matters when a later window asks
"what did the lane actually consider and reject," because these files record conclusions and
generally not the discarded alternatives.

| Patches | Substance lives in |
|---|---|
| 0938, 0939 | `todolist.md` (TODO-0937-CHIR); `code/deferral_gate.py` docstring; commit messages. |
| 0942–0945 | `series_standard_model/corrigenda/SM-2_composition_corrigendum.md` + `corrigenda/code/0943_…py`, `0945_…py`; `corrigenda/W_ring_harmonization_query.md`. |
| 0946–0948 | `review/0946_w0_chirality_source.md`; `review/0947_w0_ring_order.md` (6/6). |
| 0950, 0951 | `review/0950_capacity1_residual_consumption.md` (7/7); `review/0951_c3_klift_recompute.md` (5/5). |
| 0952–0960 | `review/0952_…package.md`, `0953_conv047_adjudication.md`, `0954_…package.md` + `…wrapper.md`, `0955_…`, `0956_…addendum.md`, `0957_…`, `0958_…final_round.md`, `0959_round_economy_resolution.md`, `0960_conv048_adjudication_and_enactment.md`; **reviewer returns verbatim** at `reviews/verbatim/` (committed at 0974a, Step F). |
| 0961–0968 | `sketches/0961_piece1_scoping.md`, `0963_piece1_route_a_first_step.md`, `0964_piece1_hostile_pass.md`; `0965_piece1_assembly.md`, `0966_piece1_physical_delta.md`; `review/0967_conv049_reviewer_package.md`, `0968_conv049_adjudication.md`; `code/0968_three_plane_lemma.py` (5/5). |
| 0969–0971 | `review/0971_tarrow2_reread.md` (6/6); 0969's content is its commit message and the `reviews-CONV-049.md` annotations. |
| 0970 | `sketches/0970_1dbeta_scoping.md`; `problem_histories/PH-OPEN-CHIR-1d-beta.md`. |
| 0972–0974 | `../../dynamical_substrate_law/l4e_delta_epsilon.md` (5/5); `…/nonreciprocity_is_the_arrow.md` (6/6); `handovers/2026-09-13_session_228_…md`. |

### Why the gap happened, and what changed because of it

The capture rider (bootup §3) binds Tier-4 capture to the patch-presentation contract precisely
because that contract is the one habit honoured unasked. It held for 0936, 0937, 0940, 0941 and 0949
— **and those five are the session's derivations.** It lapsed across the panel, corrigendum and
scoping patches, which were not felt to be "physics/derivation" patches. That intuition was wrong in
at least three places: CONV-048's joint-corner finding, CONV-049's 3-plane lemma and 0966's
proxy-sensitivity bound were all substantive reasoning, and two of the three came from reviewers
rather than from the lane.

Nothing in this note is a rule change; the lane does not amend the operating system from a
documentation patch. It is a recorded observation for whoever next revisits the rider: **the
"pure-bookkeeping/organizational" exemption is doing more work than it was designed for, and a panel
adjudication is not bookkeeping.**
