# Problem History: OPEN-CHIR-1d-β — the spatial chirality capacity question (THEO-CHIR-CAPACITY-1)

**Created:** 9 June 2026 (Session 157-close / 158, chirality lane; PH created Patch 0932).
**Status:** **Capacity half (1d-β-ii) RESOLVED** — V1 (emergence-by-condensation) excluded / V3 (primitive) confirmed, conditional on Mechanism A, by **THEO-CHIR-CAPACITY-1** (enacted Patch 0927; 3/3 review-closed). **OPEN-CHIR-1d-β remains OPEN** for the V2 reopener (cross-sector OPEN-SM-4) and the located residual (derive pointwise non-degeneracy of the dynamical η).
**Frontier entries:** OPEN-CHIR-1d-β (sector home `frontier_sectors/CHIR.md`); V2-reopener co-owned with OPEN-SM-4 (`frontier_sectors/SM.md`).
**Sector record:** `frontier_sectors/CHIR.md` (CAPACITY-1 enacted changelog-style — no theorem-registry body-row, per CHIR precedent).
**Why this PH exists:** this one question was developed across **two patch-bands by two windows** — the **08xx** band (F.1/DSL window: the C1 closure computation) and the **09xx** band (chirality lane: swarm review, adjudication, enactment). Patch numbers alone do not reveal that they are one development; this file is the problem-keyed trail that crosses the band boundary.

---

## The problem

Is the substrate chirality primitive FI-C-9 a genuine primitive (V3), or emergent by spontaneous condensation of the det-coset ℤ₂ order parameter η (V1)? (V2 — fully derived — was excluded at the axiom level earlier, by STATUS-2.) The decisive quantity is `sign(μ²)`: μ²<0 ⇒ η condenses ⇒ V1 (emergent); μ²>0 ⇒ η does not condense ⇒ V3 confirmed / V1 excluded. Framing guard: off-critical / μ²>0 / unbroken ⇒ **primitive**, not emergent.

## Resolution (capacity half, 1d-β-ii)

`ρ(M) ≤ 2/3 < 1` (det-coset sign-correlation spectral radius, homogeneity-free) ⇒ no condensation ⇒ μ²>0 ⇒ **V1 excluded / V3 confirmed**, conditional on Mechanism A + two named sub-conditions: per-edge independence + pointwise non-degeneracy of the dynamical η. Spatial analog of the temporal TARROW-2 move. Status theorem, not a derivation. Stays open: the V2 reopener (OPEN-SM-4, CPT-linked) and the residual (whether the substrate *guarantees* pointwise non-degeneracy — the narrow PCD door).

## Development trail (cross-band — the point of this file)

Pointer-map only: patch · band · one-line · path. The canonical content lives in the pointed-to files; do not re-narrate here.

**Prior provenance (pre-this-session, cross-window):**
- `0653` (09xx-era) · ID **reserved** for the capacity verdict.
- `0680` · **THEO-CHIR-VW-1** reduced the capacity question to "is the DSL measure reflection-positive (H1)?" — if H1 ⇒ μ²>0 ⇒ V3-by-principle. (3/3-closed; H1 not proved.)
- `~1100` (08xx/11xx, F.1/DM window) · χ_sym = N/m² computed; `sign(μ²)=sign(m²)`; the (H-NESS) obstruction sharpened. "CAPACITY-1 stays reserved."

**The closing arc — 08xx band (F.1/DSL window: the C1 closure computation):**
- `0826` · equal-weight closure: shared-edge sign law + row-sum bound `R(m)=m·(2/π)arcsin(1/m)<1`. Sound but **equal-weight only**. → `dynamical_substrate_law/sketches/lcapa_axis2_signcorr_closure.md`, `dynamical_substrate_law/code/0826_lcapa_signcorr_rowsum.py`.
- `0827` · weighted attempt: "homogeneity ⇒ max row sum = avg ≤ 1." **FALSIFIED by the 09xx lane (0922).**
- `0828` · the repair (**adopted**): refined-chord quadratic-form bound `ρ(M) ≤ κ(z*) = (2/π)arcsin(z*)/z* < 1`, **homogeneity-free**; pointwise `p(v)≥4 ⇒ z*≤½ ⇒ ρ≤2/3`. → `dynamical_substrate_law/sketches/pathA_pointwise_chord_closure.md`, `dynamical_substrate_law/code/0828_pathA_pointwise_chord_bound.py`.

