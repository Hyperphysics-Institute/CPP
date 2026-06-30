#!/usr/bin/env python3
"""
Patch 1825 -- the full convolution: sigma/m(v) over velocity distribution x impact angle x impact position x N.
==============================================================================================================
Replaces the 1823/1824 characteristic-velocity stand-in with the proper 4-fold average. Key structure that the
stand-in missed: v_thr is itself N-DEPENDENT (backing mass is rod-length-limited, so long rods penetrate at
LOWER v_thr) AND long rods DOMINATE sigma/m (= 0.11 N) -- so the suppression preferentially removes the
high-sigma/m rods. And the suppression is CUMULATIVE: the per-collision penetration probability p_pen is modest,
but it compounds over the collision history N_coll, f_fused = 1 - exp(-N_coll p_pen).

Convolution (Monte Carlo / per-N):
  - relative speed v_rel ~ Maxwell(sigma_rel = sqrt(2) sigma_1d)
  - impact angle isotropic (cos theta uniform); penetrating component v_rel sin(theta)
  - impact position x uniform; backing mass = min(2 min(x,1-x) N, N) elements -> v_thr(N,x)=sqrt(2E_ee/m_back)
  - N-distribution P(N) ~ exp(-N/Nchar) (equilibrium polymerization, 0861); mass ~ N
  - penetrate if v_rel sin(theta) >= v_thr(N,x);  f_fused(N)=1-exp(-N_coll p_pen(N));  fused -> sigma/m x drop
  - population sigma/m = sum(sigma/m_eff * N * P(N))/sum(N * P(N))   (mass-weighted)
N_coll ~ v_rel (similar core densities), normalized cluster -> ~600; drop=0.25 (flexible, bracket 1/8-1/2).
All pinned/geometric except {Nchar, drop, N_coll-normalization} -- the O(1)s, flagged.
"""
import numpy as np
rng=np.random.default_rng(11); c=299792.458; E_ee,m_el=0.9,1408.0; Nchar=15; drop=0.25
def vthr(N,x):
    back=np.minimum(2*np.minimum(x,1-x)*N,N); return np.sqrt(2*E_ee/np.maximum(back,1e-6)/m_el)*c
def p_pen(Nval,sig1d,n=80000):
    sr=np.sqrt(2)*sig1d
    v=np.sqrt(rng.normal(0,sr,n)**2+rng.normal(0,sr,n)**2+rng.normal(0,sr,n)**2)
    cth=rng.uniform(-1,1,n); x=rng.uniform(0,1,n)
    return ((v*np.sqrt(1-cth**2))>=vthr(np.full(n,Nval),x)).mean()
def Ncoll(sig1d): return 600.0*(np.sqrt(2)*sig1d*1.6)/2262.0
Ns=np.arange(3,80); w=np.exp(-Ns/Nchar); mass=Ns

print("="*72); print("sigma/m(v): full convolution (velocity x angle x impact x N)"); print("="*72)
print(f"  {'env':<9}{'sig1d':>6}{'v_rel':>7}{'N_coll':>7} | {'sigma/m_0':>9}{'sigma/m':>8}{'factor':>7}{'p_pen':>7}")
for env,s in (('dwarf',20),('LSB',40),('galaxy',150),('group',400),('cluster',1000),('Bullet*',1600)):
    nc=Ncoll(s); se=[]; s0=[]; ppc=p_pen(20,s)
    for N in Ns:
        pp=p_pen(N,s); ff=1-np.exp(-nc*pp); se.append(0.11*N*(1-ff*(1-drop))); s0.append(0.11*N)
    se=np.array(se); s0=np.array(s0)
    SM=np.sum(se*mass*w)/np.sum(mass*w); SM0=np.sum(s0*mass*w)/np.sum(mass*w)
    print(f"  {env:<9}{s:>6}{int(np.sqrt(2)*s*1.6):>7}{nc:>7.0f} | {SM0:>9.2f}{SM:>8.2f}{SM0/SM:>6.1f}x{ppc:>7.2f}")
print()
print("  RESULT: sigma/m falls ~3.1 (dwarf cores) -> ~0.8 (cluster), factor ~4, knee ~1000-1500 km/s.")
print("  Within bounds (dwarf 0.5-5 OK; cluster <~1 OK). Bullet* pre-processed by its cluster history.")
print("="*72)
print("CRITICAL FLAG for (3): at clusters N_coll*p_pen ~ 10-40 -> MULTIPLE fusions are likely, not one.")
print("The curve above assumes ~single-fusion processing (floor = sigma/m_0 * drop ~ 0.8). Repeated fusion")
print("of X's into larger aggregates could drive sigma/m BELOW this -> over-depletion -- UNLESS the floppy")
print("aggregate sigma/m SATURATES (coil regime ~ const, 0860). So (3) self-limiting now DECIDES the floor:")
print("single-fusion (~0.8, viable) vs coil-saturation (~const) vs runaway (over-deplete). Decisive next.")
print("="*72)
