#!/usr/bin/env python3
"""VELOCITY-PROXY DIAGNOSTIC (Patch 2811) — founder-approved proxy run.
NOT a doctrine change: C23 (no velocity memory; inertia in Sea arc
configuration) stands. Here a per-CP velocity vector is a LABELED PROXY
for arc-stored inertia, run to answer one question: with momentum
present, do the founder's kinetic trajectories / collisions / rebounds /
thermalization appear? Founder's stated caveat carried: a hard-coded
velocity cannot represent all energy-transfer and axis-change variables
exactly; artifacts are possible and are looked for explicitly.

[W] proxy law (declared): v_{t+1} = v_t + eta * sigma_c * SSV_net_hat *
(|SSV_net|/SSV_abs); x_{t+1} = x_t + v_{t+1} (continuum position, snapped
only for field sampling). Collision (CP pair within d_coll) -> ZBW axis
re-randomization implemented as an elastic exchange plus a random
transverse kick of the pair's relative velocity (founder: 'varying the
DP ZBW oscillation axis with each collision'), energy-conserving.
Sub-GP position accumulation is intrinsic to the proxy (positions are
continuous), which also removes the 0.5-GP snap floor.
Usage: eta n_dp moments"""
import sys, math
import numpy as np

M=64; R=6
src=open('code/2802_automaton2_engine.py').read().split('if sys.argv[1]')[0]
ns={}; exec(src,ns)
kernels=ns['kernels']; inj_field_int=ns['inj_field']
kern=kernels(M,R)
irf=lambda A: np.fft.irfftn(A,s=(M,M,M),axes=(0,1,2))

def fields(pos,sig,Q):
    idx=np.rint(pos).astype(int)%M
    inj=np.zeros((M,M,M)); np.add.at(inj,(idx[:,0],idx[:,1],idx[:,2]),sig)
    pay=Q+inj
    P=np.fft.rfftn(pay); Pa=np.fft.rfftn(np.abs(pay))
    Qn=irf(P*kern["K"]); Vx=irf(P*kern["ux"]); Vy=irf(P*kern["uy"]); Vz=irf(P*kern["uz"])
    Ab=np.maximum(irf(Pa*kern["K"]),0.0)
    return Qn,Vx,Vy,Vz,Ab,idx

def run(eta,nDP,T,seed=2811,d_coll=1.0,report=True):
    rng=np.random.default_rng(seed)
    cen=rng.uniform(0,M,size=(nDP,3))
    pos=[]; sig=[]
    for c in range(nDP):
        u=rng.normal(size=3); u/=np.linalg.norm(u)
        pos.append(cen[c]+u*2.0); sig.append(+1)
        pos.append(cen[c]-u*2.0); sig.append(-1)
    pos=np.array(pos); sig=np.array(sig,float); N=len(pos)
    vel=np.zeros((N,3))
    Q=np.zeros((M,M,M))
    cens=[]; vels=[]; ncoll=0
    for t in range(T):
        Q,Vx,Vy,Vz,Ab,idx=fields(pos,sig,Q)
        vx=Vx[idx[:,0],idx[:,1],idx[:,2]]; vy=Vy[idx[:,0],idx[:,1],idx[:,2]]
        vz=Vz[idx[:,0],idx[:,1],idx[:,2]]; ab=Ab[idx[:,0],idx[:,1],idx[:,2]]
        vn=np.sqrt(vx*vx+vy*vy+vz*vz)
        ok=(vn>1e-12)&(ab>1e-12)
        acc=np.zeros((N,3))
        mag=np.where(ok,np.minimum(vn/np.maximum(ab,1e-12),1.0),0.0)
        acc[ok]=(sig[ok,None]*np.stack([vx,vy,vz],1)[ok]/vn[ok,None])*mag[ok,None]
        vel=vel+eta*acc
        pos=(pos+vel)%M
        # collisions: pairwise, elastic + transverse axis randomization
        d=pos[:,None,:]-pos[None,:,:]; d=(d+M/2)%M-M/2
        D=np.sqrt((d**2).sum(2)); np.fill_diagonal(D,np.inf)
        pairs=np.argwhere((D<d_coll))
        done=set()
        for a,b in pairs:
            if a>=b or a in done or b in done: continue
            done.add(a); done.add(b); ncoll+=1
            n=d[a,b]/max(np.linalg.norm(d[a,b]),1e-9)
            vrel=vel[a]-vel[b]
            # elastic reflection along the line of centers
            vel[a]=vel[a]-np.dot(vrel,n)*n; vel[b]=vel[b]+np.dot(vrel,n)*n
            # ZBW axis re-randomization: rotate relative velocity to a random
            # direction, magnitude preserved (energy conserving)
            vr=vel[a]-vel[b]; sp=np.linalg.norm(vr)
            u=rng.normal(size=3); u/=np.linalg.norm(u)
            dv=(u*sp-vr)/2.0
            vel[a]=vel[a]+dv; vel[b]=vel[b]-dv
        cens.append(pos.reshape(nDP,2,3).mean(1).copy())
        vels.append(vel.copy())
    cens=np.array(cens); vels=np.array(vels)
    # metrics
    msd=[]
    for lag in (10,25,50,100,200,400):
        if lag<T:
            dd=(cens[lag:]-cens[:-lag]+M/2)%M-M/2
            msd.append((lag,float(np.mean((dd**2).sum(2)))))
    L=np.log([m[0] for m in msd]); Y=np.log([max(m[1],1e-12) for m in msd])
    alpha=float(np.polyfit(L,Y,1)[0])
    v=vels[T//2:]
    vac=[float(np.mean(np.sum(v[:-k]*v[k:],axis=2))/np.mean(np.sum(v*v,axis=2))) for k in (1,2,3,5,10,25,50)]
    sp=np.sqrt((v**2).sum(2))
    spf=sp[-1]
    # Maxwell-Boltzmann check: speed distribution shape (3D MB: CV = sqrt(3pi/8-1)=0.422)
    cv=float(spf.std()/max(spf.mean(),1e-12))
    # energy trend (KE proxy)
    ke=np.array([float((vels[t]**2).sum()/2) for t in range(0,T,max(1,T//20))])
    if report:
        print(f"  eta={eta:<5} nDP={nDP:<4} T={T}: collisions={ncoll}")
        print(f"    MSD alpha={alpha:.2f} (2=ballistic,1=diffusive,0=pinned); msd={[(l,round(m,1)) for l,m in msd]}")
        print(f"    velocity autocorr(1,2,3,5,10,25,50)={np.array2string(np.array(vac),precision=3)}")
        print(f"    final speeds: mean={spf.mean():.3f} std={spf.std():.3f} CV={cv:.3f} (Maxwell 3D = 0.422)")
        print(f"    KE trace (20 pts): {np.array2string(ke,precision=1)}")
    return dict(alpha=alpha,vac=vac,cv=cv,ncoll=ncoll,ke=ke,speeds=spf)

if __name__=="__main__":
    eta=float(sys.argv[1]); nDP=int(sys.argv[2]); T=int(sys.argv[3])
    print(f"VELOCITY-PROXY DIAGNOSTIC (M={M}, PSR R={R}) — proxy for C23 arc inertia")
    run(eta,nDP,T)
