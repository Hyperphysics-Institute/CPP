# N2B-ROB-2 execution record — VERDICT RM1-WALL × 2 (BOTH CELLS DRAWN): THE MATCHED INSTRUMENT DRAWS BOTH WALLS DT-STABLY; THE ORIENTATION WALL BRACKETS TO (37.5°, 45°]; +y IS A FACE WALL; THE 2631 MARGINAL-CAPTURE LEGS WERE THE ECONOMY LEG'S ARTIFACT

**Patch 2638, 20 July 2026.** Execution under `n2b_rob2_prereg.md` (2637) only.
Verify: `code/2638_n2b_rob2.py` (stages controls | cells | refine run; escalate
NOT run — its frozen trigger, persistent dt-disagreement, never fired).

## 1. Controls: BOTH PASS — the instrument change is conservative

- **C-M1 (matched registered channel, w = 4):** COMPLETE, every stage
  CAP/dt-STABLE, settle **Rrms = 0.91, dmax = 1.06, Edrift = 0.01** — the exact
  ROB-1 registered-channel settle numbers reproduced under the matched launcher.
- **C-M2 (drawn-cell conservatism, φ = 30°):** COMPLETE, every stage
  CAP/dt-STABLE, settle 0.91/1.04/0.00. Deleting the economy leg flips NO drawn
  cell. The cells read.

## 2. The two cells: BOTH HALT@st7, BOTH dt-STABLE — RM1-WALL × 2

```
CELL A  phi=45  (axis +z, b=0.5D, w=4):
  st5 CAP/CAP  st6 CAP/CAP  (dt-STABLE)
  st7: 1/100 SCA  1/200 SCA  dt-STABLE  Sea=3/3 MeV  gmax=1.01/1.01  — clean miss, both legs
CELL B  +y face (b=0.5D, phi=0, w=4):
  st5 CAP/CAP  st6 CAP/CAP  (dt-STABLE)
  st7: 1/100 SCA  1/200 SCA  dt-STABLE  Sea=2/2 MeV  gmax=1.01/1.01  — clean miss, both legs
```

No FRG anywhere; both halts leave the 6-object intact (SCA classification, not
fragmentation). The escalation rung never triggers: with both legs launched at
the identical object state, the two dt legs agree at every stage of every chain
run tonight (14 stage-verdict pairs, 14 agreements).

**The 2631 signature is resolved:** under the economy launcher the 1/200 leg
CAPTURED at exactly these cells; under the matched launcher both legs MISS with
the same Sea = 2–3 MeV / γmax = 1.01 signature the 1/100 leg always showed. The
marginal capture was the re-settled object's artifact, not the encounter's
physics. The 2631 refusal to draw walls from a self-disagreeing instrument is
vindicated in both directions: the instrument was indeed the problem, and the
wall it obscured is real.

## 3. Conditional refinement (frozen trigger fired): φ = 37.5° COMPLETES

Every stage CAP/dt-STABLE, settle Rrms = 0.95, dmax = 1.27 (BOUNDED),
Edrift = 0.00. **The orientation wall brackets to (37.5°, 45°]** at w = 4 under
the matched instrument.

## 4. Reading (frozen at 2637 §4): RM1-WALL for both cells

**The envelope, now with drawn walls (w = 4, matched instrument):** the chain
completes under uniform systematic aim error of at least **2.0D lateral offset
(grid-exceeded), at least 37.5° orientation error** (wall inside (37.5°, 45°]),
**on 3 of 4 tested approach faces, with +y a drawn face wall**. Every
non-completion remains stage 7 — the first launch against the grown asymmetric
6-object — and every stage-7 halt is now a dt-stable clean miss.

**Structure registered (FORM-relevant, no classification tonight):** the
completion map over approach faces is strongly anisotropic at stage 7 — +z/−z
complete canonically, +x completes into a geometrically distinct bounded
8-object (2631 raw observation), +y misses entirely. Together with the
orientation wall, the grown 6-object's stage-7 capture cross-section depends on
presentation direction — an anisotropy exhibit for the FORM-1 agenda alongside
the +x-geometry numbers.

**Scope disclosures:** walls are drawn at w = 4 only; the ROB-1 soft-width
confirm rows tested survivors, not walls, so the walls' width behavior is
undetermined (optional successor, declared not queued: φ = 45° and +y at
w = 2). All results are aimed-convention results; FW-1 rides.

**ROB-1 supersession by citation (record not edited, per fence):** the ROB-1
consumer sentence is superseded by: *"the aimed-convention existence claim
tolerates systematic aim error to at least 2.0D offset and 37.5° orientation at
the steep width (offset wall beyond the tested grid; orientation wall inside
(37.5°, 45°]); the face map is 3-of-4 with +y a drawn wall; the soft-width
confirm rows of 2631 stand on the drawn survivors."* The two UNDRAWN entries in
the 2631 record are superseded: both cells are DRAWN as boundaries.

## 5. Standing

**ROB-1's discharge upgrades from DISCHARGED-WITH-BOUNDS to
DISCHARGED-WITH-DRAWN-WALLS** — the envelope has no undrawn cells at the tested
grid. Fences held: existence only; no rates; deposits quoted are endpoint-ledger
values (SINK-OBS-1); DISC block untouched (v = 0.10c throughout); the 2631
record unedited; **79.5% untouched.** Post-win spine: DISC executed-adverse
(block in force, amendment drafted), FUNNEL-1 discharged-at-class, **ROB-1/ROB-2
discharged-with-drawn-walls**, DEP-1 discharged (one new row owed: this record's
walls sit on {aimed convention, γ-member} axes, sink-independent — the halts are
misses with Sea ≈ 0), CORR-1 discharged, FW-1/ETA-1/AMB-1 riders in force,
REPL-1 + FORM-1 founder-placed. Remaining declared founder-free successors:
funnel upper bound b > 8D; w = 2 OFF finer-dt; (optional, declared tonight)
soft-width wall confirmation.
