"""Patch 4480 -- founder: a warm molecule loses quantum elements as it radiates, so its fringes blur because molecules that have
lost more or less are compared against each other; the glowing quantum becomes a smaller quantum group.

Two checks on C70 at 190 m/s (Hackermueller et al. 2004), standard numbers:
(1) energy lost: one thermal photon of ~1 eV changes the molecule's mass, and so its de Broglie wavelength, by a fraction
    E/(mc^2); compared with the beam's own velocity spread (8-35% FWHM, Brezger et al. 2002), which the near-field interferometer already tolerates.
(2) which-way: for one photon emitted (isotropically) while the two paths are a distance dx apart, the fringe contrast is
    multiplied by sinc(2 pi dx / lambda) (standard decoherence factor, sin(x)/x): photons much longer than the path separation
    leave the fringes; photons shorter than it erase them.  Loss of mass-energy alone would not depend on lambda/dx.
(3) momentum: the same photon carries off h/lambda; the random sideways kick, averaged over directions, gives the same sinc factor.
    Recoil and which-way record are two descriptions of one effect.
"""
import numpy as np
amu_eV = 931.494e6
m = 840*amu_eV                     # C70 rest energy, eV
for E in (1.0, 2.0):
    print(f"(1) one {E:.0f} eV photon: fractional mass (and de Broglie wavelength) change {E/m:.1e}; 100 photons {100*E/m:.1e}; spread 8-35% is {0.08/(E/m):.0e} to {0.35/(E/m):.0e} times larger")
dx = 1.0                            # micrometres, of order the grating period (0.99 um)
for lam in (0.7, 1.5, 3.0, 5.0, 10.0, 20.0):
    x = 2*np.pi*dx/lam
    print(f"(2) photon wavelength {lam:5.1f} um, path separation {dx} um: contrast factor {np.sin(x)/x:+.3f}")
h=6.62607015e-34; c=299792458.0; e=1.602176634e-19; m_kg=840*1.66053907e-27; v=190.0; d=0.99e-6
for E in (1.0, 2.0):
    p=E*e/c; lam=h*c/(E*e)
    print(f"(3) one {E:.0f} eV photon ({lam*1e6:.2f} um): sideways kick {p/m_kg:.1e} m/s vs grating kick h/(m d) {h/(m_kg*d):.1e} m/s (ratio d/lambda {d/lam:.2f}); forward change {p/(m_kg*v):.1e} of the speed")
