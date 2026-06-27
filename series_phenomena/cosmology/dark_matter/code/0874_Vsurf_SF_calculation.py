#!/usr/bin/env python3
"""
Patch 0874 (THE SF-2/SF-5 calculation: V_surf, the residual eDP->spine surface well, vs kT)
==========================================================================================
The cross route's sole remaining load-bearing item (0873): is V_surf/kT <~ 0.5? Computed here
from the SF-2/SF-5 + DM-corpus inputs. Result: MARGINAL, leaning SAFE, with the deciding number
sharpened to a single substrate ratio -- and one honest correction to the 0872/0873 bound.

SF/CORPUS INPUTS (read, not invented):
  - The eDP carries NO color. A bare Sea eDP reaches the (qDP/hTetra) spine ONLY through the
    ELECTRIC van der Waals channel (it cannot use the strong color channel that gives the qDP-qDP
    residual its depth).
  - Channel decomposition (qdp_f_as_a_number): f_color/f_electric = (alpha_s/3alpha)^2.
    alpha_s = 5/(8phi) = 0.386 (SF-5); 3alpha = 0.022 -> ratio ~ 311 (188-522 over alpha_s=0.3-0.5).
  - qDP-qDP color residual: f_color ~ 0.2, V0_color = 53 MeV. E_eDP = 88 MeV, E_qDP = 264 MeV.
  - kT_amb <~ 19 keV (0860). Hard core r_c ~ 1.0 fm = the eDP COAT (native to the structure).

ELECTRIC vdW CONTACT DEPTH (the deepest the eDP residual can be, at the well bottom r=r_c):
  V0_elec = f_color*(3alpha/alpha_s)^2 * E_eDP  ~ 34-94 keV  (central ~57 keV) = ~2-5x kT_amb.
An excess eDP rests AT the well bottom (contact), so it feels ~V0_elec from the spine -- NOT a
reduced standoff (an earlier draft wrongly applied a g(s) standoff fraction; corrected here).

THE REAL SUPPRESSION IS THE DENSITY CONTRAST (= the same rho_Sea/rho_spine as 0873):
  V_surf is the NET excess over the bulk Sea. In the bulk, an eDP already sits in electric-vdW
  wells with neighbouring Sea eDPs (the Sea is a DENSE, space-filling substrate lattice). At the
  spine it trades those for wells with the spine. The NET well is
      V_surf = V0_elec * Delta,   Delta = (spine-surface vdW - ambient-Sea vdW)/V0_elec
  = the spine-vs-ambient-Sea density/vdW CONTRAST. Crucially: because the vacuum Sea is ITSELF
  dense (0873: rho_Sea/rho_spine ~ O(1), both substrate close-packing), Delta is SMALL -- the
  eDP feels nearly the same vdW at the spine as in the bulk. This is the quantitative form of
  "bulk-Sea texture, not bound mass": the spine presents little density contrast to a dense Sea.

HONEST CORRECTION to 0872/0873: vdW is INDUCED -> ALWAYS ATTRACTIVE -> the "promiscuous-edge
orientation cancellation" (cosh, 2nd-order) that 0873 used does NOT apply. The excess is
FIRST-order: m_coat/m_spine = G*(exp(V_surf/kT)-1), G~1.6-6. So the suppression must come from
Delta (density contrast), not from orientation -- and the effective safe bar is V_surf/kT <~ 0.3
(for m_coat/m_spine < 1 at G~3), tighter than the nominal 0.5.

Run: python3 0874_Vsurf_SF_calculation.py
"""
import numpy as np
alpha=1/137.036; phi=(1+5**0.5)/2; f_color=0.20; E_eDP=88.0; E_qDP=264.0; kT=19.0e-3  # MeV

print("="*88)
print("V_surf -- residual eDP->spine surface well from SF-2/SF-5; the deciding number sharpened (0874)")
print("="*88)

print("\n(A) eDP uses ONLY the electric vdW channel. Contact depth V0_elec = f_color*(3a/a_s)^2*E_eDP:")
print(f"    {'alpha_s':>8} | {'(a_s/3a)^2':>10} | {'f_elec':>9} | {'V0_elec (keV)':>13} | {'V0_elec/kT_amb':>14}")
for a_s in (0.30,0.386,0.50):
    ratio=(a_s/(3*alpha))**2; f_e=f_color/ratio; V0=f_e*E_eDP*1e3
    print(f"    {a_s:>8.3f} | {ratio:>10.0f} | {f_e:>9.2e} | {V0:>13.1f} | {V0/(kT*1e3):>14.2f}")
