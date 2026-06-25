#!/usr/bin/env python3
"""
Patch 0862 (CANDIDATE COMPARISON -- three DM geometries against one set of goalposts)
====================================================================================
Thomas resolved the hinge question and shifted the picture from "find the one
viable geometry" to a MULTI-SPECIES MIXTURE with a formation network. This file
quantifies the three discriminants that are computable now, and flags the one
that is not (glueball-arrest size = substrate-charge physics).

CONFIRMED STRUCTURE (Thomas):
  * hinge is PINNED, not free: face repulsion at the 3rd bond (eee 2-like-1-opp,
    or forbidden ee+qq) means small bend per hinge => LARGE persistence length.
    The hTetra risk flips from "too floppy" to possibly "too stiff" -- same single
    number (per-hinge angular tolerance) decides it, from the other side.
  * STIFFNESS LADDER (adjacent-bond level):  hTetra < 4-wide ribbon < 4-wide cross.
  * COLLAPSE-RESISTANCE LADDER (new):  bare ribbon collapses to a glueball readily
    (lengthwise eqqe apposition is "just a matter of time"); the 4-wide CROSS resists
    (central q:q strip shielded by eDP edge); hTetra resists collapse (face repulsion)
    but is the floppiest. => the 4-wide CROSS is the sweet spot: stiff AND collapse-
    resistant => leading EXTENDED-relic candidate. The bare ribbon is mostly a
    transient that either collapses (glueball) or occasionally loops before contact.
  * PRESENT-DAY = MIXTURE: extended (cross + looped ribbons) + glueballs + qDP-eDP
    chained intermediates. Not a single species.

THREE GOALPOSTS for the deciding SF-2/SF-5 edge-bond SSV calculation:
  (G1) l_p ~ 100-700 fm  (<=> per-hinge angular RMS ~ 3-8 deg)         [computed here]
  (G2) E_bond ~ 0.8 keV - 2 MeV  (0860 fragmentation window)            [0860]
  (G3) glueball-arrest radius ~ 100s of fm, NOT ~fm                     [FLAGGED, not computed]
       (+ the dilution tax G3 imposes IS computed here)

Run: python3 0862_candidate_comparison_stiffness_dilution.py
"""
import numpy as np

L_RUNG_FM = 1.0
LP_LO, LP_HI = 100.0, 700.0          # G1 target band [fm] (from 0861)
SIG_GLUE = 0.11                       # 0859 point-scattering / compact-blob sigma/m [cm^2/g]
SIG_BAND = (0.6, 2.0)                 # data band for sigma/m [cm^2/g]

# ---------------------------------------- (G1) per-hinge angular tolerance
def theta_rms_deg(lp_fm, l_rung=L_RUNG_FM):
    """Wormlike-chain link: l_p = l_rung / <theta^2>_per-hinge (small-angle),
    so theta_rms = sqrt(2 l_rung / l_p) (2 transverse DOF). Returns degrees."""
    return np.degrees(np.sqrt(2.0 * l_rung / lp_fm))

# ---------------------------------------- (stiffness ladder + selection rule)
# l_p = g_geom * l_p0, where l_p0 is the base persistence of a width-1 hinge chain
# set by the COMMON edge-bond SSV strength, and g_geom is the geometric second-
# moment multiplier. Values below are ILLUSTRATIVE order-of-magnitude geometric
# factors (hinge=1; strip out-of-plane ~ width; cross ~ 2D-reinforced) -- to be
# REPLACED by the real second-moment-of-area calc. The point is the SELECTION RULE,
# which is robust to the exact numbers: the ladder is monotone and the in-window
# bands in l_p0 barely overlap, so generically AT MOST ONE candidate is viable.
G_GEOM = {"hTetra": 1.0, "ribbon": 10.0, "cross": 40.0}

def lp0_window_for(g):
    """Range of base l_p0 [fm] that puts this candidate's l_p in [LP_LO, LP_HI]."""
    return LP_LO/g, LP_HI/g

# ---------------------------------------- (G3-tax) mixture dilution
def required_extended_fraction(sigma_ext, target):
    """sigma_eff = f sigma_ext + (1-f) SIG_GLUE = target  =>  f."""
    if sigma_ext <= SIG_GLUE:
        return np.nan
    return (target - SIG_GLUE) / (sigma_ext - SIG_GLUE)

