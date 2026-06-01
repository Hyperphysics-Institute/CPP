#!/usr/bin/env python3
"""
Patch 0704 -- DM arc Step 2: free vs baryon-bound bookkeeping (the "second kill").

Question (Gate / bookkeeping): can the FREE qDP/hTetra population total ~5x the
baryonic mass (observed Omega_DM/Omega_b ~ 5.36) WITHOUT double-counting the
qDP/hTetra already bound inside nucleons?

This is an order-of-magnitude bookkeeping. The decisive finding is structural, not
numerical: the constraint is NOT scarcity (the Dipole Sea is an enormous reservoir),
so what the ~5:1 ratio actually costs is examined below.

Tags: [obs] standard cosmology; [c14/c04] CPP scales; [est] estimate.
"""
import math

# ---- observed cosmology (Planck 2018) -----------------------------------
Ob_h2, Odm_h2 = 0.02237, 0.1200          # [obs]
h = 0.6736                                # [obs]
ratio_obs = Odm_h2 / Ob_h2
rho_crit = 1.8783e-26 * h*h               # kg/m^3   [obs]
rho_b  = (Ob_h2 / (h*h)) * rho_crit
rho_dm = (Odm_h2 / (h*h)) * rho_crit
eta = 6.1e-10                             # baryon/photon ratio [obs]

GeV_kg = 1.7827e-27                       # kg per GeV/c^2 [obs]

# ---- ambient Dipole-Sea density (CPP) -----------------------------------
# A net-neutral DP at the confinement scale; lattice spacing ~ Cornell r0.
m_DP_GeV = 0.30                           # [est] QCD/constituent scale
r0_m     = 0.26e-15                       # [c14] Cornell crossover (m)
m_DP_kg  = m_DP_GeV * GeV_kg
n_Sea    = 1.0 / r0_m**3                  # one DP per lattice cell (lower bound on density)
rho_Sea  = m_DP_kg * n_Sea

# ---- derived quantities -------------------------------------------------
delta_cosmic = rho_dm / rho_Sea           # swirl overdensity needed (cosmic mean)
rho_halo = 5.0e-22                         # ~0.3 GeV/cm^3 local halo DM (kg/m^3) [obs]
delta_halo = rho_halo / rho_Sea
Omega_Sea = rho_Sea / rho_crit            # IF the uniform Sea gravitated cosmologically
# double-counting: if baryon-internal qDP/hTetra (~rho_b) were wrongly counted free
ratio_doublecounted = (rho_dm + rho_b) / rho_b

print("="*66)
print("DM arc Step 2: free vs baryon-bound bookkeeping (order-of-magnitude)")
print("="*66)
print(f"observed Omega_DM/Omega_b           : {ratio_obs:.3f}")
print(f"rho_b  (baryon)                     : {rho_b:.3e} kg/m^3")
print(f"rho_DM (dark matter, cosmic mean)   : {rho_dm:.3e} kg/m^3")
print()
print(f"ambient Dipole-Sea density (QCD-scale, lower bound):")
print(f"  rho_Sea ~ m_DP / r0^3             : {rho_Sea:.3e} kg/m^3"
      f"  (~{rho_Sea/2.3e17:.0e}x nuclear density)")
print()
print("1) IS ABUNDANCE THE CONSTRAINT?  No -- the reservoir is vast.")
print(f"   swirl overdensity to make cosmic-mean DM: delta = rho_DM/rho_Sea = {delta_cosmic:.1e}")
print(f"   swirl overdensity to make halo DM       : delta_halo            = {delta_halo:.1e}")
print("   => ~5:1 is trivially reachable from an infinitesimal Sea overdensity;")
print("      the ratio is set by the (free) primordial swirl amplitude, not derived.")
print()
print("2) IS DOUBLE-COUNTING THE PROBLEM?  No -- it's a ~19% effect, cleanly avoidable.")
print(f"   ratio if baryon-internal qDP/hTetra wrongly counted free: {ratio_doublecounted:.2f}")
print(f"   (vs {ratio_obs:.2f}); baryon relic is eta~{eta:.0e}, negligible vs the Sea.")
print()
print("3) THE ACTUAL CONSTRAINT: does the uniform Sea gravitate?")
print(f"   IF the uniform ambient Sea gravitated cosmologically:")
print(f"     Omega_Sea = rho_Sea/rho_crit   : {Omega_Sea:.1e}   <-- vacuum catastrophe")
print(f"   (QCD-scale gives ~1e45; a Planck-scale Sea gives ~1e120.)")
print("   The DM picture REQUIRES the uniform Sea NOT to gravitate cosmologically")
print("   while its swirl-inhomogeneities DO. That ties Step 2 to the unbuilt")
print("   cosmological sector / cosmological-constant problem (OPEN-SR-5).")
print()
print("VERDICT: NO kill, NO clean pass.")
print(" - abundance is not the constraint (reservoir vast)")
print(" - double-counting is ~19%, avoidable")
print(" - ~5:1 is an unexplained free input (relocates LCDM's coincidence; §6c concedes")
print("   'relative abundances are empirical questions')")
print(" - real open requirement: the Sea-gravitation consistency (could be a feature --")
print("   a CC-problem dodge -- or a liability vs Friedmann); GATED on OPEN-SR-5.")
