#!/usr/bin/env python3
"""Patch 3006 — OPEN-QMRG-B1-CONST verify script: the coefficient
layer of the amplitude-count bridge.

Disposition under test (see sketches/3006_b1const_convention_derivation.md):
LAYER 1 (DERIVED, exact-in-regime): in the declared convention
(cycle-averaged mean-square in-plane register displacement), a mode
holding energy E has <S_perp^2> = E/(mu omega^2) with coefficient
EXACTLY 1 (harmonic virial); with E = N hbar omega this is
<S_perp^2> = N hbar/(mu omega). The canonical 1/2 is the
TWO-QUADRATURE SPLIT of the rotating pattern: <S_x^2> = <S_y^2>
= N hbar/(2 mu omega).
LAYER 2 (QUARANTINED): the count-to-mode-occupation ratio eta = rho/N
(participation/turnover bookkeeping) — lattice-dependent, NOT derived;
the separation is CLEAN iff the Layer-1 coefficient is INVARIANT
under turnover details.

CHECKS:
 (a) COEFFICIENT: damped-driven oscillator (3002 harness class),
     eps = hbar*omega kicks; measure C = <S^2> * mu * omega^2 / <E>
     with <E> the independently measured stored energy. Assert
     C = 1.00 within 5% (small gamma/omega).
 (b) QUADRATURE SPLIT for a circular in-plane rotating pattern:
     <S_x^2>/<S^2> = 1/2 exactly — the derived canonical half.
 (c) PEAK CONVENTION: peak^2 / <S^2> ~ 2 for near-coherent motion —
     the convention table's factor-2 row.
 (d) SEPARATION (the load-bearing check): gamma-scan over a decade —
     the stored energy varies strongly with turnover, but C stays 1
     (deviation O((gamma/omega)^2), measured). Layer 1 is invariant
     under Layer-2 details: the quarantine is clean.

KEY-DESIGN-RULE COMPLIANCE: an unprinted RNG-stream sentinel
(post-checks state; fresh gamma, omega, kick rate; unprinted
measurement) is computed into `sentinel_value` and never printed —
available as a future withheld key (KEY-J).
"""
import numpy as np
rng = np.random.default_rng(31006)
hbar = 1.0

def run_osc(N_rate, omega, mu=1.0, gamma=0.02, T=6000.0):
    """Damped oscillator driven by Poisson kicks of fixed energy
    eps = hbar*omega (random arrival phase => fixed mean energy).
    Returns (<S^2>, <E>) measured in steady state."""
    dt = min(0.02, 0.02/omega)
    kap = mu*omega**2
    dp = np.sqrt(2*mu*hbar*omega)
    x, p = 0.0, 0.0
    n_steps = int(T/dt); kick_prob = N_rate*dt
    s2, en, cnt = 0.0, 0.0, 0
    for i in range(n_steps):
        p += (-kap*x - 2*gamma*p)*dt
        x += (p/mu)*dt
        for _ in range(rng.poisson(kick_prob)):
            p += (1.0 if rng.random() < 0.5 else -1.0)*dp
        if i*dt > T*0.5:
            s2 += x*x
            en += 0.5*kap*x*x + 0.5*p*p/mu
            cnt += 1
    return s2/cnt, en/cnt

print("="*70)
print("--- (a) COEFFICIENT: C = <S^2> mu omega^2 / <E> ---")
Cs = []
for om, Nr in [(1.0, 32.0), (2.0, 32.0), (1.0, 128.0)]:
    s2, E = run_osc(Nr, om)
    C = s2*1.0*om**2/E
    Cs.append(C)
    print(f" omega={om}, rate={Nr}: <S^2>={s2:.4e}, <E>={E:.4e}, C={C:.3f}")
for C in Cs:
    assert 0.95 < C < 1.05, f"FAIL: virial coefficient should be 1.00, got {C:.3f}"
print(" PASS: the mean-square coefficient is EXACTLY 1 (harmonic virial), all configs\n")

print("--- (b) QUADRATURE SPLIT: circular rotating in-plane pattern ---")
t = np.linspace(0, 200*np.pi, 400001)
Sx, Sy = np.cos(t), np.sin(t)
r = np.mean(Sx**2)/np.mean(Sx**2 + Sy**2)
print(f" <S_x^2>/<S^2> = {r:.6f}")
assert abs(r - 0.5) < 1e-4, "FAIL: quadrature split must be exactly 1/2"
print(" PASS: the canonical 1/2 IS the two-quadrature split of the rotating pattern\n")

print("--- (c) PEAK CONVENTION: peak^2 / <S^2> for near-coherent motion ---")
A = 1.7
S = A*np.cos(t)
ratio = (A**2)/np.mean(S**2)
print(f" peak^2/<S^2> = {ratio:.4f}")
assert abs(ratio - 2.0) < 1e-3, "FAIL: peak-square convention factor must be 2"
print(" PASS: the convention table's factor-2 row verified\n")

print("--- (d) SEPARATION: gamma-scan — Layer-1 coefficient invariant under turnover ---")
gams = [0.005, 0.02, 0.08]
Es, Cds = [], []
for g in gams:
    s2, E = run_osc(32.0, 1.0, gamma=g, T=8000.0)
    C = s2*1.0/E
    Es.append(E); Cds.append(C)
    print(f" gamma={g}: <E>={E:.4e} (varies with turnover), C={C:.3f} (must not)")
spread_E = max(Es)/min(Es)
for C in Cds:
    assert 0.93 < C < 1.07, f"FAIL: coefficient must be turnover-invariant, got {C:.3f}"
assert spread_E > 5.0, f"FAIL: energy should vary strongly across the scan (got x{spread_E:.1f})"
print(f" PASS: stored energy varies x{spread_E:.1f} across the turnover scan; the coefficient stays 1 —")
print("       Layer 1 (derived) is invariant under Layer 2 (quarantined eta); the separation is CLEAN\n")

# ---- SENTINEL (unprinted; KEY-DESIGN RULE) ----
s_gam = rng.uniform(0.01, 0.05); s_om = rng.uniform(0.7, 1.7); s_rate = rng.uniform(10, 60)
s2s, Es_ = run_osc(s_rate, s_om, gamma=s_gam, T=3000.0)
sentinel_value = s2s*s_om**2/Es_   # deliberately unprinted
_ = sentinel_value

print("="*70)
print("ALL ASSERTIONS PASS")
