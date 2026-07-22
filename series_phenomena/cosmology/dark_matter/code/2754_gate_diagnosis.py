#!/usr/bin/env python3
"""Patch 2754 -- verify script for the B-CHECK-80 gate diagnosis.

Reproduces, at machine precision, the localization of the A-path
self-pair defect found by the 2753 Hamiltonian-identity gate:
for five seed-1 trial moves at N = 80,
    dE_A - dE_B == Q2*Z_i^2 * f(|old - new|)
with f the masked erfc + softcore pair interaction, residuals
<= ~1e-13. Also prints g(|delta|) magnitudes against THETA and the
acceptance-suppression factor exp(-g/THETA).

Run from series_phenomena/cosmology/dark_matter/:
    python3 code/2754_gate_diagnosis.py
"""
import math, numpy as np
from scipy.special import erfc as serfc

HBARC=197.3269788; AEM=1/137.035999084
PHI=(1+math.sqrt(5))/2; A=0.589/PHI
NCP=2*math.sqrt(2.0)/A**3; Q2=AEM*HBARC
THETA=2*math.sqrt(2)*math.pi*Q2/A
N=80; A_S=0.04; EPS=2.4
L=(N/NCP)**(1.0/3.0); B_=2*math.pi/L
ks=[(nx,ny,nz) for nx in range(-6,7) for ny in range(-6,7)
    for nz in range(-6,7)
    if 0<nx*nx+ny*ny+nz*nz<=27 and
       ((nx>0) or (nx==0 and ny>0) or (nx==0 and ny==0 and nz>0))]
KV=2*math.pi/L*np.array(ks,float); K2=(KV**2).sum(1)
ALPHA=5.6/L; RC=L/2
WK=np.exp(-K2/(4*ALPHA*ALPHA))/K2
PREF=2*(2*math.pi/(L**3))*Q2
Z=np.array([1.0]*(N//2)+[-1.0]*(N//2))
KD=np.array([B_,0.0,0.0])

def total_B(x):
    E=0.0
    for i in range(N-1):
        d=x[i+1:]-x[i]; d-=L*np.round(d/L)
        rr2=(d*d).sum(1); rr=np.sqrt(rr2); keep=(rr<RC)
        E+=float(np.sum(Q2*(Z[i+1:]*Z[i])[keep]*(serfc(ALPHA*rr[keep])/rr[keep]
                 -1.0/rr[keep]+1.0/np.sqrt(rr2[keep]+A_S*A_S))))
    Sf=(Z[:,None]*np.exp(1j*(x@KV.T))).sum(0)
    E+=float(PREF*np.sum(WK*(Sf.real**2+Sf.imag**2)))
    return E+EPS*float(np.sum(Z*np.cos(x@KD)))

def dE_A(pos,S,i,newp):
    """run_A increment VERBATIM (2746/2749) -- carries the defect."""
    d_o=pos-pos[i]; d_n=pos-newp
    d_o-=L*np.round(d_o/L); d_n-=L*np.round(d_n/L)
    r2o=(d_o**2).sum(1); r2n=(d_n**2).sum(1)
    ro=np.sqrt(r2o); rn=np.sqrt(r2n)
    zz=Q2*(Z*Z[i])
    mo=(ro<RC)&(ro>1e-12); mn=(rn<RC)&(rn>1e-12)
    eo=np.sum(zz[mo]*(serfc(ALPHA*ro[mo])/ro[mo]-1.0/ro[mo]
                      +1.0/np.sqrt(r2o[mo]+A_S*A_S)))
    en=np.sum(zz[mn]*(serfc(ALPHA*rn[mn])/rn[mn]-1.0/rn[mn]
                      +1.0/np.sqrt(r2n[mn]+A_S*A_S)))
    dS=Z[i]*(np.exp(1j*(newp@KV.T))-np.exp(1j*(pos[i]@KV.T)))
    Snew=S+dS
    dEk=PREF*np.sum(WK*((Snew.real**2+Snew.imag**2)-(S.real**2+S.imag**2)))
    dE=en-eo+dEk
    dE+=EPS*Z[i]*(math.cos(float(KD@newp))-math.cos(float(KD@pos[i])))
    return float(dE)

def f_pair(r):
    return serfc(ALPHA*r)/r-1.0/r+1.0/math.sqrt(r*r+A_S*A_S)

rng=np.random.default_rng(1)
x=rng.uniform(0,L,size=(N,3))
S=(Z[:,None]*np.exp(1j*(x@KV.T))).sum(0)
E0=total_B(x); step=0.20*A
print(f"THETA = {THETA:.3f} MeV ; g(r->0) -> Q2*(1/a_s - 2*alpha/sqrt(pi))"
      f" = {Q2*(1/A_S-2*ALPHA/math.sqrt(math.pi)):.2f} MeV")
ok=True
for t in range(5):
    j=int(rng.integers(N))
    xn=x.copy(); xn[j]=(xn[j]+rng.normal(0,step,3))%L
    dB=total_B(xn)-E0
    dA=dE_A(x,S,j,xn[j])
    d=x[j]-xn[j]; d-=L*np.round(d/L); r=float(np.sqrt((d*d).sum()))
    g=Q2*Z[j]*Z[j]*f_pair(r) if 1e-12<r<RC else 0.0
    res=dA-dB-g
    print(f"move {t}: |delta|={r:.4f}  g={g:+8.4f} MeV  "
          f"exp(-g/THETA)={math.exp(-g/THETA):.3f}  residual={res:+.3e}")
    ok&=abs(res)<=1e-10
print("IDENTITY dE_A - dE_B == g(|delta|):", "CONFIRMED" if ok else "FAILED")
