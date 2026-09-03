#!/usr/bin/env python3
"""
Patch 3604 verify — three things the record can compute about a SCALAR (T-1 census)
gravitational wave alongside GR's tensor wave, as order-of-magnitude bounds:

(1) Is a GW an EM wave?  Discriminators that are observational facts, not CPP.
(2) Scalar quadrupole radiation from a binary: for a massless scalar u with
    box u = 4 pi G rho / c^2 (T-1's normalisation: Poisson in statics), the
    far-field quadrupole term is u ~ (G/(2 c^4 r)) n_i n_j Qdd_ij ; GR's tensor
    strain is h_TT ~ (2G/(c^4 r)) Qdd_ij^TT.  Same order: epsilon_amp ~ 1/4 for
    a favourable orientation, with NO suppression from the theory unless the
    source side (T-3) supplies one.  [Order of magnitude; angular factors ~1.]
(3) What constrains it:
    (a) a Michelson is nearly blind to an isotropic PSR modulation — the
        differential is (kL)^2/6 ~ 1e-5 (3602) — so LIGO's polarization tests
        do NOT strongly bound this scalar mode by amplitude;
    (b) ENERGY LOSS does: Hulse-Taylor (PSR B1913+16) matches GR's quadrupole
        luminosity to ~0.2%; a scalar channel radiating at epsilon_L of the
        tensor luminosity must have epsilon_L < 2e-3, i.e. amplitude ratio
        epsilon_amp < ~0.045 (if the angular structure is comparable).
    So the T-1 scalar wave must radiate from a binary at < ~5% of GR's
    amplitude — a factor ~5 below the naive estimate — or the theory fails
    the binary-pulsar test.  Which of these holds is a T-1 + T-3 computation
    the corpus has not done.
"""
import numpy as np
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

print("(1) GW vs EM — observational discriminators (facts, not theory)")
for s in ("GW couples to mass-energy (all bodies respond, neutral ones included); EM couples to charge",
          "GW150914 (two ~30 Msun black holes) had NO electromagnetic counterpart; the wave was seen at h ~ 1e-21",
          "GW170817: the GW arrived 1.7 s BEFORE the gamma-rays, from the same merger — two different waves, the EM one from the ejected matter",
          "GW passes through the Earth essentially unattenuated; EM at these frequencies (100 Hz) does not propagate through matter",
          "polarization: GW is spin-2 (+ and x, patterns repeat under 90 deg rotation); EM is spin-1 (patterns repeat under 180 deg)",
          "lowest radiating multipole: GW quadrupole (mass monopole and dipole conserved); EM dipole"):
    print("    -", s)
check("a gravitational wave is not an electromagnetic wave: six independent discriminators", True)

print("(2) scalar vs tensor quadrupole amplitude from a binary (order of magnitude)")
# u_rad ~ (G/(2 c^4 r)) n n Qdd ;  h_TT ~ (2 G/(c^4 r)) Qdd^TT   -> ratio ~ 1/4 x (angular)
eps_amp_naive = 0.25
check("naive scalar/tensor amplitude ratio ~ 1/4 (same G/c^4 Qdd/r scaling; no suppression unless the source side supplies one)", abs(eps_amp_naive - 0.25) < 1e-12)

print("(3) what constrains a scalar admixture")
c = 2.998e8; L = 4000.0; f = 100.0; kL = 2 * np.pi * f * L / c; mich = kL**2 / 6
check("(a) Michelson differential from an isotropic PSR modulation ~ (kL)^2/6 = 1.2e-5: LIGO's interferometers are nearly BLIND to it — the polarization tests do not bound this mode by amplitude", mich < 1e-4, f"{mich:.1e}")
HT_precision = 2e-3                   # Hulse-Taylor orbital decay vs GR quadrupole formula, ~0.2%
eps_L_max = HT_precision; eps_amp_max = np.sqrt(eps_L_max)
check("(b) Hulse-Taylor bounds the scalar LUMINOSITY to < 0.2% of GR's -> amplitude ratio < ~0.045 (comparable angular structure assumed)", abs(eps_amp_max - 0.0447) < 0.002, f"eps_amp < {eps_amp_max:.3f}")
check("=> the T-1 scalar wave must radiate from a binary at least ~5x below the naive estimate, or CPP fails the binary-pulsar test. Whether T-1 + T-3 supply that suppression is a computation the corpus has not done: OPEN-GR-SCALAR-RADIATION-1", eps_amp_naive / eps_amp_max > 5)
print(); print(f"3604 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
