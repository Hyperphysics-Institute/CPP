#!/usr/bin/env python3
"""4354 -- the founder's far-field relay (founders_voice/4354), in the simplest form that keeps his words.

No DI-bit of the origin family goes beyond the GP_PSR. Every GP does the same thing, so a GP in the origin's band
re-radiates the influence it received; that reaches its own PSR, is re-radiated again, and so on.
Model: a unit of influence hops a distance P (one PSR, in a random direction) per relay step; each GP passes on exactly
what it received (lossless, isotropic). A unit is absorbed at R_max (stands in for infinity).  Lengths in lattice
units; the well is P -> 0.9 P on the same lattice.
Measured per spherical shell of radius R:
  net   = outward crossings - inward crossings, per unit emitted (Gauss: 1 at every R),
  gross = all crossings per unit emitted (the raw traffic a counter on one GP would see, summed over the sphere),
then converted to what a test charge reads (a) per GP of area, (b) per PSR-sized cross-section."""
import numpy as np
rng = np.random.default_rng(4354)

def run(P, n=40000, rmax_psr=30.0, shells_psr=(2, 4, 8, 16)):
    Rmax = rmax_psr * P
    x = rng.normal(size=(n, 3)); x *= (P / np.linalg.norm(x, axis=1))[:, None]   # start on the band, radius P
    alive = np.ones(n, bool)
    shells = np.array(shells_psr) * P
    net = np.zeros(len(shells)); gross = np.zeros(len(shells))
    for _ in range(20000):
        if not alive.any(): break
        u = rng.normal(size=(alive.sum(), 3)); u /= np.linalg.norm(u, axis=1)[:, None]
        r0 = np.linalg.norm(x[alive], axis=1)
        x[alive] += P * u
        r1 = np.linalg.norm(x[alive], axis=1)
        for k, s in enumerate(shells):
            out = (r0 < s) & (r1 >= s); inn = (r0 >= s) & (r1 < s)
            net[k] += out.sum() - inn.sum(); gross[k] += out.sum() + inn.sum()
        idx = np.where(alive)[0]; alive[idx[r1 >= Rmax]] = False
    return shells, net / n, gross / n

print("(gross/(R/PSR) ~ constant near the source: the raw traffic per unit area falls as 1/R, like a potential;\n absorption at R_max = 30 PSR bends it down at large R. Net per unit area falls as 1/R^2, like a field.)\n")
print("relay: hop = one PSR, lossless, isotropic; per unit of influence emitted from the band")
res = {}
for P in (8.0, 7.2):
    sh, net, gross = run(P)
    res[P] = (sh, net, gross)
    for s, a, g in zip(sh, net, gross):
        print(f"P={P:4.1f}  R={s/P:4.0f} PSR  net outward {a:6.3f}   gross crossings {g:7.2f}   gross / (R/PSR) {g/(s/P):5.2f}")
print("\nwhat a test charge at R (in PSRs) reads, well (P=7.2) / flat (P=8):")
for k, s in enumerate(res[8.0][0]):
    r = s / 8.0
    netA = res[8.0][1][k] / (4*np.pi*(r*8.0)**2); netB = res[7.2][1][k] / (4*np.pi*(r*7.2)**2)
    print(f"  R={r:4.0f} PSR   net flux per GP of area: ratio {netB/netA:6.3f}   per PSR cross-section: ratio "
          f"{(netB*7.2**2)/(netA*8.0**2):6.3f}")
print("\n(1+kappa)^2 for a 10%% PSR shrink = %.3f" % (1/0.9**2))
