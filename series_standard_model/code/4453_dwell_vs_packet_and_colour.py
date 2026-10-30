"""Patch 4453 -- founder: the click histogram shows only the dwell time before emission commits, not how long the ZBW cycling lasts;
what produces the colour, given the ZBW rate ~1e20 Hz and visible light ~1e15 Hz?

Part 1. Dwell-then-burst vs a packet lasting the lifetime.  A random delay does not change a packet's spectrum (it is a phase shift),
        so the line width is set by the packet's own length.  Measured natural widths equal 1/(2 pi tau) with tau the measured lifetime:
        Na D2 16.25 ns -> 9.79 MHz, Rb D2 26.24 ns -> 6.07 MHz (reference widths, e.g. Steck's alkali data, are computed from the lifetimes;
        direct Doppler-free line-width measurements agree within their precision), H Lyman-alpha 1.596 ns -> 99.7 MHz.
        A short burst (e.g. 1000 cycles) would be broad whatever its delay.
Part 2. Coherence length ~ c x lifetime (expected, not measured here; field visibility falls as exp(-dt/2tau), so 1/e at ~2 c tau).
Part 4. Dwell plus a tau-long packet: an exponential dwell convolved with an exponential packet of the same tau gives a click
        histogram that starts at zero and rises (t exp(-t/tau)); the measured single-atom histogram rises sharply at t = 0.
Part 3. The colour as the difference of two ZBW-scale rhythms: (m c^2 + E_n)/h for the two orbits, both ~1.2356e20 Hz,
        differing by the light's frequency, one part in about 50,000.
"""
import numpy as np
c, h, eV, me = 2.998e8, 6.626e-34, 1.602e-19, 9.109e-31
for name, tau, measured, lam in (("Na D2", 16.25e-9, 9.79e6, 589.0e-9), ("Rb D2", 26.24e-9, 6.07e6, 780.2e-9), ("H Lyman-alpha", 1.596e-9, None, 121.6e-9)):
    w = 1/(2*np.pi*tau)
    burst = 0.62*(c/lam)/1000          # spectral FWHM of a Gaussian burst N cycles wide ~ 0.62 f / N (4450)
    m = f"{measured/1e6:.2f} MHz, reference" if measured else "n/a"
    print(f"Part 1  {name}: 1/(2 pi tau) = {w/1e6:.2f} MHz (measured natural width {m}); a 1000-cycle burst after any delay: {burst/1e6:.0f} MHz")
    print(f"Part 2  {name}: coherence length c tau = {c*tau:.2f} m")
Ry = 13.6057
r1 = (me*c**2/eV - Ry)*eV/h; r2 = (me*c**2/eV - Ry/4)*eV/h
print(f"Part 3  ZBW-scale rhythm, orbit 1: {r1:.7e} Hz; orbit 2: {r2:.7e} Hz; difference {r2 - r1:.4e} Hz (Lyman-alpha 2.467e15); "
      f"fraction {(r2 - r1)/r1:.1e} (1 part in {r1/(r2 - r1):.0f})")
rng = np.random.default_rng(5)
tau = 1.0
dwell, pk = rng.exponential(tau, 200000), rng.exponential(tau, 200000)
for name, t in (("emission starting at excitation", pk), ("exponential dwell, then tau-long packet", dwell + pk)):
    h, _ = np.histogram(t, bins=8, range=(0, 4*tau))
    print(f"Part 4  {name:40s}: " + " ".join(f"{x/len(t):.3f}" for x in h) + "  (bins of tau/2)")
print("        burst of 1000 cycles at 589 nm is %.2f mm long: its fringes are lost beyond about a millimetre of path difference" % (1000*589e-9*1e3))
