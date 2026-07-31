"""Directed relay: front class + volume-averaged LW discriminant (Patch 2889)"""
import numpy as np, math, itertools

NN=[d for d in itertools.product((-1,0,1),repeat=3) if sorted(map(abs,d))==[0,1,1]]
c_lat=math.sqrt(2)

def deposit(M,pos,q):
    g=np.zeros((M,M,M)); f=[pos[i]-math.floor(pos[i]) for i in range(3)]
    i0=[int(math.floor(pos[i])) for i in range(3)]
    for dx in(0,1):
        for dy in(0,1):
            for dz in(0,1):
                w=(f[0] if dx else 1-f[0])*(f[1] if dy else 1-f[1])*(f[2] if dz else 1-f[2])
                g[(i0[0]+dx)%M,(i0[1]+dy)%M,(i0[2]+dz)%M]+=q*w
    return g

def adv_step(Qd,inj,M):
    Qd_new=np.empty_like(Qd); inj12=inj/12.
    for i,(dx,dy,dz) in enumerate(NN):
        Qd_new[i]=(np.roll(np.roll(np.roll(Qd[i],dx,0),dy,1),dz,2)+
                   np.roll(np.roll(np.roll(inj12,dx,0),dy,1),dz,2))
    return Qd_new

# Test 1: front propagation class
M=96; Qd=np.zeros((12,M,M,M)); inj=np.zeros((M,M,M)); inj[M//2,M//2,M//2]=1.; zero=np.zeros((M,M,M))
ax=np.arange(M); d=np.minimum(np.abs(ax-M//2),M-np.abs(ax-M//2))
D=np.sqrt(d[:,None,None]**2+d[None,:,None]**2+d[None,None,:]**2)
print(f"FRONT TEST (M={M})  analytical: <r>/t={c_lat:.4f}, p=1.000")
print(f"{'t':>3} {'<r>':>8} {'<r>/t':>8}")
rb=[]
for t in range(1,13):
    Qd=adv_step(Qd,inj if t==1 else zero,M)
    Qtot=Qd.sum(0); w=np.abs(Qtot); s=w.sum()
    r=float((w*D).sum()/s) if s>0 else 0.; rb.append(r)
    print(f"{t:3d} {r:8.4f} {r/t:8.4f}")
ta=np.arange(2,13,dtype=float)
p=np.polyfit(np.log(ta),np.log(np.array(rb[1:])),1)[0]
print(f"  fitted p={p:.4f}  [band: BALLISTIC if p in [0.95,1.05]]")

# Test 2: volume-averaged LW discriminant
M=128; NMOV=40
print(f"\nVOL-LW TEST (M={M}, NMOV={NMOV})")
print(f"  A_vol = <Dx_field>/(beta*<r_field>)   LW->0, Retarded->-1")
results=[]
for beta in(0.10,0.20,0.40):
    v=beta*c_lat
    Qd=np.zeros((12,M,M,M)); pos=np.array([40.,M/2.,M/2.])
    for n in range(NMOV):
        inj=deposit(M,pos%M,1.)-1./M**3
        Qd=adv_step(Qd,inj,M)
        pos+=np.array([v,0.,0.])
    src=pos-np.array([v,0.,0.])
    Qtot=np.abs(Qd.sum(0)); total=Qtot.sum()
    # x-displacement weighted average
    xi=np.arange(M,dtype=float); sx=src[0]%M
    dx=xi-sx; dx-=M*np.round(dx/M)
    yi=np.arange(M,dtype=float); sy=src[1]%M
    dy=yi-sy; dy-=M*np.round(dy/M)
    zi=np.arange(M,dtype=float); sz=src[2]%M
    dz=zi-sz; dz-=M*np.round(dz/M)
    mean_dx=float((dx[:,None,None]*Qtot).sum()/total)
    R=np.sqrt(dx[:,None,None]**2+dy[None,:,None]**2+dz[None,None,:]**2)
    mean_r=float((R*Qtot).sum()/total)
    Av=mean_dx/(beta*mean_r)
    results.append((beta,Av))
    print(f"  beta={beta:.2f}: A_vol={Av:8.4f}  <Dx>={mean_dx:7.3f}  <r>={mean_r:7.3f}")
import statistics as st
Avals=[r[1] for r in results]
m=st.mean(Avals); sd=st.pstdev(Avals); spread=abs(sd/m) if m else 1e9
print(f"\n  mean A_vol={m:.4f}  spread/|mean|={spread:.3f}")
print(f"  LW    |A_vol|<0.15 -> {'LW-LIKE' if abs(m)<0.15 else 'not LW'}")
ret_ok=m<-0.50 and spread<0.30
print(f"  RETARDED A_vol<-0.50 and spread<0.30 -> {'RETARDED' if ret_ok else 'not retarded'}")
if ret_ok: verdict="RETARDED"
elif abs(m)<0.15: verdict="LW-LIKE"
else: verdict="INCONCLUSIVE"
print(f"\n  VERDICT: {verdict}")
print(f"\nSUMMARY: front p={p:.4f}, LW={verdict}")
