#!/usr/bin/env python3
"""
Patch 0703 — DM arc Step 1: self-interaction sigma/m vs the SIDM bound.

Falsification-first Gate-1 quantitative check (the "cheapest potential kill").

Question: do net-neutral qDP / hTetra structures, treated as the dark-matter
constituents, have a self-interaction cross-section per unit mass sigma/m below
the self-interacting-dark-matter (SIDM) bound (~1 cm^2/g at cluster scales)?

This is an ORDER-OF-MAGNITUDE estimate. Inputs and their provenance are tagged:
  [c14]   = read from companion c14 (Cornell potential / confinement scale)
  [est]   = estimated from the confinement scale (NOT a paper number)
  [obs]   = observational / standard-physics input
The dominant uncertainties are (a) the constituent mass [est] (factor ~few) and
(b) possible near-threshold resonant enhancement of the residual cross-section
(factor up to ~1e2-1e3). The geometric size r0 is used as a CONSERVATIVE (large)
cross-section; "subquantum" structures would be smaller, increasing the margin.
"""

import math

# ---- physical constants -------------------------------------------------
hbar_c_GeV_fm = 0.19733          # GeV*fm                              [obs]
fm2_to_cm2    = 1.0e-26          # 1 fm^2 = 1e-26 cm^2                  [obs]
GeV_to_g      = 1.78266e-24      # 1 GeV/c^2 in grams                  [obs]
t_hubble_s    = 4.35e17          # ~13.8 Gyr in seconds                [obs]

# ---- bonding / structure scale (from c14) -------------------------------
alpha_s = 0.3                    # strong coupling at ~r0              [c14]
r0_fm   = 0.26                   # Cornell crossover radius (fm)       [c14]
# residual interaction range for two COLOR-NEUTRAL structures is taken ~ r0
# (conservative: the structure's own size; "subquantum" => likely smaller).
R_int_fm = r0_fm

# geometric residual cross-section sigma ~ pi R^2
sigma_geom_fm2 = math.pi * R_int_fm**2
sigma_geom_cm2 = sigma_geom_fm2 * fm2_to_cm2

# ---- constituent masses -------------------------------------------------
# c04 gives mass = Compton standing-wave energy (mc^2 = hbar*nu_C) but NOT an
# absolute qDP/hTetra value. We bracket by the only available scale:
#   qDP  ~ constituent/QCD scale (lightest -> LARGEST sigma/m -> the binding case)
#   hTetra ~ charm/baryon cornerstone scale (heavier -> smaller sigma/m)
m_qDP_GeV    = 0.30              # [est] light/conservative
m_hTetra_GeV = 1.5               # [est] charm/baryon-frame scale

# binding-energy scale sanity check (NOT the mass): alpha_s*hbar_c/r0
E_bind_GeV = alpha_s * hbar_c_GeV_fm / r0_fm

# ---- halo environment ---------------------------------------------------
rho_DM_GeV_cm3 = 0.3             # local/halo fiducial (GeV/cm^3)      [obs]
rho_DM_g_cm3   = rho_DM_GeV_cm3 * GeV_to_g
v_halo_cm_s    = 2.0e7           # ~200 km/s galactic                  [obs]
v_clus_cm_s    = 1.0e8           # ~1000 km/s cluster                  [obs]

SIDM_bound = 1.0                 # cm^2/g (cluster-scale order)        [obs]

def sigma_over_m(sigma_cm2, m_GeV):
    return sigma_cm2 / (m_GeV * GeV_to_g)

def collisions_per_hubble(som_cm2_g, v_cm_s, rho_g_cm3=rho_DM_g_cm3):
    # Gamma = n sigma v = rho * (sigma/m) * v ; N = Gamma * t_H
    return rho_g_cm3 * som_cm2_g * v_cm_s * t_hubble_s

print("="*64)
print("DM arc Step 1: sigma/m vs SIDM bound  (order-of-magnitude)")
print("="*64)
print(f"r0 (residual range, conservative)   : {R_int_fm:.3f} fm   [c14]")
print(f"sigma_geom = pi r0^2                 : {sigma_geom_fm2:.3f} fm^2"
      f" = {sigma_geom_cm2:.3e} cm^2")
print(f"binding-scale check alpha_s hc / r0  : {E_bind_GeV:.3f} GeV (sanity, not mass)")
print()

for name, m in [("qDP  (light, the binding case)", m_qDP_GeV),
                ("hTetra (charm/baryon frame)   ", m_hTetra_GeV)]:
    som = sigma_over_m(sigma_geom_cm2, m)
    print(f"{name}: m = {m:.2f} GeV")
    print(f"    sigma/m (geometric)            : {som:.3e} cm^2/g"
          f"   ({SIDM_bound/som:.0f}x below bound)")
    for label, enh in [("x1   geometric", 1), ("x100 resonant", 100),
                       ("x1000 strong res.", 1000)]:
        s = som*enh
        flag = "PASS" if s < SIDM_bound else "FAIL"
        print(f"      {label:18s}: sigma/m = {s:.3e} cm^2/g  -> {flag}")
    Ncol = collisions_per_hubble(som, v_halo_cm_s)
    print(f"    collisions/particle/Hubble(halo,geom): {Ncol:.2e}")
    print()

print("Verdict logic:")
print(" - geometric estimate clears the SIDM bound by ~2-3 orders for both species")
print(" - survival is robust UNLESS a near-threshold resonance/large scattering")
print("   length enhances the residual cross-section by ~1e2-1e3 (nucleon-like),")
print("   which would push the light qDP channel to/above the bound.")
print(" - => NO kill at Step 1; Gate-1 closure now requires bounding the residual")
print("   qDP/hTetra scattering length (resonance check).")
