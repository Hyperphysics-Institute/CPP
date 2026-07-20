# FORM-1 Agenda B — the transit-γ sink continuum derivation, part I: the T1-reproduction theorem, the phase-decoherence boundary mechanism, and the reduced-model pre-registration, committed before any run

**Patch 2655, 20 July 2026. Status: FORM-1 SESSION OPEN under charter v1.1
(`form1_session_charter.md`, Patch 2646 as amended Patch 2648 J2). Full Step-1
priority bootup executed per charter §7 (no lightweight mode). This patch is
derivation + pre-registration ONLY: no model run, no instrument run, no number
that could satisfy or fail any tier exists at this patch.** Working set: the
charter + its cited records (2626, 2628/2629, 2631, 2638, 2640, 2642, 2644),
DEP-1 (2627), the pinned 2626/2629 instrument (`code/2629_sink_obs1.py` exec-load
of `code/2602_hgamma_gates_b1.py` through the 2609 cut), and the registered
constants read from that artifact: E_qq = 66.27 MeV, d = D = 1.15 fm,
τ_C = 2π·ℏc/264 = 4.6957 fm/c, m_q = κ_q = 132 MeV/c², η = 0.5,
βd ∈ {2 (SOFT), 4 (STEEP)}, ω(w) = (w/D)·√(2E_qq/m_q) = 1.743 / 2.614 / 3.486
c/fm at w = 2 / 3 / 4 (the 2628 §2 registered frequencies, reproduced from the
constants to the printed digit).

**Fences (charter §6, verbatim, none moved):** DISC block per the 2648
adjudicated amendment (endpoint-ledger consumers open under the mandatory rider;
schedule/timing/mechanism consumers BLOCKED pending this session — nothing in
this patch consumes any deposit); no rates, no σ_cap, no relic contact;
v = 0.10c for any instrumental check; FW-1/ETA-1/AMB-1 riders in force; w = 3
quarantined (diagnostic only — and every diagnostic width introduced below
inherits the same quarantine); NB-S3a-1 boundary; Sea layer OUT of scope;
records unedited; **79.5% untouched under every reading of this patch and every
reading of the Agenda-B arc it opens.**

---

## 1. FB-T1 — the continuum sink law reproduces T1's ledger identity as its integral law (derivation; engine-theorem strength; NOT a world-call)

**The continuum law (the unique drag-form continuum limit of the registered
split map).** The registered discrete sink acts once per τ_C: with V̄ the
window-averaged velocity and V_osc = V − V̄, the split maps
V → V̄ + √(1−η)·V_osc and books the removed kinetic energy exactly
(`Sea += KEpre − rke(P)`). The continuum law with the identical per-τ_C action
on the oscillatory sector is linear drag on the oscillatory velocity component:

  dv_osc/dt = −λ_v·v_osc,  λ_v = −ln(1−η)/(2τ_C)   [η = 0.5 → λ_v = ln2/(2τ_C)]

with sink power booked as the transfer channel

  dSea/dt = P_sink(t) = −dE_mech/dt ≥ 0,  E_mech = KE + U_s + U_e.

**FB-T1 (theorem, about the law as written):** any sink of this transfer-channel
form satisfies, identically at every t and every γ,

  Sea(t) = E₀ − E_mech(t)          (exactly; δ ≡ 0 in the continuum),

because the law is DEFINED as a pure energy-transfer channel: every unit of
energy leaving the mechanical sector is booked, and no term of the law
references the shed schedule. This is T1's identity (2628 §1) with the drift
term δ(t) → 0: **the ledger identity is the energy first-integral of the
drag-form continuum sink** — schedule-blind by construction, at every γ,
exactly as the discrete T1 is schedule-blind by construction. Corollary
(S_end convergence): S_end = E₀ − E_mech(asymptotic state); for dt-robust end
states (settled CAP / separated SCA) the discretized law's S_end inherits
dt-convergence at the integrator's drift order — the 2629 P2 result derived
from the continuum side. **Charter note:** per charter §3, reproducing T1 is
the ENTRY CONDITION for Agenda B, not the test. FB-T1 opens the door; §§2–4
below are the test.

## 2. FB-MECH — the phase-robustness boundary: mechanism derivation (no numbers yet that touch any tier)

The discretized law differs from the continuum law only in the SCHEDULE: the
discrete sink is a stroboscopic phase-sampler. Each shed s_k = η·KE_osc-class
at the split instant t_k = k·τ_C is a sample of a quantity oscillating at 2ω
(the kinetic energy of a mode of frequency ω oscillates at 2ω). A sampled
schedule is dt-covered exactly where the SAMPLED PHASE is dt-robust. Two
derivation-level phase-error channels for the registered symplectic-Euler
(P-then-H) integrator:

