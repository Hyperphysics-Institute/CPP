#!/usr/bin/env python3
"""AUTOMATON-2 ENGINE (Patch 2802) under the ratified C19-C30 spec +
frozen 2801 execution prereg. FCC even-parity sublattice, native
12-neighbor adjacency; field rule = directed-front kernel W_R
(translation-invariance reduction of the C22 origin-directed hop
relay); CP rule = C19/C20 verbatim, NOTHING added.
Stages: g1 | g2 | g3 | run R chunk | (analysis in 2803)."""
import sys, math, pickle, os, json
import numpy as np, itertools

os.makedirs("/tmp/auto2",exist_ok=True)
NN=[d for d in itertools.product((-1,0,1),repeat=3) if sorted(map(abs,d))==[0,1,1]]

def front_kernel(R,extent=13):
    """Directed outward 12-neighbor relay from origin, R hops.
    Returns dict {delta:(weight)} on the graph-distance-R front."""
    g={(0,0,0):1.0}
    for hop in range(R):
        gn={}
        for (p,w) in g.items():
            d0=math.sqrt(p[0]**2+p[1]**2+p[2]**2)
            outs=[tuple(p[i]+d[i] for i in range(3)) for d in NN
                  if math.sqrt((p[0]+d[0])**2+(p[1]+d[1])**2+(p[2]+d[2])**2)>d0+1e-9]
            for q in outs: gn[q]=gn.get(q,0.0)+w/len(outs)
        g=gn
    assert abs(sum(g.values())-1.0)<1e-9
    return g

def kernels(M,R):
    W=front_kernel(R)
    K=np.zeros((M,M,M)); UX=np.zeros((M,M,M)); UY=np.zeros((M,M,M)); UZ=np.zeros((M,M,M))
    for (d,w) in W.items():
        i,j,k=(d[0]%M,d[1]%M,d[2]%M)
        r=math.sqrt(d[0]**2+d[1]**2+d[2]**2)
        K[i,j,k]+=w
        UX[i,j,k]+=w*d[0]/r; UY[i,j,k]+=w*d[1]/r; UZ[i,j,k]+=w*d[2]/r
    F=np.fft.rfftn
    return {"K":F(K),"ux":F(UX),"uy":F(UY),"uz":F(UZ),"M":M,"R":R,"front":len(W)}

def moment(Q,inj,kern):
    pay=Q+inj; M=kern["M"]
    P=np.fft.rfftn(pay); Pa=np.fft.rfftn(np.abs(pay))
    irf=lambda A: np.fft.irfftn(A,s=(M,M,M),axes=(0,1,2))
    return (irf(P*kern["K"]),irf(P*kern["ux"]),irf(P*kern["uy"]),
            irf(P*kern["uz"]),np.maximum(irf(Pa*kern["K"]),0.0))

def fcc_sites(M):
    idx=np.indices((M,M,M)).reshape(3,-1).T
    return idx[(idx.sum(1)%2)==0]

def snap_fcc(p,M):
    """nearest even-parity site to continuum point p (per-CP)."""
    c=np.rint(p).astype(int)
    if (c.sum())%2==0: return c%M
    best=None; bd=1e9
    for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        q=c+np.array(d); dist=np.sum((p-q)**2)
        if dist<bd: bd=dist; best=q
    return best%M

def cp_step(pos,sig,Vx,Vy,Vz,Aab,R,M):
    out=pos.copy()
    i,j,k=pos[:,0],pos[:,1],pos[:,2]
    vx=Vx[i,j,k]; vy=Vy[i,j,k]; vz=Vz[i,j,k]; ab=Aab[i,j,k]
    vn=np.sqrt(vx*vx+vy*vy+vz*vz)
    for c in range(len(pos)):
        if vn[c]<=1e-12 or ab[c]<=1e-12: continue
        d=min(vn[c]/ab[c],1.0)*R
        tgt=pos[c]+sig[c]*d*np.array([vx[c],vy[c],vz[c]])/vn[c]
        out[c]=snap_fcc(tgt,M)
    return out

def inj_field(pos,sig,M):
    f=np.zeros((M,M,M))
    np.add.at(f,(pos[:,0],pos[:,1],pos[:,2]),sig)
    return f

