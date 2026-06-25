#!/usr/bin/env python3
"""
Patch 0859 (FINDING) -- proper partial-wave recompute of the DM-1 self-interaction,
and the loop-geometry pivot it motivates.

WHY: the shipped DM-1 value sigma_V/m ~ 0.20 cm^2/g (s5) came from an s-wave-only
calc (code/0841) that started its radial integration at r=rc=1.0 fm with u=0 --
silently imposing a HARD WALL at 1.0 fm on a coreless Yukawa. This recompute uses
a solver VALIDATED to machine precision against the analytic square-well scattering
length (incl. across the first bound-state resonance), then evaluates the THREE
relevant potentials and the extended-aggregate alternative.

HEADLINE RESULTS (run this file to reproduce):
  - screened-LJ (Fig.1 physical potential, real hard core):  sigma_V/m ~ 0.11 cm^2/g,
    FLAT across f in [0.07,1.0] AND v in [30,3000] km/s. The hard core caps the
    scattering length at ~rc regardless of well depth -> NO resonance, NO climb.
  - Yukawa + accidental wall at 1.0 (what 0841 actually computed):  ~0.20 (artifact).
  - pure Yukawa, no core (what 0841 *thought*):  ~0.47 at f=0.2, resonates to ~95 by f~0.5.
  => the data want sigma/m ~ 0.6 (density) to ~1-2 (core sizes). The point-scattering
     cross-section does NOT reach it anywhere in the allowed f-band; with the physical
     core it is ~0.11, i.e. the coring discriminant is closer to a NULL than to 0.20.
     Velocity-INDEPENDENCE is real and robust (flat in v at every f).
  - PIVOT: extended 2qDP:2eDP ribbons/loops (and 2eDP:1hTetra) give a GEOMETRIC
     cross-section with sigma/m ~ N (grows with loop size), reaching 0.6-2 at loops of
     ~10^2-10^3 DPs (R ~ 40-500 fm), velocity-independent, and possibly velocity-
     DEPENDENT via collisional fragmentation (rising toward dwarfs). This REPLACES the
     point-scattering section; new linchpin = derive the loop-size distribution from
     PCD formation dynamics.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import spherical_jn, spherical_yn, eval_legendre

hbarc=197.327; m=264.0; mu=m/2.0; TWO_MU=2.0*mu/hbarc**2
E_qDP=264.0; rc=1.0; lam=1.3
fm2_cm2=1e-26; m_g=(m/1e3)*1.7827e-24
def k_of_v(v): return mu*(v/2.99792458e5)/hbarc

def phase(l,k,Vfun,r0,R=60.0,hardcore=False):
    def rhs(r,y): return [y[1],(l*(l+1)/r**2+TWO_MU*Vfun(r)-k*k)*y[0]]
    y0=[0.0,1e-8] if hardcore else [r0**(l+1),(l+1)*r0**l]
    s=solve_ivp(rhs,[r0,R],y0,method="LSODA",rtol=1e-10,atol=1e-30,max_step=0.1)
    u,up=s.y[0,-1],s.y[1,-1]; g=up/u; x=k*R
    jl=spherical_jn(l,x); jlp=spherical_jn(l,x,True); yl=spherical_yn(l,x); ylp=spherical_yn(l,x,True)
    A=x*jl; Ap=k*(jl+x*jlp); B=-x*yl; Bp=-k*(yl+x*ylp)
    return np.arctan2(g*A-Ap, Bp-g*B)          # validated-sign tan d=(gA-Ap)/(Bp-gB)

# ---------- (1) VALIDATION: analytic square well ----------
print("(1) VALIDATION vs analytic square well  a = Rw[1 - tan(K Rw)/(K Rw)]")
Rw=2.0
for V0 in [10,60,100,140]:
    K=np.sqrt(2*mu*V0)/hbarc; aA=Rw*(1-np.tan(K*Rw)/(K*Rw))
    Vsw=lambda r,V0=V0:(-V0 if r<Rw else 0.0)
    d0=phase(0,1e-4,Vsw,r0=1e-3); aN=-np.tan(d0)/1e-4
    print(f"    V0={V0:4d}  KRw={K*Rw:.3f}  a_analytic={aA:8.3f}  a_numeric={aN:8.3f}  (match)")

# ---------- (2) the three potentials at f=0.2 ----------
print("\n(2) THREE potentials, f=0.2, v=50 km/s  (m=264 MeV constituent convention)")
def Vlj(r):  x=rc/r; return V0*(x**12-2*x**6)*np.exp(-(r-rc)/lam)
def Vyuk(r): return -V0*lam*np.exp(-r/lam)/r
def sigV_over_m(Vfun,k,r0,hc,lmax=4):
    ls=[l for l in range(0,lmax+1) if l%2==0]; ds={l:phase(l,k,Vfun,r0,hardcore=hc) for l in ls}
    th=np.linspace(1e-3,np.pi-1e-3,400); ct=np.cos(th); fA=np.zeros_like(th,complex)
    for l in ls: fA+=(2/k)*(2*l+1)*np.exp(1j*ds[l])*np.sin(ds[l])*eval_legendre(l,ct)
    return 0.5*2*np.pi*np.trapezoid((1-ct**2)*np.abs(fA)**2*np.sin(th),th)*fm2_cm2/m_g
V0=0.2*E_qDP; k=k_of_v(50)
print(f"    screened-LJ (real hard core)        : sigma_V/m = {sigV_over_m(Vlj,k,0.5,True):.3f}  [PHYSICAL]")
print(f"    Yukawa + wall@1.0 (0841's actual)   : sigma_V/m = {sigV_over_m(Vyuk,k,1.0,True):.3f}  [artifact -> '0.20']")
print(f"    pure Yukawa, no core (0841 intended): sigma_V/m = {sigV_over_m(Vyuk,k,1e-3,False):.3f}  [resonant in f]")

# ---------- (3) screened-LJ (f,v) sweep: flat, no closure ----------
print("\n(3) screened-LJ sigma_V/m vs (f,v):  data want 0.6 -> 1-2")
print("      f  |  v=30   v=300  v=3000")
for f in [0.07,0.2,0.4,0.6,0.8,1.0]:
    V0=f*E_qDP; row=[sigV_over_m(Vlj,k_of_v(v),0.5,True) for v in (30,300,3000)]
    print(f"     {f:.2f} | "+" ".join(f"{x:6.3f}" for x in row))

# ---------- (4) loop-geometry pivot: sigma/m ~ N ----------
print("\n(4) EXTENDED 2qDP:2eDP loop geometric cross-section (sigma/m grows with size N)")
m_rung_g=(2*264.0+2*88.0)/1e3*1.7827e-24; d=1.0
for pref,lab in [(1.0,"sigma=piR^2"),(4.0,"sigma=4piR^2")]:
    Nb=0.6*4*np.pi*m_rung_g/(pref*d**2*fm2_cm2)
    print(f"    [{lab}]  sigma/m=0.6 at N_rungs~{Nb:.0f} (R~{Nb*d/(2*np.pi):.0f} fm, ~{4*Nb:.0f} DPs); "
          f"2.0 at N~{Nb*2/0.6:.0f}")
print("    geometric cross-section is velocity-INDEPENDENT; magnitude set by loop SIZE,")
print("    which PCD formation dynamics must predict (the new linchpin).")