- **Channel T (timing).** The first-order integrator's global trajectory error
  shifts the excitation onset (contact time t_x and the kick profile) by
  δt ∝ dt. The sampled phase at fixed clock time t_k shifts by
  δφ_T ≈ 2ω·δt(dt). Linear in ω, linear in dt.
- **Channel A (anharmonic amplitude — the dominant stiff-width channel).** The
  registered Morse well has energy-dependent frequency
  ω(E) = ω₀·√(1 − E/E_qq) (exact for Morse), so dω/dE = −ω₀/(2E_qq) near the
  bottom and steeper at large amplitude. The integrator's bounded energy error
  δE(dt) (modified-Hamiltonian amplitude, ∝ dt·⟨F·v⟩-class for symplectic
  Euler, with F_max = E_qq·β/2 ∝ ω) therefore produces a SECULAR phase drift

    δφ_A(per window) ≈ |dω/dE|·δE(dt)·τ_C = (ω₀/(2E_qq))·δE(dt)·τ_C,

  with δE(dt) ∝ ω·dt at the kick — so **δφ_A ∝ ω²·dt**: quadratic in
  stiffness. A transit-class encounter pumps E toward E_qq, where |dω/dE|
  grows without bound — the amplitude leg (2629 P3) is the same channel read
  along the other axis.

- **Window-sum cancellation (why the convergent regime is so clean).** The
  registered single-pass observable sums sheds over the W-A window
  (t ≤ t_x + 2τ_C), spanning ω·2τ_C/π ≈ 2.6 (w = 2) to 5.2 (w = 4) full
  periods of the 2ω oscillation. For a sum approximating an integral over
  whole periods, a common-mode phase offset δφ cancels at first order
  (the integral of the derivative of a periodic function over its period
  vanishes), leaving a second-order residual ~ δφ²/2-class plus a
  partial-period linear residual ~ δφ/(2π·N_p)-class. Hence in the coherent
  regime the observed final-inc is SMALL-quadratic in δφ; once δφ approaches
  ~1 rad the cancellation structure is destroyed and the final-inc saturates
  at the sample-variance plateau (order the per-sample oscillation fraction
  over √N_split — an O(10%) class for the 2–3 splits the W-A window holds).

**The boundary statement (the derivation's second required output, charter
§3 item 2):** the schedule is dt-covered iff the accumulated sampled-phase
decoherence over the shed-active window is small:

  Ξ(ω, dt, E_exc) ≡ N_w·[2ω·δt(dt) + (ω/(2E_qq))·δE(dt)·τ_C] ≲ 1,

