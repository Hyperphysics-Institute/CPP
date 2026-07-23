#!/usr/bin/env python3
"""Sanity check 1 (handover 2783 S4): do chord and geodesic metrics induce
the SAME vertex-shell partition on I1 (600-cell, 120 vertices, source=v0)?
Construction copied verbatim from frozen code/2694_r1_l2r_execution.py."""
import itertools, math, numpy as np
PHI=(1+math.sqrt(5))/2; L_UNIT=0.589; A=L_UNIT/PHI
verts=[]
for s in itertools.product([0.5,-0.5],repeat=4): verts.append(s)
for i in range(4):
    for s in (1.0,-1.0):
        v=[0.0]*4; v[i]=s; verts.append(tuple(v))
ep=[(0,1,2,3),(0,2,3,1),(0,3,1,2),(1,0,3,2),(1,2,0,3),(1,3,2,0),(2,0,1,3),(2,1,3,0),(2,3,0,1),(3,0,2,1),(3,1,0,2),(3,2,1,0)]
base=(PHI/2,0.5,1/(2*PHI),0.0); seen=set()
for perm in ep:
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                v=[0.0]*4; vals=(s1*base[0],s2*base[1],s3*base[2],0.0)
                for k in range(4): v[perm[k]]=vals[k]
                t=tuple(round(x,9) for x in v)
                if t not in seen: seen.add(t); verts.append(t)
V=np.array(verts); assert len(V)==120
D4=np.linalg.norm(V[:,None,:]-V[None,:,:],axis=2)*L_UNIT
dmin=D4[D4>1e-9].min()
Dg=np.where(np.abs(D4-dmin)<1e-6,1.0,1e9); np.fill_diagonal(Dg,0.0)
for k in range(120): Dg=np.minimum(Dg,Dg[:,k][:,None]+Dg[k,:][None,:])
Dg*=A
# shells from source vertex 0, both metrics
rc=np.round(D4[0],6); rg=np.round(Dg[0],6)
shc=sorted(set(rc[1:])); shg=sorted(set(rg[1:]))
print(f"chord shells   ({len(shc)}): {shc}")
print(f"geodesic shells({len(shg)}): {shg}")
# partition identity: map each vertex to (chord-shell-index, geo-shell-index)
ci={s:i for i,s in enumerate(shc)}; gi={s:i for i,s in enumerate(shg)}
pairs=set((ci[rc[v]],gi[rg[v]]) for v in range(1,120))
mono = all(len(set(g for c,g in pairs if c==cc))==1 for cc in range(len(shc)))
inv  = all(len(set(c for c,g in pairs if g==gg))==1 for gg in range(len(shg)))
print(f"pairs (chord-idx, geo-idx): {sorted(pairs)}")
print(f"chord->geo single-valued: {mono}; geo->chord single-valued: {inv}")
print(f"IDENTICAL PARTITION: {'YES' if (mono and inv and len(shc)==len(shg)) else 'NO'}")
# shell multiplicities
import collections
mc=collections.Counter(rc[1:]); print("chord shell sizes:", [mc[s] for s in shc])
#!/usr/bin/env python3
"""Sanity check 2: periodic FCC/HCP/dhcp tori, minimum-image kernel.
Verify: site counts, all-sites-z=12 at nn distance, min box vs nn safety,
image-tie census at nn shell, and solver runs with 1/D_minimage kernel."""
import math, numpy as np
PHI=(1+math.sqrt(5))/2; L_UNIT=0.589; A=L_UNIT/PHI
alpha=A/(math.pi*math.sqrt(2))

def fcc_torus(na,nb,nc):
    ac=A*math.sqrt(2.0)  # conventional cubic edge
    basis=np.array([[0,0,0],[0,.5,.5],[.5,0,.5],[.5,.5,0]])*ac
    pts=[]
    for i in range(na):
        for j in range(nb):
            for k in range(nc):
                for b in basis: pts.append(b+np.array([i,j,k])*ac)
    box=np.array([na,nb,nc])*ac
    return np.array(pts),box

