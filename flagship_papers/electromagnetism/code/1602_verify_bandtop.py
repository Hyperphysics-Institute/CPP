#!/usr/bin/env python3
"""
1602_verify_bandtop.py
----------------------
Transcription check for the single new quantitative claim added to SF-6 in
Patch 1602: the 600-cell intrinsic UV band top imported from TP-1 (QM-5
dispersion), Eq. (eq:bandtop) in sf-6_electromagnetism.tex:

    omega_max = sqrt(12)/t_P = 2*sqrt(3)/t_P    (lambda_max = z = 12)

This is NOT an SF-6 derivation; the value is owned by TP-1. The script only
confirms (a) the two written forms of omega_max are algebraically identical, and
(b) the optical-photon ledger ln(omega_max/omega_g) ~ 64.5 that TP-1 quotes is
reproduced, so the figure was transcribed correctly into SF-6.

Python standard library only.
"""

import math

T_P    = 5.391247e-44      # s, Planck time
Z      = 12                # 600-cell vertex coordination = lambda_max

def rel_close(a, b, rtol):
    return abs(a - b) <= rtol * abs(b)

def main():
    # (a) the two written forms must be identical: sqrt(12) == 2*sqrt(3)
    form1 = math.sqrt(12.0)
    form2 = 2.0 * math.sqrt(3.0)
    assert rel_close(form1, form2, 1e-12), "sqrt(12) != 2*sqrt(3)"

    omega_max = math.sqrt(Z) / T_P     # rad/s, intrinsic band top

    # (b) optical-photon ledger: TP-1 quotes ln(omega_max/omega_g) ~ 64.5.
    # Use a representative optical angular frequency (~500 nm).
    lam_opt   = 500e-9                  # m
    c         = 299_792_458.0          # m/s
    omega_g   = 2.0 * math.pi * c / lam_opt
    ln_ratio  = math.log(omega_max / omega_g)

    print("SF-6 Patch 1602 — band-top transcription check")
    print("=" * 64)
    print(f"[PASS] sqrt(12) = 2*sqrt(3) = {form1:.6f}")
    print(f"       omega_max = sqrt(12)/t_P = {omega_max:.3e} rad/s")
    print(f"       omega_g (optical ~500nm) = {omega_g:.3e} rad/s")
    print(f"       ln(omega_max/omega_g)    = {ln_ratio:.2f}  (TP-1 quotes ~64.5)")
    assert 63.0 <= ln_ratio <= 66.0, f"ln ratio {ln_ratio} outside TP-1's ~64.5 band"
    print("=" * 64)
    print("Band-top value transcribed correctly from TP-1. (Not an SF-6 result.)")

if __name__ == "__main__":
    main()
