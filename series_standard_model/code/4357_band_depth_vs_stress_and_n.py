#!/usr/bin/env python3
"""4357 -- the landing-band depth as a function of the local stress, and N on c01's grid scale.
PSR = l_P/(1+u) (ratified dictionary, u = k*Delta|SSV|); floor l_P/2 at u = 1 (R-core surface, lapse 1/2).
R-DIBIT-COUNT-AT-FLOOR: N = GPs inside a ball of radius l_P/2. At stress u the PSR ball holds (2/(1+u))^3 N GPs, so the
band fills the outer fraction ((1+u)/2)^3 of it: depth = 1 - (1 - ((1+u)/2)^3)^(1/3) of the local PSR."""
import numpy as np
print("u = k*Delta|SSV|      where                         band depth (fraction of the local PSR)")
for u, where in ((0.0, 'reference: zero stress'), (7e-10, "Earth's surface (u ~ GM/rc^2)"), (2e-6, "Sun's surface"),
                 (0.2, 'neutron-star surface (~GM/rc^2)'), (0.5, ''), (0.9, ''), (1.0, 'R-core surface (floor l_P/2)')):
    r = (1 + u) / 2
    print(f"  {u:<10.3g} {where:32s} {1 - (1 - r**3) ** (1/3):.4%}")
ratio = 1e30   # c01: true grid ~ l_P/1e30 (order of magnitude)
N = 4 * np.pi / 3 * (ratio / 2) ** 3
print(f"\nN on c01's grid scale (PSR_0/a ~ 1e30): N = (4 pi/3)(PSR_0/2a)^3 ~ {N:.1e} DI-bits per GP per Moment "
      f"(= {N/12:.1e} submoments at 12 per submoment); order of magnitude only")
