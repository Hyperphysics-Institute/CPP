"""Patch 4446 -- founder: the photon goes out at right angles to the CP's swing, along the collision vector (a rogue DI-bit wave);
forward reinforcement and rear cancellation; the photon is an envelope holding a total energy sum of many ZBW cycles; what sets
the swing rate (Compton? the energy difference?).

Part 1. Hydrogen 2p -> 1s: the light's frequency Delta E / h, against (a) the Compton frequency and (b) the classical orbital
        revolution frequencies of n = 1 and n = 2 (genuine tests, both fail).  (c) The difference of the two states' rhythms
        (m c^2 + E_n)/h is the Bohr frequency condition: an identity, not a test.  Its content is that in QM the charge density of
        an atom between two states (quadratic in the two) oscillates at that difference.
Part 2. ILLUSTRATIVE: E = h f fixes a photon's energy whatever its packet length, so a per-cycle share is not independent.
Part 4. Line sharpness: Lyman-alpha's linewidth / frequency ~ 4e-8, so the radiating swing rate stays constant to that level while
        the swing dies away (a Coulomb fall that changed its rate with its energy would chirp).
Part 3. A random trigger at a steady rate gives exponential decay (the measured law); environment-dependent decay (Purcell
        effect; Kleppner's inhibited emission) requires the trigger to depend on the surroundings.
"""
import numpy as np
h, c, eV, Ry = 6.626e-34, 2.998e8, 1.602e-19, 13.6057
me = 9.109e-31
E1, E2 = -Ry, -Ry/4
fL = (E2 - E1)*eV/h
fC = me*c**2/h
alpha, a0 = 1/137.036, 5.29177e-11
v1, v2 = alpha*c, alpha*c/2
fr1, fr2 = v1/(2*np.pi*a0), v2/(2*np.pi*4*a0)
print(f"Part 1  light (Delta E / h) {fL:.3e} Hz")
print(f"        (a) Compton {fC:.3e} Hz (ratio {fL/fC:.1e})")
print(f"        (b) classical revolution n=1 {fr1:.3e}, n=2 {fr2:.3e}, difference {fr1-fr2:.3e} Hz (ratio to light {(fr1-fr2)/fL:.2f})")
fr_1 = (me*c**2 + E1*eV)/h; fr_2 = (me*c**2 + E2*eV)/h
print(f"        (c) rhythms (m c^2 + E_n)/h: n=1 {fr_1:.6e}, n=2 {fr_2:.6e} Hz; difference {fr_2 - fr_1:.4e} Hz (Bohr condition, identity)")
for tau in (1e-9, 1.6e-9, 10e-9):
    N = fL*tau
    print(f"Part 2  packet {tau*1e9:4.1f} ns at the same colour: {N:.1e} cycles; measured photon energy {h*fL/eV:.2f} eV every time"
          f" (a per-cycle sum would need {h*fL/eV/N:.1e} eV per cycle, changing with packet length)")
rng = np.random.default_rng(1)
tau = 1.6e-9
t = rng.exponential(tau, 200000)
for k in (1, 2, 3):
    print(f"Part 3  random trigger at rate 1/tau: fraction still excited after {k} tau = {np.mean(t > k*tau):.3f} (exp(-{k}) = {np.exp(-k):.3f})")
print(f"Part 4  Lyman-alpha linewidth {1/(2*np.pi*1.596e-9):.1e} Hz on {fL:.3e} Hz: swing rate constant to {1/(2*np.pi*1.596e-9)/fL:.0e}")
