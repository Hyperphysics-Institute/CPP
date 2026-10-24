"""Patch 4420 -- founder: each interplate CP coasts like any CP, by its own interaction with the local sea ('charge in front,
discharge in back'); its resistance reaches the plates by DI-bits; no watering down; no twist, because each CP's interaction
depends on its velocity through the sea, not on the plates' orientation.

The inertial part is orientation-blind, as he says. But the FORCES between the moving charges, carried by DI-bits, are not:
for two opposite charges moving together, the census channel (4411: exactly Lienard-Wiechert; force on a co-moving charge
-(1 - v^2) grad of the convection potential, equipotentials Heaviside ellipsoids) gives forces that are equal and opposite but
NOT along the line joining them when the pair is tilted to the motion. That makes a couple ~ v^2 sin(2 theta): the classical
Trouton-Noble torque. Classically no turning is seen, for two equivalent reasons: by Lorentz's corresponding states a structure
in equilibrium at rest stays in equilibrium when moving if every force transforms alike; and in Laue's terms (1911) the lab-frame
couple equals the rate of change of the angular momentum carried by the moving body's stresses and field, so nothing turns.
CPP must meet the same condition.

Units: q = 1, separation d = 1, c = 1.
"""
import numpy as np
def force_on_B(v, theta):
    # charge A (+1) at origin, charge B (-1) at r = (cos t, sin t); both move along x at speed v
    x, y = np.cos(theta), np.sin(theta)
    R3 = (x**2 + (1 - v**2)*y**2)**1.5
    E = np.array([x, (1 - v**2)*y])/R3          # grad-based field shape of the convection potential (up to constants)
    return -(1 - v**2)*E                          # force on the opposite charge (attractive), co-moving
print("Couple on a co-moving opposite pair tilted at theta to the motion (census / Lienard-Wiechert channel):")
for v in (0.001, 0.1, 0.5):
    row = []
    for th in (0, 30, 45, 60, 90):
        t = np.radians(th); F = force_on_B(v, t)
        r = np.array([np.cos(t), np.sin(t)])
        torque = r[0]*F[1] - r[1]*F[0]            # couple of the equal-and-opposite pair = r x F_B
        row.append(f"{th:2d} deg: couple {torque:+.2e}")
    print(f"  v {v}: " + ";  ".join(row))
print("  zero at 0 and 90 degrees, largest near 45 at low speed (the peak moves past 45 as v grows), growing as v^2:")
print("  the force on each charge is off the line between them (the velocity-dependent, magnetic-like part of the census).")
print("  equal and opposite (no net push) but not collinear: a couple. No turning results if every force holding the structure")
print("  follows the same rule (corresponding states; 4410), equivalently if the couple is matched by the rate of change of the")
print("  angular momentum the moving stresses and field carry (Laue).")
