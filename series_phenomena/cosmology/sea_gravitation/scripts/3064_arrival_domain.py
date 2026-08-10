#!/usr/bin/env python3
"""3064_arrival_domain.py — the ARRIVAL-DOMAIN construction (Patch
3064, founder's local-summation framing): the ongoing-arrival domain
of a GP is the ball B(O, chi_h) exactly. Source at comoving d
contributes to O's future sum iff d <= chi(t_e) for some emission
t_e >= now; chi strictly decreasing => condition = d <= chi_h(now).
Spherical by receiver isotropy; unique by construction."""
import numpy as np
from scipy.integrate import quad
OM, OL = 0.315, 0.685
E = lambda a: np.sqrt(OM/a**3 + OL)
chi = lambda a0: quad(lambda a: 1/(a*a*E(a)), a0, np.inf, limit=200)[0]
ch = chi(1.0)
mono = all(chi(a1) < chi(a0) for a0, a1 in [(1.0,1.2),(1.2,2.0),(2.0,5.0)])
ok = mono and ch > 0 and np.isfinite(ch)
print(f"chi_h(now) = {ch:.4f}/H0; chi(t_e) strictly decreasing: {mono}")
print(f"arrival domain = B(O, chi_h) exactly; L = R_h as a RADIUS; "
      f"{'PASS' if ok else 'FAIL'}")
