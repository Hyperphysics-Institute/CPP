#!/usr/bin/env python3
"""Computation #2 (Patch 2462) -- the registry priced BOTH WAYS in one bond model
(H2/Q5 closure). Axial same-corner qCP nearest-neighbor bonds (4/junction; rod 15
junctions open, ring 16 closed). Bond forms: harmonic k=2E_qq/s0^2 (= the registered
2443 -A/r+K/r^2 curvature at its own minimum -- gate-grepped) + Morse a=1/s0 (same
curvature, anharmonicity sensitivity; stiffer on the compressed inner edge). TWO s0
references, both run per the commission: (i) s0=1.15 straight-registry (the ring pays
the inner-edge compression, H2) vs (ii) s0=ring-native lengths (the ring is the
REGISTERED native structure; the rod pays instead). E_qq mapped {40,66,100,170}.
Mode curvatures by exact finite difference on the scaffold (no MC noise), netted
against computation #1 dance curvatures (ivw-combined). Ring-straight in THREE
bookkeepings: letter (full depth, per the commission), strain-only (conservative),
and double-count-corrected (E_qq_eff = E_qq - 55.6, the dance own soft-core qq
contact -- derived, not tuned). Imports the 2461 scaffold/energy definitions from
`code/2461_ssv_kinematics.py` (same directory); run from anywhere -- the import path
is resolved from this file's own location."""
import numpy as np
# scaffold/energy definitions: execute code/2461_ssv_kinematics.py (module part, before __main__) first
exec(open(__file__.replace("2462_registry_both_ways","2461_ssv_kinematics")).read().split("if __name__")[0])
def qidx(k,c): return 8*k+c
def bonds(closed):
    B=[]
    for k in range(N if closed else N-1):
        for c in range(4): B.append((qidx(k,c),qidx((k+1)%N,c)))
    return B
Pr,_,_=ring_scaffold(); Ps,_,_=straight_scaffold()
Br=bonds(True); Bs=bonds(False)
def lengths(P,B): return np.array([np.linalg.norm(P[i]-P[j]) for i,j in B])
Lr0=lengths(Pr,Br); Ls0=lengths(Ps,Bs)
ECON=ALPHA_S*AHC/np.sqrt(d**2+A_QQ**2)   # dance's own soft-core qq contact Coulomb
print(f"double-count anchor: dance soft-core qq contact = {ECON:.1f} MeV (cf central E_qq=66)")
def Vh(r,s0,Eqq):
    k=2*Eqq/s0**2; return -Eqq+0.5*k*(r-s0)**2
def Vm(r,s0,Eqq):
    a=1.0/s0; return Eqq*((1-np.exp(-a*(r-s0)))**2-1)
def Eb(P,B,s0v,Eqq,form): return (Vh if form=='h' else Vm)(lengths(P,B),s0v,Eqq).sum()
modes={'tilt m=0':(dict(tilt=[0.04]*N),0.04),'tilt m=1':(dict(tilt=[0.04*np.cos(2*np.pi*k/N) for k in range(N)]),0.04),
       'tilt m=2':(dict(tilt=[0.04*np.cos(4*np.pi*k/N) for k in range(N)]),0.04),'ellipt  ':(dict(ell=0.02),0.02)}
dance={'tilt m=0':(+218,95),'tilt m=1':(-90,71),'tilt m=2':(-304,56),'ellipt  ':(+280,610)}
dance_rs=(-70.4,4.6)
Pp={n:ring_scaffold(**kw)[0] for n,(kw,_) in modes.items()}
Pm_={'tilt m=0':ring_scaffold(tilt=[-0.04]*N)[0],
     'tilt m=1':ring_scaffold(tilt=[-0.04*np.cos(2*np.pi*k/N) for k in range(N)])[0],
     'tilt m=2':ring_scaffold(tilt=[-0.04*np.cos(4*np.pi*k/N) for k in range(N)])[0],
     'ellipt  ':ring_scaffold(ell=-0.02)[0]}
print("\nMODE NETS over full grid (verdict at BINDING >3sigma criterion):")
for form in ('h','m'):
    for hyp in ('i','ii'):
        s0r=1.15*np.ones(len(Br)) if hyp=='i' else Lr0.copy()
        for Eqq in (40,66,100,170):
            outs=[]
            worst=None
            for name,(kw,x) in modes.items():
                c=(Eb(Pp[name],Br,s0r,Eqq,form)+Eb(Pm_[name],Br,s0r,Eqq,form)-2*Eb(Pr,Br,s0r,Eqq,form))/x**2
                dc,de=dance[name]; net=dc+c; sig=net/de
                outs.append(f"{name.strip()}:{net:+6.0f}({sig:+.1f}s)")
                if worst is None or sig<worst[1]: worst=(name,sig)
            kill = worst[1] < -3.0
            print(f"  {form}/{hyp} E_qq={Eqq:>3}: "+" ".join(outs)+("   ** >3s KILL: "+worst[0] if kill else ""))
print("\nRING-STRAIGHT, three bookkeepings (bond ch | net with dance -70.4+-4.6):")
for form in ('h',):
    for hyp in ('i','ii'):
        s0r=1.15*np.ones(len(Br)) if hyp=='i' else Lr0.copy()
        s0s=1.15*np.ones(len(Bs)) if hyp=='i' else Lr0[:len(Bs)].copy()
        for Eqq in (40,66,100,170):
            L=Eb(Pr,Br,s0r,Eqq,form)-Eb(Ps,Bs,s0s,Eqq,form)                 # letter (full depth)
            S=(Eb(Pr,Br,s0r,Eqq,form)+Eqq*len(Br))-(Eb(Ps,Bs,s0s,Eqq,form)+Eqq*len(Bs))  # strain-only
            Ee=max(Eqq-ECON,0.0)
            Dcc=S-Ee*(len(Br)-len(Bs))                                       # double-count-corrected depth
            print(f"  {form}/{hyp} E_qq={Eqq:>3}: letter {L:+8.1f} -> net {dance_rs[0]+L:+8.1f} | "
                  f"strain-only {S:+7.1f} -> net {dance_rs[0]+S:+7.1f} | "
                  f"dc-corrected {Dcc:+7.1f} -> net {dance_rs[0]+Dcc:+7.1f}")
