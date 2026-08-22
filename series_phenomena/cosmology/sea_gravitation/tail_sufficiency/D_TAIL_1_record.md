# **D-TAIL-1: VARIANCE IS NOT A SUFFICIENT DESCRIPTION OF THE DRIVE.** Verdict **TAIL-SENSITIVE** on a power-gated instrument (control separated at 29.8 SE): at IDENTICAL variance, changing only the drive's tail structure moves f_b by **7.8 SE**, ρ_swap by **12.6 SE**, and **f_dwell by 41.7 SE** — while the SHORT-tailed (uniform) drive is indistinguishable from Gaussian at 0.9–1.9 SE, so the Sea responds to **heavy tails specifically, not to non-Gaussianity in general**; **every instrument in this corpus specifies its drive by σ alone, and that specification is now known to be incomplete** — and since the Sea's own force series is intrinsically intermittent (3183) while every surrogate is Gaussian, our instruments have been driving with the one tail structure the Sea does not natively have

**Patch 3193 (22 Aug 2026). Executes `D_TAIL_1_prereg.md` (Patch 3192,
committed BEFORE this ran). Container.**

## §1 — Power gate, then the measurement

Control G(σ = 0.30) vs G(σ = 0.45): f_b = 0.44479 ± 0.00092 vs
0.40608 ± 0.00092 ⇒ **29.8 SE, PASS.** f_b can see drive changes;
nothing below is a blind statistic.

Matched-variance drives (measured σ printed, all 0.3000–0.3005):

| drive | measured kurtosis | f_b | Δ vs G |
|---|---|---|---|
| G (Gaussian) | +0.00 | 0.44479 ± 0.00092 | — |
| S2 (2% bursts) | +143.9 | 0.44252 ± 0.00025 | 2.4 SE |
| S05 (0.5% bursts) | +56.6 | 0.43692 ± 0.00041 | **7.8 SE** |
| U (uniform, short tails) | −1.20 | 0.44583 ± 0.00060 | 0.9 SE |

**Secondary statistics, reported per §4 and far more sensitive:**

| pair | f_dwell | ρ_swap |
|---|---|---|
| G vs S2 | +0.0177 (**41.7 SE**) | −0.0126 (12.6 SE) |
| G vs S05 | +0.0098 (19.6 SE) | −0.0119 (9.5 SE) |
| G vs U | −0.0011 (1.9 SE) | +0.0027 (1.1 SE) |

**VERDICT (frozen words): TAIL-SENSITIVE.**

## §2 — The worker's expectation, scored

§5 pre-declared **VARIANCE-SUFFICIENT**, reasoned from the Sea's known
indifference to drive magnitude. **SCORED WRONG.** Fifth consecutive
pre-declaration not confirmed as stated — and this one was wrong in
the direction that FAVOURS the founder's picture, having been recorded
explicitly as running against it. All five stand in the record.

## §3 — What the pattern says (structure, not just a verdict)

1. **The response is to HEAVY tails, not to non-Gaussianity.** The
   uniform drive — as non-Gaussian as S2 in its own way, but
   SHORT-tailed — is indistinguishable from Gaussian on every
   statistic. The Sea notices rare large kicks; it does not notice
   the absence of them. The prereg included U precisely so this
   asymmetry could appear, and it did.
2. **The effect is NOT monotone in kurtosis on f_b** (S2 has 2.5×
   S05's measured kurtosis but a third of the separation), while it
   IS monotone on f_dwell. So kurtosis is not the controlling
   variable; burst RATE and burst AMPLITUDE enter differently.
   **Recorded as an observation; no mechanism adopted.**
3. **Direction, offered as HYPOTHESIS only:** bursty forcing raises
   dwell and lowers swap rate — rare impulses displace a partner
   sharply but briefly, whereas continuous jostling at the same
   variance sustains the proximity that partner exchange requires.
   Untested; falsifier not designed here.

## §4 — Consequences (the reason this matters beyond one campaign)

- **Corpus-wide:** σ_n alone does not specify a drive. Two
  instruments agreeing on σ may be driving the Sea differently, and
  every past comparison assuming otherwise carries an unquantified
  exposure. **Flagged, not costed — quantifying it requires knowing
  each instrument's actual tail structure.**
- **The founder's DM diagnosis (3177 §2.3) has its MECHANISM
  supported:** intermittent and smooth driving DO give materially
  different statistics at matched variance, in this Sea, measured.
  **This is not a DM finding** — it is the mechanism's premise, and
  the DM claim needs its own instrument and freeze.
- **D-JITTER-1 is partially REINSTATED — a second time, and in a
  third role.** 3181 refuted the MAGNITUDE premise (d_s^emp
  insensitive to σ_n); 3184 rehabilitated it for tail FIDELITY; this
  patch shows the Sea's equilibrium observables respond to tail
  SHAPE at fixed variance. **The open question this makes sharp and
  cheap: does d_s^emp itself shift under matched-variance tail
  changes?** If it does, the calibration inherits a dependence nobody
  has measured. **Not run here; it needs its own freeze, and it is
  the obvious next experiment.**

## §5 — Honest limits

Two seeds per cell, not four — the four-seed design exceeded the
container's wall clock, and the reduction is recorded rather than
hidden. Every SE above is computed from the seeds actually run, so
the frozen 3-SE thresholds were applied at the achieved precision,
not an assumed one. The measured kurtosis of S05 (+56.6) falls well
below its analytic value (~597), the known downward bias of
fourth-moment estimators on heavy tails at finite sample — which is
itself a reminder of the CONV-022 lesson and why f_dwell, a
first-moment quantity, carries the strongest signal here.
