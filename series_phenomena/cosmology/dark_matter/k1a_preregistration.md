# K1a pre-registration: the conservative collision instrument (O1a) — capability census against the code, the frozen dynamical rules, live-list rules, the energy ledger and the emergent-transfer clause, the control battery, grids and economy, committed before any derivation

**Patch 2572, 19 July 2026. Status: K1a OPENED at pre-registration; NO derivation performed.**
Governed by the NB-S3a-1 charter v1.1 (2569) and this document only. Named inputs include the
frozen 2571 handoff table. **Verify: none needed at prereg (declarations only).** Collision check
clean (no prior K1a/O1a registration).

## 0. Target and scope

**Target:** for the non-DEAD cells of both channels, the K1a observables at dance strength:
**encounter probability** (does cross-contention engage), **dwell-time distributions** (time with
cross-DP center separation < 1.5·a_qq or cross-energy < −2·floor), **transient-trapping
statistics**, and the **translational-energy transfer** ΔKE across the encounter. **Permanent
capture is NOT an O1a observable** (charter §1): end-states that would classify CAPTURED under
the 2564/2565 classifiers are recorded as **TRAPPED-AT-END (permanence unresolved)** — the K1b
sink question owns permanence. No rates, no abundance, no L-content, no composition reading.

## 1. Capability census (charter §3 rule; against `code/2565_k1_r0_rp_gate.py` and 2557)

**Exists, banked, consumed as-is:** the translating-home minimal extension (C-1-validated
ballistic transport); the CL-A/CL-B classifier pair (C-3-validated); the live-reach evaluation
path (2565 diagnostic branch — same reach-S rule on current positions).
**Does NOT exist and is REGISTERED by this prereg as the O1a layer (each element charter-licensed
§1/§2):** (i) promotion of live lists from diagnostic to registered rule under §4's frozen
conventions; (ii) the conservative rigid-body scaffold dynamics — translation AND rotation — under
the exact back-reaction law of §3, with the pinned masses; (iii) the energy/momentum ledger of §5.
Nothing else is added; any rule found necessary mid-execution beyond (i)–(iii) is Branch I,
founder-routed (the 2564 kill condition inherited).

## 2. Closed input list (nothing else may enter)

Instrument constants and machinery verbatim from 2557; the 2565 extension and classifiers; pinned
masses m_qCP = 132, m_eCP = 44 (M_qDP = 264, M_eDP = 88 MeV/c²; I_DP = 2·m·(ℓ/2)² with ℓ the
species contact scale); the 2564 grids MINUS the 2571 unanimous-DEAD cells (**named input: the
handoff table — qq runs 49 cells, qe runs 28**); the 2570 orientation classes (5) × parities (2)
— identical enumeration across map and instrument; dt union {1/100, 1/50, 1/25}; TC = 60, burn
0.15 for bound contexts (encounters run un-burned — the transient IS the observable); chaotic
floor ±2 MeV; E↔v mapping as declared at 2565 (relativistic per-DP). EXCLUDED, named: window/
wall/pin/kT·L/16/abundance; any dissipation term; any coupling coefficient other than unity.

## 3. The O1a dynamical rules (frozen; the ONLY new dynamics)

Per step, for each structure S with center R_S, velocity V_S, axis â_S, angular velocity ω_S:

- **F_S = Σ_{i∈S, j∉S} F_ij** (the registered pairwise force at CP positions P; cross-structure
  terms only). Newton-pair antisymmetry F_A = −F_B holds by construction and is ASSERTED
  numerically each run.
- **V_S ← V_S + (F_S / M_S)·dt**;  **ω_S ← ω_S + (τ_S / I_S)·dt** with
  τ_S = Σ_{i∈S} (h_i − R_S) × F_i (torque about the scaffold center, evaluated at home points
  h_i to keep the rigid layer self-consistent);  **R_S ← R_S + V_S·dt**; â_S rotated by ω_S·dt.
- Homes h_i = R_S ± â_S·ℓ/2 (the rigid frame); CP dynamics (contention, arrest, chase) entirely
  unchanged.
- **No damping term exists in this instrument.** The unity coupling is not tunable; if unity
  transfer is ever argued wrong, that argument is an open derivation elsewhere, never a K1a knob.

## 4. Live-list rules (frozen)

Primary convention: the reach-S rule re-evaluated **every step** on current positions P — the
letter of the definition at the finest admissible cadence; registered radii unchanged (no new
cutoffs; binary lists as registered — a smooth entry/exit weighting would be a NEW rule and is
not licensed; dt-union convergence stands in for smoothness concerns). Secondary convention (the
union probe): re-evaluation every Moment cycle (TAUC). **Commitment survival:** an out-CP's
committed target persists until hit or arrest exactly as coded — list changes act only at
retarget events (no mid-chase retargeting is introduced).

## 5. Energy ledger and the emergent-transfer clause (frozen before any run)

