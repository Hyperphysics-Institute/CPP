#!/usr/bin/env python3
"""
Patch 0875 (compute rho_spine/rho_Sea -> the framing breaks -> corona reframed and RETIRED)
==========================================================================================
Thomas: compute rho_spine/rho_Sea (the 0874 deciding number; corona safe iff <~1.15). Doing it
literally reveals the framing is MIS-POSED, and the correct (energy-scale) analysis RETIRES the
corona. This OVERTURNS the 0873/0874 V_surf-vs-kT framing -- the third revision of this section.

WHY THE RATIO BREAKS: the vacuum DP-Sea lattice spacing is fixed at l_P (Planck) [SF-2 line 1297;
EU-1], while the spine's qDP/hTetra units sit at r_c ~ 1 fm ~ 1e20 l_P. So rho_spine (~nuclear,
4.7e14 g/cm^3) vs any 'rho_Sea' is 1e43 (vs the balanced vacuum's gravitating rho_Lambda) or
1e-79 (vs the Planck-dense substrate) -- NEVER ~1. The '<~1.15' bar implicitly assumed a dilute,
fm-scale, ACCRETING eDP reservoir comparable to the spine. No such reservoir exists.

THE CORRECT TEST (energy-scale): a sigma/m-diluting coat needs real eDP MASS bound at the surface.
That needs (a) a well deep enough to bind a real eDP and (b) a reservoir to fill it. BOTH fail:
  (a) V0_elec ~ 34-94 keV (0874) is ~1500x SHALLOWER than the eDP creation energy E_eDP = 88 MeV.
      A well << the particle rest energy cannot create+bind a real quantum (costs 88 MeV, returns
      0.05 MeV). It only POLARIZES the balanced vacuum -> vacuum-polarization SELF-ENERGY, already
      inside the dressed m_unit, scaling per-unit with N (NOT a surface coat).
  (b) the only dense reservoir is the vacuum Sea, which is BALANCED (ground state, no net mass).
      A hypothetical real-eDP halo gas is ultra-dilute (n r_c^3 ~ 1e-38) -> coat/core ~ 1e-37.

CONSEQUENCE: the V_surf well is real but UNFILLED; the corona does NOT preferentially dilute the
extended aggregate. sigma/m (the d_f physics) survives undiluted. Corona risk RETIRED -- modulo
(i) sub-dominant surface self-energy (~perimeter, vanishes per-unit at large N), (ii) the standard
sub-threshold-well -> virtual-only result, and (iii) THIRD-revision status -> panel scrutiny.
Consistency check: the same argument means MONOMERS (DM-1 baseline) also carry no real-eDP coat --
m_unit is the dressed mass DM-1 already used; no correction to DM-1. The reframing is internally
consistent with the shipped program.

Run: python3 0875_rho_spine_rho_Sea_and_corona_reframe.py
"""

import numpy as np
# unit conversions
MeV_per_fm3_to_g_cm3 = 1.78e12   # 1 MeV/fm^3 -> g/cm^3
m_unit=264.0; r_c=1.0            # MeV, fm  (qDP; hTetra heavier)
E_eDP=88.0e3                     # keV  (eDP creation/excitation energy)
V0_elec=(34,57,94)              # keV  (electric vdW contact depth, 0874)
kT=19.0                          # keV
lP_fm=1.616e-20                  # Planck length in fm
rho_Lambda=6e-30                 # g/cm^3 (gravitating vacuum)

