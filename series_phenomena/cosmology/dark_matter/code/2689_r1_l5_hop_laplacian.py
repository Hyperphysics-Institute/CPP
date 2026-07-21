#!/usr/bin/env python3
"""FA-SG-R1 leg L5 (Patch 2689): OPTIONAL J6 hop-Laplacian alternative
assembly -- a NEW pre-registered branch (Grok's adopted ruling), run because
the [ADJ] trigger fired: legs L1-L4 left a live representation-dependence
question (J3-REVISE showed the scale normalization-sensitive; the L2
committed consistency test failed), so whether the staggered-exponential
structure is a property of ANY screened z=12 lattice operator or of the
dense 1/r multiple-scattering assembly specifically is live.

Assembly (zero free parameters, all inputs frozen upstream): nearest-
neighbor hop (graph) Laplacian on the z=12 edge set,
  (Delta f)_i = sum_{j~i} (f_j - f_i),
whose continuum limit on any z=12 Barlow packing is Delta f -> 2 a^2
Lap f (isotropy of the 12-shell). The screened equation (-Lap + kappa^2)
phi = s discretizes to
  A phi = s,  A = -Delta + 2 (kappa a)^2 I,  kappa a = 2  ->  A = -Delta + 8I.
Source: unit at the central site. Frozen classes (charter SS2 R1-L5):
J6-CONCORD (staggered + exponential + l compatible with the joint band
[0.0836, 0.0956] fm) / J6-DIVERGE (materially different structure or scale;
adverse to neither branch by itself per the new-branch ruling).

Analytic expectations, stated pre-run: A is an M-matrix (positive diagonal,
non-positive off-diagonal, diagonally dominant), hence A^{-1} >= 0
elementwise (Perron): the response is strictly POSITIVE -- no staggering is
possible in this assembly. Decay from the lattice dispersion along [001]:
4 + 8 cosh(q/sqrt2) = 12 + 2(kappa a)^2 -> cosh(q/sqrt2) = 2 ->
q = sqrt2 * arccosh(2) / a -> l_hop = a/q ~ 0.537 a ~ 0.195 fm.
"""
import math, numpy as np
from scipy.spatial import cKDTree

PHI=(1+math.sqrt(5))/2; A_=0.589/PHI; kappa=2.0/A_
q=math.sqrt(2.0)*math.acosh(2.0)
print(f"analytic dispersion prediction: q = sqrt2*arccosh(2)/a = {q:.4f}/a -> "
      f"l_hop = {A_/q:.4f} fm ; small-kappa (continuum) limit l = 1/kappa = {A_/2:.4f} fm")

def fcc_ball(R):
    pts=[]
    for i in range(-2*R,2*R+1):
        for j in range(-2*R,2*R+1):
            for k in range(-2*R,2*R+1):
                if (i+j+k)%2==0:
                    x=np.array([i,j,k])/math.sqrt(2.0)
                    if np.linalg.norm(x)<=R: pts.append(x)
    return np.array(pts)
def layered_ball(R,seq):
    dz=math.sqrt(2.0/3.0)
    offs=[np.array([0.0,0.0]),np.array([0.5,math.sqrt(3)/6]),np.array([1.0,math.sqrt(3)/3])]
    e1=np.array([1.0,0.0]); e2=np.array([0.5,math.sqrt(3)/2])
    pts=[]; M=int(R/dz)+2; K=int(R)+3
    for m in range(-M,M+1):
        z=m*dz; o=offs[seq[m]]
        for p in range(-2*K,2*K+1):
            for qq in range(-2*K,2*K+1):
                xy=p*e1+qq*e2+o
                if xy@xy+z*z<=R*R+1e-9: pts.append([xy[0],xy[1],z])
    return np.array(pts)

for name,P_nn in (("FCC R=9", fcc_ball(9)),
                  ("HCP R=9", layered_ball(9,{m:m%2 for m in range(-14,15)}))):
    P=P_nn*A_
    T=cKDTree(P)
    pairs=T.query_pairs(A_*1.001,output_type='ndarray')
    N=len(P)
    L=np.zeros((N,N))
    for a,b in pairs:
        L[a,b]=L[b,a]=1.0
    deg=L.sum(1)
    Aop=np.diag(deg)+8.0*np.eye(N)-L      # -Delta + 2(kappa a)^2
    src=int(np.argmin(np.linalg.norm(P-P.mean(0),axis=1)))
    s=np.zeros(N); s[src]=1.0
    phi=np.linalg.solve(Aop,s)
    r0=np.linalg.norm(P-P[src],axis=1)
    m=r0>1e-9
    negfrac=(phi[m]<0).mean()
    minphi=phi[m].min()
    # envelope on bin-mean |phi|*r
    bins=np.arange(0.3,2.4,0.05); rc,fv=[],[]
    for b in bins:
        mm=(r0>=b)&(r0<b+0.05)
        if mm.sum()>=3: rc.append(r0[mm].mean()); fv.append(np.abs(phi[mm]).mean())
    rc,fv=np.array(rc),np.array(fv)
    out=[]
    for lo,hi in [(0.45,1.3),(0.55,1.6),(0.7,1.8)]:
        w=(rc>=lo)&(rc<=hi)
        c=np.polyfit(rc[w],np.log(fv[w]*rc[w]),1)
        y=np.log(fv[w]*rc[w]); yh=np.polyval(c,rc[w])
        r2=1-np.sum((y-yh)**2)/np.sum((y-y.mean())**2)
        out.append((-1.0/c[0],r2))
    ls=np.array([o[0] for o in out])
    print(f"\n{name}: N={N}  interior degree check mode={int(np.bincount(deg.astype(int)).argmax())}")
    print(f"  positivity: min response = {minphi:.3e} ; negative-site fraction = {negfrac:.3f} "
          f"-> {'NO STAGGERING (M-matrix positivity confirmed)' if negfrac==0 else 'staggered'}")
    for (l,r2),(lo,hi) in zip(out,[(0.45,1.3),(0.55,1.6),(0.7,1.8)]):
        print(f"  window {lo:.2f}-{hi:.2f}: l = {l:.4f} fm (R2={r2:.4f})")
    print(f"  l_hop = {ls.mean():.4f} +/- {ls.std():.4f} fm vs analytic {A_/q:.4f} fm "
          f"vs joint band [0.0836, 0.0956] fm")

print("\nVERDICT (frozen classes): J6-DIVERGE -- the hop-Laplacian assembly yields")
print("NO sign staggering (elementwise-positive resolvent, M-matrix/Perron; confirmed")
print("numerically) and a materially different scale (~0.19 fm ~ 2x the joint band).")
print("Per the new-branch ruling this is a representation-dependence finding in its")
print("own right, adverse to neither branch by itself: the staggered exponential at")
print("l = 1/(2 kappa) is a property of the dense 1/r multiple-scattering assembly")
print("specifically, arena-independent WITHIN that assembly (L1), not of every")
print("screened z=12 lattice operator.")
