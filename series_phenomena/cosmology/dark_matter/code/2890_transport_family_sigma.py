"""Thomas's unification: Q_d <- (1-s) advect + s isotropize.  s=0 directed, s=1 convolution."""
import numpy as np, math, itertools
NN=[d for d in itertools.product((-1,0,1),repeat=3) if sorted(map(abs,d))==[0,1,1]]
c_lat=math.sqrt(2)
def step(Qd,inj,s):
    adv=np.empty_like(Qd)
    for i,(dx,dy,dz) in enumerate(NN):
        adv[i]=np.roll(np.roll(np.roll(Qd[i],dx,0),dy,1),dz,2)
    if s>0:
        mean=adv.mean(0)
        adv=(1-s)*adv + s*mean          # scatter fraction s into isotropy
    return adv + inj/12.
M=48; c=M//2
ax=np.arange(M); dd=np.minimum(np.abs(ax-c),M-np.abs(ax-c))
D=np.sqrt(dd[:,None,None]**2+dd[None,:,None]**2+dd[None,None,:]**2)
zero=np.zeros((M,M,M))
imp=np.zeros((M,M,M)); imp[c,c,c]=1.0
print(f"{'sigma':>6} | {'bulk p':>8} {'edge/t':>8} | {'static slope':>13} {'(want -1)':>10}")
print("-"*56)
for s in (0.0,0.25,0.5,0.75,1.0):
    # --- front: bulk exponent and edge speed
    Qd=np.zeros((12,M,M,M)); rb=[]; ed=[]
    for t in range(1,11):
        Qd=step(Qd,imp if t==1 else zero,s)
        w=np.abs(Qd.sum(0)); tot=w.sum()
        rb.append(float((w*D).sum()/tot))
        nz=w>(w.max()*1e-12); ed.append(float(D[nz].max()))
    ta=np.arange(2,11,dtype=float)
    p=np.polyfit(np.log(ta),np.log(np.array(rb[1:])),1)[0]
    edge_sp=ed[3]/4.0
    # --- statics: continuous injection with neutralising background
    Qd=np.zeros((12,M,M,M)); src=np.zeros((M,M,M)); src[c,c,c]=1.0
    inj=src-1.0/M**3
    for t in range(80): Qd=step(Qd,inj,s)
    F=np.abs(Qd.sum(0))
    mask=(D>=3)&(D<=10)
    rr=D[mask]; ff=F[mask]; ok=ff>0
    slope=np.polyfit(np.log(rr[ok]),np.log(ff[ok]),1)[0] if ok.sum()>20 else float('nan')
    print(f"{s:6.2f} | {p:8.4f} {edge_sp:8.4f} | {slope:13.4f}")
print("\nbulk p: 1.0=ballistic, 0.5=diffusive")
print("static slope: potential ~ 1/r gives -1 ; rays give a much flatter/noisier fit")
