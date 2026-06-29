#!/usr/bin/env python3
"""
Patch 0898 -- Direct-electrostatic (Madelung) e-binding window-mapping.
=======================================================================
Founder geometric correction (TLA, staged verbatim in reasoning/0898.md): the e-e bond is NOT a
vdW/London residual between interpenetrating neutral eDP coats (the 0896/0897 framing). When the four
hTetras compress into a Cross-Rod element the eCPs rotate 90deg to become COPLANAR with the qCPs; a
transverse cut is a stable alternating-charge square (4 qCP inner square + alternating-polarity eCP
outer vertices). No perimeter interpenetration. => the binding is FIRST-ORDER electrostatic (Madelung),
directly computable from charge geometry, with NO polarizability / Q_stiff / OPEN-FP-SF-2-eta dependence.
This script maps E_ee = M*(alpha*hbar*c/d) against the window and shows it is in-window, not fine-tuned,
for M~1-2 and any d >~ 1 fm -- and that this RE-DERIVES 0865's fm-Coulomb-ceiling-at-window-top result.
The absolute number still needs the pinned eCP spacing d and the exact alternating-charge factor M.
"""

import numpy as np
hbarc=197.3269804; alpha=1/137.035999
coul_fm=alpha*hbarc   # 1.440 MeV*fm : first-order Coulomb energy*separation, unit charges
WIN=(0.8e-3,2.0)      # MeV
print("="*70); print("Direct-electrostatic (Madelung) e-binding: does it reach the window?"); print("="*70)
print(f"\n  first-order Coulomb scale  alpha*hbar*c = {coul_fm:.3f} MeV*fm")
print(f"  E_ee = M * (alpha*hbar*c / d),  M = O(1) alternating-charge (Madelung) factor, d = eCP spacing")
print(f"\n  d-range that lands E_ee in-window [0.8 keV, 2 MeV], for a few M:")
for M in (1.0,1.6,2.0):
    d_lo=M*coul_fm/WIN[1]; d_hi=M*coul_fm/WIN[0]
    print(f"    M={M:.1f}:  d in [{d_lo:.2f} fm, {d_hi:.0f} fm]   (E_ee= {M*coul_fm/1.0*1e3:.0f} keV @ d=1 fm ; {M*coul_fm/2.0*1e3:.0f} keV @ d=2 fm)")
print(f"\n  => for M~1-2 and ANY spacing d >~ 1 fm, E_ee is in-window. NOT fine-tuned:")
print(f"     the fm-scale Coulomb ceiling {coul_fm:.2f} MeV already sits at the window TOP, so any")
print(f"     d >~ 1 fm drops it into the window. (This is exactly 0865's 'fm-Coulomb ceiling at the")
print(f"     window top' -- which in the DIRECT-electrostatic picture is a derivation, not a coincidence.)")
print(f"\n  Ordering: E_qq = color-Madelung of the inner qCP square ~ (alpha_s/3alpha)*E_ee-scale stiffer,")
print(f"     so E_qq > E_ee falls out of the SAME geometry (inner color square vs outer electric square).")
print("="*70)
