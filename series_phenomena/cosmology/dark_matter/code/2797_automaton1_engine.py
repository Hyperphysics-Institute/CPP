#!/usr/bin/env python3
"""AUTOMATON-1 ENGINE (Patch 2797) under the FROZEN 2796 prereg.
The founder's Moment rule, verbatim commitments 14-18 + DR-1..DR-3:
synchronous; periodic M^3; payload = net charge relay / |S_R| shell;
SSV_net vector sum, SSV_abs gross sum; d = (|net|/abs)*R along
sigma_c*SSV_net; zero-net stasis; carriers erased; self-parcel
structurally excluded (shell excludes distance 0).
Stages: v1 | v2 | v3 (gates, BLOCKING) | run R | bias R axis | analyze."""
import sys, math, json, pickle, os
import numpy as np

os.makedirs("/tmp/auto1",exist_ok=True)

def kernels(M,R):
    ax=np.arange(M); axm=np.minimum(ax,M-ax)
    X=axm[:,None,None]; Y=axm[None,:,None]; Z=axm[None,None,:]
    D=np.sqrt(X**2+Y**2+Z**2)
    # signed minimum-image displacement components for unit vectors
    sx=np.where(ax<=M//2,ax,ax-M)
    DX=sx[:,None,None]*np.ones((1,M,M)); DY=sx[None,:,None]*np.ones((M,1,M)); DZ=sx[None,None,:]*np.ones((M,M,1))
    shell=(D>R-0.5)&(D<=R+0.5)
    S=int(shell.sum())
    with np.errstate(invalid='ignore',divide='ignore'):
        ux=np.where(shell,DX/np.maximum(D,1e-9),0.0)/S
        uy=np.where(shell,DY/np.maximum(D,1e-9),0.0)/S
        uz=np.where(shell,DZ/np.maximum(D,1e-9),0.0)/S
    K=shell.astype(float)/S
    F=lambda a: np.fft.rfftn(a)
    return {"S":S,"K":F(K),"ux":F(ux),"uy":F(uy),"uz":F(uz),"M":M,"R":R,
            "aniso":(abs(np.sum(shell*np.abs(DX))-np.sum(shell*np.abs(DY))),abs(np.sum(shell*np.abs(DX))-np.sum(shell*np.abs(DZ))),np.sum(shell*np.abs(DX)))}

def moment(Q,inj,kern):
    """One synchronous Moment. Q: net charge field (from t-1 aggregation).
    Returns new Q, SSV vector field components, SSV_abs field."""
    pay=Q+inj
    P=np.fft.rfftn(pay); Pa=np.fft.rfftn(np.abs(pay))
    M=kern["M"]
    irf=lambda A: np.fft.irfftn(A,s=(M,M,M))
    Qn=irf(P*kern["K"])
    Vx=irf(P*kern["ux"]); Vy=irf(P*kern["uy"]); Vz=irf(P*kern["uz"])
    Aab=irf(Pa*kern["K"])
    return Qn,Vx,Vy,Vz,np.maximum(Aab,0.0)

def cp_step(pos,sig,Vx,Vy,Vz,Aab,R,M):
    i,j,k=pos[:,0],pos[:,1],pos[:,2]
    vx=Vx[i,j,k]; vy=Vy[i,j,k]; vz=Vz[i,j,k]; ab=Aab[i,j,k]
    vn=np.sqrt(vx*vx+vy*vy+vz*vz)
    move=(vn>1e-12)&(ab>1e-12)
    d=np.where(move,np.minimum(vn/np.maximum(ab,1e-12),1.0)*R,0.0)
    sc=np.where(move,sig*d/np.maximum(vn,1e-12),0.0)
    np_=pos+np.rint(np.stack([vx,vy,vz],1)*sc[:,None]).astype(int)
    return np_%M

def inj_field(pos,sig,M):
    inj=np.zeros((M,M,M))
    np.add.at(inj,(pos[:,0],pos[:,1],pos[:,2]),sig)
    return inj

if sys.argv[1]=="v1":
    M,R=32,3; kern=kernels(M,R)
    posP=np.array([[0,0,0]]); posN=np.array([[M//2,M//2,M//2]])
    inj=np.zeros((M,M,M)); inj[0,0,0]=1.0; inj[M//2,M//2,M//2]=-1.0
    Q=np.zeros((M,M,M)); acc=None; nav=0
    for t in range(6*M):
        Q,Vx,Vy,Vz,Aab=moment(Q,inj,kern)
        if t>=4*M:
            vmag=np.sqrt(Vx**2+Vy**2+Vz**2)
            acc=vmag if acc is None else acc+vmag; nav+=1
    vbar=acc/nav
    rs=np.arange(2*R,M//3+1)
    vals=[np.mean([vbar[r,0,0],vbar[0,r,0],vbar[0,0,r],vbar[-r,0,0],vbar[0,-r,0],vbar[0,0,-r]]) for r in rs]
    co=np.polyfit(np.log(rs),np.log(vals),1); p=-co[0]
    ok=1.8<=p<=2.2
    print(f"V-1: static dipole field |V|(r) axes fit r^-p, p = {p:.3f} over r in [{rs[0]},{rs[-1]}] -> {'PASS' if ok else 'FAIL-STOP'}")
    for r,v in zip(rs,vals): print(f"   r={r}: |V|={v:.3e}")
    sys.exit(0 if ok else 1)

if sys.argv[1]=="v2":
    M,R=24,3; kern=kernels(M,R)
    rng=np.random.default_rng(2796)
    N=432; pos=rng.integers(0,M,size=(N,3)); sig=np.array([1]*(N//2)+[-1]*(N//2))
    Q=np.zeros((M,M,M)); l1=[]
    for t in range(10000):
        inj=inj_field(pos,sig,M)
        Q,Vx,Vy,Vz,Aab=moment(Q,inj,kern)
        pos=cp_step(pos,sig,Vx,Vy,Vz,Aab,R,M)
        if t%100==0: l1.append(np.abs(Q).sum())
    l1=np.array(l1)
    netQ=Q.sum()
    half=len(l1)//2
    trend=(l1[half:].mean()-l1[:half].mean())/l1[:half].mean()
    ok=(abs(netQ)<1e-6) and (abs(trend)<0.10)
    print(f"V-2: net charge = {netQ:.2e} (exact conservation {'OK' if abs(netQ)<1e-6 else 'FAIL'}); "
          f"L1 second-half/first-half trend = {trend*100:+.1f}% -> {'PASS' if ok else 'FAIL-STOP'}")
    print(f"   L1 trace (every 1000 M): {np.array2string(l1[::10],precision=1)}")
    sys.exit(0 if ok else 1)

if sys.argv[1]=="v3":
    ok=True
    for R in (2,3,4):
        kern=kernels(24,R)
        a1,a2,tot=kern["aniso"]
        an=max(a1,a2)/tot
        print(f"V-3: R={R} shell |S|={kern['S']} dipole-moment axis anisotropy = {an*100:.2f}% -> {'PASS' if an<=0.02 else 'FAIL'}")
        ok&=(an<=0.02)
    sys.exit(0 if ok else 1)

if sys.argv[1]=="run":
    R=int(sys.argv[2]); M=24; N=432
    WARM=20000; PROD=80000; EVERY=20
    kern=kernels(M,R)
    ck=f"/tmp/auto1/run_R{R}.pkl"
    if os.path.exists(ck):
        st=pickle.load(open(ck,"rb")); pos=st["pos"]; sig=st["sig"]; Q=st["Q"]; t0=st["t"]; samples=st["samples"]
    else:
        rng=np.random.default_rng(2796+R)
        pos=rng.integers(0,M,size=(N,3)); sig=np.array([1]*(N//2)+[-1]*(N//2)); Q=np.zeros((M,M,M)); t0=0; samples=[]
    T=WARM+PROD
    chunk=int(sys.argv[3]) if len(sys.argv)>3 else T-t0
    tend=min(t0+chunk,T)
    for t in range(t0,tend):
        inj=inj_field(pos,sig,M)
        Q,Vx,Vy,Vz,Aab=moment(Q,inj,kern)
        pos=cp_step(pos,sig,Vx,Vy,Vz,Aab,R,M)
        if t>=WARM and (t-WARM)%EVERY==0:
            samples.append(pos.copy().astype(np.int8))
    pickle.dump({"pos":pos,"sig":sig,"Q":Q,"t":tend,"samples":samples},open(ck,"wb"))
    print(f"[R={R}] {tend}/{T} Moments  samples={len(samples)}")
    if tend==T: print(f"[R={R}] COMPLETE")

if sys.argv[1]=="bias":
    R=int(sys.argv[2]); axis=int(sys.argv[3]); M=24; N=432; EPS=0.02
    kern=kernels(M,R)
    st=pickle.load(open(f"/tmp/auto1/run_R{R}.pkl","rb"))
    pos=st["pos"].copy(); sig=st["sig"].copy(); Q=st["Q"].copy()
    dip=[]
    for t in range(10000):
        inj=inj_field(pos,sig,M)
        Q,Vx,Vy,Vz,Aab=moment(Q,inj,kern)
        V=[Vx,Vy,Vz]; V[axis]=V[axis]+EPS
        pos=cp_step(pos,sig,V[0],V[1],V[2],Aab,R,M)
        if t%20==0 and t>2000:
            sx=np.where(np.arange(M)<=M//2,np.arange(M),np.arange(M)-M)
            com=np.array([ (sig*sx[pos[:,a]]).mean() for a in range(3)])
            dip.append(com)
    dip=np.array(dip).mean(0)
    print(f"[R={R} axis={axis}] biased-run signed dipole response = {np.array2string(dip,precision=4)}")
    json.dump(dip.tolist(),open(f"/tmp/auto1/bias_R{R}_a{axis}.json","w"))
