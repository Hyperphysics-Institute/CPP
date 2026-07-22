#!/usr/bin/env python3
"""C2R-L2 (Patch 2773): near-core chi(r) by the founder superposition
specification; delta-ell/ell_LO COMPUTED through the frozen operator.

Frozen route (c2r_l2_prereg.md, Patch 2772):
  cloud   rho_hat(r) = kappa^2 e^{-kappa r}/(4 pi r), unit total charge;
  kernel  g(r) = (1 - e^{-kappa r})/r,  g(0) = kappa  (diagonal self-medium);
  corrected system (I + alpha*Gtilde) psi = 1/r0, source = point (unchanged);
  baseline (I + alpha*G) phi = 1/r0 re-solved in the SAME run for pairing.
Arenas: A0 FCC ball, A1 HCP ball (2685 builders, sanity-gated). R = 7, 9.
Windows (frozen): [0.45,1.3], [0.55,1.6], [0.7,1.8] fm; bin-mean |f|;
fit: log-linear on r*|f| (identical machinery to 2685).
Deterministic; no seeds; no stochastic elements.
"""
import math, numpy as np
from scipy.spatial import cKDTree

PHI=(1+math.sqrt(5))/2; L_UNIT=0.589; L_EDGE=L_UNIT/PHI
KAPPA=2.0/L_EDGE; ALPHA=L_EDGE/(math.pi*math.sqrt(2))
print(f"frozen inputs: a={L_EDGE:.10f} fm  kappa={KAPPA:.6f} /fm  alpha={ALPHA:.8f} fm")
print(f"diagonal self-medium term alpha*kappa = {ALPHA*KAPPA:.6f}  "
      f"(effective stiffness 1+alpha*kappa = {1+ALPHA*KAPPA:.6f})")

# ---- committed builders (verbatim from 2685) ------------------------------
def fcc_ball(R):
    pts=[]
    for i in range(-2*R,2*R+1):
        for j in range(-2*R,2*R+1):
            for k in range(-2*R,2*R+1):
                if (i+j+k)%2==0:
                    x=np.array([i,j,k])/math.sqrt(2.0)
                    if np.linalg.norm(x)<=R: pts.append(x)
    return np.array(pts)

def layered_ball(R, seq):
    dz=math.sqrt(2.0/3.0)
    offs=[np.array([0.0,0.0]),np.array([0.5,math.sqrt(3)/6]),np.array([1.0,math.sqrt(3)/3])]
    e1=np.array([1.0,0.0]); e2=np.array([0.5,math.sqrt(3)/2])
    pts=[]; M=int(R/dz)+2; K=int(R)+3
    for m in range(-M,M+1):
        z=m*dz; o=offs[seq[m]]
        for p in range(-2*K,2*K+1):
            for q in range(-2*K,2*K+1):
                xy=p*e1+q*e2+o
                if xy@xy+z*z<=R*R+1e-9: pts.append([xy[0],xy[1],z])
    return np.array(pts)

def hcp_seq(M): return {m: m%2 for m in range(-M-2,M+3)}

def sanity(P,name):
    T=cKDTree(P); d,_=T.query(P,k=2); mind=d[:,1].min()
    ctr=P.mean(0); rc=np.linalg.norm(P-ctr,axis=1)
    interior=rc<rc.max()-1.1
    coord=np.array([len(x)-1 for x in T.query_ball_point(P[interior],1.001)])
    ok=(abs(mind-1.0)<1e-6) and (np.bincount(coord).argmax()==12) and (coord.min()==12)
    print(f"  sanity {name}: N={len(P)}  min-chord={mind:.6f} a  interior z: "
          f"min={coord.min()} mode={np.bincount(coord).argmax()} max={coord.max()}  "
          f"-> {'PASS' if ok else 'FAIL'}")
    assert ok
    return len(P)

# ---- solves ---------------------------------------------------------------
def solve_pair(P_nn):
    P=P_nn*L_EDGE
    src=int(np.argmin(np.linalg.norm(P-P.mean(0),axis=1)))
    mask=np.ones(len(P),bool); mask[src]=False
    Q=P[mask]; r0=np.linalg.norm(Q-P[src],axis=1)
    Dm=np.linalg.norm(Q[:,None,:]-Q[None,:,:],axis=2)
    np.fill_diagonal(Dm,np.inf)
    G=1.0/Dm                                   # baseline point kernel
    Gt=(1.0-np.exp(-KAPPA*Dm))/Dm              # cloud kernel, off-diagonal
    np.fill_diagonal(Gt,KAPPA)                 # g(0)=kappa self-medium term
    b=1.0/r0
    phi =np.linalg.solve(np.eye(len(Q))+ALPHA*G , b)
    phit=np.linalg.solve(np.eye(len(Q))+ALPHA*Gt, b)
    return r0,phi,phit,Q

def stagger(Q,phi,r0):
    m=(r0>=0.4)&(r0<=2.0)
    T=cKDTree(Q)
    pr=T.query_pairs(L_EDGE*1.001,output_type='ndarray')
    pr=pr[m[pr[:,0]]&m[pr[:,1]]]
    flip=(np.sign(phi[pr[:,0]])!=np.sign(phi[pr[:,1]])).mean()
    return flip,(phi[m]<0).mean()

def env_fit(r0,phi,lo,hi,bw=0.05):
    bins=np.arange(0.3,2.4,bw); rc,fab=[],[]
    for b in bins:
        m=(r0>=b)&(r0<b+bw)
        if m.sum()>=3: rc.append(r0[m].mean()); fab.append(np.abs(phi[m]).mean())
    rc,fab=np.array(rc),np.array(fab)
    w=(rc>=lo)&(rc<=hi)&(fab>0)
    c=np.polyfit(rc[w],np.log(fab[w]*rc[w]),1)
    y=np.log(fab[w]*rc[w]); yh=np.polyval(c,rc[w])
    r2=1-np.sum((y-yh)**2)/np.sum((y-np.mean(y))**2)
    return -1.0/c[0], r2

