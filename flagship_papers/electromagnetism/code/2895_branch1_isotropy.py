"""Is the Branch-1 field ISOTROPIC at fixed radius, or confined to rays?
   Angular binning in genuine solid-angle patches (HEALPix-like via lat/lon equal-area)."""
import numpy as np, math, itertools
rng=np.random.default_rng(11)
NN=np.array([d for d in itertools.product((-1,0,1),repeat=3)
             if sorted(map(abs,d))==[0,1,1]],dtype=float)
NN/=np.linalg.norm(NN,axis=1,keepdims=True)

def bits(mode,T=50,per=40000):
    P=[];dirs=[]
    for t in range(T):
        if mode=="continuum":
            v=rng.normal(size=(per,3)); d=v/np.linalg.norm(v,axis=1,keepdims=True)
        elif mode=="fcc12":
            d=NN[rng.integers(0,12,size=per)]
        elif mode=="lattice_paths":
            # bit walks toward a RANDOM shell GP: random target direction, then
            # each hop takes the FCC edge best aligned with that target
            v=rng.normal(size=(per,3)); tgt=v/np.linalg.norm(v,axis=1,keepdims=True)
            d=tgt          # net displacement direction after many aligned hops
        dirs.append(d); P.append(np.zeros((per,3)))
        for i in range(len(P)): P[i]=P[i]+dirs[i]
    return np.vstack(P)

def aniso(X,r0,dr=3.0,nlat=8,nlon=16):
    r=np.linalg.norm(X,axis=1); m=(r>r0-dr)&(r<r0+dr)
    Y=X[m]; rr=r[m]
    if len(Y)<500: return float('nan')
    ct=Y[:,2]/rr                      # cos(theta), equal-area in cos(theta)
    ph=np.arctan2(Y[:,1],Y[:,0])
    i=np.clip(((ct+1)/2*nlat).astype(int),0,nlat-1)
    j=np.clip(((ph+math.pi)/(2*math.pi)*nlon).astype(int),0,nlon-1)
    cnt=np.zeros(nlat*nlon); np.add.at(cnt,i*nlon+j,1.0)
    return float(np.std(cnt)/np.mean(cnt))

print("Angular anisotropy (CV across equal-area solid-angle patches)")
print("  ~0.05 = isotropic (Poisson noise only) | >1 = ray-structured")
print(f"{'mode':>16} {'r=15':>9} {'r=25':>9} {'r=35':>9}")
print("-"*46)
for mode,label in (("continuum","continuum"),("lattice_paths","lattice paths"),
                   ("fcc12","12 FCC rays")):
    X=bits(mode)
    print(f"{label:>16} {aniso(X,15):9.4f} {aniso(X,25):9.4f} {aniso(X,35):9.4f}")
