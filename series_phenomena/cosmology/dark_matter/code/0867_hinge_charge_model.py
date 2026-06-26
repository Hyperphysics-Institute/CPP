#!/usr/bin/env python3
"""
Patch 0867 (G1 CONFRONTATION -- explicit point-charge hinge model: kappa_full = kappa_bare
- kappa_screen, the buckling failure mode, and why G1 is genuinely the make-or-break)
=========================================================================================
G1: the angular spring kappa_theta of the rung-rung hinge must land l_p in [100,700] fm,
i.e. kappa_theta/kT_form in [100,700] (l_p/l_rung = kappa_theta/kT_form).

Unlike G2 (depth had the fm-scale Coulomb ceiling) and G3 (concentration over-determined
it), kappa_theta is the 2nd derivative of the SAME sub-Planck near-cancellation in the bend
coordinate, with NO external ceiling. This script does NOT fabricate the absolute kappa_theta.
It builds an explicit point-charge hinge to extract the coupling-independent STRUCTURE and
report what the geometry actually says -- win or kill.

MODEL EVOLUTION (honesty trail):
  v1 placed the opposite-charge screeners ON the hinge axis, equidistant from both free tips
  at every bend angle -> screening decouples from the bend (zero curvature contribution),
  leaving only the bare free-vertex repulsion. Real result, but it misses the cancellation.
  v2 (this file) puts the opposite charges on the CONCAVE side (offset y_s toward where the
  tips bend), so screening couples. The decomposition is then:
        kappa_full(y_s) = kappa_bare  -  kappa_screen(y_s)
  kappa_bare = bend curvature from the like-charge free-vertex repulsion alone (placement-
  independent, restoring); kappa_screen = curvature removed by the bend-coupled opposite
  charges. The SIGN of kappa_full depends on whether kappa_screen < kappa_bare.

THE GEOMETRY (bend plane xy; hinge pivot at origin; hinge axis z):
  free tips TA=L(sin b, cos b,0), TB=L(-sin b, cos b,0), b=(pi-alpha)/2, charge +1 (e:e, repel);
  opposite charges S1=(0,y_s,+s_z), S2=(0,y_s,-s_z), charge -1 (the bonded-pair screeners).
  alpha=0 straight; alpha>0 bends tips toward +y (toward the screeners). Energy = sum qi qj/rij.

Run: python3 0867_hinge_charge_model.py
"""
import numpy as np

L = 1.0
S_Z = 0.30   # half the opposite-pair separation along the hinge axis

def energy(alpha, y_s, repulsion_only=False):
    b = (np.pi-alpha)/2.0
    TA = np.array([ L*np.sin(b), L*np.cos(b), 0.0]); TB = np.array([-L*np.sin(b), L*np.cos(b), 0.0])
    S1 = np.array([0.0, y_s, +S_Z]);                 S2 = np.array([0.0, y_s, -S_Z])
    pos = [TA, TB, S1, S2]; q = [+1.0,+1.0,-1.0,-1.0]
    if repulsion_only: q = [+1.0,+1.0,0.0,0.0]
    E=0.0
    for i in range(4):
        for j in range(i+1,4):
            E += q[i]*q[j]/max(np.linalg.norm(pos[i]-pos[j]),1e-12)
    return E

def kappa0(y_s, repulsion_only=False, h=np.radians(0.25)):
    """Bend curvature of the STRAIGHT config: d2E/dalpha2|_0 (units q^2/L)."""
    return (energy(h,y_s,repulsion_only) - 2*energy(0.0,y_s,repulsion_only) + energy(h,y_s,repulsion_only))/h**2 \
           if False else (energy(2*h,y_s,repulsion_only)-2*energy(h,y_s,repulsion_only)+energy(0.0,y_s,repulsion_only))/h**2

def depth(y_s):
    return abs(energy(0.0, y_s))   # |net energy| of straight config -> residual E_ee proxy

print("="*80)
print("G1 CONFRONTATION -- explicit point-charge hinge model (Patch 0867)")
print("="*80)

kbare = kappa0(0.0, repulsion_only=True)
print(f"\n(A) BARE free-vertex repulsion curvature (placement-independent, restoring)")
print(f"    kappa_bare = {kbare:.4f} q^2/L  (the like-charge e:e 1-3 stiffening; always > 0)")

print(f"\n(B) DECOMPOSITION kappa_full = kappa_bare - kappa_screen, vs concave offset y_s")
print(f"    {'y_s/L':>7} | {'kappa_full':>11} | {'kappa_screen':>12} | {'sign':>14}")
buck_edge = None; prev = None
for y_s in (0.00,0.10,0.15,0.20,0.30,0.45,0.60,0.90,1.20):
    kf = kappa0(y_s); ks = kbare - kf
    sign = "restoring" if kf>0 else "BUCKLES (kf<0)"
    if prev is not None and prev>0 and kf<=0 and buck_edge is None:
        buck_edge = y_s
    prev = kf
    print(f"    {y_s:>7.2f} | {kf:>11.4f} | {ks:>12.4f} | {sign:>14}")
