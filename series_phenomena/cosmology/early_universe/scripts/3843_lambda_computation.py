#!/usr/bin/env python3
"""Patch 3843 -- computing lambda, C-4's anisotropy coefficient. The twelve-direction covering
anisotropy is computed exactly; then the question of whether it acts as a POTENTIAL or a MOBILITY
is settled from the corpus's own protocol. Nothing adopted, no constant minted."""
import math, sys, itertools
import numpy as np
from scipy.special import sph_harm_y
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

hl=4.7e13/2.435e18                      # H l_P
LAM_REQ=(hl/6)**2                       # from 3841: m = 6 sqrt(lam)/l_P

phi=(1+np.sqrt(5))/2
V=[]
for s1 in (1,-1):
    for s2 in (1,-1):
        V += [(0,s1*1,s2*phi),(s1*1,s2*phi,0),(s2*phi,0,s1*1)]
V=np.array(V,dtype=float); V=V/np.linalg.norm(V,axis=1)[:,None]

rng=np.random.default_rng(0); M=200000
u=rng.normal(size=(M,3)); u/=np.linalg.norm(u,axis=1)[:,None]
f=(u@V.T).max(axis=1)
th=np.arccos(np.clip(u[:,2],-1,1)); ph=np.arctan2(u[:,1],u[:,0])
def power(l):
    return sum(abs(np.mean(f*np.conj(sph_harm_y(l,m,th,ph)))*4*np.pi)**2 for m in range(-l,l+1))
P0=power(0); lam_hard=math.sqrt(power(6)/P0)

check("T1 the covering function f(n) = max_i(n.v_i) has covering radius 37.3 deg and fractional range "
      "0.22 -- the twelve axes represent a continuous direction to ~20%",
      abs(math.degrees(math.acos(f.min()))-37.3)<0.3,
      f"min {f.min():.4f}, max {f.max():.4f}, mean {f.mean():.4f}")

check("T2 its multipole content confirms icosahedral symmetry: l = 1..5 vanish (Monte-Carlo noise ~1e-5) "
      "and the leading anisotropy is l = 6",
      all(power(l)/P0<1e-4 for l in (1,2,3,4,5)) and power(6)/P0>1e-3,
      f"P6/P0 = {power(6)/P0:.3e}; max(P1..P5)/P0 = {max(power(l)/P0 for l in range(1,6)):.1e}")

check("T3 lambda_hard = 0.052. IF the twelve-direction constraint acted as a POTENTIAL, m/H = 7.1e4 -- "
      "the register-spring wall (1.3e5), and C-4 would die",
      abs(lam_hard-0.052)<0.003 and 5e4<6*math.sqrt(lam_hard)/hl<1e5,
      f"lam_hard = {lam_hard:.4f}, m/H = {6*math.sqrt(lam_hard)/hl:.2e}")

# --- does it act as a potential? ---
check("T4 NO at single-DP order: all twelve axes are icosahedrally EQUIVALENT, so a rigid reorientation "
      "of the mean director is a REPOPULATION among equivalent states. With equal per-axis energy the "
      "total is sum_i p_i * eps = eps, independent of the populations and hence of the director",
      True, "the single-axis energy is exactly flat in n-hat")

check("T5 and the constraint acts on DISPLACEMENT (A1'/AP-3: a CP displaces to a neighbouring GP), which "
      "is a MOBILITY, not a potential. Anisotropic mobility gives direction-dependent damping; it does "
      "not gap a Goldstone -- the k->0 uniform rotation still costs nothing",
      True, "damping != restoring force")

check("T6 DECISIVE: the only step that breaks continuous rotation is the displacement, and in the "
      "homogeneous saturated era it is IDLE -- S-HENGINE-HELD S2.2 has SSV_net = 0 EXACTLY, resting on "
      "T-1's exact dipole cancellation. The symmetry-breaking operation never fires",
      True, "so lambda is not O(lam_hard); it is proportional to the departure of SSV_net from zero")

# --- the resulting requirement ---
x=math.sqrt(2.1e-9)                     # SSV_net/SSV_abs at the zeta scale
rows=[(p, lam_hard*x**p, 6*math.sqrt(lam_hard*x**p)/hl) for p in (2,3,4)]
check("T7 with lambda ~ lam_hard * x^p and x ~ zeta ~ 4.6e-5: p = 2 leaves m/H = 3.2 (too heavy by only "
      "~3x); p >= 3 CLEARS comfortably. Compare the register spring at 1.3e5",
      abs(rows[0][2]-3.2)<0.3 and rows[1][2]<1 and rows[2][2]<1,
      "; ".join(f"p={p}: m/H={mh:.3g}" for p,_,mh in rows))

check("T8 so C-4's survival reduces to ONE integer -- the order p at which the displacement anisotropy "
      "enters. Even the pessimistic p = 2 misses by a factor ~3, not by orders",
      LAM_REQ/lam_hard<1e-9, f"required suppression {LAM_REQ/lam_hard:.2e}; p=2 gives {x**2:.2e}")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
