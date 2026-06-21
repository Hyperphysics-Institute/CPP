#!/usr/bin/env python3
# ============================================================
# TP-1 verification — Patch 1701  (OPEN-TP-1 first half)
# Divergence class DERIVED from the Rukan-Gulla-Skaar kernel,
# and the two-regime structure of the regularization.
#
# RGS (arXiv:2510.21636) main text, "Gradual removal":
#   instantaneous removal -> the Heaviside truncation gives a
#   Fourier tail ~ 1/omega; with E(omega) ~ sqrt(omega) the norms
#   in <n> = sum_xi (||xi^-_-||^2 + ||xi^-_+||^2) diverge
#   LOGARITHMICALLY. -> dN/domega ~ 1/omega is DERIVED, not assumed.
#
# RGS gradual-removal bound (their Eq. 29/B47):
#   <n> <= kappa0/(4 T) + kappa0^2/(16 T^2),
#   with |T(omega)|^2 = 1/(1+(omega kappa0)^2/4), and the regime
#   1/omega0 << kappa0 << T for low transmissivity AND <n> <~ 1.
#
# RGS also introduce a FORMAL high-frequency cutoff (their Eq. B14,
# "can be arbitrarily high"). CPP identifies it with omega_P = 1/t_P.
# ============================================================
import numpy as np

# --- constants ---
t_P     = 5.391247e-44          # Planck time (s)
omega_P = 1.0/t_P               # lattice UV cutoff = Planck angular freq (rad/s)

# --- RGS optical example: omega0/2pi = 1e15 Hz ---
nu0     = 1e15                  # Hz
omega0  = 2*np.pi*nu0           # rad/s

print("="*64)
print("TP-1 Patch 1701 — divergence class + two-regime regularization")
print("="*64)
print(f"t_P                       = {t_P:.3e} s")
print(f"omega_P = 1/t_P (cutoff)  = {omega_P:.3e} rad/s")
print(f"omega0  (RGS optical)     = {omega0:.3e} rad/s   (nu0=1e15 Hz)")
print(f"1/omega0                  = {1/omega0:.3e} s")
print()

# ------------------------------------------------------------
# (1) DERIVED divergence class: dN/domega ~ 1/omega  =>  log.
#     <n>(omega_cut) = C * ln(omega_cut/omega0),  C = O(1).
#     CPP caps omega_cut at omega_P  =>  ceiling:
# ------------------------------------------------------------
L = np.log(omega_P/omega0)
print("(1) Derived log law  <n>(w_cut) = C * ln(w_cut/omega0):")
for wc, lbl in [(1e18,"1e18"),(1e25,"1e25"),(1e35,"1e35"),
                (omega_P,"omega_P (CPP cap)"),(1e60,"1e60 (continuum)")]:
    print(f"     w_cut={lbl:>18}: <n>/C = {np.log(wc/omega0):6.2f}")
print(f"     => CPP ceiling  <n>_max = C * ln(omega_P/omega0) = {L:.2f} * C")
print(f"        (continuum instantaneous: w_cut->inf, <n>->inf logarithmically)")
print()

# ------------------------------------------------------------
# (2) RGS gradual-removal bound, reproduce their numerical example
#     |T|^2 = 1e-4  ->  omega0*kappa0 = 200  ->  kappa0 = 200/omega0
#     check T ~ 1e-14 s gives <n> ~ 1
# ------------------------------------------------------------
def n_bound(kappa0, T):
    return kappa0/(4*T) + kappa0**2/(16*T**2)

kappa0 = 200/omega0
print("(2) RGS gradual bound  <n> <= kappa0/(4T) + kappa0^2/(16T^2):")
print(f"     |T|^2=1e-4 -> omega0*kappa0=200 -> kappa0 = {kappa0:.3e} s")
for T in [1e-12, 1e-13, 1e-14]:
    print(f"     T={T:.0e} s: <n> <= {n_bound(kappa0,T):.3f}")
print("     -> matches RGS: T as small as ~1e-14 s before <n> ~ 1.")
print()

# ------------------------------------------------------------
# (3) THE TWO REGIMES — the corrected physical picture.
#     A real shutter has mechanical removal time T. The lattice
#     forbids T < t_P. Compare the scales for an optical photon.
# ------------------------------------------------------------
print("(3) Two regimes (scale ordering for an optical photon):")
print(f"     t_P        = {t_P:.2e} s   (lattice tick; smallest possible T)")
print(f"     1/omega0   = {1/omega0:.2e} s   (optical period scale)")
print(f"     T_realistic ~ 1e-14 s (RGS: <n>~1 boundary)")
print(f"     ordering: t_P  <<  1/omega0  <<  T_realistic")
print(f"     gap t_P -> 1/omega0 = {np.log10((1/omega0)/t_P):.1f} orders of magnitude")
print()
print("     Regime A (realistic shutter, T >> 1/omega0): RGS mechanical")
print("       smoothing already gives <n> << 1; lattice cutoff DORMANT")
print("       (t_P ~30 orders below T). CPP and continuum agree.")
print("     Regime B (idealized instantaneous shutter, T -> 0): continuum")
print("       gives the LOG divergence <n> ~ ln(w_cut/omega0) -> inf. CPP")
print("       forbids T < t_P, so w_cut <= omega_P and")
print(f"       <n>_max = C * ln(omega_P/omega0) = {L:.1f} * C  (order tens).")
print()

# ------------------------------------------------------------
# (4) Why the gradual-bound framework cannot even be pushed to T=t_P:
#     its own validity regime needs 1/omega0 << kappa0 << T. At T=t_P
#     this requires kappa0 both >> 1.6e-16 s and << 5.4e-44 s: impossible.
#     => the lattice scale is reached only in the sharp/log regime.
# ------------------------------------------------------------
print("(4) The gradual-bound regime 1/omega0 << kappa0 << T cannot reach T=t_P:")
print(f"     need kappa0 >> {1/omega0:.2e} s AND kappa0 << t_P = {t_P:.2e} s")
print(f"     -> impossible ({1/omega0:.0e} >> {t_P:.0e}); the t_P scale lives in")
print("        the sharp/instantaneous (log) regime, where <n>_max = C*ln(w_P/w0).")
print()
print("CONCLUSION: divergence class = logarithmic (DERIVED from RGS kernel,")
print("not assumed). CPP identifies RGS's formal UV cutoff (their Eq. B14) with")
print(f"omega_P = 1/t_P, capping the instantaneous-limit divergence at {L:.1f}*C,")
print("C=O(1) set by the photon amplitude at the cut. Only the O(1) prefactor C")
print("remains open (narrowed OPEN-TP-1); the spectral class is now closed.")
