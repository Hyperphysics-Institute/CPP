#!/usr/bin/env python3
# ============================================================
# TP-1 verification — Patch 1706  (OPEN-TP-1 advance)
# The cutoff is INTRINSIC, not imposed: the 600-cell mode spectrum
# has a hard band top, and it carries a 600-cell fingerprint.
#
# QM-5 dispersion (their Field Operators section):
#     omega_k = c * sqrt(|lambda_k|) / l_P ,
#   lambda_k in {12, 1+phi, phi-1, 1-phi, -phi, -(1+phi)}  (six distinct).
# Largest eigenvalue lambda_max = 12 = z (the 600-cell coordination).
# Hence the field has a MAXIMUM mode frequency (no modes above it):
#     omega_max = sqrt(12) * c/l_P = sqrt(12)/t_P = 2*sqrt(3)/t_P.
#
# This answers the panel's T3 caveat (ChatGPT/Copilot): the cutoff is
# not a generic imposed "Planck cutoff at 1/t_P" but the intrinsic top
# of the 600-cell band, fixed by QM-5's spectrum and carrying sqrt(z).
# ============================================================
import math

t_P     = 5.391247e-44          # Planck time (s)
inv_tP  = 1.0/t_P               # = c/l_P = Planck angular frequency
phi     = (1+math.sqrt(5))/2

# six distinct 600-cell adjacency eigenvalues (QM-5 eq. eigenvalues)
eigs = [12, 1+phi, phi-1, 1-phi, -phi, -(1+phi)]
lam_max = max(eigs)             # = 12 = z
print("600-cell adjacency eigenvalues:", [round(e,4) for e in eigs])
print(f"lambda_max = z = {lam_max}")
print()

# intrinsic band-top mode frequency
omega_max = math.sqrt(lam_max) * inv_tP
print(f"omega_max = sqrt(12)/t_P = 2*sqrt(3)/t_P = {omega_max:.4e} rad/s")
print(f"  (sqrt(12) = 2*sqrt(3) = {math.sqrt(12):.5f})")
print()

# three candidate cutoffs, for comparison
nu0    = 1e15
omega0 = 2*math.pi*nu0
cands = {
    "naive 1/t_P (v0.3 placeholder)"     : inv_tP,
    "continuum-limit pi/l_P = pi/t_P"    : math.pi*inv_tP,
    "INTRINSIC 600-cell band top sqrt(12)/t_P": omega_max,
}
print(f"optical omega0 = 2*pi*1e15 = {omega0:.4e} rad/s")
print("ceiling <N>_max = C * ln(omega_cut / omega0):")
for name, wc in cands.items():
    print(f"   {name:<42}: ln = {math.log(wc/omega0):6.3f}  -> {math.log(wc/omega0):.2f} C")
print()

dln = math.log(math.sqrt(12))
print(f"shift from naive to band-top = ln(sqrt(12)) = {dln:.4f}  (+{100*dln/math.log(inv_tP/omega0):.1f}% on the ceiling)")
print()
print("KEY POINTS")
print("1. INTRINSIC regularization: the 600-cell spectrum is finite with a hard")
print("   band top omega_max; there are NO modes above it, so <N> is finite by the")
print("   finiteness of the lattice spectrum, not by an imposed cutoff.")
print("2. FRAMEWORK FINGERPRINT: omega_max = sqrt(z)/t_P = sqrt(12)/t_P = 2*sqrt(3)/t_P;")
print("   the coordination z=12 enters. A generic Planck-cutoff theory uses 1/t_P.")
print(f"3. Revised ceiling: <N>_max = C * ln(sqrt(12)/(t_P*omega0)) = {math.log(omega_max/omega0):.2f} C.")
print("4. C remains O(1), now interpretable via the 600-cell density of states near")
print("   the band top (van Hove); its precise numerical value (the HS mode sum")
print("   ||T2||^2_HS over the lattice modes) is the residual OPEN-TP-1.")
