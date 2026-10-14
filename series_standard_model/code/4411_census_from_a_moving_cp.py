"""Patch 4411 (Claude-initiated; 4410 owed item (b), first part) -- what does the light-speed DI-bit relay give for the
census around a MOVING CP?

A CP moving at v through the absolute frame broadcasts DI-bits each Moment; they travel at light speed from where the CP
was.  At a receiving GP, arrivals come from the retarded position (distance R, direction n), and because the source
moves, successive Moments' DI-bits arrive compressed by 1/(1 - n.v) (more per Moment ahead, fewer behind).

Two ways to build a receiver's count:
  (i)  flux: each arrival weighted 1/R^2 (inverse-square spreading), counted per receiver Moment: 1/(R^2 (1 - n.v));
  (ii) census: each arrival weighted as the static census from its emission point, 1/R (the corpus's u = sum m/r,
       flat-harmonic), counted per receiver Moment: 1/(R (1 - n.v))  -- this is the Lienard-Wiechert potential.
For each, find the distances ahead and behind at which the count equals its value one unit to the side.
"""
import numpy as np
from scipy.optimize import brentq

def ret(x, y, v):
    f = lambda t: np.hypot(x - v*t, y) + t
    tr = brentq(f, -1e4, 0.0)
    Rx, Ry = x - v*tr, y; R = np.hypot(Rx, Ry)
    return R, Rx/R

def flux(x, y, v):
    R, nx = ret(x, y, v); return 1/(R*R*(1 - v*nx))

def census(x, y, v):
    R, nx = ret(x, y, v); return 1/(R*(1 - v*nx))

for v in (0.001, 0.1, 0.5, 0.9):
    g = 1/np.sqrt(1 - v*v)
    for name, F in (("(i) flux 1/R^2", flux), ("(ii) census 1/R", census)):
        t = F(0, 1, v)
        xa = brentq(lambda x: F(x, 0, v) - t, 1e-6, 50); xb = brentq(lambda x: F(-x, 0, v) - t, 1e-6, 50)
        print(f"  v = {v:5}: {name:16s} ahead {xa:.6f}  behind {xb:.6f}   (1/gamma = {1/g:.6f})")
print()
print("  (i) is lopsided at first order in v (ahead ~ sqrt(1 - v), behind ~ sqrt(1 + v)).")
print("  (ii) is front-back symmetric (exactly, at all orders) and flattened by exactly 1/gamma: Heaviside's ellipsoid.")
print("      The 1/R weight per arrival is the retarded Green's function of GR-1j's wave equation: assumed, not derived.")

print("\nOblique check of the census ellipsoid X^2 + (1 - v^2) rho^2 = 1 (v = 0.5):")
v = 0.5
for ang in (0, 30, 60, 90, 120, 150, 180):
    a = np.radians(ang)
    # point on the Heaviside ellipsoid at polar angle a from the motion
    r = 1/np.sqrt(np.cos(a)**2 + (1 - v*v)*np.sin(a)**2)
    print(f"  angle {ang:3d}: census {census(r*np.cos(a), r*np.sin(a), v):.6f}  (constant 1 = on one equipotential)")

print("\nForce on the axis at present distance 1, computed from retarded arrivals:")
def raw_vec_axis(x, v):
    R, nx = ret(x, 0.0, v); return nx/(R*R*(1 - v*nx))
for v in (0.001, 0.1, 0.5):
    ahead = raw_vec_axis(1.0, v); behind = -raw_vec_axis(-1.0, v)
    true = 1 - v*v       # field of a uniformly moving charge on its axis at present distance 1
    print(f"  v = {v:5}: raw vector sum ahead {ahead:.4f}, behind {behind:.4f};  true field (1 - v^2) {true:.4f} both sides")
print("  -> a raw vector sum of arrivals is lopsided at first order: a co-moving pair would get a net push ~ 2v")
print("     (a self-drive), not a front-back distortion; the census gradient times (1 - v^2) is the full co-moving force.")
