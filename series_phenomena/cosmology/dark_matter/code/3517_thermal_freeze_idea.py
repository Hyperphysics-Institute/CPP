#!/usr/bin/env python3
"""Patch 3517 — an IDEA, checked, not a reading: if the lone-qCP residue is a THERMAL freeze (pair ⇌ two lone charges;
the founder's 'does not go to completion because of the violence of thermal collisions') rather than a dilution-only
freeze, what exponent p follows?  Toy Boltzmann in comoving density n_c = n a³:
    dn_c/dt = −k a⁻³ (n_c² − n_eq,c²),   n_eq² = K(T)·n_pair,  K = exp(−E_b/kT),  n_pair ≈ n_q/2,
with kT = E_b·exp(−t/τ) and a = exp(t/τ): the same τ cools and dilutes (τ in units of the pairing time 1/(k n_q)).
p = d ln n_c,∞ / d ln n_q at fixed τ (composition mode: n_q perturbed, T and a not)."""
import math
ok=[]
def T(n,c,m): ok.append(c); print(("PASS " if c else "FAIL ")+n+": "+m)
def relic(nq, tau, k=1.0, dt=None):
    n = math.sqrt(math.exp(-1.0)*nq/2); t = 0.0; dt = dt or min(1e-2, tau/200)
    while t < 40*tau:
        kT = math.exp(-t/tau); a3 = math.exp(3*t/tau)
        neq2 = (math.exp(-1.0/kT) if kT > 5e-3 else 0.0)*nq/2*a3          # n_eq,c² = K·(n_q/2)/a³ · a⁶ (pairs dilute too)
        rate = k/a3*(n*n - neq2); step = dt
        if abs(rate)*step > 0.1*max(n,1e-30): step = 0.1*max(n,1e-30)/abs(rate)
        n -= step*rate; t += step
        if n < 1e-300: break
    return n
def p_of(tau, d=0.05):
    a, b = relic(math.exp(d), tau), relic(math.exp(-d), tau)
    return (math.log(a)-math.log(b))/(2*d)
print("  expansion/cooling time τ (in pairing times) → p:")
res = {}
for tau in [0.03, 0.3, 3, 30, 100, 300, 1000, 3000]:
    res[tau] = p_of(tau); print(f"    τ = {tau:6.2f}: p = {res[tau]:.3f}  {'IN BAND' if 0.209<=res[tau]<=0.480 else ''}")
T("T1", abs(res[0.03]-0.5) < 0.03, "fast expansion (τ ≪ pairing time): the equilibrium population at kT ≈ E_b is frozen in — p = 1/2, the Saha stoichiometry n_lone² ∝ n_pair ∝ n_q, kernel-independent")
T("T2", res[3000] < res[300] < res[30], f"slow expansion (τ ≫ pairing time): standard freeze-out — the comoving relic depends on n_q only through the freeze time (logarithmically), so p falls toward 0, slowly: p = {res[30]:.2f}, {res[300]:.2f}, {res[3000]:.2f} at τ = 30, 300, 3000")
inb = [tau for tau,p in res.items() if 0.209 <= p <= 0.480]
T("T3", len(inb) > 0, f"the D1 band [0.21, 0.48] is crossed for τ ≈ {min(inb)}–{max(inb)} pairing times: the band is reached only when the expansion is SLOWER than pairing by a few hundred to a few thousand times — the opposite regime from the dilution-only freeze of 3512, which needed a quench")
print(f"{sum(1 for c in ok if c)}/{len(ok)} pass")
