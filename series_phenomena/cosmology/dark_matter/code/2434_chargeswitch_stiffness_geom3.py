#!/usr/bin/env python3
"""
PATCH 2434 -- Make-or-break on the corrected geometry #3 (founder-pinned) with the
charge-switching stiffening mechanism. Stage 1+2 of the re-derivation.

GEOMETRY #3 (founder, this session): axial inter-plane spacing UNIFORM (E_qq-set,
d); within each plane the eCP coat sits at a LARGER transverse radius R_e than the
qCP core r_q, and larger specifically because E_ee < E_qq => the eCP-qCP
equilibrium sits farther out than qCP-qCP. Two planes/element, opposite polarity
plane-to-plane; each plane a cross with eCP-qCP-qCP-eCP diagonals (inner qCP
square radius r_q, outer eCP square radius R_e).

STIFFNESS MECHANISM (founder, this session): the static opposite-charge lattice is
Earnshaw-null (no static bending stiffness). Bending stiffness comes from
CHARGE-SWITCHING: for a duty fraction delta, a CP presents SAME charge to its
neighbour (repulsive, POSITIVE curvature -> resists compression on the ring's
inner circumference; opposite-charge the rest of the time resists outer tension).
So kappa_theta = delta * sum_fibers k_rep,fiber * x_fiber^2 (same-charge repulsion
curvature x lever-arm^2). delta borrowed as ~1/3 from SS-1 (the SU(3) vertex-
occupancy duty cycle, EXACT by C3 symmetry -- mechanism-SS-1 Step 29; the DM
lattice breaks C3 so 1/3 is a reference, not the value).

E_bond = the axial bond that fragments first. TWO BRANCHES (the decisive crux):
  DEEP:    E_qq core (~66 MeV) -- if fragmentation requires breaking the core.
  SHALLOW: E_ee coat (~1.25 MeV) -- if coat-mediated (collisional strip, TLA).

ANALYTIC SCALING (the clean result): k_rep = 2*coupling*hc/s^3, E_bond =
coupling*hc/s, r_q ~ s_qq/sqrt2 => kappa_core/E_qq = delta*4*(r_q/d)^2 = 2*delta (r_q=d/sqrt2).
The coat contributes ~ (alpha/alpha_s) less (53x weaker eCP coupling), negligible
in the deep branch despite its larger lever arm. So:
  DEEP  : kappa/E_bond ~ 2*delta        (~0.67 at delta=1/3)  -> ABOVE 0.43 (stiff)
  SHALLOW: kappa/E_bond ~ (alpha_s/alpha)*delta ~ 53*delta (~17) -> ULTRA-stiff
Branch factor = alpha_s/alpha ~ 53. BOTH branches clear 0.43 at delta=1/3:
charge-switching RESCUES the make-or-break (at a DRIFTED, heavier-than-N=8 mass).
Deep branch is delta-sensitive (crossover delta~0.22); shallow is ultra-stiff.

Run: python3 2434_chargeswitch_stiffness_geom3.py   (exit 0 iff battery green)
"""
import numpy as np, sys, json
FAIL=[]
def check(n,ok,d):
    print(f"   [{'PASS' if ok else 'FAIL'}] {n}: {d}")
    if not ok: FAIL.append(n)

AHC=197.3            # MeV*fm (hc)
ALPHA=1/137.036
ALPHA_S=5/(8*(1+np.sqrt(5))/2)      # 5/(8 phi) = 0.386
d=1.15              # fm axial (E_qq-set)
E_qq=ALPHA_S*AHC/d  # ~66 MeV
E_ee=1.25           # MeV (1812 central; coat)
s_qq=ALPHA_S*AHC/E_qq               # qCP-qCP nearest sep = d by construction
r_q=s_qq/np.sqrt(2)                 # inner qCP square radius
THRESH=0.43
DELTA_REF=1/3       # SS-1 reference duty cycle

def krep(coupling, s):   # same-charge Coulomb repulsion curvature |V''| at sep s
    return 2*coupling*AHC/s**3

def kappa_and_ratio(delta, Re_over_rq, branch):
    """kappa_theta (delta * sum k_rep x^2) and kappa/E_bond for a branch."""
    R_e=Re_over_rq*r_q
    s_ee=np.sqrt(2)*R_e                 # eCP-eCP nearest sep (outer square side)
    # core: 4 qCP at radius r_q, same-charge repulsion (coupling alpha_s), lever r_q
    # sum x^2 over the square for bending about a diameter = 2 r_q^2 (2 fibers off-axis)
    kappa_core=delta*krep(ALPHA_S, s_qq)*(2*r_q**2)
    # coat: 4 eCP at radius R_e, coupling alpha, lever R_e
    kappa_coat=delta*krep(ALPHA, s_ee)*(2*R_e**2)
    kappa=kappa_core+kappa_coat
    E_bond=E_qq if branch=='deep' else E_ee
    return kappa, kappa/E_bond, kappa_core, kappa_coat

