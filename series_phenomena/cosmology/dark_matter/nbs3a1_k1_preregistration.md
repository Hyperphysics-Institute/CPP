# NB-S3a-1 Phase K1 pre-registration: two-body capture at dance strength — the representational-premise gate, closed inputs, frozen grids and classifiers, routes, and readings, committed before any derivation

**Patch 2564, 18 July 2026. Status: PHASE K1 OPENED at pre-registration; NO derivation performed.**
Governed by `nbs3a1_project_charter.md` (2560) and this document only. Panel ITEM 9 amendments not
received (dispatch deferred, 2563 rider); charter Q3 is internalized here as §1's blocking gate; Q1's
adjudication hook is §6(e); Q2 belongs to K3 and nothing here touches it. Late-arriving amendments bind
every not-yet-run cell as riders. **Verify: none needed at prereg (no structural computation; grids and
classifiers are declarations).** Collision check clean (no prior K1/NBS3A1-K1 registration).

## 0. Target and scope

**Target:** capture cross-sections σ_cap(E_rel) at dance strength for the charter's two encounter
channels — **qDP+qDP** and **qDP+eDP** — as functions of relative kinetic energy and impact parameter,
under dance_v8 (reach-S) with initialized velocities. **Scope limits (frozen):** K1 delivers
cross-sections ONLY. No rate is assembled (rates = density × flux × σ live in later phases under their
own preregs); no abundance statement; no L-content of any kind; no composition reading (trap clause);
the FORM-L window/wall quantities are not inputs and may not appear. Adverse or null capture across the
grid is a reportable K1 result per the charter's pre-commitment.

## 1. THE RP-GATE (blocking; runs FIRST; internalizes charter Q3)

**The representational premise, stated from the instrument as registered (2557 definitions):** dance_v8
is home-anchored — every CP carries a scaffold home H, and each step moves it toward a contention
target or back toward H (`dest = P[tgt] if out else H`). The registered instrument has only ever run
bound configurations. An UNBOUND incoming DP is representable, if at all, by the **minimal extension**:
the DP's home scaffold translates rigidly with the initial relative velocity (a co-moving home frame),
with NO other rule change — no new forces, no modified contention, no altered arrest logic. Anything
beyond home-translation is a new dynamical rule → **the charter's K1 kill condition fires: Branch I,
founder-routed, named gap "unbound-state representation."**

**Gate controls (all three must pass before any production cell runs; pass criteria frozen now):**
- **C-1 (free flight):** a single DP with translating home and no partner must translate uniformly —
  net displacement matches the initialized velocity within the chaotic floor; no self-trapping.
- **C-2 (over-barrier pass-through):** a head-on encounter at E_rel far above every registered well
  scale (declared: E_rel = 500 MeV) must NOT capture under every classifier in §3.
- **C-3 (bound-state recovery):** the same two-body system initialized at contact separation with zero
  relative velocity must register as CAPTURED under every §3 classifier — reproducing the registered
  bound lineage; a C-3 failure means the classifier, not the physics, is broken.
Any control failing after the minimal extension is implemented faithfully → the kill condition, as
above. Repairing a control by adding rules = the same kill condition, not a repair.

## 2. Closed input list (nothing else may enter)

1. **Instrument:** dance_v8 with reach-S, VERBATIM from `code/2557_reregistration_reach_s.py`
   (constants AHC, α_s = 5/(8φ) [pre-existing upstream lineage, fence-noted], a_qq/a_ee/a_qe, TAUC,
   pins m_qCP = 132 / m_eCP = 44, soft-a, SSV/FREF machinery), plus ONLY the §1 minimal extension.
2. **Species geometry:** the registered DP units (qDP = the registered qCP–qCP pair at a_qq contact
   scale; eDP likewise at its registered scale) — from the 2450/2455 lineage as consumed by every
   dance campaign since.
3. **Run conventions:** dt union {1/100, 1/50, 1/25}·TAUC (the three registered cells); both
   registered FREF conventions; TC = 60-class budget with burn 0.15; chaotic floor ±2 MeV on every
   energy readout. Where a K1-specific choice is forced (e.g., FREF for a two-body system), all
   defensible conventions are computed and the union reported with spread disclosed (2541 §3 rule).
