# SINK-OBS-1 execution record — VERDICT RS-OBS-FULL: THE ENDPOINT-LEDGER OBSERVABLE REGISTERS, WITH BOTH MECHANISM LEGS; THE FOUNDER'S QUESTION HAS ITS ANSWER AT ENGINE-THEOREM STRENGTH

**Patch 2629, 20 July 2026.** Execution under `sink_obs1_derivation_prereg.md`
(2628) §3 only. Verify: `code/2629_sink_obs1.py` (stages p1 | p2 | p3, all run).
Instrument: `n1_disc2` verbatim from the pinned 2626 artifact.

## 1. Raw outputs (verbatim)

```
[P1] v=0.10, single-pass (W-A) final-inc vs width:
  w=2: S_WA(1/100,200,400) = 149.86, 151.10, 151.72   final-inc 0.0041
  w=3: S_WA = 122.68, 149.74, 161.40                  final-inc 0.0722   [DIAGNOSTIC-QUARANTINED]
  w=4: S_WA = 228.35, 203.85, 182.72                  final-inc 0.1156
  MONOTONE-INCREASING: True
[P2] S_cum, w=4, dt 1/200 -> 1/400 -> 1/800:
  v=0.10: 296.83, 292.53, 292.88   increments 4.30 -> 0.35 FALLING
          final-inc 0.0012 <= Edrift/S + 1% = 0.0252   (Edrift 14.70 -> 8.40 -> 4.45)
  v=0.95: 579.69, 572.47, 575.57   increments 7.21 -> 3.10 FALLING
          final-inc 0.0054 <= 0.0183                   (Edrift 34.12 -> 9.55 -> 4.78)
[P3] w=4, single-pass final-inc: v=0.05 -> 0.0365  <  v=0.10 -> 0.1156   True
```

## 2. Reading (frozen at 2628 §3): RS-OBS-FULL — P1 ∧ P2 ∧ P3 all pass

- **P1 (the founder's named target):** convergence quality is strictly monotone in
  stiffness — 0.41% → 7.2% → 11.6% across w = 2 → 3 → 4 — with the diagnostic
  width landing BETWEEN the registered widths exactly as the zero-fit ω-scaling
  (1.74 → 2.61 → 3.49 c/fm) requires. The stiffness leg of T2 stands.
- **P2 (the corollary in its own currency):** the endpoint-ledger deposit
  converges at BOTH anchors with falling increments through dt = 1/800, final
  increments 0.12% and 0.54%, each inside its own measured drift band. T1's
  corollary stands: **S_end is dt-convergent at drift order at low AND transit γ.**
  (At transit-γ, where every sub-window quantity failed two discriminators, the
  endpoint ledger holds a half-percent band.)
- **P3:** gentler excitation at fixed stiffness improves single-pass convergence
  3× (3.7% vs 11.6%). The amplitude leg stands.

## 3. THE REGISTERED ANSWER (the 2628 §4 draft, now in force at its stated strength)

**The sink's derivation-covered observable at transit-γ is the endpoint-ledger
deposit S_end — total Sea at the asymptotic state — convergent at the integrator's
drift order at every tested γ, by the exact ledger identity T1 (engine-theorem
strength; NOT a world-call). The shed schedule (single-pass, per-cycle, any
sub-window sum) is not an observable of the discretized law outside the
phase-robust regime, which is bounded by stiffness [P1] and excitation amplitude
[P3]. For the FORM-1 session: a continuum derivation of the sink should reproduce
T1's identity as its integral law and predict the phase-robustness boundary the
discretized law exhibits — the soft-vs-steep split is its acceptance test, now
three-point calibrated (0.41% / 7.2% / 11.6% at ω = 1.74 / 2.61 / 3.49 c/fm).**

## 4. Standing

The DISC block MOVES NOWHERE (as fenced): the amendment proposal (endpoint-ledger
deposits consumable with drift band vs schedule quantities blocked pending FORM-1)
sits drafted at 2628 §4 for the next CONV-001 dispatch — the founder's word on
timing. w = 3 results are quarantined (diagnostic only, no DM consumer). The DISC
arc's ledger updates: 2624 convicted a window; 2626 exonerated windows and
convicted the schedule; 2629 registers WHY, and names the one deposit object the
law actually owns. ETA-1's rider language now has a derivational referent.
FUNNEL-1 unchanged; EDGE-2(i) queued; no rates, no σ_cap, no relic contact;
**79.5% untouched.** Founder-free queue after this patch: ROB-1, R-B items 1–4.
Founder-placed queue: REPL-1 dispatch, FORM-1 dedicated session (agenda now two
items with the acceptance test above), the CONV-001 amendment dispatch when ready.
