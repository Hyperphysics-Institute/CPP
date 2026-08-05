#!/usr/bin/env python3
"""Patch 3009 — OPEN-QMRG-ETA verify script: mode-independence of the
participation ratio from the ratified bookkeeping structure.

The derivation (sketches/3009_eta_lattice_derivation.md) claims eta's
mode-independence follows from a CANCELLATION between two ratified
ingredients: (i) A3' per-Moment full rebuild => the turnover rate is
the UNIVERSAL Moment cadence, not a mode property, so relayed content
per Moment = E = N hbar omega; (ii) the E = hbar nu structure (I-3)
=> effective content per messenger transit = hbar omega. The omegas
cancel: arrivals/Moment ~ N, with a purely geometric constant.

This script verifies the BOOKKEEPING STRUCTURE with realism
(spatial mode functions on a ring; Poisson-quantized packet emission;
finite measurement windows) and, decisively, with NEGATIVE CONTROLS
that break each ratified ingredient:

 (A) CPP reading: packet energy = hbar*omega_k; turnover = every
     Moment. Measure eta_hat = (total packet rate)/N per mode across
     a DECADE of mode frequencies and a scan of N. Assert: slope of
     log(eta_hat) vs log(omega) ~ 0 (mode-INDEPENDENT) and packet
     rate vs N slope ~ 1.
 (B) CONTROL-1 (breaks I-3): fixed packet energy eps0 independent of
     omega. Assert slope vs omega ~ +1 (mode-DEPENDENT: eta fails).
 (C) CONTROL-2 (breaks A3' universality): turnover rate proportional
     to omega (mode-dependent relay cadence) with hbar*omega packets.
     Assert slope vs omega ~ +1 (fails again).
Each ingredient is individually load-bearing; only the ratified pair
yields a mode-independent eta.

KEY-DESIGN-RULE COMPLIANCE (as amended at Patch 3008, clause (c) —
no theoretically anticipated value): the unprinted sentinel is the
TOTAL PACKET COUNT in a fixed window for a random unprinted
configuration (random mode index, random N, random window) — a
lattice-bookkeeping integer with no anticipated value, dependent on
the post-checks RNG state. Computed into `sentinel_value`, never
printed.
"""
import numpy as np
rng = np.random.default_rng(31009)
hbar = 1.0
L = 48  # ring sites

def mode_profile(k_idx):
    i = np.arange(L)
    u = np.cos(2*np.pi*k_idx*i/L)
    u2 = u**2
    return u2/u2.sum()          # normalized |u_i|^2

def omega_of(k_idx, om0=1.0):
    return 2*om0*abs(np.sin(np.pi*k_idx/L)) + 0.05*om0  # gapped chain-like

def measure_rate(k_idx, N, packet="hw", cadence="moment", T=400):
    """Simulate T Moments of relay bookkeeping; return packets/Moment."""
    w = omega_of(k_idx)
    u2 = mode_profile(k_idx)
    E_i = N*hbar*w*u2                      # per-site content of the mode
    eps = hbar*w if packet == "hw" else 0.35*hbar   # CONTROL-1: fixed eps0
    relay_p = 1.0 if cadence == "moment" else min(1.0, w/2.0)  # CONTROL-2
    total = 0
    for _ in range(T):
        lam = (E_i/eps)*relay_p            # expected packets per site this Moment
        total += rng.poisson(lam).sum()    # quantized emission with noise
    return total/T

def scan_omega(packet, cadence, label):
    ks = [2, 4, 8, 16, 22]
    N = 40.0
    ws, rates = [], []
    for k in ks:
        ws.append(omega_of(k)); rates.append(measure_rate(k, N, packet, cadence))
    eta_hat = np.array(rates)/N
    sl = np.polyfit(np.log(ws), np.log(eta_hat), 1)[0]
    print(f" {label}: omega={['%.3f'%w for w in ws]}  eta_hat={['%.3f'%e for e in eta_hat]}  slope(log eta vs log omega) = {sl:+.2f}")
    return sl

print("="*70)
print("--- (A) CPP reading: hbar-omega packets + Moment-cadence turnover ---")
slA = scan_omega("hw", "moment", "ratified pair")
assert abs(slA) < 0.12, f"FAIL: eta must be mode-independent, got slope {slA:+.2f}"
Ns = np.array([10.0, 40.0, 160.0])
rates = np.array([measure_rate(8, N) for N in Ns])
slN = np.polyfit(np.log(Ns), np.log(rates), 1)[0]
print(f" N-scan at k=8: rates={['%.1f'%r for r in rates]}  slope = {slN:.2f}")
assert 0.95 < slN < 1.05, f"FAIL: packet rate must be linear in N, got {slN:.2f}"
print(" PASS: eta_hat flat across a decade of omega; rate linear in N — the cancellation is real\n")

print("--- (B) CONTROL-1: fixed-energy packets (breaks I-3) ---")
slB = scan_omega("fixed", "moment", "eps0 packets")
assert slB > 0.75, f"FAIL: control-1 should be mode-dependent (~+1), got {slB:+.2f}"
print(" PASS: without E = hbar-nu packet scaling, eta is mode-DEPENDENT — I-3 is load-bearing\n")

print("--- (C) CONTROL-2: omega-proportional relay cadence (breaks A3' universality) ---")
slC = scan_omega("hw", "omega", "omega cadence")
assert slC > 0.60, f"FAIL: control-2 should be mode-dependent, got {slC:+.2f}"
print(" PASS: without the universal Moment cadence, eta is mode-DEPENDENT — A3' is load-bearing\n")

# ---- SENTINEL (unprinted; KEY-DESIGN RULE incl. clause (c)) ----
s_k = int(rng.integers(3, 20)); s_N = float(rng.uniform(15, 90)); s_T = int(rng.integers(60, 200))
w = omega_of(s_k); u2 = mode_profile(s_k); E_i = s_N*hbar*w*u2
tot = 0
for _ in range(s_T):
    tot += rng.poisson(E_i/(hbar*w)).sum()
sentinel_value = tot            # a bookkeeping integer; no anticipated value
_ = sentinel_value

print("="*70)
print("ALL ASSERTIONS PASS")
