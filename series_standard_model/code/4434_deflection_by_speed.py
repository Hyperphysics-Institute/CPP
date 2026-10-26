"""Patch 4434 -- founder: the limb gradient produces gravity and the electron's velocity has no effect on it; the background is
perceived but neutralized (no gradient in mass-free space).

GR's deflection of a particle of speed v passing a mass M at impact parameter b (weak field, G = c = 1):
    delta = (2 M / (b v^2)) (1 + v^2)
A velocity-independent push (the limb, clock half; 4403) gives the Newtonian part 2M/(b v^2). The remainder, 2M/b, independent of
v, must come from the space part (the PSR / mu-epsilon rescaling, 4415 condition (ii)); for light it is half the total.
"""
M, b = 1.0, 1e6
print(f"{'v':>6s} {'GR total':>12s} {'limb (clock) part':>18s} {'space part':>12s} {'space share':>12s}")
for v in (0.01, 0.1, 0.5, 0.9, 1.0):
    tot = 2*M/(b*v**2)*(1 + v**2); limb = 2*M/(b*v**2); space = tot - limb
    print(f"{v:6.2f} {tot:12.4e} {limb:18.4e} {space:12.4e} {space/tot:12.3f}")
print("  slow particles: almost all from the velocity-independent limb push; light: half and half (the factor 2).")
