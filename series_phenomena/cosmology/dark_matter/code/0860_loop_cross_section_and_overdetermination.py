#!/usr/bin/env python3
"""
Patch 0860 (FINDING / cross-section pass for the extended-aggregate pivot)
=========================================================================
Sets the GOALPOSTS for the formation-dynamics campaign that the 0859 recompute
opened. 0859 showed the point-scattering sigma/m is ~0.11 (flat, ~5-20x too small).
The pivot: DM = extended 2eDP:2qDP charge-offset ribbons/loops, geometric
cross-section sigma/m ~ N. This file works out, properly:

  (a) the PRECISE N-target (loop size in DP-rungs) that lands sigma/m in the
      data band [0.6, 2] cm^2/g, across the stiff-hoop <-> floppy-coil range
      with orientation averaging;
  (b) the SENSITIVITY of that target to the stiffness assumption -- and the
      result that ONLY stiff (persistence length >~ loop size) hoops give BOTH
      sigma/m ~ N (a magnitude knob) AND the data-preferred velocity TREND;
  (c) the (N, E_bond) OVER-DETERMINATION LEDGER: magnitude -> N; cosmological
      lifetime -> E_bond floor; fragmentation-onset across dwarf..cluster v ->
      an E_bond window. The test is whether a single (N, E_bond) lives in all
      three boxes. We do NOT assert it does; we compute the boxes and report
      the overlap and the falsifiable condition it imposes on the ambient
      thermal-eDP scale.

NOTHING here asserts PCD dynamics produce this N. That is the make-or-break
campaign this pass is scoping. sigma_geo is an UPPER bound on transport sigma
(loops can pass through / link / deform), so every N-target below is a LOWER
bound on the true required loop size.

Conventions inherited from the DM lane (cf. code/0859): hbarc=197.327 MeV.fm,
constituent scale 264 MeV, 1 fm^2 = 1e-26 cm^2, 1 MeV/c^2 = 1.7827e-27 g.
Run: python3 0860_loop_cross_section_and_overdetermination.py
"""
import numpy as np

# ---------------------------------------------------------------- constants
HBARC   = 197.327                 # MeV.fm
FM2_CM2 = 1.0e-26                 # cm^2 per fm^2
G_PER_MEV = 1.7827e-27           # g per (MeV/c^2)
C_KMS   = 2.99792458e5           # km/s
HBAR_S  = 6.582119e-22           # MeV.s   (hbar)
T_HUBBLE_S = 4.42e17             # s  (~14 Gyr)

# ---- structural inputs (parametric; defaults stated, swap to taste) -------
ELL_FM    = 1.0     # DP-rung spacing along the ribbon [fm]  (contact/PSR scale)
W_FM      = 2.0     # ribbon width (4-CP-wide => ~2 CP-widths) [fm], edge-on only
M_RUNG    = 264.0   # mass per 2eDP:2qDP rung [MeV].  CONTINUITY choice = the
                    # 264 MeV constituent the point-scattering used. A heavier
                    # rung scales every N-target UP linearly (table printed).
SIG_LO, SIG_HI = 0.6, 2.0        # data band for sigma/m [cm^2/g]

# velocity scales for the fragmentation box
V_DWARF = 30.0      # km/s  (Fornax-class 1D dispersion ~ 11; rel ~ 2.26*sig1D)
V_CLUST = 1500.0    # km/s  (cluster-scale collision velocities)

# ------------------------------------------------ sigma/m, geometric models
def sigma_over_m(N, model, m_rung=M_RUNG, ell=ELL_FM, w=W_FM):
    """Return sigma/m [cm^2/g] for a loop/coil of N rungs.
    Loop circumference = N*ell => bounded-disk radius R = N*ell/(2*pi)."""
    R = N * ell / (2.0 * np.pi)                  # fm
    if model == "hoop_faceon":      # opaque bounded disk, face-on (MAX)
        sigma_fm2 = np.pi * R**2
    elif model == "hoop_oavg":      # Cauchy orientation avg of a flat disk = pi R^2 / 2
        sigma_fm2 = 0.5 * np.pi * R**2
    elif model == "hoop_edgeon":    # ribbon strip seen edge-on (MIN, ~const-ish)
        sigma_fm2 = 2.0 * R * w
    elif model == "coil_ideal":     # floppy ideal chain: Rg = ell*sqrt(N/6), area ~ pi Rg^2
        Rg = ell * np.sqrt(N / 6.0)
        sigma_fm2 = np.pi * Rg**2
    elif model == "coil_saw":       # self-avoiding walk: R ~ ell*N^0.588
        Rsaw = ell * N**0.588
        sigma_fm2 = np.pi * Rsaw**2
    else:
        raise ValueError(model)
    M_g = N * m_rung * G_PER_MEV                  # g
    return sigma_fm2 * FM2_CM2 / M_g

