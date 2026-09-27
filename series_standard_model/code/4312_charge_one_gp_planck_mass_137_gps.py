#!/usr/bin/env python3
"""4312 -- the exchange.  AP-4: every GP emits N0 DI-bits per Moment.  4301: coupling strength = (organised emission)/(4 pi R),
R = GPs per PSR.  A unit charge is ONE GP's emission: alpha = N0/(4 pi R).  A Planck mass couples at strength 1 (GR-1a's
hierarchy alpha_G = (m/m_P)^2): its organised emission is G_P N0 with G_P N0/(4 pi R) = 1.  So G_P = 1/alpha."""
import numpy as np
alpha=1/137.035999; me=9.1093837015e-31; mP=2.176434e-8
print(f"a unit charge = one GP's emission N0 = 4 pi alpha R;  a Planck mass = the coherent emission of G_P = 1/alpha = {1/alpha:.3f} GPs")
print(f"an electron's gravitational source = (m_e/m_P) x G_P = {(me/mP)/alpha:.2e} GP-emissions (coherent), against its charge's 1.0")
for R in (1e30,1e32):
    N0=4*np.pi*alpha*R; rc=np.sqrt(N0/(4*np.pi)); rP=np.sqrt(G:=1/alpha)*rc
    print(f"R = {R:.0e}: N0 = {N0:.2e};  crowding radius of one GP's volley = {rc:.2e} GPs = sqrt(alpha R);"
          f"  of a Planck mass's = {rP:.2e} GPs = sqrt(R) = sqrt(s x PSR)/s  (the geometric mean of the two lattice lengths)")
print("600-cell counts for comparison (none is 137): vertices 120, edges 720, faces 1200, cells 600; icosahedral neighbours 12.")
