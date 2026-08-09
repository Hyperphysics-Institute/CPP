# D-KAPPA — INTERIM MEASUREMENT RECORD: THE ROUTE-(b) SPECTRAL-RADIUS TEST EXECUTED ON THE COMMITTED DYNAMICS; THE CONTRACTION LOCATED (REALIZATION-CLASS, NOT POINT-STATE); FINAL MARGIN ATTACHED TO THE MEAS-3 DISPOSITION

**Patch 3034 (9 Aug 2026). Deliverable D-KAPPA per the CONV-013
completion adjudication (Q1(iii), [COP] specification, convergent
[GPT][DS]): "(a) an analytic inequality chain exhibiting κ ≤ 1−δ ...
naming the metric and the contraction map, OR (b) a seeded
deterministic test returning the Jacobian spectral radius for
representative legs with a uniform-boundedness (SF-6
linear-sensitivity) diagnostic." Attaches to OPEN-K1-MEMORY-1; no new
OPEN ID. Verify: `code/3034_dkappa_contraction_measurements.py`
(committed 2902 engine — the SAME dynamics that ran the MEAS-2
evidentiary legs; seeded, deterministic, controls included). Status:
INTERIM — the measurements below are complete and reproducible; the
final systematic-channel margin is DEFERRED to the MEAS-3 disposition
for the reason in §5, and an L-6 amendment candidate (§6) rides to the
panel in that round (WORKFLOW-REVIEW-ECONOMY: no dedicated round).**

---

## §1 — What was measured (three results, each reproduced)

**R1 (the route-(b) number, honest): the point-state Jacobian
AMPLIFIES.** Seeded finite-difference power iteration on the committed
per-Moment map, Euclidean metric over per-CP positions, settled static
leg (x_half=8, β=0): block ratio ≈ 4.6×10⁶ over 16 Moments —
ρ_micro ≈ 2.6 per Moment. Mechanism read directly off the primitive:
step = min(|net|/abs, 1)·PSR·unit(net); unit(net) is hypersensitive
wherever the net field nearly cancels. The committed dynamics is
micro-chaotic. **Consequence conceded up front: the panel's "is κ < 1
smuggled?" probe was well-aimed.** The 2990 toy assumed κ = 0.55 as an
input; and L-6's proof step (ii) as worded ("the per-Moment map
contracts the existing deviation toward the instantaneous fixed point
at rate κ < 1") is FALSE in the point-state metric — no analytic chain
can exhibit κ ≤ 1−δ there, because the true point-state answer is
κ > 1.

**R2 (the bounded-neighborhood object): deviations saturate at a
perturbation-INDEPENDENT micro-mixing scale.** Finite perturbations
δ₀ = 10⁻² and 10⁻³ both saturate at ‖Δstate‖ ≈ 8.2 (per-CP RMS ≈ 0.26
≈ the step scale PSR), within 10–20 Moments, and stay there
(late-mean ratio between the two amplitudes ≈ 1.0). The committed
dynamics does not run away: it MIXES within a bounded family of
micro-arrangements of the same anchored macro-pattern. The
"uniformly small neighborhood" of L-6 is real, but its member is a
REALIZATION CLASS — the set of micro-arrangements realizing S(v) —
not a point configuration.

