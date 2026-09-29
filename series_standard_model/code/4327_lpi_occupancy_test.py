#!/usr/bin/env python3
"""4327 -- founder (founders_voice/4327): DP-arc CPs move because of SSV_net (V_i); the SCALE of their movement is set by
SSV_abs.  So the swing L scales with the local PSR, and L/PSR is SSV_abs-invariant: T2's swing condition (4326) holds.

Pressed to the end: alpha = c * PSR / (2L) (4324) also contains the landing occupancy c = N / (GPs of the landing shell).
In a gravitational well SR-1's PSR_eff = l_P/(1 + kappa), kappa = k dSSV > 0, and c07 (light slows in a well) needs the
DI-bit landing radius to shrink with it: R_eff = R0/(1+kappa).  AP-4 as the founder stated it at 4311: every GP emits the
same N regardless of the field.  Then c = N/(4 pi R_eff^2) = c0 (1+kappa)^2, and alpha rises with it.
The weak-field map: kappa ~ -d(U/c^2) (deeper well, U more negative, kappa larger).  k_alpha: d alpha/alpha = k_alpha d(U/c^2)."""
import numpy as np
kmax = 5.5e-7 + 2*5.2e-7          # Leefer et al. 2013, 2-sigma

def alpha_ratio(kappa, rule):
    c0 = 1.0                       # full covering at the baseline
    c = c0*(1+kappa)**2            # fixed N, shrunk shell (AP-4 + c07)
    PSR_over_L = 1.0               # founder 4327: L scales with the PSR
    if rule == "additive (sum of all DI-bits)":
        ceff = c
    elif rule == "per-source once (origin address, AP-4 payload)":
        ceff = min(c, 1.0)
    elif rule == "N scales with shell GPs (contra 4311)":
        ceff = c0
    return ceff*PSR_over_L/c0

dU = -1e-9                         # a slightly deeper potential
kappa = -dU
print(f"{'counting rule at the landing GP':52s} {'k_alpha':>10s}   vs |k_alpha| < {kmax:.1e}")
for rule in ["additive (sum of all DI-bits)", "per-source once (origin address, AP-4 payload)",
             "N scales with shell GPs (contra 4311)"]:
    k = (alpha_ratio(kappa, rule) - 1)/dU
    verdict = "EXCLUDED by ~%.0e" % (abs(k)/kmax) if abs(k) > kmax else "allowed"
    print(f"{rule:52s} {k:10.3f}   {verdict}")
print("\nThe swing passes T2 (founder 4327).  The OCCUPANCY fails it at O(1) unless the landing GP counts each source")
print("once per Moment, or unless per-GP emission rises in a well (which the founder ruled out at 4311).")
print("Per-source-once pins c = 1 wherever the baseline is at full covering and every site is at least as stressed;")
print("then alpha = PSR/(2L) exactly, everywhere: the swing is the whole of alpha.")
print("It needs the baseline (least-stressed region anywhere) to sit at full covering: a site LESS stressed than the")
print("baseline would have c < 1 and a smaller alpha.")
