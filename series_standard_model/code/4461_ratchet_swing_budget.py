"""Patch 4461 -- founder: the orbital electron is an extended unit (a dynamic cloud of DP arc-separation carrying the orbital's kinetic energy,
blended with the static polarized cloud of DPs); a collision knocks the CP out of resonance; each emission-swing cycle the CP is re-energized from
the undischarged high-energy pool, drops from high on one side through the nucleus to low on the other, radiating all the way, is recharged,
moves slightly sideways (the nuclear pull overrides the kick's direction), and repeats until the interval is discharged.

Part 1. Budget: Lyman-alpha (10.2 eV, 2.466e15 Hz, lifetime 1.596 ns) radiates over ~3.9e6 cycles; Q = 2 pi f tau ~ 2.5e7; the energy leaving per
        cycle is ~1/(f tau) of what remains, ~2.6e-6 eV at the start.  A full high-to-low drop per pass (energy-level difference 10.2 eV)
        radiated each pass would be millions of photons' worth.
Part 2. Envelope (box of length tau, same initial power and total energy as the exponential, which sets where the lobes fall): a swing radiating the same amount each pass until the pool is empty has a box envelope -> sinc^2 line with side lobes
        (about 4.6% of peak between 1.2/tau and 1.8/tau); radiating a fixed share of what remains -> exponential envelope -> Lorentzian, falling smoothly (no side lobes).
Part 3. A harmonic restoring force (proportional to displacement, as inside a uniform cloud of charge) keeps a fixed rate whatever the
        amplitude.  For an electron CP inside a uniform sphere of charge +e (opposite in sign to the CP; a cloud of
        its own sign would push it out): omega^2 = k e^2/(m R^3).  The radius giving Lyman-alpha's rate.
Part 4. A rough model of his asymmetric pass (from rest at the upper Bohr radius n_u^2 a0, through the nucleus, to rest at the lower n_l^2 a0) under the Coulomb
        pull: pass time = fall time from n_u^2 a0 + fall time from n_l^2 a0, fall time from r = (pi/2) sqrt(m r^3/(2 k e^2)); out-and-back = two
        passes.  The energy difference is taken out at the nucleus (where the point-Coulomb time is negligible); the recharge leg is
        given zero time; Bohr (circular-orbit) radii as turning points -- 2 n^2 a0 (zero-angular-momentum orbit of that energy) would
        lower every rate by 2^1.5.  Only the ordering and the ratios carry the argument.  Compared with the measured lines (Bohr: f = R_H c (1/n_l^2 - 1/n_u^2)).
"""
import numpy as np
h, c, eV, me, k_e2 = 6.62607015e-34, 2.99792458e8, 1.602176634e-19, 9.1093837e-31, 2.307077e-28
a0 = 5.29177e-11
f, tau, dE = 2.466e15, 1.596e-9, 10.2
N = f*tau
print(f"Part 1  cycles in a lifetime {N:.2e}; Q = 2 pi f tau = {2*np.pi*f*tau:.2e}; first-cycle energy out {dE/N:.1e} eV "
      f"(share per cycle {1/N:.1e}); {dE:.1f} eV per pass for {N:.1e} passes = {N:.1e} photons' worth")
# Part 2: box vs exponential envelope spectra
T = 8*tau
t = np.linspace(0, T, 2**18, endpoint=False)
for name, env in (("box", (t < tau).astype(float)), ("exponential", np.exp(-t/(2*tau)))):
    S = np.abs(np.fft.rfft(env))**2; S /= S.max()
    nu = np.fft.rfftfreq(t.size, t[1]-t[0])
    lobe = S[(nu > 1.2/tau) & (nu < 1.8/tau)].max()
    print(f"Part 2  {name:11s}: largest response between 1.2/tau and 1.8/tau = {lobe:.3f} of peak")
R = (k_e2/(me*(2*np.pi*f)**2))**(1/3)
print(f"Part 3  uniform-cloud radius for Lyman-alpha's rate: R = {R:.3e} m = {R/a0:.2f} Bohr radii")

def tfall(r): return np.pi/2*np.sqrt(me*r**3/(2*k_e2))
RHc = 3.28984196e15
for name, nu_, nl in (("Lyman-alpha", 2, 1), ("Lyman-beta", 3, 1), ("Balmer-alpha", 3, 2)):
    fswing = 1/(2*(tfall(nu_**2*a0) + tfall(nl**2*a0)))
    fline = RHc*(1/nl**2 - 1/nu_**2)
    print(f"Part 4  {name:12s} {nu_}->{nl}: swing {fswing:.2e} Hz, line {fline:.2e} Hz, ratio {fswing/fline:.2f}")
print(f"        model Lyman-beta/Lyman-alpha {(1/(tfall(9*a0)+tfall(a0)))/(1/(tfall(4*a0)+tfall(a0))):.2f} (measured {(1-1/9)/(1-1/4):.2f}); "
      f"model Lyman-beta/Balmer-alpha {(tfall(9*a0)+tfall(4*a0))/(tfall(9*a0)+tfall(a0)):.2f} (measured {(1-1/9)/(1/4-1/9):.2f})")
