#!/usr/bin/env python3
# ============================================================
# TP-1 verification — Patch 1700
# Lattice regularization of shutter-induced photon creation.
#
# Claim under test: the truncated-photon expected photon number <N>,
# which diverges in continuum QFT only in the instantaneous-shutter
# limit (Rukan-Gulla-Skaar, arXiv:2510.21636), is rendered FINITE by
# the CPP ultraviolet cutoff omega_cut <= omega_P = 1/t_P (QM-5 sec.7),
# and is bounded above for ALL physical shutters by a Planck-set
# ceiling <N>_max ~ kappa * ln(omega_P/omega_gamma).
#
# This script does NOT reproduce the RGS Bogoliubov kernel (that fixes
# the O(1) coefficient kappa and is OPEN-TP-1). It establishes the
# cutoff-regularization scaling and the numeric ceiling, which depend
# only on (a) the divergence being ultraviolet [RGS] and (b) CPP having
# a UV cutoff at 1/t_P [QM-5].
# ============================================================
import numpy as np

# --- Fundamental constants ---
t_P     = 5.391247e-44          # Planck time (s)  [CODATA]
c       = 2.99792458e8          # m/s
omega_P = 1.0 / t_P             # lattice UV cutoff = Planck angular frequency (rad/s)

# --- Representative optical photon (500 nm) ---
lam      = 500e-9
omega_g  = 2*np.pi*c/lam

print("="*60)
print("TP-1  Patch 1700  — truncation regularization")
print("="*60)
print(f"omega_P (= 1/t_P, lattice cutoff) = {omega_P:.4e} rad/s")
print(f"omega_g (optical, 500 nm)         = {omega_g:.4e} rad/s")
print(f"omega_P/omega_g                   = {omega_P/omega_g:.4e}")
L = np.log(omega_P/omega_g)
print(f"L = ln(omega_P/omega_g)           = {L:.3f}")
print(f"=> CPP ceiling  <N>_max ~ kappa*L = {L:.1f} * kappa   (order tens)")
print()

# ------------------------------------------------------------
# Mild (logarithmic) UV spectrum:  dN/dw = kappa / w  on [w_g, w_cut]
#   <N>(w_cut) = kappa * ln(w_cut / w_g)
# This is the divergence class consistent with the RGS qualitative
# statement that "even 1000 photons would be extremely unlikely"
# for realistic shutter speeds (a slow, logarithmic growth).
# ------------------------------------------------------------
def N_log(w_cut, kappa=1.0):
    return kappa*np.log(w_cut/omega_g)

print("Log model  <N>(w_cut), kappa=1:")
rows = [(1e16,"1e16"),(1e20,"1e20"),(1e30,"1e30"),
        (1e40,"1e40"),(omega_P,"omega_P (CPP cut)"),(1e60,"1e60"),(1e80,"1e80")]
for wc, lbl in rows:
    print(f"   w_cut={lbl:>18}: <N>={N_log(wc):7.2f}")
print("   continuum w_cut->inf : <N> -> +infinity (logarithmic, slow)")
print(f"   CPP value at the cut : <N>_max = {N_log(omega_P):.2f} * kappa")
print()

# ------------------------------------------------------------
# Shutter sharpness needed to reach N photons (log model):
#   w_cut ~ w_g * exp(N/kappa)   ->   tau_s ~ 1/w_cut
# Compare against the smallest physical switching time t_P.
# ------------------------------------------------------------
print("Shutter sharpness required to reach N photons (log model):")
for N in [10, 100, 1000]:
    for kappa in [1.0, 0.1]:
        expo = N/kappa
        if expo > 700:                      # float overflow guard
            w_need, tau_need = np.inf, 0.0
        else:
            w_need = omega_g*np.exp(expo)
            tau_need = 1.0/w_need
        flag = "  <-- requires tau_s < t_P : UNPHYSICAL (CPP forbids)" \
               if (tau_need < t_P) else ""
        print(f"   N={N:4d}, kappa={kappa}: tau_s~{tau_need:.2e} s{flag}")
print(f"   (smallest physical switching time = t_P = {t_P:.2e} s)")
print()

# ------------------------------------------------------------
# Robustness: a mild power-law spectrum dN/dw = kappa*(w_g/w)^p, 0<p<1
# also diverges as w_cut->inf and is finite once cut at omega_P.
# (Magnitude is strongly model-dependent; finiteness-under-cutoff is not.)
# ------------------------------------------------------------
def N_pow(w_cut, p, kappa=1.0):
    return kappa/(1-p)*((w_cut/omega_g)**(1-p) - 1)

print("Power-law model (p=0.5)  <N>(w_cut)/kappa  [robustness of finiteness]:")
for wc, lbl in [(1e20,"1e20"),(omega_P,"omega_P (CPP cut)"),(1e80,"1e80")]:
    print(f"   w_cut={lbl:>18}: ~{N_pow(wc,0.5):.3e} * kappa")
print()
print("CONCLUSION: any created-photon spectrum with unbounded UV support")
print("diverges as the shutter -> instantaneous (continuum); the CPP cut at")
print("omega_P = 1/t_P makes <N> finite for every physical shutter, with an")
print("optical-photon ceiling of order tens (log class). Coefficient kappa")
print("requires the RGS kernel cut at pi/l_P  -> OPEN-TP-1.")
