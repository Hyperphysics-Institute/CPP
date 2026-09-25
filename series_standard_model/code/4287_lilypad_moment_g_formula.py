#!/usr/bin/env python3
"""4287 -- the founder's electron magnet (founders_voice/4287): outer -eCP on a circle, inner +eCP on a lily-pad
pass-through of the core, B = the difference.  Far field per SF-6 l.319 (moving charge -> rotational sea polarization,
Maxwell limit): each CP's moment is (q/2)<r x v>.  |r x v| = v * b, b = distance from the core to the CP's line of motion.
  mu / mu_B = [ <v b>_outer - <v b>_inner ] / (c r_ZBW),   mu_B = e hbar/2m = (e c/2) r_ZBW   (same circulation sense)
Units m = c = hbar = 1 (lengths r_ZBW, energies mc^2)."""
import numpy as np
from scipy.integrate import solve_ivp

print("(1) direct check of mu = (q/2)<r x v> = (q c/2)<b> on an integrated lily-pad (massless pole, H = |p|c + V):")
def run(V_grad, r0, p0, T=400.0):
    def f(t,y):
        x,yy,px,py=y; p=np.hypot(px,py); gx,gy=V_grad(x,yy); return [px/p,py/p,-gx,-gy]
    s=solve_ivp(f,(0,T),[*r0,*p0],rtol=1e-10,atol=1e-12,dense_output=True,max_step=0.01)
    t=np.linspace(0,T,400001); x,y,px,py=s.sol(t); p=np.hypot(px,py)
    rxv=x*py/p-y*px/p; L=x*py-y*px
    return rxv.mean(), (L/p).mean(), L.std()/abs(L.mean()), np.hypot(x,y).min(), np.hypot(x,y).max()
s_=0.5  # linear well V = s r
g=lambda x,y:(s_*x/np.hypot(x,y), s_*y/np.hypot(x,y))
for Lin in (0.05,0.15,0.30):
    # start at r = 1 moving mostly radially inward with angular momentum Lin, |p| = 0.5 (E = 1 at r = 1)
    p0=0.5; pt=Lin/1.0; pr=-np.sqrt(p0**2-pt**2)
    a,b,dL,rmin,rmax=run(g,(1.0,0.0),(pr,pt))
    print(f"  inner L = {Lin:.2f} hbar:  <r x v>/c = {a:.5f}   <L/|p|> = <b> = {b:.5f}   (L conserved to {dL:.1e})"
          f"   closest {rmin:.4f}, farthest {rmax:.4f} r_ZBW")
print("  -> the two agree: a speed-c charge's magnet is (q c/2) x its mean distance b from the core to its line of motion.")
print("     A true pass-through (L = 0, b = 0) makes no magnet at all, however fast it moves.")

print("\n(2) SPIN-1's slow circles recast in this form (4286 rows F):")
vo,Ro,vi,ri=0.02491,2*5.878,0.03523,5.878
print(f"  outer v b = {vo*Ro:.4f},  inner v b = {vi*ri:.4f},  net = {vo*Ro-vi*ri:.4f} mu_B  -> g = {2*(vo*Ro-vi*ri):.4f}")
print("  Two failures, not one: the inner cancels 71% of the outer, AND the outer alone is only 0.29 mu_B (g 0.59).")

print("\n(3) any MASSIVE charge on a circle (mass m, L = m v R):  mu = (e/2) v R = (e/2m) L  ->  g = 1 exactly, at any R, v.")
print("    With the inner's opposite moment subtracted, g < 1.  No massive two-CP carrier reaches g = 2.")

print("\n(4) the founder's picture with massless poles at c (4281/SF-6 inertia):  g = 2 mu/mu_B = 2 (R - <b_in>)/r_ZBW")
for bi in (0.0,0.1,0.25,0.5):
    R=1+bi
    print(f"  inner lily-pad <b> = {bi:.2f} r_ZBW  ->  g = 2 needs the outer circle at R = {R:.2f} r_ZBW;"
          f"  outer's own L = hbar/2 - L_in, its motion energy = (hbar/2 - L_in) c / R")
print("  pure pass-through (<b> = 0): outer at R = r_ZBW carries all of hbar/2 with motion energy mc^2/2  -> g = 2 exactly.")
