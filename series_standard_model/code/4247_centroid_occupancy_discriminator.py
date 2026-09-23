#!/usr/bin/env python3
"""4247 -- who is in the W0 centroid: the NC integers as the discriminator (founders_voice/4247).
Two readings of the beta-decay centroid on file: (A) 4225 -- the W0 captures and STABILISES the d's linear -eCP in its
centroid; the orbital pole transits the pocket by chance (4229/4231: pocket 0.0025 fm, rate factor 1.2e-3).
(B) founder's recollection at 4247 -- both -eCPs pass through the centroid by chance; possibly the +qCP core sits in it.
4246's channel logic gives d_iso = 1 - 2 f, f = fraction of W0 formations with the linear -eCP in the centroid."""
import numpy as np
pocket=0.0025      # fm, W scale, 4229
A=0.105            # fm, linear -eCP displacement scale, SS-2 reasoning (offset outside its vertex; "reasonable for a linear oscillator amplitude")
# harmonic 1D motion x = A sin(wt): fraction of time with |x| < pocket
f=(2/np.pi)*np.arcsin(min(1,pocket/A))
print(f"(B) transit by chance: linear amplitude ~{A} fm, pocket {pocket} fm -> time fraction in pocket f = {f:.4f}")
for lab,ff in [("(A) stabilised capture",1.0),("(B) transit by chance",f)]:
    d=1-2*ff; print(f"  {lab:24s} f = {ff:.4f}: d_iso = 1 - 2f = {d:+.3f}   (measured 2 T3(d) = -1)   linear-oscillator weight = {d-1:+.3f} (needs -2)")
print("-> the neutral-current integers require f = 1: the linear -eCP must be IN the centroid whenever a W0 stands beside a down quark.")
print("   A core sitting in the centroid changes nothing here unless it makes the linear -eCP's occupancy 1 -- it does the opposite:")
print("   an oscillator through the core is at the core only in passing.")
hold=0.35; T_e=2*np.pi*197.327/0.511; T_q=2*np.pi*197.327/312.76
print(f"   hold time 'one Moment' read as a light-crossing of the bracelet (~{hold} fm/c) vs oscillation periods: m_e Compton {T_e:.0f} fm/c, m_const Compton {T_q:.1f} fm/c -> the hold cannot wait for the oscillator.")
print("   robustness: 0.105 fm is SS-2's static displacement used as the amplitude scale; for ANY amplitude >= 0.01 fm, f <= 0.16 and d_iso >= +0.68.")
