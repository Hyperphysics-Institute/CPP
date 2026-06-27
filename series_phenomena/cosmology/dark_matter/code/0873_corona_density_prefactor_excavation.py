#!/usr/bin/env python3
"""
Patch 0873 (fork (a): excavate rho_Sea/rho_spine from the relic docs -> the density does NOT
close Channel 2; the corona reduces ENTIRELY to the single SF number V_surf/kT)
==========================================================================================
0872 left the corona as a conditional bound on TWO inputs: V_surf/kT (kinetic trapping +
equilibrium excess) and the prefactor G ~ (rho_Sea/rho_spine)*(perimeter*lambda_D/A_spine) for
the equilibrium-excess channel. Fork (a): is rho_Sea/rho_spine already bracketed favorably (small)
in the qDP relic/abundance corpus, closing the excess channel in-house? Excavation result: NO.

WHAT THE RELIC DOCS GIVE (and what they do NOT):
  - qdp_relic_abundance_scoping (0843): the COSMIC ratio Omega_DM/Omega_b ~ 5.36 is NOT derived
    (relocated to the free swirl amplitude). -> the cosmic abundance is a free parameter, not a
    bracket, and is a GLOBAL number; it does not give a LOCAL coat ratio.
  - qdp_f_as_a_number (0835): residual fraction f ~ 0.2 (a DEPTH fraction, not a density).
  - qdp_required_inputs (0833): substrate scales E_eDP~88 MeV, E_qDP~m_qDP~264 MeV.
  - qdp_energetic_eos (0832): the spine local density is a HARD-CORE close-packing CEILING (no
    equilibrium density; quantum pressure + hard core). -> rho_spine ~ substrate close-packing.
  None of these is a LOCAL rho_Sea/rho_spine.

THE TRAP (named and avoided): 0866's Sea-vs-relic hierarchy C = [hTetra]/[ribbon] >> 1 is a
GLOBAL species-count ratio (few relic ribbons in a vast Sea) -- it over-determined the GLUEBALL
chaperoning (more chaperones = good). It is NOT the local coat mass ratio. The corona coat forms
LOCALLY around each spine, where the ambient Sea and the spine are BOTH substrate at the same
close-packing/lattice scale -> rho_Sea/rho_spine (LOCAL) ~ O(1). The cosmic hierarchy does NOT
suppress the local coat. (If anything the geometric factor perimeter*lambda_D/A_spine ~ few.)

CONSEQUENCE: G ~ O(1)-few, NOT << 1. The density gives NO safety margin for Channel 2. The
equilibrium-excess channel therefore reduces ENTIRELY to V_surf/kT, with a STRINGENT threshold
(V_surf/kT <~ 0.5), far tighter than the trapping threshold (~60-90). So:

  CORONA SAFE  <=>  V_surf/kT <~ 0.5   (equilibrium-excess channel is binding; trapping is slack)

Fork (a) did NOT retire half the risk. It LOCALIZED the entire corona risk to one SF number,
V_surf/kT, and showed the density cannot help. Honest, and the burden is now fully on SF.

Run: python3 0873_corona_density_prefactor_excavation.py
"""
import numpy as np

print("="*86)
print("CORONA density prefactor -- fork (a) excavation: density does NOT close Channel 2 (0873)")
print("="*86)

print("\n(A) LOCAL geometric prefactor G ~ (rho_Sea/rho_spine)*(perimeter*lambda_D/A_spine)")
print("    local rho_Sea/rho_spine ~ O(1): ambient Sea and spine are BOTH substrate close-packing")
print("    (qdp_energetic_eos: spine = hard-core close-packing ceiling). The cosmic hierarchy")
print("    (0866 C>>1, global species count) does NOT apply to the local coat.")
print(f"    {'cross perimeter':>15} | {'lambda_D (rungs)':>16} | {'A_spine (rung^2)':>16} | {'geom factor':>11} | {'G (rho~1)':>9}")
for (perim,lamD,Aspine) in [(8,1.0,5),(10,1.5,5),(12,2.0,4)]:
    geom=perim*lamD/Aspine
    print(f"    {perim:>15d} | {lamD:>16.1f} | {Aspine:>16d} | {geom:>11.2f} | {geom:>9.2f}")
print("    => G ~ 1.6-6 (order unity to a few). NO density suppression. (Hoped-for G<<1 absent.)")

print("\n(B) Equilibrium-excess threshold with G~O(1)-few: m_coat/m_spine = G*(cosh(V/kT)-1) << 1")
print(f"    {'V_surf/kT':>10} | {'cosh-1':>8} | {'m_coat/m_spine (G=1)':>20} | {'(G=3)':>8} | verdict")
for x in (0.2,0.3,0.5,0.8,1.0):
    c=np.cosh(x)-1
    v="safe" if 3*c<0.3 else ("marginal" if 3*c<1 else "DILUTES")
    print(f"    {x:>10.2f} | {c:>8.3f} | {c:>20.3f} | {3*c:>8.3f} | {v}")
print("    => binding threshold V_surf/kT <~ 0.5 (G=1) to <~0.3 (G=3). The equilibrium-excess")
print("       channel needs a SHALLOW residual well, <~ half kT. No density margin to relax it.")

print("\n(C) The two channels, now both reduced to the SAME single SF number V_surf/kT:")
print("    kinetic trapping  : safe unless V_surf/kT >~ 60-90  (i.e. V_surf >~ 0.6 E_bond)  -- SLACK")
print("    equilibrium excess: safe iff   V_surf/kT <~ 0.3-0.5                               -- BINDING")
print("    => CORONA SAFE  <=>  V_surf/kT <~ 0.5.  One SF/substrate number decides the cross route.")

print("\n(D) Is V_surf/kT <~ 0.5 plausible? (the physical case, still SF-pending)")
print("    V_surf = residual, Sea-SCREENED, ORIENTATION-AVERAGED well of a PROMISCUOUS, charge-")
print("    cancelled ee-edge to a BARE eDP (not an hTetra). kT_amb <~ 19 keV (0860); E_bond ~ keV-MeV.")
print("    V_surf/kT <~ 0.5 means V_surf <~ ~10 keV -- BELOW the bond window. Plausible IF the")
print("    promiscuous edge gives a sub-thermal residual to a bare eDP; a few-kT residual would be")
print("    MARGINAL-to-diluting. This is precisely the SF residual-charge-geometry quantity to pin.")

print("\n"+"="*86)
print("FORK (a) RESULT (Layer C, honest -- did NOT close the half I hoped): the relic/abundance")
print("docs do NOT bracket a favorable rho_Sea/rho_spine. The cosmic Sea-vs-relic hierarchy (0866)")
print("is a GLOBAL species count and does NOT apply to the LOCAL coat; locally Sea and spine are both")
print("substrate close-packing, so the prefactor G ~ O(1)-few gives NO safety margin. The corona's")
print("equilibrium-excess channel therefore reduces ENTIRELY to V_surf/kT, with a STRINGENT binding")
print("threshold V_surf/kT <~ 0.5 (vs the slack trapping threshold ~60-90). NET: the entire corona")
print("risk is now localized to ONE SF number -- V_surf/kT, required <~ 0.5 -- which is plausible")
print("(promiscuous charge-cancelled screened edge to a bare eDP) but SF-pending. The cross route's")
print("last open item is a single, sharply-posed SF residual-charge-geometry calculation.")
print("="*86)
