#!/usr/bin/env python3
"""ALPHA-1 S4-N execution (Patch 2709) under the FROZEN 2708 prereg.
Two-species Metropolis MC, minimum-image truncated-shifted soft Coulomb.
Seeded, deterministic. All parameters frozen upstream; zero tuned."""
import math, numpy as np

HBARC=197.3269788; ALPHA=1/137.035999084
PHI=(1+math.sqrt(5))/2; a_dp=0.589/PHI
KAPPA=2.0/a_dp; NCP=2*math.sqrt(2.0)/a_dp**3
Q2=ALPHA*HBARC; THETA=2*math.sqrt(2)*math.pi*Q2/a_dp

def run(N, a_s, seed, eq_sweeps, sweeps, label):
    rng=np.random.default_rng(seed)
    L=(N/NCP)**(1.0/3.0); half=L/2.0
    z=np.array([1.0]*(N//2)+[-1.0]*(N//2))
    pos=rng.uniform(0,L,size=(N,3))
    rcut=half; 
    def pair_e(dr2, zz):
        r=np.sqrt(dr2+a_s*a_s)
        rc=math.sqrt(rcut*rcut+a_s*a_s)
        e=Q2*zz*(1.0/r-1.0/rc)
        e[dr2>rcut*rcut]=0.0
        return e
    def de_move(i, newp):
        d_old=pos-pos[i]; d_new=pos-newp
        d_old-=L*np.round(d_old/L); d_new-=L*np.round(d_new/L)
        r2o=(d_old**2).sum(1); r2n=(d_new**2).sum(1)
        zz=z*z[i]
        eo=pair_e(r2o,zz); en=pair_e(r2n,zz)
        eo[i]=0; en[i]=0
        return en.sum()-eo.sum()
    step=0.20*a_dp; acc=0; tot=0
    # histogram accumulators: charge-weighted and same/opp counts about EVERY particle
    nb=90; rmax=min(half,0.9); edges=np.linspace(0,rmax,nb+1); 
    hz=np.zeros(nb); hz2=np.zeros(nb); nsamp=0; cnt=np.zeros(nb)
    for sw in range(eq_sweeps+sweeps):
        for _ in range(N):
            i=rng.integers(N)
            newp=(pos[i]+rng.normal(0,step,3))%L
            dE=de_move(i,newp)
            tot+=1
            if dE<=0 or rng.random()<math.exp(-dE/THETA):
                pos[i]=newp; acc+=1
        if sw>=eq_sweeps and (sw-eq_sweeps)%5==0:
            # charge correlation: for each particle, sign-normalized neighbor charge
            zsum=np.zeros(nb); c=np.zeros(nb)
            for i in range(N):
                d=pos-pos[i]; d-=L*np.round(d/L)
                r=np.sqrt((d**2).sum(1)); r[i]=1e9
                w=z*z[i]  # +1 same, -1 opposite; response profile ~ -<w> (opposite excess)
                idx=np.clip((r/rmax*nb).astype(int),0,nb)
                m=idx<nb
                zsum+=np.bincount(idx[m],weights=-w[m],minlength=nb)  # + means opposite-charge excess
                c+=np.bincount(idx[m],minlength=nb)
            prof=np.where(c>0,zsum/np.maximum(c,1),0.0)
            hz+=prof; hz2+=prof*prof; cnt+=c; nsamp+=1
    mean=hz/nsamp; var=hz2/nsamp-mean**2; sem=np.sqrt(np.maximum(var,0)/nsamp)
    rc_=0.5*(edges[:-1]+edges[1:])
    # P1: sign alternation check beyond 2*a_s out to 3/kappa
    lo=2*a_s; hi=3.0/KAPPA
    m=(rc_>lo)&(rc_<hi)&(cnt/nsamp>50)
    lead=np.sign(mean[m][np.argmax(np.abs(mean[m]))])
    viol=np.sum((np.sign(mean[m])!=lead)&(np.abs(mean[m])>2*sem[m]))
    # P2: kappa fit on |mean*r| over [0.10,0.45]
    mf=(rc_>=0.10)&(rc_<=0.45)&(mean>0)
    kfit=np.nan
    if mf.sum()>=5:
        cpoly=np.polyfit(rc_[mf],np.log(mean[mf]*rc_[mf]),1); kfit=-cpoly[0]
    print(f"[{label}] N={N} a_s={a_s} L={L:.3f} fm  acc={acc/tot:.2f}  samples={nsamp}")
    print(f"   P1 window ({lo:.3f},{hi:.3f}) fm: significant sign-alternations = {viol} "
          f"-> {'MONOTONIC' if viol==0 else 'ALTERNATING'}")
    print(f"   P2: kappa_fit = {kfit:.3f} /fm  (kappa_D = {KAPPA:.3f}; ratio {kfit/KAPPA:.3f})")
    # print profile summary at a few radii
    for rq in (0.10,0.18,0.28,0.40,0.55,0.70):
        j=int(rq/rmax*nb)
        print(f"     r={rc_[j]:.3f}: rho_z={mean[j]:+.5f} +/- {sem[j]:.5f}")
    return viol==0, kfit

print(f"frozen params: theta={THETA:.4f} MeV  q^2={Q2:.5f} MeV fm  n_CP={NCP:.3f}/fm^3  "
      f"kappa_D={KAPPA:.4f}/fm  Gamma={Q2*KAPPA/THETA:.4f}")
r1=run(686,0.04,20260721,500,2000,"MAIN")
r2=run(432,0.02,20260722,300,1200,"ROB-a")
r3=run(432,0.08,20260723,300,1200,"ROB-b")
mono=[r1[0],r2[0],r3[0]]; kf=[r1[1],r2[1],r3[1]]
P1=r1[0]; P2=(0.75<=r1[1]/KAPPA<=1.25)
P3=(mono[1]==mono[0]==mono[2]) and all(0.6<=k/KAPPA<=1.4 for k in kf[1:])
print(f"\nP1={'PASS' if P1 else 'FAIL'}  P2={'PASS' if P2 else 'FAIL'}  P3={'PASS' if P3 else 'FAIL'}"
      f"  ->  S4-N {'PASS' if (P1 and P2 and P3) else 'FAIL'}")
