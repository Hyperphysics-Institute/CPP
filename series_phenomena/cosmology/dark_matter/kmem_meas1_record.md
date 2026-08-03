# K-MEM-MEAS-1 — EXECUTION RECORD: UNRESOLVED-BY-FLOOR (frozen reading, applied as-is)

**Patch 2968 (3 Aug 2026). Executes the 2967 preregistration verbatim
on the committed 2902 mobile-Sea engine. All three legs ran to
completion; the frozen §5 floor clause fired; no branch reading is
made; no threshold was retuned. Assumptions carried: PROTOCOL-D1
(2960); PRINCIPLE-R1 (RATIFIED 2963; distinct from K-MEM =
OPEN-K1-MEMORY-1B).**

## §1 — EXECUTION

Driver `code/2968_kmem_step_driver.py` (checkpointed, leg-atomic);
analysis `code/2968_kmem_analysis.py` (prereg §4/§5 verbatim); raw
traces archived at `data/2968_kmem_{L1,L2,L3}.json`. One driver-path
fix (engine relative path, no physics content) made before any leg
ran; disclosed. Legs: L1 (step 0→0.10, standard domain, 240 Moments,
937 CPs), L2 (no-step control, 144 Moments), L3 (domain-scaling leg,
186 Moments, 361 CPs). All complete; checkpoint/resume exercised
(L1 across three calls, bit-exact resume).

## §2 — FROZEN STATISTICS (data as-is)

- **L2 control:** sigma_ctrl = 3.93e-3; static-pattern offset
  F_stat = +8.96e-4 (the 2918 persistent-core analogue, present as
  expected).
- **L1:** F_0 = +9.25e-3, F_inf = +2.27e-3, S = 6.99e-3,
  thr = max(0.10·S, 3σ) = 1.18e-2, t_settle = 198 (T_ball = 36),
  r_tail = 1.20e-2.
- **L3:** F_0 = −5.26e-3, F_inf = −7.21e-4, S = 4.54e-3,
  thr = 1.18e-2, t_settle = 66 (T_ball = 27), r_tail = 6.54e-3.

## §3 — FROZEN READING

**S < 3·sigma_ctrl in BOTH step legs → UNRESOLVED-BY-FLOOR.** Per
the preregistration: reported, no branch fired, no retuning inside
this preregistration. The apparent F_0 values themselves sit at the
chatter scale — the "step" statistics above are floor-dominated and
carry no kernel information; they are printed because the prereg
requires the statistics computed on the data as-is, not because they
mean anything.

## §4 — WHAT WAS LEARNED (registered, claim-free)

1. **The floor is now measured:** sigma_ctrl = 3.93e-3 per-Moment
   axial-force chatter on the standard geometry — consistent with the
   2908 deterministic-chaos finding and the 2918 decomposition (true
   motion response ~0.026·β ≈ 2.6e-3 at β = 0.10, i.e. BELOW the
   single-leg floor by design of nature, not of the prereg).
2. **The instrument path works end-to-end:** step sequencing on the
   committed engine, causal History pre-fill, checkpointed resume,
   frozen-analysis pipeline — all exercised and archived.
3. **The follow-on is ensemble design, and it is NOT executed here:**
   the 2908 adjudicated position ("ensembles thereby fully
   legitimised") licenses a seed-ensemble step measurement
   (per-seed paired step/no-step legs, ensemble-averaged transient);
   the required fresh preregistration must freeze ensemble size,
   pairing rule, and the same branch semantics. Any such run is a NEW
   preregistration per 2967 §5's no-retune clause.

## §5 — DISPOSITION

This record joins the combined CONV-011 package (T-1/T-2/T-3 +
E-1/E-2 + the 2951 roadblock item + PR2 verdict ambiguity) as a
REGISTERED MEASUREMENT with an UNRESOLVED reading — evidentiary
weight, if any, is the panel's to assign (Darwin-precedent treatment,
2874 §5). The T-3 §6 prediction (Markovian-plus-stiffness at d_DP)
remains UNTESTED at instrument grade: neither supported nor damaged
by a floor-limited run, and the exportable falsifier stands exactly
as registered.

## §6 — LEDGER

Nothing moves: six of seven; PR7 PARTIAL (1B OPEN); B7 holds DM-1/
DM-3 banners; Candidate (B) 79.5%; 2855 PROVISIONAL; d_DP ceiling
ACTIVE. No value of any open quantity was minted; all quantities
above are toy-instrument statistics in engine units.
