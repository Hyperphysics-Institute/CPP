#!/usr/bin/env python3
"""
Patch 0861 (CAMPAIGN OPENER -- PCD formation dynamics of the DM ribbon/loop)
============================================================================
The make-or-break calculation 0859 opened and 0860 set goalposts for:
does PCD aggregation produce loops of N ~ 10^2-10^3 rungs at persistence
length l_p >~ loop size? This opener does NOT assert it does. It builds the
formation-kinetics framework, computes the loop-size DISTRIBUTION it predicts
*given* the two substrate inputs, and shows those two inputs COLLAPSE to a
single deciding quantity -- the 2eDP:2qDP rung-bond SSV potential -- whose
depth and angular stiffness then fix everything.

PCD -> polymer-physics bridge (the energetics, made concrete):
  * a "bond" is an SSV binding well of depth E_bond between adjacent rungs;
  * the attempt/detachment clock is the PCD cycle rate nu_PCD (Perceive-
    Compute-Displace) -- the substrate's fundamental frequency, = the nu0 of
    the 0860 lifetime estimate;
  * thermal-eDP fluctuations at the formation-epoch scale kT_form drive
    reversible rung addition/removal => an EQUILIBRIUM-POLYMERIZATION length
    distribution that freezes out when detach-rate drops below the Hubble rate.

TWO substrate inputs, ONE source:
  E_bond  = DEPTH of the rung-bond SSV well      -> length dist + lifetime + fragmentation
  l_p     = ANGULAR STIFFNESS (kappa/kT) of the well -> loop size (closure) + cross-section scaling
Both fall out of the SAME 2eDP:2qDP rung-bond SSV potential (SF-2/SF-5).
Derive that one potential and the DM picture closes as a near-prediction.

THE CONVERGENCE this file demonstrates (computed, not asserted):
  * semiflexible ring-closure (Shimada-Yamakawa) peaks the loop population at
    contour length L* ~ 3.4 l_p  =>  N* ~ 3.4 l_p/l_rung,  R* ~ 0.54 l_p;
  * requiring N* in the 0860 band [355, 2366] needs l_p ~ 100-700 fm;
  * that SAME l_p is what 0860 INDEPENDENTLY required for sigma/m ~ N.
  Two independent constraints (cross-section scaling; formation peak) point to
  ONE l_p ~ 100-700 fm. The loop-size knob is not free -- it is l_p.

Conventions inherited from the DM lane (cf. 0859/0860).
Run: python3 0861_formation_kinetics_loop_distribution.py
"""
import numpy as np

# --------------------------------------------------------------- constants
L_RUNG_FM = 1.0                  # rung spacing along the ribbon [fm]
N_LO, N_HI = 355.0, 2366.0       # 0860 N-target band (face-on .. orient-avg hoop)
R_LO_0860, R_HI_0860 = 56.0, 377.0   # 0860 R-band [fm]
LIFE_FLOOR_kT = 100.0            # 0860: E_bond >~ 100 kT_present for 14 Gyr survival

# --------------------------------------- (1) equilibrium-polymer length dist
def mean_length_vs_Ebond(Ebond_over_kTform):
    """Equilibrium (living) polymerization: <N> ~ exp(E_bond/2kT) at fixed
    activity (concentration folded into an O(1) prefactor set to 1 here).
    The distribution is Flory/exponential: P(N) ∝ exp(-N/<N>)."""
    return np.exp(0.5 * Ebond_over_kTform)

def Ebond_for_meanN(N_target):
    """Invert <N> ~ exp(E_bond/2kT_form): E_bond/kT_form = 2 ln <N>."""
    return 2.0 * np.log(N_target)

# --------------------------------------- (2) semiflexible ring closure (SY)
def J_SY_stiff(u):
    """Shimada-Yamakawa stiff-chain ring-closure J-factor shape, u = L/l_p.
    g(u) = u^-5 exp(-14.054/u + 0.246 u). Valid u <~ 6 (the relevant regime).
    Captures: bending suppression for u<1, entropic L^-3/2-like decay above,
    PEAK at u* ~ 3.4 (matches the DNA-calibrated optimal-cyclization length)."""
    return u**(-5.0) * np.exp(-14.054/u + 0.246*u)

def closure_peak_u():
    u = np.linspace(0.5, 6.0, 20000)
    g = J_SY_stiff(u)
    return u[np.argmax(g)]

# --------------------------------------- (3) loop-size population
def loop_population(L_over_lp, meanN, lp_fm):
    """P_loop(L) ∝ P_lin(L) * J_SY(L).  L in units of l_p; convert supply
    term to rung units via N = L/l_rung = (L/l_p)*(l_p/l_rung)."""
    N = L_over_lp * (lp_fm / L_RUNG_FM)
    P_lin = np.exp(-N / meanN)            # Flory supply of linear chains length N
    return P_lin * J_SY_stiff(L_over_lp)

