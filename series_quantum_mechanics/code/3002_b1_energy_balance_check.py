#!/usr/bin/env python3
"""Patch 3002 — OPEN-QMRG-B1 verify script: the amplitude-count bridge
from elastic energy balance.

Toy model: one elastic Sea element = damped harmonic oscillator
(mass mu, stiffness kappa, natural omega = sqrt(kappa/mu), damping
gamma = per-Moment turnover), driven by N messenger kicks per unit
time, each a momentum increment delta-p.

CHECKS:
 (a) CYCLE-DISTRIBUTED kicks (arrival times uniform over the cycle —
     the P-3 temporal-synchrony reading: messengers sample the ZBW
     cycle, they are not phase-locked to one quadrature): each kick
     delivers fixed MEAN energy eps = dp^2/(2 mu); steady state
     <S^2> proportional to N  ->  log-log slope +1.
     THIS IS THE BRIDGE: intensity-like count (AP-2).
 (b) NEGATIVE CONTROL — PHASE-LOCKED kicks at the velocity quadrature
     (the rival 'coherent fixed-displacement-increment' reading):
     energy per kick grows with amplitude; steady state amplitude
     proportional to N  ->  <S^2> slope +2 (amplitude-like count,
     CONTRADICTING ratified AP-2's intensity clause).
 (c) MODE NORMALIZATION: with per-kick energy set to the mode quantum
     eps = hbar*omega, steady-state <S^2> proportional to
     N*hbar/(mu*omega)  ->  slope -1 vs omega. This RECOVERS the
     canonical 1/(2 omega) field normalization as an OUTPUT — the
     relation QM-5 presupposes is here predicted, not consumed
     (mutual-support prohibition honored).
 (d) ROBUSTNESS: elasticity-free statistical route — the planar sum of
     N cycle-distributed unit increments has <|S|^2> proportional to
     N (random-walk) — the same exponent from a second mechanism.
"""
import numpy as np
rng = np.random.default_rng(31002)

def steady_S2(N, omega, mu=1.0, gamma=0.05, dp=0.01, phase_locked=False,
              T=4000.0, dt=None, eps_quantum=None):
    if dt is None: dt = min(0.02, 0.02/omega)
    kap = mu*omega**2
    x, p = 0.0, 0.0
    # kick schedule: N kicks per unit time, Poisson-ish uniform
    n_steps = int(T/dt)
    kick_prob = N*dt
    acc, cnt = 0.0, 0
    if eps_quantum is not None:
        dp = np.sqrt(2*mu*eps_quantum)
    for i in range(n_steps):
        t = i*dt
        # damped oscillator, symplectic-ish Euler
        p += (-kap*x - 2*gamma*p)*dt
        x += (p/mu)*dt
        k = rng.poisson(kick_prob)
        for _ in range(k):
            if phase_locked:
                # kick along the instantaneous velocity direction (resonant quadrature)
                s = 1.0 if p >= 0 else -1.0
                p += s*dp
            else:
                # cycle-distributed: random sign = random arrival phase w.r.t. quadrature
                p += (1.0 if rng.random() < 0.5 else -1.0)*dp
        if t > T*0.5:
            acc += x*x; cnt += 1
    return acc/cnt

def slope(xs, ys, label):
    sl = np.polyfit(np.log(xs), np.log(ys), 1)[0]
    print(f" {label}: values={['%.3e'%v for v in ys]}  log-log slope = {sl:.2f}")
    return sl

print("="*70)
print("--- (a) BRIDGE: cycle-distributed kicks, <S^2> vs N ---")
Ns = np.array([2.0, 8.0, 32.0, 128.0])
ya = np.array([steady_S2(N, omega=1.0) for N in Ns])
sa = slope(Ns, ya, "cycle-distributed")
assert 0.85 < sa < 1.15, f"FAIL: expected slope ~1 (S^2 ~ N), got {sa:.2f}"
print(" PASS: <S^2> proportional to N — the intensity-like (AP-2) scaling\n")

print("--- (b) NEGATIVE CONTROL: phase-locked kicks, <S^2> vs N ---")
yb = np.array([steady_S2(N, omega=1.0, phase_locked=True) for N in Ns])
sb = slope(Ns, yb, "phase-locked")
assert 1.7 < sb < 2.3, f"FAIL: expected slope ~2 (S^2 ~ N^2), got {sb:.2f}"
print(" PASS: the rival amplitude-like reading requires quadrature phase-locking — slope 2, contradicting AP-2's intensity clause\n")

print("--- (c) MODE NORMALIZATION: eps = hbar*omega per kick, <S^2> vs omega at fixed N ---")
hbar = 1.0
oms = np.array([0.5, 1.0, 2.0, 4.0])
yc = np.array([steady_S2(N=32.0, omega=om, eps_quantum=hbar*om) for om in oms])
sc = slope(oms, yc, "omega-scan")
assert -1.3 < sc < -0.7, f"FAIL: expected slope ~-1 (S^2 ~ N hbar/(mu omega)), got {sc:.2f}"
print(" PASS: per-quantum displacement^2 ~ hbar/(mu omega) — the canonical 1/(2 omega) normalization RECOVERED as output\n")

print("--- (d) ROBUSTNESS: elasticity-free planar random-walk sum ---")
Nd = np.array([10, 100, 1000, 10000])
yd = []
for N in Nd:
    trials = 400
    tot = 0.0
    for _ in range(trials):
        th = rng.uniform(0, 2*np.pi, size=N)
        v = np.array([np.cos(th).sum(), np.sin(th).sum()])
        tot += v@v
    yd.append(tot/trials)
sd = slope(Nd.astype(float), np.array(yd), "random-walk")
assert 0.9 < sd < 1.1, f"FAIL: expected slope ~1, got {sd:.2f}"
print(" PASS: the statistical route gives the same exponent — two mechanisms, one scaling\n")
print("="*70)
print("ALL ASSERTIONS PASS")
