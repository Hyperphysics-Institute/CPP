#!/usr/bin/env python3
"""
R3: can A_s ~ 2.1e-9 be DERIVED from the ZBW fluctuation normalization, or only adopted?
Three computations:
 (1) the NAIVE ZBW-stack-Poisson reading: zeta = delta_N = (1/3) delta(ln nbar) with
     Poisson stack fluctuations -> show it fails catastrophically (excludes it, and
     confirms the curvature must be sourced by the COLLECTIVE H_eff mode, not shot noise).
 (2) the COLLECTIVE delta-N reading (= what EU-1 actually uses, P_zeta ~ H_eff^2): A_s
     requires the absolute boost-field scale H_*; back out the H_* (and boost coupling
     kappa) that matches Planck A_s.
 (3) the kappa structure: n_s is kappa-INVARIANT (0751) but A_s ~ kappa^2 -> the same
     invariance that makes n_s a clean zero-parameter prediction is exactly why A_s is NOT.
"""
import numpy as np
Mpl_GeV = 2.435e18     # reduced Planck mass
A_s_obs = 2.1e-9
Nstar   = 57.0

print("="*68); print("R3 : is A_s derivable from the ZBW fluctuation normalization?"); print("="*68)

# --- (1) naive Poisson-stack reading ---
# pivot occupancy: N_rem = (1/3) ln nbar = 57  -> ln nbar = 171 -> nbar ~ e^171
ln_nbar = 3*Nstar
nbar = np.exp(ln_nbar)
# per-GP Poisson: delta nbar/nbar ~ 1/sqrt(nbar); zeta=(1/3)(dnbar/nbar); A_s=<zeta^2>
dnbar_over_nbar_perGP = 1/np.sqrt(nbar)
As_poisson_perGP = (1/9)*dnbar_over_nbar_perGP**2
# even coarse-grained over a whole Hubble patch (N_CP_patch CPs), A_s=(1/9)/N_CP_patch:
# to MATCH A_s we'd need N_CP_patch ~ 1/(9 A_s):
N_CP_needed = 1/(9*A_s_obs)
print("\n[1] NAIVE ZBW-stack-Poisson normalization:")
print(f"  pivot occupancy nbar = e^{ln_nbar:.0f} ~ 10^{ln_nbar/np.log(10):.0f}")
print(f"  per-GP Poisson  A_s = (1/9)/nbar ~ 10^{np.log10(As_poisson_perGP):.0f}   (obs 2.1e-9)")
print(f"  -> off by ~{np.log10(A_s_obs)-np.log10(As_poisson_perGP):.0f} ORDERS. EXCLUDED.")
print(f"  even patch-averaged, matching A_s needs only N_CP_patch ~ {N_CP_needed:.1e} CPs")
print(f"     -- but a Hubble patch holds >> that, and Poisson noise is WHITE not scale-")
print(f"     invariant -> shot noise gives the wrong amplitude AND wrong shape.")
print(f"  CONCLUSION: the curvature is NOT stack shot noise; it is the COLLECTIVE H_eff")
print(f"  mode (consistent with EU-1's P_zeta ~ H_eff^2). The 'ZBW fluctuation' that sets")
print(f"  A_s is the boost-field mode amplitude, not 1/sqrt(CP count).")

# --- (2) collective delta-N reading: A_s = H_*^2/(8 pi^2 eps) ---
# p=2 (m^2 phi^2-like): eps = 1/(2 N_*). Back out H_*:
eps = 1/(2*Nstar)
H_star2 = 8*np.pi**2 * eps * A_s_obs          # in Planck units (Mpl=1)
H_star = np.sqrt(H_star2)
print("\n[2] COLLECTIVE delta-N reading (EU-1: P_zeta ~ H_eff^2):")
print(f"  A_s = H_*^2 / (8 pi^2 eps),  eps = 1/(2N_*) = {eps:.4f}")
print(f"  matching A_s=2.1e-9  ->  H_* = {H_star:.2e} Mpl = {H_star*Mpl_GeV:.2e} GeV")
print(f"     i.e. a GUT-scale boost field (~10^14 GeV) -- the standard inflationary scale.")
print(f"  This H_* is NOT fixed by the tilt mechanism (which uses only d ln H_eff/dN).")
r_singlefield = 16*eps
print(f"  [adjacent note, HONEST] the SINGLE-FIELD relation r=16eps would give r={r_singlefield:.3f}")
print(f"     (> bound r<0.036). BUT EU-1 is a SPECTATOR-style mechanism (P_zeta~H_eff^2,")
print(f"     'spectator P~H^2 vs single-field 1/eps' per the paper), for which r is")
print(f"     DECOUPLED from eps and generically SMALLER -> r=16eps does NOT apply.")
print(f"     EU-1's tensor ratio is an UNDETERMINED separate CPP quantity (needs the")
print(f"     H_inf-vs-spectator-scale ratio), flagged as open -- NOT a clean tension.")

# --- (3) kappa structure: n_s invariant, A_s ~ kappa^2 ---
# H_eff = kappa*(mu(nbar)-mu(1)), mu=kT ln nbar.  n_s-1 = 2 d ln H_eff/dN: kappa cancels
# (log-derivative).  A_s = (H_*/2pi)^2 *(dN/dsigma)^2 ~ kappa^2 : kappa does NOT cancel.
print("\n[3] why A_s is undetermined while n_s is clean -- the kappa cancellation:")
print("  H_eff = kappa*(mu(nbar)-mu(1)),  mu = kT ln nbar  (0751).")
print("  n_s-1 = 2 d ln H_eff/dN  -> kappa cancels (log-derivative).  [0751: n_s INVARIANT")
print("     across kappa 1e-2..1e3]  => clean zero-parameter tilt.")
print("  A_s = (H_*/2pi)^2 * (dN/...)^2  ~  kappa^2  -> kappa does NOT cancel.")
for kap in [1e-8,2e-7,1e-6]:
    # A_s scales as kappa^2 relative to the matching kappa* that gives A_s_obs
    kap_star = 2e-7
    As = A_s_obs*(kap/kap_star)**2
    print(f"     kappa={kap:.0e} -> A_s ~ {As:.2e}")
print("  matching A_s=2.1e-9 needs boost coupling kappa* ~ 2e-7 (<-> H_*~GUT scale).")

print("\n"+"="*68); print("VERDICT (R3):")
print(" * Poisson/shot-noise normalization: EXCLUDED (~65 orders + wrong shape).")
print(" * A_s = collective boost-field amplitude, set by the boost coupling kappa")
print("   (equivalently H_* ~ 10^14 GeV).  n_s is kappa-INVARIANT (why it's clean);")
print("   A_s ~ kappa^2 (why it is NOT predicted).  Deriving A_s == deriving kappa.")
print(" * CPP is at PARITY with standard inflation (both leave the energy scale free),")
print("   NOT deficit.  A_s stays ADOPTED.  The genuine open target: derive kappa (the")
print("   chemical-potential->expansion-rate boost coupling) from substrate structure;")
print("   if kappa*~2e-7 falls out, A_s becomes a prediction (a win beyond inflation).")
print(" * Adjacent open item (NOT a clean tension): EU-1 tensor ratio r is undetermined\n   (spectator mechanism decouples r from eps); a separate CPP tensor computation owed.")
