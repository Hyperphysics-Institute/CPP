#!/usr/bin/env python3
"""4331 -- T1 (4326) made quantitative as a REQUIRED law for the swing.

With alpha = PSR/(2L) (4330: solid band), the measured running of alpha fixes how the swing must shorten as a charge
is probed closer.  Leading-log QED:  1/alpha(Q) = 1/alpha0 - (2/(3 pi)) sum_f N_c Q_f^2 ln(Q/m_f)  for Q > m_f
(Q in units of mass; the probing distance r ~ hbar/(Q c)).  So L(r) = (PSR/2)/alpha(r) and
        dL/d ln r = (PSR/(3 pi)) * sum_{f: r < lambdabar_f} N_c Q_f^2
-- inside each charged species' reduced Compton length the swing shortens by PSR/(3 pi) x N_c Q_f^2 per e-fold closer.
c04: the electron's eDP polarisation cloud has radius r_th = lambdabar_C/2 (c04 eq. rth).  The electron's running
begins at r ~ lambdabar_C, the cloud's diameter: the swing starts to shorten where the probe enters the charge-stressed
(SSV_net) cloud -- the founder's 4327 split, located."""
import numpy as np
a0inv = 137.035999084
me, mmu, mtau, MZ = 0.51099895e-3, 0.1056583755, 1.77686, 91.1876   # GeV
k = 2/(3*np.pi)

print("required swing law (alpha = PSR/(2L), leading log)")
print(f"   electron only: dL/d ln r = PSR/(3 pi) = {1/(3*np.pi):.4f} PSR per e-fold closer, inside lambdabar_C")
print(f"   L0 = {a0inv/2:.3f} PSR (r > lambdabar_C)")
print("\n   r / lambdabar_C     1/alpha (e only)   L (PSR)")
for x in [1, 1e-1, 1e-2, 1e-3, (me/mmu)]:
    ai = a0inv - k*np.log(1/x)
    print(f"   {x:14.3e}   {ai:14.3f}   {ai/2:8.3f}")

print("\nleptons only, to the Z (the hadronic part is taken from data in QED, not from this formula):")
ai = a0inv - k*(np.log(MZ/me) + np.log(MZ/mmu) + np.log(MZ/mtau))
print(f"   1/alpha(M_Z) leptonic leading log = {ai:.2f}  (measured, all species, MS-bar: ~127.95)")
print(f"   L(M_Z) = {ai/2:.2f} PSR from leptons; {127.95/2:.2f} PSR with the measured value")

print("\nonset: QED's electron running starts at r ~ lambdabar_C;  c04's cloud radius r_th = lambdabar_C/2, diameter lambdabar_C.")
print("   So the swing must start shortening where the probe enters the electron's polarisation cloud, and shorten")
print(f"   by PSR/(3 pi) = {1/(3*np.pi):.4f} PSR per e-fold deeper.  That is the law the DP-arc stress model must reproduce.")
