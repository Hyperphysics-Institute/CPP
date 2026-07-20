# N2B-ROB-3 execution record — VERDICT RS-W-DEPENDENT × 2: BOTH CELLS COMPLETE DT-STABLY AT w = 2; THE STAGE-7 WALLS ARE STEEP-ONLY — STIFFNESS ENTERS THE MARGINAL-AIM BOUNDARY; THE SOFT ENVELOPE IS WALL-FREE ON THE TESTED GRID

**Patch 2644, 20 July 2026.** Execution under `n2b_rob3_prereg.md` (2643) only.
Verify: `code/2644_n2b_rob3.py` (stages controls | cells run; escalate NOT run —
no dt-disagreement anywhere; refine NOT run — its frozen trigger, Cell A-soft
halting, never fired).

## 1. Controls: BOTH PASS

- **C-S1 (matched soft registered channel):** COMPLETE, every stage
  CAP/dt-STABLE, settle **0.84/0.86/0.01** — the exact RS1/2631 soft-row
  numbers, reproduced by the matched instrument unasked (the gate demanded only
  completion + dt-stability; the decimal agreement is the second happy accident
  of its kind, disclosed as such and still not a requirement).
- **C-S2 (drawn-soft-cell conservatism, φ = 30°):** COMPLETE, dt-stable,
  settle 0.84/0.86/0.00. No drawn cell flips. The cells read.

## 2. The two cells: BOTH COMPLETE, EVERY PAIR DT-STABLE

```
CELL A-soft  phi=45  (w=2): st5-st8 all CAP/CAP dt-STABLE
  settle 0.84/0.87/0.01  — CANONICAL geometry class
CELL B-soft  +y face (w=2): st5-st8 all CAP/CAP dt-STABLE
  settle 1.01/1.26/0.01  — the DISTINCT geometry class
```

No FRG; no escalation trigger (16 of 16 stage-verdict pairs agree; the matched
instrument's running total across ROB-2 + ROB-3 is now **30 of 30
dt-agreements**). The refinement's license (Cell A-soft halting) never issues;
φ = 37.5° at w = 2 does not run and the steep bracket question dissolves at
this width — there is no soft wall to bracket.

## 3. Reading (frozen at 2643 §4): RS-W-DEPENDENT for both cells

**The walls are width-DEPENDENT — steep-only.** At w = 2 the chain completes at
φ = 45° and on the +y face where w = 4 halts dt-stably (2638). The soft
envelope on the tested grid is **wall-free**: ≥ 2.0D offset (2631 soft rows),
the full tested orientation range through 45°, and **4 of 4 faces**. The FORM-1
exhibit gains the stiffness clause, per the frozen reading: **the stage-7
marginal-aim boundary is stiffness-coupled** — the steep target presents
capture walls the soft target does not.

**Coherence observations, registered without claim:** (i) this is the third
independent appearance of stiffness as the discriminating axis in the N2-B
family — the DISC arc's deposit sensitivity is stiffness-coupled (w = 4
phase-sensitive, w = 2 convergent at 0.8%, 2626), the SINK-OBS-1 mechanism leg
is stiffness-monotone (2629 P1), and now the marginal-aim walls exist at the
stiff width only; (ii) the funnel's width wash-out (2642: ON reach
width-identical) and tonight's width-dependent walls are NOT in tension — the
funnel is a single capture at generous aim where the sink dominates; the walls
live at marginal aim against the grown asymmetric 6-object, where the well's
forgiveness (b_W(w2) = 4.5D vs 2.5D) plausibly buys the soft width its
completions. Both routings are FORM-1's to derive.

**Raw geometry observation (extends the 2631/2638 exhibit):** at w = 2 the
face map sorts into two settled-geometry classes — ±z and φ-perturbed +z
launches settle CANONICAL (0.84/0.86–0.87), while BOTH off-axis faces settle
the DISTINCT class (+x: 1.01/1.27 at 2631; +y: 1.01/1.26 tonight — matching to
the second decimal across different faces). The distinct class is a
face-family property, not a +x accident. Registered as raw shape numbers for
the FORM-1 agenda; no isomer/orientation classification tonight.

## 4. Standing

**ROB-3 is DISCHARGED** — the width-sharing sentence is answered: the walls are
steep-only, the soft envelope is wall-free on the tested grid, and the FORM-1
anisotropy exhibit now carries three coordinated exhibits (the steep walls with
the (37.5°, 45°] bracket; the two-class settled-geometry face map, now
width-replicated for the distinct class; the stiffness-coupling clause).
Consumer sentence licensed (FW-1 riding): *"under the aimed convention the
soft-width (w = 2) assembly chain completes across the full tested perturbation
grid — ≥ 2.0D offset, orientations through 45°, all four tested faces — while
the steep-width (w = 4) chain presents dt-stable walls at (37.5°, 45°] and +y;
the marginal-aim boundary is stiffness-coupled."* DEP-1 row appended at this
patch. Fences held: existence only; no rates; endpoint-ledger deposits only;
v = 0.10c, DISC block untouched; the steep walls of 2638 untouched (this record
reads the soft width only); 2631/2638 records unedited; **79.5% untouched.**

**The founder-free queue is EMPTY — including the optional item.** The
founder's packet (2636 §4) is unchanged by Patches 2637–2644: zero flags
raised, zero amendments needed; the eight patches add one candidate line to
the FORM-1 agenda (the three-exhibit set above) that travels with the standing
FORM-1 founder-placed item, not with the dispatch.
