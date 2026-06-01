#!/usr/bin/env python3
"""
Patch 0705 -- DM arc R2: the vacuum-Sea cosmological-constant estimate and whether
its (l_P/R_H)^2 suppression is derived or a restatement of the Lambda ~ 1/R_H^2
coincidence.

The c08 development notes record: rho_Lambda_CPP = alpha_geom * (E_P/l_P^3) * (l_P/R_H)^2
~ 3.5e-10 J/m^3 vs observed ~5.3e-10 (factor 1.5). This script reproduces it and
tests the sensitivity to the choice of R_H -- which CPP does not currently fix.
"""
import math

# constants
E_P  = 1.9561e9      # J            (Planck energy)
l_P  = 1.6162e-35    # m            (Planck length)
c    = 2.9979e8      # m/s
H0   = 2.184e-18     # 1/s          (67.4 km/s/Mpc)
alpha_geom = 0.5594  # c02 600-cell Voronoi efficiency (dimensionless, derived)

rho_Planck = E_P / l_P**3            # ~Planck energy density (the "10^120" density)
rho_obs    = 5.3e-10                 # J/m^3, observed dark-energy density

# candidate horizon scales (CPP does not single one out):
R_hubble   = c / H0                  # Hubble length          ~1.37e26 m
R_particle = 3.2 * R_hubble          # particle horizon       ~4.4e26 m (comoving, LCDM)
R_dS       = R_hubble                # de Sitter / event horizon ~ Hubble length

def rho_Lambda(R_H):
    return alpha_geom * rho_Planck * (l_P / R_H)**2

print("="*66)
print("R2: vacuum-Sea Lambda estimate  rho = alpha_geom * rho_Pl * (l_P/R_H)^2")
print("="*66)
print(f"rho_Planck = E_P/l_P^3              : {rho_Planck:.3e} J/m^3  (the catastrophe scale)")
print(f"observed rho_Lambda                 : {rho_obs:.3e} J/m^3")
print()
for name, R in [("Hubble length  c/H0", R_hubble),
                ("particle horizon ~3.2 c/H0", R_particle)]:
    r = rho_Lambda(R)
    print(f"R_H = {name:26s} = {R:.2e} m")
    print(f"    rho_Lambda_CPP = {r:.3e} J/m^3   ->  {r/rho_obs:6.2f} x observed")
print()
print("Reading:")
print(" - The MAGNITUDE works: rho_Pl is suppressed by (l_P/R_H)^2 ~ 1e-122, which is")
print("   exactly the factor that turns the Planck density into ~the observed Lambda.")
print(" - BUT that factor IS the well-known Lambda ~ 1/R_H^2 coincidence: the result")
print(f"   swings by ~{ (rho_Lambda(R_hubble)/rho_Lambda(R_particle)):.0f}x depending on which horizon you insert,")
print("   and CPP does not yet derive which R_H is correct or WHY rho_vac ~ 1/R_H^2.")
print(" - So as it stands this is a numerically-close ESTIMATE / coincidence-restatement,")
print("   not a derivation. Deriving the (l_P/R_H)^2 suppression from CPP substrate")
print("   dynamics is the open requirement -- and it is also a coincidence-problem flag:")
print("   R_H grows with time, so a vacuum density tracking 1/R_H^2 is dynamical, not a")
print("   true constant (this is the standard 'why now' issue, inherited not solved).")
print()
print("Bearing on the DM arc (R2):")
print(" - GOOD: c05 sources gravity from the GRADIENT of net SSV, so a uniform Sea is")
print("   locally inert by construction -- consistent with DM = Sea inhomogeneities.")
print(" - The SAME Sea would source BOTH a (suppressed) uniform Lambda AND (unsuppressed)")
print("   local-gradient DM gravity: a genuine dark-energy<->dark-matter unification angle.")
print(" - REQUIREMENT: show ONE consistent CPP cosmological sector yields all three --")
print("   suppressed uniform Lambda, unsuppressed inhomogeneity gravity, and Friedmann --")
print("   rather than three separate assumptions. This is the scoped content of OPEN-SR-5.")
