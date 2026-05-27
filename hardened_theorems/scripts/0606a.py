#!/usr/bin/env python3
"""
scripts/0606a.py -- verification of the computational claims in the THEO-DSL-8
vertex-aligned umbrella (Patch 0606a): the closed-form coefficient ratio
(F-DSL-8-4) and the second-order coefficient closed forms.

Run: python3 scripts/0606a.py
"""
import sympy as sp
phi = (1 + sp.sqrt(5))/2
ok = True
def check(label, lhs, rhs):
    global ok
    p = (sp.simplify(lhs - rhs) == 0); ok = ok and p
    print(f"  [{'PASS' if p else 'FAIL'}] {label}")

alpha1 =  6/phi**2     # Patch 0606
alpha2 = -9/phi**2     # Patch 0591

print("== F-DSL-8-4: ratio is exactly -3/2, phi-independent ==")
check("alpha_2/alpha_1 = -3/2", alpha2/alpha1, sp.Rational(-3,2))
print("== alpha_2 closed forms ==")
check("alpha_2 = -9/phi^2 = -9(2-phi) = 9phi-18", alpha2, 9*phi - 18)
print(f"  alpha_2 ~ {float(alpha2):.4f}  (claim -3.438)")
print(f"  ratio   = {sp.simplify(alpha2/alpha1)}  (claim -3/2)")
print("RESULT:", "ALL PASS" if ok else "FAIL")
import sys; sys.exit(0 if ok else 1)
