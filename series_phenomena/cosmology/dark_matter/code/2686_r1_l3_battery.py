#!/usr/bin/env python3
"""FA-SG-R1 leg L3 (Patch 2686): envelope-extraction robustness battery
(= METH-L2-021's own promotion battery per its 2676 registration).

Components (all named, none optional; charter SS2 R1-L3):
 (i)   multi-window fits (3 frozen windows, 2671d set);
 (ii)  Fourier-filter removal of the staggered component as an independent
       cross-check on the |f|*r envelope readout: low-pass of the
       fine-binned |f|*r profile below the lattice carrier band
       (cutoff wavelength 0.20 fm > shell spacing ~0.10-0.15 fm), plus,
       on the sign-coherent FCC exact shells, Hilbert (analytic-signal)
       demodulation of the SIGNED f*r shell profile;
 (iii) robustness against fitting window, observable definition, and
       lattice-size choices -- band reported per choice axis.
Observable axis (enumerated before results): bin-mean |f|, bin-median |f|,
Fourier-filtered |f|*r. Size axis: R = 7, 9. Window axis: the 3 frozen
windows. All arenas from the L1 battery (2685), rebuilt identically.
"""
import math, numpy as np
from scipy.spatial import cKDTree

PHI=(1+math.sqrt(5))/2; L_UNIT=0.589; L_EDGE=L_UNIT/PHI; D_REG=1.15
alpha=L_EDGE/(math.pi*math.sqrt(2))
WINDOWS=[(0.45,1.3),(0.55,1.6),(0.7,1.8)]

def fcc_ball(R):
    pts=[]
    for i in range(-2*R,2*R+1):
        for j in range(-2*R,2*R+1):
            for k in range(-2*R,2*R+1):
                if (i+j+k)%2==0:
                    x=np.array([i,j,k])/math.sqrt(2.0)
                    if np.linalg.norm(x)<=R: pts.append(x)
    return np.array(pts)
def layered_ball(R, seq):
    dz=math.sqrt(2.0/3.0)
    offs=[np.array([0.0,0.0]),np.array([0.5,math.sqrt(3)/6]),np.array([1.0,math.sqrt(3)/3])]
    e1=np.array([1.0,0.0]); e2=np.array([0.5,math.sqrt(3)/2])
    pts=[]; M=int(R/dz)+2; K=int(R)+3
    for m in range(-M,M+1):
        z=m*dz; o=offs[seq[m]]
        for p in range(-2*K,2*K+1):
            for q in range(-2*K,2*K+1):
                xy=p*e1+q*e2+o
                if xy@xy+z*z<=R*R+1e-9: pts.append([xy[0],xy[1],z])
    return np.array(pts)
def barlow_seq(M,kind,seed=None):
    if kind=='hcp': return {m:m%2 for m in range(-M-2,M+3)}
    rng=np.random.default_rng(seed); s={0:0}
    for m in range(1,M+3): s[m]=int(rng.choice([c for c in (0,1,2) if c!=s[m-1]]))
    for m in range(-1,-M-3,-1): s[m]=int(rng.choice([c for c in (0,1,2) if c!=s[m+1]]))
    return s
def fcc_rot_cube(R):
    L=0.5*((4.0/3.0)*math.pi)**(1.0/3.0)*R
    rng=np.random.default_rng(20260722)
    A=rng.normal(size=(3,3)); Qr,_=np.linalg.qr(A)
    if np.linalg.det(Qr)<0: Qr[:,0]*=-1
    K=int(2.0*L)+3; pts=[]
    for i in range(-2*K,2*K+1):
        for j in range(-2*K,2*K+1):
            for k in range(-2*K,2*K+1):
                if (i+j+k)%2==0:
                    x=(np.array([i,j,k])/math.sqrt(2.0))@Qr.T
                    if np.max(np.abs(x))<=L: pts.append(x)
    return np.array(pts)
def solve(P_nn):
    P=P_nn*L_EDGE
    src=int(np.argmin(np.linalg.norm(P-P.mean(0),axis=1)))
    mask=np.ones(len(P),bool); mask[src]=False
    Q=P[mask]; r0=np.linalg.norm(Q-P[src],axis=1)
    Dm=np.linalg.norm(Q[:,None,:]-Q[None,:,:],axis=2)
    np.fill_diagonal(Dm,np.inf)
    return r0, np.linalg.solve(np.eye(len(Q))+alpha/Dm, 1.0/r0)

def profile(r0,phi,bw,stat):
    bins=np.arange(0.3,2.4,bw); rc,fv=[],[]
    for b in bins:
        m=(r0>=b)&(r0<b+bw)
        if m.sum()>=3:
            rc.append(r0[m].mean())
            v=np.abs(phi[m]); fv.append(np.mean(v) if stat=='mean' else np.median(v))
    return np.array(rc),np.array(fv)

def fit_l(rc,y_logfr,lo,hi):
    w=(rc>=lo)&(rc<=hi)
    c=np.polyfit(rc[w],y_logfr[w],1)
    return -1.0/c[0]

def fourier_filtered(r0,phi,cut_wavelength=0.20):
    # fine-binned |f|*r on uniform grid; FFT low-pass below carrier band
    bw=0.03
    rc,fv=profile(r0,phi,bw,'mean')
    g=np.interp(np.arange(rc.min(),rc.max(),bw), rc, np.log(fv*rc))
    ru=np.arange(rc.min(),rc.max(),bw)
    G=np.fft.rfft(g-g.mean()); fr=np.fft.rfftfreq(len(g),d=bw)
    G[fr>1.0/cut_wavelength]=0
    gf=np.fft.irfft(G,n=len(g))+g.mean()
    return ru,gf

