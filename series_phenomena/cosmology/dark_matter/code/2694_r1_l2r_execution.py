#!/usr/bin/env python3
"""FA-SG-R1-L2R execution (Patch 2694) under the FROZEN 2693 charter.
All predictions, ensembles, classifiers, and tolerance constructions are
the charter's; nothing here was chosen after results existed.
Part A: staggering-onset sweep. Part B: 17-way structural class.
Part C: dimensionless-observable consistency, ensemble-self-calibrated."""
import itertools, math, numpy as np

PHI=(1+math.sqrt(5))/2; L_UNIT=0.589; A=L_UNIT/PHI
alpha=A/(math.pi*math.sqrt(2))

def solve(P,src):
    mask=np.ones(len(P),bool); mask[src]=False
    Q=P[mask]; r0=np.linalg.norm(Q-P[src],axis=1)
    D=np.linalg.norm(Q[:,None,:]-Q[None,:,:],axis=2); np.fill_diagonal(D,np.inf)
    f=np.linalg.solve(np.eye(len(Q))+alpha/D,1.0/r0)
    return r0,f
def shellprof(r0,f):
    sh=sorted(set(np.round(r0,6))); rl,fl=[],[]
    for s in sh:
        m=np.abs(r0-s)<1e-6; rl.append(s); fl.append(f[m].mean())
    return np.array(rl),np.array(fl)
def obs(r0,f,edge):
    rl,fl=shellprof(r0,f)
    O1=(f<0).mean()
    # O2: nn sign-flip over graph edges of the arena
    # (computed on full site set incl. distances = minimal chord)
    return O1,rl,fl
def classify(rl,fl,O1):
    g=np.abs(fl)*rl; best_fm=0.0; best_sh=0; i=0
    while i<len(rl):
        j=i
        while j+1<len(rl) and np.sign(fl[j+1])==np.sign(fl[i]) and g[j+1]<=g[j]: j+=1
        best_fm=max(best_fm,rl[j]-rl[i]); best_sh=max(best_sh,j-i+1); i=j+1
    return (O1>=0.25) and (best_fm<0.3), best_sh
def nnflip(P,src,f_full,edge):
    # f_full indexed over response sites; map back
    mask=np.ones(len(P),bool); mask[src]=False
    idx=np.where(mask)[0]
    val=np.zeros(len(P)); val[idx]=f_full
    from scipy.spatial import cKDTree
    T=cKDTree(P); prs=T.query_pairs(edge*1.001,output_type='ndarray')
    flips=0; tot=0
    for a,b in prs:
        if a==src or b==src: continue
        tot+=1; flips+= (np.sign(val[a])!=np.sign(val[b]))
    return flips/tot

def fcc_ball_r(rad_fm):
    pts=[]; R=int(rad_fm/A)+2
    for i in range(-2*R,2*R+1):
        for j in range(-2*R,2*R+1):
            for k in range(-2*R,2*R+1):
                if (i+j+k)%2==0:
                    x=np.array([i,j,k])/math.sqrt(2.0)*A
                    if np.linalg.norm(x)<=rad_fm+1e-9: pts.append(x)
    return np.array(pts)
def layered_ball_r(rad_fm,seq):
    dz=math.sqrt(2.0/3.0); e1=np.array([1.0,0.0]); e2=np.array([0.5,math.sqrt(3)/2])
    offs=[np.array([0.0,0.0]),np.array([0.5,math.sqrt(3)/6]),np.array([1.0,math.sqrt(3)/3])]
    pts=[]; M=int(rad_fm/(dz*A))+2; K=int(rad_fm/A)+3
    for m in range(-M,M+1):
        z=m*dz*A; o=offs[seq[m]]
        for p in range(-2*K,2*K+1):
            for q in range(-2*K,2*K+1):
                xy=(p*e1+q*e2+o)*A
                if xy@xy+z*z<=rad_fm**2+1e-9: pts.append([xy[0],xy[1],z])
    return np.array(pts)

print("== PART A: staggering-onset sweep (frozen N ladder via radius truncation) ==")
prev=None; Nstar=None; curve=[]
for rad in (0.40,0.52,0.60,0.75,0.85,0.95,1.00,1.05,1.15,1.25):
    P=fcc_ball_r(rad); src=int(np.argmin(np.linalg.norm(P,axis=1)))
    r0,f=solve(P,src); nf=(f<0).mean(); curve.append((len(P),nf))
    print(f"   N={len(P):4d} (r<={rad:.2f} fm): neg-frac={nf:.3f}")
for i,(N,nf) in enumerate(curve):
    if nf>=0.25 and all(nf2>=0.25 for _,nf2 in curve[i:]): Nstar=N; break
print(f"   ONSET N* = {Nstar}  ->  P-A (N* exists and < 120): {'HOLDS' if (Nstar is not None and Nstar<120) else 'FAILS'}")

print("\n== PART B/C: ensemble E (15 members) + I1 (both metrics) ==")
rng=np.random.default_rng(20260723)
seq={}; last=-1
for m in range(-30,31):
    c=[x for x in (0,1,2) if x!=last]; seq[m]=int(rng.choice(c)); last=seq[m]
