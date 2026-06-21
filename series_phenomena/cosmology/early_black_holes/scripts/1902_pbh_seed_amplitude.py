#!/usr/bin/env python3
"""
1902_pbh_seed_amplitude.py  —  OPEN-COSMO-PBH-1 Sub-target 2 verify.

Question: does the ADOPTED EU-1 primordial spectrum (smooth delta-N result,
n_s = 1 - 2/N_*, alpha_s = -2/N_*^2; Patch 0742 / EU-1 v1.0), extrapolated from
the CMB pivot down to LRD-seed scales (M ~ 1e2..1e5 Msun), reach the amplitude
required to form primordial black holes (PBHs) by occupancy-retention?

Method: pure order-of-magnitude. Curvature power P_R(k) = A_s (k/k_*)^(n_s-1 + 0.5 alpha_s ln(k/k_*)).
PBH formation in the rare-tail (Press-Schechter-like) collapse fraction
    beta ~ exp(-delta_c^2 / (2 sigma_delta^2)),  sigma_delta ~ sqrt(P_R) (O(1) transfer dropped).
Required threshold delta_c ~ 0.45 (radiation-era collapse, standard).

No CPP-specific claim is computed here beyond the EU-1 spectrum it ships; the point
is to show the amplitude gap is so large that NO threshold/EoS effect can close it.
"""
import math

# --- EU-1 adopted spectrum (Patch 0742 / EU-1 v1.0) ---
N_star = 57.0                     # observable pivot e-folds (CP-count fixed; PRED-C-96)
n_s     = 1.0 - 2.0/N_star        # 0.9649
alpha_s = -2.0/N_star**2          # -0.00062
A_s     = 2.1e-9                  # scalar amplitude at CMB pivot (Planck), k_* = 0.05 Mpc^-1
k_pivot = 0.05                    # Mpc^-1
delta_c = 0.45                    # radiation-era collapse threshold (standard)

# --- comoving wavenumber of a PBH of horizon mass M (rough; k ~ 7e5 (M/Msun)^-1/2 Mpc^-1) ---
def k_of_M(M_solar):
    return 7.0e5 * M_solar**(-0.5)

def P_R(k):
    x = math.log(k / k_pivot)
    expo = (n_s - 1.0) * x + 0.5 * alpha_s * x * x
    return A_s * math.exp(expo)

def beta(P):
    sigma = math.sqrt(P)
    # exponent magnitude; guard against overflow in exp
    arg = delta_c**2 / (2.0 * sigma**2)
    return sigma, arg   # return arg = -ln(beta); beta = exp(-arg)

print(f"EU-1 adopted spectrum:  n_s = {n_s:.4f},  alpha_s = {alpha_s:.5f},  A_s = {A_s:.2e}")
print(f"Threshold delta_c = {delta_c}")
print()
print(f"{'M [Msun]':>10} | {'k [Mpc^-1]':>11} | {'P_R(k)':>10} | {'sigma_delta':>11} | {'-ln(beta)':>12}")
print("-"*66)
for M in [1e2, 1e3, 1e4, 1e5]:
    k = k_of_M(M)
    P = P_R(k)
    sig, arg = beta(P)
    print(f"{M:>10.0e} | {k:>11.2e} | {P:>10.2e} | {sig:>11.2e} | {arg:>12.2e}")

print()
# What sigma would be needed for even a rare-seed-relevant beta ~ 1e-20?
beta_target = 1e-20
sigma_needed = delta_c / math.sqrt(2.0 * (-math.log(beta_target)))
P_needed = sigma_needed**2
print(f"For even a rare-seed beta ~ {beta_target:.0e}:  need sigma_delta ~ {sigma_needed:.3f}  (P_R ~ {P_needed:.2e})")
P_have = P_R(k_of_M(1e3))
print(f"EU-1 delivers at 1e3 Msun:                 sigma_delta ~ {math.sqrt(P_have):.2e}  (P_R ~ {P_have:.2e})")
print(f"Amplitude deficit in P_R:                  ~{P_needed/P_have:.1e}x  (~{math.log10(P_needed/P_have):.1f} orders of magnitude)")
print()
print("VERDICT: EU-1's near-scale-invariant spectrum is ~7 orders of magnitude below the")
print("PBH-formation amplitude at LRD-seed scales. The red tilt + negative running make")
print("smaller scales WORSE, and the final-e-fold cliff (0741/0742) suppresses the lightest")
print("scales hardest of all. No threshold drop or QCD-EoS softening (which act on the")
print("O(1) exponent prefactor) can close a ~10^8 gap in -ln(beta). => occupancy-retention")
print("PBH channel is a NULL at LRD-seed masses. CPP must seed early SMBHs astrophysically,")
print("same as LCDM. This REINFORCES the Patch 1900 non-discriminating verdict.")
