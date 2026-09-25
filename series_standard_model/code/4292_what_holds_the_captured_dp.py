#!/usr/bin/env python3
"""4292 -- founders_voice/4292: compute what works.
(A) Target. Default: the three CPs (core -eCP, inner +eCP, outer -eCP) carry equal moving inertia m_c (CPs identical
    but for charge), and binding is negligible at these speeds, so m_c = m_e/3.  Then mu = (e/2m_c) sum s_i L_i with
    s = +1 for each -eCP (moment antiparallel to its L) and -1 for the +eCP, and mu = g (e/2m_e) S gives
        g = 3 (1 - 2 f),   f = L_inner / S  (about the centre of mass).       g = 2  <=>  f = 1/6.
(B) Rose realisation (4291, static core, sinusoidal swing): g = m_e(1 - x/2)/(m_o + m_i x/2), x = W/w_o.
(C) Does Coulomb dynamics among the three point CPs hold the pair?  Planar, softened 1/r (pass-through, eps = 0.02),
    unit charges and inertias, centre-of-mass frame."""
import numpy as np, itertools
from scipy.integrate import solve_ivp
print("(A) g = 3(1 - 2f):", "  ".join(f"f={f:.4f}->g={3*(1-2*f):.3f}" for f in (0,1/6,0.25,0.5)))
print("    g = 2 needs the inner +eCP to carry exactly 1/6 of the electron's spin; the two -eCPs carry 5/6.")
x=0.4; mo=mi=1/3
print(f"(B) static core, m_o = m_i = m_e/3: g = 3(1-x/2)/(1+x/2);  g = 2 at x = {x}:  g = {(1-x/2)/(mo+mi*x/2):.4f},"
      f"  f = (x/2)/(1+x/2) = {(x/2)/(1+x/2):.4f}")
wr=1-x
print(f"    meeting the partner at each tip (W = w_o - w_r): w_r = {wr:.1f} w_o -> {2*wr:.1f} touches per outer revolution"
      f" (6 touches per 5 circuits)")
q=np.array([-1.,+1.,-1.]); eps=0.02; P=[(0,1),(0,2),(1,2)]
def rhs(t,y):
    X=y[:6].reshape(3,2); a=np.zeros((3,2))
    for i,j in P:
        d=X[i]-X[j]; f=q[i]*q[j]*d/(d@d+eps*eps)**1.5; a[i]+=f; a[j]-=f
    return np.concatenate([y[6:],a.ravel()])
def energy(X,V):
    E=0.5*(V*V).sum()
    for i,j in P: d=X[i]-X[j]; E+=q[i]*q[j]/np.sqrt(d@d+eps*eps)
    return E
def go(X,V,T=60):
    X=X-X.mean(0); V=V-V.mean(0); E=energy(X,V)
    s=solve_ivp(rhs,(0,T),np.concatenate([X.ravel(),V.ravel()]),method='DOP853',rtol=1e-8,atol=1e-10,t_eval=np.linspace(0,T,601))
    Y=s.y[:6].reshape(3,2,-1); d=[np.hypot(*(Y[i]-Y[j])) for i,j in P]
    return E,[di[-1] for di in d],[di.max() for di in d]
print("(C) founder-type starts: core at 0, inner at a between, outer at 1; inner velocity (vr, vt), outer vo; E < 0 only")
n=br=0; pat={}
for a,vr,vt,vo in itertools.product((0.3,0.5,0.7),(-1.0,-0.5,0.0),(0.2,0.6),(0.2,0.5,0.8)):
    X=np.array([[0,0],[a,0],[1,0]],float); V=np.array([[0,0],[vr,vt],[0,vo]],float)
    E,df,dm=go(X,V)
    if E>=0: continue
    n+=1
    if max(dm)>6:
        br+=1; k="inner stays with outer" if df[2]<df[0] else "inner stays with core"; pat[k]=pat.get(k,0)+1
print(f"    {n} bound-energy starts: {br} break up within t = 60 into a neutral (+,-) pair and a free -eCP  {pat}")
print("    Euler line (-,+,-) rotating rigidly at d = 0.5, +e in the middle, nudged by delta:")
for delta in (0.0,1e-4,1e-2):
    dd=0.5; vv=np.sqrt(3/(4*dd))
    E,df,dm=go(np.array([[-dd,0],[0,delta],[dd,0]],float),np.array([[0,-vv],[0,0],[0,vv]],float),T=80)
    print(f"      delta = {delta:.0e}: largest separation {max(dm):7.2f}  ({'holds' if max(dm)<3 else 'breaks up'})")
print("    -> Coulomb forces between the three point CPs do not hold the captured pair: no rate or outer shape is")
print("       selected by them, because no bound orbit survives.")
