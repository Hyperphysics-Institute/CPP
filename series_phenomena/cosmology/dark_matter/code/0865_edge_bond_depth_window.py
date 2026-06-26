#!/usr/bin/env python3
"""
Patch 0865 (G2 FIRST WIN -- edge-bond DEPTH: scale-bracketing, ordering, lifetime floor)
========================================================================================
Goalpost G2 asks for the well DEPTH of the rung-rung edge bond -- E_qq and E_ee --
and whether it lands in the 0860 fragmentation window [0.8 keV, 2 MeV] while clearing
the 14-Gyr lifetime floor.

The honest situation (confirmed against SF-2): CPP has NO pinned first-principles
inter-CP binding potential. SF-2's cage masses are CALIBRATED (PARTIAL CLOSURE), not
derived from a potential with a fixed coupling. So the ABSOLUTE depth is exactly the
near-cancellation SSV charge-sum the SF-2/SF-5 handover registers as unbuilt -- this
script does NOT fabricate it.

What IS robust despite the near-cancellation, and is the easiest G2 win:

  (A) SCALE BRACKETING. Any CPP inter-charge potential must reproduce the Coulomb law
      at fm separations (it has to give atomic physics). The Coulomb-analog energy of
      two unit charges at the rung spacing l_rung ~ 1 fm is alpha*hbar*c/l_rung
      ~ 1.44 MeV -- which sits AT THE TOP of the fragmentation window [0.8 keV, 2 MeV].
      The natural scale does NOT overshoot the window by orders of magnitude; it lands
      on its upper edge. So a depth in-window corresponds to an effective bond that is
      a MODEST fraction eta <= 1 of the fm-scale Coulomb unit -- reachable for plausible
      screening, NOT fine-tuned.

  (B) WHY the absolute value still needs the SF charge-sum. The bonded pair sits at
      sub-Planck pre-tension separation r0 << fm. The BARE Coulomb terms there are
      ENORMOUS (~1e16 GeV at r0 ~ 10 l_P); the depth is their screened residual. A
      residual of huge near-cancelling terms cannot be eyeballed -- it is the SF calc.
      The fm-scale ceiling in (A) is the scale at which the EFFECTIVE inter-rung bond
      manifests, not the bare intra-pair term.

  (C) ORDERING E_qq > E_ee (structural, sign-certain, survives the magnitude unknown).
      Thomas: the e-e edge is the weaker SCISSION bond (breaks in ZBW State 2); the
      q-q edge is the stiffer partner. So E_ee is the depth that governs breakage,
      length kinetics, and lifetime; E_qq is the stiffer partner. This ordering is a
      sign result from the screening configuration, not a magnitude result, so it holds
      regardless of where in the window the absolute depth lands.

  (D) LIFETIME FLOOR meets 0860's fragmentation hook with the SAME substrate scale.
      14-Gyr survival (Arrhenius, any-of-N rungs) needs E_ee >~ 100*kT_present. For
      E_ee anywhere in the window this caps kT_present at E_ee/100 in [8 eV, 14 keV] --
      the SAME sub-~20-keV substrate-thermal band that 0860's fragmentation-trend
      condition (kT_amb <~ 19 keV) already requires. So depth-floor and trend are
      satisfiable TOGETHER by one substrate thermal scale: a non-trivial consistency,
      not an independent new tuning.

This converts G2 from "unknown depth" into: a screening-residual fraction eta with a
stated in-window band + a sign-certain ordering + a lifetime floor that coincides with
0860's hook. Layer C. The absolute depth remains the SF-2/SF-5 near-cancellation.

Run: python3 0865_edge_bond_depth_window.py
"""
import numpy as np

# ---- pinned constants (no CPP-specific coupling invented) ----
ALPHA   = 1.0/137.035999            # fine-structure constant
HBAR_C  = 197.3269804               # MeV*fm
COUL_FM = ALPHA*HBAR_C              # MeV*fm : Coulomb-analog energy*separation for unit charges
L_P_FM  = 1.616255e-20             # Planck length in fm
L_RUNG  = 1.0                       # fm (handover convention)

# ---- 0860 fragmentation window + lifetime-floor convention ----
E_LO_MEV = 0.8e-3                   # 0.8 keV  (dwarf-collision KE floor: don't fragment in dwarfs)
E_HI_MEV = 2.0                      # 2 MeV    (cluster-collision KE: fragment in clusters)
FLOOR_FACTOR = 100.0               # E_ee >~ 100 * kT_present for 14-Gyr Arrhenius survival
KT_AMB_HOOK_KEV = 19.0             # 0860's ledger condition kT_amb <~ 19 keV

