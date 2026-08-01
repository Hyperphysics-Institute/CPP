# PRE-REGISTRATION — CONDITION-A SIGN ROUND (SIGN-ONLY BANDS)

**Patch 2909. Committed and presented BEFORE any sign-round leg beyond
the three admitted 2908 gate legs is executed or read. Implements
restructure item (1) of `mobile_sea_chaos_and_power_analysis.md`.
CURVATURE BANDS ARE EXPLICITLY RENOUNCED for this round (infeasible per
the 2908 power wall); this round answers ONE question: the SIGN of the
Sea's differential response — CONJ-FP-1 Condition A.**

## §1 — PROCEDURE

Configuration and engine exactly as validated at 2907/2908: symmetric
classes A (on-plane) and B (mid-cell), transits centred on x = 0,
mirror-symmetrised seeded jitter, gated kernel, grid-matched windows
(β = 0 → 100, 0.05 → 100, 0.10 → 75, 0.20 → 63), T_eq = 40.

Ensemble: seeds {1, 2, 3} × classes {A, B} × β {0, 0.05, 0.10, 0.20},
paired mobile/frozen legs. The three legs already run at the 2908 gate
(fro A1/B1 β=0, mob A1 β=0) are admitted as-is; all others are fresh.
Differential values Δᵢ = D_mob − D_fro at matched (class, seed, β);
**18 moving-β values** in total. Round-2 values are NOT pooled (different
design, known systematics).

## §2 — FROZEN BANDS (sign-only)

Let M, SE = mean and (std/√18) of the 18 moving-β values; M_β, SE_β the
per-β 6-member statistics. Validity: the 6 mobile β = 0 legs' pooled mean
must be consistent with 0 within 2σ (chaos-floor check), else
INCONCLUSIVE.

| verdict | criterion |
|---|---|
| **CONDITION A HOLDS (provisional)** | M > 0, M ≥ 3·SE, and no β with M_β < −2·SE_β |
| **CONDITION A FAILS — DRAG (provisional)** | M < 0, \|M\| ≥ 3·SE, and no β with M_β > +2·SE_β |
| **POWERED NULL — LW-DRESSING SUSPECT** | \|M\| < 1·SE and SE ≤ 0.35×10⁻³ — not a Condition-A verdict; escalates the 2899 LW-like-dressing review |
| **INCONCLUSIVE** | anything else |

Provisional status: a HOLDS/FAILS verdict requires a follow-up
domain-size variation (≥1.3× in ρ_max and length, sign unchanged) before
promotion to a CONJ-FP-1 condition verdict; that variation is a
subsequent pre-registered patch.

**Power, declared:** per-value SE ≈ 1.1–1.3×10⁻³ (chaos statistics,
τ ≈ 3 Moments) ⟹ pooled SE ≈ 0.27–0.31×10⁻³; a real +1.0×10⁻³ response
resolves at ~3.5σ.

**Worker expectation, declared: CONDITION A HOLDS** (the 13-of-15 tally
plus the founder's volume-transfer picture). Declared so a confirming
result is weaker evidence; the tally itself remains weightless until
this round's bands speak.
