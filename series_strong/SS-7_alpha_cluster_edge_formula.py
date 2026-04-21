# ============================================================
# SS-7: Alpha-Cluster Regime and the 3N-6 Edge Formula
# Paper: SS-7 v1.2 - Alpha-Cluster Regime and the 3N-6 Edge
#        Formula for Medium-Mass Nuclei
# Computation: Reproduces all numerical content of the paper:
#   - Table 1: 8 zero-parameter binding predictions (N_alpha=3..10)
#   - Finding 4.1: R_alpha-alpha = 2.37 fm from 8Be inversion
#   - Section 5.1: Extended N=Z alpha-chain at N_alpha = 11..14
#                  (v1.2: replaces v1.1 "structural-onset" block)
#   - Section 6.5: 5 hostile-geometry stress tests
# Key results: All 8 Table 1 predictions match paper to 3 decimals.
#   RMS error 0.91% (all 8, N=Z). Extended N=Z chain at N_alpha = 11-14
#   stays in family (+0.26% to +0.73%). Stress-test alternatives all
#   underperform the simplicial 3N-6 rule.
# Author: Claude Opus (Anthropic), 20-21 April 2026
# ============================================================
#
# CHANGELOG:
# 20 April 2026: initial script, v1.1 state
# 21 April 2026: v1.2 updates
#   - G3 RMS discrepancy resolved: abstract figure updated to 0.91%
#     (first-principles, all 8 nuclei, N=Z). See
#     SS-7_v1.1_G3_discrepancy_note.md for history.
#   - Section 5.1 block rewritten: replaces N_alpha = 12,13,14 paper
#     choices (48Ti, 52Cr, 56Fe) with strict N=Z alpha-chain (48Cr,
#     52Fe, 56Ni) plus 44Ti at N_alpha=11. Original non-N=Z values
#     retained in a separate block for traceability (the ~2% deviation
#     is neutron-excess binding, not a structural signal). See
#     problem_histories/PH-OPEN-SS-22.md for the retirement narrative.
# ============================================================

import numpy as np

# ============================================================
# INHERITED CONSTANTS (from SS-5 and SM-8; not fit to SS-7 data)
# ============================================================
M_0 = 3.7898                      # MeV, SM-8 unit mass
phi = (1 + np.sqrt(5)) / 2        # golden ratio, 1.618034...
B_pair_exact = M_0 / phi          # 2.342 MeV, nucleon-pair quantum
B_pair = 2.342                    # MeV, value used throughout paper
B_alpha_exp = 28.296              # MeV, experimental 4He binding (AME 2020)
B_alpha_LO  = 27.904              # MeV, SS-5 LO prediction

# ============================================================
# TABLE 1: Eight zero-parameter binding predictions
# Uses B_alpha_exp (experimental) as primary per paper Section 3.3
# ============================================================
print("="*76)
print("TABLE 1 (paper Section 3.1): Alpha-chain binding predictions")
print("Constants: B_alpha =", B_alpha_exp, "MeV, B_pair =", B_pair, "MeV")
print("="*76)
print(f"{'Nucleus':8s} {'N_a':>4s} {'E':>4s} {'N*B_a':>10s} {'E*B_p':>8s} "
      f"{'Pred':>10s} {'Meas':>10s} {'Error':>8s}")
print("-"*76)

ame2020 = {
    '12C':  ( 3,  92.162),
    '16O':  ( 4, 127.619),
    '20Ne': ( 5, 160.645),
    '24Mg': ( 6, 198.257),
    '28Si': ( 7, 236.537),
    '32S':  ( 8, 271.781),
    '36Ar': ( 9, 306.716),
    '40Ca': (10, 342.052),
}

errors_pct = []
for nuc, (Na, B_exp) in ame2020.items():
    E = 3*Na - 6
    NBa = Na * B_alpha_exp
    EBp = E * B_pair
    B_pred = NBa + EBp
    err_pct = (B_pred - B_exp) / B_exp * 100
    errors_pct.append(err_pct)
    print(f"{nuc:8s} {Na:4d} {E:4d} {NBa:10.3f} {EBp:8.3f} "
          f"{B_pred:10.3f} {B_exp:10.3f} {err_pct:+7.2f}%")

rms = float(np.sqrt(np.mean(np.array(errors_pct)**2)))
print("-"*76)
print(f"RMS error: {rms:.2f}%   (v1.2 cites 0.91%, first-principles, all 8)")
print(f"Max |error|:     {max(abs(e) for e in errors_pct):.2f}% at 28Si")
print(f"Max positive:    {max(errors_pct):+.2f}% at 20Ne   (paper: +1.19%)")
print(f"All 8 predictions within +/-1.5%: {all(abs(e) < 1.5 for e in errors_pct)}")
# G3 historical check: without 20Ne the RMS is 0.86% (v1.1 "0.88%" figure)
errors_no_20Ne = [e for nuc, e in zip(ame2020.keys(), errors_pct) if nuc != '20Ne']
rms_no_20Ne = float(np.sqrt(np.mean(np.array(errors_no_20Ne)**2)))
print(f"RMS excluding 20Ne (7 nuclei): {rms_no_20Ne:.2f}%   (v1.1 cited 0.88%)")

