"""4092 (EW lane) -- which orthogonal pair does a captured DP occupy? The capture supplies only ONE plane;
the second must come from MOTION -- and that selects HELICITY geometrically.

4091 left this: the 600-cell has 60 orthogonal plane pairs at a vertex; which does a captured DP use?

U1  THE CAPTURE SUPPLIES ONLY ONE PLANE. SPIN-1's inner CP (r_in) and outer CP (2 r_in) orbit the SAME
    central -eCP about a COMMON axis -- coplanar (4090). A single-DP capture gives ONE plane, so the
    capture geometry cannot select an orthogonal PAIR by itself.
U2  AND THE OBVIOUS FIX RUNS BACKWARDS. SPIN-1 assigns single-DP capture to FERMIONS and double-DP capture
    to BOSONS. If the second plane had to come from a second captured DP, only BOSONS could be handed --
    but helicity and V-A act on FERMIONS. So the second plane cannot come from a second DP.
U3  IT COMES FROM MOTION -- 4089's (4th-axis, direction-of-travel) leg. For a moving fermion:
    plane 1 = the captured-DP orbit (spin), plane 2 = the rotation its motion through the sea produces.
U4  THE CONSEQUENCE, tested: the pseudoscalar tracks the component of the spin axis ALONG the direction of
    travel and vanishes for transverse spin. HELICITY is selected by the geometry, not postulated.
U5  CONTROL: transverse spin must give exactly zero; and both hands must remain available (no sign).

NOTE (error caught in-patch): a first version built the spin plane from an arbitrary orthonormal basis,
whose ORIENTATION jumps discontinuously with the angle -- 0 deg and 180 deg both came out +2.000000, a
spurious result. The spin bivector must be oriented by the spin axis itself (its 3-space dual).
"""
import numpy as np

def wedge(a, b): return np.outer(a, b) - np.outer(b, a)
def pf(B): return 2.0*(B[0,1]*B[2,3] - B[0,2]*B[1,3] + B[0,3]*B[1,2])

def spin_bivector(om):
    """Oriented spin bivector: the 3-space dual of the spin axis, B_ij = eps_ijk om_k."""
    B = np.zeros((4,4))
    B[2,3], B[3,1], B[1,2] = om[1], om[2], om[3]
    return B - B.T

print("U1  a single captured DP gives ONE plane (SPIN-1's orbits are coplanar, 4090) -- no orthogonal pair.")
print("U2  a second captured DP would make BOSONS handed and leave FERMIONS unhanded -- backwards.")
print("    (SPIN-1: single-DP capture = fermion, double-DP capture = boson.)")
print("    => the second plane must come from MOTION: 4089's (4th-axis, travel-direction) leg.\n")

W = np.array([1., 0, 0, 0])      # 4th axis
v = np.array([0, 1., 0, 0])      # direction of travel (in physical 3-space)
print("U3/U4  pseudoscalar vs angle between spin axis and direction of travel")
print("     angle      pseudoscalar     2*cos(angle)")
for deg in (0, 30, 60, 90, 120, 180):
    th = np.radians(deg)
    om = np.array([0, np.cos(th), np.sin(th), 0.0])
    print(f"     {deg:>3d} deg    {pf(spin_bivector(om) + wedge(W, v)):+.6f}      {2*np.cos(th):+.6f}")

vals = {d: pf(spin_bivector(np.array([0, np.cos(np.radians(d)), np.sin(np.radians(d)), 0.0])) + wedge(W, v))
        for d in (0, 90, 180)}
print("\n    => the pseudoscalar is exactly 2*cos(angle): the component of spin ALONG the motion.")
print("       That is HELICITY, selected by the geometry itself rather than postulated.")
print(f"\nU5  CONTROL: transverse spin (90 deg) = {vals[90]:+.6f} (must be zero);")
print(f"    0 deg = {vals[0]:+.4f} and 180 deg = {vals[180]:+.4f} (must be opposite -- both hands available)")
assert abs(vals[90]) < 1e-12 and abs(vals[0]) > 1 and vals[0]*vals[180] < 0
print("\n    The geometry selects the QUANTITY (helicity) but still not the SIGN -- unchanged since 4046.")