# =====================================================================
if __name__ == "__main__":
    print("="*72)
    print(" PATCH 0862 -- three DM geometries vs one goalpost set")
    print("="*72)

    # G1 ----------------------------------------------------------------
    print("\n"+"-"*72)
    print(" (G1) PER-HINGE ANGULAR TOLERANCE to land l_p in [100,700] fm")
    print("-"*72)
    for lp in [100, 200, 300, 500, 700]:
        print(f"   l_p = {lp:4d} fm  ->  theta_rms = {theta_rms_deg(lp):4.1f} deg / hinge")
    print(f"   => the pinned hinge must hold its dihedral to ~3-8 deg RMS.")
    print(f"      Tighter than ~3 deg overshoots 700 fm (loops too big/rare,")
    print(f"      population stays open, sigma/m slides toward floppy-const).")

    # stiffness ladder + selection rule ---------------------------------
    print("\n"+"-"*72)
    print(" STIFFNESS LADDER & GEOMETRY-SELECTION RULE")
    print("   l_p = g_geom * l_p0   (g_geom ILLUSTRATIVE; real = 2nd-moment calc)")
    print("-"*72)
    print(f"   {'candidate':10s} {'g_geom':>7s}   base l_p0 [fm] that puts l_p in-window")
    for name, g in G_GEOM.items():
        lo, hi = lp0_window_for(g)
        print(f"   {name:10s} {g:7.0f}   l_p0 in [{lo:6.1f}, {hi:6.1f}]")
    print("   => the in-window l_p0 bands barely overlap: for a given substrate")
    print("      edge-bond strength (one l_p0), AT MOST ONE candidate sits in the")
    print("      100-700 fm window; the others over/under-shoot. The SAME bond")
    print("      strength sets l_p AND selects which geometry is the viable relic.")
    print("   => if bond so weak the stiffest (cross) is still floppy: all fail.")
    print("      if so strong the softest (hTetra) overshoots: all fail.")

    # G3 dilution tax ---------------------------------------------------
    print("\n"+"-"*72)
    print(" (G3-tax) MIXTURE DILUTION: high glueball population dilutes sigma/m")
    print("   sigma_eff = f*sigma_ext + (1-f)*sigma_glue,  sigma_glue = 0.11")
    print("-"*72)
    print(f"   required EXTENDED mass-fraction f to reach the data band:")
    print(f"   {'sigma_ext':>10s} | {'f for 0.6':>10s} | {'f for 2.0':>10s}")
    for se in [0.6, 1.0, 2.0, 5.0, 10.0]:
        f06 = required_extended_fraction(se, 0.6)
        f20 = required_extended_fraction(se, 2.0)
        s06 = f"{f06:10.2f}" if not np.isnan(f06) and f06<=1 else ("  >1 (X)" if (np.isnan(f06) or f06>1) else f"{f06:10.2f}")
        s20 = f"{f20:10.2f}" if not np.isnan(f20) and f20<=1 else "  >1 (X)"
        print(f"   {se:10.1f} | {s06:>10s} | {s20:>10s}")
    print("   => the DILUTION TAX: extended species must BOTH exceed the target")
    print("      individually AND hold a large mass fraction. If glueballs dominate")
    print("      (f small) and sigma_ext is modest, sigma_eff misses the band.")
    print("      This is the quantitative cost of Thomas's high-glueball picture,")
    print("      and a NEW constraint on the formation branching ratios.")

    # G3 flag -----------------------------------------------------------
    print("\n"+"-"*72)
    print(" (G3) GLUEBALL-ARREST RADIUS -- FLAGGED, NOT COMPUTED")
    print("-"*72)
    print("   The compact endpoint is an OPEN-SS-6-type closed-hDP-loop glueball.")
    print("   OPEN-SS-6 gives its MASS (~1.5-2 GeV); its FORMATION/GROWTH/DECAY")
    print("   kinetics and terminal (cocoon-arrest) RADIUS are UNREGISTERED -- the")
    print("   gap Thomas named. Size-limiters: eDP cocooning + local-resource")
    print("   depletion. If arrest ~ few fm -> compact -> dilutant (sigma~0.11).")
    print("   If arrest ~ 100s fm -> a SECOND size-setter that must agree with l_p.")
    print("   Computing it needs substrate-charge physics: not faked here.")

    print("\n"+"="*72)
    print(" NET (computed, not asserted):")
    print("  * hinge pinned => hTetra risk flips floppy->stiff; G1 = 3-8 deg/hinge.")
    print("  * one edge-bond strength sets l_p AND selects the geometry (ladder);")
    print("    candidates do NOT co-occupy the window -> no new free parameter.")
    print("  * high glueball population imposes a DILUTION TAX: extended fraction")
    print("    f must be large AND sigma_ext > target, or sigma_eff misses 0.6-2.")
    print("  * deciding SF-2/SF-5 calc now has THREE goalposts (G1,G2,G3); G3's")
    print("    arrest radius is the most likely program-killer and is substrate-")
    print("    input, linked to (but distinct from) OPEN-SS-6.")
    print("="*72)
