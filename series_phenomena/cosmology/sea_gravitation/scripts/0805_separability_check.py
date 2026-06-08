#!/usr/bin/env python3
"""
0805_separability_check.py  --  DM-2 Step 1: separability of D2 (ground-state
exclusion) from c08 Open Problem 1 (strong-field nonlinear Einstein closure).

c08 field equation:
    box(u) + F[u] = (8 pi G / c^4) T,     u := Delta|SSV|  (the EXCESS),
    F[u] = 2 k u^2 / (1 + k u)^2  *  box( ln(1 + k u) ).

Structural claims the separability argument rests on (all use only the WRITTEN
F form + the metric mapping -- never the strong-field closure / OP1):

  CHECK 1  Uniform mean Sea (u=const, incl. 0): F = 0 exactly (gradient factor).
  CHECK 2  F is CUBIC-leading in the excess amplitude: F(0)=F'(0)=F''(0)=0,
           leading term 2 k^2 u^2 u''. (Prefactor O(u^2) x box(ln) O(u).)
  CHECK 3  Linear term box(u) and the cubic F both average to ZERO for a
           zero-mean, statistically SYMMETRIC fluctuation (parity). A
           parity-breaking (skewed / non-Gaussian) fluctuation sources a
           nonzero mean -> the residual gravitating channel.
  CHECK 4  Geometry route: constant g_tt => zero curvature, OP1-independent.
"""

import sympy as sp

k = sp.symbols('k', positive=True)
x, y, z, t = sp.symbols('x y z t', real=True)
eps = sp.symbols('epsilon', positive=True)

def box1d(expr):           # structural stand-in: parity/vanishing tests are
    return sp.diff(expr, x, 2)   # operator-agnostic (derivative of const = 0)

print("="*70)
print("CHECK 1 -- uniform mean Sea: F = 0 for u = const (incl. u=0)")
for uc in [sp.Integer(0), sp.Symbol('u0', real=True)]:
    F = 2*k*uc**2/(1+k*uc)**2 * box1d(sp.log(1+k*uc))   # box of a constant = 0
    print(f"  u={uc}: F={sp.simplify(F)}  -> {'PASS' if sp.simplify(F)==0 else 'FAIL'}")

print("="*70)
print("CHECK 2 -- F is cubic-leading; leading integrand = 2 k^2 u^2 u''")
d = sp.Function('d')
u = eps*d(x)
F = 2*k*u**2/(1+k*u)**2 * sp.diff(sp.log(1+k*u), x, 2)
ser = sp.series(F, eps, 0, 5).removeO()
c0,c1,c2,c3 = (sp.simplify(ser.coeff(eps,i)) for i in range(4))
print(f"  O(e^0)={c0}  O(e^1)={c1}  O(e^2)={c2}")
print(f"  O(e^3)= {c3}")
expected = 2*k**2*d(x)**2*sp.diff(d(x),x,2)
ok2 = (c0==0 and c1==0 and c2==0 and sp.simplify(c3-expected)==0)
print(f"  matches 2 k^2 d^2 d'' and lower orders vanish -> {'PASS' if ok2 else 'FAIL'}")

print("="*70)
print("CHECK 3 -- mean source vanishes for symmetric fluctuation; survives for skewed")
# leading cubic integrand as a functional of the fluctuation profile
def cubic_avg(profile):
    integ = (2*k**2*profile**2*sp.diff(profile,x,2))
    return sp.simplify(sp.integrate(integ,(x,0,2*sp.pi))/(2*sp.pi))
def linear_avg(profile):   # box(u) term, leading order
    return sp.simplify(sp.integrate(sp.diff(profile,x,2),(x,0,2*sp.pi))/(2*sp.pi))

sym = sp.sin(x)                         # symmetric, zero-mean
skew = sp.sin(x) + sp.Rational(1,2)*sp.cos(2*x)  # zero-mean but parity-broken (skewed)
a_sym, a_skew = cubic_avg(sym), cubic_avg(skew)
l_sym, l_skew = linear_avg(sym), linear_avg(skew)
print(f"  <box(u)>  symmetric = {l_sym}   skewed = {l_skew}   (linear term: always 0)")
print(f"  <F>_cubic symmetric = {a_sym}   -> {'vanishes (PASS: parity protects)' if a_sym==0 else 'nonzero'}")
print(f"  <F>_cubic skewed    = {a_skew}   -> {'nonzero (residual channel real)' if a_skew!=0 else 'vanishes'}")
ok3 = (l_sym==0 and l_skew==0 and a_sym==0 and a_skew!=0)
print(f"  -> mean-source vanishes iff fluctuation symmetric -> {'PASS' if ok3 else 'FAIL'}")

print("="*70)
print("CHECK 4 -- geometry route: constant g_tt => zero curvature (OP1-independent)")
A = sp.Symbol('A', positive=True)
g = sp.diag(-A,1,1,1); ginv=g.inv(); co=[t,x,y,z]; n=4
Gamma=[[[sp.simplify(sum(ginv[i,l]*(sp.diff(g[l,j],co[m])+sp.diff(g[l,m],co[j])
       -sp.diff(g[j,m],co[l]) ) for l in range(n))/2) for m in range(n)]
       for j in range(n)] for i in range(n)]
allzero=all(Gamma[i][j][m]==0 for i in range(n) for j in range(n) for m in range(n))
print(f"  all Christoffels zero for constant g_tt -> {'PASS' if allzero else 'FAIL'}")

print("="*70)
print("SUMMARY")
print("  Mean uniform Sea non-gravitating from established c08 results (CHECK 1,4).")
print("  F cubic-leading (CHECK 2); linear term + cubic F both average to zero for a")
print("  symmetric zero-mean fluctuation (CHECK 3) -- so ground-state exclusion holds")
print("  WITHOUT OP1, conditional on: (a) weak-field truncation k*d<<1 at ZBW scale,")
print("  (b) statistical symmetry of the ZBW zero-point (bounded skew/non-Gaussianity).")
print("  Residual gravitation = parity-breaking part only -> the net-broadcast lemma.")
all_ok = ok2 and ok3 and allzero
print(f"\n  ALL STRUCTURAL CHECKS: {'PASS' if all_ok else 'SEE ABOVE'}")