arenas=[("FCC r1.00",fcc_ball_r(1.00)),("HCP r1.00",layered_ball_r(1.00,{m:m%2 for m in range(-30,31)})),
        ("RandB r1.00",layered_ball_r(1.00,seq)),("FCC r0.95",fcc_ball_r(0.95)),("FCC r1.05",fcc_ball_r(1.05))]
ensO=[]
for name,P in arenas:
    d=np.linalg.norm(P[:,None,:]-P[None,:,:],axis=2); np.fill_diagonal(d,np.inf)
    edge=d.min()
    center=int(np.argmin(np.linalg.norm(P-P.mean(0),axis=1)))
    dc=np.linalg.norm(P-P[center],axis=1); order=np.argsort(dc)
    srcs=[center,int(order[1]),int(order[2])]
    for src in srcs:
        r0,f=solve(P,src); rl,fl=shellprof(r0,f)
        O1=(f<0).mean(); osc,run_sh=classify(rl,fl,O1); O2=nnflip(P,src,f,edge)
        ensO.append((O1,O2,run_sh,osc))
        print(f"   {name:12s} N={len(P):3d} src@{src:3d}: O1={O1:.3f} O2={O2:.3f} O3={run_sh} class={'OSC' if osc else 'CLEAN'}")
allosc_E=all(o[3] for o in ensO)

# I1 both metrics
verts=[]
for s in itertools.product([0.5,-0.5],repeat=4): verts.append(s)
for i in range(4):
    for s in (1.0,-1.0):
        v=[0.0]*4; v[i]=s; verts.append(tuple(v))
ep=[(0,1,2,3),(0,2,3,1),(0,3,1,2),(1,0,3,2),(1,2,0,3),(1,3,2,0),(2,0,1,3),(2,1,3,0),(2,3,0,1),(3,0,2,1),(3,1,0,2),(3,2,1,0)]
base=(PHI/2,0.5,1/(2*PHI),0.0); seen=set()
for perm in ep:
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                v=[0.0]*4; vals=(s1*base[0],s2*base[1],s3*base[2],0.0)
                for k in range(4): v[perm[k]]=vals[k]
                t=tuple(round(x,9) for x in v)
                if t not in seen: seen.add(t); verts.append(t)
V=np.array(verts); D4=np.linalg.norm(V[:,None,:]-V[None,:,:],axis=2)*L_UNIT
dmin=D4[D4>1e-9].min()
Dg=np.where(np.abs(D4-dmin)<1e-6,1.0,1e9); np.fill_diagonal(Dg,0.0)
for k in range(120): Dg=np.minimum(Dg,Dg[:,k][:,None]+Dg[k,:][None,:])
Dg*=A
i1O={}
for lbl,D in (("chord",D4),("geodesic",Dg)):
    resp=np.arange(1,120); r0=D[0,resp]
    G=np.zeros((119,119))
    for a_ in range(119):
        for b_ in range(119):
            if a_!=b_: G[a_,b_]=1.0/D[resp[a_],resp[b_]]
    f=np.linalg.solve(np.eye(119)+alpha*G,1.0/r0)
    rl,fl=shellprof(r0,f); O1=(f<0).mean(); osc,run_sh=classify(rl,fl,O1)
    val=np.zeros(120); val[resp]=f
    prs=np.argwhere(np.abs(D4-dmin)<1e-6); flips=0; tot=0
    for a_,b_ in prs:
        if a_<b_ and a_!=0 and b_!=0:
            tot+=1; flips+=(np.sign(val[a_])!=np.sign(val[b_]))
    O2=flips/tot
    i1O[lbl]=(O1,O2,run_sh,osc)
    print(f"   I1 {lbl:9s}          : O1={O1:.3f} O2={O2:.3f} O3={run_sh} class={'OSC' if osc else 'CLEAN'}")

print(f"\nPASS-B (all 15 ensemble + both I1 metrics OSC): "
      f"{'PASS' if allosc_E and all(v[3] for v in i1O.values()) else 'FAIL'}")

print("\n== PART C: bands = ensemble [min,max] expanded by I1 metric spread ==")
res={}
for k,name in ((0,'O1'),(1,'O2'),(2,'O3')):
    lo=min(o[k] for o in ensO); hi=max(o[k] for o in ensO)
    spread=abs(i1O['chord'][k]-i1O['geodesic'][k])
    lo2,hi2=lo-spread,hi+spread
    inb={lbl:(lo2-1e-12<=i1O[lbl][k]<=hi2+1e-12) for lbl in i1O}
    res[name]=inb
    print(f"   {name}: ensemble [{lo:.3f},{hi:.3f}] spread {spread:.3f} -> band [{lo2:.3f},{hi2:.3f}] ; "
          f"I1 chord={i1O['chord'][k]:.3f} in={inb['chord']} ; geodesic={i1O['geodesic'][k]:.3f} in={inb['geodesic']}")
passC=all(sum(res[n][lbl] for n in res)>=2 for lbl in ('chord','geodesic'))
print(f"PASS-C (>=2 of 3 per metric): {'PASS' if passC else 'FAIL'}")
print("\nGeometric fact (Copilot): diameter-matched 3D ball at 1.18 fm holds "
      f"{len(fcc_ball_r(0.60))} sites vs I1's 120 -- joint diameter+count matching requires the 3-sphere.")
