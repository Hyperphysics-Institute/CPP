#!/usr/bin/env python3
"""
scripts/0606.py -- verification of the one computational claim in Patch 0606
(A1_V) that is checkable here: the magnitude ratio Finding A1V-F2.

NOTE on scope: Patch 0606 CITES |alpha_1| = 6/phi^2 ~ 2.292 from Patch-0598-era
Sequence-2A scoping rather than re-deriving it from a per-orbit (B.1, B.3)
decomposition (those vertex-aligned first-order sub-class values were not in
context at patch-time). Re-derivation is OPEN-A1V-1 (Layer 4). What IS
checkable here is the ratio against the edge-aligned radial component.

Run: python3 scripts/0606.py
"""
import sympy as sp
phi = (1 + sp.sqrt(5))/2
ok = True
def check(label, lhs, rhs):
    global ok
    p = (sp.simplify(lhs - rhs) == 0); ok = ok and p
    print(f"  [{'PASS' if p else 'FAIL'}] {label}")

alpha1_V   = 6/phi**2          # vertex-aligned first-order, substrate-primitive
alpha1_Erho = 3/phi**3         # edge-aligned first-order, radial component

print("== A1V-F2: magnitude ratio = 2 phi ==")
check("|alpha_1^V| / |alpha_1^{E,rho}| = 2 phi", alpha1_V/alpha1_Erho, 2*phi)
check("alpha_1 closed forms 6/phi^2 = 6(2-phi) = 12-6phi",
      alpha1_V, 12 - 6*phi)
print(f"  alpha_1^V    ~ {float(alpha1_V):.4f}  (claim +2.292)")
print(f"  ratio 2 phi  ~ {float(2*phi):.4f}  (claim 3.236)")
print("RESULT:", "ALL PASS" if ok else "FAIL")
import sys; sys.exit(0 if ok else 1)
