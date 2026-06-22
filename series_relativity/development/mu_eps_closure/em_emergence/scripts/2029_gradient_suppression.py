#!/usr/bin/env python3
"""
ChatGPT's narrowed attack (anisotropy -> LOCALITY): is the scalar channel isolated from g_ij
BEYOND leading order, for the observable R2 tests (local alpha / LPI bound)?
c07 metric: g_tt = 1 - k|SSV|_abs (scalar);  g_ij = delta_ij + k|grad SSV_net|_ij (gradient).
In a uniform region grad SSV = 0 => g_ij = delta_ij EXACTLY => scalar isolation exact.
The ONLY breaking is the gradient. Quantify its size for terrestrial atomic-clock LPI.
"""
c = 2.998e8
# Terrestrial gravity: SSV ~ Phi (Newtonian potential); gradient scale L_grad = Phi/|grad Phi|
GM = 3.986e14          # m^3/s^2 (Earth)
R  = 6.371e6           # m
Phi = GM/R             # ~ |potential| at surface (m^2/s^2)
gradPhi = GM/R**2      # = g ~ 9.8 m/s^2
L_grad = Phi/gradPhi   # scale over which SSV varies
L_atom = 1e-10         # m (atom / clock transition length scale)

ratio = L_atom/L_grad  # fractional spatial-sector (g_ij) contribution to local alpha vs the scalar effect
LPI_bound = 1e-6       # |k_alpha| atomic-clock LPI bound (conservative; tighter ~1e-7)

print(f"  Phi (SSV proxy)         ~ {Phi:.3e} m^2/s^2")
print(f"  |grad Phi| = g          ~ {gradPhi:.3f} m/s^2")
print(f"  L_grad = Phi/|gradPhi|  ~ {L_grad:.3e} m   (~ Earth radius, as expected)")
print(f"  L_atom                  ~ {L_atom:.1e} m")
print(f"  spatial-sector / scalar = L_atom/L_grad ~ {ratio:.2e}")
print(f"  LPI bound               ~ {LPI_bound:.0e}")
print(f"  orders BELOW the bound  ~ {np.log10(LPI_bound/ratio):.1f}" if False else
      f"  orders BELOW the bound  ~ {__import__('math').log10(LPI_bound/ratio):.1f}")
print()
print("  In a uniform region g_ij = delta_ij EXACTLY (c07 form) => scalar isolation is EXACT.")
print("  The leading spatial-sector contribution to local alpha is gradient-driven, suppressed by")
print(f"  L_atom/L_grad ~ {ratio:.1e} -- about 11 orders BELOW the LPI bound for terrestrial clocks.")
print("  => scalar-channel isolation holds to FAR beyond the precision R2 tests.")
print()
print("  CAVEAT (honest): (a) order-of-magnitude estimate, not a rigorous bound; (b) relies on the")
print("  c07 metric form g_ij = delta_ij + k|grad SSV| being COMPLETE for the static local-alpha sector")
print("  -- the 1110 audit flagged c07's metric map is limited for GW *radiation* (no TT modes);")
print("  completeness for the STATIC sector is plausible but not established.")
