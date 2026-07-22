#!/usr/bin/env python3
"""C2R-L1 verify (Patch 2770): the occupied-core screening closure.

Per the frozen prereg (2769): (A) alpha = kappa^2/(4 pi n) at the
operating point vs the imposed alpha = a/(pi sqrt2); (B) S_cont vs
S_disc by direct FCC lattice generation; (C) the decomposition of
the gap into the r < a core-medium contribution and the outer
discrete-vs-continuum residual; (D) decision quantities D1, D2.
Deterministic; no seeds.
"""
import numpy as np

phi = (1 + 5**0.5) / 2
a = 0.589 / phi                      # fm, lattice constant (frozen)
kappa = 2.0 / a                      # operating point kappa*a = 2
n = np.sqrt(2.0) / a**3              # FCC site density

alpha_imposed = a / (np.pi * np.sqrt(2.0))
alpha_derived = kappa**2 / (4 * np.pi * n)
D1 = abs(alpha_derived / alpha_imposed - 1.0)

S_cont = 4 * np.pi * n / kappa**2    # = 1/alpha_derived

# FCC lattice generation (primitive vectors, half-integer cubic form)
m = 14                               # generation range (converged; e^-2rho)
pts = []
for i in range(-m, m + 1):
    for j in range(-m, m + 1):
        for k in range(-m, m + 1):
            if (i + j + k) % 2 == 0 and not (i == j == k == 0):
                pts.append((i, j, k))
pts = np.array(pts, float) / np.sqrt(2.0)   # nn distance = 1 (units of a)
rho = np.linalg.norm(pts, axis=1)
rho = rho[rho <= 12.0]
S_disc = np.sum(np.exp(-2.0 * rho) / rho) / a          # fm^-1

# Convergence check: shrink cutoff by 2 and compare
rho2 = rho[rho <= 10.0]
S_disc_inner = np.sum(np.exp(-2.0 * rho2) / rho2) / a
conv = abs(S_disc - S_disc_inner) / S_disc

# Decomposition
core_frac = 1.0 - (1.0 + 2.0) * np.exp(-2.0)           # 1 - 3e^-2
S_core = S_cont * core_frac                             # r < a continuum medium
S_outer_cont = S_cont - S_core                          # r > a continuum
outer_excess = (S_disc - S_outer_cont) / S_outer_cont   # shell discreteness vs outer continuum
ratio = S_cont / S_disc                                 # the L4 record's 1.611

print(f"a           = {a:.10f} fm")
print(f"kappa       = {kappa:.6f} fm^-1   (kappa*a = 2)")
print(f"n_FCC       = {n:.6f} fm^-3")
print(f"alpha_imposed = a/(pi sqrt2)   = {alpha_imposed:.8f} fm")
print(f"alpha_derived = kappa^2/(4pin) = {alpha_derived:.8f} fm")
print(f"D1 = |alpha_derived/alpha_imposed - 1| = {D1:.3e}")
print(f"S_cont      = 1/alpha = {S_cont:.4f} fm^-1")
print(f"S_disc      = {S_disc:.4f} fm^-1   (lattice sum, cutoff 12a; conv {conv:.1e})")
print(f"S_cont/S_disc = {ratio:.4f}   (L4 record: 1.611)")
print(f"core-medium fraction 1-3e^-2 = {core_frac:.4f}   (L4 record's '59% self-exclusion')")
print(f"S_core(r<a, continuum medium) = {S_core:.4f} fm^-1")
print(f"S_outer_cont(r>a)             = {S_outer_cont:.4f} fm^-1")
print(f"shell-discreteness excess over outer continuum = {outer_excess:+.1%}")
print(f"identity check: S_disc = S_outer_cont*(1+excess): {S_outer_cont*(1+outer_excess):.4f}")
print(f"D2: ell_LO = committed envelope at derived alpha = 0.0904 +/- 0.0028 fm (no re-run owed, D1 = 0)")