print(f"    => screening SUBTRACTS curvature. With equal |charge|, even a small concave offset")
print(f"       (y_s ~ {buck_edge if buck_edge else '<0.15'}) drives kappa_screen > kappa_bare -> kappa_full < 0:")
print(f"       the straight chain BUCKLES. NEW FAILURE MODE not in the 'clearly restoring' framing.")

print(f"\n(C) THE RESTORING WINDOW is a knife-edge ('medium' = near the buckling cliff)")
print(f"    A restoring hinge with 'medium' (sub-bare) stiffness needs kappa_screen JUST below")
print(f"    kappa_bare. Tune the opposite-charge magnitude q_s (relative to tips) at fixed y_s=0.30:")
print(f"    {'q_s':>6} | {'kappa_full':>11} | {'kappa_full/E_ee':>15} | {'sign':>10}")
def energy_qs(alpha, y_s, q_s):
    b=(np.pi-alpha)/2.0
    TA=np.array([L*np.sin(b),L*np.cos(b),0]); TB=np.array([-L*np.sin(b),L*np.cos(b),0])
    S1=np.array([0,y_s,S_Z]); S2=np.array([0,y_s,-S_Z])
    pos=[TA,TB,S1,S2]; q=[1,1,-q_s,-q_s]; E=0
    for i in range(4):
        for j in range(i+1,4): E+=q[i]*q[j]/max(np.linalg.norm(pos[i]-pos[j]),1e-12)
    return E
def k0_qs(y_s,q_s,h=np.radians(0.25)):
    return (energy_qs(2*h,y_s,q_s)-2*energy_qs(h,y_s,q_s)+energy_qs(0,y_s,q_s))/h**2
ratios=[]
for q_s in (0.10,0.20,0.30,0.40,0.50,0.70):
    kf=k0_qs(0.30,q_s); Eee=abs(energy_qs(0.0,0.30,q_s)); r=kf/Eee if Eee>0 else float('nan')
    if kf>0: ratios.append(r)
    print(f"    {q_s:>6.2f} | {kf:>11.4f} | {r:>15.4f} | {'restoring' if kf>0 else 'buckles':>10}")
if ratios:
    print(f"    => in the restoring window kappa_full/E_ee ranges ~[{min(ratios):.3f},{max(ratios):.3f}] and")
    print(f"       SHRINKS toward 0 as q_s rises to the buckling edge. So 'medium stiffness' sits")
    print(f"       next to a buckling cliff: the softer you want it, the closer to instability.")

print(f"\n(D) ANHARMONIC CEILING (axial restoring case y_s=0, valid harmonic reference)")
kf0 = kappa0(0.0); E0 = energy(0.0,0.0)
for amp_deg in (10,20,45,70,90,110):
    amp=np.radians(amp_deg); Eh=E0+0.5*kf0*amp**2; Ea=energy(amp,0.0)
    print(f"    bend {amp_deg:>3d} deg | harmonic={Eh:+8.4f} | actual={Ea:+8.4f} | dev={ (Ea-Eh)/abs(Eh-E0+1e-12):+7.2%}")
print(f"    => harmonic to ~20-45 deg; stiffens toward ~90 deg (superposition ceiling).")

print(f"\n(E) THE BRIDGE + make-or-break, stated precisely")
print(f"    kappa_theta/kT_form = (kappa_theta/E_ee) * (E_ee/kT_form)")
print(f"    The model gives kappa_theta/E_ee that (i) is SIGN-CONDITIONAL (buckling cliff) and")
print(f"    (ii) shrinks to 0 at the cliff -> NOT bracketable to an in-band number from geometry.")
print(f"    Two-pronged make-or-break, both needing SF-2/SF-5 hTetra charge placement:")
print(f"      PRONG 1 (sign safety): is kappa_screen < kappa_bare? (opposite charges far/weak enough")
print(f"        that the straight chain does NOT buckle).  <-- NEW, surfaced by this model.")
print(f"      PRONG 2 (magnitude):  given a restoring kappa_full, is kappa_full/E_ee * E_ee/kT_form")
print(f"        in [100,700]?  (E_ee from G2 window; kT_form from 0860 thermal ratio).")

print("\n"+"="*80)
print("G1 VERDICT (Layer C, honest -- a partial KILL-RISK, not a pass): the hinge is restoring")
print("ONLY if the bend-coupled opposite-charge screening stays curvature-subdominant; the")
print("explicit model shows equal-magnitude concave screening BUCKLES the straight chain -- a")
print("failure mode the prior 'clearly restoring' framing missed. 'Medium' stiffness is a")
print("knife-edge next to that buckling cliff (kappa_full/E_ee -> 0 there). So G1 cannot be")
print("bracketed from geometry alone: it needs the SF-2/SF-5 sub-Planck charge placement to")
print("decide BOTH sign-safety (no buckling) AND magnitude. This is the genuine make-or-break,")
print("and the model SHARPENS it to two precise, decidable SF questions rather than a stiffness")
print("guess -- and newly flags BUCKLING as a real way the whole extended-aggregate channel dies.")
print("="*80)