with N_w ≈ 2 (the W-A window's split count). Ξ is monotone increasing in
stiffness (through ω and through δE ∝ ω·dt) and in excitation amplitude
(through δE and through the anharmonic growth of |dω/dE| at large E) — **the
boundary is bounded by exactly the two legs the instrument registered (2629
P1 stiffness, P3 amplitude), now as one derived functional.** The soft width
sits in the cancellation-protected regime; the steep width crosses Ξ ~ 1 and
saturates. The ordering final-inc(w=2) < final-inc(w=3) < final-inc(w=4) is
structural (Ξ strictly monotone in ω at fixed dt, v).

## 3. FB-RM — the reduced-model pre-registration (the derivation's quantitative arm; spec FROZEN here, run next patch, no iteration)

Order-of-magnitude hand evaluation of Ξ's O(1) coefficients is not
registerable arithmetic. The derivation's quantitative content is therefore
evaluated by a REDUCED MODEL — the continuum law of §1 and its stroboscopic
discretization of §2, instantiated at the registered constants with zero free
parameters — specified completely here before any run. Tuning discipline
(charter v1.1 Tier 2, verbatim): **no form parameter, cutoff, coarse-graining
rule, phase convention, or effective damping coefficient may be adjusted after
this patch; the model is run ONCE per cell; a derivation that reaches the
calibration points by tuning FAILS regardless of numerical agreement.** Every
spec item below carries its registered source.

**RM spec (frozen):**
1. **Degrees of freedom:** two qCPs, masses m = κ_q = 132 MeV/c² each
   [SF-6 pin, Patch 2496; engine constant KQ], relative 1D coordinate r,
   plus the incident's initial drift. Scope disclosure: the single-pair
   reduction is the minimal mechanism carrier; it targets LOCATION-CLASS and
   ORDERING, not per-mille values — stated before the run, in the same font
   as the nucleus1 operationalization precedent.
2. **Potential:** U(r) = E_qq·[(1−e^{−β(r−d)})² − 1] with E_qq = 66.2707 MeV,
   d = 1.15 fm, β = w/d [the 2584-lineage registered form and pins], PLUS the
   registered soft electric qq kernel between the pair at the engine's charge
   weights [2602 constants A_QQ, √α_s weighting] — attractive (opposite
   polarity, the B1 incident is C = −1 against a +1 near vertex).
3. **Kinematics:** incident released at r₀ = 4D with inward v₀ = 0.10c
   [B1 launch geometry, 2602/2629 verbatim]; target member initially at rest.
4. **Integrator:** relativistic symplectic Euler exactly as the engine
   (P ← P + F(r)·dt, then r-update with vel(P)), dt = τ_C·dtf.
5. **Sink:** the engine split verbatim — once per τ_C (spc = round(1/dtf)
   steps), V̄ from the accumulated per-step velocity average, V_osc = V − V̄,
   V → V̄ + √(1−η)·V_osc with η = 0.5, exact ledger booking of removed KE.
6. **Observable:** S_WA = Σ sheds with t ≤ t_x + 2τ_C, t_x = first r < 2D
   [the 2629 W-A window verbatim]; final-inc = |S(finest) − S(next)|/S(finest)
   on the registered dt ladder.
7. **Cells (calibration face):** w ∈ {2, 3, 4} × dtf ∈ {1/100, 1/200, 1/400},
   v = 0.10c — the P1 protocol's cells, one run each.
8. **Cells (holdout face, computed in the same single pass, output SEALED
   into the Tier-3 prediction block of the next patch before any registered-
   instrument run):** (H1) w = 2.5 (ω = 2.179 c/fm; DIAGNOSTIC-QUARANTINED
   exactly as w = 3 — no DM consumer may ever cite a w = 2.5 result) at
   dtf ∈ {1/100, 1/200, 1/400}; (H2, extrapolative) w = 4 at
   dtf ∈ {1/400, 1/800}; (H3, extrapolative) w = 2 at dtf ∈ {1/400, 1/800}.

**Tier-2 reading classes (frozen, with derivation-independent anchors —
justified so the thresholds cannot be gerrymandered):** "convergent class" =
final-inc ≤ 2.5%, the ceiling of the P2 endpoint drift-band criterion
(Edrift/S + 1% evaluated 1.8–2.5% at the registered anchors, 2629); "saturated
class" = final-inc ≥ 5.0% (twice the convergent ceiling); "marginal" between.
- **FB-ORD (ordering leg):** model final-inc at the finest pair strictly
  monotone increasing in w across {2, 3, 4}. The registered instrument's P1
  row already shows the monotone ordering; FB-ORD asks whether the DERIVED
  law reproduces it without tuning.
- **FB-LOC (location leg):** model places w = 2 in the convergent class and
  w = 4 in the saturated class at the finest registered pair — the boundary
  between them, where the instrument put it.
- **Tier-2 PASS = FB-ORD ∧ FB-LOC.** Tier-2-only pass reads FD-PARTIAL for
  Agenda B per charter v1.1; FD-FULL additionally requires Tier 3.
- **FB-RC:** any model-implementation defect discovered after the run routes
  to the instrument-hazard lineage template (J4 discipline applies to the
  reduced model as to any new instrument: spec-to-code trace table in the
  verify header; guard triggers; the model code is NEW instrumentation and
  this section is its pre-registration).

**Tier-3 structure (frozen):** after the model run, the H1/H2/H3 model
outputs are written as PREDICTIONS (class + direction per cell) in the
execution patch, BEFORE the registered instrument runs them. The registered-
instrument holdout run (next-next patch) carries a pin control — the P1
calibration row must reproduce the 2629 printed values — and then executes
H1/H2/H3 as width/dt extensions of the pinned 2629 instrument (no other
change; w = 2.5 quarantined as declared). **Tier-3 PASS** = every holdout
cell lands in its predicted class with its predicted direction. Predicted
direction content the mechanism commits to NOW, ahead of the model numbers:
under §2, H2 (w = 4 at finer dt) must move DOWNWARD out of saturation as
Ξ ∝ dt falls (a "fundamental non-convergence" account predicts flat), and
H3 (w = 2 at finer dt) must continue converging. H1's class is the genuine
open risk — the boundary's location at ω = 2.179 is exactly what the
derivation is for.

**Kill discipline (charter §5 applied):** model non-monotone or wrong
location → Agenda B composes as **FD-BOUNDARY** (FB-T1 stands as theorem;
the boundary prediction failed; schedule quantities REMAIN blocked; adverse
direction, same font). Tier-2 pass + any Tier-3 holdout miss → **FD-PARTIAL**
with the missed holdout named as the residue. All classes compose with
Agenda A per charter §5; no class may be renamed after a result exists.

## 4. Bookkeeping

No registry changes at this patch; no consumer sentence rides on anything
here; the DISC amendment's pending clause is untouched until the arc
composes. Next patch: RM execution (§3 cells, one pass, verify script
`code/2656_form1_b_rm.py`) + the Tier-3 prediction block. Reasoning:
`reasoning/2655.md` (no computation at this patch; stated).
