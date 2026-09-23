#!/usr/bin/env python3
"""4240 -- TODO-4234-DELTA, first computation: g_A = (5/3) x R from the cage.
Part A: the 5/3 from the SS-2 cage (two u at mirror-equivalent vertices V1,V2; d at V3), the SS-1c colour singlet
        (totally antisymmetric over V1..V3), L = 0, and quantum spin-1/2 (premise: OPEN-QM-3, as used throughout 4223-4228).
Part B: which FAMILY can supply R = 0.765, tested jointly against mu_p (4126: M_N/m_q = 3.00 with m_q = m_p/3).
        B1 Dirac quark confined in a cavity (lower-component reduction; imported MIT boundary)  -- one spinor, both observables.
        B2 spin-orbit sharing at the constituent scale (each quark's j split s = R j, l = (1-R) j; moment ~ (1+R)/2).
Part C: in family B2 read as a moving Dirac quark, the momentum R requires, against the corpus's own scales.
Inputs: m_const = m_p/3 (SS-2 line 183 -- an assignment, not a derivation), l_unit = hbar c/Lambda = 0.589 fm (SS-2),
        r_ZBW = hbar c/m_const, SS-2 cage distances u-u 1.071, u-d 0.620 fm."""
import itertools, numpy as np
from scipy.optimize import brentq
from scipy.special import spherical_jn as jn
from scipy.integrate import quad
hc=197.327; MN=938.919; mp=938.272; mq=mp/3; muN=hc/(2*MN)
gA_t=1.2754; mup_t=2.79285; mun_t=-1.91304
print("="*78); print("PART A -- the 5/3 from exchange symmetry of the SS-2 cage"); print("="*78)
# basis: quark slots (V1,V2,V3); flavour fixed u,u,d as in SS-2; spin up=+1/2 (index 0), down (index 1)
def ket(spins):
    v=np.zeros(8); v[spins[0]*4+spins[1]*2+spins[2]]=1; return v
U,D=0,1
# colour antisymmetric (SS-1c) and L = 0 symmetric => spin x flavour symmetric under V1<->V2 (the two u's).
# J=1/2, Jz=+1/2 states of three spins: enumerate, then impose symmetry under swap of slots 1,2.
basis=[ket(s) for s in itertools.product([0,1],repeat=3) if sum(1 for x in s if x==0)==2]  # Jz=+1/2
def swap12(v):
    w=np.zeros(8)
    for i in range(8):
        a,b,c=(i>>2)&1,(i>>1)&1,i&1; w[b*4+a*2+c]+=v[i]
    return w
def Sz(v,slot):
    w=np.zeros(8)
    for i in range(8):
        bit=(i>>(2-slot))&1; w[i]=v[i]*(0.5 if bit==0 else -0.5)
    return w
def S2(v):  # total spin squared
    ops=[]
    def sp(v,slot,sign):
        w=np.zeros(8)
        for i in range(8):
            bit=(i>>(2-slot))&1
            if sign>0 and bit==1: w[i ^ (1<<(2-slot))]+=v[i]
            if sign<0 and bit==0: w[i ^ (1<<(2-slot))]+=v[i]
        return w
    Szt=sum(Sz(v,k) for k in range(3))
    Sp=lambda x: sum(sp(x,k,+1) for k in range(3)); Sm=lambda x: sum(sp(x,k,-1) for k in range(3))
    Szf=lambda x: sum(Sz(x,k) for k in range(3))
    return Sm(Sp(v))+Szf(Szf(v))+Szf(v)
B=np.array(basis).T
# build the J=1/2 subspace symmetric under 1<->2
H=np.array([[bi@S2(bj) for bj in basis] for bi in basis]); P=np.array([[bi@swap12(bj) for bj in basis] for bi in basis])
ev,vec=np.linalg.eigh(H+10*P)   # S^2=3/4 and P=+1  -> eigenvalue 0.75+10
k=np.argmin(abs(ev-10.75)); c=vec[:,k]; psi=B@c
Du=psi@(2*Sz(psi,0))+psi@(2*Sz(psi,1)); Dd=psi@(2*Sz(psi,2))
print(f"J=1/2, Jz=+1/2 state symmetric under V1<->V2 (unique: eigenvalue count {sum(abs(ev-10.75)<1e-9)}):")
print(f"  Delta u = {Du:+.4f} (4/3)   Delta d = {Dd:+.4f} (-1/3)   g_A(R=1) = Delta u - Delta d = {Du-Dd:.4f} (5/3)")
print(f"  classical product u^ u^ d_ (4126's shorthand, NOT the state): Delta u - Delta d = {2-(-1):.1f}")
kk=np.argmin(abs(ev-(0.75-10))); psiA=B@vec[:,kk]
print(f"  the ANTIsymmetric J=1/2 state would give g_A = {psiA@(2*Sz(psiA,0))+psiA@(2*Sz(psiA,1))-psiA@(2*Sz(psiA,2)):+.4f} -- excluded by colour x Pauli")
print("\n"+"="*78); print("PART B1 -- Dirac quark in a cavity: one spinor, g_A AND mu_p"); print("="*78)
def state(m,R):
    F=lambda k: jn(0,k*R)-k/(np.sqrt(k*k+(m/hc)**2)+m/hc)*jn(1,k*R)
    ks=np.linspace(0.05,3.5/R,4000); v=[F(k) for k in ks]
    for i in range(len(ks)-1):
        if v[i]*v[i+1]<0: k=brentq(F,ks[i],ks[i+1]); break
    E=np.sqrt(k*k+(m/hc)**2); a=k/(E+m/hc)
    f=lambda r: jn(0,k*r); g=lambda r: a*jn(1,k*r)
    Nf=quad(lambda r:f(r)**2*r*r,0,R)[0]; Ng=quad(lambda r:g(r)**2*r*r,0,R)[0]; I3=quad(lambda r:f(r)*g(r)*r**3,0,R)[0]
    N=Nf+Ng; return k*R, Ng/N, (Nf-Ng/3)/N, (2/3)*I3/N
