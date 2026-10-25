"""Patch 4432 -- founder: the partly real DPs at Planck/PSR distance from the moving CP dominate the SSV_abs at its GP; ordinary
sea DPs and the real CPs of nearby atoms are minuscule by comparison; the effect falls as 1/r^2.

Relative contributions at the CP's GP, weight w(r) per unit of (realized) charge, for two weights (his 1/r^2; 4411's census 1/r):
  own cloud: partly real charge at one Planck length (12 neighbouring DPs, realness fraction eps; illustrative, conservative)
CAVEAT: a continuum 1/r^2 sum at r = l_P may not be CPP-native: one DI-bit per GP per origin family (R-DIBIT-FAMILY-EXCLUSION,
INWARD-FILL), and the registered relay (4355) brings distant sources in as relayed register state (1/r potential, 1/r^2 field).
  a nearby atom: Z ~ 10 real charges at 1e-10 m (and a nucleus-scale 1e-15 m for comparison)
  the Earth: ~ 3.6e51 nucleon-scale charges at 6.4e6 m (gravity's source)
"""
import numpy as np
lP = 1.616e-35
def contrib(n, r, p): return n/r**p
for p, name in ((2, "1/r^2 (his)"), (1, "1/r (census, 4411)")):
    own = contrib(12*1e-3, lP, p)          # say 12 neighbouring DPs at one Planck length, only 0.1% real
    atom = contrib(10, 1e-10, p); nuc = contrib(10, 1e-15, p)
    earth = contrib(3.6e51, 6.4e6, p)
    print(f"weight {name}: own cloud (0.1% real, 12 DPs at l_P) {own:.1e};  atom at 1e-10 m {atom:.1e} (ratio {own/atom:.0e});"
          f"  at 1e-15 m {nuc:.1e} (ratio {own/nuc:.0e});  Earth {earth:.1e} (ratio {own/earth:.0e})")
print("  1/r^2: the CP's own nearby partly real charge dominates its GP over atoms (5e46) and the whole Earth (5e29);")
print("  1/r (the census weight): it still dominates atoms, but a raw count of the Earth's charges outweighs it by ~1e12 --")
print("  so proximity settles membership only with his 1/r^2 weight, or if matter counts only by its exposed (G-sized) share.")
print("  Either way the totality equals the CP's own share only if the paired sea DPs add ~nothing:")
print("  Paired sea DPs: under a per-contribution count (4416's reading P) ~12 sit at one Planck length too, contributing")
print(f"  {contrib(12, lP, 2):.1e} (1/r^2) -- comparable to or larger than the own cloud unless a paired DP counts as ~0.")

print("Robustness:")
earth2, earth1 = 3.6e51/6.4e6**2, 3.6e51/6.4e6
print(f"  1/r^2: the cloud beats the Earth down to a realness of {earth2/(12/lP**2):.0e}")
print(f"  1/r:   12 fully real DPs at l_P fall short of the Earth by {earth1/(12/lP):.0e}")
univ = 1e80/4.4e26
print(f"  1/r over the observable universe (~1e80 charges to ~4e26 m): {univ:.0e} -- outweighs the cloud (100% real) by {univ/(12/lP):.0e}")
print("  (a Sciama/Mach-like candidate for the vacuum baseline under a 1/r sum)")
print("  Gravity under 1/r^2: the Earth's share at the electron's GP is ~1e-30 of the own cloud, while weak-field gravity needs")
print("  U ~ 7e-10 -- so gravity must act on the moving electron through a different sum or register.")
