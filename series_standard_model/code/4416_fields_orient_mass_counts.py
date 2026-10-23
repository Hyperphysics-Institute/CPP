"""Patch 4416 -- founder (on 4415): mu-epsilon changes because there is more SSV_abs, which happens next to mass (more CPs);
more SSV_abs reduces the PSR. A stronger E or B field creates more SSV_net through separation or arcs, but not more
SSV_abs, because it does not add CPs, only orients the DPs (separation) and/or speeds the arcs.

What part 1 shows is a symmetry identity, not a property of a particular sea: with the + and - members of each DP starting
together and moved by +d/2 and -d/2, each DP's unsigned (count) term w(|x+d/2-r|) + w(|x-d/2-r|) is even in d and its signed
term is odd in d, for ANY radial weight w (1/r, 1/r^2, or per-contribution magnitudes). So the count changes only at second
order. Real DPs have a nonzero, randomly oriented internal separation, so for them the first-order count term cancels only
on average. The size of the second-order count change is dominated by the CPs nearest the receiver and varies with the
sample (sign included); only its scaling (x4 per doubling) is meaningful.

Part 1. Central-charge field (softened 1/r^2; near the centre displacements reach ~0.08 at the largest separation, which
        is large next to the CP spacing; harmless to the scaling). At three receivers: change in the unsigned count census
        sum 1/r, the signed scalar census sum q/r (the bound-charge potential, not V_i), and the vector sum
        sum q (x - r)/|x - r|^3 (the rank-1 channel, V_i-like), as the separation doubles.
Part 2. Uniform field (rigid opposite shift of the two sublattices): count change from granularity and edges only.
Part 3. Sizes: the gravitating share of field energy, and the QED light-speed shift, for 1 T and 1 MV/m.
"""
import numpy as np
rng = np.random.default_rng(4416)
N = 200000
x = rng.normal(size=(N, 3)); x /= np.linalg.norm(x, axis=1)[:, None]
x *= rng.random(N)[:, None]**(1/3)
def central(p):
    r = np.linalg.norm(p, axis=1)[:, None]
    return p/r/np.maximum(r, 0.05)**2
def censuses(plus, minus, rec):
    dp = plus - rec; dm = minus - rec
    rp = np.maximum(np.linalg.norm(dp, axis=1), 1e-3); rm = np.maximum(np.linalg.norm(dm, axis=1), 1e-3)
    count = (1/rp + 1/rm).sum(); signed = (1/rp - 1/rm).sum()
    vec = (dp/rp[:, None]**3 - dm/rm[:, None]**3).sum(axis=0)
    return count, signed, vec
receivers = np.array([[0.3, 0, 0], [0, 0.4, 0.1], [-0.2, 0.2, -0.3]])
print("Part 1 (central field; changes relative to the zero-separation count census):")
for rec in receivers:
    c0, s0, v0 = censuses(x, x, rec)
    print(f"  receiver {rec}:")
    for eps in (1e-4, 2e-4, 4e-4):
        d = eps*central(x)
        c, s, v = censuses(x + d/2, x - d/2, rec)
        print(f"    separation {eps:.0e}: count {(c-c0)/c0:+.2e}  signed scalar {s/c0:+.2e}  |vector sum| {np.linalg.norm(v)/c0:.2e}")
print("  count: x~4 per doubling (second order); signed scalar and vector sum: x2 (first order).")

print("Part 2 (uniform field along z: + shifted +d/2, - shifted -d/2):")
for rec in receivers:
    c0, _, _ = censuses(x, x, rec)
    row = []
    for eps in (1e-4, 2e-4, 4e-4):
        d = np.array([0, 0, eps])
        c, s, v = censuses(x + d/2, x - d/2, rec)
        row.append(f"{eps:.0e}: count {(c-c0)/c0:+.1e}, |vector| {np.linalg.norm(v)/c0:.1e}")
    print(f"  receiver {rec}: " + ";  ".join(row))
print("  in a uniform field the count change is tiny and second order (granularity and the sea's edge); in an infinite,")
print("  smooth sea it would be exactly zero, while the field's energy density E^2 is not zero.")

c = 2.998e8; G = 6.674e-11; mu0 = 4e-7*np.pi; eps0 = 8.854e-12; A_e = 1.32e-24
for label, u in (("B = 1 T", 1.0**2/(2*mu0)), ("E = 1 MV/m", 0.5*eps0*(1e6)**2)):
    rho = u/c**2
    print(f"Part 3 ({label}): energy density {u:.2e} J/m^3 -> mass density {rho:.1e} kg/m^3; potential over 1 m ~ {G*rho/c**2:.0e}")
print(f"  QED index shift at 1 T: n_par - 1 = {7*A_e:.1e} (light-by-light; PVLAS consistent with zero)")
