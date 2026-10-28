"""Patch 4445 -- founder: a photon is an envelope (packet) of ZBW oscillations; its frequency is set by the envelope duration,
short high-energy bursts vs long low-energy packets; the which-way detector absorbs part of the particle.

Part 1. Measured packets: the envelope duration (decay lifetime) sets the packet length and the linewidth; the frequency is the
        carrier inside, f = Delta E / h.  Hydrogen Lyman-alpha (2p, 1.596 ns) and the Mossbauer line of Fe-57 (14.4 keV, 141 ns mean life).
Part 2. Envelope-set frequency would be about 1/tau; compare with the measured carrier.
Part 4 (appended). Classical damping of a charge swinging at Delta E/h, weighted by the measured oscillator strength, gives the lifetime.
Part 3. Which-way and visibility: Englert's relation V^2 + D^2 <= 1 (fringe visibility V, path distinguishability D); fringes
        vanish with full path information even when nothing is absorbed (polarization tags; internal-state tags).
"""
import numpy as np
h, c, eV = 6.626e-34, 2.998e8, 1.602e-19
for name, E_eV, tau in (("H Lyman-alpha (2p)", 10.2, 1.596e-9), ("Fe-57 Mossbauer", 14.4e3, 141e-9)):
    f = E_eV*eV/h
    print(f"Part 1  {name}: carrier f = {f:.2e} Hz; envelope {tau*1e9:.1f} ns -> packet {c*tau:.2f} m long, "
          f"{f*tau:.1e} carrier cycles, linewidth {1/(2*np.pi*tau):.1e} Hz (fractional {1/(2*np.pi*tau)/f:.0e})")
    print(f"Part 2  {name}: 1/tau = {1/tau:.1e} Hz, vs carrier {f:.2e} Hz (ratio {f*tau:.0e})")
print("Part 3  V^2 + D^2 <= 1:")
for D in (0.0, 0.5, 0.9, 1.0):
    print(f"   path distinguishability D = {D}: fringe visibility at most {np.sqrt(1 - D**2):.2f}")
# Part 4. A charge swinging at the carrier frequency radiates its energy away at the classical damping rate; weighted by hydrogen's
# measured transition strength it gives the measured 2p lifetime (frequency and packet length together).
e, eps0, me = 1.602e-19, 8.854e-12, 9.109e-31
w = 2*np.pi*10.2*eV/h
gam_cl = e**2*w**2/(6*np.pi*eps0*me*c**3)
f_osc, g_ratio = 0.4162, 2/6          # Lyman-alpha absorption oscillator strength; g(1s)/g(2p)
A = 3*gam_cl*f_osc*g_ratio
print(f"Part 4  classical damping time at Lyman-alpha {1/gam_cl*1e9:.2f} ns; with f = {f_osc} and g-ratio 1/3: A = {A:.3e} /s, tau = {1/A*1e9:.2f} ns (measured 1.596 ns)")
