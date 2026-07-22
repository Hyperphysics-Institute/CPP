#!/usr/bin/env python3
"""S4-X X5-LIN (Patch 2743-2744) -- the amplitude diagnosis closer,
redesigned at prereg-freeze per the 2741 spec's own license.

PREREGISTRATION (frozen HERE before any run):
DESIGN CHANGE FROM THE 2741 SKETCH (recorded openly): instead of an
underpowered small-eps driven ladder, ONE UNDRIVEN chain + EXACT
EXPONENTIAL REWEIGHTING: for the Gibbs measure of the implemented H,
the driven mean at ANY eps is the tilt identity
M(eps) = <A e^{-beta eps A}>_0 / <e^{-beta eps A}>_0.
Computing M(eps) from an undriven chain gives the ENTIRE response
curve with exact Gibbs semantics; comparing M(2.4) against the
DIRECTLY-DRIVEN means already on record (X3-LONG k1x: -4.460, same
box/parameters) is then a decisive test of whether the driven chains
sampled Gibbs(H + eps A).
CHAIN: N = 432, a_s = 0.04, seed 20260770, NO drive, 16,000 sweeps
(1,000 eq + 15,000 sampling), fresh full summation every 10 sweeps
(1,500 samples). Stored per sample: Re and Im of rho_z at the three
representative vectors k1x/(b,b,0)/(b,b,b) + shell-mean |rho|^2.
ESTIMATORS: S_var per vector = (<A^2>+<B^2>)/N ; M(eps) at eps in
{0.3, 0.6, 1.2, 1.8, 2.4} MeV by reweighting with 10-block jackknife
errors and ESS_w = (sum w)^2 / sum w^2 reported; cumulants <A^3>
(symmetry check: must be ~0) and excess kurtosis gamma_2 =
<A^4>_c / <A^2>^2 (the non-Gaussianity that a real nonlinear
enhancement requires).
PRE-REGISTERED EXPECTATION MARKER (worker, honest, non-binding): the
1.62x enhancement, if it were true nonlinear Gibbs response, requires
gamma_2 ~ 200 for this mode -- wildly super-CLT for a 432-particle
collective variable; the worker therefore EXPECTS band B2. The frozen
bands decide, not the expectation.
FROZEN BANDS:
B1 (NONLINEAR-GIBBS; diagnosis CLOSES): M_rw(2.4) agrees with the
direct driven mean (-4.460 +/- 0.28, X3-LONG k1x) within 2 sigma
combined -> the driven chains were faithful; the enhancement is real
nonlinear response of a non-Gaussian mode; FDT-linear inapplicable at
beta*eps*sigma ~ 0.43; instruments reconciled; the curve = a
non-Gaussianity measurement; PR3 satisfied via the exact small-eps
limit + validated correspondence.
B2 (GIBBS-INCONSISTENT DRIVE; ESCALATE): M_rw(2.4) sits at the
near-linear value (-beta*eps*<A^2> = -2.75-ish, curvature small,
gamma_2 << 200) AND differs from the direct driven mean by > 2 sigma
-> the driven chains did NOT sample Gibbs(H + eps A); escalation
adjudication convenes; AUTOMATON-1 elevated; the driven-probe
implementation goes under audit line by line.
B3 (PARTIAL): ESS_w(2.4) < 200 or intermediate -> extend chain,
report, no verdict."""
import math, json, pickle, os, numpy as np
from scipy.special import erfc as serfc

HBARC=197.3269788; AEM=1/137.035999084
PHI=(1+math.sqrt(5))/2; A=0.589/PHI; KAPPA=2.0/A
NCP=2*math.sqrt(2.0)/A**3; Q2=AEM*HBARC
THETA=2*math.sqrt(2)*math.pi*Q2/A
N=432; A_S=0.04; SEED=20260770; EQ=1000; TOTAL=16000

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
    return kv,(kv**2).sum(1),np.array(ks)

def run_chunk(max_sweeps):
    ck="/tmp/x5lin_ck.pkl"
    L=(N/NCP)**(1.0/3.0); alpha=5.6/L; rc=L/2; b=2*math.pi/L
    kv,k2,nvec=make_k(L)
    wk=np.exp(-k2/(4*alpha*alpha))/k2
    pref_k=2*(2*math.pi/(L**3))*Q2
    reps=[int(np.where((nvec==v).all(1))[0][0]) for v in ([1,0,0],[1,1,0],[1,1,1])]
    n2=np.round(k2/b**2).astype(int)
    z=np.array([1.0]*(N//2)+[-1.0]*(N//2))
    if os.path.exists(ck):
        st=pickle.load(open(ck,"rb")); rng=st["rng"]; pos=st["pos"]; S=st["S"]
        done=st["done"]; ser=st["ser"]; shl=st["shl"]; acc=st["acc"]; tot=st["tot"]
    else:
        rng=np.random.default_rng(SEED)
        pos=rng.uniform(0,L,size=(N,3))
        S=(z[:,None]*np.exp(1j*(pos@kv.T))).sum(0)
        done=0; ser=[]; shl=[]; acc=0; tot=0
    step=0.20*A
    end=min(TOTAL,done+max_sweeps)
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
                              +1.0/np.sqrt(r2o[mo]+A_S*A_S)))
            en=np.sum(zz[mn]*(serfc(alpha*rn[mn])/rn[mn]-1.0/rn[mn]
                              +1.0/np.sqrt(r2n[mn]+A_S*A_S)))
            dS=z[i]*(np.exp(1j*(newp@kv.T))-np.exp(1j*(pos[i]@kv.T)))
            Snew=S+dS
            dEk=pref_k*np.sum(wk*((Snew.real**2+Snew.imag**2)-(S.real**2+S.imag**2)))
            dE=en-eo+dEk; tot+=1
            if dE<=0 or rng.random()<math.exp(-dE/THETA):
                pos[i]=newp; S=Snew; acc+=1
        if s_>=EQ and (s_-EQ)%10==0:
            Sf=(z[:,None]*np.exp(1j*(pos@kv.T))).sum(0)
            ser.append([float(Sf[j].real) for j in reps]+[float(Sf[j].imag) for j in reps])
            shl.append([float(np.mean(np.abs(Sf[n2==s])**2))/N for s in (1,2,3)])
    done=end
    pickle.dump({"rng":rng,"pos":pos,"S":S,"done":done,"ser":ser,"shl":shl,
                 "acc":acc,"tot":tot},open(ck,"wb"))
    print(f"[X5-LIN] {done}/{TOTAL} sweeps  acc={acc/max(tot,1):.2f}  samples={len(ser)}")
    if done>=TOTAL:
        json.dump({"ser":ser,"shl":shl,"L":L},open("/tmp/x5lin.json","w"))
        print("[X5-LIN] COMPLETE -> json")

