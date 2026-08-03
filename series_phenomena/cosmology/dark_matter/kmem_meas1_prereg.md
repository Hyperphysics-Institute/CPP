# K-MEM-MEAS-1 — PREREGISTRATION: STEP-RESPONSE KERNEL MEASUREMENT ON THE MOBILE-SEA ENGINE (frozen before execution)

**Patch 2967 (3 Aug 2026). Preregisters the discriminating computation
for the T-3 §6 kernel decomposition (`k1_t3_ring_stiffness.md`) on the
committed 2902 mobile-Sea engine, per founder direction this session
("do the K-MEM measurement if you have the resources") and per the
2874 §4.1 standing rule: a favourable convergence gets a COMPUTATION
before it gets a vote. The T-1-based cancellation structure is the
arc's SEVENTH favourable convergence; this measurement is the
computation. All thresholds, windows, and branch readings below are
frozen BEFORE any driver code exists or any leg runs; the execution
patch (next) may not alter them. Assumptions carried: PROTOCOL-D1
(2960); PRINCIPLE-R1 (RATIFIED 2963 — distinct from PR7 clause 2's
"R1 (memory)" = OPEN-K1-MEMORY-1B = K-MEM, per the 2831 naming
motion). No value of any open quantity will be minted.**

## §1 — WHAT IS BEING TESTED, AND WHAT CANNOT BE DECIDED

**Tested (evidence-class, Tier-2):** the mechanism-derived prediction
of T-3 §6 — **Markovian-plus-stiffness**: after a velocity step of the
source, the Sea's force response settles to its steady value within
the BALLISTIC transit of the correlated volume, with NO long-time
dissipative tail; and the transient's support SCALES WITH DOMAIN SIZE
(geometric/ballistic origin), which a genuine Sea memory kernel would
not do. The domain-scaling leg is this preregistration's transient-
separation instrument (S1 spec item 5, at toy grade).

**Explicitly NOT decidable here (scope fences, frozen):**
- K4's bound at PHYSICAL d_DP (S1 spec item 2) — this is a Tier-2 toy
  Sea; no physical-scale claim is made or implied.
- K4 leg 2 (ambient physical Sea v/c bound) — untouched.
- OPEN-PHASE-THRESH-1 — no phase adjudication; no oscillation leg is
  chartered here (deferred; if any phase quantity is incidentally
  computed it is REPORTED, never judged).
- OPEN-CALIB-COUNT-1, the f-derivation, N — untouched.
- **No PR enactment; no evidentiary credit self-assigned.** Per 2874
  §5's Darwin-precedent treatment, this record enters as REGISTERED
  MEASUREMENT with evidentiary weight assigned by the panel at the
  combined CONV-011 review of the T-1/T-2/T-3 package. Six of seven
  stands; 1B remains OPEN regardless of branch.

## §2 — INSTRUMENT (committed, unmodified)

`flagship_papers/electromagnetism/code/2902_mobile_sea_engine.py`:
`build_sea`, `History`, `field_at`, `moment_step`, with
`mobile_sea=True` (the Sea must respond; frozen-Sea legs measure
nothing about the kernel). Engine constants as committed (PSR = 0.5,
D0 = 0.6, softening, CLAT = 1). The kernel gate stands: the driver
adds NO kernel changes — it only sequences the committed step and
records `src_net[0]` (axial force on the source) each Moment.
Retarded-time warm start (`tr_guess`) is used as committed.

## §3 — LEGS (frozen)

Source charge +1 at x_src0 on the axis; History pre-filled with the
source STATIC (beta = 0 backward extrapolation) — the step is then
causal within the record.

