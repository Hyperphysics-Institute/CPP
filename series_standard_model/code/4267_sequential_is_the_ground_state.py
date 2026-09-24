#!/usr/bin/env python3
"""4267 -- the founder's sequential picture (4263: one line at a time, direction chosen at each passage through the
vertex, energy carried through -- R-ZBW-PASS-THROUGH) is the classical reading of the quantum ground state of the
same well, not a different state.
In a harmonic well, straight line orbits through the centre are exact classical solutions with zero angular momentum;
an ensemble of them with random directions is the classical L = 0 ensemble.  The quantum ground state is L = 0.
Check, isotropic well K = 1 (units m_const, c, hbar): quantum ground (Gaussian, <p^2> = 3/2) against classical line
orbits at the SAME energy (E = 3/2 hbar omega, p along the line = p_max sin(omega t), p_max^2 = 3), NR and REL-weighted
by the free-spinor R.  Then the ruled anisotropic set is taken from 4262/4263 rows."""
import numpy as np
rng=np.random.default_rng(4267); N=4_000_000; gA_t=1.2754
R=lambda P2:1/3+2/3*np.mean(1/np.sqrt(P2+1))
q=(rng.normal(size=(N,3))*np.sqrt(0.5)); Rq=R((q**2).sum(1))
pl=np.sqrt(3)*np.sin(rng.uniform(0,2*np.pi,N)); Rc=R(pl**2)
print(f"isotropic K=1:  quantum ground state          <p^2> = {np.mean((q**2).sum(1)):.3f}   R = {Rq:.4f}   (5/3)R = {5/3*Rq:.4f}")
print(f"                classical line orbits, same E <p^2> = {np.mean(pl**2):.3f}   R = {Rc:.4f}   (5/3)R = {5/3*Rc:.4f}")
print(f"                difference in (5/3)R: {5/3*(Rc-Rq):+.4f} ({100*(Rc/Rq-1):+.2f}%)")
print("\nruled anisotropic set (rows on file): quantum ground state 1.3331 (4262); sequential bounce readings 1.3162-1.3830")
print("(4263 (E), whose chi-3 'n = 1' row is exactly an isotropic Gaussian's |p|); classical bounce 1.3219.")
print("\n-> Line orbits through the centre at the ground-state energy reproduce the quantum ground state's g_A to 0.5%:")
print("   the sequential picture and the simultaneous-mode ground state are one state described two ways.  The quantum")
print("   number is the one to carry; with the u-u exchange (4262), 1.310.  No separate 'sequential exchange' exists.")
