#!/usr/bin/env python3
"""4300 -- what a derivation of hbar can mean.  SI fixes h exactly (2019) as it fixes c (1983): hbar's SI number is a unit
convention.  The derivable content is dimensionless.  (Values: CODATA 2018.)"""
import numpy as np
hbar=1.054571817e-34; c=299792458.0; G=6.67430e-11; me=9.1093837015e-31; e=1.602176634e-19; eps0=8.8541878128e-12
mP=np.sqrt(hbar*c/G); tP=np.sqrt(hbar*G/c**5); EP=mP*c*c
print(f"(1) the corpus identity: E_P t_P = {EP*tP/hbar:.12f} hbar  (E_P and t_P are built from hbar; c03: 'by construction')")
print(f"    G = hbar c / m_P^2: {hbar*c/mP**2/G:.12f} G  (identity: m_P = sqrt(hbar c/G))")
a=e*e/(4*np.pi*eps0*hbar*c); aG=G*me*me/(hbar*c)
print(f"(2) dimensionless targets in which hbar appears:")
print(f"    fine-structure constant  alpha   = e^2/(4 pi eps0 hbar c) = {a:.10f} = 1/{1/a:.6f}   (charge vs action)")
print(f"    gravitational coupling   alpha_G = G m_e^2/(hbar c) = (m_e/m_P)^2 = {aG:.4e}   (mass hierarchy)")
print(f"    first place alpha meets the electron's magnet: a_e ~ alpha/(2 pi) = {a/(2*np.pi):.6f}  (measured 0.0011597)")
