# PRE-REGISTRATION AMENDMENT — DIFFERENTIAL DRESSED DRIVE (MOBILE − FROZEN)

**Patch 2903. Committed BEFORE any differential run is executed or read.
This amendment ADDS an observable with its own bands; it does not touch,
widen, or reinterpret the §4 bands of
`mobile_sea_moving_source_prereg.md`, which remain frozen for the
original observable.**

---

## §1 — OBSERVABLE

For each β, two runs with **identical** Sea geometry, source trajectory,
equilibration, and measurement window:

- **MOBILE leg:** Sea CPs move per the primitive (the physical run).
- **FROZEN leg:** Sea CPs held at their initial symmetric configuration
  (`mobile_sea = False`); the source's transit and all retardation are
  otherwise identical.

> **ΔD(β) ≡ ⟨SSV_net,x⟩_mobile − ⟨SSV_net,x⟩_frozen**

The transit-lock systematic (§3 of the execution record) is common-mode
to first order and subtracts; ΔD isolates the Sea's *response* — the
entrained-arc contribution, which is the mechanism under test.

**Windows matched to the grid period** (resolution 1 of the execution
record): T_meas = the integer nearest an integer multiple k·(2.5/β)
chosen to land in [60, 100] Moments; β = 0 uses T_meas = 100.
Specifically: β = 0.05 → 100 (k = 2); β = 0.10 → 75 (k = 3); β = 0.20 →
63 (k = 5). T_eq = 40 throughout. β grid for this round:
{0.05, 0.10, 0.20} (three points; the fit is β²-only, two parameters).

## §2 — FROZEN BANDS FOR ΔD

Floor: ΔF₀ = |ΔD(0)|, same paired procedure at β = 0. Signal quality
Q_Δ: |ΔD(β)| > 5·ΔF₀ at every β, else INCONCLUSIVE.

| outcome | criterion |
|---|---|
| **CANCELLATION (provisional)** | Q_Δ holds; sign of ΔD uniform in β; β²-only fit ΔD/β = k(1 − c_sub β²) gives **\|c_sub\| < 0.05** |
| **RETAINED (provisional)** | Q_Δ holds; sign uniform; **c_sub ∈ [0.10, 0.30]** |
| **DRAG SIGN (provisional)** | Q_Δ holds; **ΔD < 0 at every β** — Condition A fails |
| **INCONCLUSIVE** | anything else |

**Every banded outcome above is PROVISIONAL:** the §5 convergence
variations of the original prereg (domain size, inner cutoff, softening,
window) still gate any final verdict, unchanged. A provisional band from
one configuration is reportable as provisional only.

**Interpretation note, frozen in advance:** ΔD is the *response* drive.
The frozen leg's own D_frozen is pure kinematics on an unresponsive
symmetric Sea and is expected to be artifact-dominated; it is recorded
but carries no band.

**Worker expectation, declared again in advance: CANCELLATION.** A
confirming result is accordingly weaker evidence than a disconfirming
one.

## §3 — EXECUTION DISCIPLINE

The differential runs execute in the patch AFTER this amendment is
committed (2904). If the round is cut short, partial results are reported
as partial; bands are not revisited. Re-banding after any result is
forbidden, as ever.