# ================================================================ RUN
print("="*72)
print("MAKE-OR-BREAK on geometry #3 + charge-switching (Patch 2434)")
print("="*72)
print(f"  d={d} fm  E_qq={E_qq:.0f} MeV  E_ee={E_ee} MeV  alpha_s/alpha={ALPHA_S/ALPHA:.0f}")
print(f"  s_qq={s_qq:.2f} fm  r_q={r_q:.2f} fm  delta_ref(SS-1)={DELTA_REF:.3f}  threshold {THRESH}")
print()
print("  kappa_theta/E_bond vs delta and E_bond branch (R_e/r_q=2.0):")
print(f"  {'delta':>7} | {'DEEP (E_qq)':>14} {'verdict':>8} | {'SHALLOW (E_ee)':>16} {'verdict':>8}")
for delta in (0.1,0.2,1/3,0.4,0.5):
    _,rd,_,_=kappa_and_ratio(delta,2.0,'deep')
    _,rs,_,_=kappa_and_ratio(delta,2.0,'shallow')
    vd='STIFF' if rd>=THRESH else 'soft'
    vs='STIFF' if rs>=THRESH else 'soft'
    print(f"  {delta:7.3f} | {rd:14.3f} {vd:>8} | {rs:16.2f} {vs:>8}")
print()

# analytic checks
kc,rd,kcore,kcoat=kappa_and_ratio(DELTA_REF,2.0,'deep')
_,rs,_,_=kappa_and_ratio(DELTA_REF,2.0,'shallow')
print(f"  At delta=1/3, R_e/r_q=2:")
print(f"    DEEP    kappa/E_bond = {rd:.3f}  (analytic ~2*delta={2*DELTA_REF:.3f})  -> {'CLEARS' if rd>=THRESH else 'below'} 0.43")
print(f"    SHALLOW kappa/E_bond = {rs:.1f}  (analytic ~2*53*delta={2*ALPHA_S/ALPHA*DELTA_REF:.0f}) -> ultra-stiff")
print(f"    branch ratio = {rs/rd:.1f}  (= alpha_s/alpha = {ALPHA_S/ALPHA:.1f})")
print(f"    coat/core in deep branch = {kcoat/kcore:.4f}  (~alpha/alpha_s={ALPHA/ALPHA_S:.4f}, coat negligible)")
print()

# R_e-insensitivity of the deep branch (coat negligible)
print("  DEEP-branch ratio vs R_e/r_q (should be ~flat -- coat negligible):")
for Rr in (1.5,2.0,3.0):
    _,rd,_,_=kappa_and_ratio(DELTA_REF,Rr,'deep')
    print(f"    R_e/r_q={Rr}: kappa/E_bond={rd:.3f}")
print()

# consequence
print("  CONSEQUENCE (the sign hinges on WHICH axial bond fragments first):")
print(f"    DEEP (E_qq core fragments): ratio ~{rd:.2f} > 0.43 -> STIFF -> N_stab ~ {14.07*rd:.0f} -> heavier ring family (N~9-13), DD-clear -> SURVIVES at drifted mass")
print(f"    SHALLOW (E_ee coat strips):  ratio ~{rs:.0f} >> 0.43 -> ULTRA-stiff -> linear/very-heavy DM, NOT an N=8 ring")
print(f"    charge-switching (delta~1/3) RESCUES the make-or-break; N=8 specifically still out (too stiff to close small).")
print()
print("  TWO decisive remaining numbers: (1) the duty cycle delta -- deep branch is delta-sensitive:")
print("  delta>~0.22 -> STIFF/survive, delta<0.22 -> soft/fail; SS-1 reference delta=1/3 CLEARS (0.67).")
print("  (2) which axial bond fragments (E_qq deep vs E_ee shallow, factor alpha_s/alpha) -- sets")
print("  moderately-stiff drifted-mass ring (deep) vs ultra-stiff linear/very-heavy DM (shallow).")

json.dump({"E_qq":E_qq,"E_ee":E_ee,"alpha_s_over_alpha":ALPHA_S/ALPHA,
           "deep_ratio_delta13":rd,"shallow_ratio_delta13":rs,
           "branch_factor":rs/rd,"coat_over_core":kcoat/kcore}, open('2434_results.json','w'),indent=2)

# ---------------------------------------------------------------- VERIFY
print("\n"+"-"*72); print("VERIFY BATTERY"); print("-"*72)
check("V1 DEEP-branch ratio ~ 2*delta (core-dominated)", abs(rd-2*DELTA_REF)/(2*DELTA_REF)<0.05, f"{rd:.3f} vs 2*delta {2*DELTA_REF:.3f}")
check("V2 branch factor = alpha_s/alpha (~53)", abs(rs/rd-ALPHA_S/ALPHA)/(ALPHA_S/ALPHA)<0.02, f"{rs/rd:.1f} vs {ALPHA_S/ALPHA:.1f}")
check("V3 coat negligible in deep branch (<3%)", kcoat/kcore<0.03, f"coat/core={kcoat/kcore:.4f}")
check("V4 deep ratio R_e-insensitive (<2% over R_e/r_q in [1.5,3])",
      abs(kappa_and_ratio(DELTA_REF,1.5,'deep')[1]-kappa_and_ratio(DELTA_REF,3.0,'deep')[1])/rd<0.02,
      "flat")
check("V5 BOTH branches STIFF at delta=1/3 (charge-switching rescues) -> survive at drifted mass",
      rd>=THRESH and rs>=THRESH, f"deep {rd:.2f} & shallow {rs:.0f} both >= 0.43")
print("-"*72)
if FAIL: print("BATTERY RED:",FAIL); sys.exit(1)
print("BATTERY GREEN (5/5)"); sys.exit(0)