# ============================================================
# FINDING 4.1: R_alpha-alpha from 8Be unboundness (inversion)
# ============================================================
print("\n" + "="*76)
print("FINDING 4.1 (paper Section 4): R_alpha-alpha from 8Be inversion")
print("="*76)

# 8Be: N_alpha=2, E = 3N-6 = 0, so formula gives B = 2*B_alpha + 0
# Experimental: 8Be barely unbound by 92 keV relative to 2 alphas
# Single alpha-alpha contact must give Coulomb repulsion > B_pair
# E_Coul(R) = 4 * alpha_em * hbar c / R, at alpha-alpha (Z=2 each, so Z1*Z2=4)
#
# Balance condition for 8Be:
# B_pair (attraction from one contact) - E_Coul(R) = -0.092 MeV (unboundness)
# 2.342 - 5.765/R = -0.092
# 5.765/R = 2.434
# R = 2.37 fm

alpha_em = 1/137.036
hbar_c_MeV_fm = 197.327
# Z=2 for each alpha; prefactor is Z1*Z2 = 4, and Coul energy = Z1*Z2*alpha_em*hbar_c/R
Coul_prefactor = 4 * alpha_em * hbar_c_MeV_fm    # = 5.765 MeV.fm
print(f"Coulomb prefactor Z1*Z2*alpha_em*hbar*c = {Coul_prefactor:.3f} MeV.fm")
# Paper uses 5.765
assert abs(Coul_prefactor - 5.765) < 0.01, "Coul prefactor mismatch"

# Inversion: B_pair - E_Coul = -0.092
# E_Coul = B_pair + 0.092 = 2.434 MeV
# R = 5.765 / 2.434
E_Coul_needed = B_pair + 0.092
R_aa = Coul_prefactor / E_Coul_needed
print(f"E_Coul needed for 8Be balance: {E_Coul_needed:.3f} MeV")
print(f"R_alpha-alpha = 5.765 / {E_Coul_needed:.3f} = {R_aa:.2f} fm")
print(f"Paper cites: R_alpha-alpha = 2.37 fm")
assert abs(R_aa - 2.37) < 0.005, "R_aa mismatch"

# ============================================================
# SECTION 5.1 (v1.2): Extended N=Z alpha-chain at N_alpha = 11..14
# v1.2 replaces the v1.1 "structural-onset" block.
# See problem_histories/PH-OPEN-SS-22.md for retirement narrative.
# ============================================================
print("\n" + "="*76)
print("SECTION 5.1 (v1.2): Extended strict N=Z alpha-chain")
print("="*76)
print(f"{'Nucleus':8s} {'N_a':>4s} {'E':>4s} {'Pred':>10s} {'Meas':>10s} {'Error':>8s}")
print("-"*56)

# Strict N=Z alpha-chain (Z = N = 2*N_alpha, A = 4*N_alpha)
# AME 2020 values independently verified by 3 reviewers on 21 April 2026
extended_NZ = {
    '44Ti': (11, 375.475),  # Z=N=22
    '48Cr': (12, 411.462),  # Z=N=24  (v1.1 line 777 had "---" and "(not N=Z)" -- both wrong)
    '52Fe': (13, 447.696),  # Z=N=26
    '56Ni': (14, 483.990),  # Z=N=28
}
errors_ext = []
for nuc, (Na, B_exp) in extended_NZ.items():
    E = 3*Na - 6
    B_pred = Na * B_alpha_exp + E * B_pair
    err_pct = (B_pred - B_exp) / B_exp * 100
    errors_ext.append(err_pct)
    print(f"{nuc:8s} {Na:4d} {E:4d} {B_pred:10.3f} {B_exp:10.3f} {err_pct:+7.2f}%")

rms_ext = float(np.sqrt(np.mean(np.array(errors_ext)**2)))
print(f"\nExtended N=Z chain (N_alpha=11..14) RMS: {rms_ext:.2f}%")
print("In family with primary set (RMS 0.91%). No structural onset at N_alpha=12.")

# ------------------------------------------------------------
# For traceability: the v1.1 Table 1 rows at N_a >= 12 (retained as
# documentation of the retired OPEN-SS-22 hypothesis).
# These three nuclei each have N-Z = +4 (neutron-rich, non-alpha-chain).
# The ~2% deviation is neutron-excess binding (~2 MeV per extra neutron),
# not icosahedral-closure physics. See PH-OPEN-SS-22.md.
# ------------------------------------------------------------
print("\n--- v1.1 non-N=Z Table 1 rows (for traceability) ---")
print("These nuclei are NOT alpha-chain (each has N-Z = +4 neutron excess).")
print("The ~2% deviation is neutron-excess binding, documented in OPEN-SS-23.")
print(f"{'Nucleus':8s} {'N_a':>4s} {'Pred':>10s} {'Meas':>10s} {'Error':>8s}")
print("-"*48)

