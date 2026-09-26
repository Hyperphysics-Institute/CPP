#!/usr/bin/env python3
"""4301 -- founders_voice/4301 made quantitative.  Lattice quantities: GP spacing s, Moment t_M, PSR = c t_M, N = DI-bits a
GP emits per Moment (AP-4: the same for every GP), f1 = the least force (one DI-bit's push: one GP of displacement per Moment).
Founder's action quantum: hbar_CPP = f1 * s * t_M   (least-stress work over one GP, over one Moment).
Broadcast: DI-bits spread over a sphere; a target CP of cross-section sigma at distance r intercepts N sigma/(4 pi r^2) per
Moment, each delivering a push f1: F(r) = N sigma f1/(4 pi r^2)  ->  U(r) = N sigma f1/(4 pi r)  (Coulomb's 1/r emerges).
Then e^2/(4 pi eps0) = U r = N sigma f1/(4 pi), and alpha = (e^2/4 pi eps0)/(hbar c) = N sigma/(4 pi s PSR):  f1 CANCELS."""
import numpy as np
alpha=1/137.035999
print("alpha = N sigma / (4 pi s PSR); with sigma = s^2 (the target intercepts what lands on its own GP):  alpha = N s / (4 pi PSR)")
print("The conversion layer (f1: force per DI-bit) cancels; alpha depends only on two lattice counts, N and PSR/s.")
for lab,ratio in (("GR-FE-1: PSR/s = 1e30",1e30),("EU budget: PSR/s = 1/9.9e-33",1/9.9e-33)):
    N=alpha*4*np.pi*ratio
    cover=4*np.pi*ratio**2; band=4*np.pi*ratio**2*0.1*ratio
    print(f"  {lab:28s}: alpha = 1/137 needs N = {N:.2e} DI-bits per GP per Moment")
    print(f"      versus 'one DI-bit on every GP of the PSR sphere' N = {cover:.1e}, or every GP of the 10% landing band N = {band:.1e}")
    print(f"      -> the covering picture over-emits by {cover/N:.0e} (sphere) to {band/N:.0e} (band); or each push is that much smaller than 1 GP.")
print("With N = the covering count itself, alpha would be PSR/s = 1e30 -- charge 1e32 times too strong.")
print("Distance-independence check: U(r) r is constant, so alpha does not depend on r (Coulomb's law is reproduced).")
