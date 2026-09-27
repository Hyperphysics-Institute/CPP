#!/usr/bin/env python3
"""4310 -- calibrate N (DI-bits per GP per Moment) to alpha, then audit which independent observables also depend on N."""
import numpy as np
alpha=1/137.035999; lP=1.616255e-35; me=9.1093837015e-31; mP=2.176434e-8
print("(A) N calibrated to alpha:  N = 4 pi alpha (PSR/s)")
for R in (1e30,1/9.9e-33): print(f"    PSR/s = {R:.1e}: N = {4*np.pi*alpha*R:.2e} per GP per Moment")
print("(B) black-hole PSR, surface-count reading (N = 4 pi (PSR_min/s)^2):  PSR_min = sqrt(alpha s PSR)")
for R in (1e30,1/9.9e-33): print(f"    PSR/s = {R:.1e}: PSR_min = {np.sqrt(alpha/R):.1e} l_P;  SR-1 register floor l_P/2 = 5.0e-01 l_P  -> disagree by {0.5/np.sqrt(alpha/R):.0e}")
print("    SR-1: PSR_eff = l_P/(1 + k dSSV): reaching 1e-16 l_P needs k dSSV ~ 1e16 somewhere, and no register floor.")
print("(C) gravity as it stands (GR-1a): Q_grav = (m c^2/E_P) Q_Planck, k = alpha l_P^3/E_P with alpha CANCELLING;")
print(f"    alpha_geom (c02) = {3*(11+5*5**0.5)*(5+5**0.5)**0.5/320:.4f}, a Voronoi factor -- not 1/137; GR-1a's '(e/e_P)^2 set by geometry' is unsupported.")
print(f"    alpha_G = (m_e/m_P)^2 = {(me/mP)**2:.3e};  alpha_G/alpha = {(me/mP)**2/alpha:.2e}: the number a count-based gravity must explain.")
print("(D) EU e-fold budget N = ln(l_P/s) + 1.31 counts e-folds, not emissions: neither a conflict nor a check.")
