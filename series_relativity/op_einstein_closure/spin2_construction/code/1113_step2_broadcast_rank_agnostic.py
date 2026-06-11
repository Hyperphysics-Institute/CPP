#!/usr/bin/env python3
"""
1113_step2_broadcast_rank_agnostic.py -- spin-2 construction, Step 2 (the Q_ij broadcast law).

Two separable questions inside 'broadcast law':
 (i)  can the PCD icosahedral shell-sum PROPAGATE a rank-2 field (give Box Q = src)?  -> YES (rank-agnostic)
 (ii) does the Grid Point HAVE a quadrupole d.o.f. to broadcast?                       -> NO (scalar+vector only)
Conclusion: propagation is native once Q_ij exists; the missing piece is the d.o.f. itself,
a foundational LSP extension. op:einstein (a) NOT closed. NO VERDICT MOVED.
"""
import numpy as np, sympy as sp
phi=(1+np.sqrt(5))/2; raw=[]
for a,b in [(1,phi),(1,-phi),(-1,phi),(-1,-phi)]:
    raw+=[(0,a,b),(a,b,0),(b,0,a)]
V=np.array(raw,float); V/=np.linalg.norm(V,axis=1,keepdims=True)
print("(i) shell sum(v_i v_j) =", np.round(V.T@V,9)[0].tolist(), "= 4I -> L f = (2a^2)grad^2 f, isotropic,")
print("    component-wise => rank-agnostic: a broadcast Q_ij gets Box Q_ij = source, as 1108 for scalar/vector.")
ex=sp.Matrix([1,0,0]); ey=sp.Matrix([0,1,0]); k=sp.Matrix([0,0,1])
for nm,e in [('+',ex*ex.T-ey*ey.T),('x',ex*ey.T+ey*ex.T)]:
    print(f"(ii) helicity-2 '{nm}': traceless={sp.trace(e)==0}, transverse={sp.simplify(e*k)==sp.zeros(3,1)} -> propagates at c with Box Q=0")
print("(ii) GP LSP today = scalar(1)+vector(3); no rank-2 part. Q_ij (5) is a NEW d.o.f.,")
print("     not grad of the vector (1109). 600-cell H_g(l=2) = geometric slot (1112); carrying it = LSP extension.")
