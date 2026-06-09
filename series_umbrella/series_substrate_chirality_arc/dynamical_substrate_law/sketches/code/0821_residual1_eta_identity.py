import numpy as np, itertools, collections
rng=np.random.default_rng(31); phi=(1+np.sqrt(5))/2
def even_perms(t):
    P=[p for p in itertools.permutations(range(4))
       if sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])%2==0]
    return set(tuple(t[p[i]] for i in range(4)) for p in P)
V=set()
for i in range(4):
    for s in (1,-1): v=[0,0,0,0]; v[i]=s; V.add(tuple(v))
for s in itertools.product([0.5,-0.5],repeat=4): V.add(s)
for sg in itertools.product([1,-1],repeat=3):
    for w in even_perms([0,sg[0]*0.5,sg[1]*1/(2*phi),sg[2]*phi/2]): V.add(w)
V=np.array(sorted(V)); N=len(V)
Dm=np.sqrt(((V[:,None]-V[None])**2).sum(-1)); ed=np.min(Dm[Dm>1e-6]); A=(np.abs(Dm-ed)<1e-6)
nbr=[np.where(A[v])[0] for v in range(N)]; Kc=1/12.0
# graph distance
dist=np.full((N,N),-1)
for s in range(N):
    dist[s,s]=0; q=collections.deque([s])
    while q:
        u=q.popleft()
        for w in np.where(A[u])[0]:
            if dist[s,w]<0: dist[s,w]=dist[s,u]+1; q.append(w)
nhat=np.array([1.0,phi,phi**2,phi**3]); nhat/=np.linalg.norm(nhat)
# edge list + per-vertex incident edges
E={}; 
for v in range(N):
    for w in nbr[v]:
        E[tuple(sorted((v,int(w))))]=True
edges=list(E.keys()); eidx={e:i for i,e in enumerate(edges)}; nE=len(edges)
inc=[[eidx[tuple(sorted((v,int(w))))] for w in nbr[v]] for v in range(N)]
bias=np.array([ (lambda d: d/np.linalg.norm(d))(V[max(e)]-V[min(e)])@nhat for e in edges])

def orient_weights(frame):
    r1,r2=frame
    W=[]
    for v in range(N):
        ws=[]
        for w in nbr[v]:
            d=V[w]-V[v]; d/=np.linalg.norm(d)
            ws.append(np.sign(np.linalg.det(np.array([d,nhat,r1,r2]))))
        W.append(np.array(ws))
    return W

def corr_vs_dist(W, m_read, delta, MC=8000):
    # eta_v = sign( sum over m_read incident edges of w_e * x_e )
    readidx=[]; readw=[]
    for v in range(N):
        order=sorted(range(len(nbr[v])), key=lambda k:-abs((V[nbr[v][k]]-V[v])@nhat))[:m_read]
        readidx.append([inc[v][k] for k in order]); readw.append(W[v][order])
    em=np.zeros(N); acc=np.zeros((N,N))
    for _ in range(MC):
        x=delta*bias+rng.normal(size=nE)
        eta=np.array([np.sign(readw[v]@x[readidx[v]]) for v in range(N)])
        em+=eta; acc+=np.outer(eta,eta)
    em/=MC; acc/=MC; C=acc-np.outer(em,em)
    cd={d: C[dist==d].mean() for d in range(0,4)}
    return cd, np.arctanh(np.clip(abs(cd[1]),0,0.999))

f0=(np.array([1.,-1,0,0])/np.sqrt(2), np.array([0,0,1.,-1])/np.sqrt(2))
print(f"K_c (mean-field) = {Kc:.4f}\n")
print("RESIDUAL 1a -- canonical vertex-figure eta (m=12), correlator vs graph distance (real measure, delta=0.08):")
cd,K=corr_vs_dist(orient_weights(f0),12,0.08)
for d in range(4): print(f"   d={d}: <eta eta>_c = {cd[d]:+.4f}")
print(f"   => K_lift=|arctanh(C_nn)|={K:.4f}, K_lift/K_c={K/Kc:.2f}; decay d2/d1={abs(cd[2]/cd[1]):.2f} (short-range if <<1)\n")

print("RESIDUAL 1b -- scan candidate local eta-modes (support m + orientation frame); is ANY super-critical?")
f1=(np.array([1.,1,-1,-1])/2, np.array([1.,-1,1,-1])/2)
f2=(np.array([1.,0,-1,0])/np.sqrt(2), np.array([0,1.,0,-1])/np.sqrt(2))
print(f"{'frame':>7}{'m':>4}{'C_nn':>9}{'K_lift':>9}{'/K_c':>7}  status")
maxK=0
for nm,fr in [('f0',f0),('f1',f1),('f2',f2)]:
    W=orient_weights(fr)
    for m in [4,6,8,12]:
        cd,K=corr_vs_dist(W,m,0.08,MC=6000); maxK=max(maxK,K)
        print(f"{nm:>7}{m:4d}{cd[1]:+9.4f}{K:9.4f}{K/Kc:7.2f}  {'SUPER-CRIT' if K>Kc else 'sub-crit'}")
print(f"\n   MAX K_lift over scanned modes = {maxK:.4f}  vs K_c = {Kc:.4f}  =>  {'A MODE ORDERS' if maxK>Kc else 'NO candidate mode orders'}")
