#!/usr/bin/env python3
"""
Rod transport-efficiency: does a long rigid Cross-Rod's MOMENTUM-TRANSFER cross-section
(what cores a halo) track its GEOMETRIC cross-section (what sigma/m=0.11*N counts), or is
it suppressed?  The fork: eps = sigma_T/sigma_geom ~ 1 => sigma_T/m ~ 0.11*N grows with N
=> long rods over-core => SHORT (N~15) wins; eps small and falling with N => long rods OK.

Model: two identical hard capsules (spherocylinders), radius r, cylinder length L, thin-rod
inertia (I_perp=M L^2/12, I_par=M r^2/2).  Elastic, frictionless (normal impulse) rigid-body
collision with rotation.  Orientations isotropic, impact parameter uniform in a disk.  In the
CM frame the incoming relative velocity is along +z; we measure the deflection theta of the
relative CM velocity and accumulate sigma_geom (collision area) and sigma_T=<(1-cos theta)>*area.
Aspect ratio A = L/(2r).  Cross-Rod is 4-CP wide => A ~ N/4 (N elements).
Sanity: A->0 (sphere) must give eps=1 (hard-sphere sigma_T=sigma_geom).
"""
import numpy as np
rng = np.random.default_rng(7)

def seg_seg_closest(p1,d1,h1,p2,d2,h2):
    # closest points between segment i: c_i + s*d_i, s in [-h_i,h_i]; d_i unit. Returns dist, and the two points.
    r = p1-p2
    a=1.0; b=np.dot(d1,d2); c=1.0
    d=np.dot(d1,r); e=np.dot(d2,r)
    den=a*c-b*b
    if den>1e-9:
        s=(b*e-c*d)/den; s=np.clip(s,-h1,h1)
    else:
        s=0.0
    t=(b*s+e)/c; 
    if t<-h2 or t>h2:
        t=np.clip(t,-h2,h2); s=np.clip((b*t-d)/a,-h1,h1)
    cp1=p1+s*d1; cp2=p2+t*d2
    return np.linalg.norm(cp1-cp2), cp1, cp2

def rand_dir():
    v=rng.normal(size=3); return v/np.linalg.norm(v)

def inertia_inv(dhat,Iperp,Ipar):
    P=np.outer(dhat,dhat)
    return (1.0/Ipar)*P + (1.0/Iperp)*(np.eye(3)-P)

def collide_theta(A, n_s):
    r=1.0; L=2*r*A; h=L/2.0; twor=2*r
    M=1.0; Iperp=M*L*L/12.0 if L>0 else M*r*r*0.4; Ipar=M*r*r*0.5
    Rmax=(L+twor)*1.1 + twor          # impact-param disk radius
    reach=(L+twor)*1.2
    dzs=np.linspace(-reach,reach,80)
    ncol=0; sumT=0.0
    for _ in range(n_s):
        d1=rand_dir(); d2=rand_dir()
        # impact parameter uniform in disk
        rr=Rmax*np.sqrt(rng.random()); ph=2*np.pi*rng.random()
        bx,by=rr*np.cos(ph),rr*np.sin(ph)
        p2=np.array([0.,0.,0.])                  # capsule2 CM at origin
        # capsule1 sweeps along +z: CM = (bx,by,dz)
        dist=np.empty_like(dzs)
        for i,dz in enumerate(dzs):
            dist[i]=seg_seg_closest(np.array([bx,by,dz]),d1,h,p2,d2,h)[0]
        below=dist<twor
        if not below.any(): 
            continue
        i0=np.argmax(below)                       # first entering contact (coming from -z)
        if i0==0: 
            # started already overlapping; refine outward not needed, use it
            dzc=dzs[0]
        else:
            # bisect between dzs[i0-1] (outside) and dzs[i0] (inside)
            lo,hi=dzs[i0-1],dzs[i0]
            for _ in range(30):
                mid=0.5*(lo+hi)
                dm=seg_seg_closest(np.array([bx,by,mid]),d1,h,p2,d2,h)[0]
                if dm<twor: hi=mid
                else: lo=mid
            dzc=hi
        pc1=np.array([bx,by,dzc])
        dist_c,cp1,cp2=seg_seg_closest(pc1,d1,h,p2,d2,h)
        nhat=cp1-cp2; nn=np.linalg.norm(nhat)
        if nn<1e-9: 
            continue
        nhat=nhat/nn
        cpt=0.5*(cp1+cp2)                         # contact point
        r1=cpt-pc1; r2=cpt-p2
        # CM-frame incoming: v1=+u/2 z, v2=-u/2 z ; u=1 along z
        u=np.array([0.,0.,1.0])
        v1=0.5*u; v2=-0.5*u; w1=np.zeros(3); w2=np.zeros(3)
        # relative velocity at contact (1 minus 2)
        vc=(v1+np.cross(w1,r1))-(v2+np.cross(w2,r2))
        vn=np.dot(vc,nhat)
        if vn>=0:                                  # separating; not a real approaching contact
            continue
        Ii1=inertia_inv(d1,Iperp,Ipar); Ii2=inertia_inv(d2,Iperp,Ipar)
        # effective normal mass
        t1=np.cross(Ii1@np.cross(r1,nhat),r1)
        t2=np.cross(Ii2@np.cross(r2,nhat),r2)
        keff=1.0/M+1.0/M+np.dot(nhat,t1+t2)
        j=-(1+1.0)*vn/keff                         # elastic e=1
        J=j*nhat
        v1n=v1+J/M; v2n=v2-J/M
        u_out=v1n-v2n
        cth=np.dot(u,u_out)/(np.linalg.norm(u)*np.linalg.norm(u_out))
        cth=np.clip(cth,-1,1)
        ncol+=1; sumT+=(1-cth)
    area=np.pi*Rmax*Rmax
    sig_geom=area*ncol/n_s
    sig_T=area*sumT/n_s
    return sig_geom,sig_T,ncol

print(f"{'A=L/2r':>8} {'N~4A':>6} {'sig_geom/r^2':>13} {'sig_T/r^2':>11} {'eps=sT/sg':>10} {'sig_T/mass*':>11} {'Ncol':>6}")
print("  (mass ~ N ~ 4A;  sig_T/mass* = (sig_T/r^2)/(4A) tracks the physical sigma_T/m scaling)")
for A in [0.0, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0]:
    ns = 4000 if A<=8 else (2500 if A<=32 else 1500)
    sg,sT,nc=collide_theta(A, ns)
    Nn=max(4*A,1.0)
    sTm=(sT)/(4*A) if A>0 else sT
    eps=sT/sg if sg>0 else float('nan')
    print(f"{A:>8.1f} {Nn:>6.0f} {sg:>13.2f} {sT:>11.2f} {eps:>10.3f} {sTm:>11.3f} {nc:>6d}")
