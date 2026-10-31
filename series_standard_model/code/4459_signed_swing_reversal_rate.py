"""Patch 4459 -- founder: the DP displacement swings forward and back with the direction of the CP's oscillation (a signed swing, radiated
like a dipole antenna's); two parts out of step giving net-zero V_i, a dark fringe, is "consistent with what could be produced".

Part 1. Assumes linear superposition (an arithmetic check, not a test of the relay); energy taken as the square of the swing (not derived in CPP).
        Two equal signed swings, same polarization, half a cycle apart sum to zero; in step they double: time-averaged energy x2 the two parts'
        separate total (x4 one part alone) at the bright band, 0 at the dark; averaged over the phase difference (the fringe pattern), the
        separate total.
Part 2. Each reversal of the CP's direction makes one reversal of the radiated DP displacement, so the radiated swing reverses as often as the
        CP does.  Hydrogen's Lyman-alpha (2.47e15 Hz) needs 4.9e15 reversals a second; a CP reversing at the free electron's zitterbewegung
        rate (2 m c^2/h ~ 2.5e20 Hz, about 4.9e20 reversals a second) would radiate at that rate: wavelength h/(2mc) ~ 1.2 pm (half the Compton
        wavelength), photon energy 2 m c^2 ~ 1.02 MeV.
"""
import numpy as np
x = np.linspace(0, 3, 3001)
a, b = np.cos(2*np.pi*x), np.cos(2*np.pi*x + np.pi)
print(f"Part 1  half a cycle apart: max |V_i sum| = {np.max(np.abs(a + b)):.1e};  in step: max |sum| = {np.max(np.abs(a + a)):.2f}")
print(f"        mean energy: two separately {np.mean(a**2) + np.mean(b**2):.3f}; bright band {np.mean((a + a)**2):.3f}; dark band {np.mean((a + b)**2):.1e}")
deltas = np.linspace(0, 2*np.pi, 721)[:-1]
avg = np.mean([np.mean((a + np.cos(2*np.pi*x + d))**2) for d in deltas])
print(f"        averaged over the phase difference (fringe pattern): {avg:.3f}")
h, c, me = 6.62607015e-34, 2.99792458e8, 9.1093837e-31
fL = 2.467e15
fZ = 2*me*c**2/h
print(f"Part 2  Lyman-alpha {fL:.3e} Hz: {2*fL:.2e} reversals/s, wavelength {c/fL*1e9:.1f} nm")
print(f"        zitterbewegung {fZ:.3e} Hz: {2*fZ:.2e} reversals/s, wavelength {c/fZ*1e12:.2f} pm, photon energy {h*fZ/1.602176634e-13:.3f} MeV; ratio to Lyman-alpha {fZ/fL:.2e}")
