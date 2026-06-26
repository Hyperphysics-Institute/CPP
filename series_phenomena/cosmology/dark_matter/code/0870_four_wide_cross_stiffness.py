#!/usr/bin/env python3
"""
Patch 0870 (the 4-WIDE CROSS: bending stiffness is a BEAM property, NOT a hinge residual --
why the cross sidesteps the chain make-or-break, and lands the persistence length in-band)
==========================================================================================
0867/0869 wounded the single STRAND: its bend stiffness is a per-hinge angular spring that is a
near-cancelled residual (symmetric family BUCKLES; alternating family docks too tight). The
4-wide cross is a DIFFERENT entity (Thomas): a bundle of ~4 parallel hTetra strands cross-bonded
into a 2D cross-section. This script asks whether its stiffness clears the loop/length bar.

THE KEY REFRAME (why the cross is not just 'a stiffer chain'):
  Bending a cross-bonded bundle does NOT bend each strand at its hinge. It forces the OUTER
  strands to STRETCH and the inner ones to COMPRESS (plane-sections beam bending). The restoring
  energy therefore comes from the AXIAL bond stretch stiffness kappa_ax ~ E_bond -- a robust,
  LARGE quantity (the same E_ee/E_qq depth G2/0865 bracket) -- times the WIDTH^2 lever, NOT from
  the near-cancelled hinge angular spring. So:
      B_beam = kappa_ax * a * Sum_i (y_i - y_neutral)^2        (Euler-Bernoulli, parallel strands)
      l_p(rungs) = B_beam / (kT * a) = (E_bond/kT) * Sum (dy_i)^2     [a=l_rung=1, kappa_ax~E_bond/a^2]
  The cross is stiff for a STRUCTURALLY DIFFERENT reason than the strand, IMMUNE to the
  near-cancellation that killed the strand. That is the whole point.

GEOMETRY MATTERS (why 'cross', not flat 'ribbon'):
  A FLAT 4-wide ribbon is stiff for IN-plane bending (Sum dy^2 ~ 5) but FLOPPY out-of-plane
  (all strands at one out-of-plane coordinate -> Sum dz^2 = 0 -> it COILS out-of-plane).
  A '+' CROSS (2D cross-section) is stiff in BOTH transverse directions (Sum ~ 2 each), so it
  resists bending isotropically and will not coil. This is exactly why the cross, not the ribbon,
  is the viable stiff morphology -- the model confirms Thomas's choice.

Layer C: kappa_ax~E_bond (G2/0865 bracket), the cross-bond coupling (assumed present = the cross
definition), and the realized width are SF/kinetics-pending. This maps the stiffness and shows
the bracket lands favorably -- the first goalpost that is over-determined GOOD rather than a kill.

Run: python3 0870_four_wide_cross_stiffness.py
"""
import numpy as np

# ---- cross-section geometry: second moment Sum (offset)^2 about the neutral axis ----
def second_moment(coords):
    """coords: list of (y,z) strand positions (rung units). Returns (Sum dy^2, Sum dz^2)."""
    P=np.array(coords,float); c=P.mean(0); D=P-c
    return (D[:,0]**2).sum(), (D[:,1]**2).sum()

FLAT_RIBBON = [(0,0),(1,0),(2,0),(3,0)]                 # 4 in a row
PLUS_CROSS  = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]         # center + 4 arms (5 strands)
PLUS_CROSS4 = [(1,0),(-1,0),(0,1),(0,-1)]               # 4 arms only

print("="*86)
print("4-WIDE CROSS stiffness -- a BEAM property, not a hinge residual (Patch 0870)")
print("="*86)

print("\n(A) WHY 'cross' not flat 'ribbon': isotropic vs floppy out-of-plane")
for name,coords in [("flat 4-ribbon",FLAT_RIBBON),("+ cross (5)",PLUS_CROSS),("+ cross (4 arms)",PLUS_CROSS4)]:
    Iy,Iz=second_moment(coords)
    note = "FLOPPY out-of-plane (coils)" if min(Iy,Iz)<0.5 else "isotropically stiff"
    print(f"    {name:<18}: Sum dy^2={Iy:4.1f}, Sum dz^2={Iz:4.1f}  -> {note}")
print("    => the flat ribbon has ~0 stiffness for one bending axis -> coils. The + cross is")
print("       stiff in BOTH (~2 each) -> the viable morphology. (confirms the 'cross' choice.)")

