# PREREGISTRATION — K-MEM ROUTE C (THE CORRECTED-INSTRUMENT CAMPAIGN): THE FROZEN MINORITY DESIGN CLASS INSTANTIATED; ISOLATION + MARGIN IN ONE CAMPAIGN

**Patch 3053 (10 Aug 2026). Executes the CONV-017 adjudication's
frozen Route C design class (Patch 3050 §1: GPT+DeepSeek convergent
design, armed by the ratified R3 at the Patch 3052 G1 FAIL) plus the
3052-derived resolvability requirement. FROZEN at this patch: the arm
structure (ΔT targets + geometric distinctness), the calibration and
pilot protocol, the drive ladder, the leg counts, every statistic,
and the total disposition tree. Deliberately DELEGATED to the
pre-launch calibration step (and disclosed as such): the raw
coordinates (x_src0 per arm) realizing the frozen ΔT targets, to be
computed from the ENGINE's own kinematics rather than from a possibly
misread convention — the design is frozen in the measured quantities,
not in coordinates this prereg cannot independently verify. Sequence:
this prereg → driver + frozen analysis committed (next patch) →
calibration → pilot → launch (founder mechanical, Kila6) → single
adjudication round on completion (no interim looks).**

---

## §1 — Design variables and the confound being broken

Two clocks: **T_exit** (the Moment the source leaves the measurement
domain — determined by source start x_src0, source kinematics, and
x_half) and **T_BALL** (the ballistic/post-transient window —
determined by x_half alone; empirically 1.5·x_half at x=24). Routes
A/B confounded them (the artifact domain had T_exit = t-of-T_BALL
exactly). Route C varies **ΔT ≡ T_exit − T_close** independently of
geometry, where T_close is the ballistic-window close as computed by
the frozen analysis's own windowing; the calibration step (§3)
measures both clocks per configuration from the engine before any
evidentiary leg.

## §2 — Arms (FROZEN)

| Arm | Role | ΔT target | Geometry | N_pairs |
|---|---|---|---|---|
| **A0** | DIAGNOSTIC (artifact reproduction; NON-inferential) | **0** | the Route B d24 configuration verbatim (x_half=24, x_src0=−18) | 128 |
| **A1** | INFERENTIAL | **−12** | x_half = 20 | 384 |
| **A2** | INFERENTIAL | **+8** | x_half = 24 class (the +ΔT side requires the larger domain for wall margin; calibration realizes x_src0 with start ≥ 4 units inside the boundary — a frozen constraint) | 384 |
| **A3** | INFERENTIAL | **−12** | x_half = 16 | 384 |

Design-class compliance: T_exit < T_close arm (A1, A3) ✓; T_exit >
T_close arm (A2) ✓; two geometrically distinct configurations sharing
the same ΔT (A1 at x=20, A3 at x=16, both −12) ✓; the artifact
configuration reproduced under the new instrument (A0) — the
ISOLATION the minority demanded: the boundary-mode must APPEAR at
ΔT=0 and VANISH at ΔT=±. Common frozen leg parameters: t_step = 24;
T_END = 288; late window [240, 288); annulus RHO = (1, 8); spacing
2.5; 2907 jitter convention; shared-seed pair matching (step vs ctrl
differ ONLY in the β step); master seed 30530810, per-leg seeds
derived; leg-atomic resumable writes to `data/kmemC/`.

## §3 — Calibration + pilot (pre-launch; disclosed; evidence-excluded)

1. **Kinematic calibration** (no Sea statistics): per arm, the driver
   runs the engine's source kinematics to report (T_exit, T_close)
   and tunes x_src0 to hit the frozen ΔT target within ±2 Moments;
   the realized (x_src0, T_exit, T_close, ΔT) table is committed in
   the launch log BEFORE any evidentiary leg. A0 is NOT tuned (it is
   the verbatim Route B configuration; its measured ΔT is reported
   as-is and must land within ±3 of 0, else STOP and report).
2. **Resolvability pilot** (drive sizing; 4 pairs per inferential
   arm, EXCLUDED from evidence): the systematic response must stand
   ≥ 10σ proud of the floor at full N (the 3052 lesson: β=0.1 gave
   2σ at 512 pairs). Frozen drive ladder β_f ∈ {0.6, 0.8, 1.0},
   starting at 0.6: project SNR(N=384) from the pilot; if < 10,
   escalate one rung and re-pilot; the chosen rung (one value for
   ALL arms) and the projection are committed in the launch log.
   No other parameter may move at pilot; the ladder is exhaustive —
   if 1.0 still projects < 10, STOP and report (instrument redesign,
   panel).

