"""Patch 4450 -- founder: the one-cycle photon he proposes is a perfectly sinusoidal discharge of a single frequency, not a square wave;
a cascade starting at one point in the DP Sea spreads and releases exactly Delta E.

Part 1. Spectral width (FWHM of the power spectrum, as a fraction of the central frequency), by FFT, for pulses about one cycle long:
        a true single sine cycle sin(2 pi t) on [0, T] (starts and ends at zero); a cosine cycle with jumps at its ends; a Hann envelope
        one cycle wide at half height (window 2T); Gaussian envelopes one cycle wide (amplitude FWHM, and intensity FWHM, the 4448
        convention); and Gaussians 10 and 100 cycles wide.  The spread falls as (0.44 to 0.62)/N, depending on how length is measured.
Part 2. Cascade timing: a single sweep across the atom at light speed (an assumption: he named no speed) vs the 1.6 ns emission;
        the sweep speed that would last 1.6 ns.
"""
import numpy as np
def fwhm_fraction(sig, dt, f0):
    n = 2**22
    S = np.abs(np.fft.rfft(sig, n))**2
    fr = np.fft.rfftfreq(n, dt)
    S /= S.max()
    above = fr[S >= 0.5]
    return (above.max() - above.min())/f0, fr[np.argmax(S)]/f0
f0 = 1.0; T = 1/f0; dt = T/2000
t = np.arange(-60*T, 60*T, dt)
cases = []
cases.append(("one true sine cycle, sin on [0, T]", np.where((t >= 0) & (t <= T), np.sin(2*np.pi*f0*t), 0.0)))
cases.append(("one cosine cycle, jumps at its ends", np.where(np.abs(t) <= T/2, np.cos(2*np.pi*f0*t), 0.0)))
cases.append(("Hann envelope one cycle wide at half height", np.where(np.abs(t) <= T, np.cos(np.pi*t/(2*T))**2*np.cos(2*np.pi*f0*t), 0.0)))
for label, N, conv in (("Gaussian, amplitude one cycle wide", 1, 1.0), ("Gaussian, intensity one cycle wide (4448)", 1, np.sqrt(2)),
                       ("Gaussian, amplitude 10 cycles wide", 10, 1.0), ("Gaussian, amplitude 100 cycles wide", 100, 1.0)):
    sigma = N*T/2.355*conv
    tt = np.arange(-8*sigma - T, 8*sigma + T, dt)
    cases.append((label, (np.exp(-tt**2/(2*sigma**2))*np.cos(2*np.pi*f0*tt), tt)))
print("Part 1  spectral FWHM / central frequency:")
for name, sig in cases:
    s = sig[0] if isinstance(sig, tuple) else sig
    w, peak = fwhm_fraction(s, dt, f0)
    print(f"   {name:46s}: {w:.3f}  (peak at {peak:.2f} f0)")
print("   measured Lyman-alpha: 4e-8 (millions of cycles)")
c, a0, fL, tau = 2.998e8, 5.29e-11, 2.467e15, 1.596e-9
print(f"Part 2  sweep across the radius at light speed: {a0/c:.2e} s = {a0/c*fL:.1e} of a cycle (diameter: {2*a0/c*fL:.1e}); "
      f"emission lasts {tau:.2e} s = {tau*fL:.1e} cycles; a single sweep lasting 1.6 ns would move at {a0/tau*100:.1f} cm/s")
