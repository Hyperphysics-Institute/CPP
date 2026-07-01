#!/usr/bin/env python3
"""
OPEN-COSMO-DM-4 (patch 2204, substrate-cosmology lane): derive kT_form and <N> from CPP substrate cosmology.
============================================================================================================
The DM 2203 handover asked: derive nu_PCD, H_form, E_bond -> kT_form -> <N>, and decide whether kT_form lands
near E_bond/13 (=> N_form ~ 400-1000 dwarf normalization) naturally, by tuning, or outside (kill).

RESULT (see output): with the physically-correct vibrational Arrhenius detach prefactor nu_vib ~ 1.5e22 Hz and
standard Friedmann H(T), the self-consistent thermal-contact freeze-out gives kT_form ~ 1.3-5.4 MeV,
E_bond/kT_form ~ 49-51, and <N> ~ 1e4-1e6 -- OVER the dwarf target 400-1000 by ~2-3 orders (over-cored). The
1846 target "kT_form~5 MeV, ratio~13" used phi~1 (close-packed, unphysical); the physical dilute-gas
phi~1e-9..1e-14 (0881) moves the band-required ratio to ~34-45, which the forward freeze-out ~matches (~50) ->
<N> lands ~2-3 orders high, not in-window. Landing in-window needs either DM colder than radiation by ~1e2
(unpinned decoupling) or a nucleation/depletion cap (the equilibrium <N>~1e5 exceeds plausible monomers-per-
nucleus, so the true size is likely nucleation-limited -> kT_form is NOT the sole controlling variable).
VERDICT: N_form is NOT a zero-parameter prediction; the natural case over-cores; the reduction to kT_form (1846)
is incomplete. Dwarf branch not secured; cluster sigma/m ~ 1/v^2 branch stands (independent).
"""

import numpy as np
from scipy.optimize import brentq

# ---- constants ----
MPl   = 1.22e22        # MeV (Planck mass)
hbar_Hz_per_MeV = 1.519e21   # Hz per MeV (1/hbar)
tP    = 5.391e-44      # s (Planck time)
nu_Planck = 1.0/tP     # 1.85e43 Hz  (substrate clock, 0774: 1 PCD tick / t_P)
d_fm  = 1.0
m_el  = 1408.0         # MeV (DM element = 8qCP+8eCP)
E_qq  = 66.0           # MeV (color core bond)
c_over_d = 3.0e23      # Hz (c / 1 fm)

def H_Hz(T_MeV, gstar):
    # standard radiation-era Friedmann: H = 1.66 sqrt(g*) T^2 / MPl  [MeV] -> Hz
    return 1.66*np.sqrt(gstar)*T_MeV**2/MPl * hbar_Hz_per_MeV

def gstar(T_MeV):
    # crude g*(T): ~10.75 below ~100 MeV, ~60-75 across QCD/EW
    if T_MeV < 100: return 10.75
    if T_MeV < 1000: return 61.75
    return 75.0

# vibrational attempt frequency (Arrhenius prefactor for detachment): nu ~ (1/2pi)(1/d) sqrt(2 E_bond/m_el)
def nu_vib(E_bond):
    return (1/(2*np.pi))*c_over_d*np.sqrt(2*E_bond/m_el)

def solve_kTform(E_bond, nu):
    # freeze-out (thermal contact kT_form = T_rad): nu*exp(-E_bond/kT) = H(kT)
    def f(T):
        return np.log(nu) - E_bond/T - np.log(H_Hz(T, gstar(T)))
    return brentq(f, 1e-3, 5e3)

def N_of(E_bond, kT, phi):
    return np.sqrt(phi)*np.exp(E_bond/(2*kT))

print("="*94)
print("OPEN-COSMO-DM-4: forward freeze-out kT_form and <N>  (self-consistent, thermal-contact kT_form=T_rad)")
print("="*94)
print(f"nu_Planck (1/t_P, substrate clock) = {nu_Planck:.2e} Hz")
print(f"nu_vib(E_qq=66)  (Arrhenius detach prefactor) = {nu_vib(66):.2e} Hz")
print(f"Target: N_form ~ 400-1000 (dwarf normalization, 1845/1846)\n")

for label, nu_fn in [("nu_vib (correct Arrhenius prefactor)", nu_vib),
                     ("nu_Planck (1/t_P substrate tick)", lambda E: nu_Planck)]:
    print(f"--- {label} ---")
    print(f"{'E_bond':>7}{'nu(Hz)':>11}{'kT_form':>9}{'E/kT':>7}{'<N>@phi=1e-11':>15}{'<N> range(1e-9..1e-14)':>24}")
    for nb in (1,2,4):
        Eb = nb*E_qq; nu = nu_fn(Eb)
        kT = solve_kTform(Eb, nu)
        Nmid = N_of(Eb,kT,1e-11); Nhi = N_of(Eb,kT,1e-9); Nlo = N_of(Eb,kT,1e-14)
        print(f"{Eb:>7.0f}{nu:>11.1e}{kT:>9.2f}{Eb/kT:>7.1f}{Nmid:>15.1e}   {Nlo:.1e} .. {Nhi:.1e}")
    print()

print("="*94)
print("COMPARISON: what the 1846 phi~1 assumption gave vs the physical dilute-gas phi (0881)")
print("="*94)
print(f"{'phi':>10}{'E_bond/kT_form for N=700':>26}{'implied kT_form (E_bond=66)':>28}")
for phi in (1.0, 1e-2, 1e-9, 1e-11, 1e-14):
    r = 2*np.log(700/np.sqrt(phi))
    print(f"{phi:>10.0e}{r:>26.1f}{66/r:>28.2f}")
print(" -> 1846 used phi~1 (close-packed, unphysical) => ratio~13, kT_form~5 MeV.")
print("    0881's dilute-gas phi~1e-9..1e-14 => ratio~33-46, kT_form~1.4-2.0 MeV. The target moved.")
print()

print("="*94)
print("DM-COLDER (decoupled) VARIANT: what radiation-epoch T_rad lands N=700, if kT_DM != T_rad")
print("="*94)
# if DM colder: freeze-out set by kT_DM, but H set by T_rad. N=700 needs E/kT_DM = 2 ln(700/sqrt(phi))
for phi in (1e-9,1e-11,1e-14):
    Eb=66.0; ratio = 2*np.log(700/np.sqrt(phi)); kT_DM = Eb/ratio
    # need nu*exp(-ratio)=H(T_rad) -> H = nu_vib*exp(-ratio); back out T_rad
    Hneed = nu_vib(Eb)*np.exp(-ratio)   # Hz
    # invert H(T_rad): T_rad = sqrt(Hneed / (1.66 sqrt(g) /MPl * hbar))
    def g(T): return gstar(T)
    def hf(T): return H_Hz(T,g(T))-Hneed
    try: Trad = brentq(hf,1e-3,1e6)
    except Exception: Trad=float('nan')
    print(f"  phi={phi:.0e}: N=700 => kT_DM~{kT_DM:.2f} MeV, needs T_rad~{Trad:.0f} MeV => DM/rad temp ratio ~ {kT_DM/Trad:.1e}")
print(" -> landing in-window needs DM colder than radiation by ~1e2 at the QCD epoch (an unpinned decoupling).")
