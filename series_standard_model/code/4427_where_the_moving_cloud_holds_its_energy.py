"""Patch 4427 -- founder: the DP organization's energy depends on the angle to the velocity axis; the SSV_abs modification is
zero at 90 degrees and maximum along the axis; total stored energy rises with speed, spread over the lopsided sphere.

Two different angle-dependent quantities, compared:
Part 1. The moving CP's light sphere / PSR (4409): reach 1 - v ahead, 1 + v behind, sqrt(1 - v^2) across. Its MODIFICATION is
        first order in v along the axis (front shorter, back longer) and only second order across (1 - sqrt(1 - v^2) ~ v^2/2).
        Likewise the DI-bit arrival-rate compression 1/(1 - n.v) (4411): largest along the axis, unchanged across at first order.
Part 2. Where the moving charge's FIELD ENERGY sits (census = Lienard-Wiechert, 4411, conditional): energy density at present
        distance r and angle theta, relative to rest: (E^2 + B^2)/E0^2 = (1 - v^2)^2 (1 + v^2 sin^2 t) / (1 - v^2 sin^2 t)^3.
        Integrated over r outside the contracted core: energy per unit solid angle against theta.
"""
import numpy as np
print("Part 1 (the PSR / light-sphere modification by angle, fraction of rest reach):")
for v in (0.3, 0.6, 0.9):
    th = np.radians([0, 45, 90, 135, 180])
    # reach of the shifted unit sphere from the moved centre, at angle th to the motion: solve |r n + v x_hat| = 1
    reach = -v*np.cos(th) + np.sqrt(1 - v**2*np.sin(th)**2)
    print(f"  v {v}: " + "  ".join(f"{int(np.degrees(t)):3d} deg {r - 1:+.3f}" for t, r in zip(th, reach)))
print("  modification: first order along the axis (ahead and behind, opposite signs), second order across -- as he says")

print("Part 2 (field-energy density at the same present distance, relative to rest, by angle):")
for v in (0.3, 0.6, 0.9):
    row = []
    for deg in (0, 30, 60, 90):
        s2 = np.sin(np.radians(deg))**2
        rel = (1 - v**2)**2*(1 + v**2*s2)/(1 - v**2*s2)**3
        row.append(f"{deg:2d} deg x{rel:7.3f}")
    print(f"  v {v}: " + "   ".join(row))
print("Part 2b (share of the field energy outside the contracted core, by angle band, v = 0.9):")
v = 0.9; g = 1/np.sqrt(1 - v**2)
t = np.linspace(0, np.pi, 20001)
s2 = np.sin(t)**2
# energy per solid angle outside contracted core: integrate density * r^2 dr from r_core(t) to inf -> density_coef / r_core(t)
rcore = 1/np.sqrt(g**2*np.cos(t)**2 + np.sin(t)**2)          # contracted core x^2 g^2 + rho^2 = 1
coef = (1 - v**2)**2*(1 + v**2*s2)/(1 - v**2*s2)**3
dE = coef/rcore*np.sin(t)                                     # per d(theta), up to constants
band = lambda lo, hi: np.trapezoid(dE[(t >= np.radians(lo)) & (t <= np.radians(hi))], t[(t >= np.radians(lo)) & (t <= np.radians(hi))])
tot = np.trapezoid(dE, t)
for lo, hi in ((0, 30), (30, 60), (60, 90)):
    sh = (band(lo, hi) + band(180 - hi, 180 - lo))/tot
    print(f"  within {lo:2d}-{hi:2d} deg of the axis (both sides): {sh:.3f} of the energy (a solid-angle share alone would be {np.cos(np.radians(lo)) - np.cos(np.radians(hi)):.3f})")
print("  the moving charge's field energy concentrates ACROSS the motion (a pancake): strongest at 90 degrees, weakest along")
print("  the axis -- the opposite of 'zero at 90, maximum along the axis' for the stored energy.")

print("Part 3 (readings under which both can hold):")
print("  (a) the field-energy density is even in v: no first-order term anywhere; at second order ~ 1 + v^2 (4 sin^2 t - 2):")
for deg in (0, 45, 90):
    s2 = np.sin(np.radians(deg))**2; v = 0.05
    exact = (1 - v**2)**2*(1 + v**2*s2)/(1 - v**2*s2)**3 - 1
    print(f"    v = 0.05, {deg:2d} deg: exact change {exact:+.5f}, second-order estimate {v**2*(4*s2 - 2):+.5f}")
print("  (b) orientation: a co-moving DP whose separation axis makes angle a with the motion has its spacing contracted by")
for a in (0, 45, 90):
    for v in (0.6,):
        g = 1/np.sqrt(1 - v**2); ar = np.radians(a)
        L = np.sqrt((np.cos(ar)/g)**2 + np.sin(ar)**2)
        print(f"    v {v}, axis {a:2d} deg to the motion: spacing x{L:.4f} (change {L - 1:+.4f})")
print("    -> zero change at 90 degrees, largest along the motion: his 'zero at 90, maximum collinear', consistent with the pancake")
print("  note: 1/(1 - n.v) uses the retarded direction n; Part 2 uses the present-position angle.")
