#!/usr/bin/env python3
"""Patch 3513 — pressure flag only, NOT a D1 reading: if the naked-qCP residue is the knock-off yield from
trios/extras (founder, 12 Sep) and the trio inventory is set by ONE Poisson landing at the count law's end
(per-GP q-occupancy 2λ, λ = q_local·½ per sign, so δ ln λ = δ ln n_q at fixed total), what exponent does the
landing statistics alone give?  No dynamics, no knock-off rate, no repulsive-era dilution — all three are open."""
import math
ok=[]
def T(n,c,m): ok.append(c); print(("PASS " if c else "FAIL ")+n+": "+m)
def pois(k,m): return math.exp(-m)*m**k/math.factorial(k)
def extras(lam):            # captured CPs beyond a pair, per GP, for total Poisson mean 2λ; mixed-sign requirement dropped (upper bound on the count, exponent barely affected)
    m=2*lam; return sum((k-2)*pois(k,m) for k in range(3,40))
def trios(lam):             # exactly three, mixed sign (3/4 of sign assignments)
    return 0.75*pois(3,2*lam)
def slope(f,lam,d=1e-3): return (math.log(f(lam*math.exp(d)))-math.log(f(lam*math.exp(-d))))/(2*d)
p3=slope(trios,0.5); pe=slope(extras,0.5)
print(f"  at λ = ½ per sign (n̄ = 1, q = ½): trio-only exponent = {p3:.3f} (analytic 3 − 2λ = {3-1.0:.1f}); all-extras exponent = {pe:.3f}")
T("T1", abs(p3-2.0)<1e-3, "trio inventory from one Poisson landing scales as n_q^2 at the count law's end — the naive knock-off reading sits ABOVE the band on the p = 1 side, worse than the p = 1 endpoint (3936: fails ~5×)")
T("T2", pe>1.5, f"counting every captured extra (third, fourth, …) as knock-off feedstock gives p = {pe:.2f}: still super-linear")
for lam in [0.05,0.1,0.2,0.5,1.0]: print(f"    λ = {lam}: trio exponent {slope(trios,lam):.2f}, extras exponent {slope(extras,lam):.2f}")
T("T3", slope(trios,0.05)>2.5, "and lower freeze occupancy makes it MORE super-linear (→ 3): landing statistics cannot deliver the band; if the founder's knock-off picture is right, the band must come from the DYNAMICS — how long the repulsive era keeps trios forming and breaking before the freeze — which is the unregistered rate")
print(f"{sum(1 for c in ok if c)}/{len(ok)} pass")