Tracked per step: KE_trans = Σ ½M_S V_S², KE_rot = Σ ½I_S ω_S², U_cross(P), and their sum.
**Disclosure, pre-committed:** the contention layer is non-Hamiltonian (choreographed CP motion),
so exact conservation of the tracked sum is NOT expected; the pre-registered requirement is
dt-CONVERGENCE of the ledger drift. **The emergent-transfer clause:** a dt-stable,
floor-exceeding systematic transfer of translational energy into the contention layer during
encounters is RECORDED AS AN OBSERVATION (candidate emergent Sea-coupling signal, of direct
interest to K1b R-A) and is NOT consumed as capture license — permanence still belongs to K1b;
conversely, a dt-unstable drift is an integrator artifact and is reported as such. This clause is
frozen now precisely because the observation, if it appears, will be tempting in both directions.

## 6. Control battery (all pass criteria frozen; production is gated on ALL passing)

- **CTRL-1 — bound-state invariance (mandatory, 2568):** the registered contact-pair bound
  configuration run WITH the full O1a layer active must remain bound (CL-A/CL-B = CAP) with
  final-window energies within the chaotic floor of the 2565 C-3 record, in every dt cell.
- **CTRL-2 — zero-coupling ballistic:** back-reaction coefficient set to zero must reproduce the
  2565 C-1 and C-2 results identically (regression guard on the banked extension).
- **CTRL-3 — dead-cell pass-through:** the (E = 100, b = 0) qq cell (unanimous-DEAD) with full
  O1a active: no TRAPPED-AT-END in any dt cell; total momentum conserved through the encounter
  within the §6 tolerance.
- **CTRL-4 — scaffold-layer reversal:** contention frozen (CPs pinned to homes), the pure
  rigid-body layer run forward T then reversed: return to initial state within an integrator
  tolerance that must shrink with dt² (Euler-order convergence declared).
- **CTRL-5 — exchange symmetry:** A↔B relabeling yields identical trajectories.
- **CTRL-6 — mirror symmetry:** b → −b with mirrored orientations yields mirrored trajectories.
- Tolerances: momentum |ΔP_tot|/P_scale < 10⁻³ per run at dt = 1/100 with dt-convergence shown;
  CTRL-4 return error declared per above. Any control failure → the run set halts; the failure
  is Branch I with the control named (no in-campaign repair beyond faithful-implementation fixes
  of the 2571-disclosure class, which are disclosed and re-run).

## 7. Grids and economy (frozen)

**Convention-union probe set (all conventions: dt × FREF{sys, dp} × list{per-step, per-cycle}),
declared now:** qq (10, 0.5), (15, 0.75), (5, 1.0), (1, 0.25), (20, 0)·a_qq; qe (0.5, 0.5),
(1, 0.25), (5, 0), — six cells spanning channel, E, and b. **Production tier:** all non-DEAD
cells × 10 class-parity combinations × dt union, at the PRIMARY conventions (FREF_sys; per-step
lists), with the probe-set spread carried as a disclosed systematic band on every production
observable. Primary-convention rationale recorded a priori: FREF_sys matches campaign precedent
(scaffold-max SSV); per-step lists are the definition's letter. Choosing any convention by its
production output = Branch T.

## 8. Observables and end-state classification (frozen)

Per run: engagement flag (any cross-structure contention commitment occurred); dwell time (per §0
definition); ΔKE_trans (initial minus final, MeV); end-state ∈ {ESCAPED, TRAPPED-AT-END,
UNRESOLVED} via the 2564 classifiers with CAP relabeled TRAPPED-AT-END per §0. Encounter
probability per cell = engagement across class-parity combinations (reported per class, never
phase-space-averaged — the 2570 discipline). All tables frozen before any comparison sentence;
the single permitted comparison: the epoch-band rows' dwell/trapping census stated as ambient
context (charter fence — not a success criterion).

## 9. Fences restated at maximum temptation

TRAPPED-AT-END is not capture and may not be summed, rated, or forwarded as capture; the
emergent-transfer observation (§5) is banked-only; no convention, tolerance, or grid choice by
output; the 2571 map may not be softened by anything found here (revival of dead cells requires
the §5-class evidence to be taken to K1b/charter level first); any new √5 → fence; no composition
reading under any outcome.

## 10. Readings (frozen)

Controls all pass + production tables freeze → **K1a DELIVERED**: the dwell/trapping/transfer
tables bank as K1b R-A's consumption input (the transfer derivation needs dwell-times to transfer
DURING) and as K2's encounter-statistics input. Any control fails → Branch I, control named.
Engagement null across accessible cells → DELIVERED-ADVERSE for the channel, recorded as-is
(charter pre-commitment; equal-status result). UNRESOLVED-dominated → honest partial; resolved
cells freeze; a longer-TC successor routes to governance.

## 11. Bookkeeping

79.5% untouched. Queue: K1a execution (controls patch, then production patch) → K1b R-A prereg
(the SF-6→Sea transfer derivation, consuming the dwell tables) → K2. REACH-AUDIT-2 holds its
audit slot. Next patch: K1a controls execution, under this document only.
