"""4087 (EW lane) -- F5 re-examined: my 4085 comparison was against the wrong quantity, and the correct
one turns F5 into a falsifiable PREDICTION rather than a factor-400 failure.

4085 compared powers of delta directly to the Jarlskog invariant J = 3.08e-5 and found delta^3 ~400x too
large, delta^9 ~13x too small. That comparison was ILL-POSED: J is not a CP-violating PHASE. It is

    J = s12 s13 s23 c12 c13^2 c23 sin(delta_CP)

-- a product of three small MIXING ANGLES with the sine of the phase. In the Standard Model the smallness
of J comes almost entirely from the ANGLES; the phase itself is LARGE (delta_CP ~ 68 deg, sin ~ 0.93).

So CPP does not need a tiny CP-violating parameter at all. It needs (a) an O(1) phase -- which a substrate
T-arrow can naturally supply -- and (b) the CKM mixing angles, which are a SEPARATE, already-registered
problem (SF-2's 'generation-transition CKM-like statistical suppression').

P1  reconstruct J from PDG angles and phase; verify the decomposition.
P2  how much of J's smallness is angles vs phase?
P3  THE PREDICTION: if the substrate phase is MAXIMAL (sin delta_CP = 1), what J follows, and how close is
    it to observation? A maximal phase is the natural output of a substrate arrow with no free parameter.
P4  what F5 therefore reduces to, stated honestly.
"""
import numpy as np
# PDG 2024 Wolfenstein-equivalent standard-parametrisation values
s12, s13, s23 = 0.22500, 0.003675, 0.04182
d_cp = 1.196                      # radians (~68.5 deg)
c12, c13, c23 = np.sqrt(1-s12**2), np.sqrt(1-s13**2), np.sqrt(1-s23**2)

def jarlskog(sin_d):
    return s12*s13*s23*c12*c13**2*c23*sin_d

print("P1  reconstruct J from the standard parametrisation")
J_obs = jarlskog(np.sin(d_cp))
print(f"    s12 = {s12}, s13 = {s13}, s23 = {s23}, delta_CP = {d_cp:.3f} rad = {np.degrees(d_cp):.1f} deg")
print(f"    J (reconstructed) = {J_obs:.3e}    PDG quotes J ~ 3.08e-5")
assert abs(J_obs - 3.08e-5)/3.08e-5 < 0.15

print("\nP2  where does J's smallness come from?")
angles_only = s12*s13*s23*c12*c13**2*c23
print(f"    angle product (phase set to 1)     = {angles_only:.3e}")
print(f"    sin(delta_CP)                      = {np.sin(d_cp):.3f}")
print(f"    => the ANGLES supply the {1/angles_only:.0f}-fold suppression; the PHASE is O(1) and supplies")
print(f"       only a factor {np.sin(d_cp):.2f}. J is small because the mixing is small, NOT because CP")
print(f"       violation is weak.")

print("\nP3  THE PREDICTION: a maximal substrate phase")
J_max = jarlskog(1.0)
print(f"    if sin(delta_CP) = 1 (maximal CP violation, the natural output of an arrow with no free")
print(f"    parameter), then  J_predicted = {J_max:.3e}")
print(f"    observed J = 3.08e-5  =>  ratio predicted/observed = {J_max/3.08e-5:.3f}  ({abs(J_max/3.08e-5-1)*100:.0f}% high)")
print(f"    equivalently, observation implies sin(delta_CP) = {3.08e-5/angles_only:.3f}, i.e. delta_CP is")
print(f"    within {90-np.degrees(np.arcsin(min(1,3.08e-5/angles_only))):.0f} deg of maximal.")
print("    NOTE: this looks attractive at J level (9% high) but see P3b -- at PHASE level it is excluded.")

print("\nP3b IS THE MAXIMAL-PHASE PREDICTION ACTUALLY VIABLE? (the check that matters)")
sig = 0.044   # rad, approximate PDG uncertainty on delta_CP
print(f"    measured delta_CP = {d_cp:.3f} +/- {sig:.3f} rad; maximal = pi/2 = {np.pi/2:.3f} rad")
print(f"    distance from maximal = {(np.pi/2 - d_cp)/sig:.1f} sigma")
print("    => a STRICTLY maximal phase is EXCLUDED by the measured phase, by many sigma.")
print("       So the strict prediction FAILS. What survives is the reframing, which is the real result:")
print("       the substrate quantity F5 needs is O(1), not 3e-5.")

print("\nP4  what F5 reduces to")
print("    NOT: find a substrate parameter of size 3e-5 (4085's framing -- wrong quantity).")
print("    BUT: (a) show the substrate phase is O(1) -- NOT maximal, which P3b excludes at 8.5 sigma;")
print("             the arrow must produce a phase near 68.5 deg, which is NOT a free win; and")
print("         (b) derive the three CKM mixing angles, which is a SEPARATE registered problem in SF-2")
print("             ('generation-transition CKM-like statistical suppression'), not a chirality problem.")
print("    F5 is therefore NOT a failure of chi4. It is a boundary between the chirality axiom and the")
print("    generation/mixing problem -- and no prediction is claimed here: the maximal-phase reading is excluded (P3b).")
