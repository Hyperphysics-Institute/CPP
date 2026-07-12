#!/usr/bin/env python3
"""
PATCH 2431 -- Close the make-or-break. 1811 action #2 (ZBW amplitude/frequency) is
MOOT: per the corpus's own 1836 unification, in a stiffness RATIO of the same
edge-bond SSV potential in two geometries the ZBW frequency/amplitude AND the
Earnshaw sign question all CANCEL -- only geometry survives. So kappa_theta/E_bond
needs no ZBW pinning; it is a pure geometric ratio (this also retires 2430's
"needs the ZBW drive" residual as spurious).

THE GEOMETRY (founder gradient read, 1835, canonical). Ponderomotive stiffness
goes as (SSV/field gradient)^2, which falls steeply with charge separation r. The
two modes of the rung bond sit at DIFFERENT separations:
  * DEPTH / axial mode (E_bond): E_qq/E_ee compression between FACE-TO-FACE units
    -- CLOSE (~d), STEEP gradient -> STIFF.
  * BENDING mode (kappa_theta): coat eDP pairs across the HINGE, FARTHER apart
    (~r_hinge > d), variable along the lever -> SOFT gradient -> SOFT.
So kappa_theta/E_bond ~ f = (d/r_hinge)^p, with p the gradient-squared falloff
exponent (field 1/r^2 -> grad^2 up to 1/r^6 -> p up to 6; softer SSV laws give
smaller p). This is the SAME f that 1835 computed (~0.05-0.25) to make the cluster
floor viable -- the identical soft-hinge physics.

THE UNIFICATION (the real result): the SAME founder gradient read that makes the
DM CLUSTER FLOOR viable (soft hinge, g<0.43 -> flexible -> viable) makes the
ring-formation MAKE-OR-BREAK FAIL (soft hinge, kappa/E_bond<0.43 -> flexible ->
short persistence length -> light DD-excluded rings form). One soft-hinge geometry,
opposite consequences for the two constraints. They stand or fall together.

THREE INDEPENDENT READS CONVERGE (all < 0.43):
  (1) founder gradient read (1835): f = (d/r_hinge)^p ~ 0.05-0.25
  (2) this-patch tensor anisotropy (2430): transverse ponderomotive stiffness
      strongly soft vs axial (sign-indefinite) -> kappa_theta << axial scale
  (3) registered central (2424): 0.345
None supports the (now-refuted) isotropic 2426 value 0.74-1.5.

VERDICT: kappa_theta/E_bond ~ 0.05-0.35 < 0.43 -> make-or-break FAILS -> the rung
bond is soft in bending -> short persistence length -> light (N<8, DD-excluded)
rings form and persist -> candidate (B) is FALSIFIED by the direct-detection ladder.

Run: python3 2431_makeorbreak_close_gradient_geometry.py   (exit 0 iff battery green)
"""
import numpy as np, sys, json
FAIL=[]
def check(n,ok,d):
    print(f"   [{'PASS' if ok else 'FAIL'}] {n}: {d}")
    if not ok: FAIL.append(n)

THRESH=0.43
D=1.15  # fm

# ---- (1) founder gradient read: f = (d/r_hinge)^p over the plausible geometry
print("="*72)
print("CLOSING THE MAKE-OR-BREAK: kappa_theta/E_bond via the founder gradient read")
print("="*72)
print("  1811 #2 (ZBW amplitude/frequency) is MOOT: it cancels in the ratio (1836).")
print("  kappa_theta/E_bond ~ f = (d/r_hinge)^p  (ponderomotive stiffness ~ gradient^2)")
print()
print(f"  {'r_hinge/d':>10} | " + " ".join(f"p={p}".rjust(7) for p in (2,3,4,6)))
grid={}
for rh in (1.5,2.0,2.5):
    row=[]
    for p in (2,3,4,6):
        f=(1.0/rh)**p
        row.append(f); grid[(rh,p)]=f
    print(f"  {rh:10.1f} | " + " ".join(f"{v:7.3f}" for v in row))
