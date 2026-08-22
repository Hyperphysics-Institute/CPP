# PREREGISTRATION — D-JITTER-1 **PHASE B**: INSTALL THE COMPUTED ARRIVAL DRIVE

**Patch 3177, 22 August 2026. VideoCPU. Founder GO given 22 Aug.**
Executes charter §4B. **Every statement in §3–§6 is frozen BEFORE any
Phase B computation runs**, per §9 claim hygiene. Lane: cosmology block
(3100–3199).

Charter §4B, verbatim: *install the computed arrival drive in the v2
instrument in place of Gaussian σ_n (additively switchable, default
unchanged, bit-identity regression required); success = the
self-generated attractor reproduces without tuning.*

---

## §1 — INPUTS (all committed, none re-derived here)

- Phase A: **R = 1.357 ± 0.097** in nearest-neighbour-field units at
  K = 32, CONVERGENT (+1.39% vs the 5% gate); monopole part 1.357,
  paired-dipole part 0.030 (`phaseA_record.md`,
  `scripts/3168_phaseA_shell_sum.py`, seed 5, M = 100).
- The v2 instrument's Gaussian surrogate σ_n, and the committed
  attractor **σ\* ≈ 0.249** (3138).
- f_b from the eight-size campaign at the working spacing.

## §2 — THE MISSING PIECE PHASE A DECLARED

Phase A's R is in nearest-neighbour-field units; σ_n is in instrument
units. **The response kernel is the conversion, and Phase B's first job
is to compute it — not to assume it.**

**This is the same class of defect the band audit just caught**
(`../dark_matter/band_provenance_audit_3176.md`): a number carried
across observables as though the conversion were 1. Phase A declared
this boundary in advance and refused the comparison; Phase B honours
that by computing the kernel explicitly and reporting it as a number
with its own uncertainty **before** any attractor comparison is made.
If the kernel cannot be computed to better than a factor of 2, that is
reported and the attractor test is declared UNRESOLVED-BY-KERNEL rather
than run against a guess.

## §3 — FROZEN STATEMENTS

**B-1 — REGRESSION GATE (runs first; blocks everything else).**
With the computed drive switched OFF, the v2 instrument must reproduce
its committed results **bit-identically** (element-exact float64). Any
mismatch ⇒ Phase B VOID, no partial rescue; the installation is
reverted and the discrepancy recorded. Nothing in §4–§6 may be computed
before B-1 returns PASS.

**B-2 — THE KERNEL.** Statistic: κ ≡ σ_n^equiv / R, the instrument-unit
fluctuation produced per unit of nearest-neighbour-field arrival
fluctuation. Resolution floor: MC standard error over the same
configuration ensemble (M = 100), reported beside the value. Reported
with its uncertainty; **no verdict attached to κ itself.**

**B-3 — THE ATTRACTOR TEST (the charter's success criterion).**
Run the instrument with the computed drive installed at κ·R, no tuning
of any kind. Frozen readings:
- **REPRODUCES** iff the self-generated attractor lands within a factor
  of 2 of σ\* = 0.249 — i.e. σ_gen ∈ [0.125, 0.498].
- **MISSES-HIGH** iff σ_gen > 0.498; **MISSES-LOW** iff σ_gen < 0.125.
- **UNRESOLVED-BY-KERNEL** iff κ's own uncertainty spans a factor of 2
  or more, in which case no reading above may be declared.

The factor-2 band is chosen to match the corpus's standing band
convention and is frozen here, before σ_gen exists. **It is NOT
inherited from any prior campaign's band** — the 3176 audit is the
reason that sentence is written down.

**B-4 — INTERMITTENCY (new; the founder's microdynamics, made
testable).** The founder's registered picture
(`founders_voice/founder_ruling_inside_sea_dp_entities_2026-08-18.md`;
elaborated 21–22 Aug) describes CP motion as **saltatory**: long
stretches of conservative DP-arc cycling punctuated by rare close
encounters whose force dominates while they last. A Gaussian surrogate
has excess kurtosis 0 by construction. Frozen statistic: the **excess
kurtosis γ₂ of the computed arrival series**, with MC SE over M = 100.
- **INTERMITTENT** iff γ₂ > 1 at ≥ 3 MC SE.
- **NEAR-GAUSSIAN** iff |γ₂| ≤ 1 at ≥ 3 MC SE.
- **UNRESOLVED** otherwise.

**B-4 is a genuine test of the founder's picture, and it can fail.**
The picture predicts INTERMITTENT. A NEAR-GAUSSIAN return means either
the shell-sum arrival model is too coarse to express the saltatory
dynamics, or the picture's intermittency does not survive superposition
over ~10⁴ arrivals — and the record must say which alternatives remain
open rather than choosing one.

**B-5 — BOTH STATISTICS, NEITHER SELECTED (founder's ruling, 22 Aug).**
The founder ruled that whether the signal lives in the mean or the
tails is not knowable in advance and should be probed rather than
guessed. Therefore **B-3 (mean-based) and B-4 (tail-based) are BOTH
computed and BOTH reported in every outcome**, including outcomes where
one is favourable and the other is not. Neither may be selected after
the fact; neither may be omitted from a dispatch. A mixed return is a
result, not a failure.

## §4 — WHAT PHASE B MAY NOT DO

- No Phase C content: nothing touches Λ, c_Li, d_s^emp = 4.64, or the
  four-rate kinetics. Those remain the founder's item.
- No re-tuning of R, f_b, f_pair, or the shell model to improve B-3. If
  B-3 misses, it misses; the model's simplifications (12k² growth, 5%
  band, f_pair = 0.5, uniform-ensemble stand-in) are then the named
  candidates for a future pass, tightened on their own merits and never
  against σ\*.
- No claim about DM. Phase B is DE-lane instrument work.

## §5 — HAZARD DIRECTION (declared)

A REPRODUCES return favours the arrival model and makes d_s derivable
in principle — favourable to the programme. A MISSES return damages the
arrival model as posed. **The worker's pre-declared expectation:
MISSES-HIGH is most likely**, because R = 1.357 in nearest-neighbour
units is large and the kernel would have to suppress it by roughly 5×
to land on 0.249. Recorded before κ is computed so it cannot be shaded
afterward.

## §6 — CORRUPTION GUARD

VideoCPU, 16 cores, GPU declined (bit-reproducibility). BLAS/OMP pinned
to 1 thread. The B-1 regression gate IS the arithmetic check for this
phase; unlike the β-ladder there is no long leg campaign to duplicate.
Every reported number carries its MC SE.

## §7 — EXECUTION

Driver: `scripts/3177_phaseB_driver.py` (written next, after this
preregistration is committed — freeze-then-run order preserved, and
this file's commit is the freeze).
