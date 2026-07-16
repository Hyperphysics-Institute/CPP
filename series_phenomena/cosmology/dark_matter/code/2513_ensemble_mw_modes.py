#!/usr/bin/env python3
"""OPEN-DM-MW-MODES-1 (Patch 2513) -- ensemble-averaged Momentwise mode curvatures at the
PINNED coefficient (2496: kappa_q=132, kappa_e=44 MeV/c^2; kscale=1.0 ONLY -- G7, never fit).
Executes the registry-named fix for C7 (mode decorrelation): the perturbation REALIZATION is
varied over a deterministic phase/amplitude grid and per-member paired curvatures are
ensemble-averaged. dance_v8 is imported VERBATIM from 2510 (dynamics untouched).

Pre-registration: reasoning/2513.md SS1-4, committed-in-file before this ran.
Ensembles: m0 amplitudes {+-0.04,+-0.02} (4); m1/m2 phases 2*pi*j/8, x=0.04 (8 each);
ell phases 2*pi*j/8, ell=0.02 (8). dt = tauC/{50,25}. Primary observable E_tot
(matched-pair KE convention, flag verbatim-in-force). Classification per mode per dt:
|<c>| vs 2*SEM. Diagnostic: m2 amplitude-scaling x=0.02 phases {0,pi/2} at dt=1/50.
Deterministic; no RNG."""
import numpy as np, time, sys
import os
_D=os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(_D,"2461_ssv_kinematics.py")).read().split("if __name__")[0])
_src=open(os.path.join(_D,"2510_hardened_dance_inertia.py")).read().split("Pr,Cr,SPr=ring_scaffold()")[0]
exec("\n".join(l for l in _src.splitlines() if not l.startswith("exec(") and not l.startswith("import ")))

def ring_scaffold_ph(tilt=None, ell=0.0, psi=0.0):
    """2461 ring_scaffold with an ellipticity PHASE (psi=0 reproduces 2461 exactly)."""
    S=[]
    for k in range(N):
        phi=2*np.pi*k/N
        R=R0*(1+ell*np.cos(2*phi+psi))
        cx=R*(1-np.cos(phi)); cz=R*np.sin(phi)
        th=phi+(tilt[k] if tilt is not None else 0.0)
        c,s=np.cos(th),np.sin(th); par=(-1)**k
        h=A_Q/2
        q=[(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)]
        for (x,y,sg) in q: S.append(((cx+x*c,y,cz-x*s),sg*par,'q',k))
        for (x,y,sg) in q:
            n=np.hypot(x,y); X,Y=R_E*x/n,R_E*y/n
            S.append(((cx+X*c,Y,cz-X*s),-sg*par,'e',k))
    P=np.array([s[0] for s in S]); C=np.array([float(s[1]) for s in S])
    return P,C,[s[2] for s in S]

Pr,Cr,SPr=ring_scaffold(); Ps,Cs,SPs=straight_scaffold()
Fr=ssv_vectors(Pr,Cr,SPr); Fs=ssv_vectors(Ps,Cs,SPs)
FREF=max(np.linalg.norm(Fr,axis=1).max(),np.linalg.norm(Fs,axis=1).max())

def etot(P,dtf):
    E,K,_,_=dance_v8(P,Cr,SPr,FREF,dtf)
    return E.mean()+K.mean(), E.mean()

def members():
    """(mode_name, geometry, x) triples per the pre-registered grid."""
    out={'m0':[],'m1':[],'m2':[],'ell':[]}
    for x in (+0.04,-0.04,+0.02,-0.02):
        out['m0'].append((ring_scaffold(tilt=[x]*N)[0],abs(x)))
    for j in range(8):
        ph=2*np.pi*j/8
        out['m1'].append((ring_scaffold(tilt=[0.04*np.cos(2*np.pi*k/N+ph) for k in range(N)])[0],0.04))
        out['m2'].append((ring_scaffold(tilt=[0.04*np.cos(4*np.pi*k/N+ph) for k in range(N)])[0],0.04))
        out['ell'].append((ring_scaffold_ph(ell=0.02,psi=ph)[0],0.02))
    return out

