# N2B-DISC-1 execution record — VERDICT RD3 (CONTROL FAILURE; THE CELL STOPS UNREAD)

**Patch 2621, 20 July 2026.** Execution under `n2b_disc1_prereg.md` (2620) only.
Verify script: `code/2621_n2b_disc1.py`, stage `controls`. **Only the control stage
was executed; per the prereg's frozen rule ("run FIRST; any failure stops the cell
unread") members M1–M5 were NOT run and nothing substantive is read from this cell.**
The RC4 discipline governs: raw disclosed below, nothing read, re-entry only via
corrected prereg.

## 1. Raw control outputs (disclosed verbatim)

```
[C1] registered: CAP Sea=304.706982 gmax=2.097582
[C1] n1_disc   : CAP Sea=304.706982 gmax=2.097582
[C1] match: cls=True dSea=0.00e+00 dg=0.00e+00
[C2] eta=0 v=0.10 dt=1/200: Sea=-1.421e-13 (|Sea|<1e-6: True) Edrift=25.446 (<FLOOR 2.0: False)
[C2r] eta=0 v=0.95 dt=1/200 (reported): Sea=-8.527e-14 Edrift=24.496 cls=SCA
[C3] isolated square: max ktA=0.0079 max ktB=0.0000 MeV (both <1: True)
```

## 2. Reading (controls only; frozen at prereg §2/§4)

- **C1 — convention-pin (METH-L2-015): PASS, exact.** The instrumented engine
  reproduces the registered 2609 timing cell bitwise on classification, Sea, and
  gmax (ΔSea = 0.0, Δgmax = 0.0). The instrumentation is dynamics-invariant as
  declared.
- **C2 — sink-OFF null: FAIL on the Edrift leg.** Sea = −1.4×10⁻¹³ MeV — the
  machine-zero deposit confirms η = 0 is algebraically the split removed, exactly as
  the prereg stated. But Edrift = 25.4 MeV ≫ FLOOR = 2.0 at (v = 0.10, dt = 1/200).
  Verdict: **RD3 — control failure; the cell stops unread.**
- **C3 — decomposition sanity: PASS.** Isolated settled square: max KE_trans^A =
  0.008 MeV, max KE_trans^B = 0.000 MeV — both methods read zero translational KE
  for an object at rest.

## 3. What is and is not established by this record

Established: the instrumentation is faithful (C1 exact); the two decompositions are
sane at rest (C3); η = 0 deposits exactly nothing (C2's Sea leg). NOT established:
anything about deposit physicality, partition-independence, dt-convergence, the
funnel, or ON/OFF trajectory behavior — none of it ran. The DISC-1 BLOCK STANDS
UNCHANGED (it neither lifts nor hardens on a control failure; the discriminator has
simply not yet been executed).

## 4. The defect question (declared; diagnostic is the next patch)

The failing gate transferred FLOOR = 2.0 MeV from the registered G-SP lineage
(at-equilibrium HOLD tests, small oscillation, sink ON) to a full 5-body transit
with the sink OFF. Candidate diagnosis, to be TESTED not asserted: with η = 0 there
is no sink continuously draining oscillatory energy, so bare integrator truncation
error on the stiff Morse wells accumulates undamped — a property of the instrument
baseline, not of the physics under test. Discriminating measurement (next patch, the
2612 pattern): Edrift(η = 0) vs dt across {1/100, 1/200, 1/400, 1/800} at the C2
cell. If drift falls with dt at a clean order, the corrected prereg gates the OFF
null on convergence (order + dt-scaled bound); if it does not fall, the engine has
an η = 0 defect and the hunt widens. **Nothing about the corrected gate is chosen
until the diagnostic reads.**

## 5. Standing

Prereg 2620 is SPENT (its C2 gate as frozen cannot pass on this instrument; preregs
are never edited post-hoc). Sequence forward, founder-free: defect diagnostic (next
patch) → corrected prereg N2B-DISC-1-2 → execution. The 2618 condition spine,
EDGE-2(i), FW-1, and 79.5% are all untouched. This record is written in the same
font as a win.