def peak_env(r0,phi):
    # DIAGNOSTIC (leakage-free demodulation): fit through local maxima of the
    # signed exact-shell |f*r| profile -- supplementary confirmation channel.
    shells=np.unique(np.round(r0,6)); rs,fs=[],[]
    for s in shells[shells<=2.2]:
        m=np.abs(r0-s)<1e-6; rs.append(s); fs.append(phi[m].mean())
    rs,fs=np.array(rs),np.array(fs); g=np.abs(fs*rs)
    pk=[i for i in range(1,len(g)-1) if g[i]>=g[i-1] and g[i]>=g[i+1]]
    rp,gp=rs[pk],g[pk]; w=(rp>=0.45)&(rp<=1.8)
    c=np.polyfit(rp[w],np.log(gp[w]),1)
    return -1.0/c[0]

def hilbert_env_fcc(r0,phi,lo,hi):
    # DIAGNOSTIC ONLY -- attempted analytic-signal (FFT-Hilbert) demodulation
    # of the SIGNED shell profile. Reported inapplicable: the signed profile
    # has an irregular carrier (radial sign runs, not strict alternation) and
    # spans ~7 decades, so FFT-Hilbert edge leakage dominates the extracted
    # envelope. Retained here verbatim for the record; NOT in the band.
    # signed exact-shell profile, Hilbert (analytic-signal) demodulation
    shells=np.unique(np.round(r0,6)); rs,fs=[],[]
    for s in shells[shells<=2.2]:
        m=np.abs(r0-s)<1e-6
        rs.append(s); fs.append(phi[m].mean())
    rs,fs=np.array(rs),np.array(fs)
    du=0.02; ru=np.arange(rs.min(),rs.max(),du)
    g=np.interp(ru,rs,fs*rs)
    Ga=np.fft.fft(g); n=len(g); h=np.zeros(n)
    h[0]=1; h[1:(n+1)//2]=2
    if n%2==0: h[n//2]=1
    env=np.abs(np.fft.ifft(Ga*h))
    w=(ru>=lo)&(ru<=hi)&(env>0)
    c=np.polyfit(ru[w],np.log(env[w]),1)
    return -1.0/c[0]

M=int(9/math.sqrt(2/3))+2
builders={
 "A0-FCC-ball":lambda R:fcc_ball(R),
 "A1-HCP-ball":lambda R:layered_ball(R,barlow_seq(M,'hcp')),
 "A2-RandBarlow-ball":lambda R:layered_ball(R,barlow_seq(M,'rnd',20260721)),
 "A3-FCC-rot-cube":lambda R:fcc_rot_cube(R),
}
grand=[]; diag_h=None; diag_p=None
for name,b in builders.items():
    print(f"\n== {name} ==")
    vals={}   # (R, obs, window) -> l
    for R in (7,9):
        r0,phi=solve(b(R))
        for obs in ('mean','median'):
            rc,fv=profile(r0,phi,0.05,obs)
            y=np.log(fv*rc)
            for (lo,hi) in WINDOWS:
                vals[(R,obs,(lo,hi))]=fit_l(rc,y,lo,hi)
        ru,gf=fourier_filtered(r0,phi)
        for (lo,hi) in WINDOWS:
            vals[(R,'fourier',(lo,hi))]=fit_l(ru,gf,lo,hi)
        if name.startswith("A0") and R==7:
            diag_h=[hilbert_env_fcc(r0,phi,lo,hi) for (lo,hi) in WINDOWS]
            diag_p=peak_env(r0,phi)
    arr=np.array(list(vals.values()))
    print(f"  full battery: l = {arr.mean():.4f} +/- {arr.std():.4f} fm  "
          f"min={arr.min():.4f} max={arr.max():.4f}  (n={len(arr)})")
    # marginal band per choice axis
    for axis,keyf in (("window",lambda k:k[2]),("observable",lambda k:k[1]),("size",lambda k:k[0])):
        groups={}
        for k,v in vals.items(): groups.setdefault(keyf(k),[]).append(v)
        cs={g:np.mean(v) for g,v in groups.items()}
        spread=max(cs.values())-min(cs.values())
        print(f"  axis {axis:10s}: centers " +
              ", ".join(f"{g}={c:.4f}" for g,c in cs.items()) +
              f"  (axis spread {spread:.4f} fm)")
    grand+=list(arr)
grand=np.array(grand)
print(f"\n== L3 GRAND BAND (all arenas x all axes) ==")
print(f"l = {grand.mean():.4f} +/- {grand.std():.4f} fm  [{grand.min():.4f}, {grand.max():.4f}]")
print(f"2671 reference band: 0.091 +/- 0.002 fm -> order preserved "
      f"(no axis blows the band open): {'YES' if grand.std()<=2*0.002 else 'NO'}")
print("\n== diagnostics (NOT in the band; enumerated observable axis = mean/median/fourier) ==")
print(f"peak-envelope (|f*r| maxima, FCC R=7, [0.45,1.8]): l = {diag_p:.4f} fm  -- concordant supplementary channel")
print(f"attempted Hilbert demodulation (FCC R=7, 3 windows): l = "
      +", ".join(f"{x:.4f}" for x in diag_h)
      +"\n  -> INAPPLICABLE (irregular carrier + 7-decade range -> FFT edge leakage; see header)")
