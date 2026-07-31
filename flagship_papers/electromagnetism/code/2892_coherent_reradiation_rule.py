"""Founder rule: re-radiation at every CP every Moment, SIGNED, conserving SSV_net.
   w_d = S/12 + (V.dhat)/4   -- derived from  sum(dhat)=0, sum(dhat_i dhat_j)=4 delta_ij
   Compare against the incoherent (amplitude-only) rule that gave diffusion."""
import numpy as np, math, itertools
NN=[np.array(d,dtype=float) for d in itertools.product((-1,0,1),repeat=3)
    if sorted(map(abs,d))==[0,1,1]]
DH=[d/np.linalg.norm(d) for d in NN]
c_lat=math.sqrt(2)

def roll_to(A,d):
    return np.roll(np.roll(np.roll(A,int(d[0]),0),int(d[1]),1),int(d[2]),2)

def step_coherent(Qd,inj):
    S=Qd.sum(0)+inj                      # total at each site (signed)
    V=sum(Qd[i]*DH[i][k] for i in range(12) for k in (0,) )*0  # placeholder
    Vx=sum(Qd[i]*DH[i][0] for i in range(12))
    Vy=sum(Qd[i]*DH[i][1] for i in range(12))
    Vz=sum(Qd[i]*DH[i][2] for i in range(12))
    out=np.empty_like(Qd)
    for i in range(12):
        w=S/12.0 + (Vx*DH[i][0]+Vy*DH[i][1]+Vz*DH[i][2])/4.0
        out[i]=roll_to(w,NN[i])
    return out

def step_incoherent(Qd,inj):             # the sigma=1 rule that diffused
    S=Qd.sum(0)+inj
    out=np.empty_like(Qd)
    for i in range(12):
        out[i]=roll_to(S/12.0,NN[i])
    return out

M=48; c=M//2
ax=np.arange(M); dd=np.minimum(np.abs(ax-c),M-np.abs(ax-c))
D=np.sqrt(dd[:,None,None]**2+dd[None,:,None]**2+dd[None,None,:]**2)
imp=np.zeros((M,M,M)); imp[c,c,c]=1.0; zero=np.zeros((M,M,M))

for name,fn in (("COHERENT (SSV_net conserved)",step_coherent),
                ("INCOHERENT (amplitude only)",step_incoherent)):
    Qd=np.zeros((12,M,M,M)); rb=[]; ed=[]
    for t in range(1,11):
        Qd=fn(Qd,imp if t==1 else zero)
        w=np.abs(Qd.sum(0)); s=w.sum()
        rb.append(float((w*D).sum()/s))
        nz=w>(w.max()*1e-12); ed.append(float(D[nz].max()))
    ta=np.arange(2,11,dtype=float)
    p=np.polyfit(np.log(ta-1),np.log(np.array(rb[1:])),1)[0]   # (t-1) offset corrected
    print(f"{name}")
    print(f"   bulk p = {p:.4f}   [1.0 ballistic / 0.5 diffusive]")
    print(f"   edge/t = {ed[3]/4:.4f}  (t=4)   <r> at t=10: {rb[-1]:.3f}")
