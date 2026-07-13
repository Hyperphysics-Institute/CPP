#!/usr/bin/env python3
"""
PATCH 2446 -- OPEN-DM-FLOQUET-1 / distributed-collision energetics: bending-to-FORM a
loop vs bending-to-BREAK a loop equilibrium. Founder reframe (12 July): a real collision
(extended +/- collider: DM ring or baryon) delivers its KE across SEVERAL planes with a
min-max-min axial force envelope -- NOT a focused single-plane slip. So the failure
channel is DISTRIBUTED FLEXURE, and the question is how distributed the bend is.

Uses the 2443 finite-angle bond model (shared calibration): V(r)=-A_eff/r+K/r^2,
A_eff=(1-2 delta) alpha_s hc, delta=3/7, d=1.15 fm; bond at lever x has L=d+2x sin(theta/2).
Cross-section: 4 core (r_q=d/sqrt2) + 4 coat (R_e=1.6 r_q). N_planes=16 -> ring angle
theta_ring = 2pi/16 = 22.5 deg/hinge.

Computes: U(theta) per hinge, the fragmentation angle theta_frag (outer bond reaches its
inflection r=1.5d -> dissociating), E_form (bend 16 hinges to ring angle), and E_break(l)
(distributed blow, raised-cosine hinge-angle bump over l hinges, energy to drive peak
hinge to theta_frag). Compares to a 0.49-1 MeV collision quantum.

Absolute energies are Layer-C (scale with the true bond depth, 2444); the ROBUST outputs
are the ORDERING (form >> break >> elastic blow) and the PROTECTIVE l-scaling of E_break.
"""
import numpy as np
AHC=197.3; PHI=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI); DELTA=3/7
d=1.15; r_q=d/np.sqrt(2); R_e=1.6*r_q; NPL=16; th_ring=2*np.pi/NPL
A_eff=(1-2*DELTA)*ALPHA_S*AHC; K=A_eff*d/2
def V(r): return -A_eff/r+K/r**2
depth=-V(d); 
# coat: 10% depth (2443 convention), same shape
def Vcoat(r): return (V(r))*0.10
depth_coat=depth*0.10
d_infl=3*K/A_eff   # inflection radius (V''=0): 1.5 d
print("="*76); print("DISTRIBUTED-COLLISION ENERGETICS -- form vs break a loop"); print("="*76)
print(f"d={d} r_q={r_q:.3f} R_e={R_e:.3f}  theta_ring=2pi/16={np.degrees(th_ring):.1f}deg")
print(f"core depth={depth*1000:.0f}keV (Layer-C shape) coat depth={depth_coat*1000:.0f}keV")
print(f"inflection radius d_infl=1.5d={d_infl:.3f} fm (bond dissociates past here)")
print()
# per-hinge bend energy U(theta) and max outer-bond stretch fraction
xs_core=r_q*np.cos(np.radians(45)+np.array([0,np.pi/2,np.pi,3*np.pi/2]))
xs_coat=R_e*np.cos(np.radians(45)+np.array([0,np.pi/2,np.pi,3*np.pi/2]))
def U_of(theta):
    s=np.sin(theta/2); U=0.0
    for x in xs_core: U+=V(d+2*x*s)-V(d)
    for x in xs_coat: U+=Vcoat(d+2*x*s)-Vcoat(d)
    return U
def outer_coat_L(theta):
    s=np.sin(theta/2); return d+2*max(xs_coat)*s   # most-stretched coat bond
# fragmentation angle: outer coat bond reaches inflection (starts dissociating)
from scipy.optimize import brentq
th_frag=brentq(lambda th: outer_coat_L(th)-d_infl, 0.01, np.pi)
print(f"theta_frag (outer coat bond hits inflection) = {np.degrees(th_frag):.1f} deg")
print(f"  ring-closure angle {np.degrees(th_ring):.1f} deg vs frag {np.degrees(th_frag):.1f} deg "
      f"-> margin x{th_frag/th_ring:.2f} (ring closure stays BELOW fragmentation)")
