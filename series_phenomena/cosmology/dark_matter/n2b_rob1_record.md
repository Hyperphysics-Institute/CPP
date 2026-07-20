# N2B-ROB-1 execution record — VERDICT RR2 (DISCHARGED-WITH-BOUNDS): THE AIMED CONVENTION'S ENVELOPE IS WIDE WHERE DRAWN (≥2.0D OFFSET, ≥30° ORIENTATION, 3 OF 4 FACES), WIDTH-SHARED, WITH TWO CELLS UNDRAWN-AT-THIS-INSTRUMENT

**Patch 2631, 20 July 2026.** Execution under `n2b_rob1_prereg.md` (2630) only.
Verify: `code/2631_n2b_rob1.py` (stages control | f1 | f2 | f3 | soft, all run;
the soft stage's survivor rows were finalized to the steep outcome per the
prereg's own §1 definition before the soft stage ran).

## 1. C-R′ — the gating control: PASS

The uniform aimed launcher completes the registered chain 4→8 at w = 4, every
stage CAP/dt-STABLE, settle **Rrms = 0.91, dmax = 1.06, Edrift = 0.01** — on the
registered steep benchmarks. The cell reads.

## 2. Family results (w = 4)

```
F1 lateral offset:  b=0.0  COMPLETE   b=1.0  COMPLETE   b=1.5  COMPLETE   b=2.0  COMPLETE
                    (settles 0.91–0.94 / 1.04–1.24 / Edrift ≤ 0.01)
F2 orientation:     phi=15 COMPLETE   phi=30 COMPLETE
                    phi=45 HALT@st7 — dt-UNSTABLE (1/100 SCA, Sea=3, gmax=1.01; 1/200 CAP)
F3 approach face:   +x COMPLETE (settle Rrms=1.17, dmax=1.70 — bounded, distinct geometry)
                    -z COMPLETE (0.91 / 1.06)
                    +y HALT@st7 — dt-UNSTABLE (1/100 SCA, Sea=2, gmax=1.01; 1/200 CAP)
```

## 3. Soft confirm rows (w = 2): ALL COMPLETE

Registered channel 0.84/0.86/0.01 (the exact 2616 RS1 numbers, reproduced);
b = 2.0D → 0.84/0.87; φ = 30° → 0.84/0.86; +x face → 1.01/1.27 (the distinct
face geometry REPLICATES at the soft width). **The drawn envelope is
width-shared at every tested survivor.**

## 4. Reading (frozen at 2630 §4): RR2 — DISCHARGED-WITH-BOUNDS

**The envelope, where dt-stable:** the chain completes under uniform systematic
aim error of at least **2.0D lateral offset (grid-exceeded), at least 30°
orientation error, and on 3 of 4 tested approach faces**, at BOTH widths on every
tested survivor. Stage-of-first-failure map: every non-completion is **stage 7**
— the first launch against the grown, asymmetric 6-object.

**Two cells register UNDRAWN-AT-THIS-INSTRUMENT (φ = 45°, +y face):** both halts
are dt-UNSTABLE with an identical disclosed signature — at dt = 1/100 the
incident MISSES cleanly (Sea = 2–3 MeV, γmax = 1.01, no engagement) while at
dt = 1/200 it captures. Instrument disclosure: the registered launcher's 1/200
economy leg briefly re-settles the object before launch (2611, cited in the
prereg lineage), so the two dt legs launch at marginally different object states
— invisible everywhere else, visible exactly at marginal aim against the
asymmetric 6-object. Per the frozen readings, no wall is drawn at these cells;
they are neither completions nor boundaries. Successors declared (NOT run):
finer-dt and/or economy-leg-matched re-runs of the two cells; a φ ∈ (30°, 45°)
refinement if a wall is wanted rather than bracketed.

**Raw observation, registered without claim:** the +x-face chain settles into a
BOUNDED but geometrically distinct 8-object at both widths (steep 1.17/1.70 vs
canonical 0.91/1.06; soft 1.01/1.27 vs 0.84/0.86) — a face-dependent final
geometry (isomer or orientation question; N3- and FORM-relevant; no
classification tonight).

**No FRG fired anywhere** (48 stage runs) — consistent with the 2609 robustness
lineage.

## 5. Standing

**ROB-1 is DISCHARGED-WITH-BOUNDS** — Seat 1's condition is satisfied with the
envelope drawn above and its two undrawn cells named. Consumer sentence licensed
by this record (FW-1 riding): *"the aimed-convention existence claim tolerates
systematic aim error to at least 2.0D offset and 30° orientation at both widths;
the tested envelope's walls, where they exist, sit beyond the tested grid or at
marginal-aim cells the instrument cannot yet draw."* Fences held: existence
only; no rates; deposits quoted are endpoint-ledger values (SINK-OBS-1); DISC
block untouched; 79.5% untouched. Post-win spine status: DISC-1 executed-adverse
(block in force, amendment drafted), FUNNEL-1 discharged-at-class, **ROB-1
discharged-with-bounds**, DEP-1 discharged, CORR-1 discharged, FW-1/ETA-1/AMB-1
riders in force, REPL-1 + FORM-1 founder-placed. Founder-free queue after this
patch: **R-B items 1–4** (the last founder-free items standing).
