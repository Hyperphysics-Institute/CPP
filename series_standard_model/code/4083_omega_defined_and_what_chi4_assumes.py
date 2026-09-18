"""4083 (EW lane) -- is omega defined for a seeding unpaired CP? Yes -- and its orientation must be FREE.
Which tells us exactly what chi4 is: a faithful encoding of V-A, not a derivation of it.

SPIN-1: an unpaired -eCP MOVING through the DP Sea captures a DP; the inner +CP orbits at r_in, the outer
-CP at 2 r_in; the orbital angular momentum is hbar/2. So for a seeding unpaired CP:
   * a 3D spin axis omega EXISTS (the captured DP's orbital axis), and
   * a velocity v EXISTS (the capture happens BECAUSE the CP moves through the sea).
Hence helicity  b = sign(omega . v)  is well defined. 4076's B2 write rule survives.

BUT SPIN-1 nowhere fixes the orbital plane's ORIENTATION relative to v (checked: the paper's only
orientation discussion is the DP's internal rigid-body phase lock; its open-problems list defers the
qDP orbital planes). That is not a gap -- it is REQUIRED:
   * if omega were always parallel to v, every particle would have the same helicity: no spin-up/down.
   * if omega were always perpendicular to v, helicity would vanish identically: no weak coupling at all.
   * a FREE orientation is exactly what makes omega the SPIN STATE, and b the particle's PHYSICAL HELICITY.

J1  free orientation => <b> = 0 over an unpolarised ensemble (no substrate handedness -- consistent with
    CAPACITY-1 V3: the substrate does NOT spontaneously become chiral), while each particle has a definite b.
J2  a response LINEAR in b (4076 B3) then gives: zero asymmetry unpolarised, FULL asymmetry polarised --
    the observed signature of V-A (beta asymmetry from polarised nuclei).
J3  THE HONEST ACCOUNTING: what is axiomatic and what is derived.
J4  CONTROL: an EVEN response gives zero asymmetry even for a fully polarised sample.
"""
import numpy as np
rng = np.random.default_rng(4083)

def helicity_bits(n, polarisation=0.0):
    """n particles with velocity +z; spin axes isotropic except for a polarisation fraction along +z."""
    v = np.array([0,0,1.0])
    om = rng.normal(size=(n,3)); om /= np.linalg.norm(om,axis=1)[:,None]
    npol = int(polarisation*n)
    om[:npol] = v                                   # polarised fraction aligned
    return np.sign(om @ v)

print("J1  free orbital-plane orientation => no substrate handedness, but definite per-particle helicity")
b = helicity_bits(200000)
print(f"    <b> over an unpolarised ensemble = {b.mean():+.5f}  (consistent with V3: no spontaneous chirality)")
print(f"    fraction with b = +1: {np.mean(b>0):.4f}, b = -1: {np.mean(b<0):.4f}  (each particle definite)")
assert abs(b.mean()) < 0.01

print("\nJ2  the right observable: net helicity of the DECAYED population (longitudinal polarisation)")
print("    NOTE (estimator error caught in-patch): my first version compared population counts, which")
print("    measures imbalance of the SAMPLE, not of the RESPONSE. The physical V-A signature is that beta")
print("    electrons are longitudinally polarised even from UNPOLARISED sources.")
def net_helicity(kind, c=1.0, n=400000):
    b = helicity_bits(n)                      # unpolarised source: <b> = 0
    w = (1 + c*b) if kind == "linear" else (1 + c*b*b)
    w = np.clip(w, 0, None)                   # rates are non-negative
    return float(np.sum(w*b)/np.sum(w))
for c in (0.0, 0.25, 0.5, 1.0):
    print(f"    coupling c = {c:<5.2f}  linear response -> net helicity {net_helicity('linear',c):+.4f}"
          f"   even response -> {net_helicity('even',c):+.4f}")
print("    => LINEAR: emitted particles carry net helicity from an unpolarised source, saturating at -1/+1")
print("       for c = 1 (MAXIMAL V-A). EVEN: exactly zero at every coupling. This is the observed pattern.")

print("\nJ3  THE HONEST ACCOUNTING -- what chi4 derives and what it assumes")
print("    DERIVED (already in the corpus):")
print("      * omega exists                        -- SPIN-1's captured-DP orbit")
print("      * v exists                            -- the capture requires motion through the sea")
print("      * b = sign(omega.v) is P-odd          -- 4076 B2, 20,000/20,000")
print("      * <b> = 0 for the substrate            -- J1, consistent with CAPACITY-1 V3")
print("      * a linear response gives the observed polarised/unpolarised pattern -- J2")
print("    ASSUMED (the irreducible axiom):")
print("      * that the weak response is LINEAR in b rather than even")
print("      * the UNIVERSAL SIGN of that linear term -- i.e. WHICH helicity couples")
print("    => chi4 is a faithful CPP ENCODING of V-A. It is not a DERIVATION of V-A.")
print("       The sign is exactly the one P-odd primitive the arc has been hunting since 4046.")

print("\nJ4  CONTROL: even response must give exactly zero net helicity at every coupling")
print(f"    even, c = 1: {net_helicity('even',1.0):+.6f}   linear, c = 1: {net_helicity('linear',1.0):+.6f}")
tol = 5/np.sqrt(400000)     # sampling error of the estimator, not an arbitrary threshold
print(f"    sampling tolerance 5/sqrt(n) = {tol:.5f}: even response is consistent with exactly zero")
assert abs(net_helicity('even',1.0)) < tol and abs(net_helicity('linear',1.0)) > 0.99
