#!/usr/bin/env python3
"""4358 -- what the registered rules (one DI-bit per GP, fixed count N, PSR-shell-mean relay) predict for atomic clocks.
4355-4356: far-field coupling ~ N / (GPs per PSR volume) ~ (1+u)^3 at fixed count -> d ln(alpha) = -3 d(Phi/c^2)
(k_alpha = -3, Phi < 0 deeper in the well).  Test: Earth's orbit is eccentric, so the Sun's potential at the lab varies
annually; Lange et al., PRL 126, 011102 (2021), Yb+ E3/E2 vs Cs: (c^2/alpha) d alpha/d Phi = (14 +/- 11) x 1e-9."""
GM_sun, c, au, e = 1.32712440018e20, 299792458.0, 1.495978707e11, 0.0167
phi = GM_sun / (au * c**2)                    # |Phi|/c^2 at 1 au
dphi = 2 * e * phi                            # peak-to-peak annual swing (perihelion - aphelion)
pred = 3 * dphi
bound = (14 + 2 * 11) * 1e-9 * dphi           # 2-sigma upper bound on |d alpha/alpha| over the same swing
print(f"solar potential at 1 au: {phi:.3e} c^2; annual swing (peak-to-peak): {dphi:.3e} c^2")
print(f"predicted annual swing in alpha (k = -3): {pred:.2e}")
print(f"allowed by Lange 2021 (2 sigma):          {bound:.2e}")
print(f"excess: {pred/bound:.1e}x")
