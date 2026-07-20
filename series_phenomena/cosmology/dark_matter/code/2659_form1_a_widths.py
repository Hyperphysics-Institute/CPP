#!/usr/bin/env python3
"""
PATCH 2659 -- FORM-1 Agenda A arithmetic: the zero-parameter lattice width
candidates and the exhibit-side scale checks. Pure registered-constant
arithmetic; no dynamics, no fit. Sources: d = 1.15 fm [2433 strong-SSV
registration, engine constant D]; l_unit = 0.589 fm and l_edge = l_unit/phi =
0.364 fm [SS-2 lattice grounding]; E_qq = alpha_s*hbar*c/d [1812 pin, engine
EQQ]; m = kappa_q = 132 [SF-6 pin].
"""
import numpy as np
PHI = (1 + np.sqrt(5)) / 2
AHC = 197.3
ALPHA_S = 5 / (8 * PHI)
D = 1.15
L_UNIT = AHC / 335.0          # hbar*c / Lambda_QCD per SS-2 (= 0.589 fm)
L_EDGE = L_UNIT / PHI         # 0.364 fm
EQQ = ALPHA_S * AHC / D
M = 132.0

print(f"l_unit = {L_UNIT:.4f} fm   l_edge = {L_EDGE:.4f} fm   d = {D} fm   EQQ = {EQQ:.3f} MeV")
for name, ell in (("d/l_unit", L_UNIT), ("d/l_edge", L_EDGE)):
    bd = D / ell
    om = (bd / D) * np.sqrt(2 * EQQ / M)
    print(f"  candidate beta*d = {name} = {bd:.4f}   -> omega = {om:.3f} c/fm")
print(f"  registered bracket members: beta*d = 2 (SOFT, omega 1.743), 4 (STEEP, omega 3.485)")
print(f"  2658 diagnostic chaos-onset window: omega in (2.18, 2.61) c/fm  <->  beta*d in (2.50, 3.00)")
print(f"  soft-member coincidence: |d/l_unit - 2|/2 = {abs(D/L_UNIT-2)/2*100:.1f}%")
# analytic well reach ratio (exhibit 5 scale check): b_W ~ 1/beta class
print(f"  well-forgiveness ratio soft/steep (1/beta class): {4/2:.1f}x  "
      f"[registered analytic wells 4.5D vs 2.5D = {4.5/2.5:.2f}x -- same class]")
