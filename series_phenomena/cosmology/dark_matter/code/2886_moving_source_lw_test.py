import importlib.util, math, numpy as np
spec=importlib.util.spec_from_file_location("a2","/tmp/a2_funcs.py")
a2=importlib.util.module_from_spec(spec); spec.loader.exec_module(a2)

M,R = 48,4
kern = a2.kernels(M,R)
W    = a2.front_kernel(R)
# measure the relay's propagation speed empirically from the kernel itself
c_lat = sum(w*math.sqrt(d[0]**2+d[1]**2+d[2]**2) for d,w in W.items())/sum(W.values())
print(f"kernel front: {len(W)} sites, mean euclidean radius = c_lat = {c_lat:.4f} units/Moment")

def deposit(M, pos, q):
    """trilinear deposition of charge q at fractional position pos"""
    g=np.zeros((M,M,M)); x,y,z=pos
    x0,y0,z0=int(math.floor(x)),int(math.floor(y)),int(math.floor(z))
    fx,fy,fz=x-x0,y-y0,z-z0
    for dx in (0,1):
        for dy in (0,1):
            for dz in (0,1):
                w=(fx if dx else 1-fx)*(fy if dy else 1-fy)*(fz if dz else 1-fz)
                g[(x0+dx)%M,(y0+dy)%M,(z0+dz)%M]+=q*w
    return g

def run(beta, n_eq=40, n_mov=40):
    v = beta*c_lat
    Q=np.zeros((M,M,M)); Vx=Vy=Vz=None
    pos=np.array([M/2.,M/2.,M/2.])
    for n in range(n_eq+n_mov):
        if n>=n_eq: pos=pos+np.array([v,0,0])
        inj = deposit(M,pos%M,1.0) - (1.0/M**3)
        Q,Vx,Vy,Vz,Aab = a2.moment(Q,inj,kern)
    return pos%M, Vx,Vy,Vz

def aim(beta):
    src,Vx,Vy,Vz = run(beta)
    out=[]
    for r in (4.,6.,8.):
        off=r/math.sqrt(2.)
        vals=[]
        for sgn in (+1,-1):          # +perp and -perp, averaged
            for ax in (+1,-1):       # fore and aft placements
                p=np.array([src[0]+ax*off, src[1]+sgn*off, src[2]])
                i,j,k=[int(round(c))%M for c in p]
                ux,uy = Vx[i,j,k], Vy[i,j,k]
                uperp = uy*sgn
                if abs(uperp)<1e-14: continue
                x_aim = p[0] - (sgn*off)*(ux/uy) if abs(uy)>1e-14 else np.nan
                vals.append((x_aim-src[0])/(beta*r))
        out.append((r, float(np.mean(vals)) if vals else float('nan')))
    return out

print(f"\n{'beta':>6} | {'r=4':>10} {'r=6':>10} {'r=8':>10}   (A discriminant)")
print("-"*54)
res={}
for beta in (0.10,0.20,0.40):
    a=aim(beta); res[beta]=a
    print(f"{beta:6.2f} | " + " ".join(f"{v:10.4f}" for _,v in a))
allA=[v for b in res for _,v in res[b]]
m=np.nanmean(allA); sd=np.nanstd(allA)
print(f"\nmean A = {m:.4f}   spread/mean = {abs(sd/m) if m else float('nan'):.3f}")
print("LW band  |A|<0.15 ->", "LW-LIKE" if abs(m)<0.15 else "not LW")
print("RET band  A<-0.50 ->", "RETARDED" if m<-0.50 else "not retarded")
