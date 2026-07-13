#!/usr/bin/env python3
"""
PATCH 2447 -- OPEN-DM-FLOQUET-1 / collision kinematics: does a DM-rod/ring or baryon
collision at realistic CM energies deliver the ~17 MeV (form) / ~3.5 MeV (break)
bending thresholds (2446)? Closes the formation-coherence caveat and connects the
bending force to the ring-creation collision force (founder: central strike, ends
resist by inertia -> symmetric bending mode -> largest bend).

MASSES (repo): m_element=1408 MeV (2 planes) -> m_plane=704 MeV; N_planes=16 ->
M_rod = 8*1408 = 11.26 GeV (= candidate B mass). baryon ~938 MeV.
THRESHOLDS (2446): E_form=16.9 MeV (bend 16 hinges to 22.5deg, elastic ring),
E_break=3.5 MeV (focused, fragment one hinge), E_elastic~0.49 MeV (coat scale).
GEOMETRY: d=1.15 fm; L_rod=15*d=17.25 fm; R_ring=16 d/(2 pi)=2.93 fm (rod curls ~1 turn).
"""
import numpy as np
MeV=1.0; GeV=1e3
m_plane=704.0; NPL=16; M_rod=8*1408.0; m_bary=938.0
mu_rr=M_rod/2; mu_br=m_bary*M_rod/(m_bary+M_rod)
d=1.15; L_rod=(NPL-1)*d; R_ring=NPL*d/(2*np.pi)
E_form=16.9; E_break=3.5; E_elastic=0.49
kappa=13.7   # MeV, effective bending stiffness (2443, Layer C)
c_kms=299792.458
print("="*76); print("COLLISION KINEMATICS -- form/break thresholds vs CM energy"); print("="*76)
print(f"M_rod={M_rod/1e3:.2f} GeV (16 planes)  m_plane={m_plane} MeV  baryon={m_bary} MeV")
print(f"mu(rod-rod)={mu_rr/1e3:.2f} GeV  mu(baryon-rod)={mu_br:.0f} MeV")
print(f"L_rod={L_rod:.1f} fm  R_ring={R_ring:.2f} fm (rod is {L_rod/R_ring:.1f}x R_ring -> curls ~1 turn)")
print(f"thresholds: form={E_form} MeV  break={E_break} MeV  elastic~{E_elastic} MeV")
print()
def v_for(E,mu):  # beta = v/c for CM kinetic energy E = 0.5 mu v^2 (non-rel)
    return np.sqrt(2*E/mu)
print("="*76); print("(1) VELOCITY THRESHOLDS (beta=v/c, and km/s)"); print("="*76)
for lab,mu in [("rod-rod",mu_rr),("baryon-rod",mu_br)]:
    print(f"  {lab} (mu={mu:.0f} MeV):")
    for tag,E in [("elastic",E_elastic),("break",E_break),("form",E_form)]:
        b=v_for(E,mu)
        print(f"     {tag:8s} E={E:5.1f} MeV -> beta={b:.4f}  = {b*c_kms:8.0f} km/s")
print()
print("="*76); print("(2) COMPARE TO ACTUAL VELOCITY REGIMES"); print("="*76)
regimes=[("present galactic (DM disp)",250),("galaxy-cluster (high)",1500),
         ("primordial ~0.08c",0.08*c_kms),("primordial ~0.2c",0.2*c_kms)]
print(f"  {'regime':>28} {'km/s':>9} {'beta':>8} {'E_cm(rod-rod)':>14} {'verdict':>16}")
for lab,vk in regimes:
    b=vk/c_kms; Ecm=0.5*mu_rr*b**2
    vd=("forms ring" if Ecm>=E_form else "can break" if Ecm>=E_break else
        "flexes(elastic)" if Ecm>=E_elastic else "inert (< elastic)")
    print(f"  {lab:>28} {vk:>9.0f} {b:>8.5f} {Ecm:>11.4f} MeV {vd:>16}")
print()
print("  => present galactic DM-DM collisions deliver ~keV (<<0.49 MeV): rods are")
print("     COLLISIONALLY INERT now (good for CDM: dark matter stable/collisionless today).")
print("     Ring FORMATION needs beta~0.08 (~23000 km/s) -> early-universe/primordial")
print("     turbulence epoch, NOT present galaxies. Break needs beta~0.035.")
print()
print("="*76); print("(3) BENDING EFFICIENCY -- sudden vs adiabatic (founder: ends resist)"); print("="*76)
# fundamental bending period vs collision time. Discrete bending chain: omega_fund^2 ~
# (kappa/(m_plane d^2)) * (pi/NPL)^4 (4th-order bending dispersion, longest mode).
AHC=197.3
I_eff=m_plane*d**2
om2=(kappa/I_eff)*(np.pi/NPL)**4          # in c^2/fm^2 (natural units, energy in MeV)
om=np.sqrt(om2)                            # 1/fm (c=1)
tau_bend=2*np.pi/om                        # fm/c
print(f"  fundamental bending: I_eff=m_plane d^2={I_eff:.0f} MeV fm^2, omega={om:.4f} /fm,")
print(f"  tau_bend=2pi/omega={tau_bend:.0f} fm/c = {tau_bend*3.336e-24:.2e} s")
print(f"  {'beta':>8} {'tau_coll[fm/c]':>15} {'tau_coll/tau_bend':>18} {'regime':>22}")
for b in [0.001,0.035,0.078,0.2]:
    tau_coll=L_rod/b                       # interaction time ~ rod size / v
    ratio=tau_coll/tau_bend
    reg="SUDDEN (efficient bend)" if ratio<1 else "adiabatic (rigid, weak bend)"
    print(f"  {b:>8.3f} {tau_coll:>15.0f} {ratio:>18.2f} {reg:>28}")
print()
print("  => at formation velocities (beta~0.08) the collision is SUDDEN (tau_coll<tau_bend):")
print("     the center is struck before the inertial ends respond -> efficient symmetric")
print("     bending, as the founder described. At galactic beta~0.001 it is deeply")
print("     ADIABATIC (rod translates rigidly) AND sub-elastic -> no bending either way.")
print()
print("="*76); print("HONEST READ (G7)"); print("="*76)
print(f"  - Consistent hierarchy: present galactic (~keV, inert) << break (beta~0.035)")
print(f"    << form (beta~0.078). Rings form PRIMORDIALLY; DM rods are stable now.")
print(f"  - This CLOSES the formation-coherence caveat: formation needs a sudden,")
print(f"    rod-spanning, central-ish hit at beta>~0.08 -- available primordially, not now.")
print("  - CAVEATS: non-relativistic KE (fine, beta<=0.2); E_form/E_break absolute are")
print("    Layer C (2446); the bending EFFICIENCY (fraction of E_cm into the bend vs")
print("    translation/x-bonding/rebound) is order-unity in the sudden regime but NOT")
print("    computed exactly -- a true impulse-partition calc is owed. Full 360deg ring")
print("    closure vs a shallow-arc + end-bond (or two-rod x-bond then relax) is a")
print("    geometry question the energy threshold does not settle.")
print("  - Candidate (B): UNRESOLVED. This is formation-channel physics (input to the")
print("    cosmological-abundance question, parked with Omega_DM), NOT a make-or-break")
print("    promotion. Registry NOT promoted.")