def analyze():
    beta=1.0/THETA
    d=json.load(open("/tmp/x5lin.json"))
    ser=np.array(d["ser"]); shl=np.array(d["shl"]); n=len(ser)
    names=["k1x","k2v","k3v"]
    print(f"samples={n}; shell S_zz reference: "
          +"  ".join(f"n2={s+1}:{shl[:,s].mean():.4f}" for s in range(3)))
    Adat=ser[:,0]  # k1x real part
    varA=Adat.var(ddof=1); S_var=2*varA/N
    Bdat=ser[:,3]
    print(f"k1x: Var(A)={varA:.2f} -> S_var={S_var:.4f} ; S from A,B = "
          f"{(Adat.var(ddof=1)+Bdat.var(ddof=1))/N:.4f}")
    m3=np.mean((Adat-Adat.mean())**3)
    m4=np.mean((Adat-Adat.mean())**4)
    g2=(m4-3*varA*varA)/varA**2
    print(f"cumulants: <A>={Adat.mean():+.3f} (sym~0) ; skew m3/s3={m3/varA**1.5:+.3f} ; "
          f"excess kurtosis gamma2={g2:+.3f}  (nonlinear-Gibbs 1.62x needs ~+200)")
    print("\nReweighted response curve M(eps) [10-block jackknife]:")
    nb=10; bl=n//nb
    for eps in (0.3,0.6,1.2,1.8,2.4):
        w=np.exp(-beta*eps*(Adat-Adat.mean()))  # center for stability; shift-invariant ratio
        Aa=Adat
        M=np.sum(Aa*w)/np.sum(w)
        jk=[]
        for j in range(nb):
            m=np.ones(n,bool); m[j*bl:(j+1)*bl]=False
            jk.append(np.sum(Aa[m]*w[m])/np.sum(w[m]))
        jk=np.array(jk); Me=math.sqrt((nb-1)/nb*np.sum((jk-jk.mean())**2))
        essw=np.sum(w)**2/np.sum(w*w)
        lin=-beta*eps*varA
        print(f"  eps={eps}: M_rw={M:+.3f}+/-{Me:.3f}  linear={lin:+.3f}  "
              f"ratio={M/lin if lin!=0 else 0:.3f}  ESS_w={essw:.0f}")
    # frozen band evaluation at eps=2.4
    eps=2.4
    w=np.exp(-beta*eps*(Adat-Adat.mean()))
    M=np.sum(Adat*w)/np.sum(w)
    jk=[]
    for j in range(nb):
        m=np.ones(n,bool); m[j*bl:(j+1)*bl]=False
        jk.append(np.sum(Adat[m]*w[m])/np.sum(w[m]))
    jk=np.array(jk); Me=math.sqrt((nb-1)/nb*np.sum((jk-jk.mean())**2))
    essw=np.sum(w)**2/np.sum(w*w)
    direct=-4.460; de=0.28
    D=abs(M-direct)/math.sqrt(Me*Me+de*de)
    lin=-beta*eps*varA
    Dlin=abs(M-lin)/max(Me,1e-9)
    print(f"\nBand evaluation at eps=2.4: M_rw={M:+.3f}+/-{Me:.3f} vs direct {direct}+/-{de} "
          f"-> {D:.2f} sigma ; vs linear {lin:+.3f} -> {Dlin:.2f} sigma ; ESS_w={essw:.0f}")
    if essw<200: v="B3 PARTIAL (ESS_w<200): extend chain"
    elif D<=2: v="B1 NONLINEAR-GIBBS: diagnosis CLOSES"
    elif Dlin<=2 and D>2: v="B2 GIBBS-INCONSISTENT DRIVE: ESCALATE (AUTOMATON-1 elevated)"
    else: v="B3 PARTIAL/intermediate"
    print(f"FROZEN VERDICT: {v}")

if __name__=="__main__":
    import sys
    if sys.argv[1]=="analyze": analyze()
    else: run_chunk(int(sys.argv[1]))
