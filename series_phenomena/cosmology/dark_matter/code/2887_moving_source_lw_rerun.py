import importlib.util, math, numpy as np
spec=importlib.util.spec_from_file_location("a2","/tmp/a2_funcs.py")
a2=importlib.util.module_from_spec(spec); spec.loader.exec_module(a2)

M,R,NMOV = 128,4,40
kern=a2.kernels(M,R); W=a2.front_kernel(R)
c_lat=sum(w*math.sqrt(d[0]**2+d[1]**2+d[2]**2) for d,w in W.items())/sum(W.values())
print(f"M={M} R={R}  c_lat={c_lat:.4f} units/Moment  front={len(W)} sites")

def deposit(M,pos,q):
    g=np.zeros((M,M,M)); x,y,z=pos
    x0,y0,z0=int(math.floor(x)),int(math.floor(y)),int(math.floor(z))
    fx,fy,fz=x-x0,y-y0,z-z0
    for dx in(0,1):
        for dy in(0,1):
            for dz in(0,1):
                w=(fx if dx else 1-fx)*(fy if dy else 1-fy)*(fz if dz else 1-fz)
                g[(x0+dx)%M,(y0+dy)%M,(z0+dz)%M]+=q*w
    return g

def interp(F,p,M):
    """trilinear read -- matches the deposition, removes rounding error"""
    x,y,z=p; x0,y0,z0=int(math.floor(x)),int(math.floor(y)),int(math.floor(z))
    fx,fy,fz=x-x0,y-y0,z-z0; s=0.0
    for dx in(0,1):
        for dy in(0,1):
            for dz in(0,1):
                w=(fx if dx else 1-fx)*(fy if dy else 1-fy)*(fz if dz else 1-fz)
                s+=w*F[(x0+dx)%M,(y0+dy)%M,(z0+dz)%M]
    return s

def run(beta):
    """source moves from Moment 0 -- field built entirely by uniform motion"""
    v=beta*c_lat; Q=np.zeros((M,M,M))
    start=np.array([30.,M/2.,M/2.])
    pos=start.copy()
    for n in range(NMOV):
        inj=deposit(M,pos%M,1.0)-(1.0/M**3)
        Q,Vx,Vy,Vz,Aab=a2.moment(Q,inj,kern)
        pos=pos+np.array([v,0,0])
    travel=pos[0]-start[0]
    return pos-np.array([v,0,0]), Vx,Vy,Vz, travel

print(f"\n{'beta':>6} {'travel':>8} | {'r':>3} {'A(fore)':>10} {'A(aft)':>10}")
print("-"*48)
rows=[]
for beta in (0.10,0.20,0.40):
    src,Vx,Vy,Vz,travel=run(beta)
    for r in (4.,6.,8.):
        off=r/math.sqrt(2.)
        got={}
        for ax in (+1,-1):
            vals=[]
            for sgn in (+1,-1):
                P=np.array([src[0]+ax*off, src[1]+sgn*off, src[2]])
                ux=interp(Vx,P%M,M); uy=interp(Vy,P%M,M)
                if abs(uy)<1e-13: continue
                x_aim=P[0]-(sgn*off)*(ux/uy)
                vals.append((x_aim-src[0])/(beta*r))
            got[ax]=float(np.mean(vals)) if vals else float('nan')
        rows.append((beta,r,got[+1],got[-1]))
        print(f"{beta:6.2f} {travel:8.1f} | {r:3.0f} {got[+1]:10.4f} {got[-1]:10.4f}")

import statistics as st
for name,idx in (("fore",2),("aft",3)):
    A=[x[idx] for x in rows]
    m=st.mean(A); sd=st.pstdev(A)
    print(f"\n{name.upper():5} mean A={m:8.4f}  spread/|mean|={abs(sd/m):.3f}"
          f"   linearity(<0.30): {'PASS' if abs(sd/m)<0.30 else 'FAIL'}")
    print(f"      LW |A|<0.15 -> {'LW-LIKE' if abs(m)<0.15 else 'not LW'}"
          f" | RET A<-0.50 -> {'RETARDED' if m<-0.50 else 'not retarded'}")
    perb={}
    for b in (0.10,0.20,0.40):
        q=[x[idx] for x in rows if x[0]==b]
        perb[b]=sum(1 for v in q if v<-0.50)
    print(f"      per-beta count of radii with A<-0.50 (need >=2 of 3): {perb}")