def N_for_target(sig_target, model, **kw):
    """Invert sigma/m(N)=target. Linear-in-N models invert closed-form via a probe;
    general case by monotone bisection."""
    lo, hi = 1.0, 1e9
    f = lambda N: sigma_over_m(N, model, **kw) - sig_target
    if f(lo) > 0:      # already above target at N=1 (won't happen here)
        return lo
    for _ in range(200):
        mid = np.sqrt(lo*hi)
        if f(mid) > 0: hi = mid
        else:          lo = mid
        if hi/lo < 1+1e-9: break
    return np.sqrt(lo*hi)

# --------------------------------------------------------- scaling check
def scaling_exponent(model, m_rung=M_RUNG):
    Ns = np.array([100., 1000.])
    s  = np.array([sigma_over_m(N, model, m_rung=m_rung) for N in Ns])
    return np.log(s[1]/s[0]) / np.log(Ns[1]/Ns[0])   # d ln(sigma/m)/d ln N

# --------------------------------------------------- collision energetics
def collision_KE_MeV(N, v_kms, m_rung=M_RUNG):
    """KE of a loop-loop collision in the COM frame: (1/2) mu v_rel^2,
    mu = (N m_rung)/2 for two equal loops.  Non-rel (v<<c)."""
    mu = 0.5 * N * m_rung               # MeV
    beta2 = (v_kms / C_KMS)**2
    return 0.5 * mu * beta2             # MeV

def Ebond_lifetime_floor_in_kT(N, nu0_Hz):
    """Arrhenius survival of the WHOLE loop (any one of N rungs breaking
    fragments it) for a Hubble time:
        N * nu0 * t_H * exp(-E_bond/kT_amb) <~ 1
    => E_bond/kT_amb >~ ln(N nu0 t_H).  Returns that log (the floor in kT units)."""
    return np.log(N * nu0_Hz * T_HUBBLE_S)

