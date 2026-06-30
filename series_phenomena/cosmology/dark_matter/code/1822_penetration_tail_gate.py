#!/usr/bin/env python3
"""
Patch 1822 -- the strip-then-fuse gate, RE-FOUNDED on the penetration tail (retracts 1821's persistence).
========================================================================================================
1821 rested the gate on "bare spots persist because the late Sea can't re-coat." Thomas corrected this:
the just-stripped eDPs are locally present and DO recombine -- persistence is false. RETRACT that framing.
The gate is re-founded on the right physics (Thomas): fusion vs recombination is decided at the instant of
collision by whether the impact drives the two cores through the mutual eDP coat into E_qq (color) range.
That is a PENETRATION question -- and 1816's v_pen ~ 1.1e4 km/s ("coat holds at all DM velocities") was too
coarse: it used the LOCAL PATCH mass (~1 element). For a perpendicular, central hit on a long rod, the
ROD-TAIL INERTIA backs the contact (Thomas: tails resist acceleration -> reaction force -> full KE pays into
penetration), and because the collision KE is held in the DP Sea (SF-6) the relative velocity is SUSTAINED
(no instantaneous rebound) so the stress wave recruits that backing during the penetration. With the right
backing mass the threshold drops into the CLUSTER BAND.

THRESHOLD (perpendicular, central, long rod):  (1/2) m_eff v_perp^2 = E_ee,  v_perp = v sin(theta).
Two backing-mass models (bracket the estimate); all inputs pinned/geometric (E_ee=0.9, E_qq=66, m_el=1408):
 (A) stress-wave recruitment m_eff=(v_sound/v_perp)(delta/d) m_el  (v_sound=sqrt(E_qq/m_el) c, E_qq core)
 (B) fixed rod-fraction       m_eff=f_back N m_el
"""
import numpy as np
c=299792.458; E_ee,E_qq,m_el=0.9,66.0,1408.0
v_sound=np.sqrt(E_qq/m_el)
print("="*72); print("Penetration threshold with ROD-TAIL backing (re-founds the gate)"); print("="*72)
print(f"  v_sound (E_qq core) = {v_sound*c:.0f} km/s")
print(f"  1816 LOCAL-patch v_pen = {np.sqrt(2*E_ee/m_el)*c:.0f} km/s  <- too coarse (1-element mass)\n")
print("  (A) stress-wave backing:  v_thr = 2 E_ee/(v_sound (delta/d) m_el)")
for dd in (1.0,0.7,0.5):
    print(f"      delta/d={dd:.1f} -> v_thr = {2*E_ee/(v_sound*dd*m_el)*c:6.0f} km/s")
print("  (B) fixed rod-fraction:   v_thr = sqrt(2 E_ee/(f_back N m_el))")
for N,fb in ((60,0.5),(30,0.5),(30,0.25),(15,0.5)):
    print(f"      N={N:>2} f_back={fb} -> v_thr = {np.sqrt(2*E_ee/(fb*N*m_el))*c:6.0f} km/s")
print(f"\n  => v_thr ~ 1700-3900 km/s (both models) -- IN THE CLUSTER BAND, far above dwarf (60).")

print("\n  Velocity dependence via perpendicularity acceptance (need v sin(theta) >= v_thr):")
print(f"  {'v_thr':>6} | " + " | ".join(f"v={v}" for v in (2000,3000,4000)))
for vthr in (1740,2770,3485):
    cells=[]
    for v in (2000,3000,4000):
        s=vthr/v
        cells.append(f"perp<={90-np.degrees(np.arcsin(s)):.0f}deg" if s<=1 else "  --  ")
    print(f"  {vthr:>6} | " + " | ".join(f"{x:>10}" for x in cells))
print("  (acceptance = half-angle around perpendicular that penetrates; WIDENS with v -> fusion frac up)")

print("\n" + "="*72)
print("VERDICT: GATE HOLDS, re-founded correctly. Rod-tail backing (+ SF-6 sustained velocity) drops the")
print("penetration threshold from ~1.1e4 km/s (1816 local) to ~1.7-3.9e3 km/s (cluster band) for")
print("perpendicular/central/long-rod hits. So the PENETRATING TAIL is real and populated at cluster")
print("velocities, OFF at dwarf -> strip-then-fuse fires in clusters only. Velocity dependence rides on")
print("BOTH clearing v_thr AND the widening perpendicularity acceptance -> fusion fraction rises with v")
print("-> sigma/m FALLS with v (right sign, threshold-like/steep). Three knobs, all pinned/geometric:")
print("velocity, perpendicularity (v sin theta), centrality+length (backing mass). REVISES 1816 (its")
print("'coat holds everywhere' is true on AVERAGE but misses the braced-perpendicular penetrating tail).")
print("="*72)
