# EXECUTION RECORD — HYBRID ROUND 3: ADEQUACY GATE PASSES (THE BASIS IS RIGHT), VERDICT INCONCLUSIVE AS FROZEN — AND THE FROZEN SYMMETRY ASSERT UNCOVERS A PARITY DEFECT IN THE SHARED STAGE-2 EVALUATOR, PRESENT SINCE 2914

**Patch 2920. Executed against the FROZEN prereg of Patch 2919
(`code/2920_round3_execution.py`, archive
`data/2920_round3_results.json`). Inputs: the 72 banked legs only.**

## §1 — FROZEN RESULTS

- **Model-adequacy gate: PASS** — χ²/dof = 1.419 (< 1.5) over 57
  admitted bins × 3 dof. The corrected four-component basis
  p₀ + p_tr/T + βp₁ + β³p₃ fits the substrate output. The round-2
  basis indictment (2917 §4) is thereby confirmed constructively.
- **Frozen mirror-symmetry assert: FAIL** — D₀(0) = +4.65e-4, not 0.
  The computation was completed with the assert recorded rather than
  aborted (mechanical necessity; disclosed here, not softened).
- Central values: k₀ = +6.09e-3, c₀ = +14.2; k₁ = +1.15e-2;
  k_tot = +1.76e-2, c_tot = +16.6.
- Bootstrap: σ_{c₀} = 25.7, σ_{c_tot} = 2.87.
- **VERDICT (frozen bands): STATIC-SEA INCONCLUSIVE (σ) |
  TOTAL INCONCLUSIVE (σ).** No band is claimed.
- Sanity register: (ii) **p₀ vs control corr +0.676, amp ratio 1.14 —
  BOTH PASS**, the fitted core is the control's pattern; (i) k₀+k₁ =
  +0.0176, above the +0.011..0.014 register; (iii) p_tr
  odd-dominant, register expected even — (i) and (iii) misses are
  consistent with the §2 defect and are not explained away here.

## §2 — THE DEFECT THE ASSERT CAUGHT (audited to root cause)

Post-verdict diagnostics, disclosed as such:

1. Odd-projecting the fitted p₀ (exact by construction) still gives
   D₀(0) = +2.2e-4. So the asymmetry is not (only) noise in p₀ — it
   is in the evaluator.
2. **Kernel parity audit: CLEAN.** An exact mirror dipole pair sums
   to +0.00e+00 axial force. The kernel is not the defect.
3. **Root cause, proven:** the pattern lookup
   `digitize(ξ_ret, XB) − 1` assigns edge-landing cells
   asymmetrically: cells at x = ±5.0 read the pattern at −4.5 / +5.5
   respectively; the x = 0 column reads +0.5. Cell columns at
   0, ±5.0, ±10.0 (integer bin edges) all break mirror cancellation.
   **This defect is in the SHARED Stage-2 machinery inherited
   unchanged from 2914** — it contaminated rounds 1, 2, and 3, hiding
   inside the ~25% slack of the k_h cross-validation. Artifact scale
   ~2–5e-4 against drives of ~1e-3–1e-2: material for curvature,
   subdominant for sign — no sign-level result of the arc is
   endangered, and the round-2 basis indictment stands independently
   (it was made from Stage-1 amplitudes, not the evaluator).
4. Failure-mode ledger, sixth instance, same genus: *inheriting from
   the arc rather than the spec* — "machinery of 2914 unchanged" was
   treated as a virtue and froze a defect in. The catch mechanism
   was, again, two of the worker's own numbers disagreeing (an exact
   analytic zero vs +2.2e-4) — this time PRE-REGISTERED as an assert,
   which is why round 3 caught in one turn what three rounds missed.

## §3 — DISPOSITION

Round 3 stands as INCONCLUSIVE under its frozen terms. The evaluator
defect is a demonstrated internal contradiction, so per the 2914
precedent (defective instrument retired WITH disclosure, corrected
instrument pre-registered before judging), the fix — symmetric
linear interpolation of the pattern at ξ_ret, plus odd-projection of
the p₀ channel — is pre-registered at Patch 2921 (Round 3b) and only
that prereg's bands may be judged by it. Nothing about the data,
basis, gate, or bands changes.

## §4 — STANDING

Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds
DM-1/2/3; Candidate (B) 79.5%. G1, P-A2-1, statics suspension, 7 July
ruling stand. CONJ-FP-1: A HOLDS, B CLOSED, curvature OPEN.
Anti-screening question OPEN (2918).
