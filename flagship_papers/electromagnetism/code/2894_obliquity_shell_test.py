"""Kirchhoff obliquity (DI-bit/scalar conserving) vs 2892 vector-conserving rule.
   Does N sub-Moment hops build a SHELL at r~N*sqrt2, or a filled diffusive ball?"""
import numpy as np, math, itertools
NN=[np.array(d,float) for d in itertools.product((-1,0,1),repeat=3)
    if sorted(map(abs,d))==[0,1,1]]
DH=[d/np.linalg.norm(d) for d in NN]
def roll_to(A,d): return np.roll(np.roll(np.roll(A,int(d[0]),0),int(d[1]),1),int(d[2]),2)
def mk(k):
    def st(Qd,inj):
        S=Qd.sum(0)+inj
        Vx=sum(Qd[i]*DH[i][0] for i in range(12))
        Vy=sum(Qd[i]*DH[i][1] for i in range(12))
        Vz=sum(Qd[i]*DH[i][2] for i in range(12))
        out=np.empty_like(Qd)
        for i in range(12):
            out[i]=roll_to(S/12.+k*(Vx*DH[i][0]+Vy*DH[i][1]+Vz*DH[i][2]),NN[i])
        return out
    return st
M=64;c=M//2
ax=np.arange(M);dd=np.minimum(np.abs(ax-c),M-np.abs(ax-c))
D=np.sqrt(dd[:,None,None]**2+dd[None,:,None]**2+dd[None,None,:]**2)
imp=np.zeros((M,M,M));imp[c,c,c]=1.0;zero=np.zeros((M,M,M))
print(f"{'rule':>26} {'bulk p':>8} {'shell frac':>11} {'bits kept':>10}")
print("-"*60)
for name,k in (("KIRCHHOFF  (1+cos)/12",1/12.),("2892 vector (1+3cos)/12",1/4.),
               ("isotropic  (no dipole)",0.0)):
    Qd=np.zeros((12,M,M,M)); rb=[]
    for t in range(1,13):
        Qd=mk(k)(Qd,imp if t==1 else zero)
        w=np.abs(Qd.sum(0)); s=w.sum(); rb.append(float((w*D).sum()/s))
    ta=np.arange(2,13,dtype=float)
    p=np.polyfit(np.log(ta-1),np.log(np.array(rb[1:])),1)[0]
    # shell fraction: |Q| in outer 25% of the light cone r<=t*sqrt2
    T=12; Rc=T*math.sqrt(2); w=np.abs(Qd.sum(0))
    frac=float(w[(D>=0.75*Rc)&(D<=Rc)].sum()/w.sum())
    bits=float(Qd.sum())        # signed total = DI-bit count
    print(f"{name:>26} {p:8.4f} {frac:11.4f} {bits:10.5f}")
print("\nshell frac -> 1 : energy on the expanding shell (ballistic wave)")
print("shell frac -> 0 : filled ball (diffusive)")
print("bits kept  = signed sum; 1.0 means DI-bit count conserved")
