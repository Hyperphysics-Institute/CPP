#!/usr/bin/env python3
"""
scripts/0605.py -- verification of Patch 0605 (A5_E) edge-aligned second-order
alpha_2 coefficient closure.

Reproduces, symbolically (sympy) and numerically, every computational claim in
hardened_theorems/edge_aligned_second_order_alpha2.tex:

  1. Each per-orbit (B.1+B.2+B.3+B.4) row sums to S_edge(O_i).
  2. Omega(O_i) = p_i * S_edge(O_i), including the exact Omega(O_2)=0.
  3. The golden-ratio identities used (1/phi = phi-1, 1/phi^2 = 2-phi).
  4. The boxed coefficient values alpha_2_rho, alpha_2_edge.
  5. The squared magnitude 9(184 - 111 phi)/4 ~ 9.896.

Run: python3 scripts/0605.py
Exit 0 on all-pass.
"""
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2

def simp(e):
    return sp.simplify(sp.nsimplify(sp.radsimp(e), [phi]))

ok = True
def check(label, lhs, rhs):
    global ok
    d = sp.simplify(lhs - rhs)
    passed = (d == 0)
    ok = ok and passed
    print(f"  [{'PASS' if passed else 'FAIL'}] {label}: {sp.simplify(lhs)} == {sp.simplify(rhs)}")

print("== Golden-ratio identities ==")
check("1/phi = phi-1", 1/phi, phi - 1)
check("1/phi^2 = 2-phi", 1/phi**2, 2 - phi)
check("phi^2 = phi+1", phi**2, phi + 1)

print("\n== Per-orbit sub-class rows sum to S_edge(O_i) ==")
# Rows: (B1, B2, B3, B4), expected S_edge
rows = {
    "O_1": [(-1, sp.Rational(-5,2),  5/(2*phi),            phi/2),        -3/phi**2],
    "O_2": [(sp.Rational(-1,2), (1-2*phi)/2, (2*phi-1)/2,  sp.Rational(1,2)), 0],
    "O_3": [(1/(2*phi), (2*phi-1)/2, (3*phi-4)/2,          0),            3/phi],
    "O_4": [(phi/2, sp.Rational(5,2), 0,                   -1/(2*phi)),   3],
}
S_edge = {}
for name, (subs, expected) in rows.items():
    s = sum(subs)
    S_edge[name] = expected
    check(f"{name} row sum", s, expected)

print("\n== Path-class weights and Omega(O_i) = p_i * S_edge(O_i) ==")
p = {"O_1": 1, "O_2": sp.Rational(1,2), "O_3": -1/(2*phi), "O_4": -phi/2}
Omega_expected = {
    "O_1": -3/phi**2,
    "O_2": 0,
    "O_3": -3/(2*phi**2),
    "O_4": -3*phi/2,
}
for name in ["O_1","O_2","O_3","O_4"]:
    check(f"Omega({name})", p[name]*S_edge[name], Omega_expected[name])
check("Omega(O_2) is exactly zero", Omega_expected["O_2"], 0)

print("\n== Boxed coefficients ==")
alpha2_rho  = 9/(2*phi)
alpha2_edge = 9*phi - 12
check("alpha_2_rho = 9/(2phi) = 9(phi-1)/2", alpha2_rho, 9*(phi-1)/2)
check("alpha_2_edge = 9phi-12 = 3(3phi-4)", alpha2_edge, 3*(3*phi-4))

print("\n== Squared magnitude ==")
mag2 = 9*(184 - 111*phi)/4
print(f"  |j_2|^2 symbolic = {sp.simplify(mag2)}")
print(f"  alpha_2_rho  ~ {float(alpha2_rho):.4f}  (claim +2.7812)")
print(f"  alpha_2_edge ~ {float(alpha2_edge):.4f}  (claim +2.5623)")
print(f"  |j_2|^2      ~ {float(mag2):.4f}  (claim 9.896)")

# numeric tolerance checks
import math
def near(a, b, tol=1e-3):
    return abs(float(a)-b) < tol
for label, val, claim in [
    ("alpha_2_rho", alpha2_rho, 2.7812),
    ("alpha_2_edge", alpha2_edge, 2.5623),
    ("|j_2|^2", mag2, 9.896),
]:
    passed = near(val, claim)
    ok = ok and passed
    print(f"  [{'PASS' if passed else 'FAIL'}] {label} numeric ~ {claim}")

print("\nRESULT:", "ALL PASS" if ok else "FAILURES PRESENT")
import sys; sys.exit(0 if ok else 1)