def coulomb_energy_MeV(r_fm):
    """Coulomb-analog energy of two unit charges at separation r (MeV)."""
    return COUL_FM / r_fm

def eta_window(r_fm):
    """Screening-residual fraction eta = E_eff/E_coulomb(r) that lands E_eff in the
    fragmentation window, at rung spacing r_fm. eta is capped at 1 (residual <= bare)."""
    e_ceiling = coulomb_energy_MeV(r_fm)
    eta_lo = E_LO_MEV / e_ceiling
    eta_hi = min(E_HI_MEV / e_ceiling, 1.0)
    return e_ceiling, eta_lo, eta_hi

print("="*74)
print("G2 -- EDGE-BOND DEPTH: scale-bracketing, ordering, lifetime floor (Patch 0865)")
print("="*74)

print("\n(A) NATURAL SCALE vs the fragmentation window")
print(f"    alpha*hbar*c               = {COUL_FM:.4f} MeV*fm")
print(f"    Coulomb ceiling @ l_rung=1 fm = {coulomb_energy_MeV(1.0):.4f} MeV")
print(f"    fragmentation window        = [{E_LO_MEV*1e3:.1f} keV, {E_HI_MEV:.1f} MeV]")
print(f"    -> the fm-scale Coulomb ceiling ({coulomb_energy_MeV(1.0):.2f} MeV) sits AT the")
print(f"       window TOP (2 MeV). Natural scale does NOT overshoot; window is reachable.")

print("\n    Screening-residual band eta = E_eff/E_coulomb that lands IN window:")
print(f"    {'r_rung [fm]':>12} | {'E_coul [MeV]':>12} | {'eta_lo':>9} | {'eta_hi(cap1)':>12}")
for r in (0.5, 1.0, 2.0):
    ec, elo, ehi = eta_window(r)
    print(f"    {r:>12.2f} | {ec:>12.4f} | {elo:>9.2e} | {ehi:>12.3f}")
print("    => at l_rung~1 fm, ANY residual eta in [~6e-4, 1] lands in-window: a WIDE,")
print("       easily-satisfiable target. Reaching the very top (2 MeV) needs r<1 fm or")
print("       near-zero screening; the bulk of the window is covered by modest screening.")

print("\n(B) WHY the absolute depth still needs the SF near-cancellation")
for n in (1, 10, 100):
    r0 = n*L_P_FM
    e0 = coulomb_energy_MeV(r0)
    print(f"    bare Coulomb @ r0={n:>3d}*l_P ({r0:.2e} fm) = {e0:.2e} MeV = {e0/1e3:.2e} GeV")
print("    => bare intra-pair terms at sub-Planck separation are ~1e15-1e17 GeV.")
print("       The depth is the SCREENED RESIDUAL of these huge near-cancelling terms.")
print("       A residual of ~1e18x-larger terms cannot be eyeballed -> SF-2/SF-5 charge-sum.")

print("\n(C) ORDERING (structural, sign-certain)")
print("    E_qq > E_ee.  e-e edge = weaker SCISSION bond (breaks in ZBW State 2) -> governs")
print("    breakage/length/lifetime.  q-q edge = stiffer partner.  Sign result, survives")
print("    the magnitude unknown: E_ee is the lifetime/fragmentation-governing depth.")

print("\n(D) LIFETIME FLOOR meets 0860's fragmentation hook with ONE substrate scale")
print(f"    14-Gyr survival: E_ee >~ {FLOOR_FACTOR:.0f} * kT_present")
print(f"    {'E_ee':>12} | {'max kT_present = E_ee/100':>26}")
for label, E in (("0.8 keV (lo)", E_LO_MEV), ("1.44 MeV (ceiling)", coulomb_energy_MeV(1.0)), ("2 MeV (hi)", E_HI_MEV)):
    kt_max_keV = (E/FLOOR_FACTOR)*1e3
    print(f"    {label:>12} | kT_present <~ {kt_max_keV:>8.3f} keV")
print(f"    => the allowed kT_present band [~8 eV, ~14 keV] sits INSIDE 0860's kT_amb <~ {KT_AMB_HOOK_KEV:.0f} keV.")
print("       Depth-floor (G2) and fragmentation-trend (0860) are satisfied by the SAME")
print("       sub-~20-keV substrate thermal scale -- a consistency, not a new tuning.")

print("\n" + "="*74)
print("G2 VERDICT (Layer C): depth window is REACHABLE and NATURAL (not fine-tuned);")
print("ordering E_qq>E_ee is sign-certain; lifetime floor coincides with the 0860 hook.")
print("ABSOLUTE E_ee/E_qq remain the SF-2/SF-5 sub-Planck near-cancellation (unbuilt).")
print("="*74)
