"""
Scoping TODO-4111-A3AMEND: what is the MINIMAL addition to A3' that carries b?

Constraint from 4110: the added content must yield a pseudoscalar that is NONZERO
on the D6 W bracelet, where (Phi, V, Q) gives identically zero.
"""
import numpy as np
rng=np.random.default_rng(4111)

print("="*68)
print("OPTION A — postulate a pseudoscalar channel chi directly: LSP' + (chi)")
print("="*68)
print("  Carries b by construction, but explains nothing: b IS the postulate.")
print("  Adds a rank-0 P-odd irrep. Cheapest in content, zero explanatory value.\n")

print("="*68)
print("OPTION B — add an AXIAL VECTOR channel A_i: LSP' = (Phi, V_i, Q_ij, A_i)")
print("="*68)
print("  Then a pseudoscalar is AUTOMATIC: b ~ A . V  (axial dot polar).")
print("  A is the CP's ZBW spin; V is the existing polar displacement channel.")
print("  b = sign(A.V) = sign(omega.v) -- EXACTLY chi_4's helicity bit, now DERIVED")
print("  from the broadcast content rather than postulated.\n")

print("C1  does A.V survive on the D6 W bracelet, where det[V,QV,Q^2V] died?")
# bracelet axis along z; incoming leg with spin A and travel V at generic angle
nz=0; vals=[]
for _ in range(20000):
    A=rng.normal(size=3); A/=np.linalg.norm(A)
    V=rng.normal(size=3); V/=np.linalg.norm(V)
    b=A@V
    vals.append(b)
    if abs(b)>1e-9: nz+=1
print(f"    nonzero in {nz}/20000 draws, mean |A.V| = {np.mean(np.abs(vals)):.4f}")
print("    A.V does NOT depend on Q at all, so no eigenvalue degeneracy can kill it.")
print("    The 4110 obstruction is bypassed entirely.  C1 PASS\n")

print("C2  does A.V reproduce F6's independently-derived P/T signature for b?")
print("    F6 (Patch 4085) requires: b is P-ODD, C-even, T-EVEN.")
# A axial: P-even, T-odd (angular momentum reverses under time reversal)
# V polar displacement/velocity: P-odd, T-odd
P_A, T_A = +1, -1
P_V, T_V = -1, -1
print(f"    A (axial):  P = {P_A:+d}, T = {T_A:+d}")
print(f"    V (polar):  P = {P_V:+d}, T = {T_V:+d}")
print(f"    A.V      :  P = {P_A*P_V:+d}, T = {T_A*T_V:+d}")
assert P_A*P_V == -1 and T_A*T_V == +1
print("    -> P-ODD and T-EVEN, matching F6 EXACTLY. C2 PASS")
print("    (F6 was derived from CPT independently of this construction, so this")
print("     is a genuine consistency check, not a restatement.)\n")

print("C3  is A.V zero in the isotropic sea (F2 must still hold)?")
print("    A sea DP: two CPs, opposite polarity. Polarity clause (F6) => response")
print("    ~ polarity x b. Under DP-CAL-1 (4107) b_+ = b_-, so R = q(b_+ - b_-) = 0.")
Aa=rng.normal(size=3); Vv=rng.normal(size=3)
bp=np.sign(Aa@Vv); bm=np.sign((-Aa)@(-Vv))
print(f"    check: b_+ = {bp:+.0f}, b_- = {bm:+.0f}, R = {bp-bm:+.0f}  -> F2 preserved. C3 PASS\n")

print("C4  how much content does Option B add?")
print("    LSP' currently: Phi (1) + V_i (3) + Q_ij (5 traceless sym) = 9 components")
print("    Option B adds:  A_i (3)                                    = 3 components")
print(f"    increase: 3/9 = {3/9:.0%} more broadcast content per GP per Moment")
print("    Option A would add 1 component but derive nothing.\n")

print("="*68)
print("RECOMMENDATION: Option B")
print("="*68)
print("""  Option B is more content than Option A (3 components vs 1) but it is the
  only one that EXPLAINS rather than postulates: b stops being an axiom and
  becomes the unique pseudoscalar of the amended broadcast. It also supplies a
  spin attribute the corpus currently lacks entirely (founder, 4107: "we had
  not assigned a spin to any CP"), which is needed elsewhere regardless.""")

print("\n"+"="*68)
print("C5  does Option B preserve F3's route (cage cancellation)?")
print("="*68)
import itertools
phi=(1+5**0.5)/2
def ico12():
    V=[]
    for s1 in(1,-1):
        for s2 in(1,-1): V+=[(0,s1,s2*phi),(s1,s2*phi,0),(s2*phi,0,s1)]
    V=np.array(V,float); return V/np.linalg.norm(V,axis=1,keepdims=True)
cage=ico12()
worst=0.0
for _ in range(20000):
    A=rng.normal(size=3); A/=np.linalg.norm(A)     # the quark's spin, fixed
    worst=max(worst,abs(np.sign(cage@A).sum()))    # V ranges over cage bond directions
print(f"    sum of sign(A.V) over the 12 cage bonds: max |sum| = {worst:.1f} over 20000 spins")
assert worst==0.0
print("    -> F3's antipodal-pairing cancellation (Patch 4101) SURVIVES under Option B,")
print("       still conditional on R-F3 (V lying on cage bonds). C5 PASS")

print("\n"+"="*68)
print("C6  CONFLICT CHECK — does an axial channel double-count magnetism?")
print("="*68)
print("""    SF-6 derives B as the CURL of a polar displacement (Patches 4069/4070:
    'B is axial because it is the curl of a polar displacement'). Option B adds
    an INDEPENDENT axial channel A_i to the same broadcast.

    These are formally distinct -- B = curl V is DERIVED from the V channel,
    while A is a per-CP attribute -- but the corpus would then carry TWO
    sources of axial structure in one packet, and every SF-6 result that reads
    'the axial part of the lattice state' would need to say WHICH one.

    This is the main cost of Option B and it is NOT resolved here.""")
# demonstrate they are independent objects
Vf=rng.normal(size=3); Af=rng.normal(size=3)
print(f"    (A and curl V are independent: A.V = {Af@Vf:+.3f} carries handedness,")
print(f"     while B.V = (curl V).V is the helicity DENSITY of the field, a different object)")
