# ROUND 3 ABORTED AT THE SYMMETRY GATE — THE ZBW SEA IS CHAOTIC, AND WHAT THAT MEANS FOR THE PROGRAMME

**Patch 2908. The round-3 gate (`mobile_sea_round3_prereg.md`) fired
exactly as frozen: no moving leg was run or read.**

---

## §1 — GATE RESULT

Frozen β = 0 legs: class A −2.4×10⁻¹⁶, class B −2.4×10⁻¹⁷ — the
mirror-symmetrised construction is EXACTLY symmetric. **Mobile β = 0
leg: +8.4×10⁻⁴ ≫ 10⁻¹². GATE FAIL ⟹ ROUND ABORTED** before any β > 0
leg existed.

## §2 — DIAGNOSIS: DETERMINISTIC CHAOS (measured)

Twin-run diagnostic (`reasoning/2908.md` for code inline; single-CP
perturbation 10⁻¹²):

- Symmetric run |D(t)|: 2.4×10⁻¹⁶ (t=0) → 9.9×10⁻¹³ (t=20) →
  1.5×10⁻⁵ (t=40) → saturation at the chatter level ~10⁻³ by t≈50.
- Twin divergence: max position difference 10⁻¹² → O(1) by t≈50.
- **Lyapunov-like rate λ ≈ 0.56/Moment (e-folding 1.8 Moments).**

The ZBW pair oscillation (the step-cap nonlinearity plus pass-through
dynamics) is strongly chaotic. Machine-epsilon seeds reach the chatter
amplitude in ~30 e-foldings ≈ 53 Moments — matching the observed onset.
**The round-3 premise (symmetry-protected zero floor for the mobile leg)
is physically impossible in this system.** Two corollaries, one bad, one
good: no exact-cancellation design can beat the chatter; and the chatter
is genuinely self-randomising, so ensemble averaging is fully legitimate
and the per-window statistics behave as ~T/τ independent samples with
τ ≈ 3 Moments (this retroactively explains every SE observed in rounds
1–2).

## §3 — THE POWER WALL, STATED WITHOUT FLINCHING

With response ~1×10⁻³ and chaotic chatter 6–9×10⁻³ per Moment:

- **Condition A (SIGN of the response):** needs SE ≈ 0.3×10⁻³ per β ⟹
  ~1200 measurement-Moments per β — **about 2–3× the data already
  taken. FEASIBLE.** (Standing suggestive tally: 13 of 15 differential
  values positive, pooled +1.05 ± 0.40 ×10⁻³.)
- **The curvature c_sub (the actual B1 question):** the curvature
  modifies the drive by cβ² ≤ 0.8% of a 10⁻³ signal ⟹ per-point SE
  ~2×10⁻⁶ ⟹ **~10⁷–10⁸ measurement-Moments. INFEASIBLE by 3–4 orders
  of magnitude in this environment, at this configuration, by direct
  drive measurement.** None of rounds 1–3 was ever within reach of the
  curvature bands; recording this is the honest close-out of that hope.

## §4 — RESTRUCTURED PROGRAMME (worker decision under PD-006)

1. **SIGN ROUND (near-term, cheap):** one pre-registered round with
   SIGN-ONLY bands (Condition A verdict at 3σ pooled), ensemble sized by
   the §3 arithmetic, explicitly renouncing curvature bands. Settles
   CONJ-FP-1 Condition A on the substrate.
2. **HYBRID PIPELINE (the curvature route):** the Patch-2901 division of
   labour, now forced rather than preferred: use the substrate engine to
   measure the Sea's ENTRAINMENT RESPONSE FUNCTION (an integrated,
   all-pairs observable with √N_pairs ≈ 30× chatter suppression, plus
   ensemble gain), then compute the dressed drive's curvature
   ANALYTICALLY from the measured response via the 2900-class retarded
   integral — deterministic, chatter-free. The curvature question moves
   from an impossible direct measurement to a two-stage computation in
   which each stage is high-SNR.
3. Boosted-coupling runs (source charge ≫ 1, SNR ∝ Q_s) are retained as
   a cross-check only, pending regime checks (strong sources drive the
   Sea nonperturbatively).

## §5 — STANDING

Round-3 curvature bands: never engaged (aborted pre-read). CONJ-FP-1
Condition A OPEN pending the sign round; B CLOSED per 2895. Ledger
untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds; Candidate (B)
79.5%. G1, P-A2-1, statics suspension, 7 July ruling stand.
