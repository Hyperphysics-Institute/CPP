#!/usr/bin/env python3
"""P-X4/P-X5 scale scan (Patch 2809): PSR/spacing separation vs
liveness, clustering, fidelity, and turnover. Usage: R fill_denom moments"""
import sys, pickle, numpy as np, collections
src=open('code/2802_automaton2_engine.py').read().split('if sys.argv[1]')[0]
ns={}; exec(src,ns)
kernels=ns['kernels']; moment=ns['moment']; cp_step=ns['cp_step']; inj_field=ns['inj_field']; fcc_sites=ns['fcc_sites']
M=24
R=int(sys.argv[1]); den=int(sys.argv[2]); T=int(sys.argv[3])
kern=kernels(M,R)
rng=np.random.default_rng(2809+R*10+den)
sites=fcc_sites(M); N=(len(sites)//den)//2*2  # fill = N/len(sites) = 1/den (corrected; earlier runs mislabeled)
pos=sites[rng.choice(len(sites),N,replace=False)].copy()
sig=np.array([1]*(N//2)+[-1]*(N//2)); rng.shuffle(sig)
Q=np.zeros((M,M,M)); mov=[]; snaps=[]
for t in range(T):
    inj=inj_field(pos,sig,M)
    Q,Vx,Vy,Vz,Aab=moment(Q,inj,kern)
    new=cp_step(pos,sig,Vx,Vy,Vz,Aab,R,M)
    mov.append(float((new!=pos).any(axis=1).mean())); pos=new
    if t>=T//2 and t%(max(1,T//20))==0: snaps.append(pos.copy())
snaps=np.array(snaps)
def clusters(p):
    n=len(p); dd=p[:,None,:]-p[None,:,:]; dd=(dd+M//2)%M-M//2
    D=np.sqrt((dd**2).sum(2)); adj=(D<=1.5)&(D>1e-9)
    lab=-np.ones(n,int); nl=0
    for a in range(n):
        if lab[a]>=0: continue
        st=[a]; lab[a]=nl
        while st:
            x=st.pop()
            for b in np.where(adj[x]&(lab<0))[0]: lab[b]=nl; st.append(b)
        nl+=1
    return lab
# PSR occupancy: mean CPs within R of a CP
p0=snaps[0]; dd=p0[:,None,:]-p0[None,:,:]; dd=(dd+M//2)%M-M//2
D0=np.sqrt((dd**2).sum(2))
occ=float(((D0<=R)&(D0>1e-9)).sum(1).mean())
# fidelity: nearest-unlike partner identity across snapshots
plus=np.where(sig>0)[0]; minus=np.where(sig<0)[0]
def part(p):
    dd=p[plus][:,None,:]-p[minus][None,:,:]; dd=(dd+M//2)%M-M//2
    return np.argmin(np.sqrt((dd**2).sum(2)),axis=1)
pa=part(snaps[0]); pb=part(snaps[-1])
fid=float(np.mean(pa==pb))
# turnover: per-CP cluster-membership change rate between snapshots
labs=[clusters(s) for s in snaps]
szs=[collections.Counter(l.tolist()) for l in labs]
mx=[max(s.values()) for s in szs]
# events: change in the multiset of cluster sizes between consecutive snaps
ev=sum(1 for a in range(len(labs)-1)
       if sorted(collections.Counter(labs[a].tolist()).values())!=sorted(collections.Counter(labs[a+1].tolist()).values()))
small=np.mean([sum(k*v for k,v in collections.Counter(s.values()).items() if k<=2)/len(sig) for s in szs])
print(f"R={R} fill=1/{den} N={N}: PSR occupancy={occ:.1f} CPs; mover={np.mean(mov[-T//4:]):.3f}; "
      f"max cluster mean={np.mean(mx):.1f} (range {min(mx)}-{max(mx)}); pairs<=2 frac={small:.2f}; "
      f"fidelity={fid*100:.0f}%; cluster-spectrum change events={ev}/{len(labs)-1}")