# =====================================================================
if __name__ == "__main__":
    print("="*72)
    print(" PATCH 0861 -- PCD formation dynamics: loop-size distribution")
    print(" (campaign opener; goalposts from 0860; nothing asserted about PCD)")
    print("="*72)

    # (1) length distribution -------------------------------------------
    print("\n"+"-"*72)
    print(" (1) EQUILIBRIUM-POLYMER LENGTH: <N> ~ exp(E_bond/2kT_form)")
    print("-"*72)
    for x in [10, 14, 18, 22]:
        print(f"   E_bond/kT_form = {x:3d}  ->  <N> ~ {mean_length_vs_Ebond(x):10.1f}")
    print(f"   to reach <N> ~ 1e3 need E_bond/kT_form ~ {Ebond_for_meanN(1e3):.1f}")
    print(f"   distribution is exponential P(N) ∝ exp(-N/<N>): a BROAD population,")
    print(f"   not a delta -- consistent with a coring spread across systems.")

    # (2) closure peak ---------------------------------------------------
    print("\n"+"-"*72)
    print(" (2) SEMIFLEXIBLE RING CLOSURE peaks the loop population")
    print("-"*72)
    u_star = closure_peak_u()
    print(f"   Shimada-Yamakawa J-factor peaks at L* = {u_star:.2f} * l_p")
    print(f"   => N* = {u_star:.2f} * (l_p/l_rung),   R* = L*/(2pi) = {u_star/(2*np.pi):.3f} * l_p")
    print(f"   (matches the DNA-calibrated optimal-cyclization length ~3.4 l_p.)")
    print(f"   Loops SMALLER than ~l_p are bending-suppressed (exp); LARGER are")
    print(f"   entropy-suppressed (power law). Stiffness PICKS the loop size.")

    # (3) the l_p that lands N* in the 0860 band ------------------------
    print("\n"+"-"*72)
    print(" (3) CONVERGENCE: the l_p needed for the formation peak to land in")
    print("     the 0860 cross-section band -- vs the l_p 0860 itself required")
    print("-"*72)
    lp_lo = N_LO * L_RUNG_FM / u_star
    lp_hi = N_HI * L_RUNG_FM / u_star
    print(f"   formation peak N* in [{N_LO:.0f},{N_HI:.0f}]  =>  l_p in "
          f"[{lp_lo:.0f}, {lp_hi:.0f}] fm")
    print(f"   resulting R* = 0.54 l_p in [{0.54*lp_lo:.0f}, {0.54*lp_hi:.0f}] fm")
    print(f"   0860 cross-section R-band:        [{R_LO_0860:.0f}, {R_HI_0860:.0f}] fm")
    print(f"   0860 stiffness requirement: l_p >~ loop size (R) for sigma/m ~ N.")
    print(f"   => BOTH constraints point to l_p ~ 1e2-7e2 fm. The loop-size knob")
    print(f"      COLLAPSES onto l_p, a single substrate quantity.")

    # (3') show the actual peaked population for a representative l_p ----
    print("\n   representative loop population (l_p=300 fm, <N>=1e3):")
    Lu = np.linspace(0.6, 8.0, 400)
    P  = loop_population(Lu, meanN=1e3, lp_fm=300.0)
    Lpk = Lu[np.argmax(P)]
    print(f"      population peaks at L = {Lpk:.2f} l_p  ->  N_peak = "
          f"{Lpk*300/L_RUNG_FM:.0f} rungs,  R_peak = {Lpk*300/(2*np.pi):.0f} fm")

    # (4) two-temperature consistency with the 0860 ledger --------------
    print("\n"+"-"*72)
    print(" (4) TWO-TEMPERATURE CONSISTENCY (formation vs present/lifetime)")
    print("-"*72)
    EkT_form = Ebond_for_meanN(1e3)              # ~13.8
    ratio = LIFE_FLOOR_kT / EkT_form
    print(f"   length:   E_bond/kT_form  ~ {EkT_form:.1f}   (for <N> ~ 1e3)")
    print(f"   lifetime: E_bond/kT_present >~ {LIFE_FLOOR_kT:.0f}   (0860, 14 Gyr)")
    print(f"   => consistent IFF  kT_form / kT_present >~ {ratio:.1f}")
    print(f"      i.e. the formation bath ~{ratio:.0f}x hotter than the present")
    print(f"      substrate thermal scale -- trivially satisfied by cosmological")
    print(f"      cooling, but the absolute scales need the substrate thermal")
    print(f"      history (SF-input) to make numerical.")

    # (5) freeze-out clock ----------------------------------------------
    print("\n"+"-"*72)
    print(" (5) FREEZE-OUT: distribution locks when detach-rate < Hubble-rate")
    print("-"*72)
    print("   detach-rate per bond = nu_PCD * exp(-E_bond/kT(t)); as kT(t) falls")
    print("   the Boltzmann factor crashes and the distribution freezes. The")
    print("   freeze epoch sets WHICH kT_form is imprinted. nu_PCD (the PCD cycle")
    print("   rate) is the same attempt clock used in the 0860 lifetime floor.")
    print("   Quantitative freeze-out needs nu_PCD and kT(t): SF / substrate-")
    print("   cosmology input. Flagged, not faked.")

    print("\n"+"="*72)
    print(" VERDICT (computed, not asserted):")
    print("  * loop size is NOT a free knob: it is set by l_p via ring-closure,")
    print("    N* ~ 3.4 l_p/l_rung. ONE quantity controls it.")
    print("  * the l_p that lands N* in the 0860 band (~1e2-7e2 fm) is the SAME")
    print("    l_p 0860 needed for sigma/m ~ N. Two constraints, one answer.")
    print("  * E_bond and l_p both come from the 2eDP:2qDP rung-bond SSV well")
    print("    (depth + angular stiffness). DERIVING THAT ONE POTENTIAL is the")
    print("    make-or-break campaign. Goalposts: E_bond ~ 0.8 keV-2 MeV window")
    print("    (0860 fragmentation), l_p ~ 1e2-7e2 fm (this patch).")
    print("  * STILL OPEN: the SSV rung-bond potential itself (SF-2/SF-5). Until")
    print("    derived, the DM picture is Layer-C consistency, not prediction.")
    print("="*72)
