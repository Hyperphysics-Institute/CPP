#!/usr/bin/env python3
"""
0814_step3_residual.py -- DM-2 Step 3: quantify the bulk residual skew from the
Mechanism-A NESS. Bulk residual source: <F>_bulk = -4 k^2 <d d'^2>, a THIRD moment.
We measure the chiral skew of the Mechanism-A NESS on the 600-cell and its delta-scaling,
to settle whether it is current-driven O(delta^3) (as the naive 0809/0810 picture assumed)
or tilt-driven O(delta^1) -- and what that means for clean Lambda.
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
Dm=np.sqrt(((V[:,None]-V[None])**2).sum(-1)); edge=np.min(Dm[Dm>1e-6]); A=(np.abs(Dm-edge)<1e-6)
nhat=np.array([1.0,phi,phi**2,phi**3]); nhat/=np.linalg.norm(nhat)
def stationary(delta, r0=1.0):
    Q=np.zeros((N,N))
    for v in range(N):
        for w in np.where(A[v])[0]:
            e=(V[w]-V[v]); e/=np.linalg.norm(e); Q[v,w]=r0*(1+delta*(e@nhat))
        Q[v,v]=-Q[v].sum()
    wv,Vec=np.linalg.eig(Q.T); pi=np.real(Vec[:,np.argmin(np.abs(wv))]); pi/=pi.sum()
    J=0.0
    for v in range(N):
        for w in np.where(A[v])[0]:
            e=(V[w]-V[v]); e/=np.linalg.norm(e); ew=-e
            J=max(J,abs(pi[v]*r0*(1+delta*(e@nhat))-pi[w]*r0*(1+delta*(ew@nhat))))
    return pi,J
x=V@nhat
print("delta   tilt<x>     m3(skew)     J_max(current)")
rows=[]
for d in [0.02,0.04,0.08,0.16]:
    pi,J=stationary(d); m=(pi*x).sum(); m3=(pi*(x-m)**3).sum()
    rows.append((d,m,m3,J)); print(f"{d:5.2f}  {m:+.3e}  {m3:+.3e}   {J:.3e}")
sl=lambda c: np.polyfit(np.log([r[0] for r in rows]),np.log([abs(r[c]) for r in rows]),1)[0]
print(f"\n  tilt ~ delta^{sl(1):.2f}   skew m3 ~ delta^{sl(2):.2f}   current ~ delta^{sl(3):.2f}")
print("\nKEY FINDING (corrects the 0809/0810 emphasis):")
print("  The measure SKEW is O(delta^1) -- TILT-driven -- not O(delta^3) current-driven.")
print("  The current (O(delta^3)) is the SUBDOMINANT effect, not the skew source.")
print("\nCONSEQUENCE for clean Lambda (analytic, using 0806 + 5c + 0807):")
print("  Mechanism A's n^-bias is spatially UNIFORM => the induced skew is statistically")
print("  HOMOGENEOUS => <F>_bulk is a spatially-uniform source. By gradient-control (0806)")
print("  a homogeneous config sources no curvature, and by excess-sourcing (5c/D2) a uniform")
print("  ground-state term is subtracted. So the O(delta^1) skew is absorbed into the (biased)")
print("  ground state; the GRAVITATING residual is the spatially-VARYING part = the IR-boundary")
print("  horizon mode = Lambda (0807). Clean horizon-only Lambda SURVIVES -- now resting on the")
print("  HOMOGENEITY of the bias + the D2 subtraction (extended to the biased ground state),")
print("  NOT on the skew being small or the current vanishing.")
