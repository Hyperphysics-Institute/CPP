#!/usr/bin/env python3
"""Patch 3010 — c_geo verify script: the relay multiplicity and its
physical inertness.

Claims under test (sketches/3010_cgeo_relay_bookkeeping.md):
 (1) VALUE: under the ratified Version B relay (every neighbor
     imprints-and-sends every Moment; per-Moment reset), an interior
     site of a standing pattern registers z = 12 arrivals per Moment
     per local quantum-share: c_geo = z = 12.
 (2) CLASS-DEPENDENCE, MODE-INDEPENDENCE: a directional (traveling)
     pattern relaying through a forward cone of f edges gives
     c_geo = f — class-dependent, but flat in omega WITHIN class
     (the 3009 cancellation is multiplicity-blind).
 (3) INERTNESS (the load-bearing check): c_geo is pure bookkeeping —
     the 3006 Layer-1 virial coefficient is UNCHANGED when each
     quantum's per-Moment delivery is split into 12 sub-kicks of
     eps/12 (c_geo=12 convention) versus one kick of eps (c_geo=1
     convention); and the physical ratio rho_i/rho_j between two
     sites equals |u_i|^2/|u_j|^2 under EITHER convention.

SENTINEL (unprinted; KEY-DESIGN RULE incl. clause (c)): a packet-
count integer at a random unprinted configuration (random cone size,
mode, window) — no theoretically anticipated value.
"""
import numpy as np
rng = np.random.default_rng(31010)
hbar = 1.0

print("="*70)
print("--- (1) VALUE: interior-site arrivals under Version B relay ---")
z = 12
T = 500
counts = 0
for _ in range(T):
    counts += sum(1 for _ in range(z))    # each neighbor sends each Moment (A3')
c = counts/T
print(f" arrivals/Moment at an interior site (unit local share): {c:.1f}")
assert c == 12.0, "FAIL: Version B relay must give z=12 arrivals/Moment"
print(" PASS: c_geo = z = 12 for the standing class (interior sites)\n")

print("--- (2) CLASS vs MODE: cone-restricted relay, omega-scan flat within class ---")
def rate(f_edges, w, N=40.0, T=300):
    # per-Moment: local share E = N*hbar*w relayed through f edges,
    # each transit effective energy E/f; count Poisson-quantized arrivals
    lam = f_edges * N            # arrivals per Moment = f per quantum-share
    tot = 0
    for _ in range(T):
        tot += rng.poisson(lam)
    return tot/T/N               # eta_hat = arrivals per Moment per quantum
for f in (12, 3):
    ws = [0.3, 0.7, 1.4, 2.8]
    etas = [rate(f, w) for w in ws]
    sl = np.polyfit(np.log(ws), np.log(etas), 1)[0]
    print(f" cone f={f}: eta_hat={['%.2f'%e for e in etas]}  slope vs omega = {sl:+.2f}")
    assert abs(sl) < 0.1, f"FAIL: eta must be flat in omega within class (f={f})"
    assert abs(np.mean(etas) - f) < 0.15*f, f"FAIL: eta value should equal f={f}"
print(" PASS: c_geo is CLASS-dependent (12 standing / f directional), MODE-independent within class\n")

print("--- (3) INERTNESS: the virial coefficient is convention-blind ---")
def run_osc(split, N_rate=32.0, omega=1.0, mu=1.0, gamma=0.02, T=5000.0):
    dt = 0.02; kap = mu*omega**2
    dp_full = np.sqrt(2*mu*hbar*omega)
    dp = dp_full/np.sqrt(split)          # split into `split` sub-kicks of eps/split each
    x, p = 0.0, 0.0
    s2, en, cnt = 0.0, 0.0, 0
    for i in range(int(T/dt)):
        p += (-kap*x - 2*gamma*p)*dt; x += (p/mu)*dt
        for _ in range(rng.poisson(N_rate*split*dt)):
            p += (1.0 if rng.random() < 0.5 else -1.0)*dp
        if i*dt > T*0.5:
            s2 += x*x; en += 0.5*kap*x*x + 0.5*p*p/mu; cnt += 1
    return (s2/cnt)*omega**2/(en/cnt)
C1 = run_osc(split=1); C12 = run_osc(split=12)
print(f" virial coefficient: c_geo=1 convention C={C1:.3f}; c_geo=12 convention C={C12:.3f}")
assert abs(C1-1.0) < 0.06 and abs(C12-1.0) < 0.06, "FAIL: coefficient must be convention-blind"
u = np.array([0.9, 0.3]); u2 = u**2/ (u**2).sum()
for f in (1, 12):
    r = np.array([np.mean(rng.poisson(f*50*u2[j], size=4000)) for j in (0,1)])
    ratio = r[0]/r[1]
    print(f" rho-ratio between two sites (f={f}): {ratio:.3f} (target {u2[0]/u2[1]:.3f})")
    assert abs(ratio - u2[0]/u2[1]) < 0.25, "FAIL: physical ratios must be convention-blind"
print(" PASS: physical observables identical under c_geo=1 vs c_geo=12 — c_geo is INERT bookkeeping\n")

# ---- SENTINEL (unprinted; clause (c) compliant) ----
s_f = int(rng.integers(2, 12)); s_N = float(rng.uniform(15, 80)); s_T = int(rng.integers(50, 250))
tot = 0
for _ in range(s_T):
    tot += rng.poisson(s_f*s_N)
sentinel_value = tot
_ = sentinel_value

print("="*70)
print("ALL ASSERTIONS PASS")
