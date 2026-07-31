"""Greedy vs PROBABILISTIC re-radiation over the 12 neighbours.
   Founder: 'absorptions and re-radiations to the 12 nearest neighbors' --
   a DISTRIBUTION over neighbours, biased toward the address."""
import numpy as np, math, itertools
rng=np.random.default_rng(31)
NN=np.array([d for d in itertools.product((-1,0,1),repeat=3)
             if sorted(map(abs,d))==[0,1,1]],dtype=float)

def route(nbits,R,mode,beta=3.0):
    v=rng.normal(size=(nbits,3)); tgt=v/np.linalg.norm(v,axis=1,keepdims=True)*R
    pos=np.zeros((nbits,3)); transit=[]; live=np.ones(nbits,bool); hops=np.zeros(nbits,int)
    for step in range(int(4*R)+30):
        if not live.any(): break
        transit.append(pos[live].copy())
        idx=np.where(live)[0]
        rem=tgt[idx]-pos[idx]
        rn=rem/np.maximum(np.linalg.norm(rem,axis=1,keepdims=True),1e-12)
        proj=rn@ (NN/np.linalg.norm(NN,axis=1,keepdims=True)).T     # cos angle, (n,12)
        if mode=="greedy":
            pick=np.argmax(proj,axis=1)
        else:                                    # softmax over the 12, bias beta
            w=np.exp(beta*proj); w/=w.sum(axis=1,keepdims=True)
            cw=np.cumsum(w,axis=1); u=rng.random((len(idx),1))
            pick=(u>cw).sum(axis=1)
        pos[idx]=pos[idx]+NN[pick]; hops[idx]+=1
        d_new=np.linalg.norm(tgt[idx]-pos[idx],axis=1)
        live[idx[d_new<math.sqrt(2)]]=False
    return np.vstack(transit), pos, hops

def aniso(X,r0,dr=2.5,nlat=8,nlon=16):
    r=np.linalg.norm(X,axis=1); m=(r>r0-dr)&(r<r0+dr)
    Y=X[m]; rr=r[m]
    if len(Y)<800: return float('nan')
    ct=Y[:,2]/rr; ph=np.arctan2(Y[:,1],Y[:,0])
    i=np.clip(((ct+1)/2*nlat).astype(int),0,nlat-1)
    j=np.clip(((ph+math.pi)/(2*math.pi)*nlon).astype(int),0,nlon-1)
    cnt=np.zeros(nlat*nlon); np.add.at(cnt,i*nlon+j,1.0)
    return float(np.std(cnt)/np.mean(cnt))

R=30
print(f"IN-TRANSIT ANISOTROPY vs radius   (noise floor ~0.03)")
print(f"{'mode':>22} {'r=4':>8} {'r=8':>8} {'r=14':>8} {'r=20':>8} {'hops':>7}")
print("-"*68)
for mode,beta,lab in (("greedy",0,"greedy (deterministic)"),
                      ("soft",6.0,"softmax beta=6"),
                      ("soft",3.0,"softmax beta=3"),
                      ("soft",1.5,"softmax beta=1.5")):
    T,arr,h=route(50000,R,mode,beta)
    print(f"{lab:>22} {aniso(T,4,dr=2):8.4f} {aniso(T,8):8.4f} "
          f"{aniso(T,14):8.4f} {aniso(T,20):8.4f} {h.mean():7.1f}")
print(f"\nideal hop count R/sqrt2 = {R/math.sqrt(2):.1f}")
