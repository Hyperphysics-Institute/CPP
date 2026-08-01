# EXECUTION RECORD — HYBRID PIPELINE ROUND 2: SIGMA IMPROVED 13×, VERDICT INCONCLUSIVE AS FROZEN, AND THE STAGE-2 MODEL INDICTED — THE PATTERN HAS A β-INDEPENDENT CORE

**Patch 2917. Executed against the ROUND 2 freeze of Patch 2914 §4 and
the window literals PINNED at Patch 2916 (β = 0.04/0.07/0.10/0.14/0.20 →
T_meas = 125/107/100/89/63, T_eq = 40). Bands unchanged from
`hybrid_pipeline_prereg.md` §3. Fresh data only; round-1 fields neither
read nor pooled.**

# VERDICTS: collapse gate (corrected χ² form) **FAILED at 4 of 5 β** —
# genuine β-structure, the β³ branch is mandatory as frozen; Stage 2
# under that branch: **INCONCLUSIVE, σ_c = 2.11 vs ≤ 0.05** — but the
# bootstrap now *localizes* c_hyb ≈ +19.7 ± 2.1, two orders of magnitude
# outside every band, and post-hoc diagnostics identify the cause as a
# STAGE-2 MODEL MIS-SPECIFICATION, not statistics. The frozen
# seeds-{10–15} escalation is statistically incapable of reaching the
# gate (√2 vs a 42× gap) and its premise (noise-limited σ) is
# contradicted by the data; per the freeze's own second step, this
# record IS the conditioning re-assessment.

---

## §1 — EXECUTION

60 fresh legs, seeds {4–9} × classes {A,B} × five β, at the 2916-pinned
windows, batched single-process (`code/2917_round2_driver.py`, resumable,
wall-clock guard; numba JIT paid once per process per the 2912 lesson).
Raw per-leg sums archived verbatim: `data/2917_round2_legs_raw.json`
(60 legs, ~1.9M binned samples). One pre-batch calibration leg
(A, seed 4, β = 0.20, T = 63) conforms to the pin and is a grid member.

**Window-pin incident, disclosed:** before Patch 2916 reached this
worker, the ambiguous 2914 §4 window rule was independently
reconstructed as {125, 100, 75, 63, 63} — wrong at three of five β. The
2916 pin arrived (founder mechanical apply) before any leg ran at a
wrong window; the eight legs already banked (β = 0.04 and the β = 0.20
calibration) used windows identical under both readings. The audit's
lesson — *freeze literals, not rules* — is hereby confirmed in live
fire within one session of being written.

## §2 — COLLAPSE GATE (CORRECTED FORM, FRESH DATA ONLY)

Aggregation: per β, ensemble-over-12-legs weighted means with
leg-to-leg standard errors (the honest noise under the 2908 chaos
result); all 72 bins clear the ≥200-sample floor. Gate: per β,
χ²/dof of p_x/β against the leave-one-out β-pooled linear pattern
(`code/2917_round2_analysis.py`):

| β | 0.04 | 0.07 | 0.10 | 0.14 | 0.20 |
|---|---|---|---|---|---|
| χ²/dof | 2.96 | 1.59 | 1.86 | 1.42 | 2.13 |

**FAIL at 4/5** (frozen bar 1.5). Round 1's χ² ≈ 0.4–1.0 was
consistency-with-linearity *at 18-leg noise*; at 60-leg noise the
β-structure is real and resolved. Stage 2 therefore runs under the
mandatory β³-modelled branch, exactly as frozen.

## §3 — STAGE 2 (β³ BRANCH): INCONCLUSIVE AS FROZEN

Identical machinery to 2914 Stage 2; only frozen changes applied
(five-β (β, β³) per-bin fit, 3 dof; fresh input)
(`code/2917_stage2_round2.py`, archive
`data/2917_stage2_round2_c_hyb.json`):

- k_h = +1.198e-2 (bootstrap +1.215e-2 ± 0.14e-2)
- c_hyb = +19.66 (bootstrap median +19.73, **σ_c = 2.11**, 16–84%:
  +17.3 … +21.5)
- **Frozen gate σ_c ≤ 0.05: FAIL ⟹ INCONCLUSIVE. No band is claimed.**

**Unbanded cross-validation, third confirmation:** k_h = +0.0120 agrees
with round 1 (+0.0106) and the directly measured differential drive
(k_Δ ≈ +0.014, Patches 2910/2912) in sign and to ~15–25%. The
pipeline's linear plumbing is stable across rounds.

