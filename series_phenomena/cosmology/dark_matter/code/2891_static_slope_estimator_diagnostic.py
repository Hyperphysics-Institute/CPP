import numpy as np, math, itertools
NN=[d for d in itertools.product((-1,0,1),repeat=3) if sorted(map(abs,d))==[0,1,1]]
def step(Qd,inj,s):
    adv=np.empty_like(Qd)
    for i,(dx,dy,dz) in enumerate(NN):
        adv[i]=np.roll(np.roll(np.roll(Qd[i],dx,0),dy,1),dz,2)
    if s>0:
        m=adv.mean(0); adv=(1-s)*adv+s*m
    return adv+inj/12.
M=48; c=M//2
ax=np.arange(M); dd=np.minimum(np.abs(ax-c),M-np.abs(ax-c))
D=np.sqrt(dd[:,None,None]**2+dd[None,:,None]**2+dd[None,None,:]**2)
src=np.zeros((M,M,M)); src[c,c,c]=1.0
s=1.0
for label,inj,nT in (("WITH background", src-1.0/M**3, 80),
                     ("WITH background", src-1.0/M**3, 90),
                     ("NO background",   src.copy(),   80)):
    Qd=np.zeros((12,M,M,M))
    for t in range(nT): Qd=step(Qd,inj,s)
    F=np.abs(Qd.sum(0))
    print(f"\n{label}, T={nT}")
    # shell-averaged profile
    prof=[]
    for rt in (3,4,5,6,7,8,10):
        sh=np.abs(D-rt)<0.5
        prof.append((rt,float(F[sh].mean())))
    for r,v in prof: print(f"   r={r:2d}  <F>={v:.6e}")
    for lo,hi in ((3,6),(3,10)):
        m=(D>=lo)&(D<=hi); rr=D[m]; ff=F[m]; ok=ff>0
        sl=np.polyfit(np.log(rr[ok]),np.log(ff[ok]),1)[0]
        # shell-mean fit (correct way: avoid per-voxel scatter)
        pr=[(r,v) for r,v in prof if lo<=r<=hi]
        sl2=np.polyfit(np.log([p[0] for p in pr]),np.log([p[1] for p in pr]),1)[0]
        print(f"   fit[{lo},{hi}]  per-voxel={sl:8.4f}   shell-mean={sl2:8.4f}")
