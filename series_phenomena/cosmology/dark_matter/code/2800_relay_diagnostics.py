#!/usr/bin/env python3
"""Patch 2800 appendix: the two relay diagnostics cited in C22.
(1) Undirected all-12 relay diffuses (no front): mass lags interior,
    outer-shell fraction collapses with R.
(2) Origin-address-DIRECTED outward relay: 100% of mass at exactly
    graph-distance R (sharp causal front on the icosahedral shell)."""
import numpy as np, itertools
def undirected(M=33,Rs=(2,3,4,6)):
    c=M//2
    nn=[d for d in itertools.product((-1,0,1),repeat=3) if sorted(map(abs,d))==[0,1,1]]
    K=np.zeros((M,M,M))
    for d in nn: K[(c+d[0])%M,(c+d[1])%M,(c+d[2])%M]=1/12
    Kf=np.fft.rfftn(np.fft.ifftshift(K))
    ax=np.arange(M)-c
    D=np.sqrt(ax[:,None,None]**2+ax[None,:,None]**2+ax[None,None,:]**2)
    for R in Rs:
        g=np.zeros((M,M,M)); g[c,c,c]=1.0
        for _ in range(R):
            g=np.fft.irfftn(np.fft.rfftn(g)*Kf,s=(M,M,M),axes=(0,1,2))
        print(f"undirected R={R}: mass at r>=R-1: {g[(D>=R-1)].sum():.2f}")
def directed(M=41,Rs=(3,4,6)):
    c=M//2
    nn=[d for d in itertools.product((-1,0,1),repeat=3) if sorted(map(abs,d))==[0,1,1]]
    ax=np.arange(M)-c
    D=np.sqrt(ax[:,None,None]**2+ax[None,:,None]**2+ax[None,None,:]**2)
    for R in Rs:
        g=np.zeros((M,M,M)); g[c,c,c]=1.0
        for hop in range(R):
            gn=np.zeros((M,M,M))
            for (i,j,k) in np.argwhere(g>0):
                w=g[i,j,k]; d0=D[i,j,k]
                outs=[(i+a,j+b,k+e) for (a,b,e) in nn if 0<=i+a<M and 0<=j+b<M and 0<=k+e<M and D[i+a,j+b,k+e]>d0+1e-9]
                for (x,y,z) in outs: gn[x,y,z]+=w/len(outs)
            g=gn
        m=g>0
        print(f"directed  R={R}: all mass at graph-distance R: {abs(g[m].sum()-1)<1e-9}; front GPs={int(m.sum())}; weight CV={g[m].std()/g[m].mean():.2f}")
if __name__=="__main__":
    undirected(); directed()
