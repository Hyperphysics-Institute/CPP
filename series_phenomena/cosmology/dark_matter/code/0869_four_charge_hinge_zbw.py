#!/usr/bin/env python3
"""
Patch 0869 (G1 two-pronged make-or-break, REFINED with Thomas's 4-charge folded-vertex
apposition [2 plus, 2 minus] + ZBW soft-spacer -- and it RELOCATES the make-or-break)
==========================================================================================
G1 must land the hinge angular spring so a loop sits in the 0860/0861 size band
(~300-2500 rungs; per-hinge bend theta0 ~ 0.14-1.2 deg, since a loop closes at
N0 = 360deg/theta0). 0867 modeled the hinge as 2 LIKE tips (++) + 2 opposite screeners (--)
and found a BUCKLING kill-risk (bend-coupled equal screening subtracts curvature -> straight
config unstable).

THOMAS'S REFINEMENT: the real folded internal vertex is NOT (++ tips vs -- screeners). It is a
4-CHARGE environment, 2 PLUS + 2 MINUS: a +/- dipole vertex V1 apposing a +/- neighbor pair
(V2,V3), in a variety of plus-minus close/far combinations, with ZBW oscillation setting mean
separations (a soft spacer against collapse). With BOTH attractive (+-) and repulsive (++/--)
pairs in the same apposition, the bend coordinate is richer than 'restore vs buckle'.

WHAT THE MODEL ACTUALLY FINDS (honest; corrects the naive hope that this simply fixes G1):
  Two sign-families exhaust the 2+,2- apposition:
   * SYMMETRIC (++ || --): L/R-symmetric. The straight config is a MAX (k0<0) -> BUCKLES (now
     seen as a symmetric double-well at +/-theta0) for all but the largest gaps; straight-stable
     only at large gap. => 0867's buckling CONFIRMED in this family.
   * ALTERNATING (+/- || +/-): inherently L/R-asymmetric -> a PREFERRED fold angle theta0 != 0
     (intrinsic curvature; NO hard buckling -- a softer outcome). BUT theta0 is ROBUSTLY LARGE
     (~10-38 deg across all gap/separation geometry; larger gap makes it WORSE, not better),
     so the loop is ROBUSTLY TOO TIGHT: N0 ~ 10-21 rungs, never the 300-2500 band.
  The STIFFNESS kappa at the minimum is a tunable near-cancellation residual (spans ~0.03-300),
  but the ANGLE theta0 is the newly-stuck quantity: landing in-band needs theta0 <~ 1 deg, i.e.
  a near-cancellation of the per-hinge TANGENTIAL force at theta=0 -- the SAME make-or-break
  near-cancellation as 0867, relocated from the curvature to the preferred angle. Still SF-pending.

NET: the refinement is genuinely DIFFERENT and partly better (alternating family removes hard
buckling), but it is NOT a pass and does NOT land the loop in-band. It trades 'buckling' for
'too-tight loops', and the make-or-break survives as a tangential-force near-cancellation that
only SF-2/SF-5 charge placement can decide. ZBW remains structurally required.

GEOMETRY (fold in xy-plane, hinge axis z; pivot at origin, arm R=1):
  V1 = radial +/- dipole at angle th: outer (R+d/2)(sin th,cos th,0), inner (R-d/2)(sin th,cos th,0).
  Anvil pair fixed: V2=(-w,R+g,0), V3=(+w,R+g,0). th=0 straight; th>0 folds toward V3.
  ZBW: every 1/r -> 1/sqrt(r^2+a^2). Arrangement = signs(outer,inner,V2,V3), 2 plus + 2 minus.

Run: python3 0869_four_charge_hinge_zbw.py
"""
import numpy as np
R=1.0

def energy(th,d,w,g,a,signs):
    s_o,s_i,s2,s3=signs
    Po=np.array([(R+d/2)*np.sin(th),(R+d/2)*np.cos(th),0.])
    Pi=np.array([(R-d/2)*np.sin(th),(R-d/2)*np.cos(th),0.])
    V2=np.array([-w,R+g,0.]); V3=np.array([w,R+g,0.]); pos=[Po,Pi,V2,V3]; q=[s_o,s_i,s2,s3]
    E=0.
    for i in range(4):
        for j in range(i+1,4):
            r=np.linalg.norm(pos[i]-pos[j]); E+=q[i]*q[j]/np.sqrt(r*r+a*a)
    return E

