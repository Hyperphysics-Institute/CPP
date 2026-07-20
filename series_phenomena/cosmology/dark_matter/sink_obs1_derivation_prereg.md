# SINK-OBS-1: the sink's derivation-covered observable at transit-γ — the endpoint-ledger theorem, the schedule non-observability account, and three pre-registered falsifiable tests, committed before any run

**Patch 2628, 20 July 2026. Status: SINK-OBS-1 OPENED — founder-placed** (Thomas's
direct question at this contact: *"What is the sink's derivation-covered observable
at transit-γ? — with the soft-vs-steep convergence split as its falsifiable
target."*). This cell answers with (i) an engine-level derivation, (ii) a mechanism
account, and (iii) three FROZEN predictions executed next patch. **Scope fence,
stated first:** everything here is derived about the REGISTERED ALGORITHM (the
2601-S2 sink as implemented in the registered 2602 engine) — engine-theorem
strength, explicitly NOT a world-call, no W-label. This cell is adjacent to and
does NOT preempt the FORM-1 dedicated session (the Morse-form derivation, panel-
demanded, still founder-placed); it hands that session a sharpened target. The
DISC block MOVES NOWHERE tonight regardless of outcome: any block-scope
modification this cell's results might motivate is drafted as a PROPOSAL for the
next CONV-001 dispatch, the founder's word as always.

## 1. T1 — the endpoint-ledger theorem (exact, by the engine's own bookkeeping)

The registered engine maintains, verbatim (2602, `n1_gamma`):

```
Sea += KEpre - rke(P)          # the split removes KE and books it, exactly
Etot = rke(P) + Us + Ue + Sea  # the conserved ledger
Edrift = max|Etot - E0|        # the measured violation
```

Therefore, **identically at every step and every γ**:

  Sea(t) = E0 − [KE(t) + U(t)] + δ(t),  |δ(t)| ≤ Edrift.

The deposit at time t is the initial energy minus the instantaneous mechanical
energy, up to measured integrator drift. **Corollary (the covered observable):**
for any encounter whose end state is dt-robust — a settled CAP cluster
(quasi-static under continued η-damping) or a separated SCA configuration
(incident free, target resettled) — Sea(t_end) inherits dt-convergence from two
dt-robust quantities: the endpoint mechanical energy and Edrift itself (measured
order-1, 2622 D1/D2). **The sink's derivation-covered observable at transit-γ is
the endpoint-ledger deposit S_end ≡ Sea at the asymptotic state, with convergence
band set by the drift band — at every γ the instrument reaches.** The shed
SCHEDULE (which cycle sheds what) appears nowhere in the identity: T1 is
schedule-blind by construction.

This derives, rather than merely observes, the DISC arc's cleanest fact: S_cum
held a 1.3–1.5% band at both anchors (2626) while every sub-window quantity
wandered — because S_cum is (up to window-end vs true-asymptote mismatch)
endpoint-determined, and nothing sub-window is.

## 2. T2 — schedule non-observability (the mechanism account)

Each split reads s_k = KE removed at t_k, a function of Vosc(t_k) — a PHASE SAMPLE
of the internal oscillation on the once-per-τ_C clock. A phase sample is covered
only where phase is robust to discretization. Phase error under the registered
first-order integrator grows ∝ ω × (accumulated timing error), and Morse
anharmonicity decoheres phase faster at larger amplitude (amplitude-dependent
frequency). Small-oscillation frequencies from the registered forms
(k = 2·E_QQ·β², β = w/D, m = 132): **ω(w=2) = 1.74 c/fm, ω(w=4) = 3.49 c/fm** —
the steep width samples phase twice as fast per unit timing error, and a transit-γ
encounter pumps large-amplitude anharmonic motion. Hence: sub-window sums are
covered in the phase-robust regime (soft, gentle) and uncovered outside it (steep,
violent) — the observed soft-vs-steep split, given a mechanism whose two legs
(stiffness, amplitude) are independently testable below.

## 3. Frozen predictions (executed next patch; kill-generous)

All runs fresh under this document, `n1_disc2` instrumentation (2626, pinned),
B1 geometry verbatim, b = 0, η = 0.5. "Final-inc" = |S(finest) − S(next)| / S(finest).

- **P1 — stiffness monotonicity (the founder's named target):** at v = 0.10,
  dt ∈ {1/100, 1/200, 1/400}, widths w ∈ {2, 3, 4}: the single-pass (W-A)
  final-inc is MONOTONE INCREASING in w. (w = 3 is a new width admitted here for
  instrument diagnosis only — no DM consumer may cite w = 3 results; it exists to
  test the account.) KILL: any non-monotone ordering kills the stiffness leg.
- **P2 — endpoint order:** S_cum final-inc at dt {1/200, 1/400, 1/800}, both
  anchors (v = 0.10 and 0.95, w = 4): increments FALL and the finest-pair
  final-inc ≤ the corresponding Edrift/S_cum ratio + 1% absolute. KILL: S_cum
  increments failing to fall at 1/800, or the band exceeding drift + 1%, kills
  T1's corollary as stated (the identity survives; the endpoint-robustness premise
  dies, and says so).
- **P3 — amplitude (gentleness) leg:** at w = 4, dt ∈ {1/100, 1/200, 1/400}:
  single-pass final-inc at v = 0.05 is SMALLER than at v = 0.10. KILL: P3 failing
  with P1/P2 passing kills the amplitude leg alone (stiffness account survives,
  recorded as partial).
- Readings: **RS-OBS-FULL** (P1 ∧ P2 ∧ P3) — the §4 answer registers with both
  mechanism legs; **RS-OBS-STIFF** (P1 ∧ P2, ¬P3) — registers with the stiffness
  leg only; **RS-OBS-LEDGER** (P2 only) — T1's corollary registers, the mechanism
  account fails, schedule non-observability stands empirically (2624/2626)
  without tonight's mechanism; **RS-OBS-DEAD** (¬P2) — the corollary is killed;
  the founder's question re-opens harder (adverse, same font). Fences: no DM
  consumers move; no block moves; w = 3 quarantined; 79.5% untouched.

## 4. The answer as it will be registered if P2 holds (draft, frozen now)

*The sink's derivation-covered observable at transit-γ is the endpoint-ledger
deposit S_end — total Sea at the asymptotic state — convergent at the integrator's
drift order at every tested γ, by the exact ledger identity T1. The shed schedule
(single-pass, per-cycle, any sub-window sum) is not an observable of the
discretized law outside the phase-robust regime, which is bounded by stiffness
[P1] and excitation amplitude [P3]. For the FORM-1 session: a continuum derivation
of the sink should reproduce T1's identity as its integral law and predict the
phase-robustness boundary that the discretized law exhibits — the soft-vs-steep
split is its acceptance test.*

**Proposal drafted for the next CONV-001 dispatch (founder's word on timing; NOT
in force):** amend the DISC block to distinguish endpoint-ledger deposits
(consumable at any γ with the drift band carried explicitly) from schedule
quantities (blocked pending FORM-1). Until dispatched and adjudicated, the block
stands whole.

## 5. Bookkeeping

Next patch: execution under §3 only. Verify script `code/2629_sink_obs1.py`.
