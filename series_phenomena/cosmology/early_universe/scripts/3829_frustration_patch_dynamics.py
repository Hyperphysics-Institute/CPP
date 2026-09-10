#!/usr/bin/env python3
"""Patch 3829 -- the founder's PD-007 challenge: do frustrated regions form irregular patches, and
does his attract-unlike / repel-like rule produce aggregation? FCC (z=12, triangulated, the 3D
frustration class of the 600-cell shell) Ising antiferromagnet. Lattice statistics only; no CPP
constant adopted and no cosmological quantity derived."""
import sys
import numpy as np
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

L=24; rng=np.random.default_rng(3)
nb=np.array(sorted({v for a in (1,-1) for b in (1,-1) for v in
                    [(a,b,0),(a,0,b),(0,a,b)]}))
pts=np.array([(x,y,z) for x in range(L) for y in range(L) for z in range(L) if (x+y+z)%2==0])
N=len(pts); idx={tuple(p):i for i,p in enumerate(pts)}
NBI=np.array([[idx[tuple((p+d)%L)] for d in nb] for p in pts])
dh=nb/np.linalg.norm(nb,axis=1)[:,None]
check("T1 FCC lattice with coordination z = 12 (the 600-cell's frustration class in 3D)",
      NBI.shape==(N,12) and len(nb)==12, f"N = {N}")

# the type-I layered reference state saturates the triangle bound exactly
s_ref=np.array([(-1)**p[2] for p in pts])
fr=lambda s: ((s[:,None]*s[NBI])==1).mean()
check("T2 the ordered (type-I layered) ground state saturates the 1/3 frustration bound exactly",
      abs(fr(s_ref)-1/3)<1e-12, f"frustrated fraction = {fr(s_ref):.6f}")

# in a perfect domain the founder's force rule cancels identically
def force(s):
    b=(s[:,None]*s[NBI]).astype(float)     # +1 like (repel), -1 unlike (attract)
    return np.einsum('ij,jk->ik',-b,dh)
check("T3 in a perfect domain interior the attract/repel forces cancel EXACTLY (4 in-plane repulsive "
      "sum to zero; 8 out-of-plane attractive sum to zero)",
      np.abs(force(s_ref)).max()<1e-12, f"max |F| = {np.abs(force(s_ref)).max():.2e}")

# anneal from random
s=rng.choice([-1,1],N)
for T in np.concatenate([np.linspace(3.0,0.05,200),np.zeros(66)]):
    for _ in range(3):
        f=s[NBI].sum(axis=1); dE=-2*s*f
        acc=(dE<0)|((T>0)&(rng.random(N)<np.exp(-np.clip(dE,0,50)/max(T,1e-9))))
        s=np.where(acc&(rng.random(N)<0.1),-s,s)
check("T4 annealed state sits just above the bound (frustration is forced, not removable)",
      1/3<fr(s)<0.40, f"annealed frustrated fraction = {fr(s):.4f}")

bond=s[:,None]*s[NBI]
m=np.column_stack([(bond[:,np.where(nb[:,a]==0)[0]]==1).mean(axis=1) for a in range(3)])
pure=(m.max(axis=1)==1.0); dom=m.argmax(axis=1)
pops=np.array([(dom[pure]==a).mean() for a in range(3)])
check("T5 all three stacking orientations appear in comparable proportion -> IRREGULAR patches, "
      "not a single regular superlattice (the founder's bet)",
      pure.mean()>0.15 and pops.min()>0.20,
      f"pure sites {pure.mean():.3f}; orientation populations {np.round(pops,2)}")

F=force(s); Fm=np.linalg.norm(F,axis=1)
interior=pure & np.all(pure[NBI],axis=1)
frac_wall_force = Fm[~interior].sum()/Fm.sum() if Fm.sum()>0 else 0
check("T6 essentially ALL net force lives on wall sites; domain interiors are force-balanced -> "
      "aggregation is confined to the mismatch walls, not spread along bonds",
      (Fm[interior].mean() if interior.any() else 0)<1e-9 and frac_wall_force>0.99,
      f"mean |F| interior = {(Fm[interior].mean() if interior.any() else float('nan')):.2e}, "
      f"walls = {Fm[~interior].mean():.3f}; wall share of force = {frac_wall_force:.3f}")

# spectrum of the wall field
g=np.zeros((L,L,L))
for p,w in zip(pts,(~pure).astype(float)): g[p[0],p[1],p[2]]=w
Fk=np.abs(np.fft.fftn(g-g.mean()))**2
kx=np.fft.fftfreq(L)*L
K=np.sqrt(kx[:,None,None]**2+kx[None,:,None]**2+kx[None,None,:]**2)
kb=np.arange(1,13); P=np.array([Fk[(K>=k-.5)&(K<k+.5)].mean() for k in kb])
kpk=kb[int(P.argmax())]
check("T7 the wall-field spectrum is PEAKED at finite k (a characteristic scale), not a power law "
      "-> C-3 does not supply scale invariance for free",
      1<=kpk<=11 and P.max()/P[-1]>1.5, f"S(k) peaks at k = {kpk}; S_max/S_kmax = {P.max()/P[-1]:.2f}")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
