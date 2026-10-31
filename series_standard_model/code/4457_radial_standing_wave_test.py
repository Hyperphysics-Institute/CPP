"""Patch 4457 -- founder: the colour is set by the DP-separation signal running from the photon's centre to its circumference and reflecting
back, a radial standing wave with a constant amplitude profile against radius; its propagation speeds up with energy (more realness, more
exposed charge, more V_i); the smallest increment is one GP per Moment, far below any radio photon.

Part 1. A wave that bounces across its own width while travelling (a waveguide mode): omega^2 = (c k_along)^2 + omega_across^2.  Its speed
        along is c sqrt(1 - (omega_across/omega)^2).  If all of the colour came from the across (radial) standing wave, omega_across = omega
        and the photon would not move.
Part 2. A FIXED sideways rhythm shared by every photon would act as a mass: the photon-mass bound m < 1e-18 eV (Particle Data Group) caps it
        at m c^2 / h.  (It does not cap a sideways structure that varies with the beam: structured photons do travel slightly slower,
        Giovannini et al. 2015.)  His case, the bounce setting the whole colour, is share = 1: no travel at all, with no bound needed.
Part 3. If the radial signal moved at c, a radial standing wave at the colour's frequency would make the photon's radius ~ c/(2f) = lambda/2.
Part 4. A profile many wavelengths wide costs only a tiny sideways share, delay ~ (k_across/k)^2/2 per unit length (Gouy/geometric).
"""
import numpy as np
h, c, eV = 6.62607015e-34, 2.99792458e8, 1.602176634e-19
print("Part 1  share of the colour from the across standing wave -> speed along (/c):")
for r in (0.0, 1e-6, 0.1, 0.5, 0.9, 1.0):
    print(f"        {r:8.1e} -> {np.sqrt(1 - r**2):.12f}")
m_eV = 1e-18
print(f"Part 2  photon-mass bound {m_eV:.0e} eV -> any across-standing frequency below {m_eV*eV/h:.1e} Hz "
      f"(visible light 5e14 Hz: share < {m_eV*eV/h/5e14:.0e})")
for name, f in (("FM radio 100 MHz", 1e8), ("visible 500 THz", 5e14), ("gamma 1 MeV", 1e6*eV/h)):
    print(f"Part 3  {name}: radius for a radial standing wave at light speed ~ {c/(2*f):.2e} m")
for w_over_lam in (0.5, 5.0, 100.0):
    share = 1/(np.pi*w_over_lam)                     # k_across/k ~ lambda/(pi w) for a Gaussian of waist w
    print(f"Part 4  profile width {w_over_lam:6.1f} wavelengths: sideways share ~{share:.1e}, speed {np.sqrt(max(0.0, 1 - share**2)):.8f} c")
