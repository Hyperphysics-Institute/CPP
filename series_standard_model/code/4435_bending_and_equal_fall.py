"""Patch 4435 -- founder: a fast particle's bending grows with speed, from (1) the slower inner limb (smaller PSR) and (2) its
accreting partly real mass 'falling faster': acceleration per unit mass rising with realness; light too.

Part 1. GR's coordinate acceleration of a particle of velocity v in a weak static field (PPN gamma = 1, isotropic coordinates):
        a = g (1 + v^2) - 4 v (v . g)  ->  across the field (tangential motion): g (1 + v^2); along it (radial): g (1 - 3 v^2);
        averaged over random directions: g (1 - v^2/3). The speed effect is DIRECTION-dependent, not a uniform 'falls faster'.
Part 2. A direction-blind rule 'acceleration per unit mass = g (1 + k v^2)' applied to the moving constituents of matter
        (nucleons' internal motion in nuclei, v^2 ~ 0.04-0.05) would make materials fall differently: the composition test
        MICROSCOPE (titanium vs platinum) bounds differences at ~1e-15.
Part 3. Light: the measured bending is 4GM/(bc^2) with PPN gamma - 1 = (2.1 +/- 2.3)e-5 (Cassini); any bending beyond the
        refraction already counted must fit inside that.
"""
import numpy as np
print("Part 1 (GR coordinate acceleration / g):")
for v in (0.1, 0.5, 0.9, 1.0):
    print(f"  v {v}: moving across the field {1 + v**2:.3f}   moving along it {1 - 3*v**2:+.3f}   random-direction average {1 - v**2/3:.3f}")
print("  sideways motion bends MORE with speed (light: x2); motion along the field gains LESS; a bound system's internal")
print("  motions, with their binding, fall exactly like the whole (the equivalence principle holds in GR).")

print("Part 2 (a direction-blind 'falls faster with realness', a = g (1 + k <v^2>) for internal motion):")
v2_Ti, v2_Pt = 0.040, 0.044      # illustrative mean nucleon v^2/c^2 inside nuclei (Fermi motion); they differ by ~10%
for k in (1.0, 1e-3, 1e-6):
    diff = k*abs(v2_Pt - v2_Ti)
    print(f"  k = {k:g}: titanium vs platinum differ by ~{diff:.0e}   (MICROSCOPE bound ~1e-15: excluded by ~{diff/1e-15:.0e})")
for n in (2, 6, 10, 20):
    print(f"  steep rule a = g (1 + 0.1 * v^{n}) difference at v ~ 0.2: ~{0.1*0.2**n:.0e} (bound 1e-15)")
print("  only a rule steeper than ~v^20 (a near-step at c) survives at nucleon speeds; Pt 1s electrons move at ~Z alpha ~ 0.57 c.")
print("  so a uniform increase of acceleration per unit mass with realness is excluded; the realized organization must fall")
print("  exactly as its mass-energy (equal fall), with any speed effect direction-dependent as in Part 1.")

print("Part 3 (light):")
print("  refraction by n = 1 + 2U (WC-DP-SEA-PV) already gives the full 4GM/(bc^2); Cassini bounds any extra at ~2e-5 of it.")