U_ring=U_of(th_ring); U_frag=U_of(th_frag)
print(f"  U(ring)={U_ring*1000:.0f} keV/hinge   U(frag)={U_frag*1000:.0f} keV/hinge")
print()
# E_form: bend all 16 hinges to ring angle (elastic, no fragmentation)
E_form=NPL*U_ring
print("="*76); print("(A) BENDING TO FORM A LOOP"); print("="*76)
print(f"  E_form = 16 * U(theta_ring) = {E_form:.2f} MeV  (all 16 hinges to 22.5deg)")
print(f"  every hinge at {np.degrees(th_ring):.1f}deg < theta_frag {np.degrees(th_frag):.1f}deg "
      f"-> ELASTIC: the rod curls into a loop WITHOUT fragmenting. Ends then bond.")
print(f"  (requires the bend delivered COHERENTLY over ~the whole rod, e.g. galactic")
print(f"   collision / primordial turbulence spanning the rod length.)")
print()
# E_break(l): distributed blow, raised-cosine hinge-angle bump over l hinges, peak->frag
print("="*76); print("(B) BENDING TO BREAK A LOOP (distributed collision)"); print("="*76)
print("  collider delivers E_coll across l hinges with a min-max-min (raised-cosine) bump.")
print("  hinge fragments only where local angle reaches theta_frag. E_break(l) = total")
print("  energy when the PEAK hinge hits theta_frag.")
print(f"  {'l (planes)':>11} {'E_break[MeV]':>13} {'vs 1 MeV blow':>15}")
def E_break(l):
    # raised-cosine hinge-angle profile, peak=theta_frag, over l hinges
    idx=np.arange(l)
    prof=0.5*(1-np.cos(2*np.pi*(idx+0.5)/l)) if l>1 else np.array([1.0])
    prof=prof/prof.max()                 # peak=1
    thetas=th_frag*prof
    return sum(U_of(t) for t in thetas)
for l in [1,2,4,8,16]:
    Eb=E_break(l); ratio=Eb/1.0
    print(f"  {l:>11} {Eb:>13.2f} {'x'+format(ratio,'.1f'):>15}")
print()
# focused-blow sanity: what angle does a 0.49 / 1 MeV FOCUSED blow reach on one hinge?
print("  focused-blow check (all energy on ONE hinge -- the worst case):")
for Ec in [0.49,1.0,2.0]:
    th=brentq(lambda t: U_of(t)-Ec, 1e-3, np.pi) if U_of(np.pi)>Ec else np.pi
    tag="ELASTIC (no frag)" if th<th_frag else "FRAGMENTS"
    print(f"    E_coll={Ec:.2f} MeV focused -> one hinge to {np.degrees(th):.1f}deg -> {tag}")
print()
print("="*76); print("HIERARCHY & READ (G7)"); print("="*76)
print(f"  elastic blow (survives)   : E_coll <~ U(frag) focused ~ {U_frag:.2f} MeV  (0.49-1 MeV lands here)")
print(f"  fragment one hinge (break): focused >~ {U_frag:.2f} MeV; DISTRIBUTED needs x l more (protective)")
print(f"  form a loop               : coherent ~ E_form = {E_form:.1f} MeV over the rod")
print(f"  => ORDERING form({E_form:.0f}) >> break({U_frag:.1f}+) >> collision quantum(0.49-1). A 0.49-1 MeV")
print(f"     blow bends a hinge to <={np.degrees(brentq(lambda t:U_of(t)-1.0,1e-3,np.pi)):.0f}deg (<frag {np.degrees(th_frag):.0f}deg) even FULLY FOCUSED -> loop survives.")
print(f"     Distribution over l planes raises E_break ~x l -> extra protection, as founder argued.")
print()
print("  CAVEATS: absolute MeV are Layer-C (scale with true bond depth, 2444); robust")
print("  claims are the ORDERING and the l-scaling. Ring-closure margin to fragmentation")
print(f"  is only x{th_frag/th_ring:.1f} (22.5 vs {np.degrees(th_frag):.0f}deg) -- positive but not large. Formation")
print("  requires a COHERENT rod-spanning bend (collision geometry), not just total energy.")
print("  Candidate (B): UNRESOLVED; this supports FLEXURE as the physical collision channel")
print("  and retires transverse plane-slip as non-physical -- input to CONV-001, not a promotion.")
