#!/usr/bin/env python3
"""4293 -- the ZBW-lock electron: hub = core -eCP locked to the inner +eCP (pass-through ZBW, 4265), rim = outer -eCP,
the captured DP's bond holding the rim.  Equal moving inertia m per CP (4292's default, flagged).  The whole dumbbell
rotates at w about the centre of mass (CM).  Moments mu = sum q_k (x_k x v_k)/2, spin S = sum m (x_k x v_k);
the electron's relation mu = -g (e/2 m_e) S, with m_e = total inertia (binding and field energy neglected).
Units e = m = 1."""
import numpy as np
def gfac(masses,charges,pos,vel,me):
    L=np.array([mk*np.cross(x,v) for mk,x,v in zip(masses,pos,vel)])
    M=np.array([qk*np.cross(x,v)/2 for qk,x,v in zip(charges,pos,vel)])
    S=L.sum(0); mu=M.sum(0); return -mu[2]/(S[2]/(2*me)), L[:,2]/S[2]
z=np.array([0,0,1.])
print("(1) rigid hub-and-rim, hub = core + inner at one point (2 CPs), rim = 1 CP at distance R; any R, any w:")
for R,w in ((1.0,1.0),(3.0,0.2),(0.1,40.0)):
    M,m=2.0,1.0; rh=-m*R/(M+m); rr=M*R/(M+m)
    pos=[np.array([rh,0,0]),np.array([rh,0,0]),np.array([rr,0,0])]; vel=[np.cross(w*z,p) for p in pos]
    g,sh=gfac([1,1,1],[-1,+1,-1],pos,vel,3.0)
    print(f"  R = {R:4.1f}, w = {w:5.1f}:  g = {g:.6f}   spin shares core/inner/rim = {sh[0]:.4f}/{sh[1]:.4f}/{sh[2]:.4f}")
print("  -> the hub's +e and -e move together, so its magnet cancels; only the rim makes the magnet.")
print("     g = (m_e/m_rim)(L_rim/S) = ((M+m)/m)(M/(M+m)) = M/m = 2: two CPs at the hub, one on the rim.")
print("\n(2) g = M_hub/m_rim for other counts (same rigid rotor):")
for M in (1,2,3):
    rh=-1/(M+1); rr=M/(M+1); pos=[np.array([rh,0,0])]*M+[np.array([rr,0,0])]; vel=[np.cross(z,p) for p in pos]
    ch=[-1]+[0]*(M-1)+[-1] if M>1 else [0,-1]
    ch=([-1,+1]+[0]*(M-2))[:M]+[-1] if M>=2 else [0,-1]
    g,_=gfac([1]*(M+1),ch,pos,vel,float(M+1))
    print(f"  hub of {M} CP(s) (neutral), rim 1 CP:  g = {g:.4f}")
print("\n(3) the hub's own ZBW swing (core and inner separate by rho = A cos(W t) along u, W >> w), time-averaged:")
R=1.0; w=1.0; Wz=97.0
for A,u,lab in ((0.0,None,"none"),(0.1,np.array([1,0,0.]),"in plane, along the dumbbell"),(0.1,np.array([0,1,0.]),"in plane, across"),(0.1,z,"out of plane")):
    t=np.linspace(0,2*np.pi*20,400001); gs=[]; Ls=[];mus=[]
    rh=-R/3; rr=2*R/3
    Lt=np.zeros(3); mt=np.zeros(3)
    for ti in t[::50]:
        c,s=np.cos(w*ti),np.sin(w*ti); Rm=np.array([[c,-s,0],[s,c,0],[0,0,1]])
        H=Rm@np.array([rh,0,0]); VH=np.cross(w*z,H)
        if u is None: rho=np.zeros(3); rhod=np.zeros(3)
        else:
            uu=Rm@u; rho=A*np.cos(Wz*ti)*uu; rhod=-A*Wz*np.sin(Wz*ti)*uu+A*np.cos(Wz*ti)*np.cross(w*z,uu)
        P=[H-rho/2,H+rho/2,Rm@np.array([rr,0,0])]; V=[VH-rhod/2,VH+rhod/2,np.cross(w*z,P[2])]
        for qk,x,v in zip((-1,1,-1),P,V): Lt+=np.cross(x,v); mt+=qk*np.cross(x,v)/2
    g=-mt[2]/(Lt[2]/(2*3.0))
    print(f"  A = {A:.1f} R, swing {lab:30s}: g = {g:.5f}")
print("  -> a swing that turns with the dumbbell adds spin but no net magnet (g slightly below 2, second order in A/R); along z, none.")
print("\n(4) if part of the electron's mass is not in the three CPs' inertia AND carries no spin: m_e = 3m(1+eps):")
for eps in (0.0,0.001,0.00116):
    print(f"  eps = {eps:.5f}:  g = 2(1+eps) = {2*(1+eps):.5f}")
print("  (recorded, not claimed: the measured a_e = 0.00116 would mean 0.116% of the mass-energy outside the CPs.)")
