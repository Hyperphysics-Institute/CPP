#!/usr/bin/env python3
"""
0816_signn_geometry.py -- DESCRIPTIVE ground for "what sign(n-hat) is" on the 600-cell.
No verdict, no new claim: substantiates the existing identification FI-C-9 = sign(n-hat)
(STATUS-2/MERGE-2), the H4->I_h breaking locus (CHI-1, 0638), and the P-odd/T-even character.
"""
import numpy as np, itertools
phi=(1+np.sqrt(5))/2
def even_perms(t):
    P=[p for p in itertools.permutations(range(4))
       if sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])%2==0]
    return set(tuple(t[p[i]] for i in range(4)) for p in P)
V=set()
for i in range(4):
    for s in (1,-1): v=[0,0,0,0]; v[i]=s; V.add(tuple(v))
for s in itertools.product([0.5,-0.5],repeat=4): V.add(s)
for sg in itertools.product([1,-1],repeat=3):
    for w in even_perms([0,sg[0]*0.5,sg[1]*1/(2*phi),sg[2]*phi/2]): V.add(w)
V=np.array(sorted(V)); N=len(V)

hi=int(np.argmax(V@np.array([1.0,0,0,0]))); nhat=V[hi]      # vertex-aligned primitive direction
d=np.round(np.linalg.norm(V-nhat,axis=1),6)
print("GROUND 1 -- shells about a vertex-aligned n-hat (Reading C; the H4 -> I_h locus):")
for val in sorted(set(d)):
    cnt=int((np.abs(d-val)<1e-6).sum())
    tag = "n-hat itself" if val<1e-6 else ("antipode" if abs(val-2)<1e-6 else
          ("icosahedron (vertex figure)" if cnt==12 else ("dodecahedron" if cnt==20 else "")))
    print(f"  distance {val:7.4f} : {cnt:3d}   {tag}")
print("  two nearest shells (12 icosa @ phi^-1, 20 dodeca @ 1) = local nbhd where n-hat")
print("  breaks H4 -> H3 = I_h; CHI-1 chi=phi^-3 is their bias ratio (0638).\n")

print("GROUND 2 -- sign(n-hat) is a Z2 ORIENTATION PSEUDOSCALAR (H4/H4+ det-coset label):")
nbr=np.where(np.abs(d-d[d>1e-6].min())<1e-6)[0]
canon=nbr[np.argsort(-(V[nbr]@np.array([0,1.0,phi,phi**2])))][:4]   # FIXED ordered 4-frame (indices)
def odet(pts, origin): return int(np.sign(np.linalg.det(pts[canon]-origin)))
s_id  = odet(V, nhat)
R=np.diag([-1.0,1,1,1]); Vr=V@R.T                                   # global reflection P (det R=-1)
s_ref = odet(Vr, R@nhat)                                            # reflect the origin too (consistent)
print(f"  sign(n-hat)               = {s_id:+d}    (one Z2 bit)")
print(f"  under global reflection P = {s_ref:+d}    => {'FLIPS (P-ODD pseudoscalar)' if s_ref==-s_id else 'no flip (BUG)'}")
print(f"  no time dependence        => T-EVEN")
print("  n-hat the DIRECTION is P-even/T-even; its ORIENTATION bit (this det-sign) is the")
print("  P-odd pseudoscalar = FI-C-9. The arrow current j=(6 delta/phi^2) n-hat (DSL-3) then")
print("  carries sign(delta)*sign(n-hat): temporal arrow x spatial handedness.")
