"""Patch 4460 -- founder: the CP oscillates back and forth through the nucleus; each reversal displaces the DP arc-separation the opposite way along
the CP's line of motion, as the current in a dipole antenna does; the radiation is cylindrical around that axis; the photon's direction is the
collision's; its sideways reach is as far as the CP's light-speed influence went during the swing, about half a metre; perhaps only one oscillation,
its amplitude the energy difference; 'ZBW' may be the wrong name for this driven swing.

Part 1. Dipole pattern: radiated strength ~ sin^2(theta) from the swing axis -- none along the axis, most at right angles; field along the axis's
        projection (transverse to travel).
Part 2. Sideways reach c x duration: Lyman-alpha lifetime 1.6 ns gives about 0.48 m (his half metre) and about 4 million cycles; one cycle
        (0.41 fs) gives about 0.12 um.
Part 3. One cycle cannot be one colour (4450): a one-cycle pulse spreads over a band about as wide as its frequency; Lyman-alpha's natural
        width (from its lifetime) (A/2pi ~ 1.0e8 Hz) is about 4e-8 of its frequency.
Part 4. A swing through the nucleus under the Coulomb pull keeps time by its energy (Kepler: rate ~ |E|^(3/2), the same as the circular orbit of
        that energy): draining from the n=2 to the n=1 energy, its rate sweeps by a factor 8 (bounce or pass-through only halves all rates);
        the line's natural width is 4e-8 (Doppler-broadened lines ~1e-5).
"""
import numpy as np
c, h = 2.99792458e8, 6.62607015e-34
th = np.radians([0, 30, 60, 90])
print("Part 1  dipole strength vs angle from swing axis:", ", ".join(f"{d:.0f} deg {s:.2f}" for d, s in zip(np.degrees(th), np.sin(th)**2)))
fL, tau, A = 2.466e15, 1.596e-9, 6.265e8
print(f"Part 2  c x lifetime = {c*tau:.2f} m, cycles = {fL*tau:.2e};  one cycle {1/fL*1e15:.2f} fs -> c x duration = {c/fL*1e6:.2f} um")
t = np.linspace(-20, 20, 400001) / fL
one = np.where(np.abs(t) < 0.5/fL, np.cos(2*np.pi*fL*t), 0.0)
F = np.abs(np.fft.rfft(one))**2; f = np.fft.rfftfreq(t.size, t[1]-t[0])
half = f[F > F.max()/2]
print(f"Part 3  one-cycle pulse: half-power band {half.min():.2e}-{half.max():.2e} Hz (width/freq {(half.max()-half.min())/fL:.2f}); "
      f"Lyman-alpha natural width {A/(2*np.pi):.2e} Hz = {A/(2*np.pi)/fL:.1e} of its frequency")
f1 = 6.5797e15                                # circular-orbit rate at the n=1 energy (= Rydberg frequency x 2)
rates = {}
for n in (2, 1):
    rates[n] = f1/n**3
    print(f"Part 4  Kepler rate at the n={n} energy: {rates[n]:.3e} Hz (pass-through, x1/2: {rates[n]/2:.3e})")
print(f"        sweep factor {rates[1]/rates[2]:.1f}; Lyman-alpha {fL:.3e} Hz lies between")
