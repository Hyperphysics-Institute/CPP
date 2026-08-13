#!/usr/bin/env python
"""Patch 3098 -- D-DS-RELIC: the expansion-history route for d_s.

Three forward computations, no adoption of any branch:

  (A) EXIT-ANCHOR MAPPING. Kinematic spine: at the EU-1 graceful exit
      the occupancy reaches n-bar = 1 (one CP per FINE GP; 0750/0751
      mu -> 0 at n* = 1); comoving dilution thereafter gives
      d(t) = 1 fine-GP x a(t)/a_exit. With l_P = N_fine ~ 1e30 fine
      GPs (0736 nested resolution) and a0/a_exit ~ T_exit/T0
      (thermal, g_* caveat ~ factor 3 across the full history):
          d_s(today)/l_P = (T_exit/T0) / N_fine.
      Tabulated over T_exit; the INVERSE mapping (which T_exit puts
      d_s in the campaign's working decade) also tabulated. No value
      adopted -- T_exit is the named EU-1 reheat debt (0738).

  (B) DYNAMICAL ADJUDICATION (0723-precedent class -- w(z) SHAPE,
      not magnitude). Fiducial background: flat LCDM, Om = 0.315,
      h = 0.674 (confrontation target, not a fit). R_h(a) = future
      event horizon. Two branches of the relic reading:
        COMOVING-d :  rho_L ~ 1/(a^2 R_h^2)
                      w_eff = -1 + (2/3)(1 + dlnR_h/dlna)
        FROZEN-d   :  rho_L ~ 1/R_h^2   (the Li form, 0723)
                      w_eff = -1 + (2/3)(dlnR_h/dlna)
      w_eff(z) tabulated for both. The comoving branch's w_eff(0)
      sits at the zero-acceleration boundary class (-1/3); the
      frozen branch reproduces the adjudicated w_now ~ -1.02.

  (C) FREEZE-EPOCH CONSISTENCY. If the weave freezes at the fidelity
      boundary d* (Stage-2/3 bracket 6-7 l_P), the comoving history
      reaches d* at 1 + z_f = d_s(comoving, today)/d*. Tabulated over
      T_exit x d*.

Anti-extraction: NO rho_Lambda value is computed anywhere below; the
only confrontation is the equation-of-state SHAPE, per the D3/0723
precedent (Hubble radius excluded on no-acceleration grounds).
"""
import numpy as np

# ---------- constants / fiducial background -------------------------
T0_K   = 2.725
K_PER_GEV = 1.16045e13
N_FINE = 1.0e30            # fine GPs per l_P (0736; c01 ~10^30)
OM, H0 = 0.315, 0.674      # fiducial flat LCDM (confrontation target)
E = lambda a: np.sqrt(OM * a**-3 + (1.0 - OM))

# ---------- (A) exit-anchor mapping ---------------------------------
print("(A) exit-anchor mapping  d_s(today)/l_P = (T_exit/T0)/N_fine")
print("    [g_* caveat: entropy-conserving a ~ 1/T used bare; full-history")
print("     g_* drift is a ~x3 systematic, recorded not resolved]")
for name, T_gev in [("T_Planck  1.22e19 GeV", 1.22e19),
                    ("          3.0e18 GeV",  3.0e18),
                    ("          1.0e18 GeV",  1.0e18),
                    ("GUT       1.0e16 GeV",  1.0e16),
                    ("          1.0e13 GeV",  1.0e13),
                    ("          1.0e10 GeV",  1.0e10)]:
    ratio = (T_gev * K_PER_GEV) / T0_K
    ds = ratio / N_FINE
    print(f"      {name}:  a0/a_exit = {ratio:.2e}  ->  d_s = {ds:9.3g} l_P")
print("    INVERSE: campaign working decade d_s in [6, 16] l_P  <->")
for ds in (6.0, 8.0, 12.0, 16.0):
    T_gev = ds * N_FINE * T0_K / K_PER_GEV
    print(f"      d_s = {ds:4.0f} l_P  <->  T_exit = {T_gev:.2e} GeV")

