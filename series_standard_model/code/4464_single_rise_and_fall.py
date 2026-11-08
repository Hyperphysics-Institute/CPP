"""Patch 4464 -- founder's new postulate: the colour is the photon's whole energy packet; out of resonance the CP's velocity goes from zero to a
maximum and back to zero once as it settles into the lower orbital, so the radiated DP arc-separation rises from zero to a maximum and falls to
zero; that one rise-and-fall is the photon's waving, shorter (more violet) for a larger energy difference.

Model: velocity v(t) = v_max sin^2(pi t / T) for 0 < t < T (zero to max to zero).  The radiated field of an accelerated charge follows the
acceleration a = dv/dt, which is positive then negative: a single-cycle pulse.
Part 1. T chosen so the radiated spectrum peaks at Lyman-alpha (2.466e15 Hz): T, the pulse length c T, the spectrum's half-power width as a
        share of the peak, and the number of fringes such a pulse could show (about peak / width), against the natural line (4.0e-8) and the
        lifetime's cycle count (3.9e6).
Part 2. Energy radiated by one such rise-and-fall (Larmor, P = e^2 a^2 / (6 pi eps0 c^3)), with v_max from KE = 10.2 eV (an upper value for an
        electron's speed in this transition), against the 10.2 eV the photon carries.
Part 3. The same pulse for the sodium D line (509 THz): its length.
"""
import numpy as np
e, eps0, c, me, eV = 1.602176634e-19, 8.8541878128e-12, 2.99792458e8, 9.1093837e-31, 1.602176634e-19
def pulse(T, n=2**20, span=400):
    t = np.linspace(-span*T/2, span*T/2, n, endpoint=False); dt = t[1]-t[0]
    v = np.where((t > 0) & (t < T), np.sin(np.pi*t/T)**2, 0.0)
    a = np.gradient(v, dt)
    S = np.abs(np.fft.rfft(a))**2; f = np.fft.rfftfreq(n, dt)
    return t, v, a, f, S
fL = 2.466e15
t, v, a, f, S = pulse(1.0)
fpk1 = f[np.argmax(S)]                      # peak frequency for T = 1
T = fpk1/fL
half = f[S > S.max()/2]*(1/T)
fpk = fpk1/T
print(f"Part 1  T for a Lyman-alpha peak: {T:.2e} s; pulse length c T = {c*T*1e6:.2f} um")
print(f"        half-power band {half.min():.2e}-{half.max():.2e} Hz, width/peak = {(half.max()-half.min())/fpk:.2f} "
      f"(natural line 4.0e-08); fringes about {fpk/(half.max()-half.min()):.1f} (lifetime cycles 3.9e+06)")
vmax = np.sqrt(2*10.2*eV/me)
amax = vmax*np.pi/T                          # max of d/dt [vmax sin^2(pi t/T)] = vmax pi / T
Erad = e**2/(6*np.pi*eps0*c**3) * (vmax*np.pi/T)**2 * (T/2)   # mean of cos^2-type a^2 over the pulse = amax^2/2
print(f"Part 2  v_max = {vmax:.2e} m/s, distance moved {vmax*T/2*1e10:.2f} Angstrom, peak acceleration {amax:.2e} m/s^2")
print(f"        Larmor energy radiated in one rise-and-fall {Erad/eV:.1e} eV, against 10.2 eV: short by a factor {10.2*eV/Erad:.1e}")
fNa = 5.09e14
print(f"Part 3  sodium D: T = {fpk1/fNa:.2e} s, length {c*fpk1/fNa*1e6:.2f} um")
