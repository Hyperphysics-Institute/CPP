# The calibrated predictions: with the wall impedance fixed by GW150914's ringdown (β = −0.025 ± 0.005), the R-core's lines are 159 Hz (2,−2) and 255 Hz (3,−3) at χ = 0.68, and 200 / 319 Hz at a = 0 — with a residual the calibration itself predicts: the ringdown damping time 18% shorter than Kerr's

**Patch 3618, Session 161, 4 Sep 2026.** Verify `code/3618_calibrated_predictions_verify.py` (5/5; nothing new in the machinery). Reasoning `reasoning/3618.md`. These are the numbers GR-2 V2.0 carries.

## §1 Provenance of every input
| input | fixed by |
|---|---|
| exterior dynamics | GR's tensor equations — the ringdown frequency (3612) |
| surface radius | areal 8M/3 (a = 0); 2.734 M at χ = 0.68 (3392 ansatz A) — from R-PSR-LAW-LOG (Mercury-calibrated second order, founder-ratified completion) and the founder's clock |
| wall impedance | β = −0.025 (band −0.02 … −0.03, 1/M) — GW150914's measured (f₂₂₀, τ₂₂₀), GWTC-3 Table XIII (3616) |
| wall law's frequency dependence | **assumed constant** across the band — the one thing an echo would supply |

## §2 The predictions (62 M_⊙; Q = Re ω / 2|Im ω|)

| line | β = −0.02 | **β = −0.025** | β = −0.03 | Q |
|---|---|---|---|---|
| **χ = 0.68, (2,−2)** | 160 Hz | **159 Hz** | 158 Hz | 3.6 |
| **χ = 0.68, (3,−3)** | 256 | **255** | 255 | 7.1 |
| χ = 0.68, (2,+2) prograde (the ringdown) | 266 | **265** | 264 | 2.5 |
| a = 0, ℓ = 2 (even / odd) | 201 / 202 | **200 / 201** | 199 / 201 | 3.5 / 4.0 |
| a = 0, ℓ = 3 (even / odd) | 319 / 320 | **319 / 319** | 318 / 318 | 5.6 / 5.8 |

The calibration band moves the lines by ±1 Hz; the systematic uncertainty is elsewhere (the Kerr surface radius; the constant-β assumption). The even and odd sectors agree to 3% at the same β — the wall dominates.

## §3 What changed from the shipped set
- V1.6 (assumed hard wall, old surface): 191 / 288 Hz. **Now: 159 / 255 Hz** — −17% and −11% — and the hard wall is excluded by the ringdown (3616), so the shipped numbers were not merely different, they were empirically ruled out.
- The (3,−3) line at **255 Hz** sits at the observed ringdown frequency of GW150914-class events (~250 Hz). Whether it is *excited* in a merger, and how it would be distinguished from the (2,2) ringdown, is OPEN-GR-EXCITATION-1 — now with a concrete stake.

## §4 The residual the calibration predicts — a falsifier with existing instruments
Fixing β to GW150914's box does not fix the *shape* of the prograde mode: at β_cal the (2,+2) mode sits at δf = −3.8%, **δτ = −18.5%** relative to Kerr. Inside the 90% box (its lower τ edge is −22%), but not at its centre: **the R-core predicts a ringdown damping time ~18% shorter than Kerr's** for GW150914-like remnants. As the ringdown measurements tighten (the loudest O4 events; combined pSEOB constraints), this becomes a clean test: a measured τ₂₂₀ at Kerr's value to ±10% falsifies a 1.33 r_S surface with a constant impedance; a measured deficit near 18% is the R-core's signature *in the ringdown itself*, with no echo required.

## §5 What V2.0 says, in one paragraph (draft, on the founder's word)
*The wall of the line set is no longer assumed. Its impedance at the ringdown frequency is fixed by GW150914's measured ringdown to a narrow band just softer than Neumann; hard walls (including this paper's V1.6 wall) are excluded by that measurement. At that impedance the R-core's lines for a 62 M_⊙, χ = 0.68 remnant are 159 Hz (2,−2) and 255 Hz (3,−3), and the prograde (2,2) mode — the ringdown — is predicted 4% below and 18% shorter-lived than Kerr's, a residual within present precision and testable with the next loud events. The surface sits at 1.33 r_S by the founder's clock mechanism and Mercury's perihelion; the exterior equations are Einstein's by the ringdown frequency; the wall's frequency dependence, which an echo would supply, is the one assumption carried.*

## §6 Owed
The V2.0 draft (founder's word); the exact ringdown box (pSEOB deviation table); EXCITATION-1 for the (3,−3)-at-255-Hz question; the C5-frame law against the target β ≈ −0.025.