WINDOWS=[(0.45,1.3),(0.55,1.6),(0.7,1.8)]
M9=int(9/math.sqrt(2/3))+2
builders={"A0-FCC-ball":lambda R: fcc_ball(R),
          "A1-HCP-ball":lambda R: layered_ball(R,hcp_seq(M9))}

deltas=[]; per_arena={}
for name,b in builders.items():
    print(f"\n== {name} ==")
    ds=[]
    for R in (7,9):
        P=b(R); sanity(P,f"{name} R={R}")
        r0,phi,phit,Q=solve_pair(P)
        f0,n0=stagger(Q,phi ,r0); f1,n1=stagger(Q,phit,r0)
        print(f"    R={R} staggering  baseline: flip={f0:.3f} neg={n0:.3f}   "
              f"corrected: flip={f1:.3f} neg={n1:.3f}")
        for lo,hi in WINDOWS:
            l0,q0=env_fit(r0,phi ,lo,hi)
            l1,q1=env_fit(r0,phit,lo,hi)
            d=l1/l0-1.0; ds.append(d); deltas.append(d)
            print(f"    R={R} window {lo:.2f}-{hi:.2f}: "
                  f"l_base={l0:.4f} (R2={q0:.3f})  l_L2={l1:.4f} (R2={q1:.3f})  "
                  f"delta={100*d:+.2f}%")
        if name=="A0-FCC-ball" and R==9:
            # deliverable (i): chi(r) profile on the nn axis between two
            # adjacent sites and radially around a site. chi(r) = sum_j q_j
            # rho_hat(|r-r_j|), q_j = -ALPHA*psi_j (corrected solution).
            qj=-ALPHA*phit
            T=cKDTree(Q); ctr=int(np.argmin(np.linalg.norm(Q-Q.mean(0),axis=1)))
            nb=T.query_ball_point(Q[ctr],L_EDGE*1.001); nb.remove(ctr)
            # pick the neighbour with the largest |q| opposite sign if any
            opp=[j for j in nb if np.sign(qj[j])!=np.sign(qj[ctr])] or nb
            j2=opp[int(np.argmax(np.abs(qj[opp])))]
            A,B=Q[ctr],Q[j2]
            print(f"\n    deliverable (i): chi(r) on nn axis, sites q_A={qj[ctr]:+.3e}"
                  f" q_B={qj[j2]:+.3e} (opposite-sign adjacent pair: "
                  f"{np.sign(qj[ctr])!=np.sign(qj[j2])})")
            print("      t      chi_A        chi_B        chi_net")
            near=T.query_ball_point((A+B)/2, 3.0*L_EDGE)
            for t in np.linspace(0.05,0.95,10):
                x=A+t*(B-A)
                cA=qj[ctr]*KAPPA**2*math.exp(-KAPPA*np.linalg.norm(x-A))/(4*math.pi*np.linalg.norm(x-A))
                cB=qj[j2 ]*KAPPA**2*math.exp(-KAPPA*np.linalg.norm(x-B))/(4*math.pi*np.linalg.norm(x-B))
                cN=sum(qj[j]*KAPPA**2*math.exp(-KAPPA*np.linalg.norm(x-Q[j]))/(4*math.pi*np.linalg.norm(x-Q[j]))
                       for j in near)
                print(f"      {t:.2f}  {cA:+.4e}  {cB:+.4e}  {cN:+.4e}")
    per_arena[name]=(np.mean(ds),np.std(ds))
    print(f"  {name}: delta-ell/ell = {100*np.mean(ds):+.2f}% +/- {100*np.std(ds):.2f}% "
          f"({len(ds)} variants)")

deltas=np.array(deltas)
D3=deltas.mean(); S3=deltas.std()
print(f"\n== paired correction, all {len(deltas)} variants ==")
print(f"delta-ell/ell_LO = {100*D3:+.2f}% +/- {100*S3:.2f}%")
print(f"D3 = |delta| = {100*abs(D3):.2f}%   vs   W = 3.1%   -> "
      f"{'<= W (CONFIRM condition 2 MET)' if abs(D3)<=0.031 else '> W (feeds C2R-CORRECTED at L4)'}")
print(f"ell_derived preview (L4 assembles): 0.0904*(1+{D3:+.4f}) = "
      f"{0.0904*(1+D3):.4f} fm (envelope +/-0.0028 carried at L4)")

# ---- analytic cross-check: homogenized corrected closure ------------------
# 1 + alpha*n*g_hat(k) = 0, g_hat = 4pi kappa^2/(k^2 (k^2+kappa^2)),
# alpha*n = kappa^2/(4pi)  =>  k^4 + kappa^2 k^2 + kappa^4 = 0.
k2=KAPPA**2*complex(-0.5, math.sqrt(3)/2)
k=complex(k2)**0.5
ell_c=1.0/abs(k.imag); lam=2*math.pi/abs(k.real)
print(f"\n== analytic continuum cross-check (OBS-class, non-adjudicative) ==")
print(f"corrected closure poles k^2 = kappa^2(-1 +/- i sqrt3)/2; "
      f"k = {k.real:.4f}{k.imag:+.4f}i /fm")
print(f"continuum decay length 1/Im(k) = {ell_c:.4f} fm ; oscillation "
      f"wavelength 2pi/Re(k) = {lam:.4f} fm  (lattice readout above is the "
      f"adjudicated object; this row is consonance only)")
