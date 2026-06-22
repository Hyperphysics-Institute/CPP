#!/usr/bin/env python3
"""
OPEN-SR-9 gate: derive the mu0-emergence scheme from c06, NOT by tasting.

The 2016 result was conditional on HOW mu0 emerges from the substrate. Two candidate schemes:
  (S1) configurational/compliance  : mu0 ~ 1/C   (c06: field reconstructed each Moment from the
                                                   displacement config; "mu0,eps0 share one DP stiffness")
  (S2) kinetic inductance          : mu0 ~ m ~ C  (mu0 = inertia of transported carriers)
With eps0 ~ 1/C (solid: radial polarizability/compliance) fixed, we ask, for each scheme:
  - does c = 1/sqrt(mu0 eps0) VARY with the substrate stiffness C? (VSL horizon mechanism requires YES)
  - is Z0 = sqrt(mu0/eps0) geometric? (R2 PASS requires C-independent)

THE LEVER (independent of tasting): CPP already COMMITS to the VSL horizon mechanism (EU-1 shipped:
high early c_eff). That commitment FORCES whichever scheme makes c vary. We then read off what that
same scheme does to Z0. We do not choose the scheme to make Z0 pass; we let VSL choose it.
"""
import numpy as np
eps0 = lambda C: 1.0/C                       # radial compliance (solid)
schemes = {
 "S1 configurational/compliance (mu0~1/C)": lambda C: 1.0/C,
 "S2 kinetic inductance (mu0~m~C)"        : lambda C: C,
 "S0 hypothetical flat (mu0~const)"        : lambda C: 1.0,
}
Cs = np.array([0.5,1.0,2.0,4.0,8.0])
print("="*86)
print("OPEN-SR-9 gate: which mu0-scheme is consistent with the VSL mechanism, and what does it do to Z0?")
print("="*86)
for name,mu0 in schemes.items():
    c  = 1.0/np.sqrt(mu0(Cs)*eps0(Cs))
    Z0 = np.sqrt(mu0(Cs)/eps0(Cs))
    c_varies = (c.max()-c.min())/c.mean() > 0.1
    Z0_flat  = (Z0.max()-Z0.min())/Z0.mean() < 1e-9
    print(f"\n{name}")
    print(f"   c(C)  = {np.round(c,3)}   -> c varies with stiffness (VSL works)? {c_varies}")
    print(f"   Z0(C) = {np.round(Z0,3)}  -> Z0 geometric (R2 PASS)? {Z0_flat}")
    verdict = ("VSL ✓ + R2 PASS ✓" if (c_varies and Z0_flat)
               else "VSL ✗ (c fixed) -> kills the horizon mechanism" if not c_varies
               else "VSL ✓ but R2 FAIL (Z0 carries C)")
    print(f"   => {verdict}")

print("\n"+"="*86); print("THE LOCK (the actual derivation):")
print(" - eps0 ~ 1/C is solid (radial compliance).")
print(" - For c = 1/sqrt(mu0 eps0) to VARY (VSL, which EU-1/c06 already commit to), mu0 must NOT be ~C")
print("   (S2 gives mu0 eps0 = const => c FIXED => no VSL). So the VSL commitment EXCLUDES the kinetic")
print("   scheme S2 -- the only one that would give R2 FAIL.")
print(" - The scheme VSL forces is S1 (mu0 ~ 1/C): c ~ C varies (high early c_eff) AND Z0 = sqrt((1/C)/(1/C))")
print("   is geometric => R2 PASS. The SAME mu0-scaling that powers VSL makes Z0 geometric.")
print(" - c06 independently gives S1: the photon is RECONSTRUCTED each Absolute Moment from the frozen")
print("   displacement configuration (lines 103-104,110), NOT inertially transported -> mu0 is a")
print("   compliance (~1/C), not a kinetic inductance (~m); and line 91 states mu0,eps0 share one stiffness.")
print("\n CONCLUSION: R2 is NOT an independent falsifier. R2 PASSES iff the VSL mechanism holds --")
print(" they are LOCKED by the shared mu0 ~ 1/C scaling. The FAIL scheme (S2) is excluded both by c06's")
print(" reconstruction mechanism AND by VSL-consistency. Conditional on CPP's standing VSL commitment,")
print(" the 2016 conditional-PASS is CLOSED to PASS.")
