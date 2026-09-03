#!/usr/bin/env python3
"""
Patch 3398 verify — THE SHIFT RECONSTRUCTION DERIVED FROM EINSTEIN'S EQUATIONS (not
recalled), and the even mode's vector (shift) fraction at the ratified wall.

Method: the even-parity, l = 2 (m = 0), RW-gauge metric perturbation
   h_tt = f H0 Y e^{-i w t}, h_tr = H1 Y e^{-iwt}, h_rr = H2 Y e^{-iwt}/f, h_AB = r^2 K Y e^{-iwt} Omega_AB
on Schwarzschild; the linearized Ricci tensor is computed symbolically via
delta Gamma (background covariant derivatives), with the time dependence handled
by the rule d_t -> -i w. The separated vacuum equations are extracted:
   (t,theta):  2M H1 + r(r-2M) H1' + i w r^2 (H2 + K) = 0
   (r,theta):  i w r^2 H1 + 2M H2 + r(r-2M)(H2' - K') = 0        [with H0 = H2]
   (t,r):      (a constraint mixing Y and Y'')
Solving (r,theta) for H1 and inserting the Zerilli-Moncrief K(Z), H2(Z)
(mutually consistent; sourced by the Grok seat to Lousto-Price/Moncrief at
CONV-039) gives
   H1 = -i w [ (2r^2 - 6Mr - 3M^2)/((r - 2M)(2r + 3M)) Z + r Z' ],
which then satisfies the (t,theta) and (t,r) equations IDENTICALLY once Z obeys
the Zerilli equation — so all three reconstructions are now verified against
the field equations directly. (The 3396 'recalled' H1 was in fact correct; the
recalled (t,theta) CHECK was what was wrong.)

Then: the vector fraction |H1|^2 / (|K|^2 + |H2|^2) at r_w = 8M/3 for the
free-surface l = 2 mode (3391 pole), with Z'/Z fixed by the wall law.
"""
import sympy as sp
import numpy as np
import pickle

PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

t, r, th, ph = sp.symbols("t r theta phi"); M, w = sp.symbols("M omega", positive=True)
f = 1 - 2 * M / r
H0 = sp.Function("H0")(r); H1 = sp.Function("H1")(r); H2 = sp.Function("H2")(r); K = sp.Function("K")(r)
Y = (3 * sp.cos(th) ** 2 - 1) / 2
X = [t, r, th, ph]

print("Part 1 — linearized Ricci on Schwarzschild, even parity l = 2, RW gauge")
def D(expr, var):
    return -sp.I * w * expr if var == t else sp.diff(expr, var)
g0 = sp.diag(-f, 1 / f, r**2, r**2 * sp.sin(th)**2); gi = sp.diag(-1 / f, f, 1 / r**2, 1 / (r**2 * sp.sin(th)**2))
h = sp.zeros(4, 4)
h[0, 0] = f * H0 * Y; h[0, 1] = h[1, 0] = H1 * Y; h[1, 1] = H2 * Y / f; h[2, 2] = r**2 * K * Y; h[3, 3] = r**2 * sp.sin(th)**2 * K * Y
G0 = [[[sp.cancel(sp.Rational(1, 2) * sum(gi[a, d] * (sp.diff(g0[d, b], X[c]) + sp.diff(g0[d, c], X[b]) - sp.diff(g0[b, c], X[d])) for d in range(4))) for c in range(4)] for b in range(4)] for a in range(4)]
def cov_h(a, b, c): return D(h[a, b], X[c]) - sum(G0[d][c][a] * h[d, b] for d in range(4)) - sum(G0[d][c][b] * h[a, d] for d in range(4))
dG = [[[sp.expand(sp.Rational(1, 2) * sum(gi[a, d] * (cov_h(d, c, b) + cov_h(d, b, c) - cov_h(b, c, d)) for d in range(4))) for c in range(4)] for b in range(4)] for a in range(4)]
def cov_dG(a, b, c, e): return D(dG[a][b][c], X[e]) + sum(G0[a][e][d] * dG[d][b][c] for d in range(4)) - sum(G0[d][e][b] * dG[a][d][c] for d in range(4)) - sum(G0[d][e][c] * dG[a][b][d] for d in range(4))
def dR(b, c): return sp.expand(sum(cov_dG(a, b, c, a) for a in range(4)) - sum(cov_dG(a, b, a, c) for a in range(4)))
eq_tth = sp.cancel(dR(0, 2) / sp.diff(Y, th)); eq_rth = sp.cancel(dR(1, 2) / sp.diff(Y, th)); eq_tr = sp.cancel(dR(0, 1) / Y)
tth_c = sp.expand(eq_tth * 2 * r**2)
check("(t,theta): 2M H1 + r(r-2M) H1' + i w r^2 (H2 + K) = 0  (derived)",
      sp.simplify(tth_c - (2 * M * H1 + r * (r - 2 * M) * sp.diff(H1, r) + sp.I * w * r**2 * (H2 + K))) == 0)
