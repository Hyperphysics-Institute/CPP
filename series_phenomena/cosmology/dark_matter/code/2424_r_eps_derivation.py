import numpy as np
# r   = l_p/l_rung   = kappa_theta / kT_form     (0863: l_p/l_rung = kappa_theta/kT)
# eps = E_bond/kT_form
# Both carry 1/kT_form -> the DECIDING ratio is kT_form-independent:
#     r/eps = kappa_theta / E_bond   (hinge stiffness-to-depth ratio; == N_stab/c_eff)
# From 2423: DD-survival (population peak at N>=8) needs r/eps >~ 0.43; central 0.345.

r_c, eps_c = 10.25, 29.7
r_over_eps_central = r_c/eps_c
survive_thresh = 0.43              # from the 2423 consistent DD-survival scan
kT_form = 16.5                     # keV (Patch 1873; rod-era anchor, ring-era caveat noted)
l_rung = 1.0                       # fm (registered)

print("REDUCTION: r and eps both -> the 2eDP:2qDP rung-bond SSV potential")
print("-"*64)
print(f"  r   = l_p/l_rung   = kappa_theta / kT_form   (l_rung = {l_rung} fm, pinned)")
print(f"  eps = E_bond/kT_form")
print(f"  kT_form ~ {kT_form} keV (registered, rod-era anchor)")
print()
print("  DECIDING ratio (kT_form cancels):  r/eps = kappa_theta / E_bond")
print(f"    central (registered): r/eps = {r_over_eps_central:.3f}")
print(f"    DD-survival threshold:  r/eps >= {survive_thresh}")
print(f"    -> central {'CLEARS' if r_over_eps_central>=survive_thresh else 'FAILS (below threshold)'} "
      f"by x{survive_thresh/r_over_eps_central:.2f}")
print()
# absolute scales (need kT_form)
kappa_c = r_c*kT_form; Ebond_c = eps_c*kT_form
print("  Absolute scales (using kT_form):")
print(f"    kappa_theta ~ r*kT_form   = {kappa_c:.0f} keV   (hinge angular stiffness)")
print(f"    E_bond      ~ eps*kT_form = {Ebond_c:.0f} keV   (rung-bond SSV well depth)")
print(f"    both inside 0860 fragmentation window [0.8 keV, 2 MeV] and 1858 E_c~0.2-0.3 MeV")
print()
kappa_need = survive_thresh*Ebond_c
Ebond_need = kappa_c/survive_thresh
print("  For survival (r/eps >= 0.43), the rung-bond SSV potential must give:")
print(f"    kappa_theta >= {kappa_need:.0f} keV  (>~25% stiffer than central {kappa_c:.0f}), OR")
print(f"    E_bond      <= {Ebond_need:.0f} keV  (>~25% shallower than central {Ebond_c:.0f})")
print()
print("  Qualitative lean: l_rung/R_s = 1/25.42 = 0.039 << 1 -> the rung bond is")
print("  NEARLY UNSCREENED Coulomb at its own scale, which favors STIFFER wells")
print("  (higher kappa_theta/E_bond) -- mildly toward survival. But 0863 warns")
print("  kappa_theta is a near-cancellation (like-charge repulsion minus screened")
print("  opposite-charge) whose magnitude cannot be eyeballed: needs the SSV charge-sum.")
print("-"*64)
print("RESULT: r and eps do not pin to a verdict from registered constants alone --")
print("they both reduce to ONE owed strong-sector number, the hinge stiffness-to-depth")
print("ratio kappa_theta/E_bond of the 2eDP:2qDP rung-bond SSV potential. Survival needs")
print(">= 0.43 (central 0.345). This IS the 'make-or-break' flagged at 0861/0863 -- now")
print("sharpened to a single numeric target that decides the whole DM candidate.")
