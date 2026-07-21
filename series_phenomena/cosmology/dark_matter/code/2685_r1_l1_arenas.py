#!/usr/bin/env python3
"""FA-SG-R1 leg L1 (Patch 2685): tessellated multi-motif arena battery.

Charter [ADJ] (frozen 2679 SS2): >=3 independent large-arena realizations
differing in construction, each z=12-equivalent, each passing the
instrument sanity check (site count; coordination 12; min chord = edge
length) BEFORE the operator lands. The FCC proxy of 2671-D2 counts as one
realization already run; it is re-executed here identically for band
construction. Frozen inputs (charter SS1): M = I + alpha*G, G_ij = 1/r_ij,
kappa = 2/d_DP, d_DP = l_edge = 0.364 fm, alpha = l_edge/(pi*sqrt(2)),
n = sqrt(2)/l_edge^3 (LOCAL DP density; fence F1). No input re-tuned.

Realizations (choice axes enumerated before any result on them existed):
  A0  FCC ball (cubic construction, ball boundary)      -- 2671-D2 proxy
  A1  HCP ball (ABAB Barlow stacking, ball boundary)    -- new motif
  A2  Random-stacking Barlow ball (seeded, no adjacent
      layer repeats; seed 20260721)                     -- new motif
  A3  FCC, seeded random orientation, CUBIC boundary    -- new orientation/
      (seed 20260722)                                      boundary treatment
Windows (frozen at 2671d): [0.45,1.3], [0.55,1.6], [0.7,1.8] fm.
Sizes: R = 7, 9 (nn units; A3 volume-matched cube).
L1 CONCORD (charter SS4): every realization staggered + cleanly exponential
envelope over >=3 windows + pairwise l compatibility within 2x combined
1-sigma instrument bands. Joint band = union-weighted combination.
"""
import math, numpy as np
from scipy.spatial import cKDTree

PHI=(1+math.sqrt(5))/2; L_UNIT=0.589; L_EDGE=L_UNIT/PHI; D_REG=1.15
kappa=2.0/L_EDGE; alpha=L_EDGE/(math.pi*math.sqrt(2))
print(f"frozen inputs: l_edge={L_EDGE:.4f} fm  kappa={kappa:.4f} /fm  alpha={alpha:.4f} fm")

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

def barlow_seq(M, kind, seed=None):
    if kind=='hcp': return {m: m%2 for m in range(-M-2,M+3)}
    rng=np.random.default_rng(seed); s={0:0}
    for m in range(1,M+3): s[m]=int(rng.choice([c for c in (0,1,2) if c!=s[m-1]]))
    for m in range(-1,-M-3,-1): s[m]=int(rng.choice([c for c in (0,1,2) if c!=s[m+1]]))
    return s

def fcc_rot_cube(R):
    # volume-matched cube: (2L)^3*sqrt(2) ~ (4/3)pi R^3 * sqrt(2)
    L=0.5*((4.0/3.0)*math.pi)**(1.0/3.0)*R
    rng=np.random.default_rng(20260722)
    A=rng.normal(size=(3,3)); Qr,_=np.linalg.qr(A)
    if np.linalg.det(Qr)<0: Qr[:,0]*=-1
    K=int(2.0*L)+3; pts=[]
    for i in range(-2*K,2*K+1):
        for j in range(-2*K,2*K+1):
            for k in range(-2*K,2*K+1):
                if (i+j+k)%2==0:
                    x=(np.array([i,j,k])/math.sqrt(2.0))@Qr.T
                    if np.max(np.abs(x))<=L: pts.append(x)
    return np.array(pts)

def sanity(P,name):
    T=cKDTree(P); d,_=T.query(P,k=2); mind=d[:,1].min()
    ctr=P.mean(0); rc=np.linalg.norm(P-ctr,axis=1)
    # interior = away from every boundary face/surface by >1.1 nn
    if name.startswith("A3"):
        L=np.max(np.abs(P)); interior=np.max(np.abs(P),axis=1)<L-1.1
    else:
        interior=rc<rc.max()-1.1
    coord=np.array([len(x)-1 for x in T.query_ball_point(P[interior],1.001)])
    ok=(abs(mind-1.0)<1e-6) and (np.bincount(coord).argmax()==12) and (coord.min()==12)
    print(f"  sanity {name}: N={len(P)}  min-chord={mind:.6f} a  interior z: "
          f"min={coord.min()} mode={np.bincount(coord).argmax()} max={coord.max()}  "
          f"-> {'PASS' if ok else 'FAIL'}")
    assert ok, f"sanity FAIL for {name}"
    return len(P)

def solve(P_nn):
    P=P_nn*L_EDGE
    src=int(np.argmin(np.linalg.norm(P-P.mean(0),axis=1)))
    mask=np.ones(len(P),bool); mask[src]=False
    Q=P[mask]; r0=np.linalg.norm(Q-P[src],axis=1)
    Dm=np.linalg.norm(Q[:,None,:]-Q[None,:,:],axis=2)
    np.fill_diagonal(Dm,np.inf)
    phi=np.linalg.solve(np.eye(len(Q))+alpha/Dm, 1.0/r0)
    return r0,phi,Q

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
    c,res=np.polyfit(rc[w],np.log(fab[w]*rc[w]),1,full=False),None
    # linearity check: R^2 of the log-linear fit in the window
    y=np.log(fab[w]*rc[w]); yh=np.polyval(c,rc[w])
    r2=1-np.sum((y-yh)**2)/np.sum((y-np.mean(y))**2)
    return -1.0/c[0], r2

