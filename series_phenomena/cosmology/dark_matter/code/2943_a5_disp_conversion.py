#!/usr/bin/env python3
# =====================================================================
# Patch 2943 -- A5-DISP CONVERSION VERIFY SCRIPT (stdlib only, CONV-003)
# =====================================================================
# Mechanical application of the FROZEN rules of Patch 2942
# (a5_disp_conversion_prereg.md). No judgment calls.
#
# BINDING SOURCE (peer-reviewed, admissible per prereg s4):
#   T. Piran & D. D. Ofengeim, Phys. Rev. D 109, L081501 (2024),
#   "Lorentz invariance violation limits from GRB 221009A"
#   (LHAASO TeV afterglow, time-of-flight, n=2 photon sector):
#     E_QG,2 >= 5.8e-8 E_Pl  (subluminal)
#     E_QG,2 >= 4.6e-8 E_Pl  (superluminal)
#
# FROZEN RULES APPLIED:
#   prereg s1: d_DP <= (hbar c / E_lim) * xi_2^(-1/2)
#   prereg s2: numeric ceiling quoted at xi_2 = 1 reference
#   prereg s3: BINDING = weaker of the two signs (superluminal here)
#   prereg s4: TOF-class, quadratic, peer-reviewed binding source
# =====================================================================
HBARC_MEV_FM = 197.3269804          # PDG
E_PL_GEV     = 1.220890e19          # PDG Planck energy

lims = {  # sign : coefficient of E_Pl
    "subluminal":   5.8e-8,
    "superluminal": 4.6e-8,
}
res = {}
for sign, coef in lims.items():
    E_lim_GeV = coef * E_PL_GEV
    E_lim_MeV = E_lim_GeV * 1e3
    d_fm = HBARC_MEV_FM / E_lim_MeV          # at xi_2 = 1
    res[sign] = (E_lim_GeV, d_fm)
    print(f"{sign:12s}: E_QG,2 >= {E_lim_GeV:.3e} GeV  "
          f"=> d_DP <= {d_fm:.3e} fm = {d_fm*1e-15:.3e} m  (xi_2 = 1)")

binding = min(res, key=lambda s: res[s][0])   # weaker limit binds
E_b, d_b = res[binding]
assert binding == "superluminal"
print()
print(f"BINDING CEILING (weaker sign = {binding}, per frozen prereg s3):")
print(f"  d_DP <= {d_b:.3e} fm * xi_2^(-1/2)")
print(f"       = {d_b*1e-15:.3e} m * xi_2^(-1/2)")
print(f"  (= {d_b*1e-15/1.616255e-35:.2e} Planck lengths at xi_2 = 1)")
print()
print("Secondary corroboration (venue unverified; NOT binding; would")
print("tighten by <= ~1.6x if admitted via the s4 substitution path):")
print("  max-likelihood 12.0 (7.2) x 10^11 GeV; DisCan 13.7 (12.5) x 10^11 GeV")
print()
print("PANEL-PENDING per Patch 2941: void if combined review overturns CASE-Q.")
