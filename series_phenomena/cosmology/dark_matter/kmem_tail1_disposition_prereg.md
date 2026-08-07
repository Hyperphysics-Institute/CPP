# OPEN-KMEM-TAIL-1 — TAIL-DISPOSITION SUPPLEMENTARY PREREGISTRATION — FROZEN — Patch 3024

**Status: FROZEN AT COMMIT. No analysis code exists for this document
at freeze time** (the 2967/2981 discipline). **Execution is gated on
FLASH SANCTION by the five-seat panel**
(`conv013_2026-08_flash_tail_prereg_sanction_dispatch.md`, this patch);
if any seat's sanction return is AMEND and the amendment is adopted,
this document re-freezes as v1.1 before any code is written. Evidentiary
standing of any result: NONE until executed under the sanctioned frozen
terms and panel-adjudicated. **No retune of anything, anywhere:** every
constant below is either carried unchanged from the frozen 2981/2983
terms or frozen HERE before any look.

**What this dispositions.** The CONV-013 completion adjudication
(Patch 3023) enacted the MEAS-2 result as FALSIFIER-CANDIDATE UNDER
MANDATORY DISPOSITION: the tail statistic is significant (1.570e-3,
scale 2.805e-5) while the domain discriminator (2.080) reads ballistic
and D̄ was not detected — a triple satisfying no frozen 2981 §3 branch
(the registered coverage gap). This prereg supplies the disposition:
**is the low-frequency PSD excess a transient/support artifact of the
frozen analysis construction, or genuine long-time memory?** It also
audits the D̄ non-detection anomaly (measured ~100× below the 2918
motion-response scale the power analysis assumed). **DATA SCOPE: the
committed `data/kmem2/` ONLY (Route A). No new runs under this
document.** The candidate artifact mechanism under test, stated for
falsifiability: the frozen 2983 PSD is computed on F[T_STEP:], which
INCLUDES the ballistic transient window (support ≤ d_DP/c, T_BALL = 36
Moments); a step-vs-control transient difference leaks power into the
low-frequency band and is not memory.

## §1 — Frozen constants

Carried unchanged from 2981/2983: T_STEP = 24, T_BALL = 36,
T_END = 240, band (0, 0.6·ω_N], tail fraction ntail = max(3, nb//10),
significance construction |tail| > 2.576 × std(pc[:ntail])/√n,
block-bootstrap CHUNK = 8 pairs, NBOOT = 10000, exclusion set = the
executed run's (empty). Frozen HERE: bootstrap seed **30241001**
(analysis-level constant, this document); T-C window-fraction set
{nb//12, nb//10, nb//8}; T-B CI level 99% percentile.

## §2 — Discriminants (all four run; none optional)

- **T-A (transient exclusion — PRIMARY):** recompute the 2983 tail
  statistic identically except the PSD input is F[T_STEP + T_BALL:]
  (ballistic window excluded) instead of F[T_STEP:]. Classes:
  T-A-ZERO (excess consistent with zero under the frozen
  construction) / T-A-SIG (remains significant).
- **T-B (domain scaling of the TAIL itself):** compute the 2983 tail
  statistic (original F[T_STEP:] windows) separately on the 128
  matched dom pairs and their 128 std counterparts; ratio
  R_tail = tail_dom / tail_std with block-bootstrap 99% percentile CI
  over pairs (chunks of 8 → 16 chunks, NBOOT, seed 30241001). Classes:
  T-B-SUPPORT (CI excludes 1 and contains 2) / T-B-MEMORY (CI excludes
  2 and contains 1) / T-B-ND (CI contains both or neither —
  non-discriminating).
- **T-C (window robustness, qualifier):** repeat T-A at the three
  frozen tail fractions. Classes: T-C-STABLE (same significance class
  at all three) / T-C-UNSTABLE (any flip).
- **T-D (D̄-scale definitional audit; no new statistics):** derive the
  expected value of the FROZEN response statistic (early-window mean
  minus late-window mean, resp_S of 2983) under the 2918
  motion-response decomposition, and state whether the 2.6e-3 scale
  applies to THIS statistic or is cancelled/attenuated by the
  differencing construction. Classes: T-D-EXPECTATION-DEFECT (the
  scale does not apply as assumed; the power analysis's premise, not
  the physics, was wrong) / T-D-PHYSICS-ANOMALY (the scale applies and
  the non-detection is physical — routes to Route B, never to retune).

## §3 — Frozen total disposition mapping (exhaustive by construction)

Over {T-A-ZERO, T-A-SIG} × {T-B-SUPPORT, T-B-MEMORY, T-B-ND} with T-C
as qualifier:

1. **T-A-ZERO ∧ T-B ∈ {SUPPORT, ND} → DISP-A SUPPORT-ARTIFACT.** The
   excess is the transient leaking into the low band. The exportable
   falsifier is UNFIRED; the MEAS-2 record re-reads as
   no-memory-detected; the L-4/L-6 indictment LIFTS; OPEN-KMEM-TAIL-1
   CLOSES; the 1B promotion bar re-arms pending D-KAPPA and a fresh
   promotion round.
2. **T-A-SIG ∧ T-B-MEMORY ∧ T-C-STABLE → DISP-B MEMORY-CONFIRMED.**
   The registered exportable falsifier FIRES: T-3 §6 + B-1 L-4 + L-6
   are contradicted; charter revision/HALT routing to the panel; the
   worker does not soften this branch.
3. **T-A-SIG ∧ (T-B ∈ {SUPPORT, ND} ∨ T-C-UNSTABLE) → DISP-C MIXED.**
   Existing data cannot disposition; **Route B activates**: an
   extended-control re-run (longer legs and/or additional domain
   scalings, per the CONV-013 [COP] Q5 item 3) under its OWN fresh
   frozen preregistration; the falsifier is neither fired nor retired.
4. **T-A-ZERO ∧ T-B-MEMORY → DISP-C MIXED** (conflict class; Route B).

T-D reports alongside whichever DISP class fires and never modifies
it; T-D-PHYSICS-ANOMALY co-routes to Route B.

## §4 — Execution and integrity protocol

Analysis code committed AFTER sanction, citing this document; single
script; branch semantics printed in §3 language only; verbatim stdout
into the execution record; standing NONE until the panel adjudicates
the record (a flash adjudication suffices if the class is DISP-A or
DISP-B unanimous-on-the-record; DISP-C convenes ordinary
adjudication). **Ledger untouched by this prereg:** 1B OPEN (HOLD,
CONV-013 final); six of seven; PR7 PARTIAL; B7; Candidate (B) 79.5%;
2855 PROVISIONAL; d_DP ceiling ACTIVE. Nothing here computes any value
of ξ₂, ζ, η, d_DP, n_DP, or N.
