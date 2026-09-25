#!/usr/bin/env python3
"""4296 -- founders_voice/4296: the +eCP is turned back past a pole by the pull of the pole it just passed.  With inertia,
energy conservation then fixes the overshoot.  Fixed poles at +-d (units d = 1, k e^2 = 1, +eCP inertia 1):
U(x) = -1/|x-1| - 1/|x+1|;  the shuttle crosses the centre only if E > U(0) = -2;  E = -2 + delta.
(A) overshoot, time-weighted spin share and g, inward pull on a pole (principal value; checked by an adaptive-impulse ODE
at delta = 0.1: 0.3149, matching).  (B) size from balance with hbar/2 (equal inertias).  (C) full planar 3-body tests."""
import numpy as np, warnings
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
warnings.filterwarnings("ignore")
alpha=1/137.035999
def turn(e): return brentq(lambda s: 1/s+1/(2+s)-e, 1e-12, 1e6)
def avgs(delta):
    e=2-delta; X=1+turn(e); v=lambda x: np.sqrt(max(2*(-e+1/abs(x-1)+1/abs(x+1)),1e-300))
    T=quad(lambda x:1/v(x),0,1,limit=500)[0]+quad(lambda x:1/v(x),1,X,limit=500)[0]
    R2=(quad(lambda x:x*x/v(x),0,1,limit=500)[0]+quad(lambda x:x*x/v(x),1,X,limit=500)[0])/T
    g_=lambda x:(1/v(x))*(-np.sign(x-1)/(x-1)**2); U=min(X-1,1.0)
    pv=quad(lambda u:g_(1+u)+g_(1-u),1e-12,U,limit=800)[0]; rest=quad(g_,-X,1-U,limit=800,points=[-1])[0]
    if X-1>U: rest+=quad(g_,1+U,X,limit=400)[0]
    return X-1,R2,(pv+rest)/(2*T),T
print(f"(A) threshold overshoot: 1/s + 1/(2+s) = 2  ->  s = (sqrt5 - 1)/2 d = {(np.sqrt(5)-1)/2:.5f} d (the golden ratio)")
for dl in (1e-1,1e-3,7.37e-5,1e-6,1e-10):
    s,R2,F,T=avgs(dl); f=R2/(2+R2)
    print(f"  delta {dl:8.2e}: overshoot {s:.4f} d  <r^2> {R2:.4f} d^2  g {3*(1-2*f):.4f}  inward pull {F:.4f}, net of push {F-0.25:+.4f}")
print("  -> g passes 2 only at delta = 7.4e-5 (the energy 0.004% above the crossing threshold); g is logarithmic in delta.")
print("(B) balance with hbar/2, equal inertias m = m_e/3:")
m=1/3
for dl in (1e-3,7.37e-5):
    s,R2,F,T=avgs(dl); K=F-0.25; Q=2+R2; d=0.25/(alpha*K*m*Q*Q); w=0.5/(m*d*d*Q)
    ratio=(2*np.pi/(4*T*np.sqrt(m*d**3/alpha)))/w
    print(f"  delta {dl:.2e}: half-length {d:.1f} r_C, poles {w*d:.4f} c, shuttle frequency / rotation frequency = {ratio:.2f}")
print("  -> at g = 2 the shuttle is SLOWER than the spin (0.7): the fixed-pole picture fails there.")
print("(C) full planar three-body rod (softened pass-through, eps = 5e-3), poles given their balance speed, +eCP at the centre:")
q=np.array([-1.,+1.,-1.]); P=[(0,1),(0,2),(1,2)]
def rod(mu,delta,K,T=40,eps=5e-3):
    mm=np.array([1.0,mu,1.0])
    def rhs(t,y):
        X=y[:6].reshape(3,2); a=np.zeros((3,2))
        for i,j in P:
            d=X[i]-X[j]; f=q[i]*q[j]*d/(d@d+eps*eps)**1.5; a[i]+=f/mm[i]; a[j]-=f/mm[j]
        return np.concatenate([y[6:],a.ravel()])
    w=np.sqrt(K); X=np.array([[-1,0],[0,0],[1,0]],float); V=np.array([[0,-w],[np.sqrt(2*delta/mu),0],[0,w]],float)
    s=solve_ivp(rhs,(0,T),np.concatenate([X.ravel(),V.ravel()]),method='DOP853',rtol=1e-9,atol=1e-11,t_eval=np.linspace(0,T,401))
    Y=s.y[:6].reshape(3,2,-1); return np.hypot(*(Y[0]-Y[2])).max(), w*s.t[-1]/(2*np.pi)
for mu,dl,K,lab in ((1.0,7.37e-5,0.4628,"equal inertia, g = 2 energy"),(0.01,1e-1,0.0649,"+eCP 1/100 of a pole, robust crossing")):
    mx,rot=rod(mu,dl,K)
    print(f"  {lab:40s}: over {rot:.1f} rotations, pole separation reaches {mx:.1f} d  ({'holds' if mx<3 else 'breaks up'})")