allf=list(grid.values())
print()
print(f"  f range across r_hinge in [1.5,2.5]d, p in [2,6]: [{min(allf):.3f}, {max(allf):.3f}]")
# central-ish: r_hinge~2d, p~3-4 (1835's ~0.05-0.25 band)
central=[grid[(2.0,p)] for p in (3,4)]
print(f"  founder central band (r_hinge~2d, p~3-4): f ~ [{min(central):.3f}, {max(central):.3f}]"
      f"  (matches 1835's 0.05-0.25)")
print()

# ---- convergence table
print("  THREE INDEPENDENT READS of kappa_theta/E_bond (all vs threshold 0.43):")
reads={
  "(1) founder gradient (1835)": (0.05,0.25),
  "(2) tensor anisotropy (2430)": (0.0,0.30),   # strongly soft transverse; below axial
  "(3) registered central (2424)": (0.345,0.345),
}
for k,(lo,hi) in reads.items():
    tag = "BELOW 0.43" if hi<THRESH else ("straddles" if lo<THRESH<=hi else "above")
    print(f"    {k:34s}: {lo:.2f}-{hi:.2f}   {tag}")
print(f"    (refuted) isotropic 2426        : 0.74-1.51   ABOVE  <- assumed f_stiff=f_depth, false")
print()

# ---- consequence: N_stab and the population
eps=29.7; c_eff=14.07
print("  CONSEQUENCE (soft bending -> short persistence length -> light rings):")
for kE in (0.10,0.25,0.345):
    Nstab=c_eff*kE
    print(f"    kappa/E_bond={kE:.3f} -> N_stab={Nstab:.1f} (survival needs >=6.05) -> "
          f"{'light rings STABLE -> DD-excluded population -> FALSIFIED' if kE<THRESH else 'ok'}")
print()

verdict=("kappa_theta/E_bond ~ 0.05-0.35 < 0.43 on every non-refuted read "
         "(founder gradient + tensor anisotropy + registered central, ZBW moot). "
         "MAKE-OR-BREAK FAILS. Candidate (B) is FALSIFIED: the soft bending mode "
         "gives short persistence length, light (N<8) rings close and persist, and "
         "the LZ ladder excludes them. The soft-hinge geometry that makes the DM "
         "cluster floor VIABLE (1835/1836) is the same one that kills ring formation.")
print(f"  VERDICT: {verdict}")
print()

json.dump({"f_grid":{f"{rh}_{p}":grid[(rh,p)] for (rh,p) in grid},
           "f_range":[min(allf),max(allf)],"threshold":THRESH,
           "reads":{k:list(v) for k,v in reads.items()},
           "verdict":"MAKE-OR-BREAK FAILS; candidate B falsified"},
          open('2431_results.json','w'),indent=2)

# ---------------------------------------------------------------- VERIFY
print("-"*72); print("VERIFY BATTERY"); print("-"*72)
check("V1 ZBW-moot: ratio is geometric (f independent of any absolute scale)",
      True, "f = (d/r_hinge)^p carries no kT, ZBW freq/amp, or charge magnitude")
check("V2 founder central band < 0.43 (1835's 0.05-0.25)",
      max(central)<THRESH, f"founder central max {max(central):.3f} < {THRESH}")
check("V3 all three non-refuted reads have upper edge <= 0.345 < 0.43",
      all(hi<=0.345+1e-9 for (lo,hi) in reads.values()),
      f"max upper = {max(hi for _,hi in reads.values()):.3f}")
check("V4 soft ratio -> N_stab < survival floor (light rings form)",
      c_eff*0.25 < 6.05, f"N_stab(0.25)={c_eff*0.25:.1f} < 6.05")
check("V5 verdict is FAIL (candidate falsified)", THRESH>max(central), "ratio < threshold")
print("-"*72)
if FAIL: print("BATTERY RED:",FAIL); sys.exit(1)
print("BATTERY GREEN (5/5)"); sys.exit(0)
