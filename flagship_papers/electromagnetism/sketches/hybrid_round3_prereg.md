# PRE-REGISTRATION — HYBRID PIPELINE ROUND 3: CORRECTED BASIS WITH THE β⁰ CORE, TWO-CHANNEL DRIVE, FRESH BANDS

**Patch 2919. Committed and presented BEFORE any Round-3 fit is
computed and BEFORE any Stage-2 number exists. Data: the 60 banked
round-2 mobile legs (`data/2917_round2_legs_raw.json`) + the 12
banked β = 0 control legs (`data/2918_control_legs_raw.json`). NO NEW
SIMULATION LEGS. The 2913 §3 bands judged a quantity the old basis
could not measure; they are retired for Round 3, not reinterpreted —
fresh bands are frozen in §4 below.**

## §1 — PER-BIN MODEL (linear LSQ; frozen)

Seven data points per (ring, ξ-bin): the five mobile β at their
2916-pinned windows plus the two β = 0 control windows —
(β, T) ∈ {(0.04,125), (0.07,107), (0.10,100), (0.14,89), (0.20,63),
(0,63), (0,125)}. Model, linear in four per-bin parameters:

> m(β, T) = p₀ + p_tr/T + β·p₁ + β³·p₃

Regressors (1, 1/T, β, β³). **Data-blind design check, run before
this commit:** column-normalized condition number **14.3** (singular
values 1.82 / 0.77 / 0.28 / 0.13) — well-posed; the β = 0 points at
both window extremes break the mobile legs' β↔1/T collinearity.
Weighted LSQ with per-point ensemble SEs; bins admitted only if
N ≥ 200 in ALL seven datasets.

## §2 — MODEL-ADEQUACY GATE (frozen; replaces the retired collapse gate)

Pooled per-bin residual χ²/dof (3 dof per bin) over all admitted
bins: **χ²/dof < 1.5 required.** Failure ⟹ verdict
INCONCLUSIVE-MODEL; no band in §4 may be claimed, and the frozen
recourse is a basis re-assessment (documented, next prereg), NOT a
post-hoc basis edit inside this round.

## §3 — STAGE 2: TWO-CHANNEL RETARDED DRIVE (deterministic; frozen)

Machinery of 2914/2917 Stage 2 unchanged (quasi-static emitters,
ξ_ret = ξ + β·d, engine-matched softening, class-A cell geometry).
Channels:

- **Static channel:** pattern p₀ alone, swept at β through the
  retarded integral → D₀(β). By mirror symmetry D₀(0) = 0 exactly
  (verify numerically as a sanity assert, |D₀(0)| < 1e-12); extract
  k₀, c₀ from D₀ = k₀β(1 − c₀β²) on the fine β grid of 2914.
- **Dynamic channel:** pattern β·p₁ + β³·p₃ → D₁(β); extract k₁, and
  c_tot from the TOTAL D₀ + D₁ = k β(1 − c_tot β²).
- **The transient channel p_tr is EXCLUDED from all drives** — it is
  an initialization artifact, not substrate physics. Disclosed here,
  frozen.

**Uncertainty:** 200-fold bootstrap resampling all seven input maps
by their SEs through the full per-bin fit and both channels;
report σ for c₀, c_tot, k₀, k₁.

## §4 — FROZEN BANDS (committed before any number)

| outcome | criterion |
|---|---|
| **STATIC-SEA CONFIRMED (provisional)** | \|c₀ − 1/5\| < 0.05 with σ_{c₀} ≤ 0.05 |
| **STATIC-SEA REFUTED (provisional)** | \|c₀ − 1/5\| > 0.15 with σ_{c₀} ≤ 0.05 |
| **TOTAL-CANCELLATION (provisional)** | \|c_tot\| < 0.05 with σ_{c_tot} ≤ 0.05 |
| **TOTAL-RETAINED (provisional)** | c_tot ∈ [0.10, 0.30] with σ_{c_tot} ≤ 0.05 |
| **INTERMEDIATE** | σ met, value outside the above |
| **INCONCLUSIVE** | any required σ > 0.05 |

The static-Sea analytic target is **c₀ = 1/5 EXACTLY** (Patch 2900).
The B1 obstruction question rides on c_tot: the drive's β² curvature
against Newton I's exact-linearity requirement.

**Escalation if INCONCLUSIVE by σ alone (frozen):** seeds {10–15}
mobile legs at the pinned windows (statistics doubling — now
meaningful, since the basis defect is removed), then re-assessment.
No other σ-recourse is permitted.

## §5 — SANITY REGISTER (frozen predictions, unbanded)

(i) k₀ + k₁ linear drive should remain compatible with the thrice
cross-validated k_h ≈ +0.011–0.014. (ii) p₀ from the joint fit should
match the 2918 control map (shape corr > 0.5, amplitude within 30%) —
if it does not, the fit is extracting something else and §2 should be
failing. (iii) p_tr should carry the even/uniform signature of 2918.

## §6 — STANDING

Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds
DM-1/2/3; Candidate (B) 79.5%. G1, P-A2-1, statics suspension, 7 July
ruling stand. CONJ-FP-1: A HOLDS, B CLOSED, curvature OPEN (this
prereg). Anti-screening question OPEN (2918).
