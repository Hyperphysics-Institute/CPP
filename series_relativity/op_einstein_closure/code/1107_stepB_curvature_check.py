#!/usr/bin/env python3
"""
1107_stepB_curvature_check.py -- c08 op:einstein arc, Step (b).

Tests the EXCESS-vs-ABSOLUTE |SSV| fork (the cheapest potential kill of the whole
CPP dark sector). c08 eq:field_eq is
    grad_l grad^l (Delta|SSV|) + F[PSR_eff, Delta|SSV|] = (8 pi G/c^4) T,
    F = 2k(Delta|SSV|)^2/(1+k Delta|SSV|)^2 * grad_l grad^l ln(1+k Delta|SSV|).
Two routes absolute |SSV| could re-enter and revive the vacuum catastrophe:
  (b1) the SOURCE term; (b2) the metric background g[PSR_eff].
If either lets a uniform Sea ground state source curvature, excess-sourcing fails and
both the CC suppression (SR-5 D2) and the DM R2 split break. NO VERDICT MOVED -- this
is the falsification-first step-(b) check, not a closure of op:einstein.
"""
import sympy as sp

print("="*64); print("(b1) source/F-term at the uniform Sea (Delta|SSV| -> 0)"); print("="*64)
k, d = sp.symbols('k Delta_SSV', positive=True)      # d = Delta|SSV| = the EXCESS
F_pref = 2*k*d**2/(1+k*d)**2
print("F prefactor at d=0 :", F_pref.subs(d, 0), "(F vanishes identically)")
print("leading order d->0 :", sp.series(F_pref, d, 0, 4).removeO(), "(pure O(d^2) excess)")
print("=> Delta|SSV|=0 => LHS = grad^2(0)+F(.,0) = 0 => uniform Sea sources nothing.")

print(); print("="*64)
print("(b2) curvature of a uniform PSR_eff background g = Omega(x)^2 eta"); print("="*64)
t, x = sp.symbols('t x'); Omega = sp.Function('Omega')(x)
eta = sp.diag(-1, 1); g = Omega**2*eta; coords = [t, x]; ginv = g.inv(); n = 2
Gamma = [[[sp.simplify(sum(ginv[l,m]*(sp.diff(g[m,i],coords[j])+sp.diff(g[m,j],coords[i])
        -sp.diff(g[i,j],coords[m])) for m in range(n))/2) for j in range(n)] for i in range(n)] for l in range(n)]
def Ric(a,b):
    s=0
    for l in range(n):
        s+=sp.diff(Gamma[l][a][b],coords[l])-sp.diff(Gamma[l][a][l],coords[b])
        for m in range(n): s+=Gamma[l][l][m]*Gamma[m][a][b]-Gamma[l][b][m]*Gamma[m][a][l]
    return sp.simplify(s)
R = sp.simplify(sum(ginv[a,b]*Ric(a,b) for a in range(n) for b in range(n)))
Oc = sp.symbols('Omega_c', positive=True)
print("R[Omega(x)] =", R)
print("R[Omega=const] =", sp.simplify(R.subs(Omega, Oc)))
print("=> uniform absolute |SSV| => flat (R=0); curvature ~ gradients of Omega = grad|SSV|.")

print(); print("="*64); print("(a-check) weak-field vacuum reduction consistency"); print("="*64)
G_,M,r = sp.symbols('G M r', positive=True); Phi=-G_*M/r
print("Laplacian(-GM/r), r>0 :", sp.simplify(sp.diff(r**2*sp.diff(Phi,r),r)/r**2), "(vacuum=0, consistent)")
print(); print("STEP (b): cheapest kill does NOT fire -- excess-sourcing holds as c08 eq is written.")
