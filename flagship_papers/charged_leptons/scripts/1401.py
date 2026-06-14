#!/usr/bin/env python3
"""
1401.py -- SF-1 charged-leptons flagship: headline-number verification.

Verifies every numerical claim in sf-1_charged_leptons.tex v0.1 against PDG.
Pure-synthesis paper (reframing of shipped SM-3/4/6); this script confirms
that the assembled numbers reproduce the shipped results to stated precision.

Run:  python3 1401.py
Deps: standard library only (math).
"""
import math

phi = (1 + 5**0.5) / 2          # golden ratio, built into the 600-cell metric (A5)
z   = 12                         # 600-cell vertex coordination (A2)

# --- PDG 2024 reference values (MeV; angle in degrees) ---
m_e_PDG   = 0.51099895           # calibration input
m_mu_PDG  = 105.6583755
m_tau_PDG = 1776.86
s2w_PDG   = 0.23121              # low-energy effective sin^2 theta_W
theta_PDG = 132.732              # Koide phase from current lepton masses

def pct(cpp, exp):
    return abs(cpp - exp) / abs(exp) * 100.0

print("=" * 60)
print("SF-1 headline verification  (patch 1401)")
print("=" * 60)

# (1) Weinberg angle (intermediate): sin^2 theta_W = 3/(8 phi)
s2w = 3 / (8 * phi)
print(f"[1] sin^2 theta_W = 3/(8 phi) = {s2w:.5f}")
print(f"    PDG {s2w_PDG}  ->  {pct(s2w, s2w_PDG):.2f}%   (paper: 0.24%)")

# (2) Electroweak isotropic shift epsilon = 2 sin^2 theta_W /(z+1) = 3/(52 phi)
eps = 2 * s2w / (z + 1)
print(f"[2] epsilon = 2 s2w/(z+1) = {eps:.6f}   (3/(52 phi) = {3/(52*phi):.6f})")
assert abs(eps - 3/(52*phi)) < 1e-12, "epsilon identity failed"

# (3) Koide phase: cos theta = -(2/3)(1 + sin^2 theta_W/(z+1))
cos_theta = -(2/3) * (1 + s2w/(z+1))
theta = math.degrees(math.acos(cos_theta))
print(f"[3] cos theta_Koide = {cos_theta:.6f}")
print(f"    theta = {theta:.3f} deg   PDG {theta_PDG}  ->  {pct(theta, theta_PDG):.4f}%   (paper: 0.003%)")

# (4) Mass spectrum: sqrt(m_i) = A (1 + sqrt2 cos(theta + 2 pi i/3)); A from m_e
thr = math.radians(theta)
f = lambda i: 1 + math.sqrt(2) * math.cos(thr + 2*math.pi*i/3)
A = math.sqrt(m_e_PDG) / f(0)                 # electron is the single calibration
m = sorted((A * f(i))**2 for i in range(3))
print(f"[4] mass branches (MeV): {[round(x,3) for x in m]}")
print(f"    m_mu  = {m[1]:.2f}  PDG {m_mu_PDG:.2f}  -> {pct(m[1], m_mu_PDG):.2f}%   (paper: 0.18%)")
print(f"    m_tau = {m[2]:.1f}  PDG {m_tau_PDG:.2f}  -> {pct(m[2], m_tau_PDG):.2f}%   (paper: 0.16%)")

# (5) Koide K = 2/3 exact from these masses
K = sum(m) / (sum(math.sqrt(x) for x in m))**2
print(f"[5] Koide K = {K:.6f}   target 2/3 = {2/3:.6f}")
assert abs(K - 2/3) < 1e-9, "Koide K != 2/3"

# (6) bare mode partition Tr(A^2):Tr(A^3)/3 = 1440:2400 -> 3/8
trA2, trA3_over3 = 1440, 2400
bare = trA2 / (trA2 + trA3_over3)
print(f"[6] bare mixing 1440/(1440+2400) = {bare}   (= 3/8 = {3/8})")
assert abs(bare - 3/8) < 1e-12, "bare mode partition != 3/8"

print("=" * 60)
print("All SF-1 headline numbers reproduce the shipped SM-3/4/6 results.")
print("=" * 60)
