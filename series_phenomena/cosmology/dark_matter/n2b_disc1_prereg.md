# N2B-DISC-1 pre-registration: the strengthened sink-ON/sink-OFF single-transit discriminator + the 7D-funnel audit (FUNNEL-1 folded) — the amended N2-B-EDGE-2 cell, committed before any run

**Patch 2620, 20 July 2026. Status: N2B-DISC-1 OPENED at pre-registration; NO run
performed.** This is the queue-head cell registered at 2618 §5 (DISC-1, unanimous,
highest, BLOCKING for every high-γ consumer, all Sea-deposit-growth discussion, and
any H-a/H-b mechanistic preference), with FUNNEL-1 folded in as its second reading
per the same adjudication. It AMENDS the N2-B-EDGE-2 declaration (2609 §6): EDGE-2
item (ii) — the single-pass sink-ON/OFF shed measurement — is executed here at the
panel-strengthened spec (Seats 1 and 5); **EDGE-2 item (i) (the v ∈ {0.97, 0.99,
0.995} grid extension) is NOT run here** and remains a separately queued declared
member. Governed by this document, the 2618 condition spine, and the B1/H-γ prereg
lineage (2598/2601/2608) only. Verify: none at prereg.

## 0. Target and framing

The registered record shows deposits GROWING with v (301→580 MeV through 0.95c, 2609)
and a capture funnel reaching ≈7D of aim error (2612 — steep captured at ~7D off the
fixed column). The question this cell answers: **is the per-encounter Sea deposit a
physical quantity — parameter-driven, partition-independent, dt-convergent — or an
artifact of the window-mean velocity split that implements the sink?** Until answered,
every high-γ consumer is blocked (2618 HOLE-1, adopted at Seat 3's strength). The
funnel question rides the same instrument: **is the ≈7D reach sink-mediated, or does
it follow from the registered potentials alone?**

**Launch convention (MANDATORY clause, 2618 adoption i):** all launches use the
**registered B1 absolute-column protocol verbatim** (incident at [b·D, 0, 4D], V0 =
[0, 0, −v], square initialized centered at origin, zero net momentum). Drift
compensation stated in advance: the settled square's centroid displacement |Δcen| is
measured and reported per cell; any cell whose funnel/boundary reading coincides with
|Δcen| > 0.5D at the reading time is FLAGGED and re-run under centroid-relative aim
as a disclosed confirmation before its verdict is read. Existence/deposit readings on
the aimed-adjacent channels carry the FW-1 firewall sentence in every consumer.

## 1. Registered inputs (verbatim; zero freedom)

Engine: exec-load of the registered artifact `code/2602_hgamma_gates_b1.py` through
the same cut as 2609 — `n1_gamma`, `rung`, `strong_FU`, constants are the registered
objects. η_ON = 0.5 (the sole admitted point, 2602); η_OFF = 0.0 (identically the
split removed: Vn = Vbar + Vosc = V, deposit ≡ 0 by construction — Seat 5's
"split-removed" member exactly). Geometry: B1 verbatim (square = `rung(1)`, incident
qCP charge −1, `S='q'`, m = 132). Widths w ∈ {2.0, 4.0}. TC = 120, the registered B1
window. dt-union unconditional on every read (2609 confession, permanent).

**Instrumentation (declared, dynamics-invariant):** a wrapper `n1_disc` whose
state-update path is the verbatim `n1_gamma` body with LOGGING LINES ONLY added. At
each split event it records: t; total relativistic KE; **method-A partition**
(KE_trans^A = per-particle KE at the window-mean velocity Vbar_i; KE_osc^A =
KE_tot − KE_trans^A — the sink's own partition); **method-B partition**, independent
by construction (KE_trans^B = √((Σm)² + |P_tot|²) − Σm, the collective
momentum-based decomposition; KE_osc^B = KE_tot − KE_trans^B); the registered
deposit ΔSea; incident–centroid distance. Closest approach t_ca = argmin over steps
of that distance. **S_1pass** = Sea accumulated through splits with t ≤ t_ca + 2τ_C
(the single-pass shed, the EDGE-2(ii) quantity); **S_cum** = Sea at window end
(reported alongside, not gated — post-capture bound motion is chaos-exposed).
**D^B** = Σ over the same splits of (KE_osc^B,pre − KE_osc^B,post) — the deposit as
method B reads it.

## 2. Controls (gating; run FIRST; any failure stops the cell unread)

- **C1 — convention-pin (METH-L2-015):** `n1_disc` reproduces the registered 2609
  timing cell (w=4, b=0, v=0.40, dt=1/100): identical classification (CAP) and Sea,
  gmax to printed precision vs the registered `n1_gamma` run in the same process.
- **C2 — sink-OFF null:** η=0 at (w=4, b=0, v=0.10, dt=1/200): Sea = 0 to machine
  precision AND Edrift < FLOOR (2.0 MeV). (η=0 at v=0.95 reported, not gated —
  integrator error at γ 4.6 is a finding, not a gate.)
- **C3 — decomposition sanity:** the isolated settled square (no incident, η=0.5,
  TC=60): KE_trans^A and KE_trans^B each < 1 MeV at every split — an object at rest
  has no translational KE under either method.

## 3. Members (frozen grids)

- **M1 — component tracking (spec a):** v ∈ {0.10, 0.40, 0.95} × b ∈ {0.0, 1.0}D ×
  w ∈ {2.0, 4.0}, η = 0.5, dt = 1/100. Per-split component logs; report S_1pass,
  S_cum, D^B, f_1pass = S_1pass/S_cum, |Δcen|. Disclosed in advance: at v = 0.95 the
  encounter spans ~1–3 split events; the profile reads what the instrument has.
- **M2 — dt-convergence × partition-independence (specs b+c):** anchors (v=0.10,
  b=0, w=4) and (v=0.95, b=0, w=4); dt ∈ {1/50, 1/100, 1/200, 1/400}. Gates read on
  S_1pass: (i) shrinking increments |S(1/400)−S(1/200)| ≤ |S(1/200)−S(1/100)| and
  final increment ≤ 5% of S(1/400), per anchor; (ii) method agreement
  |D^B − S_1pass|/S_1pass ≤ 0.10 at dt = 1/200 and 1/400, per anchor.
- **M3 — physical vs implementation (spec d):** physical spread = max−min of S_1pass
  across the M1 v-grid at (b=0, w=4, dt=1/200, method A); implementation spread =
  max−min across {dt 1/100, 1/200, 1/400} ∪ {method A, B} at each M2 anchor. Gate:
  implementation spread ≤ 20% of physical spread at BOTH anchors.
- **M4 — trajectory comparison split-ON/OFF (spec e):** identical launches, η = 0.5
  vs 0.0, at (v, b, w) ∈ {0.10, 0.95} × {0.0, 1.0}D × {4.0} plus (0.10, 0.0, 2.0),
  dt = 1/100 with dt = 1/200 confirmation on any cell whose ON/OFF classification
  pair differs between dt values. Raw table registers: classification pairs, final
  incident distance, S_1pass(ON).
- **M5 — FUNNEL-1:** (i) **analytic member, zero freedom:** the registered
  incident-well W(b) (Morse qq + alternating electric, the 2609 E-A well machinery
  reused for the WELL ONLY — the failed transit-shed model is NOT consumed), b ∈
  [0, 10]D both widths; report b_W = largest b with W(b) ≥ KE_inc(0.10c) =
  m(γ−1) ≈ 0.665 MeV. (ii) **numeric member:** capture scan at v = 0.10c, b ∈
  {1, 2, 3, 4, 5, 6, 7, 8}D, η ∈ {0.5, 0.0}, w ∈ {2.0, 4.0}, dt = 1/100;
  **dt-union 1/200 on the boundary bracket** (largest-b CAP, smallest-b non-CAP
  above it) per family. R_f = largest dt-stable CAP offset per (η, w).

## 4. Frozen readings

- **RD1 — DISCRIMINATOR CLEAN:** C1–C3 pass; M2 gates (i) and (ii) pass at both
  anchors; M3 passes → registers: **the per-encounter deposit is
  PHYSICAL-PARAMETER-DRIVEN and partition-independent within stated tolerance; the
  DISC-1 BLOCK LIFTS** — high-γ consumers, Sea-deposit-growth discussion, and
  H-a/H-b work re-open, each citing this record. f_1pass profiles register as DATA;
  **no H-a/H-b promotion occurs in this cell** (a preference, if ever taken, is its
  own registered act consuming these profiles).
- **RD2 — PARTITION-SUSPECT (adverse):** any M2/M3 gate fails dt-stably → the
  deposit registers IMPLEMENTATION-DEPENDENT in the failing regime; **the block
  STANDS and hardens** (scope named by the failing gate); model repair is a NEW
  candidate entering at the top. Recorded in the same font as a win.
- **RD3 — UNSTABLE / CONTROL FAILURE:** nothing reads; defect hunt next; the cell
  re-enters only via corrected prereg (the RC4 discipline).
- **RF1 — SINK-MEDIATED FUNNEL:** R_f(ON) − R_f(OFF) ≥ 2D with the analytic
  b_W ≪ R_f(ON) → the funnel classifies as SINK-MEDIATED and is BOUNDED by R_f(ON)
  per width (dt-stable); the 2612 "~7D reach" gets its mechanism class.
- **RF2 — POTENTIAL/DYNAMICS-DRIVEN:** R_f(ON) − R_f(OFF) < 1D → the funnel is NOT
  a sink artifact; the bound registers with the analytic member's account.
- **RF-INT:** 1D ≤ difference < 2D → MIXED registers with both bounds; no class.
- **Fences:** no rate claims, no σ_cap, no relic contact; EDGE-2(i) not run; the
  σ_cap 0.95c extension stays WITHHELD; nothing here alone enables
  promotion-adjacent citation (REPL-1 and the spine stand); 79.5% untouched.

## 5. Bookkeeping

Next patch: execution under this document only. Verify script
`code/2621_n2b_disc1.py`. Foreground-sized, chunked per member; background jobs die
at turn boundaries (standing discipline).
