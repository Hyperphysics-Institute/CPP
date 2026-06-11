#!/usr/bin/env python3
"""
1109_stepA_helicity_decomposition.py -- c08 op:einstein arc, Step (a) entry.

Tests whether c08's LSP content can source the GR tensor GW polarizations. The LSP is
(x_GP, t_abs, |SSV|_abs, SSV_net): field d.o.f. = one SCALAR (|SSV|_abs -> g_tt) + one
VECTOR (SSV_net -> g_ij). For a z-propagating plane wave, build the most general
symmetric spatial perturbation h_ij these sources can produce (up to gradients) and read
off the helicity-+/-2 part (h_xx - h_yy, h_xy) = the GR '+' and 'x' modes.
op:einstein NOT closed; this LOCATES the summit. NO VERDICT MOVED. Not a falsification of
c08 (its tensor modes are attributed to companion 7 sec 6, not audited here).
"""
import sympy as sp
z = sp.symbols('z')
S = sp.Function('S')(z)                                   # |SSV|_abs perturbation (scalar)
Vx, Vy, Vz = (sp.Function(n)(z) for n in ('Vx','Vy','Vz'))# SSV_net (vector)
V=[Vx,Vy,Vz]; A,B,C = sp.symbols('A B C'); d=lambda f: sp.diff(f,z)
def h_scalar(i,j):
    t = A*S*(1 if i==j else 0)
    if i==2 and j==2: t += B*d(d(S))
    return t
def h_vector(i,j):
    t=0
    if i==2: t+=d(V[j])
    if j==2: t+=d(V[i])
    return C*t/2
H = sp.Matrix(3,3, lambda i,j: sp.simplify(h_scalar(i,j)+h_vector(i,j)))
plus, cross = sp.simplify(H[0,0]-H[1,1]), sp.simplify(H[0,1])
print("helicity-2  + mode  (h_xx-h_yy) =", plus)
print("helicity-2  x mode  (h_xy)      =", cross)
print("=> both identically ZERO: scalar+vector cannot source the GR (+,x) tensor modes." if (plus==0 and cross==0) else "nonzero")
print("sourced instead: helicity-0 trace h_xx=h_yy=A S; helicity-0 long. h_zz; helicity-1 shear h_xz,h_yz.")
print("note: a vector displacement's elastic strain d_(i u_j) for a z-wave gives only h_iz")
print("      (helicity 0,+/-1) -- NEVER the transverse-plane quadrupole (helicity +/-2).")
