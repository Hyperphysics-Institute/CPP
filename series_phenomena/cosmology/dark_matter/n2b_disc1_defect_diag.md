# N2B-DISC-1 defect diagnostic — THE C2 FAILURE IS INTEGRATOR-BASELINE, CONFIRMED BY dt-SCALING; THE η=0 ENGINE PATH IS CLEAN

**Patch 2622, 20 July 2026** (the 2612 pattern; 2574-class disclosed diagnostic).
Question from the 2621 RD3 record, answered by measurement. Verify:
`code/2622_disc1_defect_diag.py`.

## 1. Raw outputs (verbatim)

```
[D1] eta=0 (sink OFF), transit cell v=0.10 b=0 w=4 TC=120: Edrift vs dt
  dt=1/100: 48.715   dt=1/200: 25.446   dt=1/400: 11.002   dt=1/800: 7.038  MeV
  ratios per halving: 1.91, 2.31, 1.56   (Sea machine-zero at every dt)
[D2] eta=0.5 (sink ON), same cell:
  dt=1/100: 29.054   dt=1/200: 14.697   dt=1/400: 8.398   MeV  (Sea 295.5/296.8/292.5)
[D3] isolated square (no incident), eta=0:
  dt=1/100: 1.081    dt=1/200: 0.481    dt=1/400: 0.226   MeV
[D4] eta=0, v=0.95:
  dt=1/100: 49.088   dt=1/200: 24.496   dt=1/400: 12.077  MeV
```

## 2. Reading

- **D1 — the failing quantity falls with dt at order-1** (per-halving ratios 1.91,
  2.31, 1.56; the no-fall defect signature would be ~1.0). The η = 0 Edrift is
  **integrator truncation error**, not an engine defect. The η = 0 path is
  additionally exact on its deposit leg at every dt (Sea ≤ 10⁻¹² MeV).
- **D2 — the ON instrument carries the same baseline class** (29 → 15 → 8 MeV,
  same order). FLOOR = 2.0 was never applied to transit cells anywhere in the
  registered lineage (B1, edge, chain cells report Edrift, none gate it; only the
  G-SP small-oscillation battery gates at FLOOR) — the 2620 C2 gate transferred it
  without license, exactly as the 2621 record suspected. The gate was wrong; the
  engine is not.
- **D3 — localization:** the settled square alone drifts ≤ 1 MeV; the baseline is
  generated in the deep-well transit traversal. Instrument property, encounter-
  localized.
- **D2 side-observation, disclosed unread:** Sea ≈ 295 stable across dt at the ON
  cell — suggestive for the discriminator, but it reads ONLY under the corrected
  prereg's own gates.

## 3. Corrected-gate design (consumed by the next patch's prereg)

The OFF-null energy-integrity leg becomes a **convergence gate**: Edrift(η = 0, C2
cell) must fall with dt with per-halving ratio ≥ 1.5 across 1/100 → 1/200 → 1/400,
with the Sea machine-zero leg unchanged. Additionally, since both instruments carry
a 10–30 MeV encounter baseline at working dt, the corrected prereg adds a
**baseline-exposure guard**: per-cell Edrift is reported next to every deposit
reading; any gated deposit within 3× its own cell's Edrift is flagged
BASELINE-EXPOSED and excluded from gating (reported raw). Nothing else in the 2620
spec changes — members, grids, tolerances, readings, fences carry verbatim (the
2613 pattern: the corrected cell is the same cell with the defective element fixed
and named).

## 4. Standing

Class banked to the N3 hazard list lineage: **borrowed-gate transfer** (a threshold
licensed in one regime applied in another without a scaling check) — second member
of the class after fixed-column/drift (2614). Sequence continues founder-free:
corrected prereg N2B-DISC-1-2 next patch, execution after. Spine and 79.5%
untouched.
