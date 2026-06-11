# Flagship assembly scope — "Chirality in the Conscious Point Substrate: Primitive, Emergent, or Both?"

**Register:** PLANNING ARTIFACT — a Phase-7-style assembly scope, not the paper and not a commitment to build. Moves no verdict; registers nothing. Created Patch 0933 (chirality lane), Session 158.
**Decision it serves:** lets Thomas see the flagship's shape before choosing ship-conditional-now vs wait-for-Mechanism-A.
**Source of the title/scope:** the named eventual flagship in `frontier_sectors/CHIR.md` ("Paper(s)" line, scope-sketch §7).

---

## 0. The correction this scope rests on (read first)

`theo_chir_cap_1.tex` is **THEO-CHIR-CAP-1** — the Capotauro chirality *matrix element* (the observable 𝒞_χ, B₂ irrep of D₆, max |δ| = φ⁻³ ≈ 0.0394, the magnitude side; shipped). It is **not** THEO-CHIR-CAPACITY-1, the spatial *status* theorem (μ²-sign / det-coset condensation, V1-excluded/V3-confirmed) enacted Patch 0927. **There is no `theo_chir_capacity_1.tex`.** CAPACITY-1 currently exists only as: the CHIR.md enactment record (changelog-style), the closure math in `dynamical_substrate_law/sketches/` (0826 `lcapa_axis2_signcorr_closure.md`, 0828 `pathA_pointwise_chord_closure.md`), the review suite (`chirality_derivations/review/` 0920–0926), and the Path-B sibling (`0925_capacity1B_narrowed_theorem.md`). **Drafting the CAPACITY-1 `.tex` is the single largest assembly task** (Gap 1, below).

## 1. What the flagship claims (the answer to its own title)

