#!/usr/bin/env python3
"""S4-X X5 (Patch 2737-2738) under s4x_charter.md stage X5 -> PR3,
elevated by X6 to arbiter of the a_s = 0.04 shape disagreement.

PREREGISTRATION (frozen HERE before any run):
DESIGN: Ewald MC at the MAIN parameters (N = 686, a_s = 0.04, theta =
35.1495 MeV) with a SUPERPOSED weak external potential
U_ext = sum_m eps_m * z_i * cos(k_m . r_i) driving FOUR modes at once:
k1x = (2pi/L)(1,0,0), k1y = (2pi/L)(0,1,0) [directional check, R8],
k2 = (2pi/L)(1,1,0), k3 = (2pi/L)(1,1,1). Cross-mode contamination is
O((beta*eps)^2) ~ 0.5% at eps = 2.4 MeV (beta*eps = 0.068) --
disclosed; the half-amplitude run is the linearity gate that tests it.
RUNS: D-FULL (eps = 2.4 MeV all modes, seed 20260741) and D-HALF
(eps = 1.2 MeV, seed 20260742); each 500 eq + 1500 sampling sweeps,
samples every 5 sweeps, 10-block errors. Baseline S_zz: the archived
undriven MAIN-A/B chains at the same k.
ESTIMATOR: per driven mode, S_drv(k) = -2<Re rho_z(k)> / (beta eps N)
(first-moment/driven measurement of the same normalized object the
fluctuation route calls S_zz; NO fluctuation relation assumed).
FROZEN VERDICT RULES:
V-LIN: D-FULL vs D-HALF S_drv consistent within 2 sigma per mode,
else the affected mode is quarantined.
V-DIR: k1x vs k1y S_drv consistent within 2 sigma (R8 spot check).
V1 (PR3): |S_drv - S_zz(fluctuation)| <= 2 sigma at each of the >= 3
distinct |k| -> PR3 SATISFIED at these k (the bridge TESTED, not
assumed, within the simulated system).
V2 (arbitration): if V1 passes, the sim's small-k suppression is
confirmed by an independent first-moment probe -> the X6 shape
disagreement is NOT an S_zz-estimator artifact (classification
unchanged; HNC-miss becomes the leading reading, still unclosed
pending X4/X3). If V1 fails at any k, classification updates toward
SIMULATION-ESTIMATOR-SYSTEMATIC and the affected functionals (incl.
the X6 pole numbers) are quarantined.
POWER (disclosed): per-mode S_drv precision ~10% per run; the
sim-vs-HNC separation at n^2 = 1 is ~20-25%; per-k discrimination
~2 sigma, joint over three |k| ~3.5 sigma."""
import math, json, pickle, os, numpy as np
from scipy.special import erfc as serfc

HBARC=197.3269788; ALPHA_EM=1/137.035999084
PHI=(1+math.sqrt(5))/2; A=0.589/PHI; KAPPA=2.0/A
NCP=2*math.sqrt(2.0)/A**3; Q2=ALPHA_EM*HBARC
THETA=2*math.sqrt(2)*math.pi*Q2/A
RUNS={"D-FULL":(2.4,20260741),"D-HALF":(1.2,20260742)}
NP_=686; A_S=0.04; EQ=500; SW=1500

def make_k(L,n2max=27):
    ks=[]
    for nx in range(-6,7):
        for ny in range(-6,7):
            for nz in range(-6,7):
                n2=nx*nx+ny*ny+nz*nz
                if n2==0 or n2>n2max: continue
                if (nx>0) or (nx==0 and ny>0) or (nx==0 and ny==0 and nz>0):
                    ks.append((nx,ny,nz))
    kv=2*math.pi/L*np.array(ks,float)
    return kv,(kv**2).sum(1)