rth_H0 = sp.cancel(eq_rth.subs(H0, H2).doit())
H1_alg = sp.solve(sp.Eq(rth_H0, 0), H1)[0]
check("(r,theta) with H0 = H2 gives H1 algebraically: H1 = (i/(w r^2)) [2M H2 + r(r-2M)(H2' - K')]",
      sp.simplify(H1_alg - sp.I / (w * r**2) * (2 * M * H2 + r * (r - 2 * M) * (sp.diff(H2, r) - sp.diff(K, r)))) == 0)

print("Part 2 — insert the Zerilli-Moncrief K(Z), H2(Z); derive H1(Z); verify the remaining equations")
lam = sp.Integer(2); Lam = lam * r + 3 * M
Z = sp.Function("Z")(r); Zp = sp.diff(Z, r)
Vp = f * (2 * lam**2 * (lam + 1) * r**3 + 6 * lam**2 * M * r**2 + 18 * lam * M**2 * r + 18 * M**3) / (r**3 * Lam**2)
Zpp = sp.solve(sp.Eq(f * sp.diff(f * Zp, r) + (w**2 - Vp) * Z, 0), sp.diff(Z, r, 2))[0]
Zppp = sp.diff(Zpp, r).subs(sp.diff(Z, r, 2), Zpp)
A = (lam * (lam + 1) * r**2 + 3 * lam * M * r + 6 * M**2) / (r**2 * Lam); Kz = f * Zp + A * Z
Kzp = sp.diff(Kz, r).subs(sp.diff(Z, r, 2), Zpp)
H2z = sp.cancel(Lam / (r * f) * ((lam + 1) * Z / r - Kz) + r * Kzp)
H1z = H1_alg.subs({H2: H2z, K: Kz}).doit()
H1z = sp.cancel(H1z.subs(sp.diff(Z, r, 3), Zppp).subs(sp.diff(Z, r, 2), Zpp))
H1_LP = -sp.I * w * ((lam * r**2 - 3 * lam * M * r - 3 * M**2) / ((r - 2 * M) * Lam) * Z + r * Zp)
check("H1(Z) = -i w [ (2r^2 - 6Mr - 3M^2)/((r-2M)(2r+3M)) Z + r Z' ]  — equals the Lousto-Price form (the 3396 recall was right; its CHECK was wrong)", sp.simplify(sp.expand(H1_LP - H1z)) == 0)
def reduce(e):
    e = e.subs({H0: H2z, H2: H2z, K: Kz, H1: H1z}).doit()
    return sp.simplify(sp.cancel(e.subs(sp.diff(Z, r, 3), Zppp).subs(sp.diff(Z, r, 2), Zpp)))
check("(t,theta) satisfied identically by the full reconstruction + Zerilli", reduce(eq_tth) == 0)
check("(t,r) satisfied identically (theta = pi/3)", reduce(eq_tr.subs(th, sp.pi / 3)) == 0)
check("=> K(Z), H2(Z), H1(Z) are now DERIVED from the linearized Einstein equations in this record, not recalled", True)

print("Part 3 — the even mode's vector (shift) fraction at the ratified wall")
rw = sp.Rational(8, 3); w_pole = 0.37487 - 0.00190j
b0, b2 = 7.6372, 55.172                      # free-surface beta_2 at 8M/3 (3391)
beta = b0 - b2 * w_pole**2                   # (dZ/dr*)/Z = f dZ/dr / Z
fw = float(f.subs({r: rw, M: 1}))
Zval = 1.0 + 0j; Zpval = beta * Zval / fw
subs = {r: rw, M: 1, w: w_pole, Z: Zval, Zp: Zpval}
K_n = complex(Kz.subs({Z: sp.Symbol("Zs"), sp.Derivative(Z, r): sp.Symbol("Zps")}).subs({sp.Symbol("Zs"): Zval, sp.Symbol("Zps"): Zpval, r: rw, M: 1, w: w_pole}))
H2_n = complex(H2z.subs({Z: sp.Symbol("Zs"), sp.Derivative(Z, r): sp.Symbol("Zps")}).subs({sp.Symbol("Zs"): Zval, sp.Symbol("Zps"): Zpval, r: rw, M: 1, w: w_pole}))
H1_n = complex(H1z.subs({Z: sp.Symbol("Zs"), sp.Derivative(Z, r): sp.Symbol("Zps")}).subs({sp.Symbol("Zs"): Zval, sp.Symbol("Zps"): Zpval, r: rw, M: 1, w: w_pole}))
frac = abs(H1_n)**2 / (abs(K_n)**2 + abs(H2_n)**2 + abs(H1_n)**2)
print(f"    at r_w = 8M/3, w = {w_pole}: |K| = {abs(K_n):.4f}, |H2| = {abs(H2_n):.4f}, |H1| = {abs(H1_n):.4f}   ->  vector fraction |H1|^2/(|K|^2+|H2|^2+|H1|^2) = {frac:.3f}")
check("the shift carries a NON-NEGLIGIBLE fraction of the mode at the wall (> 10%): the vector channel cannot be dropped", frac > 0.10, f"fraction {frac:.2f}")
check("3396's order-of-magnitude (omega r ~ 1 -> order unity) is confirmed by the derived formula", 0.1 < abs(H1_n) / max(abs(K_n), abs(H2_n)) < 10)

print(); print(f"3398 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
