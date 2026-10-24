"""Patch 4422 -- toward 4421's owed item 1: are the binding forces (short-range, strong) counted with the same PSR ruler?

Statement tested: a force channel whose field is relayed at light speed c and obeys a wave equation of the covariant form
(d_t^2 - c^2 lap + m^2) phi = source has, around a uniformly moving source, the static profile with the along-motion
coordinate stretched by gamma: phi_moving(x, y, z) = gamma * phi_static(gamma x, y, z) -- the |Lambda r| shape of 4411/4421 --
WHATEVER its range (m) or static law. A channel relayed at a different speed c_s flattens by sqrt(1 - v^2/c_s^2) instead,
so its forces would be counted with a different ruler and a structure bound by it would twist (4421 Case B).

Method: steady state in the source's frame, d_t = -v d_x, so -((c^2 - v^2) d_x^2 + c^2 lap_perp) phi + m^2 phi = delta.
Solved by FFT on a periodic 3D grid (160^3, box 24, small Gaussian source of width 0.25; no assumption of the answer). Measure
the aspect ratio of an equipotential: the distance ahead at which phi equals its value 4 units to the side (log interpolation).
This is an ILLUSTRATION; the proof is the one-line rescaling x' = gamma x of the steady equation. Grid errors: up to ~4% at the
strongest flattening (sign set by the source width), and for the long-range channel (m = 0.05, range ~20 in a box of 24)
periodic images make the error grow with distance (about -6% at 8 units).
"""
import numpy as np
n, L = 160, 24.0
sig = 0.25                                          # small Gaussian source (avoids the grid singularity)
k = 2*np.pi*np.fft.fftfreq(n, d=L/n)
kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
x = (np.arange(n) - n//2)*(L/n)
def steady(v, c, m):
    denom = (c**2 - v**2)*kx**2 + c**2*(ky**2 + kz**2) + m**2
    S = np.exp(-(kx**2 + ky**2 + kz**2)*sig**2/2)
    return np.fft.fftshift(np.real(np.fft.ifftn(S/denom)))
def aspect(phi, side=4.0):
    c0 = n//2; xs = x[c0:]
    lx = np.log(np.clip(phi[c0:, c0, c0], 1e-300, None)); ly = np.log(np.clip(phi[c0, c0:, c0], 1e-300, None))
    target = np.interp(side, xs, ly)                  # log-interpolated value one 'side' distance across the motion
    return np.interp(-target, -lx, xs)/side           # distance ahead with the same value, over the side distance
print("Equipotential aspect (ahead / side) for a uniformly moving source, field steady-solved on a 3D grid:")
print(f"{'channel':38s} {'v':>5s} {'measured':>9s} {'1/gamma (c)':>12s} {'sqrt(1-v^2/cs^2)':>17s}")
for label, c, m in (("long range (m=0.05), relayed at c", 1.0, 0.05),
                    ("short range (m=0.8), relayed at c", 1.0, 0.8),
                    ("short range (m=0.8), relayed at 0.7c", 0.7, 0.8)):
    for v in (0.3, 0.6):
        if v >= c: continue
        r = aspect(steady(v, c, m))
        print(f"{label:38s} {v:5.1f} {r:9.4f} {np.sqrt(1-v**2):12.4f} {np.sqrt(1-v**2/c**2):17.4f}")
print("  Relayed at c, long or short range: the same 1/gamma flattening (to grid accuracy) -- one ruler for every range.")
print("  Relayed at another speed: a different flattening -- a different ruler, and a structure bound by it would twist.")
