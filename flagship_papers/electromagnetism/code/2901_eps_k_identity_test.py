"""TEST 3 (pre-registered): is eps* . |k(eps*)| = 1 across model variants?

If yes: curvature-cancellation and LINK-2 marginality are the SAME
condition, and the substrate's eps is FORCED to eps* by the universality
of the primitive (founder ruling, 31 Jul: same rule for all CPs).
If no: the m=2, r=[1,12] match was a normalization accident.
"""
import numpy as np
import sys
sys.path.insert(0, 'flagship_papers/electromagnetism/code')
from importlib import import_module
mod = import_module('2900_entrainment_curvature')
drive = mod.drive

BETAS = np.array([0.01,0.02,0.03,0.05,0.08,0.10,0.15,0.20])
X = np.column_stack([np.ones_like(BETAS), BETAS**2, BETAS**4])

def cfit(eps, m, rmin, rmax):
    y = np.array([drive(b, eps, m, rmin, rmax) for b in BETAS])/BETAS
    coef,*_ = np.linalg.lstsq(X, y, rcond=None)
    return coef[0], -coef[1]/coef[0], -coef[2]/coef[0]

def eps_star(m, rmin, rmax, lo=1e-4, hi=1.0):
    # c(eps) is decreasing; bisect for the zero
    for _ in range(40):
        mid = 0.5*(lo+hi)
        _, c, _ = cfit(mid, m, rmin, rmax)
        lo, hi = (mid, hi) if c > 0 else (lo, mid)
    return 0.5*(lo+hi)

print(f"{'variant':>16} | {'eps*':>9} | {'|k(eps*)|':>10} | {'eps*.|k|':>9} | {'c4(eps*)':>9}")
for (m, rmin, rmax) in [(2.0,1,12),(2.0,1,20),(2.0,2,12),(2.0,0.5,12),(1.0,1,12),(3.0,1,12)]:
    es = eps_star(m, rmin, rmax)
    k, c, c4 = cfit(es, m, rmin, rmax)
    print(f"m={m} r=[{rmin:>3},{rmax:>2}] | {es:9.6f} | {abs(k):10.4f} | {es*abs(k):9.5f} | {c4:9.4f}")
