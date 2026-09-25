#!/usr/bin/env python3
"""4294 -- founders_voice/4294: can charge hold the rim?  Hub-and-rim (4293): hub 2m, rim m, m = m_e/3, separation R,
spin S = hbar/2 = (2/9) m_e w R^2.  Units: r_C = hbar/(m_e c), energies m_e c^2, alpha = k e^2/(hbar c)."""
import numpy as np
alpha=1/137.035999
def need(R):   # centripetal force on the rim, in m_e c^2 / r_C, with S = hbar/2 fixing w
    w=9/(4*R*R); return (1/3)*w*w*(2*R/3), w*(2*R/3)
print("(1) the smallest dumbbell that can carry hbar/2 with the rim below light speed:")
print(f"    rim speed = w (2R/3) = 3/(2R) c  ->  below c needs R > 1.5 r_C   (R = 1.5: speed {need(1.5)[1]:.3f} c)")
print("\n(2) force available from charge vs force needed, at R (r_C units):")
for R in (1.5,3.0,10.0):
    F,v=need(R)
    coul=alpha/R**2                          # a full, unscreened e-e Coulomb pull
    pol=12*alpha**2/R**5*3                   # hub polarised by the rim (route-H spring, reduced mass m_e/6): 2 k^2 e^4/(mu w_Z^2 R^5)
    print(f"  R = {R:5.1f}: needed {F:.3e}   full Coulomb {coul:.3e} ({coul/F:.4f} of it)   hub polarisation {pol:.3e} ({pol/F:.2e})   rim speed {v:.3f} c")
print("  -> at the smallest size (R = 1.5 r_C, rim at c) a full unscreened charge supplies under 1% of the force.")
print("     Its share grows as R (needed force falls as 1/R^3, Coulomb as 1/R^2): full charge = needed at")
Rx=1.125/alpha
print(f"     R = 1.125/alpha = {Rx:.1f} r_C = {Rx*alpha:.3f} Bohr radii, rim speed {need(Rx)[1]:.4f} c  (SPIN-1's regime, 4286 F).")
print("     But the hub is neutral: what the rim actually feels is its polarisation, 1e-3 or less of what is needed.")
print("\n(3) why: at the Compton scale the needed force is ~ m_e c^2 / r_C; Coulomb there is k e^2 / r_C^2 = alpha x that.")
print(f"    charge is short by the factor alpha = 1/{1/alpha:.1f} at best, before any screening by the neutral hub.")
print("\n(4) a force of the needed strength: the ZBW restoring force itself (route H: stiffness mu w_Z^2, w_Z = m_e c^2/hbar),")
print("    applied between hub and rim (reduced mass mu = 2 m_e/9).  Circular: w = w_Z;  S = mu w R^2 = hbar/2:")
mu=2/9; w=1.0; R=np.sqrt(0.5/(mu*w))
print(f"    R = {R:.4f} r_C;  rim radius from the centre {2*R/3:.4f} r_C, speed {w*2*R/3:.4f} c;  hub radius {R/3:.4f} r_C, speed {w*R/3:.4f} c")
print("    -> the rim runs on route (H)'s circle (hbar/mc, at c); the hub on c04's r_th (hbar/2mc, at c/2).")
print(f"    energy check: orbital energy mu w^2 R^2 = {mu*w*w*R*R:.4f} m_e c^2 -- NOT negligible (4292/4293 assumed it was).")