4. **Frozen grids (declared now, before any run):**
   - E_rel ∈ {0.5, 1, 2, 5, 10, 15, 20, 50, 100} MeV — logarithmic-ish, spanning the QCD→BBN corridor;
     the conditional epoch band [10.2, 17.0] MeV lies interior WITH its full conditionality rider and
     enters only as ambient context, never as selection evidence (charter §2).
   - Impact parameter b ∈ {0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0} × a_qq (a_qq = 0.747 fm).
   - Initial separation: declared 6·a_qq along the approach axis (beyond every reach radius in the
     registered reach-S build).
5. **Standing pre-commitments:** trap clause; √5 fence (any NEW √5 → procedure); no rate assembly
   (§0); chaotic-floor discipline; the no-re-roll rule (frozen cells are never re-run "to check").
6. **EXCLUDED, named:** the FORM-L window [8, 22] and wall (22, 24); the E_close pin; kT·L; any
   abundance target; N = 16 in any form; any grid point, classifier, or convention added after a
   result is seen (additions = Branch T).

## 3. Capture classifier (frozen; union over the two defensible readings)

A production cell's outcome is classified at end-of-run (post-burn window):
- **CL-A (separation):** CAPTURED iff the time-averaged inter-DP separation over the final 25% of
  steps < 1.5·a_qq AND shows no monotone growth over that window; ESCAPED iff final separation
  > initial separation with monotone growth over the final 25%; else UNRESOLVED.
- **CL-B (energy):** CAPTURED iff the time-averaged pair interaction energy over the final 25% sits
  below −(2·floor) = −4 MeV persistently; ESCAPED iff it returns to within ±floor of zero; else
  UNRESOLVED.
Both classifiers run on every cell; disagreement or UNRESOLVED under either → the cell reports
UNRESOLVED (never averaged away). σ_cap at each E_rel = π·b*² where b* is the largest grid b with
CAPTURED in ALL dt cells under BOTH classifiers; reported as a band across FREF conventions, with the
grid resolution carried as the b-band. **No interpolation past the grid; no refinement of the b-grid
after results are seen (Branch T); a pre-declared uniform b-grid refinement for ALL E_rel is
admissible only in a successor prereg.**

## 4. Routes (order LOCKED)

- **R-0 — the RP-GATE** (§1 controls; blocking).
- **R-A — qDP+qDP grid** (9 × 7 × 3 dt × FREF union). Freeze the σ_cap(E_rel) table.
- **R-B — qDP+eDP grid** (same structure). Freeze.
- **R-C — consolidation:** the two frozen tables side by side; energy-dependence shape described;
  the Q1 evidence hook (§6(e)) recorded. No cross-channel synthesis beyond description.

## 5. Fences restated at the point of maximum temptation

Choosing any convention, classifier threshold, grid, or run budget because it moves σ_cap toward a
preferred capture picture = Branch T. The epoch band is ambient context, not a target: a derivation
step that treats capture-at-[10.2, 17.0] as the success criterion is output-justified = Branch T.
Both charter-pre-committed directions are equal-status results: strong capture (assembly kinetics
live) and weak/null capture (assembly bottleneck — adverse for the channel, recorded as-is).

## 6. Readings (frozen)

- **(a) RP-GATE fails** → K1 CLOSED BLOCKED: Branch I, founder-routed, named gap "unbound-state
  representation"; the gate controls' outputs bank; K2 does not open on a blocked K1 without founder
  re-charter.
- **(b) Gate passes, tables freeze** → σ_cap(E_rel) REGISTERED at dance strength as bands; K1 CLOSED
  DELIVERED; the K2 prereg may consume the tables as inputs.
- **(c) Null capture across the full grid** → K1 CLOSED DELIVERED-ADVERSE (per charter
  pre-commitment); recorded as-is; no in-campaign repair, no grid extension chasing capture.
- **(d) UNRESOLVED-dominated tables** → honest partial: resolved cells freeze, UNRESOLVED fraction
  disclosed; whether a longer-TC successor prereg is warranted routes to governance, not taken here.
- **(e) Q1 evidence hook:** K1 records (descriptively, no adjudication) any observed indication that
  two-body capture under-determines plane assembly (e.g., captured pairs whose configuration is not
  a plane precursor); adjudication of phase order belongs to the K2 prereg.
- **(f) Any new √5** → fence procedure before any reading. **No composition reading under any
  outcome.**

## 7. Bookkeeping

79.5% untouched (nothing here is promotion-class). Queue: K1 R-0 → R-A → R-B → R-C, each result
frozen before the next route opens; K2 prereg only after K1 closes; the plane-resident-fraction limb,
δ_E, and MW-MODES TC-extension remain ranked behind the K-phases per the standing ordering. Next
patch: the RP-GATE execution (R-0), under this document only.
