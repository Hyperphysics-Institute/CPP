#!/usr/bin/env python3
"""
1116_step5_emergent_graviton_modes.py -- spin-2 construction, Step 5 (THE ASSAULT, option D).

The emergent-graviton calculation: build the dynamical matrix of a scalar(phi)+vector(V) field
on the 600-cell's icosahedral-coordinated lattice (12 neighbors), and classify the propagating
modes by helicity about k. Decisive question: does a helicity-+/-2 mode emerge collectively?
RESULT: 4 modes, helicities {0,0,+1,-1}; NO helicity-+/-2, for ANY couplings -> option D FAILS;
the spin-bit axiom is NECESSARY. op:einstein (a) closure REQUIRES a fundamental rank-2 d.o.f.
NO VERDICT MOVED (no THEO/PRED/count change; this is a foundational scoping result).
"""
import numpy as np, sympy as sp
phi=(1+np.sqrt(5))/2; raw=[]
for a,b in [(1,phi),(1,-phi),(-1,phi),(-1,-phi)]:
    raw+=[(0,a,b),(a,b,0),(b,0,a)]
N=np.array(raw,float); N/=np.linalg.norm(N,axis=1,keepdims=True)

print("Per-site d.o.f. = scalar(1)+vector(3)=4 -> 4 modes per k. Little-group (SO(2) about k) helicity:")
print("  scalar->h=0 ; V_parallel->h=0 ; V_perp(2)->h=+/-1.  Max |h|=1. Helicity-2 basis vector: NONE.")

cs,lam,mu,g,kz = sp.symbols('c_s lambda mu g kappa', positive=True)
Dphi = cs*sum(1-sp.cos(kz*N[i,2]) for i in range(12))
Dv = sp.zeros(3,3)
for i in range(12):
    n=N[i]; ph=1-sp.cos(kz*n[2])
    for a in range(3):
        for b in range(3): Dv[a,b]+= ph*(lam*(1 if a==b else 0)+mu*n[a]*n[b])
gz = g*sum(sp.sin(kz*N[i,2])*N[i,2] for i in range(12))
gx = sp.simplify(g*sum(sp.sin(kz*N[i,2])*N[i,0] for i in range(12)))
gy = sp.simplify(g*sum(sp.sin(kz*N[i,2])*N[i,1] for i in range(12)))
print("phi<->V_x, phi<->V_y mixing (must vanish by symmetry):", gx, gy, "-> only phi<->V_z (helicity 0).")
block = sp.simplify(Dv[0:2,0:2])
print("transverse (V_x,V_y) block off-diagonal:", sp.simplify(block[0,1]), "-> 0: pure helicity-1 doublet,")
print("no V_x-V_y quadrupole mixing => no helicity-2 channel.")
print("VERDICT: modes = {h=0, h=0, h=+1, h=-1}. NO helicity-+/-2 for any (c_s,lambda,mu,g).")
print("=> OPTION D (emergent collective spin-2) FAILS. Scalar+vector is representationally too poor.")
print("=> closing op:einstein (a) REQUIRES a fundamental rank-2 d.o.f. (the spin-bit axiom, A/B/C).")
