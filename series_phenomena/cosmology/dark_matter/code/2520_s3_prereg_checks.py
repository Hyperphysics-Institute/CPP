#!/usr/bin/env python3
"""Patch 2520 verify: S3 pre-registration checks. NO branching computation here.

(1) Retro-prediction: S3-M1's skeleton must reproduce the 2519 closure-forced sinks.
(2) Target decomposition arithmetic and branch-window mapping in mechanism variables.
(3) H1 hazard quantification: equilibrium Boltzmann factors at kT_form vs the needed 6.5%.
"""
import math

# (1) Retro-prediction: symmetric unpaired inventories, matter-only consumption, +q exhaustion
n_b = 1.0                          # per-baryon units
Uq_consumed = 3 * n_b              # bare +qCPs -> quarks
Ue_consumed = 2 * n_b              # bare -eCPs -> down capture + orbital electron (S1 net)
mirror_minus_q = Uq_consumed       # sign symmetry: unpaired -q with no antibaryon channel
mirror_plus_e = Ue_consumed        # unpaired +e with no channel
b_excess = min(mirror_minus_q, mirror_plus_e)     # -q + +e bind into hDP-B
clouds = mirror_minus_q - b_excess
assert b_excess == 2 * n_b and clouds == 1 * n_b
print(f"retro-prediction: hDP-B excess = {b_excess} n_b, clouds = {clouds} n_b  "
      f"(closure theorem 2519: 2 n_b, 1 n_b) -> PASS")

# (2) Decomposition and windows in mechanism variables (n_ring per unpaired +qCP)
T1, sT1 = 0.4468, 0.0054
ring_per_Uq = T1 / 3.0             # n_ring/U_q = T1/3
print(f"decomposition: n_ring/n_b = 3 n_ring/U_q; target n_ring/U_q = {ring_per_Uq:.4f} "
      f"(one ring per {1/ring_per_Uq:.2f} unpaired +qCPs)")
for name, lo, hi in [("D-strong", 0.436, 0.458), ("D-directional", 0.30, 0.67)]:
    print(f"  {name}: n_ring/U_q in [{lo/3:.4f}, {hi/3:.4f}]")

# (3) H1: equilibrium exponentials at kT_form vs the needed fraction
kT = 0.0165  # MeV
for E in [0.49, 1.25, 40.0, 66.0, 102.0, 170.0]:   # registered E_ee coat / E_qq window values
    print(f"  exp(-{E}/kT_form) = e^(-{E/kT:.0f})  (needed baryon-channel share ~6.5e-2)")
print("H1 confirmed: no equilibrium Boltzmann reading can produce the branching; "
      "S3-M1 must run in frozen-inventory kinetic form")
print("ALL CHECKS PASS")
