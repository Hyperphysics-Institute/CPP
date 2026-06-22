#!/usr/bin/env python3
"""
Clean test: two poles, harmonic restoring stiffness C about equilibrium +/- d0/2, driven by the
FULL inverse-square field of a charge Q at distance R (Thomas's asymmetry: near pole sees more
field, displaces more, centroid shifts). Solve self-consistently; extract alpha_E, centroid shift,
asymmetry. Sweep C. Does eps0 ~ 1/C survive, or become ~1/sqrt(C) (which would revive PASS)?
"""
import numpy as np
q=1.0; d0=1.0; Q=1.0

def respond(C, R):
    xp, xm = d0/2, -d0/2
    for _ in range(4000):
        Ep = Q/(R-xp)**2          # inverse-square field at +q (nearer R -> larger)
        Em = Q/(R-xm)**2          # at -q
        xp = d0/2 + q*Ep/C        # harmonic displacement, self-consistent (field depends on pos)
        xm = -d0/2 - q*Em/C
    p_ind = q*(xp - xm) - q*d0    # induced dipole (subtract field-free separation)
    center = (xp + xm)/2          # centroid shift -- Thomas's effect
    asym = (Ep - Em)/((Ep+Em)/2)  # fractional field asymmetry across the DP
    return p_ind/(Q/R**2), center, asym

for R,regime in [(12.0,"LINEAR / LPI-relevant (weak field, R>>d0)"),(3.0,"STRONG / large asymmetry (R~few*d0)")]:
    print("="*84); print(f"Regime: {regime}"); print("="*84)
    print(f"  {'C':>7} {'alpha_E':>11} {'centroid':>12} {'field_asym':>11}")
    Cs=np.array([0.5,1.0,2.0,4.0,8.0,16.0]); aE=[]
    for C in Cs:
        a,ctr,asym = respond(C,R); aE.append(a)
        print(f"  {C:>7.2f} {a:>11.5f} {ctr:>12.2e} {asym:>11.4f}")
    aE=np.array(aE)
    slope=np.polyfit(np.log(Cs),np.log(np.abs(aE)),1)[0]
    print(f"  d ln(alpha_E)/d ln C = {slope:+.4f}   => eps0 ~ C^({slope:+.3f})")
    print(f"  [-1.0 = 1/C, retraction stands; -0.5 = 1/sqrt(C), PASS revives]\n")
print("Centroid shift is NONZERO in both (Thomas is right: the DP is not a symmetric stretch).")
print("The test is only whether that moves the leading C-exponent of eps0 away from -1.")
