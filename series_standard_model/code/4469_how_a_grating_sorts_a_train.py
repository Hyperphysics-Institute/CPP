"""Patch 4469 -- founder: is Claude postulating that a photon is long and narrow so the spectroscope sends it to exactly the right angle?

Part 1. How a grating sorts: G grooves each re-send part of the wave; in first order, at an angle set by a fractional wavelength mismatch delta,
        groove j's contribution is delayed by j(1 + delta) periods.  The total received energy is the time integral of the squared sum.  For a
        flat wave train of M crests the half-power width in delta is about the larger of 0.9/M and 0.9/G: a long train lines up across all grooves only at one
        angle; a short train lines up over a few grooves at a range of angles.  (Computed in the frequency domain: response = sum over the
        train's spectrum of the grating's own response.)
Part 2. Measured on lasers whose pulse length is measured separately (autocorrelation): a Gaussian pulse of duration dt (FWHM) at 800 nm has a
        spectral width dlambda = 0.441 lambda^2/(c dt): 10 fs -> ~94 nm; 100 fs -> ~9 nm; 1 ps -> ~0.9 nm.
"""
import numpy as np
G = 1000
def width(M):
    scale = 1/M + 1/G
    d = np.linspace(-4*scale, 4*scale, 2001)                       # angle mismatch
    step = min(1/M, 1/G)/40
    nu = np.arange(1 - 6*scale, 1 + 6*scale, step)                 # frequency, units of the carrier
    S = np.sinc(M*(nu - 1))**2                                      # flat M-crest train's spectrum near the carrier
    R = np.empty_like(d)
    for i, dd in enumerate(d):
        x = np.pi*nu*(1 + dd)
        g = (np.sin(G*x)/(G*np.sin(x)))**2                          # G-groove grating, first order (peak at nu(1+dd) = 1)
        R[i] = np.sum(S*g)
    h = d[R >= R.max()/2]
    return h.max() - h.min()
for M in (5, 50, 500, 5000, 50000):
    print(f"Part 1  train of {M:>6} crests, {G} grooves: angular half-power width (as fractional wavelength) {width(M):.1e}; "
          f"train alone 0.9/M = {0.886/M:.1e}, grating alone 0.9/G = {0.886/G:.1e}")
c, lam = 2.99792458e8, 800e-9
for dt in (10e-15, 100e-15, 1e-12):
    print(f"Part 2  {dt*1e15:>6.0f} fs pulse at 800 nm: spectral width {0.441*lam**2/(c*dt)*1e9:.1f} nm")