print("="*84)
print("Attempt the literal ratio rho_spine/rho_Sea -- and watch the framing break")
print("="*84)
rho_spine = m_unit/r_c**3 * MeV_per_fm3_to_g_cm3
print(f"  rho_spine ~ m_unit/r_c^3 = {m_unit} MeV/fm^3 -> {rho_spine:.2e} g/cm^3 (nuclear, matches EoS)")
# vacuum 'Sea' density -- two readings, both far from rho_spine:
rho_Sea_planck = 1.0/ (lP_fm**3) * MeV_per_fm3_to_g_cm3 * 0  # balanced -> ~0 net mass
print(f"  rho_Sea (Planck lattice, balanced ground state) -> NET gravitating mass ~ rho_Lambda = {rho_Lambda:.1e} g/cm^3")
print(f"     ratio rho_spine/rho_Lambda ~ {rho_spine/rho_Lambda:.1e}   (NOT ~1)")
print(f"  rho_Sea (if read as the Planck-DENSE substrate, mass/site~m_P): ~Planck density ~5e93 g/cm^3")
print(f"     ratio rho_spine/rho_Planck ~ {rho_spine/5e93:.1e}   (NOT ~1)")
print("  => rho_spine/rho_Sea is 10^43 or 10^-79 depending on which 'Sea mass' you mean -- NEVER ~1.")
print("     The '<~1.15' threshold implicitly assumed a dilute-but-comparable ACCRETING eDP density")
print("     at the fm scale. No such reservoir exists: the vacuum Sea is Planck-scale and BALANCED.")

print("\n"+"="*84)
print("The correct question: can the electric-vdW well BIND real eDP mass? (energy-scale test)")
print("="*84)
print(f"  electric vdW well depth V0_elec ~ {V0_elec[0]}-{V0_elec[2]} keV (central {V0_elec[1]}).")
print(f"  eDP creation/excitation energy E_eDP = {E_eDP:.0f} keV = 88 MeV.")
for V0 in V0_elec:
    print(f"    E_eDP / V0_elec = {E_eDP/V0:7.0f}x  -> the well is ~{E_eDP/V0:.0f}x too shallow to pay the eDP cost")
print("  => V0_elec << E_eDP by ~1500x. The well CANNOT create+bind a real eDP excitation (creating one")
print("     costs 88 MeV; the well returns ~0.05 MeV). It can only POLARIZE the balanced vacuum --")
print("     i.e. it contributes to the unit's vacuum-polarization SELF-ENERGY, already inside m_unit.")

print("\n"+"="*84)
print("If one nonetheless imagines a dilute real-eDP gas at halo density, the coat is negligible:")
print("="*84)
for rho_halo,label in [(1e-23,'dwarf core'),(1e-25,'local')]:
    m_eDP_g=88.0*1.78e-27
    n=rho_halo/m_eDP_g                      # eDP / cm^3
    n_fm3=n*1e-39
    shell_over_core=6.0; enh=5.0; mass_ratio=88/264
    coat_over_core=n_fm3*r_c**3*shell_over_core*enh*mass_ratio
    print(f"  {label:12} rho={rho_halo:.0e} g/cm^3 -> n_eDP r_c^3 ~ {n_fm3:.1e} -> coat/core ~ {coat_over_core:.1e} (negligible)")
print("  => even as a real-eDP gas, halo densities give n r_c^3 ~ 1e-38: no coat.")

print("\n"+"="*84)
print("VERDICT: corona does NOT preferentially dilute the aggregate. The V_surf well is real but")
print("UNFILLED: V0_elec ~ 56 keV is ~1500x too shallow to bind real eDPs (E_eDP=88 MeV), and the only")
print("dense reservoir -- the vacuum Sea -- is BALANCED (its coupling is vacuum-polarization self-energy,")
print("part of the dressed m_unit, scaling per-unit with N, NOT a surface coat). So sigma/m is not")
print("diluted. This OVERTURNS the 0873/0874 V_surf-vs-kT framing, which computed the well depth without")
print("checking that a reservoir of bindable real eDPs exists -- it does not. Corona risk RETIRED")
print("(caveats: sub-dominant surface self-energy ~perimeter vanishes per-unit at large N; rests on the")
print("standard sub-threshold-well -> virtual-only result; THIRD revision -> warrants panel scrutiny).")
print("="*84)