# =====================================================================
if __name__ == "__main__":
    np.set_printoptions(precision=3)
    print("="*72)
    print(" PATCH 0860 -- loop cross-section pass + (N, E_bond) ledger")
    print(" goalposts for the formation-dynamics campaign (0859 pivot)")
    print("="*72)
    print(f" inputs: ell={ELL_FM} fm, w={W_FM} fm, m_rung={M_RUNG} MeV, "
          f"data band sigma/m in [{SIG_LO},{SIG_HI}] cm^2/g\n")

    # (A) scaling exponents -- the load-bearing qualitative claim ----------
    print("-"*72)
    print(" (A) SCALING  d ln(sigma/m)/d ln N   [=1 => sigma/m ~ N; =0 => flat]")
    print("-"*72)
    for mdl in ["hoop_faceon","hoop_oavg","hoop_edgeon","coil_ideal","coil_saw"]:
        print(f"   {mdl:14s}  exponent = {scaling_exponent(mdl):+.3f}")
    print("   => stiff hoops: sigma/m ~ N (a real magnitude knob).")
    print("      floppy coils: exponent ~ 0 (NO knob, NO trend). Stiffness is")
    print("      not optional -- it is the thing the structure calc must deliver.")

    # (B) the N-target band ------------------------------------------------
    print("\n"+"-"*72)
    print(" (B) N-TARGET to hit the data band (loop size in DP-rungs), and R")
    print("-"*72)
    for mdl in ["hoop_faceon","hoop_oavg"]:
        Nlo = N_for_target(SIG_LO, mdl); Nhi = N_for_target(SIG_HI, mdl)
        Rlo = Nlo*ELL_FM/(2*np.pi);      Rhi = Nhi*ELL_FM/(2*np.pi)
        print(f"   {mdl:12s}:  N in [{Nlo:6.0f}, {Nhi:6.0f}]   "
              f"R in [{Rlo:5.0f}, {Rhi:5.0f}] fm")
    print("   => target loop size ~10^2-10^3 DP-rungs, R ~ 50-400 fm.")
    print("      (sigma_geo is an UPPER bound => these N are LOWER bounds;")
    print("       a transport efficiency eps<1 raises every N by 1/eps.)")

    # (B') mass sensitivity ------------------------------------------------
    print("\n   mass sensitivity (orientation-averaged hoop, N at sigma/m=1.0):")
    for mr in [264., 528., 1056.]:
        N1 = N_for_target(1.0, "hoop_oavg", m_rung=mr)
        print(f"      m_rung={mr:6.0f} MeV  ->  N(sigma/m=1) = {N1:6.0f}   "
              f"(R={N1*ELL_FM/(2*np.pi):4.0f} fm)")

    # (C) the over-determination ledger -----------------------------------
    print("\n"+"-"*72)
    print(" (C) OVER-DETERMINATION LEDGER  (does one (N,E_bond) fit all 3 boxes?)")
    print("-"*72)
    N_star = N_for_target(1.0, "hoop_oavg")          # central magnitude pick
    print(f"   box A (magnitude):  N* = {N_star:.0f}  (orient-avg hoop, sigma/m=1)")

    KE_dw = collision_KE_MeV(N_star, V_DWARF)
    KE_cl = collision_KE_MeV(N_star, V_CLUST)
    print(f"   box C (fragmentation window): a loop-loop collision deposits")
    print(f"        dwarf  (v={V_DWARF:.0f} km/s): KE = {KE_dw*1e3:8.3f} keV")
    print(f"        cluster(v={V_CLUST:.0f} km/s): KE = {KE_cl:8.3f} MeV")
    print(f"      => to fragment in clusters but NOT in dwarfs (trend rises")
    print(f"         toward dwarfs), need  E_bond in [{KE_dw*1e3:.3f} keV, {KE_cl:.3f} MeV].")

    print(f"   box B (lifetime floor): E_bond/kT_amb >~ ln(N nu0 t_H)")
    for nu0 in [1e20, 1e23]:
        floor = Ebond_lifetime_floor_in_kT(N_star, nu0)
        print(f"        nu0={nu0:.0e} Hz -> E_bond >~ {floor:5.1f} kT_amb")
    floor = Ebond_lifetime_floor_in_kT(N_star, 1e23)

    # overlap: durability floor must sit BELOW the cluster ceiling
    kT_max_eV = (KE_cl * 1e6) / floor     # MeV->eV ; E_bond<=KE_cl, E_bond>=floor*kT
    print(f"\n   OVERLAP TEST: durability wants E_bond >~ {floor:.0f} kT_amb;")
    print(f"   the fragmentation window caps E_bond <~ {KE_cl:.2f} MeV (cluster).")
    print(f"   => a (N,E_bond) lives in ALL THREE boxes  IFF the ambient thermal")
    print(f"      scale  kT_amb <~ {kT_max_eV:,.0f} eV  (~{kT_max_eV/1e3:.1f} keV).")
    print(f"      This is the FALSIFIABLE hook: the substrate thermal-eDP scale")
    print(f"      must be below ~{kT_max_eV/1e3:.0f} keV for a relic that is BOTH durable")
    print(f"      over 14 Gyr AND fragmentable at cluster velocities. = SF-input.")

    print("\n"+"="*72)
    print(" VERDICT (computed, not asserted):")
    print("  * magnitude IS reachable: N ~ 3.5e2-2.4e3 rungs (R~50-400 fm). LB.")
    print("  * sigma/m ~ N and the velocity TREND require STIFF hoops")
    print("    (persistence length >~ loop size). Floppy coils give neither.")
    print("  * one (N,E_bond) can satisfy magnitude+lifetime+trend together")
    print("    PROVIDED kT_amb is below ~tens of keV. Not a 1-knob fit -- a 3-way")
    print("    consistency test with a falsifiable thermal-scale condition.")
    print("  * STILL OPEN (make-or-break): does PCD formation dynamics PRODUCE")
    print("    loops of this size and this stiffness? That is the next campaign;")
    print("    this pass only set its goalposts.")
    print("="*72)