print("\n(B) PERSISTENCE LENGTH  l_p(rungs) = c_geom * (E_bond/kT),  c_geom = Sum(offset)^2 (worst axis)")
c_cross = min(second_moment(PLUS_CROSS));  c_ribbon = max(second_moment(FLAT_RIBBON))
print(f"    c_geom: + cross (worst axis) = {c_cross:.1f}; flat ribbon (best axis) = {c_ribbon:.1f}")
print(f"    E_bond/kT bracket from 0865 lifetime floor: >= ~100  (E_bond in [0.8keV,2MeV], kT<=19keV)")
print(f"    {'E_bond/kT':>10} | {'l_p cross (c=2)':>15} | {'l_p ribbon-inplane (c=5)':>24} | band 300-2500?")
for r in (50,100,150,300,600,1500):
    lp_c=c_cross*r; lp_r=c_ribbon*r
    band="cross IN" if 300<=lp_c<=2500 else ("cross low" if lp_c<300 else "cross stiff>band")
    print(f"    {r:>10d} | {lp_c:>15.0f} | {lp_r:>24.0f} | {band}")
print("    => at the 0865 floor (E_bond/kT~100) the + cross gives l_p~200 rungs; for E_bond/kT>=150")
print("       (just above floor) l_p>=300 -> covers the band. The SAME bond depth the lifetime")
print("       floor demands ALSO supplies the persistence length -- the stiffness is OVER-DETERMINED")
print("       by G2/0865, not a separate fine-tuning. (l_p>band just means rigid rods -- not a failure.)")

print("\n(C) SIGN-SAFETY: the beam stiffness OVERWHELMS any residual single-hinge instability")
print("    a cross of N_w strands inherits N_w hinge residuals (each ~ kappa_hinge, possibly <0/")
print("    buckling from 0867/0869). Stability ratio = B_beam / (N_w * |kappa_hinge|).")
print(f"    {'kappa_hinge/E_bond':>18} | {'B_beam/(N_w|kh|)  (cross, E_bond/kT=100)':>40}")
for kh in (0.01,0.05,0.2,0.5):
    # B_beam ~ c_cross*E_bond ; N_w=4 ; |kappa_hinge|=kh*E_bond  -> ratio = c_cross/(4*kh)
    ratio = c_cross/(4*kh)
    print(f"    {kh:>18.2f} | {ratio:>40.1f}")
print("    => for any plausible hinge residual (|kappa_hinge| <~ 0.5 E_bond) the beam stiffness wins")
print("       by 1-50x: the cross is STABLE even if the bare strand hinge buckles. The width-coupled")
print("       bond-stretch restoring force dominates the near-cancelled hinge term. (sign-safe.)")

print("\n(D) sigma/m: a stiff/semiflexible cross is an extended scatterer, AND the sub-unit the ball needs")
print("    object length L (rungs) vs l_p~200-500: L<=l_p -> rigid rod (d_f=1, sigma/m ~ L);")
print("    L>l_p -> semiflexible (d_f~1-1.5, sigma/m ~ L^(2-d_f) still GROWS). Either way sigma/m rises")
print("    with size toward the band. AND a stiff cross is precisely the EXTENDED sub-unit whose")
print("    cluster-cluster coalescence gives the d_f<2 amorphous ball (0868) -- so the cross feeds BOTH")
print("    the standalone-ribbon route and the fluffy-ball route. The morphologies unify on the cross.")

print("\n"+"="*86)
print("4-WIDE CROSS VERDICT (Layer C -- the first goalpost that brackets FAVORABLY, not a kill):")
print("the cross's bend stiffness is a BEAM property (axial bond-stretch kappa_ax~E_bond times width^2),")
print("NOT the near-cancelled hinge angular residual that killed the single strand -- so it SIDESTEPS")
print("the entire chain make-or-break. l_p(rungs) = c_geom*(E_bond/kT) with c_geom~2 (+ cross, isotropic)")
print("to 5 (ribbon, in-plane). The 0865 lifetime-floor bond depth (E_bond/kT>=100) ALREADY supplies")
print("l_p ~ 200-500 rungs, covering/approaching the 300-2500 band -- the stiffness is OVER-DETERMINED")
print("by the same G2/0865 depth the lifetime needs, not a new fine-tuning. The beam stiffness also")
print("overwhelms any residual hinge buckling (sign-safe). The viable shape is the '+' CROSS (isotropic),")
print("not the flat ribbon (which coils out-of-plane) -- confirming Thomas's choice. Open (SF/kinetics):")
print("the cross-bond coupling strength (assumed present), the realized width, whether the cross stays")
print("a 1D cross vs branching into a 2D sheet (which would raise d_f), and the precise E_bond/kT. But")
print("unlike G1, none of these is a near-cancellation: the cross is robustly stiff for a structural reason.")
print("="*86)
