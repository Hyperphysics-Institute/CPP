"""Patch 4410 -- founder (on 4409): the ZBW swing speed is not known; he recalls the DP's CPs passing through each other
with a cycle much longer than one PSR per Moment (4324-4326: the CP moves at its V_i, below light speed even at the
centre; swing ~68.5 PSR apogee to apogee).  Contraction: the same inverse-square decay must act between CPs at the same
MEASURED distance (relativity principle), so the same number of Steps occurs in the same number of absolute Moments,
and the distance must become shorter.

Part 1  his argument requires shortening; the size along vs across comes from 4409's light round trips, with the
        clock rate gamma (4408) fixing 'none across'.
Part 2  the classical mechanism (Heaviside 1888; Searle; Lorentz 1895; Bell): the retarded potential of a charge
        moving at v, relayed at light speed, computed here, has equal-potential surfaces flattened by 1/gamma along the
        motion; the co-moving force follows the convection potential with the same ellipsoids.
Part 3  the same geometry, locally, as gravity's rulers in 4397: a ruler held near a mass is shortened along the line to the mass by
        sqrt(1 - beta^2) and unchanged across -- the shift direction, in both cases.
"""
import numpy as np
print("Part 1: spacing along / across the motion needed for equal light round trips (rest spacing 1)")
for v in (0.1, 0.5, 0.9):
    print(f"  v = {v}: along {np.sqrt(1-v*v):.4f}, across 1.0000")

print("\nPart 2: retarded (Lienard-Wiechert) potential of a charge moving at v, relayed at light speed (computed)")
from scipy.optimize import brentq
def phi(x, y, v):
    # field point (x, y) relative to the charge's PRESENT position; source at (v t, 0); retarded time t_r < 0
    f = lambda t: np.hypot(x - v*t, y) + t
    tr = brentq(f, -1e3, 0.0)
    Rx, Ry = x - v*tr, y; R = np.hypot(Rx, Ry)
    return 1.0/(R - v*Rx)
for v in (0.1, 0.5, 0.9):
    g = 1/np.sqrt(1 - v*v)
    target = phi(0.0, 1.0, v)                       # across, distance 1
    xa = brentq(lambda x: phi(x, 0.0, v) - target, 1e-6, 5.0)   # ahead, same potential
    print(f"  v = {v}: equal-potential distance ahead {xa:.4f} vs across 1 -> ratio {xa:.4f} (1/gamma = {1/g:.4f})")
print("  the force on a co-moving charge (electric + magnetic) follows the convection potential phi(1 - v^2), with")
print("  the same ellipsoids (Heaviside, Searle; Lorentz 1895): static balances contract by 1/gamma along the motion.")
print("  Bound systems with moving parts also need the relativistic momentum law (Bell); every force must transform alike.")

print("\nPart 3: gravity's rulers (4397), shift beta = sqrt(2u)")
for u in (0.01, 0.1, 0.375):
    b = np.sqrt(2*u)
    print(f"  u = {u}: radial ruler {np.sqrt(1-b*b):.4f}, sideways 1.0000")
