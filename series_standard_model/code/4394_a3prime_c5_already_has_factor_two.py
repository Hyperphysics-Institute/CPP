#!/usr/bin/env python3
"""Patch 4394 -- founder: have we looked at AP-4 and the axioms around it?  Applicable, wrong, incomplete?

Part 1: the corpus already splits the weak field in two (GR-1i Sec. 5 'factor 2'; c07 static map; GR-1b):
        the scalar broadcast |SSV|_abs sources g_tt (clocks), the net VECTOR V (AP-4's E slot, summed by the
        receiver into V_i) sources g_ij (space).  Scalar only -> half the bending; both -> full.
Part 2: heavier bound charge -> smaller bound state (Bohr a ~ 1/(m k)); muonic hydrogen as illustration.
        Near the Sun the coupling also weakens (k down 2U) and the inertia rises 3U: net -U (4393).
Part 3: the founder's three factors in GR-1i's bookkeeping.
"""
import sympy as sp
U = sp.symbols('U')
GM_c2, Rsun, rad2as = 1476.6, 6.957e8, 206264.806
def bending(gtt_coeff, gij_coeff):
    # light index n ~ 1 + (gtt_coeff + gij_coeff)/2 * U  (g_tt = -(1 - a U), g_ij = 1 + b U); deflection (a+b) GM/(c^2 b)
    return (gtt_coeff + gij_coeff)*GM_c2/Rsun*rad2as
print("Part 1: g_tt = -(1 - 2U) from the scalar; g_ij = 1 + b U from the vector channel")
for lab, b in (("scalar-only Sea (b = 0)", 0), ("scalar + vector (b = 2, GR-1b/GR-1i)", 2)):
    print(f"  {lab}: bending at the limb {bending(2, b):.3f} arcsec (measured 1.751)")
print("  -> the space half is carried by V (AP-4's E slot, receiver-summed into V_i).  GR-1i: 'a scalar-only Sea")
print("     would bend light half as much'; the LSP's vector extension was forced by this observable (GR-1 Sec. 4).")

print("\nPart 2: Bohr size a = hbar^2/(m k e^2)")
me, mmu, mp = 0.51099895, 105.6583755, 938.272
red = lambda m: m*mp/(m + mp)
print(f"  muon/electron mass {mmu/me:.1f}; reduced-mass ratio {red(mmu)/red(me):.1f} -> muonic hydrogen ~186x smaller")
print("  (at fixed coupling).  Near the Sun: 3 da = dk - dm - 2 domega = -2 - 3 + 2 = -3  -> da = -U.")
print("  With the pull UNCHANGED instead: 3 da = 0 - 3 + 2 = -1 -> da = -U/3 (not enough).")

print("\nPart 3: the founder's three factors, one bookkeeping (GR-1i's scalar/vector split)")
rows = [("PSR shrinkage ('Lorentz')", "scalar channel |SSV|_abs: g_tt, clocks (U); the first U of light's slowing"),
        ("Dipole Sea interaction", "vector channel V (net DP polarisation): g_ij, the second U; crystals 1 - U"
                                   " (with metric universality)"),
        ("DI-bit shell thickness", "Claude's placement, not derived: a strong-field modifier (third order on)")]
for a, b in rows:
    print(f"  {a:26s} -> {b}")
print("  4392's PV form reads the same effect as one K (PSR grid ~ 1/K); not an extra 2U.")
