# The register closure's own even-sector stability, recorded (handover item 5): under either lock (C5 q = 1, c07 q = 2/3) the junction K − qH₂ = 0 has NO zero in the upper half-plane on a contour that reaches Re ω = 0.005 and Im ω = 5e−4 (argument principle in the pole-free form; control = the horizon-equivalent wall, also 0). STABLE, including near the static zero mode. The two trapped modes' signs resolved to 3e−14: C5 0.16476 − 1.69e−4 i (Q ≈ 490, 86 Hz, τ ≈ 1.8 s at 62 M☉) is damped; c07 0.02440 − 3.6e−8 i (Q ≈ 3×10⁵, 12.7 Hz) is MARGINAL — 3654's "≈ −0.003" was a coarse-grid value, superseded

**Patch 3661, Session 164, 7 Sep 2026.** Verify `code/3661_closure_lock_stability_record_verify.py` (7/7; run from the repo root; exec's 3654 (which exec's 3644's definitions); ~20 min). Reasoning `reasoning/3661.md`. No paper touched. Ledger §5 updated. Checkpoint `session_logs/2026-09-07_session_164_checkpoint.md` rides with this patch (§15.14).

## §1 What a stability record needs, and 3654 did not do
3654 found each lock's ℓ = 2 spectrum has no pole near GR's ringdown and one long-lived trapped mode, "damped, barely". Two gaps: (a) no count of zeros in the upper half-plane — the budget interior's count (3643 §5) used a contour that stopped at Im ω = 0.005 and Re ω = 0.05, missing exactly the corner where 3650's static near-zero mode lives; (b) a mode with |Im ω| ~ 1e−4 needs its sign established, not read off a grid.

## §2 The count
The junction in its **pole-free form** `F = c_a Z + c_b dZ/dr` (K − qH₂ itself, 3654's symbolic c_a, c_b at r = 8M/3; no division by c_b, and |c_b| ≥ 0.47 on the region so the Robin and pole-free forms share zeros there). Contour: Re ω ∈ [0.005, 1.2], Im ω ∈ [5e−4, 0.4]; the bottom edge refined within ±0.012 of each trapped pole (the edge passes ~7e−4 above them), the vertical edges refined for Im ω < 0.04 (the phase turns fast as ω → 0 — the first two runs' 2.1-rad steps were there, not at the poles). Max phase step 0.51 / 0.67 / 0.39 rad.

| wall | winding number |
|---|---|
| C5 lock, q = 1 | 0 |
| c07 lock, q = 2/3 | 0 |
| horizon-equivalent (control: a black hole has no growing mode) | 0 |

**No growing even mode under the register closure, down to the static corner.** OPEN-GR-SURFACE-STABILITY-1's branch (a) (3643) holds for the closure interior as well as the budget interior — for a different reason: the closure's wall is lossless, and a lossless Robin wall on the Zerilli exterior with these coefficients is stable, not the clamp's b₂ < 0 growth (3390).

## §3 The trapped modes, resolved (r₀ = 50/100/200, spread 3e−14, contrast < 1e−13)
| lock | ω | Q | Hz @62 / @62.7 M☉ | τ |
|---|---|---|---|---|
| C5, q = 1 | 0.16476 − 1.69e−4 i | 489 | 85.9 / 84.9 | 5.9×10³ M = 1.8 s |
| c07, q = 2/3 | 0.02440 − 3.56e−8 i | 3.4×10⁵ | 12.7 / 12.6 | 2.8×10⁷ M = 2.4 h |

C5's mode is damped, sign resolved by 10 orders. **c07's is marginal:** the lock sits 0.8% from the exact static zero mode (K/H = 0.6615, 3650), and its dynamical pole is correspondingly a hair below the real axis. 3654's "≈ −0.003" for c07 is superseded (its grid step was 0.06 in Im ω; the refined value is −3.6e−8). Physically: under the c07 lock a 12.7 Hz quadrupole deformation, once excited, does not decay on any astrophysical ringdown timescale — in band, and not seen (GW250114's postmerger data are consistent with two Kerr modes only). That is a further mark against the c07 lock, already excluded by row 6 (Λ = +714); C5's 86 Hz, 1.8-s mode is equally unseen and equally excluded by 3654 (no ringdown line). Neither lock is live; this patch certifies stability, not phenomenology.

## §4 Standing
- Handover item 5 discharged. Ledger §5: the closure-interior stability record is written; row 8's "passes" now covers both interiors (budget: 3643; closure: here).
- Superseded: 3654 §2's c07 damping "−0.003" → −3.6e−8 (marginal).
- Method note (Layer 1): argument-principle contours on wall laws must be refined on the vertical edges near the real axis, not only near known poles — the ω → 0 corner is where the phase turns fastest. Recorded for the methods catalogue with 3643's winding.
- Next: V2.3 write-up (3643–3661) and CONV-042 re-cut; Session 164 handover.
