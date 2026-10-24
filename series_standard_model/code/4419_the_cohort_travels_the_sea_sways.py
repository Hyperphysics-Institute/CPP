"""Patch 4419 -- founder: the polarized DP cloud travels with the central unpaired CP (and a charged capacitor's interplate
DPs travel with it) as a coherent cohort despite heavy partner switching; the cohort arcs and separates the surrounding sea,
which sways as it passes; there is a push against the forward advance and a greater push forward, netting the constant-
velocity displacement per Moment.

Part 1. Where the front-back differential can come from, under 4415's rule (step = f x local light speed, f regenerated each
        Moment from the sea's organization, not iterated from the last step). If the co-moving cohort (weight w_c) enters
        the normalization but not the differential, the regenerated f is (v/c) * w_s/(w_s + w_c). Under 4415's rule that is
        a rescaling, not a decay; but the cohort's arcs grow with speed (w_c ~ w0 * v^2 here, illustrative), so the
        rescaling depends on speed: f no longer equals v/c, a speed-dependent (preferred-frame) error. Only if the cohort
        does not enter the reference (reading (b), not yet defined operationally) is f = v/c at every speed.
        (Under 4414's withdrawn iterated rule the same factor would compound into a decay; shown for contrast only.)
Part 2. His 'push against' and 'greater push forward' read as the front and rear signals of the rear-minus-front
        summation (displacement per Moment): their net must be exactly v at every speed (4412's marginality condition). A
        residual fractional mismatch eta per Moment, assumed linear in velocity, against an ephemeris-scale bound on
        anomalous drag (a common deceleration of the whole solar system would be invisible; a linear drag shows up on the
        orbital motion).
"""
import numpy as np
print("Part 1 (regenerated f / (v/c) under 4415's rule, cohort weight w_c = w0 v^2 relative to the sea):")
for w0 in (0.01, 0.1, 1.0):
    row = ", ".join(f"v {v:.1f}: {1/(1 + w0*v**2):.4f}" for v in (0.1, 0.3, 0.6, 0.9))
    print(f"  w0 {w0:4.2f}: {row}")
print("  a speed-dependent shortfall: a moving body would not keep its speed exactly, and the error grows with speed")
print("  through the absolute frame. Reading (b) gives 1.0000 at every speed.")
s_iter = 1/(1 + 0.01)
print(f"  (withdrawn 4414 iterated rule, contrast only: a constant factor {s_iter:.4f} compounds, 0.300 -> {0.3*s_iter**100:.3f} in 100 Moments)")

print("Part 2 (residual drag-drive mismatch eta per Moment):")
moments_per_s = 1/5.39e-44
for eta in (1e-60, 1e-50, 1e-45):
    print(f"  eta {eta:.0e}: fractional speed change per second ~ {eta*moments_per_s:.1e}")
a_bound, v_orb = 1e-14, 3e4     # order of planetary-ephemeris bounds on anomalous accelerations (m/s^2); Earth's orbital speed
rate = a_bound/v_orb
print(f"  ephemeris-scale bound: anomalous acceleration <~ {a_bound:.0e} m/s^2 on a body moving at {v_orb:.0e} m/s")
print(f"  -> fractional drag <~ {rate:.0e} per second <~ {rate/moments_per_s:.0e} per Moment (order of magnitude)")
print("  in practice the cancellation must be exact by construction, at every speed and for every species.")
