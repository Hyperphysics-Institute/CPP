# OPEN-KMEM-TAIL-1 — DISPOSITION EXECUTION RECORD — Patch 3026

**Executed 7 Aug 2026 under the FROZEN terms of
`kmem_tail1_disposition_prereg.md` (Patch 3024 §1–§3, untouched; gate
as amended Patch 3025 on the founder's economy challenge). Script
`code/3026_kmem_tail1_disposition.py` run VERBATIM, exit 0, against the
committed `data/kmem2` (commit c9b92835). Evidentiary standing: NONE
until panel-adjudicated. Per the Patch 3025 economy ruling and the §3
outcome below, NO panel round convenes on this record: DISP-C is
neither a win nor an impasse — the frozen mapping prescribes Route B,
and the single panel round (design + result together) convenes when
the disposition RESOLVES.**

## §1 — Verbatim stdout

```
pairs used 512/512; engine-fault exclusions: none
T-A transient-exclusion tail (PSD on F[60:], nb=54, ntail=5): tail = 1.576e-03 (scale 2.412e-05) -> T-A-SIG
    [reference: original-window tail (F[24:], nb=64, ntail=6) = 1.570e-03 (scale 2.805e-05) -> SIGNIFICANT]
    [T-B leg lengths: dom F -> 108 bins, std F -> 108 bins; per-subset windows per §2]
T-B tails: dom = -1.712e-03 (ntail=6), matched std = 2.268e-03 (ntail=6); R_tail = -0.755
T-B bootstrap (matched resampling, 16 chunks x 8, NBOOT=10000, seed 30241001): R_tail 99% CI [-4.133, 0.741] -> T-B-ND
T-C ntail=4: tail = 1.680e-03 (scale 2.315e-05) -> SIGNIFICANT
T-C ntail=5: tail = 1.576e-03 (scale 2.412e-05) -> SIGNIFICANT
T-C ntail=6: tail = 1.449e-03 (scale 2.476e-05) -> SIGNIFICANT
T-C -> T-C-STABLE
T-D audit (derivation from the frozen texts; no new data statistics):
  (1) The 2918 scale 0.026*beta = 2.6e-3 is defined in the MEAS-1 record §4.1 as the SUSTAINED motion response.
  (2) MEAS-1's statistic S = |F_inf - F_0| used F_0 = PRE-step window — sensitive to a sustained shift.
  (3) MEAS-2's frozen resp_S = mean(F[60:100]) - mean(F[200:240]) uses two POST-step windows — a sustained shift cancels EXACTLY; only decay BETWEEN the windows registers.
  (4) The theory's own prediction (finite support, settle within T_BALL = 36 < 60) is early = late, i.e. D_bar = 0 PREDICTED.
  (5) The 2981 power computation applied the sustained scale to a statistic structurally blind to it; the survival-to-window premise was never derived and contradicts (4).
  -> T-D-EXPECTATION-DEFECT: the scale does not apply as assumed; the observed D_bar = -2.8e-5 ~ 0 is CONSISTENT with the no-memory prediction, not anomalous. Routing per §2: not to Route B, never to retune.
----------------------------------------------------------------------
DISPOSITION (T-A-SIG ∧ T-B-ND ∧ T-C-STABLE): DISP-C MIXED — existing data cannot disposition; Route B activates: extended-control re-run under its own fresh frozen preregistration; the falsifier is neither fired nor retired.
Evidentiary standing: NONE until panel-adjudicated (prereg §4, gate as amended Patch 3025).
```

## §2 — Enacted outcome (frozen §3 language)

**DISP-C MIXED.** Route B activates: an extended-control re-run under
its OWN fresh frozen preregistration. The registered exportable
falsifier is neither fired nor retired; T-3 §6 / B-1 L-4 / L-6 remain
INDICTED-PENDING-DISPOSITION; the 1B ledger line is untouched (HOLD,
CONV-013 final). The worker enacts the frozen class exactly and does
not substitute a post-hoc reading.

## §3 — Facts of record (derivable from the frozen constructions; stated
without interpretive upgrade — weight is the panel's to assign at the
eventual round)

1. **The transient-leakage artifact hypothesis, stated falsifiably in
   the prereg, is FALSIFIED:** the tail survives ballistic-window
   exclusion essentially unchanged (1.576e-3 vs 1.570e-3) and is
   window-robust (T-C-STABLE). The low-frequency excess is real
   structure in the post-transient data, not the step transient.
2. **The tail INVERTS SIGN in the doubled domain** (std +2.268e-3 →
   dom −1.712e-3 on matched pairs). The pre-registered 99% CI on
   R_tail, [−4.133, 0.741], **excludes R = 1 (domain-independent
   memory-type) AND excludes R = 2 (ballistic box-scaling)** — both
   pre-registered alternatives are rejected by the pre-registered
   construction. The frozen class for excludes-both is T-B-ND, hence
   DISP-C. (Noted as fact, not enacted: a physical long-time memory
   kernel cannot flip sign with box size.)
3. **T-D corollary:** the 2983 domain discriminator (the 2.080 that
   CONV-013's Q3 debate centered on) divided two D̄'s that are both
   predicted ≈ 0 (per the T-D derivation) and measured ≈ 0 — it is a
   ratio at noise scale and carries no inferential weight. The tail's
   own domain scaling (T-B) is the informative discriminator.
4. **The D̄ non-detection anomaly DISSOLVES** as
   T-D-EXPECTATION-DEFECT (full chain in the stdout): the 2918 scale
   is the sustained response; the MEAS-2 statistic is post-vs-post and
   provably blind to sustained components; D̄ ≈ 0 was the theory's own
   prediction. This also explains the 2981 branch-coverage gap:
   branch 1's "D̄ detected" clause was inherited from the pre-vs-post
   statistic era and became unsatisfiable under the changed statistic.
5. Frequency-resolution note for Route B: at T_END = 240 the tail
   window is the lowest 4–6 PSD bins (periods ≈ 36–216 Moments); leg
   length directly sets low-frequency resolution.

## §4 — Route B design guidance (paid for by this record; freezes in
the Route B prereg, NOT here)

≥3 domain sizes (the sign inversion predicts structure in
tail-vs-box); longer legs (low-frequency resolution); paired design
retained; pre-committed effort bound + kill condition per WORKFLOW
rule 3(i) written before work starts; compute is founder hardware —
design freeze awaits the founder's resource green-light (PD-006).

## §5 — Ledger

Untouched: 1B OPEN (HOLD final); six of seven; PR7 PARTIAL; B7; 79.5%;
2855 PROVISIONAL; d_DP ceiling ACTIVE; W-MULTILINK-1 watching. Nothing
here computes any value of ξ₂, ζ, η, d_DP, n_DP, or N.
