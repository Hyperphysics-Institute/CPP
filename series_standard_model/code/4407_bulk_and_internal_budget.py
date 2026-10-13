"""Patch 4407 -- founder (on 4406): what is 'the drift'?; the hot ball is heavier (more internal KE, larger DP-arcs and
separation); every level of binding enrols DPs, all accelerated; CPs do not move faster in their PSR; the sea can
polarize ever more volume as v -> c.

Part 1  'drift' = the body's overall (bulk) motion, as opposed to its CPs' internal swing.  The effective internal rate
        of a moving body is 1/gamma (SR-1 strength; VTD-1's quadrature is an effective identity, not a per-CP step rule;
        the geometric step-sharing route closed negative at 2493/2500).
Part 2  falling: the internal-rate change after a second's fall is of order v^2/c^2 (a function of v alone); equal fall
        still rests on the whole-pattern boost and the sea's energy-weighted deposit (4406 items 2-3).
Part 3  the sea's unlimited enrolment as v -> c: stored energy grows without bound, as gamma m c^2 does (qualitative;
        the exact gamma is SR-1's f_eff input / SF-6 debt (c)).
"""
import numpy as np
c = 2.998e8
print("Part 1: effective internal rate of a moving body (SR-1 strength; not a per-CP step allocation)")
for b in (0.0, 0.1, 0.5, 0.9, 0.999):
    print(f"  v = {b:5.3f} c: internal rate {np.sqrt(1-b*b):.4f} = 1/gamma")
g = 29.33
print(f"  muons in the CERN storage ring (gamma = {g}): lifetime stretched {g:.2f}x, confirmed to ~0.1% (Bailey et al. 1977)")

print("\nPart 2: a body falling from rest for one second near the Earth")
v = 9.8
x = (v/c)**2
print(f"  bulk speed {v} m/s = {v/c:.2e} c; internal rate 1 - {-np.expm1(0.5*np.log1p(-x)):.2e} (a function of v alone)")

print("\nPart 3: energy stored by the sea, gamma m c^2 (in units of m c^2)")
for b in (0.5, 0.9, 0.99, 0.999, 0.9999):
    print(f"  v = {b} c: {1/np.sqrt(1-b*b):8.2f}  (grows without bound; consistent with his unlimited enrolment)")

print("\nPart 4: why a literal per-CP split breaks the cap for a longitudinal swing")
b = 0.5
print(f"  v = {b} c: bulk {b} l_P + internal {np.sqrt(1-b*b):.3f} l_P in the same direction = {b+np.sqrt(1-b*b):.2f} l_P > 1")
fw, bw = 1.0, 1.0   # lab-frame legs at the cap: forward leg covers (L + v T_f) at speed 1, backward (L - v T_b)
L = 1.0
Tf = L/(1-b); Tb = L/(1+b)
print(f"  re-timed (SR picture): forward leg lasts {Tf:.3f}, backward {Tb:.3f}; period {Tf+Tb:.3f} = 2L/(1-v^2)")
print("  -> both legs stay at the cap; the cycle lengthens (with length contraction the period dilates by exactly gamma)")
