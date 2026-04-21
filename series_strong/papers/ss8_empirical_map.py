#!/usr/bin/env python3
# ============================================================
# SS-8 Phase 1: Alpha-chain empirical map
# Purpose: extend SS-7 Table 1 across the full N=Z alpha-chain
#          and compare with the paper's choice of non-N=Z nuclei
# Author: Claude Opus, 21 April 2026
# ============================================================

# SS-7 formula: B(N_alpha) = N_alpha * B_alpha + (3*N_alpha - 6) * B_pair
B_alpha = 28.296  # MeV, from 4He binding (SS-5)
B_pair  = 2.342   # MeV, nucleon-pair binding quantum M0/phi (SS-5)

def ss7_pred(N):
    return N * B_alpha + (3*N - 6) * B_pair

# AME 2020 binding energies (MeV, total)
# Strict N=Z alpha-chain (N_alpha = A/4, A = 4*N_alpha, Z = N = 2*N_alpha)
# High confidence for N_alpha <= 14; moderate for 15-16; lower above that.
alpha_chain_NZ = {
    3:  ("12C",   92.162),
    4:  ("16O",  127.619),
    5:  ("20Ne", 160.645),
    6:  ("24Mg", 198.257),
    7:  ("28Si", 236.537),
    8:  ("32S",  271.781),
    9:  ("36Ar", 306.716),
    10: ("40Ca", 342.052),
    11: ("44Ti", 375.475),
    12: ("48Cr", 411.462),
    13: ("52Fe", 447.696),
    14: ("56Ni", 483.990),
    15: ("60Zn", 514.992),   # less-precise AME value; check before publication
    16: ("64Ge", 545.955),   # ditto
}

# Paper's Table 1 choice for N_alpha >= 12: non-N=Z, more abundant isotopes
paper_choice = {
    12: ("48Ti", 418.699),   # Z=22, N=26 (N-Z = +4)
    13: ("52Cr", 456.349),   # Z=24, N=28 (N-Z = +4)
    14: ("56Fe", 492.254),   # Z=26, N=30 (N-Z = +4)
}

print("=" * 84)
print("STRICT N=Z ALPHA-CHAIN (Z = N = 2*N_alpha, A = 4*N_alpha)")
print("=" * 84)
print(f"{'N_a':>4} {'Nuclide':>8} {'B_exp (MeV)':>13} {'B_pred (MeV)':>14} {'Residual %':>12} {'Note':>14}")
print("-" * 84)
residuals_NZ = []
for Na in sorted(alpha_chain_NZ.keys()):
    name, B_exp = alpha_chain_NZ[Na]
    B_pred = ss7_pred(Na)
    res = (B_exp - B_pred) / B_exp * 100  # + means exp > pred (underbinding by formula)
    note = ""
    if Na == 5:
        note = "(known 20Ne outlier)"
    if Na >= 15:
        note = "(check AME)"
    residuals_NZ.append((Na, res))
    print(f"{Na:>4} {name:>8} {B_exp:>13.3f} {B_pred:>14.3f} {res:>+11.2f}% {note:>14}")

print()
rms_primary = (sum(r**2 for Na, r in residuals_NZ if 3 <= Na <= 10) / 8) ** 0.5
rms_extended_14 = (sum(r**2 for Na, r in residuals_NZ if 3 <= Na <= 14) / 12) ** 0.5
rms_highNa = (sum(r**2 for Na, r in residuals_NZ if 11 <= Na <= 14) / 4) ** 0.5
print(f"RMS residual, primary set (N_a = 3-10):     {rms_primary:.2f}%")
print(f"RMS residual, extended (N_a = 3-14):        {rms_extended_14:.2f}%")
print(f"RMS residual, high-N_a set (N_a = 11-14):   {rms_highNa:.2f}%")

print()
print("=" * 84)
print("PAPER'S TABLE 1 CHOICE FOR N_a >= 12 (non-N=Z: +4 neutrons each)")
print("=" * 84)
print(f"{'N_a':>4} {'Nuclide':>8} {'B_exp (MeV)':>13} {'B_pred (MeV)':>14} {'Residual %':>12} {'N-Z':>6}")
print("-" * 84)
for Na in sorted(paper_choice.keys()):
    name, B_exp = paper_choice[Na]
    B_pred = ss7_pred(Na)
    res = (B_exp - B_pred) / B_exp * 100
    # Work out N-Z from the nuclide label (crude parse)
    if name == "48Ti": NmZ = 4
    elif name == "52Cr": NmZ = 4
    elif name == "56Fe": NmZ = 4
    print(f"{Na:>4} {name:>8} {B_exp:>13.3f} {B_pred:>14.3f} {res:>+11.2f}% {NmZ:>+6}")

print()
print("=" * 84)
print("HEAD-TO-HEAD AT N_a = 12, 13, 14")
print("=" * 84)
for Na in (12, 13, 14):
    nz_name, nz_B = alpha_chain_NZ[Na]
    pr_name, pr_B = paper_choice[Na]
    nz_res = (nz_B - ss7_pred(Na)) / nz_B * 100
    pr_res = (pr_B - ss7_pred(Na)) / pr_B * 100
    diff = pr_B - nz_B
    print(f"N_a={Na}: N=Z isotope {nz_name} residual {nz_res:+.2f}%  "
          f"|  paper's {pr_name} residual {pr_res:+.2f}%  "
          f"|  extra binding from +4 neutrons: {diff:+.2f} MeV")
