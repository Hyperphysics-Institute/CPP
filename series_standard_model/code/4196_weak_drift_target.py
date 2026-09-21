#!/usr/bin/env python3
"""4196 — the empirical target for an A-dependent DISPLACEMENT, read off the measured weak interaction.

The nuclear-spin-independent parity-violating electron-nucleus interaction (textbook non-relativistic
form; measured in caesium to 0.35% and in polarised electron scattering):
        H_PV = G_F Q_W / (4 sqrt2 m_e c) * [ sigma.p rho(r) + rho(r) sigma.p ]
Its velocity operator is  v = dH/dp = p/m  +  G_F Q_W rho(r) / (2 sqrt2 m_e c) * sigma.
I.e. wherever the electron overlaps weak-charged matter it acquires an EXTRA VELOCITY ALONG ITS OWN
SPIN, proportional to the local weak-charge density, and zero where that density is zero.
"""
import math
hbar_c = 0.1973269804                    # GeV fm
GF = 1.1663787e-5 * hbar_c**3            # GeV fm^3
GF_SI = GF * 1.602176634e-10 * 1e-45     # J m^3
m_e, c = 9.1093837e-31, 2.99792458e8
s2w = 0.2312
rho0 = 0.16                              # nucleons per fm^3, saturated nuclear matter
N_frac, Z_frac = 0.6, 0.4                # heavy nucleus
rho_W = rho0 * (-N_frac + Z_frac * (1 - 4 * s2w)) * 1e45        # weak-charge density, m^-3
v = GF_SI * abs(rho_W) / (2 * math.sqrt(2) * m_e * c)
print(f"G_F                         = {GF_SI:.4e} J m^3")
print(f"weak-charge density (heavy) = {rho_W:.3e} m^-3   ({rho_W/1e45:+.4f} per fm^3)")
print(f"G_F * |rho_W|               = {GF_SI*abs(rho_W)/1.602e-19:.2f} eV")
print(f"extra velocity along spin   = {v:.0f} m/s   = {v/c:.2e} c      inside nuclear matter")
print(f"same, in free space         = 0 m/s                       (rho_W = 0)")
print(f"hop-gate weight it implies  = kappa/sigma = {v/c/0.49:.2e}     (4194: drift/c = 0.49 kappa/sigma)")