x,w,RA,mu1=state(1e-6,1.0)
print(f"calibration, massless: x = {x:.4f} (2.0428), R = {RA:.4f} (0.653), mu/R = {mu1:.4f} = closed form {(4*x-3)/(12*x*(x-1)):.4f}")
def obs(m,R):
    x,w,RA,mu1=state(m,R); return 5/3*RA, mu1/muN, w
print(f"m = m_p/3 = {mq:.2f} MeV:")
for R in [0.589,0.620,0.631,0.883,1.071,1.5]:
    gA,mup,w=obs(mq,R); print(f"  R_c = {R:5.3f} fm   g_A = {gA:.4f}   mu_p = {mup:.3f}   w = {w:.3f}")
Rg=brentq(lambda R: obs(mq,R)[0]-gA_t,0.3,3.0); gA,mup,w=obs(mq,Rg)
print(f"  g_A = 1.2754 requires R_c = {Rg:.3f} fm (w = {w:.4f}); there mu_p = {mup:.3f} vs 2.793 ({100*(mup/mup_t-1):+.0f}%)")
print(f"  mu_p never reaches 2.793 for R_c < 3 fm: mu_p(3.0 fm) = {obs(mq,3.0)[1]:.3f}, where g_A = {obs(mq,3.0)[0]:.3f}")
print("  -> FAMILY B1 EXCLUDED: the lower-component reduction that gives R shrinks the moment to the cavity scale.")
print("\n"+"="*78); print("PART B2 -- spin-orbit sharing at the constituent scale"); print("="*78)
R=gA_t/(5/3); f=(1+R)/2
print(f"R = {R:.4f}; moment factor (1+R)/2 = {f:.4f}")
print(f"  mu_p = 3.000 x {f:.4f} = {3*f:.3f} vs 2.793 ({100*(3*f/mup_t-1):+.1f}%);  mu_n = -2.000 x {f:.4f} = {-2*f:.3f} vs -1.913 ({100*(-2*f/mun_t-1):+.1f}%)")
print(f"  (4126 at R = 1: mu_p +7.4%, mu_n +4.5%.)  ratio mu_p/mu_n unchanged at -1.500.")
print("  -> FAMILY B2 SURVIVES at the naive model's own precision; it neither confirms nor fixes R.")
print("\n"+"="*78); print("PART C -- B2 read as a moving Dirac quark: R = 1 - (2/3)(1 - m/E)"); print("="*78)
mE=1-1.5*(1-R); kreq=mq*np.sqrt(1/mE**2-1)
print(f"R = {R:.4f} requires m/E = {mE:.4f}, k = {kreq:.1f} MeV = {kreq/mq:.3f} m_const, hbar c/k = {hc/kreq:.3f} fm")
for name,k in [("hbar c / l_unit  (Lambda = 335, SS-2)",hc/0.589),("hbar c / r_ZBW   (= m_const)",mq),("hbar c / (u-d 0.620 fm)",hc/0.620),("hbar c / (u-u 1.071 fm)",hc/1.071)]:
    E=np.hypot(k,mq); Rk=1-(2/3)*(1-mq/E); print(f"  k = {name:40s} = {k:6.1f} MeV:  R = {Rk:.4f}  g_A = {5/3*Rk:.4f} ({100*(5/3*Rk/gA_t-1):+.1f}%)")
print("  -> single-|k| estimates at the three ~0.6-fm corpus scales give g_A 1.31-1.34 (+3.0 to +5.2%); at the u-u scale 1.51.")
print("     None is a derivation: R needs the momentum DISTRIBUTION of the quark's motion in the cage, not one scale.")
print("\n"+"="*78); print("PART C2 -- the corpus statement of quark motion in the cage found by search (4240 s1): SS-2 ZBW smearing at r_ZBW"); print("="*78)
for name,k in [("p = hbar/r_ZBW        (= m_const c)",mq),("p = (hbar/2)/r_ZBW    (L = hbar/2 at r_ZBW)",mq/2)]:
    E=np.hypot(k,mq); Rk=1-(2/3)*(1-mq/E); print(f"  {name:44s} k = {k:6.1f} MeV:  R = {Rk:.4f}  g_A = {5/3*Rk:.4f} ({100*(5/3*Rk/gA_t-1):+.1f}%)")
print("  -> which row applies, and whether the smearing motion is the CORE's (so it can rotate the spin axis the vertex sees)")
print("     or is the spin circulation itself (so it cannot rotate its own axis), is a picture question: TODO-4240-CORE-MOTION.")
