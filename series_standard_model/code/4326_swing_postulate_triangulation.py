#!/usr/bin/env python3
"""4326 -- the ZBW1 swing registered as a calibrated postulate (founder, 4326) and its triangulation legs.

CAL-ZBW1-SWING: at full covering in a quiet sea, the Planck-level ZBW swings L0 = PSR/(2 alpha0) apogee to apogee
(4325), alpha0 = alpha at zero momentum transfer.  Founder 4326: the CP never reaches light speed, even at the centre.

T1 (running): 4325 sec 7 (founder 4301: more stress, more energy per displacement) -> the swing shortens where the
    sea is more stressed by charge (SSV_net).  alpha = PSR/(2L) at full covering, so L/L0 = alpha0/alpha(Q).
T2 (local position invariance): the same alpha must hold at different gravitational potentials (SSV_abs).
    Atomic-dysprosium bound (Leefer et al. 2013): k_alpha = (-5.5 +- 5.2)e-7, with d(alpha)/alpha = k_alpha d(U/c^2)."""
import numpy as np
alpha0_inv = 137.035999084
alphaZ_inv = 127.95          # alpha at the Z mass (MS-bar, textbook/PDG value ~127.95)

print("CAL-ZBW1-SWING")
print(f"   L0 = PSR/(2 alpha0) = {alpha0_inv/2:.3f} PSR (quiet sea, full covering; an upper bound under stress, 4325)")
print("   founder 4326: V_i < c even at the centre  ->  Moments per cycle > 2 L0/PSR = 137.04 strictly")

print("\nT1 running: alpha grows at short distance; in the swing picture the swing shortens")
r = alphaZ_inv/alpha0_inv
print(f"   1/alpha: {alpha0_inv:.3f} (Q -> 0)  ->  {alphaZ_inv:.2f} (Q = M_Z)")
print(f"   L(M_Z)/L0 = alpha0/alpha(M_Z) = {r:.4f}: the swing must be {100*(1-r):.1f}% shorter at the Z scale")
print("   Sign: charge stress shortens the swing (founder 4301 rule) -> alpha grows -> SAME SIGN as the measured running.")
print("   Shape: QED's running is logarithmic in Q (leading log: 1/alpha(Q) = 1/alpha0 - (2/(3 pi)) sum_f N_c Q_f^2 ln(Q/m_f));")
print("   the stress law for L must reproduce that logarithm to count as a triangulation, not a sign.")

print("\nT2 local position invariance (gravity = SSV_abs)")
kmax = 5.5e-7 + 2*5.2e-7
for label, dU in [("Sun, annual (eccentricity), Earth", 3.3e-10), ("Earth surface vs infinity", 7.0e-10),
                  ("Sun at 1 AU vs infinity", 9.9e-9)]:
    print(f"   {label:34s} d(U/c^2) = {dU:.1e}: |d alpha/alpha| < {kmax*dU:.1e}  -> |dL/L| (relative to PSR) < {kmax*dU:.1e}")
print("   So gravitational stress must rescale L and PSR TOGETHER (L/PSR invariant to ~1e-6 of d(U/c^2)),")
print("   while charge stress must shorten L relative to PSR (T1). This is the founder's SSV_abs / SSV_net split (4318),")
print("   and it is 0739's 'gravity channel symmetric' (k_alpha = A_grav < 1e-6) restated for the swing.")