**The closing arc — 09xx band (chirality lane: review, adjudication, enactment):**
- `0920` · DG-3 re-fire #1 presentation. → `chirality_derivations/review/0920_dg3_capacity1_refire_presentation.md`.
- `0921` · re-fire #1 results: **2 CONFIRM / 1 RESTATE**; ChatGPT's weight-concentration falsifier **granted** (equal-weight R(m) insufficient). → `review/0921_dg3_refire_results_RESTATE.md`; verify `code/0921_weight_concentration_falsifier_check.py` (committed 0929).
- `0922` · **the lane falsifies 0827** with an explicit n̂-concentration counterexample (max row=1.0, ρ=1.0 at mean p≈2.6; max≠avg); fix must be **pointwise**, not mean. → `review/0922_review_of_0827_pathA.md`; verify `code/0922_nhat_concentration_counterexample.py` (committed 0929).
- `0923` · review + **adoption of 0828** (independently verified: analytic + 120 adversarial weightings, 0 violations). → `review/0923_review_of_0828_adopt.md`; verify `code/0923_refined_chord_bound_verification.py` (committed 0929).
- `0924` · DG-3 re-fire #2 presentation (C1 = pointwise κ-bound; residual surfaced as explicit conditionality). → `review/0924_dg3_capacity1_refire2_presentation.md`.
- `0925` · Path B **CAPACITY-1B** (unconditional-on-residual narrowed sibling) **banked, not registered**. → `chirality_derivations/0925_capacity1B_narrowed_theorem.md`.
- `0926` · re-fire #2 results: **3/3 CONFIRM, no falsifier** (PASS); Q5 conditionality calibration (named, conservative). → `review/0926_dg3_refire2_results_PASS.md`.
- `0927` · **ENACTMENT**: V1 excluded / V3 confirmed, conditional on Mechanism A. → `frontier_sectors/CHIR.md` (enactment paragraph + verdict-header ref), `theorem-registry.md` (changelog).
- `0928` · handover (Session 158). → `handovers/2026-06-09_session_158_capacity1_enacted_v3_confirmed.md`.
- `0929` · capture-audit remediation: committed the 0921/0922/0923 verify scripts.

**Downstream / adjacent (this session, not core derivation):**
- `0930` · governance: OS §15.15 capture-audit trigger clause (process lesson from the 0928 capture gap).
- `0931` · speculative record: the imprint-epoch / QGE discussion → `founders_vision/physical_metaphysical_speculation/2026-06-09_chirality_primitive_QGE_and_imprint_epoch.md` (advisory pointer at OPEN-SM-4 sub-claim (a)).

## Closure path (for the parts still open)

- **Unconditionalize:** discharge Mechanism A (OPEN-FP-F1-2 / F.1 §14.17, F.1/DM window) — would unconditionalize BOTH CAPACITY-1 (spatial) and TARROW-2 (temporal). And/or derive the residual (pointwise non-degeneracy) from the PCD layer (the per-vertex 4-D Perceive/Compute is the natural candidate).
- **V2 reopener:** the cross-sector SM CP/T phase, OPEN-SM-4 (CPT-linked, BRIDGE-1/TARROW-1). The only door to V2.

## Pointers

Sector record `frontier_sectors/CHIR.md`; arc index `series_umbrella/series_substrate_chirality_arc/chirality_derivations/INDEX.md`; review suite `chirality_derivations/review/`; closure math `dynamical_substrate_law/sketches/` (0826, 0828) + `dynamical_substrate_law/code/`; temporal analog TARROW-2 (Patch 0692); reservation lineage VW-1 (0680).