def hex_layers(na,nb,stack,c_over_a=math.sqrt(8/3)):
    """stack: string over {A,B,C}; hexagonal in-plane lattice, nn=A."""
    a1=np.array([1.0,0.0]); a2=np.array([0.5,math.sqrt(3)/2])
    offs={'A':np.array([0.0,0.0]),'B':(a1+a2)/3,'C':2*(a1+a2)/3}
    dz=c_over_a/2*A  # interlayer spacing for ideal close packing = sqrt(2/3)*A
    dz=math.sqrt(2.0/3.0)*A
    pts=[]
    for m,layer in enumerate(stack):
        o=offs[layer]
        for p in range(na):
            for q in range(nb):
                xy=(p*a1+q*a2+o)*A
                pts.append([xy[0],xy[1],m*dz])
    # lattice vectors of the torus (non-orthogonal in-plane)
    L=np.array([[na*A,0,0],[nb*0.5*A,nb*math.sqrt(3)/2*A,0],[0,0,len(stack)*dz]])
    return np.array(pts),L

def minimage_D(P,L):
    """L rows = lattice vectors. Exact minimum over 27 neighbor images."""
    n=len(P); diff=P[:,None,:]-P[None,:,:]
    best=None
    for i in (-1,0,1):
        for j in (-1,0,1):
            for k in (-1,0,1):
                sh=i*L[0]+j*L[1]+k*L[2]
                d=np.linalg.norm(diff+sh,axis=2)
                best=d if best is None else np.minimum(best,d)
    return best

def audit(name,P,L):
    D=minimage_D(P,L); np.fill_diagonal(D,np.inf)
    nn=D.min(); z=np.sum(np.abs(D-nn)<1e-9*max(1,nn),axis=1)
    boxmin=min(np.linalg.norm(v) for v in L)
    # tie census: count pairs whose minimum distance is achieved by >1 image (nn shell only)
    print(f"{name:14s} N={len(P):3d} nn={nn:.4f} z(all)={sorted(set(z))} "
          f"min|L|={boxmin:.3f} ({boxmin/nn:.2f} nn) "
          f"{'OK' if set(z)=={12} else '** z DEFECT **'}")
    return D

print("== FCC tori ==")
for dims in ((5,3,2),(3,3,3),(2,2,2),(3,2,2),(3,3,2),(2,3,4),(4,3,2),(3,3,4),(4,4,3),(4,4,4)):
    P,Lb=fcc_torus(*dims); L=np.diag(Lb)
    audit(f"FCC{dims}",P,L)

print("== HCP tori (AB stacking) ==")
for na,nb,nl in ((5,6,2),(6,5,2),(3,3,6),(5,3,4),(5,4,3),(6,3,4),(3,6,6)):
    P,L=hex_layers(na,nb,"AB"*(nl//2)) if nl%2==0 else (None,None)
    if P is None: continue
    audit(f"HCP({na},{nb})x{nl}",P,L)

print("== dhcp tori (ABAC stacking) ==")
for na,nb,nl in ((5,6,4),(3,3,12),(5,3,8),(3,3,4),(5,2,12)):
    if nl%4: continue
    P,L=hex_layers(na,nb,"ABAC"*(nl//4))
    audit(f"dhcp({na},{nb})x{nl}",P,L)

print("\n== solver smoke test: FCC(5,3,2) N=120, 1/D_minimage kernel ==")
P,Lb=fcc_torus(5,3,2); L=np.diag(Lb); D=minimage_D(P,L)
src=0; mask=np.ones(len(P),bool); mask[src]=False
r0=D[src,mask]; Dq=D[np.ix_(mask,mask)].copy(); np.fill_diagonal(Dq,np.inf)
f=np.linalg.solve(np.eye(len(r0))+alpha/Dq,1.0/r0)
negfrac=(f<0).mean()
print(f"solved OK; neg-frac={negfrac:.3f} (RESULT-ADJACENT — recon only, NOT committed)")
