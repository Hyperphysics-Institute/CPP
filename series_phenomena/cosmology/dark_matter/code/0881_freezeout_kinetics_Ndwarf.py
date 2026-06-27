#!/usr/bin/env python3
"""
Patch 0881 (freeze-out kinetics: pinning N_dwarf(v) -> the path to a single number)
===================================================================================
0878 left N_dwarf as a bracket (5-60 rungs) and called the equilibrium grown size the deciding knob.
This patch works that knob. Physical shape:

  * DWARFS DO NOT REPROCESS. A dwarf collision deposits ~0.78 keV, BELOW the bond window, so it neither
    fragments nor re-grows the rod. Hence N_dwarf = N_freeze, the PRIMORDIAL freeze-out size.
  * N_freeze is set by reversible (isodesmic) aggregation freeze-out in the early universe. For equal-K
    linear self-assembly the number-average size is  <N> = sqrt(K*phi),  K = exp(E_bond/kT_form),
    phi = DM-element volume fraction at formation  =>  N_freeze ~ sqrt(phi)*exp(E_bond/2 kT_form).
  * CLUSTERS REPROCESS. A cluster collision deposits ~1.95 MeV > E_bond -> fragments N_freeze down to
    N_cluster -> lower sigma/m (collisionless). This is the velocity dependence.

The forward map (E_bond/kT_form -> N) is EXPONENTIALLY sensitive, so N is not absolutely predicted.
But the INVERSE map (band-required N -> E_bond/kT_form) is only LOGARITHMIC in the uncertain phi, so the
required ratio is robust. The test: does that required ratio land E_bond inside the INDEPENDENTLY-required
fragmentation window [0.78 keV, 1.95 MeV] for a plausible formation temperature kT_form <~ 19 keV (0860)?

Run: python3 0881_freezeout_kinetics_Ndwarf.py
"""
import numpy as np
floor=0.11; band=(0.6,2.0)
N_band=(band[0]/floor, band[1]/floor)              # 0878: band -> N ~ 5-18 (g=1) .. up to ~60 (g=1/sqrt12)
N_lo, N_hi = 5.0, 60.0
Edep_dwarf=0.78e-3; Edep_clu=1.95                  # MeV (0860)
win=(0.78e-3, 1.95)                                # E_bond fragmentation window, MeV (0860)
kT_form_max=19e-3                                  # MeV (0860 ceiling)

print("="*84); print("Freeze-out kinetics: pinning N_dwarf(v)  (Patch 0881)"); print("="*84)

print("\n(A) phi = DM-element volume fraction at formation (cosmological estimate, bracketed):")
rho_DM=1.4e-6                 # GeV/cm^3 cosmic today
m_el=(1.0,2.0)               # GeV (element ~ 4 m_hTetra)
kT_now=2.35e-13              # MeV (CMB today, ~2.35e-4 eV)
Vel=(1e-39,1e-36)            # cm^3, element volume ~ (1-10 fm)^3
phis=[]
for mel in m_el:
  n_now=rho_DM/mel
  for kTf in (5e-3,kT_form_max):
    zfac=(kTf/kT_now)**3
    for V in Vel:
      phis.append(n_now*zfac*V)
phi_lo,phi_hi=min(phis),max(phis)
print(f"    phi ~ {phi_lo:.1e} .. {phi_hi:.1e}  (enters the inverse map only as -ln(phi), i.e. logarithmically)")

print("\n(B) INVERSE map (robust): band-required N -> E_bond/kT_form = 2 ln(N/sqrt(phi)):")
def ratio(N,phi): return 2*np.log(N/np.sqrt(phi))
rmin=ratio(N_lo,phi_hi); rmax=ratio(N_hi,phi_lo)
print(f"    N ~ {N_lo:.0f}-{N_hi:.0f}, phi ~ {phi_lo:.0e}-{phi_hi:.0e}  =>  E_bond/kT_form ~ {rmin:.0f} - {rmax:.0f}")
print(f"    (spread is small despite 4-decade phi range, because phi enters logarithmically.)")

print("\n(C) CLOSURE: does that ratio put E_bond inside the fragmentation window for kT_form <~ 19 keV?")
print(f"    {'kT_form (keV)':>13} | {'E_bond/kT~':>10} | {'E_bond (MeV)':>13} | in window [0.78keV,1.95MeV]?")
for kTf in (1e-3,5e-3,kT_form_max):
    for r in (rmin,rmax):
        Eb=r*kTf; ok = win[0]<=Eb<=win[1]
        print(f"    {kTf*1e3:>13.0f} | {r:>10.0f} | {Eb:>13.4f} | {'YES' if ok else 'no'}")

print("\n(D) Velocity dependence with E_bond in the closed range (take N_freeze=10, E_bond=0.5 MeV):")
Nf=10.0; Eb=0.5
for label,Edep,v in (("dwarf",Edep_dwarf,30),("group",0.05,300),("cluster",Edep_clu,1500)):
    frag=min(1.0,Eb/Edep) if Edep>Eb else 1.0     # fragment factor (1 = intact)
    Nv=max(1.0,Nf*frag); sm=floor*Nv
    tag = "intact -> CORE" if Edep<Eb else "fragments -> collisionless"
    print(f"    {label:>7} (v~{v:>4} km/s, E_dep={Edep*1e3:7.2f} keV): N~{Nv:4.1f}  sigma/m~{sm:4.2f}  [{tag}]")

print("\n"+"="*84)
print("N_dwarf(v) VERDICT (Layer C): N_dwarf = N_freeze (dwarfs do not reprocess). The band-required")
print("N_freeze ~ 5-60 fixes the freeze-out ratio E_bond/kT_form ~ 24-41 ROBUSTLY (logarithmic in the")
print("uncertain abundance phi), and that ratio puts E_bond inside the INDEPENDENTLY-required")
print("fragmentation window [0.78 keV, 1.95 MeV] for the whole plausible formation range kT_form <~ 19 keV.")
print("So FOUR constraints -- band magnitude (0878), reversible-aggregation freeze-out, the fragmentation")
print("window (0860), and cluster-collisionless -- CLOSE on one consistent point (E_bond ~ 0.05-1 MeV,")
print("kT_form ~ few-19 keV, N_dwarf ~ tens), with no fine-tuning beyond E_bond/kT_form ~ 24-41.")
print("NOT yet a single number: the forward map N(E_bond/kT) is exponentially sensitive, so N is pinned")
print("to 'tens' only as a consistency, not an absolute value. FALSIFIABLE: SF-2/SF-5 pins E_bond and the")
print("relic/epoch calc pins kT_form; if E_bond/kT_form falls outside ~24-41 the band is missed. Pinning")
print("either one collapses N_dwarf to a single value and the core-size-vs-halo-mass relation to a curve.")
print("CAVEAT: assumes isodesmic equilibrium freeze-out; a fully kinetic (Smoluchowski + Hubble) treatment")
print("could shift the prefactor (not the logarithmic robustness). phi inherited (abundance, DM-1 §8).")
print("="*84)