## §4 — Frozen statistics (per arm, computed by the frozen analysis only after the manifest is complete)

- **S3-C positive control:** the sustained-response detection of the
  Route B recipe with the band recentred on the pilot-committed drive
  (reference scale = 2.6×10⁻³ × β_f/0.1; factor-2 band). An
  inferential arm failing S3-C is PROSPECTIVELY NON-INTERPRETABLE
  (the minority's clause, verbatim) and drops from inference; A0 is
  exempt (diagnostic).
- **S1-C tail statistic:** the Route B S1 recipe unchanged (late-bin
  PSD excess vs scale; SIGNIFICANT / consistent-with-zero).
- **κ_sys:** the Patch 3051 estimator verbatim per arm, with per-arm
  t_post = t_step + T_close(arm) + 6 and late window [240, 288);
  BRANCH-FIT expected by design (resolvability); BRANCH-BOUND and
  INDETERMINATE retain their 3051 meanings; per-arm 99% CIs by
  full-pipeline pair bootstrap (NBOOT 10000; seed 30530811).
- **Isolation predicate P-ISO:** S1-C SIGNIFICANT at A0 AND S1-C
  consistent-with-zero at EVERY valid inferential arm.
- **Margin predicate P-κ:** κ_sys^{U99} < 1 in EVERY valid
  inferential arm, every arm resolving on BRANCH-FIT.

## §5 — FROZEN DISPOSITION TREE (total; evaluated in order; standing NONE until the single panel round)

1. Fewer than TWO inferential arms pass S3-C → **DISP-I2**
   (instrument again; no tail or margin standing; panel diagnoses).
2. S1-C SIGNIFICANT in ANY valid inferential arm → **DISP-T: THE
   FALSIFIER FIRES.** A domain-robust, control-valid long-time tail
   is the registered falsifier of T-3 §6 / B-1 L-4 / L-6: the
   indictment is SUSTAINED, item 1B FAILS on its named falsifier,
   and Candidate (B) fails requirement 7 (the demotion consequences
   execute per the registered falsifier text; panel confirms).
3. P-ISO true AND P-κ true → **DISP-R: RETIREMENT FINALIZED +
   MARGIN CERTIFIED.** The Q1 geometric retirement finalizes (the
   artifact experimentally isolated: present at ΔT=0, absent at
   ΔT=±); the trio's discharge finalizes; L-6b's κ_sys < 1 margin is
   certified with the per-arm values; **item 1B DISCHARGES → seven
   of seven** (panel single round confirms; ratification per the
   registered delegation).
4. P-ISO true, P-κ false (any valid arm marginal/indeterminate) →
   **DISP-P: PARTIAL.** The tail question retires (isolation stands
   on its own evidence); 1B remains OPEN on the margin leg alone;
   panel scopes the residual.
5. P-ISO false because A0 shows NO artifact → **DISP-X:** the
   geometric diagnosis itself fails reproduction; all Q1 standing
   reopens; panel (impasse-class).
6. else → **DISP-M2 IMPASSE** (conflicted pattern; panel).

No interim looks; the analysis refuses an incomplete manifest; no
retune after launch; one panel round on completion per the standing
single-round rule.

## §6 — Effort estimate (for the founder's launch decision)

Leg-cost scaling from the committed campaigns (Route A x=16 leg
≈ 0.39 h at T=240; Route B x=24 leg ≈ 2.6 h at T=384): at T=288 —
x=16 ≈ 0.47 h, x=20 ≈ 0.9 h (interpolated volume scaling), x=24
≈ 2.0 h. Totals: A0 256 legs ≈ 500 CPU-h; A1 768 ≈ 690; A2 768
≈ 1540; A3 768 ≈ 360; pilots+calibration ≈ 40. **Campaign ≈ 3100
CPU-h ≈ 5–6 days wall on Kila6 at Route-B parallelism.** If the
founder rules the budget heavy, the FROZEN reduction (declared now,
usable only BEFORE launch): N_pairs 384 → 256 on inferential arms
(SNR projection re-checked at pilot against the same ≥10 bar; ≈ 2100
CPU-h ≈ 4 days). No other reduction is admissible.