if sys.argv[1]=="g1":
    import importlib.util
    spec=importlib.util.spec_from_file_location("ew","code/2798_ewald_comparator.py")
    ew=importlib.util.module_from_spec(spec); spec.loader.exec_module(ew)
    M=48; npass=0
    for R in (2,3,4):
        kern=kernels(M,R)
        sites=fcc_sites(M)
        inj=np.zeros((M,M,M))
        inj[tuple(sites.T)]=-1.0/len(sites)
        inj[0,0,0]+=1.0
        Q=np.zeros((M,M,M)); acc=None; nav=0
        for t in range(6*M):
            Q,Vx,Vy,Vz,Aab=moment(Q,inj,kern)
            if t>=4*M:
                v=np.sqrt(Vx**2+Vy**2+Vz**2); acc=v if acc is None else acc+v; nav+=1
        vbar=acc/nav
        rs=np.array([r for r in range(2*R+2,17) if r%2==0])   # FCC parity: even axis sites only
        va=[np.mean([vbar[r,0,0],vbar[0,r,0],vbar[0,0,r],vbar[-r,0,0],vbar[0,-r,0],vbar[0,0,-r]]) for r in rs]
        Ee=np.linalg.norm(ew.ewald_E([(float(r),0.,0.) for r in rs],M),axis=1)
        rho=np.array(va)/Ee; rho/=rho.mean()
        pa=-np.polyfit(np.log(rs),np.log(va),1)[0]; pe=-np.polyfit(np.log(rs),np.log(Ee),1)[0]
        ok=(rho.min()>=0.90)&(rho.max()<=1.10)&(abs(pa-pe)<=0.15)
        npass+=ok
        print(f"G1 R={R}: front GPs={kern['front']}; window even r in [{rs[0]},{rs[-1]}]; "
              f"norm rho [{rho.min():.3f},{rho.max():.3f}]; p_auto={pa:.3f} vs p_Ewald={pe:.3f} "
              f"(dp={abs(pa-pe):.3f}) -> {'PASS' if ok else 'FAIL'}")
    print(f"G1: {npass}/3 -> {'GATE OPEN' if npass>=2 else 'FAIL-STOP'}")
    sys.exit(0 if npass>=2 else 1)

if sys.argv[1] in ("g2","g3"):
    M=24; R=3; N=864
    kern=kernels(M,R)
    rng=np.random.default_rng(2801+R)
    sites=fcc_sites(M)
    pos=sites[rng.choice(len(sites),N,replace=False)].copy()
    sig=np.array([1]*(N//2)+[-1]*(N//2)); rng.shuffle(sig)
    Q=np.zeros((M,M,M)); l1=[]; movers=[]
    T=20000 if sys.argv[1]=="g3" else 10000
    ck=f"/tmp/auto2/{sys.argv[1]}_state.pkl"
    t0=0
    if os.path.exists(ck):
        st=pickle.load(open(ck,"rb")); pos,sig,Q,t0,l1,movers=st
    chunk=int(sys.argv[2]) if len(sys.argv)>2 else T-t0
    for t in range(t0,min(t0+chunk,T)):
        inj=inj_field(pos,sig,M)
        Q,Vx,Vy,Vz,Aab=moment(Q,inj,kern)
        new=cp_step(pos,sig,Vx,Vy,Vz,Aab,R,M)
        movers.append(float((new!=pos).any(axis=1).mean()))
        pos=new
        if t%200==0: l1.append(float(np.abs(Q).sum()))
    pickle.dump((pos,sig,Q,min(t0+chunk,T),l1,movers),open(ck,"wb"))
    t1=min(t0+chunk,T)
    print(f"[{sys.argv[1]}] {t1}/{T} Moments; recent mover fraction={np.mean(movers[-min(1000,len(movers)):]):.3f}")
    if t1==T:
        if sys.argv[1]=="g2":
            l1=np.array(l1); half=len(l1)//2
            trend=(l1[half:].mean()-l1[:half].mean())/max(l1[:half].mean(),1e-12)
            net=Q.sum()
            ok=(abs(net)<1e-6) and (abs(trend)<0.10)
            print(f"G2: net charge={net:.2e}; L1 trend={trend*100:+.1f}% -> {'PASS' if ok else 'FAIL-STOP'}")
        else:
            mf=np.mean(movers[-T//4:])
            # clusters at distance <=1.5 among final positions
            d=pos[:,None,:]-pos[None,:,:]; d=(d+M//2)%M-M//2
            D=np.sqrt((d**2).sum(2))
            adj=(D<=1.5)&(D>1e-9)
            lab=-np.ones(N,int); nl=0
            for i in range(N):
                if lab[i]>=0: continue
                stack=[i]; lab[i]=nl
                while stack:
                    a=stack.pop()
                    for b in np.where(adj[a]&(lab<0))[0]:
                        lab[b]=nl; stack.append(b)
                nl+=1
            import collections
            cs=collections.Counter(collections.Counter(lab.tolist()).values())
            insmall=sum(k*v for k,v in cs.items() if k<=2)/N
            mx=max(k for k in cs)
            ok=(mf>=0.20) and (insmall>=0.60) and (mx<=8)
            print(f"G3: mover fraction (final quarter)={mf:.3f} (>=0.20); "
                  f"CPs in clusters<=2: {insmall*100:.0f}% (>=60%); max cluster={mx} (<=8); "
                  f"cluster census={dict(sorted(cs.items()))} -> {'PASS -- THE SEA IS ALIVE' if ok else 'FAIL (quench class)'}")
