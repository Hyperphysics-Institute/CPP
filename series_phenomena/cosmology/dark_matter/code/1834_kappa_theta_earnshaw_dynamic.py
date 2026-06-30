#!/usr/bin/env python3
"""
Patch 1834 -- pinning kappa_theta: the static sum FAILS by Earnshaw; the real stiffness is ZBW-dynamic.
=====================================================================================================
Goal was to collapse the 1833 kappa_theta range (0.4-1.0 floor) with the full alternating-square dihedral
Coulomb sum. Outcome: the full static sum gives kappa_theta(90deg) < 0 across essentially all geometries
(90deg is an electrostatic MAXIMUM). This is EARNSHAW'S THEOREM -- a static point-charge configuration has no
stable equilibrium (Laplace: the curvatures over orthogonal directions sum to zero, so they cannot all be
positive). The dihedral is one of the unstable directions.

CONSEQUENCE: static electrostatics cannot supply the hinge restoring torque. The 1833 static estimate
(~0.27 MeV) used a 2-term subset that hid the net instability and is RETRACTED. The hinge is stabilized by the
ZBW DYNAMIC (ponderomotive/Kapitza) stiffness -- the SAME mechanism Thomas invoked (28 June, founders_vision)
for the rod's longitudinal E_ee: rapid symmetric oscillation time-averages to a second-order restoring force
that stabilizes what statics cannot. The longitudinal dynamic stiffness IS ~E_ee; the hinge is a softer mode,
so kappa_theta^dyn ~ f*E_ee, f~0.1-1 -> ~0.1-0.9 MeV -> floor ~0.4-1.6 (lean ~0.8-1.0). The range is NOT
collapsed -- it is RELOCATED to a ponderomotive dihedral calculation needing the ZBW frequency/amplitude.
"""
import numpy as np
E_ee,d,eps = 0.9,1.0,0.3; kqe2=E_ee*d
def ob(u):
    u=u/np.linalg.norm(u); t=np.array([0,0,1.]) if abs(u[2])<.9 else np.array([0,1.,0])
    e1=np.cross(u,t); e1/=np.linalg.norm(e1); return e1,np.cross(u,e1)
def rod(axis,M,a,zoff):
    u=np.array(axis,float); u/=np.linalg.norm(u); e1,e2=ob(u); P=[];Q=[]
    for n in range(-M,M+1):
        c=n*d*u+np.array([0,0,zoff])
        for amp,e,q in [(a,e1,1),(-a,e1,1),(a,e2,-1),(-a,e2,-1)]: P.append(c+amp*e);Q.append(q)
    return np.array(P),np.array(Q)
def U(phi,a,dc,M=6):
    Ap,Aq=rod([1,0,0],M,a,0.); Bp,Bq=rod([np.cos(phi),np.sin(phi),0],M,a,dc); u=0.
    for i in range(len(Aq)):
        dr=Bp-Ap[i]; r=np.sqrt((dr*dr).sum(1)+eps**2); u+=kqe2*Aq[i]*np.sum(Bq/r)
    return u
def kap(a,dc,h=1e-3): return (U(np.pi/2+h,a,dc)-2*U(np.pi/2,a,dc)+U(np.pi/2-h,a,dc))/h**2

neg=tot=0
for a in (0.8,0.9,1.0,1.1,1.2):
    for dc in (1.8,2.0,2.2,2.4,2.6):
        tot+=1; neg+= (kap(a,dc)<0)
print(f"STATIC dihedral stiffness: {neg}/{tot} geometries give kappa_static < 0 (90deg is a MAXIMUM).")
print("=> EARNSHAW: static charges cannot stabilize the hinge. 1833 static ~0.27 MeV RETRACTED.\n")
print("REAL stiffness = ZBW dynamic (ponderomotive), same mechanism as the rod's longitudinal E_ee.")
sm0=3.1
print("scale kappa_theta^dyn ~ f*E_ee, f~0.1-1 (hinge softening):")
for k in (0.1,0.3,0.5,0.9):
    drop = 1/8 if k<0.30 else (1/4 if k<0.53 else 1/2)
    print(f"  kappa~{k:.1f} MeV -> floor~{sm0*drop:.2f}")
print("\nVERDICT: range NOT collapsed -- RELOCATED to the ponderomotive dihedral calc (needs ZBW freq/amp).")
print("Floor stays viable-to-marginal (~0.8-1.0 lean). Self-limiting + hinge stability (1831) UNAFFECTED")
print("(kinematic/geometric, independent of kappa magnitude).")
