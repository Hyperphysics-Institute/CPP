# EXECUTION RECORD — HYBRID PIPELINE ROUND 1: RESPONSE FIELD MEASURED, THE DISPARITY IMAGED, STAGE 2 INCONCLUSIVE

**Patch 2914. Executed against `hybrid_pipeline_prereg.md` (Patch 2913,
committed and presented before execution).**

# VERDICTS: collapse gate **FAILED AS FROZEN** (and the gate itself is
# shown defective — noise-blind, worker design error); Stage 2 under the
# frozen β³ branch: **INCONCLUSIVE**, σ_c = 27.7 vs ≤ 0.05 required.

---

## §1 — STAGE 1: THE FORE/AFT DISPARITY, IMAGED DIRECTLY

18 instrumented legs (`code/2914_response_field.py`; fields at
`data/2914_response_fields.json`; ~460k binned samples). The axial
induced-dipole field p_x(ξ)/β in the inner ring is coherently
**POSITIVE AFT of the source and NEGATIVE FORE** — an antisymmetric
polarization pattern travelling with the charge. **This is the first
direct substrate-level image of the founder's fore/aft arc disparity:**
the arcs behind the moving charge and the arcs ahead of it are
oppositely polarized, at amplitude ~0.4β (inner ring), decaying outward.

## §2 — COLLAPSE GATE: FAILED, AND THE GATE INDICTED

Frozen R < 0.25; measured R = 0.95 / 0.70 / 0.73. **However**, the
noise-only expectations computed from the stored per-bin errors are
R_n = 1.58 / 1.02 / 0.74, and the collapse χ²/dof = **0.41 / 0.47 /
1.02** — the data are *fully consistent with perfect linear collapse*.
The R-gate was designed noise-blind (it cannot be passed by perfect
physics at these statistics) — **a worker design error, recorded.** The
letter of the prereg was still honored: gate failed ⟹ Stage 2 ran under
the mandatory β³-modelled branch.

## §3 — STAGE 2 (β³ BRANCH): INCONCLUSIVE, WITH A CROSS-VALIDATION

Deterministic retarded integral over the measured pattern
(`code/2914_stage2_integral.py`; quasi-static emitters ⟹ trivial
reception retardation; dipole state evaluated at ξ_ret = ξ + β·d;
engine-matched softening). Result: c_hyb = +12.0, bootstrap
**σ_c = 27.7 ⟹ INCONCLUSIVE** by the frozen gate — with 3 β points the
β³ map is fit through noise and dominates the error budget, precisely
the failure the σ_c criterion exists to catch. No curvature statement
of any kind is licensed.

**Unbanded cross-validation, recorded:** the integral's LINEAR drive
k_h = **+0.0106** independently agrees in sign and to ~25% with the
directly measured differential drive (k_Δ ≈ +0.014, Patches 2910/2912)
— the measured pattern, pushed through independent deterministic
machinery, reproduces the observed push. The pipeline's plumbing is
validated even as its precision round fails.

## §4 — ROUND 2 (pre-registered here, frozen before execution)

Fresh data, corrected gate, better conditioning:
- **Seeds {4,…,9} (entirely fresh)** × classes {A,B} ×
  **five β values {0.04, 0.07, 0.10, 0.14, 0.20}** (β³ conditioning:
  3 dof instead of 1), matched windows (125/100/75/63/63… computed as
  round multiples of 2.5/β capped to [60,125]), same binning.
- **Corrected collapse gate, applied to the FRESH data only:**
  χ²/dof < 1.5 per β (the textbook test the R-gate should have been);
  the defective R-gate is retired with this disclosure. Because the
  revision was motivated by today's data, today's data may NOT be pooled
  into round 2.
- Stage 2 identical (β,β³ fit, bootstrap), frozen bands of 2913 §3
  unchanged, σ_c ≤ 0.05 unchanged. If σ_c > 0.05 again, the frozen
  escalation is a statistics doubling (seeds 10–15), then re-assessment
  of the σ_c budget with the conditioning measured.

## §5 — STANDING

CONJ-FP-1: A HOLDS (2912), B CLOSED (2895); curvature OPEN
(this pipeline). Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven;
B7 holds; Candidate (B) 79.5%. G1, P-A2-1, statics suspension, 7 July
ruling stand.