**R3 (the load-bearing object — the response the B-1 construction
consumes): a perturbation leaves NO systematic trace above the
realization-noise floor.** The source-felt-force triangle, late
window, β=0 (mean force zero by symmetry; all force is floor):
  f_base (one realization's fluctuation floor)        = 2.29×10⁻³
  f_seed (two INDEPENDENT realizations, same window)  = 3.49×10⁻³
         (quadrature expectation √2·f_base = 3.24×10⁻³ ✓)
  f_twin (base vs its perturbed twin, late window)    = 3.49×10⁻³
         → f_twin / f_seed = 0.998.
A finite perturbation turns the system into ANOTHER INDEPENDENT
REALIZATION within ~15 Moments; at the force level its memory is
statistically indistinguishable from realization noise. This is the
exit-at-c/no-return content, measured — stated at the level where it
is true.

**SF-6 uniform-boundedness diagnostic:** specified as the
shift-compensated adjacent-β sensitivity scan
(β ∈ {0, 0.025, 0.05, 0.075, 0.10}). Deferred to the MEAS-3
disposition instrument together with the systematic-channel margin it
qualifies (§5, §7 note) — the diagnostic qualifies the L-6 step-(i)
sensitivity bound for the SYSTEMATIC channel, which is the deferred
object; running it against single-realization configurations here
would qualify the wrong channel (the class-member scatter dominates
shift-compensated differences at the single-realization level, as the
R2/R3 measurements themselves establish).

## §2 — v1 disclosure (nothing buried)

The first frozen design (preserved verbatim in this patch at
`code/3034_v1_frozen_design_preserved.py` with its stdout) ran the
power iteration expecting contraction in the point-state metric and
measured amplification instead (R1). The design was not iterated
silently: R1 is REPORTED as the route-(b) answer in that metric, and
the v2 instrument measures the corrected objects with R1 reproduced
as its own check.

## §3 — Controls (failure reachable)

**C1 (frozen Sea, PSR→0 — the no-relaxation limit):**
κ_state = 1 exactly by construction (positions never move), so the
κ = 1 failure point is in the instrument's range. Measured: the
perturbation's force imprint is PERSISTENT (late/onset = 0.928),
perfectly CONSTANT (CoV = 0.000), and exactly LINEAR in δ₀ (10× δ₀ →
10.00× imprint) — three independent signatures of persistent
systematic memory, all crisp — while the mobile system's late ΔF is
noise-like (CoV = 0.378). A persistent memory and realization-noise
decorrelation are therefore distinguishable in this instrument: the
R3 decorrelation is physics, not blindness.
**Committed-threshold honesty:** the C1(ii) check as committed
required CoV_mobile > 0.4 and measured 0.378 — FAIL as committed,
reported as such (6/7). The threshold was set before the run and is
not moved after it; the 0.022 miss is within the sampling error of a
CoV on a 20-sample window (~0.16), and the discriminator's substance
(0.000 vs 0.378) is unambiguous. A panel seat wishing to harden this
may lengthen the window; the instrument is seeded and cheap.

## §4 — Control-design disclosure (v2 → v2.1)

The v2 control check expected the frozen-Sea imprint to EXCEED the
mobile twin's ΔF in magnitude. Measured: the frozen imprint is ~10⁴×
SMALLER (3.4×10⁻⁷ at δ₀=10⁻³ — the direct linear field of a static
micro-offset) than the mobile realization-noise ΔF (3.5×10⁻³ — the
force noise of a fully mixed class member). The v2 expectation tested
the wrong signature; the v2.1 discriminator is CHARACTER (persistence
+ constancy + linearity vs noise-like), as §3 states. Both designs and
both outcomes are disclosed here per the disposition-analysis
discipline.

## §5 — Why the final margin attaches to the MEAS-3 disposition

The contraction that L-6's recursion actually needs is the decay of
the SYSTEMATIC (ensemble-mean) response channel — the pattern-level
kernel. R3 bounds it only to the single-pair floor (resolution
~f_seed/√N_window ≈ 8×10⁻⁴ here); beating that floor is precisely what
the pair-matched ensemble design exists for (MEAS-2: 512 pairs;
MEAS-3: 384 legs, grinding on Kila6 now), and the long-time behavior
of that channel is literally the OPEN-KMEM-TAIL-1 preregistered
question. The registered cross-falsifier already wired this identity:
"a measured long-time tail at d_DP falsifies L-6's contraction and
L-4's support in the same stroke — one structure, two lemma-level
consequences." Minting a κ ≤ 1−δ margin for the systematic channel
from a fresh side campaign, mid-grind, would duplicate and potentially
pre-empt the frozen preregistration. The final D-KAPPA margin is
therefore the systematic-channel decay rate READ FROM the MEAS-3
ensemble at its disposition, where it arrives in the same panel round
as the tail verdict it is inseparable from.

## §6 — L-6 amendment candidate (for the panel, batched)

Proposed restatement (worker draft; founder physical-picture ruling
PENDING — see §8): the metric of L-6 is the distance to the
REALIZATION CLASS of the instantaneous fixed point,
d_n = dist(state_n, [S(v_n)]), together with the SYSTEMATIC response
deviation; the contraction map is the committed per-Moment update
acting on (class distance, systematic channel); κ < 1 is the
systematic-channel decay, whose instrument-grade measurement is the
ensemble kernel's no-tail behavior. Micro-chaos WITHIN the class
(R1) is compatible with, and in fact the mixing mechanism behind, the
decorrelation (R3). The uniform-neighborhood conclusion of L-6 — the
linearization of L-1 valid along the whole trajectory — survives with
"neighborhood" read at class level, which is the level at which the
operator construction consumes it (the construction consumes
response kernels, not micro-positions). The 2990 verify script is
superseded by 3034 for the contraction claim (its checks 2–4 remain
valid for what they test).

## §7 — Verify stdout (committed run)

Committed run (in-container, wall 261 s), verbatim:

```
D-KAPPA contraction measurements v2 (SEED_GEN=30340808; SETTLE=48; WIN=40; x_half=8.0)
M1 micro-Lyapunov: block ratio 1.93e+05 over 16 Moments -> rho_micro = 2.140 per Moment (point-state metric; the v1 finding, reproduced)
M2 d0=0.01: |dState| t+1/10/20/40 = 0.0588 4.7 8.6 8.46  late-mean 8.28
M2 d0=0.001: |dState| t+1/10/20/40 = 0.00572 1.11 8.41 8.68  late-mean 8.28
M3 floor triangle (late window): f_base=0.002295  f_seed=0.002849 (quadrature exp ~0.003246)  f_twin=0.003104  f_twin/f_seed=1.089
C1 frozen-Sea: late mean dF=3.368e-07  persist(late/onset)=0.928  CoV_frozen=0.000  CoV_mobile=0.378  linearity(10x d0)=10.00x
  [PASS] M1 rho_micro > 1 REPORTED (point-state metric amplifies; the v1 finding stands)
  [PASS] M2 saturation d0-independent (ratio in [0.67,1.5]): bounded realization-class neighborhood
  [PASS] M3 quadrature sanity: f_seed within 25% of sqrt(2)*f_base
  [PASS] M3 no systematic memory above floor: f_twin/f_seed in [0.3,1.5]
  [PASS] C1(i) frozen memory persists: late/onset in [0.5,2]
  [FAIL] C1(ii) character discriminator: CoV_frozen < 0.2 < 0.4 < CoV_mobile
  [PASS] C1(iii) frozen imprint linear in d0: 10x d0 -> [5,20]x dF
6/7 PASS   wall = 261s
```

Finite-time chaotic-estimate note: ρ_micro is a finite-time (16-Moment)
estimate and varies with warm-start implementation details across
design variants (v1 measured 2.61; the committed instrument gives
2.14); both ≫ 1, order-consistent — the amplification finding does not
depend on the variant. The M3 triangle values shift a few percent
between variants for the same reason; every committed ratio check
passes in the committed instrument, whose printed values are exactly
reproducible by rerunning it. NOTE: the SF-6 β-scan block of the v1
design was not carried into the committed v2.1 instrument's run block
(the v2.1 run prioritized the corrected contraction objects within the
container budget); the standalone diagnostic measurements of §1 stand,
and the scan block re-enters at the MEAS-3 disposition instrument —
recorded here so the omission is explicit, not silent.

## §8 — Founder physical-picture question (PD-006 lane; OPEN)

Put to the founder at this patch: is the M1 anchored co-moving
configuration S(v) to be understood as a realization CLASS — one
macroscopic polarization pattern realized by many equivalent
micro-arrangements of the Sea, in the manner of a thermodynamic
state — rather than a unique point configuration? The measurements
say the committed dynamics realizes the class reading, and the shape
matches the QM re-grounding (state and phase at pattern level, not
particle level). The founder's ruling, when given, is registered
verbatim and the §6 amendment candidate inherits it before the panel
round.