print("    => the deepest possible eDP residual (at contact) is ~34-94 keV ~ 2-5x kT_amb. The eDP")
print("       rests at this well bottom; the FULL contact depth is in play (no standoff reduction).")

print("\n(B) The net well is V_surf = V0_elec * Delta, Delta = spine-vs-ambient-Sea vdW/density CONTRAST")
print("    (the vacuum Sea is itself dense -> 0873's rho_Sea/rho_spine ~ O(1) -> Delta SMALL).")
print(f"    {'Delta (contrast)':>16} | {'V_surf (keV), V0=57':>19} | {'V_surf/kT_amb':>13} | {'verdict (bar ~0.3)':>18}")
V0_mid=57.0
for Delta in (0.05,0.10,0.15,0.20,0.35,0.60,1.00):
    Vs=Delta*V0_mid; r=Vs/(kT*1e3)
    v="SAFE" if r<0.3 else ("MARGINAL" if r<0.7 else "DILUTES")
    print(f"    {Delta:>16.2f} | {Vs:>19.2f} | {r:>13.2f} | {v:>18}")
print("    => SAFE needs Delta <~ 0.1-0.15 (spine surface within ~10-15% of bulk-Sea vdW). The route")
print("       lives or dies on how close the nucleated spine's local density is to the ambient Sea's.")

print("\n(C) The deciding number, restated as a density ratio: SAFE iff rho_spine/rho_Sea <~ 1.15")
print("    (Delta ~ (rho_spine-rho_Sea)/rho_Sea for vdW ~ local density). Plausibility:")
print(f"    {'rho_spine/rho_Sea':>17} | {'Delta':>7} | {'V_surf/kT':>9} | physical reading")
for ratio,note in [(1.05,"near substrate uniformity -> SAFE"),
                   (1.15,"mild nucleation -> borderline"),
                   (1.5,"compressed knot -> DILUTES"),
                   (2.5,"strongly compressed -> DILUTES")]:
    Delta=ratio-1.0; Vs=Delta*V0_mid; r=Vs/(kT*1e3)
    print(f"    {ratio:>17.2f} | {Delta:>7.2f} | {r:>9.2f} | {note}")
print("    => the corona is SAFE iff the nucleated spine is <~15% denser than the ambient vacuum Sea.")
print("       Substrate uniformity (both the dense 600-cell lattice) makes this PLAUSIBLE; a strongly")
print("       compressed knot would dilute. This is the single SF/substrate number that decides it.")

print("\n(D) Why the answer is not cleaner: the 0872/0873 orientation-cancellation does NOT apply")
print("    (vdW always attractive -> first-order excess), so Delta -- not orientation -- must do all")
print("    the suppressing, and the bar is the tighter V_surf/kT <~ 0.3. No softening to fall back on.")

print("\n"+"="*88)
print("V_surf VERDICT (Layer C, SF-grounded -- MARGINAL, leaning SAFE; NOT a clean closure): the bare")
print("Sea eDP reaches the spine only via the ELECTRIC van der Waals channel (no color), contact depth")
print("V0_elec ~ 34-94 keV ~ 2-5x kT_amb. The eDP rests at the well bottom, so the suppression cannot")
print("come from standoff NOR (corrected) from orientation cancellation -- it must come from the spine-")
print("vs-ambient-Sea DENSITY CONTRAST Delta. Because the vacuum Sea is itself a dense substrate lattice")
print("(0873: rho_Sea/rho_spine ~ O(1)), Delta is plausibly small, and the corona is SAFE iff the")
print("nucleated spine is <~15% denser than the ambient Sea (rho_spine/rho_Sea <~ 1.15). That is")
print("PLAUSIBLE under substrate uniformity but NOT established -- a strongly compressed spine would")
print("dilute. NET: the cross route's entire survival now rests on ONE sharp substrate number,")
print("rho_spine/rho_Sea <~ 1.15 -- a strong-sector / eDP-Sea packing question. Plausible, leaning safe,")
print("but the corona is NOT closed. (Reserved lemma stays unregistered.)")
print("="*88)
