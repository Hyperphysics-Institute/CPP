#!/usr/bin/env python3
"""
Patch 1824 -- pinning v_thr via Thomas's force-balance: delta* = where E_qq attraction = E_ee repulsion.
=======================================================================================================
1823 left v_thr bracketed (1700-3900) by the coat-thickness ratio delta/d, with the central guess delta/d~0.5
giving v_thr~2500 -> typical-cluster tension. Thomas reframed delta: it is NOT a fixed coat thickness but the
CROSSOVER DISTANCE at which the two cores' E_qq color attraction equals the eDP-coat E_ee repulsion. Beyond
that distance (closer), color wins and binding proceeds uninhibited. So delta* is set by a force balance, and
it is computable.

THE BALANCE. Color is CONFINED: E_qq(r) ~ alpha_s*hbarc/r inside the color range R_color, screened to ~0 beyond.
At contact r=d, E_qq = alpha_s*hbarc/d = 66 MeV -- which OVERWHELMS E_ee = 0.9 MeV by ~73x. So inside the color
range the attraction dominates the repulsion overwhelmingly; outside it, color is off. The crossover delta*
therefore sits at the COLOR-RANGE EDGE: where confined color switches on and instantly beats E_ee. R_color ~ d
(the color-bond length in the rod itself, E_qq = alpha_s*hbarc/d). => delta*/d ~ R_color/d ~ 0.8-1.0 (R_color~1
fm, d~1.0-1.3 fm) -- the natural fm/element scale, NOT the 0.5 I had guessed.
"""
import numpy as np
c=299792.458; hbarc=197.33; phi=(1+np.sqrt(5))/2; als=5/(8*phi)
E_ee,E_qq,m_el=0.9,66.0,1408.0; v_sound=np.sqrt(E_qq/m_el)
def pf(v,vt): return float(np.sqrt(np.clip(1-(vt/v)**2,0,1))) if v>vt else 0.0

print("="*72); print("delta* = color-range crossover (Thomas force balance) -> v_thr at the LOW end"); print("="*72)
print(f"  E_qq(d) = als*hbarc/d = {als*hbarc/1.15:.0f} MeV  >>  E_ee = {E_ee} MeV  (ratio ~{E_qq/E_ee:.0f}x)")
print(f"  confined color switches on at R_color ~ d and instantly dominates E_ee -> delta*/d ~ 0.8-1.0\n")
print(f"  v_thr = 2 E_ee/(v_sound (delta*/d) m_el):")
for dd in (1.2,1.0,0.8):
    print(f"    delta*/d={dd:.1f} -> v_thr = {2*E_ee/(v_sound*dd*m_el)*c:6.0f} km/s")
print(f"  => v_thr ~ 1500-2200 km/s (central ~1770), the LOW end of the 1822 band.\n")

print("  Tension relief -- sigma/m at TYPICAL cluster (2000 km/s), v_thr=1770 (p_fuse=0.47):")
print(f"  {'N':>3} {'sigma/m_0':>9} | {'flex(1/8)':>9} {'rigid(1/2)':>10} | cluster bound <~1")
for N in (10,15,20):
    som0=0.11*N; r=som0*(1-pf(2000,1770)*0.5); f=som0*(1-pf(2000,1770)*0.875)
    tag='OK' if r<1.0 else ('OK(flex)/marg(rigid)' if f<1.0 else 'TENSION')
    print(f"  {N:>3} {som0:>9.1f} | {f:>9.2f} {r:>10.2f} | {tag}")
print()
print("="*72)
print("RESULT: the force balance pins delta*/d ~ 1 (the color range = the fm/element scale), dropping")
print("v_thr to ~1770 km/s -- the LOW end. Typical clusters (~2000) now sit ABOVE threshold and ARE")
print("suppressed. Tension RELIEVED for N <~ 15 (comfortably N~10, marginally N~15); N~20 still mildly")
print("over the cluster bound, to be closed by the velocity-distribution convolution (high-v tail) and")
print("multiple-fusion compounding. This is a PINNING (physical color-range argument), not a tuning.")
print("Refines 1823's central curve (v_thr 2500 -> 1770).")
print("="*72)