## §4 — DIAGNOSIS (POST-HOC, DISCLOSED AS SUCH; NO BAND CLAIMED)

Three unbanded diagnostics were run after the verdict
(commands preserved in `reasoning/2917.md`):

1. **The unscaled pattern amplitude is nearly β-independent.**
   Inner-ring ‖p_x‖_rms = 0.0158 / 0.0157 / 0.0171 / 0.0172 / 0.0199
   across a 5× range of β. Linear fit: amp ≈ 0.0143 + 0.0259 β — at
   β = 0.04 the constant part is **~14× the motion-proportional part**.
2. Consequently ‖p_x/β‖ falls ~4× with β (0.395 → 0.100 inner ring) —
   the "collapse" tested by every gate to date cannot hold, and its
   failure is *structural*, not noisy.
3. The (β, β³) basis contains no β⁰ term, so the constant core projects
   onto β·p₁ with ~1/β weighting and manufactures enormous spurious
   curvature. A low-β restricted fit moves c from +19.7 to +11.4 —
   monotone dependence on the fit range is the signature of a
   mis-specified basis, not of a physical c.

**Reinterpretation flag for Round 1 (correction candidate, not yet a
correction):** the 2914 headline "disparity at amplitude ~0.4β (inner
ring)" is numerically indistinguishable from a *constant* amplitude
~0.016 read at β = 0.05. Whether the imaged fore/aft wave is
motion-proportional at all is now an open measurement question. The
sign observation (positive aft / negative fore) stands as an
observation; its β-scaling attribution does not.

**Candidate identifications for the β⁰ core (to be discriminated, not
assumed):** (a) static induction — the source charge polarizes the Sea
axially fore/aft regardless of motion; naive sign analysis gives
positive FORE for static induction, i.e. *opposite* the measured
orientation, which if it survives scrutiny rules (a) out or reveals a
sign convention error to be audited; (b) an equilibration transient
from the radial-dipole initial condition, β-independent by
construction and window-diluted as ~1/T_meas; (c) a genuine
motion-locked but amplitude-saturated response. These make different,
cheap, testable predictions — §6.

## §5 — ESCALATION DISPOSITION (WORKER RULING UNDER PD-006, correctable)

The frozen escalation ladder (2914 §4) is: seeds {10–15}, **then a
conditioning re-assessment**. Ruling: the first rung is skipped as
mathematically futile and this record constitutes the second rung. A
statistics doubling improves σ_c by √2 (2.11 → ~1.5) against a
required 0.05 — a 42× gap — while every diagnostic shows σ_c is
dominated by basis mis-specification, not leg noise. Running ~45 min
of compute that cannot alter the verdict would be procedure worship;
the freeze's own design placed re-assessment on the ladder for exactly
this case. The 60 banked legs remain fully valid data for any
corrected Stage-2 model — nothing is discarded.

## §6 — WHAT'S NEXT (single pointer)

**Pre-register, then run, the β = 0 CONTROL:** static-source legs
(β = 0, source held at x = 0), seeds {4–6} × classes {A,B} × two
windows T_meas ∈ {63, 125}, identical instrumentation. Frozen
discriminating predictions (committed here, before any control leg):

- **(a) static induction:** p₀ pattern equal at both windows;
  amplitude ≈ the fitted a₀ = 0.0143 (inner ring); sign orientation
  resolves the §4(a) sign question.
- **(b) equilibration transient:** window-summed amplitude scales
  ≈ ×(63⁻¹/125⁻¹) ≈ 2.0 between windows; pattern decays in time.
- **(c) motion-locked saturation:** p₀ ≈ 0 at β = 0 (no source
  motion, no pattern).

Only after the control assigns the β⁰ core does a corrected Stage-2
basis (p = p₀ + βp₁ + β³p₃, with p₀ measured) get pre-registered with
fresh bands — the c_hyb bands of 2913 §3 judge a quantity the current
basis cannot measure, and they are NOT reinterpreted retroactively.

## §7 — STANDING

CONJ-FP-1: A HOLDS (2912), B CLOSED (2895); curvature OPEN.
Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds
DM-1/2/3; Candidate (B) 79.5% PROVISIONAL-FAVORABLE. G1, P-A2-1,
statics suspension (2892), 7 July no-carried-velocity ruling stand.
