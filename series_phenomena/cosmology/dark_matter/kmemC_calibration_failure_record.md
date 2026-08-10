# ROUTE C CALIBRATION FAILURE — RECORDED IN FULL; THE PREREG'S DESIGN VARIABLE WAS WRONG; AMENDED BEFORE ANY EVIDENTIARY LEG

**Patch 3055 (10 Aug 2026). The v1 pre-launch calibration (prereg
`kmemC_routeC_prereg.md` §3.1, Patch 3053) ran on Kila6 and FAILED its
own OK-check on all four arms; the driver's pilot gate then refused to
proceed. The failing table is committed at
`data/kmemC/calibration.json` (founder commit 2bc688c9) and this
record explains it. NO evidentiary leg ran; calibration is
evidence-excluded by v1 §3; nothing has been looked at.**

## §1 — What the calibration reported

| arm | x_src0 | T_exit | T_close | ΔT measured | target | ok |
|---|---|---|---|---|---|---|
| a0 | −18.0 | 94 | 60 | +34 | 0 | ✗ |
| a1 | −15.77 | 84 | 54 | +30 | −12 | ✗ |
| a2 | −19.70 | 97 | 60 | +37 | +8 | ✗ |
| a3 | −11.83 | 71 | 48 | +23 | −12 | ✗ |

## §2 — Diagnosis: three defects, one root cause

**Root cause — the design variable did not exist in the regime the
artifact was observed in.** Reconstruction of the committed Route B
configuration (x_src0 = −18, β = 0.10, t_step = 24, T_END = 384):
the source travels L = β(T_END − t_step) = 36 units, ending at
x = +18 — **it never leaves any of the three domains** (x_half ∈
{24, 28, 32}). The Patch 3047 §4 diagnosis was about the source
TRAVEL DISTANCE coinciding with T_BALL (36 = 1.5 × 24), not about an
exit. v1 mis-read that as an exit time.

**Defect 2 — geometry/drive coupling.** T_exit ∝ 1/β, so v1's drive
ladder (β 0.6 → 0.8 → 1.0), whose purpose was sizing the SNR, would
have silently moved every arm's geometry. At β = 0.6 the source does
exit (t ≈ 94) — a different physical regime from the one under test.

**Defect 3 — bisection direction inverted**, and the v1 ΔT targets
were unreachable inside the admissible x_src0 range regardless.

## §3 — The corrected variable (prereg v2, same patch)

**Δ ≡ L − T_BALL**, L = β(T_END − t_step), T_BALL = 1.5·x_half.
Closed-form; no calibration runs; and it reproduces the Route B
pattern exactly: d24 → Δ = 0 (tail SIGNIFICANT), d28 → −6 (c.w.z.),
d32 → −12 (c.w.z.). v2 arms are frozen in Δ, with the drive isolated
into a dedicated margin arm so drive-sizing can never move geometry
again (escalation there is on N only).

## §4 — Process note (why this is a success, not a failure)

The v1 prereg deliberately delegated raw coordinates to a calibration
step *because* the source-motion convention could not be verified
from the excerpts available at freezing time (v1 §Preamble). That
delegation, plus the calibration's own OK-assertion and the pilot's
refusal to run on a not-OK table, converted a silent 3700-CPU-hour
experiment on the wrong geometry into a zero-cost correction. The
guard-rails worked exactly as designed; the amendment is recorded
here rather than smoothed away, and v1 remains in-repo unedited.