# ---------- (B) w_eff(z) adjudication -------------------------------
# EXACT DISPLACEMENT THEOREM (background-independent):
#   rho_comoving = rho_frozen / a^2  =>  w_comoving(z) = w_frozen(z) + 2/3.
# FROZEN branch = the adjudicated self-consistent Li form (0723):
#   dOmega/dx = Omega(1-Omega)(1 + 2 sqrt(Omega)/c_Li), x = ln a,
#   w = -1/3 - (2/3) sqrt(Omega)/c_Li,  c_Li = 0.8 (the 0723 coefficient),
#   Omega(today) = 0.685 (fiducial confrontation target, not a fit).
c_Li, Om0 = 0.8, 0.685
xs = np.linspace(0.0, -np.log(1.0 + 8.0), 8001)
Om = np.empty_like(xs); Om[0] = Om0
f = lambda O: O * (1.0 - O) * (1.0 + 2.0 * np.sqrt(O) / c_Li)
for i in range(1, len(xs)):
    h = xs[i] - xs[i - 1]
    k1 = f(Om[i-1]); k2 = f(Om[i-1] + h*k1/2)
    k3 = f(Om[i-1] + h*k2/2); k4 = f(Om[i-1] + h*k3)
    Om[i] = Om[i-1] + h * (k1 + 2*k2 + 2*k3 + k4) / 6.0
w_fro = lambda O: -1.0/3.0 - (2.0/3.0) * np.sqrt(O) / c_Li
print("\n(B) w_eff(z): self-consistent Li frozen branch + exact +2/3 displacement")
print("      z    Omega_L    w_eff[FROZEN-d]   w_eff[COMOVING-d]")
for z in (0.0, 0.5, 1.0, 2.0, 5.0):
    O = np.interp(-np.log(1.0 + z), xs[::-1], Om[::-1])
    print(f"    {z:4.1f}   {O:.3f}      {w_fro(O):+.4f}           {w_fro(O)+2.0/3.0:+.4f}")
w0f = w_fro(Om0); w0c = w0f + 2.0/3.0
assert abs(w0f - (-1.02)) < 0.02, "frozen branch failed to reproduce the 0723 w_now"
assert w0c > -0.40, "displacement arithmetic broken"
print(f"    FROZEN reproduces the adjudicated form: w_now = {w0f:+.4f} (0723: -1.02).")
print(f"    COMOVING is displaced by exactly +2/3: w_now = {w0c:+.4f} vs the")
print("    observed w0 = -1.03 +/- 0.03 -- a many-sigma SHAPE displacement,")
print("    sitting at the zero-acceleration class (-1/3). ADJUDICATION")
print("    (0723-precedent, shape not magnitude): the COMOVING branch is")
print("    dynamically EXCLUDED; the full-shape fit (F2 channel) is the")
print("    formal confrontation if ever contested.")

# ---------- (C) freeze-epoch consistency ----------------------------
print("\n(C) freeze-epoch: 1 + z_f = d_s(comoving, today)/d*")
for T_gev in (1.22e19, 3.0e18, 1.0e18):
    ds_com = (T_gev * K_PER_GEV) / T0_K / N_FINE
    row = "  ".join(f"d*={dstar:.0f}: z_f={ds_com/dstar - 1.0:+7.2f}"
                    for dstar in (6.0, 7.0))
    print(f"      T_exit = {T_gev:.2e} GeV (d_s_com = {ds_com:6.1f} l_P):  {row}")
print("      [negative z_f = the comoving history has NOT yet reached d* --")
print("       under that exit anchor a boundary-freeze lies in the future]")

print("\nAll gates PASS. No rho_Lambda computed; no branch adopted;")
print("T_exit remains the named EU-1 debt; the founder rules FQ-7.")