**Primitive (V3 spatial / W3 temporal) on both faces, conditional on Mechanism A.** V1/W1 (emergence-by-condensation) excluded by the capacity theorems; V2/W2 (full derivation) excluded at the axiom level; reopenable only cross-sector (OPEN-SM-4). It is a **status / foundations** result: it tightens the axiom inventory (confirms FI-C-9 is a genuine irreducible primitive, kills the emergence scenario); it adds **no new zero-parameter prediction**. Its empirical *corroboration* (not proof) is the χ = φ⁻³ magnitude carried into SM observables (CAP-1's Δp_LR = χ/6 ≈ 0.0394; δ_CP ≈ 193.3° vs NuFIT 195°±40°).

## 2. Section structure + file mapping (the 39 .tex files)

**Main text — the verdict spine (13 theorems):**

| § | Section | Theorem files | Role |
|---|---|---|---|
| §1 | Introduction & the trichotomy | `theo_chir_status_1.tex` (STATUS-1: {V1,V2,V3} exhaustive) | frame the question + the framing guard (off-critical ⇒ primitive) |
| §2 | What "chirality" denotes (classification) | `theo_chir_audit_1.tex` (AUDIT-1, 24-row) + `manifestation_inventory.md` | fix the referent across the corpus |
| §3 | Full derivation (V2) excluded | `theo_chir_status_2.tex` (STATUS-2: no axiom-level pseudoscalar; H₄→H₄⁺ ℤ₂) | close V2 at axiom level; flag OPEN-SM-4 as the sole reopener |
| §4 | The two faces and their unification | `theo_chir_merge_1.tex`, `theo_chir_merge_2.tex`, `theo_chir_pcd_orientation_1.tex`, `theo_chir_bridge_1.tex`, `theo_chir_tarrow_1.tex` | P/T faces; PCD-cycle orientation = thermodynamic arrow; ℤ₂-match (BRIDGE-1); CPT unification (TARROW-1) |
| §5 | Temporal capacity verdict (W3→W1 cond.) | `theo_chir_tarrow_2.tex` (TARROW-2) | the temporal capacity move; NESS / O(δ³) current |
| §6 | **Spatial capacity verdict (V1 excluded / V3 confirmed cond.)** | `theo_chir_vw_1.tex` (VW-1: reduce to reflection-positivity), `theo_chir_vw_2.tex` (VW-2: δ=0 anchor), **+ CAPACITY-1 `.tex` [TO BE DRAFTED]** | **centerpiece**: VW reduction → μ²-sign via refined-chord bound ρ(M)≤2/3<1 |

**Main text — the magnitude / empirical-anchor side (3 theorems):**

| § | Section | Theorem files | Role |
|---|---|---|---|
| §7 | Magnitude & corroboration | `theo_chir_chi_1.tex` (CHI-1: χ=φ⁻³ = FI-C-9 magnitude), `theo_chir_cap_1.tex` (CAP-1: 𝒞_χ matrix element, Δp_LR=χ/6), `capotauro.tex` (Capotauro mechanism, K3-doublet) | carry χ into SM observables; **framed as support "not used in the proof," not load-bearing** (per CHIR.md) |

**Main text — synthesis:**

| § | Section | Source | Role |
|---|---|---|---|
| §9 | Verdict, conditionality, open residuals | CHIR.md verdict record + `problem_histories/PH-OPEN-CHIR-1d-beta.md` | the consolidated verdict + the EU-1-style "does not block" framing (see §4 below) |
| §10 | Downstream propagation (optional) | `chirality_continuum.tex` (Layer-4 cross-sector; V−A CONT-2, chiral-polarity-bias CONT-3) | how the one frozen primitive propagates to higher-level chirality |

**Cited companion / appendix — the DSL engine (~23 files, NOT reproduced in main text):**
`dynamical_substrate_law.tex` + the geometric primitives and D₅-orbit machinery (`first_shell_inner_product_primitive`, `second_shell_inner_product_primitive`, `host_to_first_shell_projection`, `host_second_shell_uniform_projection`, `first_shell_perpendicularity`, `second_shell_perpendicularity`, `first_shell_second_shell_edge_orbits`, `first_shell_first_shell_edge_d5_orbits`, `cross_shell_edge_d5_orbits`, `first_shell_d5_orbit_projections`, `second_shell_projection_d5_orbits`) + the O(δⁿ) substrate-current coefficient machinery (`o_delta_one/two/three/four_*_coefficient`, `o_delta_squared_path_class_weights`, `o_delta_squared_substrate_locality_umbrella`, `perturbation_locality_propagation`, `second_order_parallel_to_n_structural`, `edge_aligned_invariant_subspace_structural`, `face_aligned_invariant_subspace_structural`). **Recommendation: cite as the F.1/DSL companion line, do not inline.** These underpin the NESS/O(δ³) current (§5) and the DSL but would bury the verdict narrative. The flagship is about the *verdict*, not the engine.

## 3. Where the conditionality and the two residuals are stated

- **Conditionality (Mechanism A):** stated identically in §5 (TARROW-2) and §6 (CAPACITY-1) — both verdicts are "conditional on Mechanism A (OPEN-FP-F1-2)"; consolidated in §9. The §6 statement additionally names its two sub-conditions (per-edge independence + pointwise non-degeneracy of the dynamical η).
- **Residual 1 — Mechanism A discharge (OPEN-FP-F1-2):** §9. The single unconditionalizer; discharging it makes BOTH §5 and §6 unconditional. Now a 900-lane workstream.
- **Residual 2 — pointwise non-degeneracy of the dynamical η:** §6 + §9. The narrow PCD door; carried as a named condition.
- **V2 reopener (OPEN-SM-4):** §3 + §9. Cross-sector (SM CP/T phase, CPT-linked); the only road to V2.

## 4. The EU-1-style "does not block" framing (§9)

Model on EU-1 (`PH-OPEN-EU-1.md`): EU-1 shipped framework-conditional, counting PRED-C-96 at the conditional/grounded level, with OPEN-EU-1 a registered residual that "does not block the count," noting CPP is **at parity with the field** (standard inflationary cosmology also does not derive homogeneity from first principles).

The flagship's parallel: the verdict (V3/W3 primitive on both faces) and the corroborating χ/6 and δ_CP anchors stand at the **framework-conditional** level, with **OPEN-FP-F1-2 (Mechanism A)** and the **pointwise-non-degeneracy residual** registered as residuals that **do not block**. CPP is at parity with the field: chirality-selection-from-first-principles is unsolved field-wide (the origin-of-homochirality debate — dynamical amplification vs electroweak parity violation), so the flagship is not behind; it does not claim more than it has. Shipping conditional now is upgradeable: discharging Mechanism A later is a clean v1.0 → v1.x revision swapping the conditional headline for the unconditional one.

## 5. Assembly gaps (what must be produced beyond what exists)

1. **Draft the CAPACITY-1 `.tex`** — the centerpiece §6 theorem has no formal write-up. Source: CHIR.md enactment paragraph + 0826/0828 closure sketches + 0926 review. **Largest single task.**
2. **DSL-machinery placement decision** — cited F.1/DSL companion (recommended) vs appendix. ~23 files.
3. **Intro / trichotomy narrative (§1)** — frame "Primitive, Emergent, or Both?" and its answer; new prose.
4. **Conditionality harmonization** — §5 and §6 must state Mechanism A identically; §9 consolidates. Guard against a draft that reads stronger than the engine licenses (the TARROW-2 v1.0→v1.1 lesson).
5. **Empirical-anchor honesty (§7)** — δ_CP and χ/6 framed as corroboration "not used in the proof," not load-bearing.
6. **Synthesis + residuals (§9)** — the EU-1 "does not block" paragraph; cite PH-OPEN-CHIR-1d-beta.

## 6. Recommended build sequence (Phase 7A/B/C)

- **7A (pre-draft):** draft the CAPACITY-1 `.tex` (Gap 1); decide DSL companion vs appendix (Gap 2); lock the §-skeleton. *Gate: CAPACITY-1 .tex exists and is internally consistent with the 0926-reviewed closure.*
- **7B (assembly):** slot the 13 spine theorems + 3 magnitude theorems into the skeleton; write §1 intro and §9 synthesis; harmonize conditionality (Gap 4); add §7 with the honesty framing (Gap 5). *Gate: full draft compiles, conditionality consistent, residuals stated.*
- **7C (review/ship):** cross-reviewer pass — **scoped to framing + conditionality, not new math** (the components are already 3/3-reviewed individually; the review question is "does the assembly over-claim, and is the conditionality honest"). Ship framework-conditional (EU-1 precedent), or hold for Mechanism A if the 900-lane discharge is near.

## 7. The one open decision (ship-now vs wait)

Tips on **how near OPEN-FP-F1-2 is in the 900 lane**. If Mechanism A is plausibly near, 7C waits and ships unconditional. If far/uncertain, ship conditional at 7C and upgrade later. The assembly work (7A/7B) is worth doing *either way* — it is the scaffold the Mechanism-A discharge slots into, and it is bounded (unlike the discharge).
