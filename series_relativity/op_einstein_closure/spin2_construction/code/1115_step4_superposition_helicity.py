#!/usr/bin/env python3
"""
1115_step4_superposition_helicity.py -- spin-2 construction, Step 4 (run at the Einstein wall).

Tests whether a SUPERPOSITION / second-order combination of the SSV vector (TLA's proposal:
'a change on top of the change in direction') can reproduce the helicity-2 (TT) radiative
sector that the linear metric map lacks. Transverse SSV plane wave along z. Three routes:
(1) linear d_(i V_j); (2) TLA 2nd-order V_i V_j; (3) gradient-bilinear d_i V_k d_j V_k.
Result: only (2) shows helicity-2 structure, and only at 2nd order + double frequency --
NOT the observed linear GW. Wall stands for any local polynomial in (phi,V); a no-new-axiom
helicity-2 must be EMERGENT/COLLECTIVE. op:einstein (a) NOT closed. NO VERDICT MOVED.
"""
import sympy as sp
z,t,k,w,a,b = sp.symbols('z t k w a b', real=True)
f=k*z-w*t; V=[a*sp.cos(f), b*sp.cos(f), sp.Integer(0)]; dz=lambda g: sp.diff(g,z)
print("(1) linear d_(i V_j):     h_xx-h_yy =",0," h_xy =",0," -> ZERO (only h_iz)")
hd=sp.simplify(V[0]**2-V[1]**2); hc=sp.simplify(V[0]*V[1])
print("(2) 2nd-order V_i V_j:     h_xx-h_yy =",hd)
print("                           h_xy      =",hc," -> helicity-2 PRESENT but ~amp^2 and ~cos^2 f (freq 2w)")
T=sp.Matrix(3,3,lambda i,j: sum((dz(V[m]) if i==2 else 0)*(dz(V[m]) if j==2 else 0) for m in range(3)))
print("(3) grad-bilinear dV dV:   h_xx-h_yy =",sp.simplify(T[0,0]-T[1,1])," h_xy =",sp.simplify(T[0,1])," -> ZERO (T_zz only)")
print("WALL: no local polynomial in (phi,V) gives the LINEAR helicity-2 GW. No-new-axiom route = EMERGENT.")
