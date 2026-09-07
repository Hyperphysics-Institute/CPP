# Record correction (handover item 4, owed since 3643 §1): 3390's odd-sector line at 8M/3 — "208 Hz, Q 7.9, a healthy sharp line" — was computed with J = 6.75, the 9M/4 slowness. With the 8M/3 value J = 32/9 the same wall gives 0.4501 − 0.1246 i: 235 Hz, Q 1.8 — broad and Dirichlet-like, +20.5% / −28.6% from Schwarzschild, outside the ringdown box like every lossless-transmit wall (3644). The odd sector's "sharp 208 Hz line" was the wrong slowness, not physics. Not a live line: the flat-core transmit belongs to the excluded extension

**Patch 3660, Session 164, 7 Sep 2026.** Verify `code/3660_odd_sector_8M3_J32_9_rerun_verify.py` (5/5; run from the repo root; exec's 3390's machinery). Reasoning `reasoning/3660.md`. No paper touched.

## §1 What was wrong
3384's odd wall (lossless transmit into a flat core of isotropic radius r̄ = 1.5, ψ_in ∝ x j₂(x), x = Jω r̄, junction dψ/dr* = (1/J) dψ_in/dr̄) carries the slowness J = dr*/dr̄ at the surface. 3389 asserted "J = 6.75 at any wall"; the dictionary `dr*/dr̄ = ψ(1 − v/2)/f` gives 6.75 at 9M/4 (v = 1) and **32/9 = 3.556 at 8M/3** (v = 2/3) — 3643 §1. 3390 moved the surface to 8M/3 and kept 6.75.

## §2 The re-run
3390's number is reproduced first (0.4000 − 0.0252 i, 208 Hz, Q 7.9). Tracking the branch J = 6.75 → 6 → 5 → 4.5 → 4 → 32/9:

| J | ω | Hz @62 | Q |
|---|---|---|---|
| 6.75 (3390) | 0.4000 − 0.0252 i | 208 | 7.9 |
| 5.0 | 0.4457 − 0.0717 i | 232 | 3.1 |
| **32/9 (corrected)** | **0.4501 − 0.1246 i** | **235** | **1.8** |

r₀-independent to 4e−8. Against the Schwarzschild ℓ = 2 fundamental: δf +20.5%, δτ −28.6% — outside GW150914's box, the signature of a lossless transmit wall (3644 A1: +23% / −32% in the even sector; 3643's even flat-core line at J = 32/9 is 0.4460 − 0.1411 i, 232 Hz, Q 1.6 — the two sectors now sit together).

## §3 Standing
- **Superseded:** 3390 §2's odd row ("208 Hz, Q 7.9, healthy") and 3390's "the odd sector is healthy: a sharp line" as a contrast with the even sector — the contrast was the slowness. 3384's 9M/4 odd line (J = 6.75 was right there) is untouched.
- Nothing live changes: the flat-core transmit reading is the excluded extension's (3653), and every lossless-transmit wall fails the ringdown damping (3644). The corrected number replaces the wrong one in the record; PRED-O-39's V1.9 "208 Hz (axial)" model pole is owed the correction at V2.3 with the rest of the package (the axial model line at 8M/3 is 235 Hz, Q 1.8, not 208 Hz, Q 8).
- Item 4 of the 163 handover discharged.