- **L1 (main step, standard domain):** rho ∈ [1, 8], x_half = 16,
  spacing 2.5. T_eq = 24 Moments at beta = 0; at t_step = 24 the
  prescribed advection becomes beta_f = 0.10; record through
  t_end = t_step + 6·T_ball. **T_ball(std) ≡ ceil(2·√(16² + 8²)) =
  36** (round-trip to the farthest Sea CP at CLAT = 1). t_end = 240.
  x_src0 = −0.5·beta_f·(t_end − t_step) = −10.8 (transit stays inside
  the domain).
- **L2 (control, no step):** identical geometry, beta = 0 throughout,
  144 Moments. **Noise floor sigma_ctrl ≡ std of F_x over
  t ∈ [24, 144).** Mean over the same window is the static-pattern
  offset F_stat (the 2918 persistent-core analogue), reported.
- **L3 (domain-scaling discriminator):** rho ∈ [1, 6], x_half = 12,
  spacing 2.5; same T_eq, same step to beta_f = 0.10;
  **T_ball(small) ≡ ceil(2·√(12² + 6²)) = 27**; t_end = 24 + 162 =
  186. x_src0 = −8.1.

Checkpointing across tool calls is permitted (exact-state resume);
leg-atomic appends; nothing verdict-relevant in /tmp at close.

## §4 — FROZEN STATISTICS

Per step leg: **F_0** = mean F_x over [t_step − 12, t_step);
**F_inf** = mean F_x over the tail window
**W_tail = [t_step + 4·T_ball, t_step + 6·T_ball]**;
**S = |F_inf − F_0|** (step scale);
**thr = max(0.10·S, 3·sigma_ctrl)** (settle threshold — 10% of scale
or 3× the measured chatter floor, whichever is larger);
**t_settle** = (last Moment in (t_step, t_end] with
|F_x − F_inf| > thr) − t_step;
**tail residual r_tail** = max over W_tail of |F_x − F_inf| (computed
on a centered 5-Moment moving mean to reject per-Moment chatter).

## §5 — FROZEN BRANCH READINGS

- **B-MPS (supports T-3 §6):** in BOTH L1 and L3:
  t_settle ≤ 2.0·T_ball AND r_tail ≤ thr; AND the domain-scaling
  ratio t_settle(L1)/t_settle(L3) ∈ [0.9, 2.7] (consistent with
  ballistic scaling 36/27 = 1.33 within a factor ~2).
- **B-TAIL (falsifier-class for the T-3 §6 prediction):** r_tail >
  0.5·S in BOTH L1 and L3 (a persistent tail at half the step scale,
  in both domains). **Frozen response: HALT, pre-action review,
  founder escalation — the worker's own theorem package takes the
  hit**, per the K1 charter's falsifier discipline and T-3 §6's
  registered exportable falsifier.
- **B-INT (anything else):** registered as-is, routed to the combined
  CONV-011 review with the package, no claim made. In particular a
  settle time that does NOT scale with domain, or a tail above thr
  but below 0.5·S, lands here — described, not argued.

If beta_f = 0.10 produces S < 3·sigma_ctrl (step unresolvable above
chatter), the leg reading is **UNRESOLVED-BY-FLOOR** — reported, no
branch fired, no threshold retuned within this preregistration; any
re-run at larger beta_f requires a fresh preregistration.

## §6 — DISCLOSURE DUTIES OF THE EXECUTION PATCH

Full F_x(t) traces archived in-repo under
`series_phenomena/cosmology/dark_matter/data/`; the driver script
committed same-patch; every deviation from this preregistration (if
any is forced by an engine-interface fact discovered at execution)
disclosed line-by-line with the frozen reading applied to the data
as-is wherever computable; first-run bugs disclosed per the arc's
standing practice. CONV-007 withheld-key admissibility applies to any
subsequent panel dispatch, not to this record.

## §7 — LEDGER

Nothing moves: six of seven; PR7 PARTIAL (1B OPEN =
OPEN-K1-MEMORY-1B); B7 holds DM-1/DM-3 banners; Candidate (B) 79.5%;
2855 PROVISIONAL; d_DP ceiling ACTIVE.
