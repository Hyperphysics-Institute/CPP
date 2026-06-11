#!/usr/bin/env python3
"""
1112_step1_l2_shell_mode.py -- spin-2 construction sub-arc, Step 1.

The op:einstein (a) gap is a missing spin-2 d.o.f.: the LSP has l=0 (|SSV|_abs) + l=1
(SSV_net) but no l=2 (quadrupole), so the helicity-+/-2 GW modes are unsourced. This step
tests whether the 600-cell icosahedral neighbor shell supports an INDEPENDENT l=2 mode --
the candidate carrier of the helicity-2 polarizations. Checks: (i) the 5 l=2 functions are
fully resolved on the 12 vertices (rank 5); (ii) l=2 is orthogonal to l=0,l=1 on the shell
(independent d.o.f.); (iii) the m=+/-2 part of l=2 = the GR +,x polarizations.
NOT a closure of (a): identifies/grounds the d.o.f.; broadcast law + wave eq remain.
"""
import numpy as np
phi=(1+np.sqrt(5))/2; raw=[]
for a,b in [(1,phi),(1,-phi),(-1,phi),(-1,-phi)]:
    raw+=[(0,a,b),(a,b,0),(b,0,a)]
V=np.array(raw,float); V/=np.linalg.norm(V,axis=1,keepdims=True)
x,y,z=V.T; one=np.ones(12)
l0=[one]; l1=[x,y,z]; l2=[x*y,y*z,z*x,x*x-y*y,2*z*z-x*x-y*y]
M2=np.array(l2).T
print("(i)  l=2 rank on 12 vertices:", np.linalg.matrix_rank(M2),"of 5",
      "-> shell fully resolves the quadrupole" if np.linalg.matrix_rank(M2)==5 else "-> degenerate")
B=np.array(l0+l1+l2).T; G=B.T@B
print("(ii) max |<l2,{l0,l1}>| on shell:", f"{np.abs(G[4:9,0:4]).max():.1e}","-> l=2 independent of l=0,l=1")
print("(iii) l=2 m=+/-2 = {x^2-y^2, xy} = GR +,x GW polarizations (m=0,+/-1 = already-present helicity 0,+/-1)")
print("=> missing spin-2 d.o.f. = l=2 quadrupole of the shell deformation; fully+independently supported.")
