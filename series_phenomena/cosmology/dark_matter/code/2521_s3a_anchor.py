#!/usr/bin/env python3
"""Patch 2521 verify: S3a anchor arithmetic. No mechanism computation."""
import math

phi = (1 + math.sqrt(5)) / 2
chi = phi ** -3
assert abs(chi - 0.2361) < 1e-4
assert abs(chi / 6 - 0.03934) < 1e-5           # registered Delta_p_LR = chi/6 ~ 0.0394
print(f"chi = phi^-3 = {chi:.4f}; Delta_p_LR = chi/6 = {chi/6:.5f} (registered 0.0394) OK")

eta_B, s_eta = 6.12e-10, 0.04e-10               # registered (Planck 2018, PRED-O-25 anchor)
Uq, s_Uq = 3 * eta_B, 3 * s_eta
Ue, s_Ue = 2 * eta_B, 2 * s_eta
print(f"U_q/n_gamma = 3 eta_B = ({Uq*1e9:.3f} +/- {s_Uq*1e9:.3f}) x 10^-9")
print(f"U_e/n_gamma = 2 eta_B = ({Ue*1e9:.3f} +/- {s_Ue*1e9:.3f}) x 10^-9")

T1, sT1 = 0.4468, 0.0054
target = T1 * eta_B
s_target = target * math.sqrt((sT1/T1)**2 + (s_eta/eta_B)**2)
print(f"transposed S3b target: n_ring/n_gamma = T1*eta_B = ({target*1e10:.3f} +/- {s_target*1e10:.3f}) x 10^-10")
assert abs(target - 2.734e-10) < 1e-12 * 1e2

# eta_B-scale ledger of asymmetry-forced populations (per photon)
ledger = {"baryons": eta_B, "clouds (closure-forced)": 1*eta_B, "hDP-B excess (closure-forced)": 2*eta_B,
          "rings (target)": target}
for k, v in ledger.items():
    print(f"  {k}: {v/eta_B:.4f} eta_B")
print("all asymmetry-forced populations are eta_B-scale -> S3b-D1 direction well-posed (not adopted)")
print("ALL CHECKS PASS")
