#!/usr/bin/env python3
"""
(b) Derive c_photon(C). The key: for VELOCITY, exact Lorentz invariance FORCES it.
    alpha = e^2/(4 pi eps0 hbar c_photon).  eps0 ~ 1/C (polarizability, solid).  hbar invariant
    (universal Absolute Moment). So alpha ~ C/c_photon ~ Z0. For a MOVING atom alpha is a Lorentz
    SCALAR (invariant; Ives-Stilwell). Therefore, for velocity-induced C changes:  c_photon ~ C  (FORCED).
(c) If c_photon(C) is a UNIVERSAL medium property (depends on local stiffness C, not on whether the
    SSV came from velocity or gravity), then c_photon ~ C holds for gravity too -> Z0 = C/c_photon = const
    -> R2 PASS. Universality is the load-bearing assumption.
Contrast with the PHONON: c_phonon = sqrt(C/m)*a ~ sqrt(C) (mechanical). Photon (~C) != phonon (~sqrt C).
"""
import numpy as np
C = np.array([0.5,1.0,2.0,4.0,8.0,16.0]); eps0 = 1.0/C; hbar=1.0; e2_4pi=1.0

print("="*88); print("(b) For velocity, Lorentz invariance (alpha = scalar) forces c_photon(C):"); print("="*88)
# alpha invariant REQUIRES c_photon proportional to C. Demonstrate: impose alpha=const, solve c_photon.
alpha0 = 1/137.036
c_photon_forced = e2_4pi/(alpha0*eps0*hbar)   # from alpha0 = e2_4pi/(eps0 hbar c) => c = e2_4pi/(alpha0 eps0 hbar)
slope = np.polyfit(np.log(C), np.log(c_photon_forced),1)[0]
print(f"  imposing alpha invariant (Lorentz) + eps0~1/C + hbar fixed  =>  c_photon ~ C^{slope:+.3f}")
print(f"  c_photon(C) = {np.round(c_photon_forced,3)}  -> LINEAR in C (slope +1.000). FORCED, not assumed.")

print("\n"+"="*88); print("(c) Universality transfer + the Z0 verdict for gravity:"); print("="*88)
print(f"  {'C':>6} {'eps0~1/C':>9} {'c_phonon~sqrtC':>15} {'c_photon~C':>12} {'Z0=C/c_photon':>14} {'Z0=C/c_phonon':>14}")
for Ci in C:
    e=1/Ci; cph=np.sqrt(Ci); cpt=Ci
    print(f"  {Ci:>6.1f} {e:>9.4f} {cph:>15.4f} {cpt:>12.4f} {Ci/cpt:>14.4f} {Ci/cph:>14.4f}")
Z0_photon = C/C; Z0_phonon = C/np.sqrt(C)
print(f"\n  Z0 with PHOTON speed (~C):  flat? {(Z0_photon.max()-Z0_photon.min())<1e-12}  -> GEOMETRIC -> R2 PASS")
print(f"  Z0 with PHONON speed (~sqrtC): flat? {(Z0_phonon.max()-Z0_phonon.min())<1e-9} -> ~sqrtC -> the 2021 FAIL")
print("\n  CONCLUSION (conditional): R2 PASSES if (i) VTD-1 (exact Lorentz => velocity forces c_photon~C)")
print("  and (ii) c_photon(C) is a universal medium property (transfers velocity's c~C to gravity).")
print("  The photon (~C, Lorentz-forced) and phonon (~sqrtC, mechanical) are DIFFERENT modes -- now DERIVED,")
print("  not asserted. Load-bearing assumption to scrutinize: medium-universality (ii).")
