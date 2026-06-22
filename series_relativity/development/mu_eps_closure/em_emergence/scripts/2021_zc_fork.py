#!/usr/bin/env python3
"""
Q3 done HONESTLY: drop the mu0 ~ alpha_B analogy, use only the identity + the solid eps0 ~ 1/C.
Then R2's whole verdict reduces to ONE quantity: c(C). Let the grounded mechanics pick it.

  Z0 = sqrt(mu0/eps0) = 1/(eps0 c)        [identity mu0 eps0 = 1/c^2, no analogy]
  eps0 ~ 1/C  (solid: radial polarizability q^2/C)
  =>  Z0 ~ C/c.    So Z0 geometric  <=>  c ~ C exactly.

What is c(C), grounded (NOT via the impedance route, which would be circular)?
The DP-lattice wave speed c = sqrt(C/m) * a:
  - fixed Absolute Moment omega_0 (CPP, m = C/omega_0^2):  c = omega_0 a = CONST
  - fixed inertia m:                                       c ~ sqrt(C)
  - corpus 0740/2002 (dp_sea_mu_eps_symmetry.md line 97):  c ~ sqrt(C)  ("right sign for VSL")
  - 2016 impedance route (mu0~alpha_B~1/C, eps0~1/C):      c ~ C   <-- but this is DERIVED FROM the
                                                            mu0~alpha_B analogy under test => circular.
"""
import numpy as np
C = np.array([0.5,1.0,2.0,4.0,8.0])
eps0 = 1.0/C
def verdict(c, label):
    Z0 = 1.0/(eps0*c)
    flat = (Z0.max()-Z0.min())/Z0.mean() < 1e-9
    # k_alpha ~ d ln Z0 / d ln C  (LPI: need ~0 to <1e-6 ppm level)
    dlnZ = np.gradient(np.log(Z0), np.log(C))[2]
    print(f"  {label:38s} Z0(C)={np.round(Z0,3)}  d lnZ0/d lnC = {dlnZ:+.2f}  "
          f"-> {'GEOMETRIC (PASS)' if flat else 'CARRIES C (FAIL ~6 orders)'}")

print("="*94)
print("R2 reduces to c(C):   Z0 = C/c.   Which c(C) is grounded?")
print("="*94)
verdict(C,            "c ~ C   (PASS condition)")
verdict(np.sqrt(C),   "c ~ sqrt(C)  [fixed-m AND corpus 0740]")
verdict(np.ones_like(C), "c = const   [fixed-omega_0 mechanical]")
print("\n"+"-"*94)
print("The PASS needs c ~ C EXACTLY. Is that mechanically grounded? c = sqrt(C/m)*a:")
print("  c ~ C  requires  m ~ 1/C.  But CPP's schemes give:")
print("     fixed omega_0 -> m = C/omega_0^2 (m ~ +C)  -> c = const   -> Z0 ~ C   FAIL")
print("     fixed m                          (m ~ C^0) -> c ~ sqrt(C) -> Z0 ~ sqrt(C) FAIL")
print("  Neither gives m ~ 1/C. So c ~ C is mechanically UNNATURAL; the only route that produced it")
print("  (2016) got it FROM mu0 ~ alpha_B ~ 1/C -- the very analogy Q3 asks us to drop. Circular.")
print("\nHONEST VERDICT: with the analogy removed, every GROUNDED c(C) gives Z0 carrying C => FAIL ~6 orders.")
print("The 2016/2017 conditional-PASS rested on an ungrounded (circular) c ~ C. It does NOT survive Q3.")