def analyze(d,w,g,a,signs,thmax=np.radians(85),n=1401):
    ths=np.linspace(-thmax,thmax,n); Es=np.array([energy(t,d,w,g,a,signs) for t in ths])
    k=np.argmin(Es); i0=n//2; h=ths[1]-ths[0]
    k0=(Es[i0+1]-2*Es[i0]+Es[i0-1])/h**2                 # curvature at straight (theta=0)
    lo,hi=max(0,k-10),min(n,k+11); c=np.polyfit(ths[lo:hi],Es[lo:hi],2)
    return np.degrees(ths[k]), k0, 2*c[0], abs(Es[k])    # theta0, k0@straight, kappa@min, |E|@min

ALT=(+1,-1,-1,+1)     # alternating +/- || +/-
SYM=(+1,+1,-1,-1)     # symmetric ++ || -- (the 0867-like structure, for contrast)

print("="*88)
print("G1 REFINED -- 4-charge folded-vertex hinge (2+,2-) + ZBW; the make-or-break RELOCATES (0869)")
print("="*88)
print("    loop band: N0=300-2500 rungs <=> per-hinge theta0 ~ 0.14-1.2 deg (N0=360/theta0)")

print("\n(A) SYMMETRIC family (++ || --): straight-config stability k0 -> buckle? (confirms 0867)")
print(f"    {'gap g':>6} | {'k0@straight':>11} | {'theta0(deg)':>11} | {'verdict':>20}")
for g in (0.10,0.20,0.30,0.45,0.60):
    th0,k0,kap,Ed=analyze(0.35,0.40,g,0.10,SYM)
    v="straight-stable" if k0>0 else "BUCKLE (double-well)"
    print(f"    {g:>6.2f} | {k0:>11.2f} | {th0:>11.2f} | {v:>20}")
print("    => straight config is a MAX (k0<0) -> BUCKLES for all but the largest gap. 0867 confirmed.")

print("\n(B) ALTERNATING family (+/- || +/-): a preferred angle (no hard buckling) -- but TOO TIGHT")
print(f"    {'w':>5} {'g':>5} | {'theta0(deg)':>11} | {'N0 rungs':>9} | {'kappa@min':>10} | band?")
for w in (0.40,0.60,0.90):
    for g in (0.25,0.90,2.00):
        th0,k0,kap,Ed=analyze(0.35,w,g,0.10,ALT)
        N0=abs(360/th0) if abs(th0)>1e-9 else float('inf')
        band="YES" if 300<=N0<=2500 else ("LOW (too tight)" if N0<300 else "high")
        print(f"    {w:>5.2f} {g:>5.2f} | {th0:>11.2f} | {N0:>9.0f} | {kap:>10.3f} | {band}")
print("    => theta0 is ROBUSTLY LARGE (~10-38 deg) across ALL geometry; larger gap makes it WORSE.")
print("       loops are ~10-21 rungs -- never the 300-2500 band. Intrinsic curvature is too strong.")

print("\n(C) IS theta0 tunable into the band by ANY accessible parameter? (alternating family)")
print("    theta0 is the angle at which the moving +/- vertex DOCKS onto its attractive anvil")
print("    partner -- a GEOMETRIC lever angle. Test sensitivity to charge magnitudes and lever:")
def th0_only(d,w,g,a,qs):
    qo,qi,q2,q3=qs
    def en(th):
        Po=np.array([(R+d/2)*np.sin(th),(R+d/2)*np.cos(th),0.]); Pi=np.array([(R-d/2)*np.sin(th),(R-d/2)*np.cos(th),0.])
        V2=np.array([-w,R+g,0.]); V3=np.array([w,R+g,0.]); pos=[Po,Pi,V2,V3]; q=[qo,qi,q2,q3]
        return sum(q[i]*q[j]/np.sqrt(np.dot(pos[i]-pos[j],pos[i]-pos[j])+a*a) for i in range(4) for j in range(i+1,4))
    ths=np.linspace(-np.radians(88),np.radians(88),2001); Es=np.array([en(t) for t in ths]); return np.degrees(ths[np.argmin(Es)])