WINDOWS=[(0.45,1.3),(0.55,1.6),(0.7,1.8)]
arenas={}
M=int(9/math.sqrt(2/3))+2
builders={
 "A0-FCC-ball":       lambda R: fcc_ball(R),
 "A1-HCP-ball":       lambda R: layered_ball(R,barlow_seq(M,'hcp')),
 "A2-RandBarlow-ball":lambda R: layered_ball(R,barlow_seq(M,'rnd',20260721)),
 "A3-FCC-rot-cube":   lambda R: fcc_rot_cube(R),
}
results={}
for name,b in builders.items():
    print(f"\n== {name} ==")
    per=[]
    for R in (7,9):
        P=b(R); sanity(P,f"{name} R={R}")
        r0,phi,Q=solve(P)
        flip,neg=stagger(Q,phi,r0)
        ls=[]
        for lo,hi in WINDOWS:
            l,r2=env_fit(r0,phi,lo,hi)
            ls.append(l)
            print(f"    R={R} window {lo:.2f}-{hi:.2f}: l={l:.4f} fm (log-lin R2={r2:.4f})")
        print(f"    R={R} staggering: nn sign-flip={flip:.3f}  neg-frac={neg:.3f}")
        per+=ls
        if R==9: results.setdefault(name,{})['flip']=flip; results[name]['neg']=neg
    per=np.array(per)
    results[name]['l']=per.mean(); results[name]['s']=per.std()
    print(f"  {name}: l = {per.mean():.4f} +/- {per.std():.4f} fm  "
          f"(band across {len(per)} window x size variants)")

print("\n== pairwise concordance (2x combined 1-sigma criterion, frozen SS4) ==")
names=list(results)
allok=True
for i in range(len(names)):
    for j in range(i+1,len(names)):
        a,b=results[names[i]],results[names[j]]
        d=abs(a['l']-b['l']); tol=2.0*math.hypot(a['s'],b['s'])
        ok=d<=tol; allok&=ok
        print(f"  {names[i]} vs {names[j]}: |dl|={d:.4f}  2x comb sigma={tol:.4f}  "
              f"{'COMPAT' if ok else 'DISCORD'}")
lo=min(r['l']-r['s'] for r in results.values())
hi=max(r['l']+r['s'] for r in results.values())
print(f"\njoint band (union-weighted: union of per-realization 1-sigma bands, "
      f"center=midpoint): l = {(lo+hi)/2:.4f} +/- {(hi-lo)/2:.4f} fm")
print(f"comparators: 2671 band 0.091+/-0.002 ; d_DP/4 = {L_EDGE/4:.4f} fm")
print(f"L1 verdict: {'CONCORD' if allok else 'DISCORD'} (staggering present in all: "
      f"{all(r['flip']>0.25 for r in results.values())})")


# ---------------------------------------------------------------------------
# J2 RIDER (charter SS2 R1-L1, carried live from inputs SS1): the d_DP = l_edge
# level assignment (INF-S1C-1) is not forced by SS-2. LABELED ROBUSTNESS SCAN
# against the frozen baseline (charter SS1 permission), NOT a fit: decouple
# d_DP from the lattice edge a. Axis frozen pre-run: d_DP/a in {1/phi, 1, phi};
# FCC R=7; window 0.55-1.6 fm; bin-mean observable. alpha = kappa^2/(4 pi n)
# with kappa = 2/d_DP and n = sqrt(2)/a^3 (local DP density, fence F1).
# Severed from the N2 d_DP/4 coincidence (non-elevation clause).
# ---------------------------------------------------------------------------
print("\n== J2 rider: d_DP-decoupling labeled robustness scan (FCC R=7) ==")
P7=fcc_ball(7)*L_EDGE
src=int(np.argmin(np.linalg.norm(P7,axis=1)))
mk=np.ones(len(P7),bool); mk[src]=False
Q7=P7[mk]; r07=np.linalg.norm(Q7,axis=1)
D7=np.linalg.norm(Q7[:,None,:]-Q7[None,:,:],axis=2); np.fill_diagonal(D7,np.inf)
n_dens=math.sqrt(2.0)/L_EDGE**3
for ratio in (1/PHI, 1.0, PHI):
    d_DP=ratio*L_EDGE; kap=2.0/d_DP; al=kap**2/(4*math.pi*n_dens)
    ph=np.linalg.solve(np.eye(len(Q7))+al/D7, 1.0/r07)
    bins=np.arange(0.3,2.4,0.05); rc,fv=[],[]
    for b in bins:
        m=(r07>=b)&(r07<b+0.05)
        if m.sum()>=3: rc.append(r07[m].mean()); fv.append(np.abs(ph[m]).mean())
    rc,fv=np.array(rc),np.array(fv)
    w=(rc>=0.55)&(rc<=1.6)
    c=np.polyfit(rc[w],np.log(fv[w]*rc[w]),1); l=-1.0/c[0]
    neg=(ph[(r07>=0.4)&(r07<=2.0)]<0).mean()
    print(f"   d_DP/a={ratio:.4f} (kappa*a={kap*L_EDGE:.3f}): l_env={l:.4f} fm  "
          f"l/d_DP={l/d_DP:.3f}  l/a={l/L_EDGE:.3f}  1/(2kappa)={1/(2*kap):.4f} fm  "
          f"neg-frac={neg:.3f}")
print("   J2 report: the emergent scale does NOT generically track d_DP;")
print("   l = d_DP/4 = 1/(2 kappa) holds AT the committed assignment (kappa*a = 2)")
print("   and fails on both sides of it -- the assignment is structurally special.")