def run_chunk(label,max_sweeps):
    eps,seed=RUNS[label]; N=NP_; a_s=A_S; total=EQ+SW
    ck=f"/tmp/x5_ck_{label}.pkl"
    L=(N/NCP)**(1.0/3.0); alpha=5.6/L; rc=L/2
    kv,k2=make_k(L); wk=np.exp(-k2/(4*alpha*alpha))/k2
    pref_k=2*(2*math.pi/(L**3))*Q2
    b=2*math.pi/L
    kdr=np.array([[b,0,0],[0,b,0],[b,b,0],[b,b,b]])
    z=np.array([1.0]*(N//2)+[-1.0]*(N//2))
    if os.path.exists(ck):
        st=pickle.load(open(ck,"rb")); rng=st["rng"]; pos=st["pos"]; S=st["S"]
        done=st["done"]; obs=st["obs"]; acc=st["acc"]; tot=st["tot"]
    else:
        rng=np.random.default_rng(seed)
        pos=rng.uniform(0,L,size=(N,3))
        S=(z[:,None]*np.exp(1j*(pos@kv.T))).sum(0)
        done=0; obs=[]; acc=0; tot=0
    step=0.20*A
    end=min(total,done+max_sweeps)
    for s_ in range(done,end):
        for _ in range(N):
            i=int(rng.integers(N))
            newp=(pos[i]+rng.normal(0,step,3))%L
            d_o=pos-pos[i]; d_n=pos-newp
            d_o-=L*np.round(d_o/L); d_n-=L*np.round(d_n/L)
            r2o=(d_o**2).sum(1); r2n=(d_n**2).sum(1)
            ro=np.sqrt(r2o); rn=np.sqrt(r2n)
            zz=Q2*(z*z[i])
            mo=(ro<rc)&(ro>1e-12); mn=(rn<rc)&(rn>1e-12)
            eo=np.sum(zz[mo]*(serfc(alpha*ro[mo])/ro[mo]-1.0/ro[mo]
                              +1.0/np.sqrt(r2o[mo]+a_s*a_s)))
            en=np.sum(zz[mn]*(serfc(alpha*rn[mn])/rn[mn]-1.0/rn[mn]
                              +1.0/np.sqrt(r2n[mn]+a_s*a_s)))
            dS=z[i]*(np.exp(1j*(newp@kv.T))-np.exp(1j*(pos[i]@kv.T)))
            Snew=S+dS
            dEk=pref_k*np.sum(wk*((Snew.real**2+Snew.imag**2)-(S.real**2+S.imag**2)))
            dExt=eps*z[i]*np.sum(np.cos(kdr@newp)-np.cos(kdr@pos[i]))
            dE=en-eo+dEk+dExt; tot+=1
            if dE<=0 or rng.random()<math.exp(-dE/THETA):
                pos[i]=newp; S=Snew; acc+=1
        if s_>=EQ and (s_-EQ)%5==0:
            rho=np.array([np.sum(z*np.cos(kdr[m]@pos.T)) for m in range(4)])
            obs.append(rho.tolist())
    done=end
    pickle.dump({"rng":rng,"pos":pos,"S":S,"done":done,"obs":obs,
                 "acc":acc,"tot":tot},open(ck,"wb"))
    print(f"[{label}] {done}/{total} sweeps  acc={acc/max(tot,1):.2f}  samples={len(obs)}")
    if done>=total:
        json.dump({"label":label,"eps":eps,"L":L,"obs":obs},
                  open(f"/tmp/x5_{label}.json","w"))
        print(f"[{label}] COMPLETE -> json")

def analyze():
    beta=1.0/THETA; N=NP_
    import gzip
    base={}
    for lb in ("MAIN-A","MAIN-B"):
        d=json.load(gzip.open(f"../data/s4e_chains/s4e_{lb}.json.gz"))
        k2=np.array(d["k2"]); szz=np.array(d["szz"]); L=d["L"]
        n2=np.round(k2/(2*math.pi/L)**2).astype(int)
        base[lb]={v:szz[n2==v].mean() for v in (1,2,3)}
    Szz_f={v:0.5*(base["MAIN-A"][v]+base["MAIN-B"][v]) for v in (1,2,3)}
    eS={v:abs(base["MAIN-A"][v]-base["MAIN-B"][v])/2+0.02*Szz_f[v] for v in (1,2,3)}
    names=["k1x","k1y","k2","k3"]; shell=[1,1,2,3]
    res={}
    for label in RUNS:
        d=json.load(open(f"/tmp/x5_{label}.json"))
        eps=d["eps"]; obs=np.array(d["obs"]); n=len(obs)
        nblk=10; bl=n//nblk
        bm=np.array([obs[j*bl:(j+1)*bl].mean(0) for j in range(nblk)])
        mean=bm.mean(0); sem=bm.std(0,ddof=1)/math.sqrt(nblk)
        Sd=-2*mean/(beta*eps*N); Se=2*sem/(beta*eps*N)
        res[label]=(Sd,Se)
        print(f"[{label}] eps={eps}: "+"  ".join(
            f"{names[m]}: S_drv={Sd[m]:.4f}+/-{Se[m]:.4f}" for m in range(4)))
    Sf,Ef=res["D-FULL"]; Sh,Eh=res["D-HALF"]
    print("\nV-LIN (full vs half):")
    lin=True
    for m in range(4):
        Dm=abs(Sf[m]-Sh[m])/math.sqrt(Ef[m]**2+Eh[m]**2)
        lin&=Dm<=2
        print(f"  {names[m]}: {Dm:.2f} sigma {'OK' if Dm<=2 else 'QUARANTINE'}")
    Ddir=abs(Sf[0]-Sf[1])/math.sqrt(Ef[0]**2+Ef[1]**2)
    print(f"V-DIR (k1x vs k1y): {Ddir:.2f} sigma {'OK' if Ddir<=2 else 'ANISOTROPY FLAG'}")
    # combine full+half (weighted) per shell; k1 = mean of x,y
    def comb(m): 
        w1,w2=1/Ef[m]**2,1/Eh[m]**2
        return (Sf[m]*w1+Sh[m]*w2)/(w1+w2), 1/math.sqrt(w1+w2)
    c=[comb(m) for m in range(4)]
    S1=( (c[0][0]/c[0][1]**2+c[1][0]/c[1][1]**2)/(1/c[0][1]**2+1/c[1][1]**2),
         1/math.sqrt(1/c[0][1]**2+1/c[1][1]**2) )
    drv={1:S1,2:c[2],3:c[3]}
    print("\nV1 (PR3 test: driven vs fluctuation, per |k| shell):")
    v1=True
    for v in (1,2,3):
        D=abs(drv[v][0]-Szz_f[v])/math.sqrt(drv[v][1]**2+eS[v]**2)
        v1&=D<=2
        print(f"  n2={v}: S_drv={drv[v][0]:.4f}+/-{drv[v][1]:.4f} vs "
              f"S_zz={Szz_f[v]:.4f}+/-{eS[v]:.4f} -> {D:.2f} sigma {'OK' if D<=2 else 'FAIL'}")
    # HNC comparison at same k (DH-form with kappa from committed 1.0206, plus pure-DH ref)
    L=(NP_/NCP)**(1.0/3.0); b=2*math.pi/L
    for v,kk in ((1,b),(2,b*math.sqrt(2)),(3,b*math.sqrt(3))):
        for tag,kap in (("HNC(1.0206kD)",1.0206*KAPPA),("pure-DH",KAPPA)):
            pass
    print("\nReference S(k)=k2/(k2+kap2) at the shells:")
    for v,kk in ((1,b),(2,b*math.sqrt(2)),(3,b*math.sqrt(3))):
        print(f"  n2={v}: HNC-like {kk*kk/(kk*kk+(1.0206*KAPPA)**2):.4f} ; "
              f"sim-pole-like(1.26kD) {kk*kk/(kk*kk+(1.2605*KAPPA)**2):.4f}")
    print(f"\nVERDICT: V-LIN={'PASS' if lin else 'PARTIAL'}  "
          f"V1(PR3)={'PASS -> shape disagreement CONFIRMED as real (not estimator artifact); classification unchanged, HNC-miss leading reading' if v1 else 'FAIL -> SIMULATION-ESTIMATOR-SYSTEMATIC; X6 pole numbers quarantined'}")

if __name__=="__main__":
    import sys
    if sys.argv[1]=="analyze": analyze()
    else: run_chunk(sys.argv[1],int(sys.argv[2]))