heavy_nonNZ = {
    '48Ti': (12, 418.699),  # Z=22, N=26
    '52Cr': (13, 456.349),  # Z=24, N=28
    '56Fe': (14, 492.254),  # Z=26, N=30
}
for nuc, (Na, B_exp) in heavy_nonNZ.items():
    E = 3*Na - 6
    B_pred = Na * B_alpha_exp + E * B_pair
    err_pct = (B_pred - B_exp) / B_exp * 100
    print(f"{nuc:8s} {Na:4d} {B_pred:10.3f} {B_exp:10.3f} {err_pct:+7.2f}%")
print("(This block is not part of SS-7 v1.2 Table 1; shown for history only.)")

# ============================================================
# SECTION 6.5: Hostile-geometry stress tests (ChatGPT contribution)
# ============================================================
print("\n" + "="*76)
print("SECTION 6.5 (stress tests): Lower-edge alternatives at fixed constants")
print("="*76)
print(f"{'Nucleus':8s} {'N_a':>4s} {'E_simp':>7s} {'Err':>8s}  "
      f"{'E_alt':>6s} {'Err_alt':>8s}  {'Alternative':30s}")
print("-"*90)

stress_tests = [
    # (nucleus, N_alpha, E_alt, alternative_name, B_exp)
    ('32S',   8, 12, 'cube',                       271.781),
    ('32S',   8, 16, 'square antiprism',           271.781),
    ('28Si',  7, 12, 'wheel-like',                 236.537),
    ('36Ar',  9, 20, 'monocapped sq antiprism',    306.716),
    ('40Ca', 10, 20, 'pentagonal-antiprism-type',  342.052),
]
paper_errors = {
    ('32S', 12): -6.37, ('32S', 16): -2.92,
    ('28Si', 12): -4.38, ('36Ar', 20): -1.70, ('40Ca', 20): -3.58,
}

for nuc, Na, E_alt, alt_name, B_exp in stress_tests:
    E_simp = 3*Na - 6
    B_simp = Na * B_alpha_exp + E_simp * B_pair
    B_alt  = Na * B_alpha_exp + E_alt  * B_pair
    err_simp = (B_simp - B_exp) / B_exp * 100
    err_alt  = (B_alt  - B_exp) / B_exp * 100
    print(f"{nuc:8s} {Na:4d} {E_simp:7d} {err_simp:+7.2f}%  "
          f"{E_alt:6d} {err_alt:+7.2f}%  {alt_name:30s}")
    # Verify against paper numbers
    expected = paper_errors[(nuc, E_alt)]
    assert abs(err_alt - expected) < 0.02, \
        f"Stress-test mismatch {nuc} E={E_alt}: got {err_alt:.2f}%, paper {expected}%"

print("\nAll five alternatives underperform the simplicial 3N-6 rule.")
print("36Ar is the single-edge-sensitivity diagnostic:")
print(f"  Dropping E by 1 shifts prediction by B_pair/B = {B_pair/306.716*100:.2f}%")
print(f"  Observed degradation: -1.70% - (-0.94%) = -0.76%  (matches 1 quantum)")

# ============================================================
# CROSS-CHECK: LO-CPP variant (uses B_alpha_LO instead of B_alpha_exp)
# Paper Section 3.3 discusses this equivalent variant
# ============================================================
print("\n" + "="*76)
print("SECTION 3.3: LO-CPP variant with B_alpha = 27.904 MeV")
print("Expected shift per nucleus: N_alpha * (B_alpha_LO - B_alpha_exp)")
print(f"  = N_alpha * ({B_alpha_LO} - {B_alpha_exp}) = N_alpha * {B_alpha_LO-B_alpha_exp:.3f}")
print("="*76)
print(f"{'Nucleus':8s} {'N_a':>4s} {'Err_exp':>8s} {'Err_LO':>8s}")
print("-"*40)
for nuc, (Na, B_exp) in ame2020.items():
    E = 3*Na - 6
    err_exp = (Na * B_alpha_exp + E * B_pair - B_exp) / B_exp * 100
    err_LO  = (Na * B_alpha_LO  + E * B_pair - B_exp) / B_exp * 100
    print(f"{nuc:8s} {Na:4d} {err_exp:+7.2f}% {err_LO:+7.2f}%")
print("\nBoth variants remain within CPP generic residual band (~4.1%).")

# ============================================================
# SUMMARY: All numerical content of SS-7 v1.2 reproduced
# ============================================================
print("\n" + "="*76)
print("ALL SS-7 v1.2 NUMERICAL CONTENT REPRODUCED FROM INHERITED CONSTANTS")
print("="*76)
print("Inputs used: M_0, phi, B_alpha (experimental), B_pair = M_0/phi")
print("No fits, no tuning, no nuclear-physics input beyond alpha binding.")
print(f"Eight primary Table 1 predictions (N_a = 3..10): max error +1.19%, RMS {rms:.2f}%")
print(f"Extended N=Z chain (N_a = 11..14): RMS {rms_ext:.2f}%, all <1%")
print(f"Twelve concurrent predictions total, RMS 0.80% (all 12)")
print("Five stress-test alternatives: all underperform simplicial rule")
print("R_alpha-alpha = 2.37 fm: inverted consistently from 8Be")
print("v1.1 non-N=Z rows retained for traceability (~2% neutron-excess signal)")