print(f"    anvil mag  q2 = 0.3 .. 5.0 :  theta0 = " +
      ", ".join(f"{th0_only(0.35,0.40,0.25,0.10,(+1,-1,-q2,+1)):.1f}" for q2 in (0.3,1.0,2.0,5.0)) + " deg")
print(f"    dipole mag qo = 0.3 .. 2.5 :  theta0 = " +
      ", ".join(f"{th0_only(0.35,0.40,0.25,0.10,(+qo,-1,-1,+1)):.1f}" for qo in (0.3,1.0,2.5)) + " deg")
print(f"    dipole len d  = 0.05.. 0.9 :  theta0 = " +
      ", ".join(f"{th0_only(d,0.40,0.25,0.10,(+1,-1,-1,+1)):.1f}" for d in (0.05,0.35,0.9)) + " deg")
print(f"    wide-anvil quadrupole limit:  theta0 = " +
      ", ".join(f"{th0_only(0.05,w,g,0.10,(+1,-1,-1,+1)):.1f}" for (w,g) in [(0.9,0.5),(1.5,1.0),(3.0,2.0)]) + " deg")
print("    => theta0 is ROBUSTLY ~18 deg (worse, to ~50 deg, in the wide limit) and is NOT moved")
print("       below ~17 deg by any charge magnitude or lever. It is a GEOMETRIC docking angle, not")
print("       a tunable residual. So in THIS generic 4-charge geometry there is NO accessible route")
print("       to a sub-degree (band-sized) loop -- the intrinsic-curvature route resists tuning.")

print("\n(D) ZBW: the structurally required soft-spacer (alternating family, near-balance geometry)")
print(f"    {'a (ZBW)':>8} | {'theta0(deg)':>11} | {'kappa@min':>10}")
for a in (0.02,0.05,0.10,0.20,0.35):
    th0,k0,kap,Ed=analyze(0.35,0.40,0.18,a,ALT)
    print(f"    {a:>8.2f} | {th0:>11.2f} | {kap:>10.3f}")
print("    => finite ZBW sets the mean separation -> finite kappa (spans ~10x here). Without it")
print("       attractive pairs collapse to contact (singular). ZBW is required for a defined hinge.")

print("\n"+"="*88)
print("G1 VERDICT (Layer C, refined -- honest, NOT a pass; a NEW kill-risk surfaced): Thomas's")
print("2+,2- apposition genuinely changes the risk and is partly better -- the ALTERNATING family")
print("removes 0867's HARD buckling, replacing collapse with a finite preferred fold angle. But it")
print("is NOT a rescue. In this generic 4-charge geometry the preferred angle is a GEOMETRIC docking")
print("angle, robustly ~18 deg (worse, ~50 deg, in the wide limit) and NOT moved below ~17 deg by any")
print("charge magnitude or lever -- so the alternating family self-closes into loops ~7-20 rungs,")
print("~15-50x TOO TIGHT for the 300-2500 band, and RESISTS tuning into it. The SYMMETRIC family")
print("still BUCKLES (0867 confirmed) except at large gap. So neither family lands a band-sized loop")
print("here: symmetric buckles (or straight-stable -> needs external closure), alternating curls far")
print("too tightly. The make-or-break is RELOCATED from 0867's stiffness-near-cancellation to the")
print("DOCKING ANGLE, and is now a harder, more geometric tension: the loop wants sub-degree per-hinge")
print("bend, the 4-charge docking robustly delivers tens of degrees. CAVEAT: this is ONE schematic")
print("geometry (radial dipole vs lateral pair); the true SF-2/SF-5 hTetra vertex geometry could be")
print("special (near-on-axis attractive partner -> small docking angle), but the burden is now squarely")
print("on SF to SHOW it, because the generic structure does not and resists. ZBW remains the required")
print("soft-spacer (sets finite kappa, prevents collapse). Two prongs, refined: PRONG-1 sign-safety =")
print("alternating family avoids buckling (good); PRONG-2 = can the SF vertex geometry give a sub-degree")
print("docking angle? -- now the sharp, and newly doubtful, open SF question.")
print("="*88)
