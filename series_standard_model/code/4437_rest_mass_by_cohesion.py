"""Patch 4437 -- founder: gravity's push acts on the rest mass; motion inside a body's frame, held together by internal cohesion,
contributes rest mass; the DP arc-separation from the motion of the whole has no radial force connection to the rest mass (only the
axial SSV_net); the turning acts on the entire rest mass; light (no rest mass) gets only the turning. [Claude's reading, not his words:
the turning is 4436's full-strength, mass-independent Snell turning, so the motion's effect is carried by the turning.] for the Earth-electron system taken as a whole, the electron's
kinetic energy is internal and part of that system's gravitating mass.

Part 1. Rest mass by cohesion = relativity's invariant mass: E^2 - p^2 for the system. Examples: two balls flying apart; a hot gas;
        an electron passing the Earth taken with the Earth.
Part 2. What "the push acts on the rest mass" has to mean quantitatively (4436): an acceleration g (m/E)^2 = g/gamma^2 in every
        direction. A literal Newtonian force m g on the moving body would give g/gamma across (inertia gamma m) and g/gamma^3 along
        (inertia gamma^3 m); with the full turning (4436) that misses GR.
Part 3. Why cohesion matters in GR (critic): free particles of an isotropic gas, averaged over directions, fall at (1 - v^2/3) g, not g;
        a bound body falls at g with all its internal energy weighing only when its internal stresses are included (von Laue / Tolman).
"""
import numpy as np
print("Part 1 (invariant mass M = sqrt(E^2 - p^2), c = 1):")
m = 1.0
for v in (0.6, 0.9):
    g = 1/np.sqrt(1 - v**2)
    E2, p2 = 2*g*m, 0.0                                   # two balls flying apart at +/- v
    print(f"  two balls of rest mass 1 flying apart at {v}: system rest mass {np.sqrt(E2**2 - p2**2):.3f} (> 2: their motion counts)")
me, ME = 1.0, 1e30
for v in (0.6, 0.9):
    g = 1/np.sqrt(1 - v**2)
    E, p = ME + g*me, g*me*v
    Mexcess = (g - 1)*me - p**2/(2*E)                      # sqrt(E^2 - p^2) - ME - me, expanded (avoids round-off at 1e30)
    print(f"  electron (1) passing the Earth ({ME:.0e}) at {v}: system rest mass - (Earth + electron rest) = {Mexcess:.3f}"
          f"  (kinetic energy {g - 1:.3f}: internal to the system, so it counts)")
print("Part 2 (acceleration / g; GR: across 1 + v^2, along 1 - 3 v^2):")
for v in (0.5, 0.9):
    g = 1/np.sqrt(1 - v**2)
    turn_across, turn_along = 2*v**2, 2*v**2 - 4*v**2
    print(f"  v {v}: push g/gamma^2 -> across {1/g**2 + turn_across:.3f} along {1/g**2 + turn_along:+.3f}   |"
          f" literal force m g -> across {1/g + turn_across:.3f} along {1/g**3 + turn_along:+.3f}   | GR {1 + v**2:.3f} {1 - 3*v**2:+.3f}")
print("Part 3 (free particles averaged over directions, GR: 2/3 across + 1/3 along):")
for v in (0.1, 0.3, 0.5):
    avg = (2*(1 + v**2) + (1 - 3*v**2))/3
    print(f"  v {v}: average acceleration {avg:.4f} g  (= 1 - v^2/3 = {1 - v**2/3:.4f}); the walls' or binding's stresses restore g")
