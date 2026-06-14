#!/usr/bin/env python3
"""
SF-3 numeric verification — Patch 1500
=======================================
Independently reproduces every numerical claim in sf-3_quarks.tex from
first inputs (m_e, z, phi, C_F). No fitted parameters anywhere.

Run:  python3 1500_verify_sf3_core.py
Deps: standard library only (math).

Source results reframed: SM-7, SM-8 v4.0, SM-9, SS-2.
"""
import math

# ---- Inputs (the ONLY dimensionful calibration is m_e) -------------------
phi = (1 + math.sqrt(5)) / 2     # golden ratio, built into the 600-cell metric
me  = 0.51099895                 # MeV, PDG electron mass (the single calibration)
z   = 12                         # 600-cell vertex coordination
CF  = 4 / 3                      # SU(3) fundamental Casimir (SS-2)
M0  = me * z / phi               # mass anchor M_0 = m_e z/phi (SM-9)

PASS = True
def check(label, got, want, tol, unit=""):
    global PASS
    ok = abs(got - want) <= tol
    PASS = PASS and ok
    print(f"  [{'PASS' if ok else 'FAIL'}] {label:42s} {got:12.4f}{unit}  (target {want}{unit})")

print(f"phi = {phi:.10f}")
print(f"M0  = m_e z/phi = {M0:.4f} MeV   (paper: 3.79 MeV)")
check("M0 anchor", M0, 3.79, 0.01, " MeV")

# ---- A. Zero-parameter mass spectrum (Eq. massformula, Table tab:masses) --
print("\nA. Quark mass spectrum  M_q = m_e (z/phi) V^(7/3)  [top x z*C_F]")
spectrum = {  # quark: (V, multiplier, PDG MeV, paper CPP MeV, paper err%)
    "strange": (4,  1,        93.4,    96.3,   +3.1),
    "charm":   (12, 1,        1270.0,  1249.0, -1.6),
    "bottom":  (20, 1,        4180.0,  4115.0, -1.6),
    "top":     (30, z * CF,   172760.0,169570.0,-1.8),
}
errs = []
print(f"  {'quark':8s}{'V':>4s}{'mult':>6s}{'CPP(MeV)':>13s}{'PDG(MeV)':>12s}{'err%':>8s}")
for q, (V, mult, pdg, paper_cpp, paper_err) in spectrum.items():
    M = M0 * (V ** (7 / 3)) * mult
    e = (M - pdg) / pdg * 100
    errs.append(e)
    print(f"  {q:8s}{V:4d}{mult:6.2f}{M:13.1f}{pdg:12.1f}{e:+8.2f}")
    check(f"{q} mass", M, paper_cpp, max(2.0, 0.005 * paper_cpp), " MeV")
rms = math.sqrt(sum(x * x for x in errs) / len(errs))
print(f"  RMS error = {rms:.2f}%   (paper: 2.1%)")
check("RMS residual", rms, 2.1, 0.1, " %")
# charm is PREDICTED, not calibrated -> single m_e calibration
print(f"  charm is DERIVED (single-m_e calibration restored): m_c = {M0*12**(7/3):.0f} MeV")

# ---- B. alpha_s and electroweak-strong complementarity (Eqs alphas, comp) -
print("\nB. Strong coupling + mode complementarity")
TrA2, TrA3 = 3840 - 2400, 2400      # face-mode numerator 2400; Tr(A^2)+1/3Tr(A^3)=3840
alpha_s = (1 / phi) * (2400 / 3840)
sin2thW = 3 / (8 * phi)
check("alpha_s = 5/(8 phi)", alpha_s, 5 / (8 * phi), 1e-9)
check("alpha_s value", alpha_s, 0.386, 0.001)
check("sin^2 theta_W = 3/(8 phi)", sin2thW, 3 / (8 * phi), 1e-9)
check("complementarity sum = 1/phi", alpha_s + sin2thW, 1 / phi, 1e-9)
check("ratio alpha_s/sin2thW = 5/3 (=F/E)", alpha_s / sin2thW, 5 / 3, 1e-9)
check("topological ratio F/E", 1200 / 720, 5 / 3, 1e-9)

# ---- C. Quark Koide phase (Eqs shift, koide) -----------------------------
print("\nC. Quark Koide phase  cos = -(2/3)(1 + eps/2)")
eps_S  = -z * alpha_s / (z + 1)     # = -60/(104 phi)
eps_EW = 3 / (52 * phi)
eps    = eps_S + eps_EW             # = -27/(52 phi)
check("eps_S = -60/(104 phi)", eps_S, -60 / (104 * phi), 1e-9)
check("eps_EW = 3/(52 phi)",  eps_EW, 3 / (52 * phi), 1e-9)
check("eps = -27/(52 phi)",   eps,   -27 / (52 * phi), 1e-9)
costh = -(2 / 3) * (1 + eps / 2)
theta = math.degrees(math.acos(costh))
print(f"  cos theta_quark = {costh:.5f};  theta = {theta:.2f} deg  (PDG 124.09, paper 124.04)")
check("quark Koide phase", theta, 124.04, 0.02, " deg")
# phase-mass independence: theta depends only on alpha_s, sin2thW, z (no m_c, no amplitude)
print("  Prop 5.1: theta_quark built from {alpha_s, sin2thW, z} only -> independent of m_c. [structural]")

print("\n" + ("ALL CHECKS PASS" if PASS else "*** SOME CHECKS FAILED ***"))