if __name__=='__main__':
    t0=time.time()
    # scaffold-phase sanity: psi=0 ellipse must equal 2461 geometry exactly
    assert np.allclose(ring_scaffold_ph(ell=0.02,psi=0.0)[0], ring_scaffold(ell=0.02)[0]), "psi=0 mismatch"
    print(f"FREF={FREF:.2f} (unchanged construction); kappa pinned x1.0; TC=60 burn=0.15")
    mem=members()
    results={}
    for dtf in (1/50,1/25):
        T0,E0=etot(Pr,dtf)
        print(f"\n== dt=tauC/{int(1/dtf)}: base ring Etot={T0:+.1f} Ep={E0:+.1f} ({time.time()-t0:.0f}s)")
        for nm in ('m0','m1','m2','ell'):
            cs=[]; ceps=[]
            for (P,x) in mem[nm]:
                Tp,Ep=etot(P,dtf)
                cs.append(2*(Tp-T0)/x**2); ceps.append(2*(Ep-E0)/x**2)
            cs=np.array(cs); ceps=np.array(ceps)
            mn=cs.mean(); sem=cs.std(ddof=1)/np.sqrt(len(cs))
            cls=('SIG-POS' if mn>2*sem else ('SIG-NEG' if mn<-2*sem else 'INCONCLUSIVE'))
            results[(nm,dtf)]=(mn,sem,cls)
            print(f"  {nm:3s} n={len(cs)}: <c>={mn:+10.0f} +- SEM {sem:8.0f}  [{cls}]  "
                  f"(Ep-part <c>={ceps.mean():+9.0f})  members {np.array2string(cs,precision=0,max_line_width=200)}  ({time.time()-t0:.0f}s)")
    # pre-registered diagnostic: m2 amplitude scaling, dt=1/50, phases {0, pi/2}, x=0.02
    dtf=1/50; T0,_=etot(Pr,dtf)
    print("\n== m2 amplitude-scaling diagnostic (dt=tauC/50; quadratic regime -> dT ratio ~ 4):")
    for ph in (0.0,np.pi/2):
        d04=etot(ring_scaffold(tilt=[0.04*np.cos(4*np.pi*k/N+ph) for k in range(N)])[0],dtf)[0]-T0
        d02=etot(ring_scaffold(tilt=[0.02*np.cos(4*np.pi*k/N+ph) for k in range(N)])[0],dtf)[0]-T0
        r=d04/d02 if d02!=0 else float('inf')
        print(f"  phase {ph:4.2f}: dT(0.04)={d04:+8.2f}  dT(0.02)={d02:+8.2f}  ratio={r:+6.2f}")
    # pre-registered branch reading (SS3), mechanical:
    def sig(nm,dtf): return results[(nm,dtf)]
    flips=[nm for nm in ('m0','m1','m2','ell')
           if sig(nm,1/50)[2].startswith('SIG') and sig(nm,1/25)[2].startswith('SIG')
           and np.sign(sig(nm,1/50)[0])!=np.sign(sig(nm,1/25)[0])]
    phys=('m1','m2','ell')
    allclass=all(sig(nm,d)[2]!='INCONCLUSIVE' for nm in phys for d in (1/50,1/25))
    samesign=all(np.sign(sig(nm,1/50)[0])==np.sign(sig(nm,1/25)[0]) for nm in phys)
    negboth=[nm for nm in phys if sig(nm,1/50)[2]=='SIG-NEG' and sig(nm,1/25)[2]=='SIG-NEG']
    print(f"\n== branch reading (mechanical, per reasoning/2513 SS3):")
    print(f"   flips={flips or 'none'}; phys all-classifiable={allclass}; phys same-sign={samesign}; SIG-NEG-both={negboth or 'none'}")
    if flips or not allclass: print("   -> BRANCH U: C7 STANDS (leg-based record remains operative)")
    elif negboth: print("   -> BRANCH N: decorrelation resolved, ADVERSE sign -> panel flash; verdict HELD")
    elif samesign: print("   -> BRANCH D: C7 DISCHARGED (ensemble record becomes operative)")
    else: print("   -> BRANCH U (residual sign inconsistency)")
    print(f"total {time.time()-t0:.0f}s")
