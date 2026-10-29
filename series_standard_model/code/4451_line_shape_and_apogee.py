"""Patch 4451 -- founder: the reservoir can discharge only through the CP; each ZBW swing returns to the same apogee at the upper orbit
and takes the same increment of energy, at the same rate and amplitude, until the reservoir between the two levels is spent.

Part 1. Line shape.  A packet of constant amplitude that stops when the reservoir is spent (same increment each swing) has a sinc^2
        spectrum: side lobes, and a width set by its length.  A packet whose amplitude decays exponentially (same share of what is left
        each swing) has a Lorentzian spectrum, no side lobes.  The natural line seen with Doppler broadening removed is Lorentzian, width 1/(2 pi tau); measured decays are exponential.
        (Assumes identical packets: same increment and same total Delta E give every flat packet the same length.)
Part 2. The swing's rate with its turning point at the upper orbit: a radial Coulomb swing through the nucleus out to r_max has the
        Kepler rate of an ellipse with semi-major axis r_max/2.  From the same upper orbit (n = 3), hydrogen gives two different colours.
Part 3. Isochrony: the Coulomb swing's rate depends on its size (f ~ r_max^-1.5); a shrinking swing would change its rate.
"""
import numpy as np
# Part 1: spectra of a flat-top packet and an exponential packet, same energy-weighted length
f0, T = 1.0, 1.0
dt = T/40
tau = 200.0                                              # packet time scale, in carrier cycles
t = np.arange(0, 12*tau, dt)
flat = np.where(t < 2*tau, 1.0, 0.0)*np.cos(2*np.pi*f0*t)      # flat packet, length 2 tau (side-lobe height does not depend on length)
expo = np.exp(-t/(2*tau))*np.cos(2*np.pi*f0*t)                 # amplitude decay 2 tau = energy decay tau
n = 2**22
fr = np.fft.rfftfreq(n, dt)
for name, s in (("flat (same increment each swing)", flat), ("exponential (same share each swing)", expo)):
    S = np.abs(np.fft.rfft(s, n))**2; S /= S.max()
    m = (fr > 0.9) & (fr < 1.1)
    fm, Sm = fr[m], S[m]
    above = fm[Sm >= 0.5]; w = above.max() - above.min()
    # first side lobe: largest local max away from the peak, beyond the main lobe
    pk = np.argmax(Sm)
    far = np.abs(fm - fm[pk]) > 1.5*w
    loc = (Sm[1:-1] > Sm[:-2]) & (Sm[1:-1] > Sm[2:]) & far[1:-1]
    side = Sm[1:-1][loc].max() if loc.any() else 0.0
    print(f"Part 1  {name:36s}: FWHM {w*tau*2*np.pi:.2f} x 1/(2 pi tau); largest side lobe {side:.3f} of the peak")
# Part 2: radial swing rates vs lines from n = 3
Ry_h = 3.2898e15
f_rev1 = 2*Ry_h
radial = lambda n_up: f_rev1/((n_up**2/2.0)**1.5)
for nu in (2, 3):
    print(f"Part 2  radial swing turning at orbit {nu} (r_max = {nu**2} a0): {radial(nu):.3e} Hz")
for nu, nl in ((2, 1), (3, 1), (3, 2)):
    print(f"        line {nu} -> {nl}: {Ry_h*(1/nl**2 - 1/nu**2):.3e} Hz")
print("        from orbit 3: two lines, 2.92e15 and 4.57e14 Hz (ratio 6.4); one swing turning at orbit 3 has one rate")
# Part 3
for shrink in (1.0, 0.99, 0.9):
    print(f"Part 3  swing size x{shrink}: rate x{shrink**-1.5:.4f}  (the line holds to 4e-8)")
