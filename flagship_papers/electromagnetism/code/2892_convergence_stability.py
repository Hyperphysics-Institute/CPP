import numpy as np, math, itertools
NN=[np.array(d,dtype=float) for d in itertools.product((-1,0,1),repeat=3)
    if sorted(map(abs,d))==[0,1,1]]
DH=[d/np.linalg.norm(d) for d in NN]
def roll_to(A,d): return np.roll(np.roll(np.roll(A,int(d[0]),0),int(d[1]),1),int(d[2]),2)
def step_coh(Qd,inj):
    S=Qd.sum(0)+inj
    Vx=sum(Qd[i]*DH[i][0] for i in range(12)); Vy=sum(Qd[i]*DH[i][1] for i in range(12))
    Vz=sum(Qd[i]*DH[i][2] for i in range(12))
    out=np.empty_like(Qd)
    for i in range(12):
        out[i]=roll_to(S/12.+(Vx*DH[i][0]+Vy*DH[i][1]+Vz*DH[i][2])/4.,NN[i])
    return out
def step_inc(Qd,inj):
    S=Qd.sum(0)+inj; out=np.empty_like(Qd)
    for i in range(12): out[i]=roll_to(S/12.,NN[i])
    return out
M=24;c=M//2
ax=np.arange(M);dd=np.minimum(np.abs(ax-c),M-np.abs(ax-c))
D=np.sqrt(dd[:,None,None]**2+dd[None,:,None]**2+dd[None,None,:]**2)
src=np.zeros((M,M,M));src[c,c,c]=1.0;inj=src-1.0/M**3
print(f"CONVERGENCE + STABILITY, M={M} (relax ~ (M/2)^2/D ~ 144)")
print(f"{'rule':>11} {'T':>5} {'slope[2,6]':>11} {'max|F|':>12} {'d(slope)':>10}")
for name,fn in (("coherent",step_coh),("incoherent",step_inc)):
    Qd=np.zeros((12,M,M,M)); prev=None
    for T in (100,200,400,800,1600):
        while True:
            Qd=fn(Qd,inj)
            step_coh.count=getattr(step_coh,'count',0)
            break
        # run up to T total
        pass
    # redo cleanly
    Qd=np.zeros((12,M,M,M)); t=0; prev=None
    for T in (100,200,400,800,1600):
        while t<T:
            Qd=fn(Qd,inj); t+=1
        F=np.abs(Qd.sum(0))
        pr=[(r,float(F[np.abs(D-r)<0.5].mean())) for r in (2,3,4,5,6)]
        sl=np.polyfit(np.log([p[0] for p in pr]),np.log([p[1] for p in pr]),1)[0]
        dd_=f"{abs(sl-prev):10.4f}" if prev is not None else "         -"
        print(f"{name:>11} {T:5d} {sl:11.4f} {F.max():12.4e} {dd_}")
        prev=sl
