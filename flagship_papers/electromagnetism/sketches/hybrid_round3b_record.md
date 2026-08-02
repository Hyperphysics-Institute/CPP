# EXECUTION RECORD — HYBRID ROUND 3b: PARITY-CLEAN INSTRUMENT, k_tot LANDS IN THE VALIDATED BAND, AND THE MEASURED DRIVE TURNS OVER AT β ≈ 0.15 — VERDICT INCONCLUSIVE AS FROZEN, WITH A 2σ CROSS-INSTRUMENT TENSION AND A SIGN-LEVEL DISCRIMINATOR REGISTERED

**Patch 2922. Executed against the FROZEN prereg of Patch 2921
(`code/2922_round3b_execution.py`, archive
`data/2922_round3b_results.json`). Same 72 banked legs; no new data.**

## §1 — FROZEN RESULTS

- Evaluator parity assert (abort-grade): **PASS at 4.3e-19.**
- Adequacy gate (inherited): PASS, χ²/dof = 1.419.
- **k_tot = +1.20e-2 ± 0.16e-2 — inside the thrice-validated
  +0.011..0.014 register.** Sanity (i), which failed under the
  defective evaluator (+0.0176), passes clean: the 2920 excess was
  the parity artifact. Sanity (ii) unchanged (corr 0.68, amp 1.14).
- c₀ = +11.6, σ = 7.2; c_tot = +16.0, σ = 3.4 (16–84%:
  +12.5 .. +19.1). Even residue of p₀ (noise gauge): 0.0091 rms.
- **VERDICT (frozen bands): STATIC-SEA INCONCLUSIVE (σ) |
  TOTAL INCONCLUSIVE (σ).** No band is claimed.

## §2 — WHAT THE INSTRUMENT NOW SHOWS (disclosed diagnostics)

The non-perturbative drive shape, computed from the fitted channels:
D_tot rises to a **maximum at β ≈ 0.15** and collapses toward zero by
β ≈ 0.24 — the turnover position matches the perturbative fit's own
prediction 1/√(3c) = 0.142. Within the perturbative parametrization,
c_tot ≠ 0 at ~4.7σ and c_tot ∉ [0.10, 0.30] at ~4.6σ. The σ ≤ 0.05
absolute bar, set for c = O(0.2), is dimensionally unreachable at
c = O(16) (it demands 0.3% relative precision); the 2921 §4
commitment therefore engages in substance: **the perturbative form is
declared inadequate on β ∈ [0.04, 0.20]**, and the successor question
is the drive's shape, led by its turnover.

## §3 — CROSS-INSTRUMENT CHECK (2910 direct data; disclosed, unbanded)

The direct differential drives (sign round, archived, untouched by
this pipeline): D/β = {12.0 ± 2.7, 15.2 ± 2.7, 13.8 ± 2.4}e-3 at
β = {0.05, 0.1, 0.2}. Agreement with the hybrid: sign, linear scale
(the register band both now occupy). Tension: the direct drive nearly
DOUBLES from β = 0.1 to 0.2, while the hybrid's shape has flattened
there — c_direct ≈ 3 (weakly constrained) vs c_hyb ≈ 16, ~2σ apart.
Two instruments, same substrate, different turnover locations: one of
them is misreading the high-β regime, and β ≤ 0.2 data cannot say
which.

## §4 — THE REGISTERED DISCRIMINATOR

At β = {0.25, 0.30} the two readings separate at SIGN level: the
hybrid fit predicts D(0.25) ≈ +0.4e-3 (falling) and
**D(0.30) ≈ −1.6e-3 (past turnover, drag)**; the direct trend
predicts **≥ +3e-3 (still strongly forward)**. A sign-level split is
robust to every calibration subtlety that plagued this arc.
Pre-registered as the TURNOVER TEST at Patch 2923.

## §5 — STANDING

Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds
DM-1/2/3; Candidate (B) 79.5%. G1, P-A2-1, statics suspension, 7 July
ruling stand. CONJ-FP-1: A HOLDS, B CLOSED; curvature: perturbative
form inadequate (this patch), shape question OPEN. Anti-screening
OPEN (2918).
