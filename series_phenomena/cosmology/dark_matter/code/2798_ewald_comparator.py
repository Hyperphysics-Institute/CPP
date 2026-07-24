#!/usr/bin/env python3
"""Verified exact-Coulomb comparator (Patch 2798): real-space+k-space
Ewald E-field of a unit point charge with uniform neutralizing
background (jellium) on the M^3 torus. Gate-on-the-gate V-1b: must
reproduce free space |E|=1/r^2 to <2% at r in [3,6], M=48, where
image corrections are negligible."""
import math, sys
import numpy as np

def ewald_E(points,M,alpha=None,nreal=2,kmax=8):
    if alpha is None: alpha=6.0/M
    pts=np.array(points,float)
    E=np.zeros_like(pts)
    # real-space images
    for nx in range(-nreal,nreal+1):
        for ny in range(-nreal,nreal+1):
            for nz in range(-nreal,nreal+1):
                d=pts-np.array([nx,ny,nz])*M
                r=np.linalg.norm(d,axis=1)
                f=(math.erfc if False else np.vectorize(math.erfc))(alpha*r)/r**2 + 2*alpha/math.sqrt(math.pi)*np.exp(-alpha**2*r**2)/r
                E+=d*(f/r)[:,None]
    # k-space
    V=M**3
    ks=[]
    for nx in range(-kmax,kmax+1):
        for ny in range(-kmax,kmax+1):
            for nz in range(-kmax,kmax+1):
                if nx==ny==nz==0: continue
                k2n=nx*nx+ny*ny+nz*nz
                if k2n>kmax*kmax: continue
                ks.append((nx,ny,nz))
    for (nx,ny,nz) in ks:
        k=2*math.pi/M*np.array([nx,ny,nz]); k2=k@k
        phase=pts@k
        E+= (4*math.pi/V)*(k/k2)*math.exp(-k2/(4*alpha**2))*np.sin(phase)[:,None]
    return E

if __name__=="__main__":
    M=48
    # V-1b: free-space validation at small r/M, three directions
    print("== V-1b comparator validation vs free space (M=48) ==")
    worst=0.0
    for r in (3,4,5,6):
        for u in ((1,0,0),(0,1,0),(1/math.sqrt(2),1/math.sqrt(2),0)):
            p=[np.array(u)*r]
            Em=np.linalg.norm(ewald_E(p,M)[0])
            dev=abs(Em*r*r-1.0)
            worst=max(worst,dev)
    print(f"   worst |r^2*|E| - 1| over r in [3,6], 3 directions: {worst*100:.3f}% -> {'PASS' if worst<0.02 else 'FAIL'}")
    if worst>=0.02: sys.exit(1)
    # exact axis profile for the comparative gate window
    for Mv in (48,):
        rs=np.arange(6,Mv//3+1)
        pts=[(r,0,0) for r in rs]
        Es=np.linalg.norm(ewald_E(pts,Mv),axis=1)
        print(f"== exact torus-Coulomb axis profile M={Mv} ==")
        for r,e in zip(rs,Es): print(f"   r={int(r)}: |E|={e:.6e}  (r^2|E|={e*r*r:.4f})")
        co=np.polyfit(np.log(rs[2:]),np.log(Es[2:]),1)
        print(f"   global p over [{rs[2]},{rs[-1]}]: {-co[0]:.3f}")
