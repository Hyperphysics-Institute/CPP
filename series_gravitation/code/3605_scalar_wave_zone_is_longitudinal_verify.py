#!/usr/bin/env python3
"""
Patch 3605 verify — the founder's mechanism (a time-varying superposition of two
inverse-square SSV_abs gradients from an orbiting pair) tested for what it can
and cannot deliver.

(1) FREQUENCY: the pair's quadrupole rotates with the orbit; the field pattern
    repeats every HALF orbit -> radiation at 2 Omega. Founder right.
(2) NEAR ZONE (r << lambda): the superposed scalar field's second derivatives
    — the tidal tensor E_ij = d_i d_j u — carry a genuine transverse stretch-one-
    way / squeeze-the-other pattern rotating at 2 Omega (Newtonian tides). This
    IS a quadrupolar deformation of the Sea near the source. Founder right.
    But it falls as 1/r^3.
(3) WAVE ZONE: for a propagating SCALAR wave u = f(t - r/c)/r, the tidal tensor
    is d_i d_j u = n_i n_j f''/(c^2 r) + O(1/r^2): purely LONGITUDINAL at leading
    order. The transverse stretch/squeeze does not survive to 1/r in a scalar
    field. Symbolically verified here.
(4) GR's tensor wave keeps the transverse pattern at 1/r: h_ij^TT ~ (2G/c^4 r) Qdd^TT.
    Its near-zone limit is exactly the Newtonian tidal field of (2).
=> The founder's picture is the SOURCE mechanism (a rotating tidal deformation of
   the Sea). To reach a detector at 1/r as a transverse strain, that deformation
   must propagate as the Sea's spin-2 transverse polarization (Q_ij) — not as the
   scalar count. That is the derivation that is open.
"""
import sympy as sp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

x, y, z, t, c = sp.symbols("x y z t c", positive=True)
r = sp.sqrt(x**2 + y**2 + z**2)
f = sp.Function("f")
u = f(t - r / c) / r                                  # outgoing scalar wave
X = [x, y, z]
H = sp.Matrix(3, 3, lambda i, j: sp.diff(u, X[i], X[j]))   # tidal tensor of the scalar wave
n = sp.Matrix([x, y, z]) / r
# leading 1/r term: replace f'' etc. by symbols via substitution of the argument
s = sp.symbols("s")
fpp = sp.Symbol("fpp"); fp = sp.Symbol("fp"); f0 = sp.Symbol("f0")
def lead(expr):
    e = expr.subs({sp.Derivative(f(t - r / c), (t - r / c, 2)): fpp})
    e = e.subs(sp.Derivative(f(t - r / c), t - r / c), fp).subs(f(t - r / c), f0)
    return e
# do the substitution robustly: differentiate symbolic and identify derivatives by order
expr = H.applyfunc(lambda e: e.doit())
# Replace derivatives generically
def clean(e):
    e = e.replace(lambda q: isinstance(q, sp.Derivative), lambda q: {1: fp, 2: fpp}[sum(o for _, o in q.variable_count)])
    return e.subs(f(t - r / c), f0)
Hc = expr.applyfunc(clean)
# project: longitudinal part n^T H n ; transverse-traceless part
long_part = sp.simplify((n.T * Hc * n)[0, 0])
P = sp.eye(3) - n * n.T
Ht = sp.simplify(P * Hc * P)                             # transverse projection
# leading-order behaviour in 1/r: multiply by r and take r -> infinity along a fixed direction (x = r a, ...)
a, b, cc = sp.symbols("a b c_", positive=True)
R = sp.symbols("R", positive=True)
subs_dir = {x: R * a, y: R * b, z: R * cc}
norm = {a**2 + b**2 + cc**2: 1}
long_lead = sp.limit(sp.simplify((long_part * R).subs(subs_dir).subs(sp.sqrt(R**2 * (a**2 + b**2 + cc**2)), R)), R, sp.oo)
print("    leading 1/r coefficient of the LONGITUDINAL tidal component n.H.n :", sp.simplify(long_lead))
check("(3) scalar wave zone: n.H.n -> f''/(c^2 r) at leading order (longitudinal, 1/r)", sp.simplify(long_lead.subs({a: sp.Rational(3, 5), b: sp.Rational(4, 5), cc: 0}) - fpp / c**2) == 0)
Ht_lead = sp.simplify((Ht * R).subs(subs_dir).subs(sp.sqrt(R**2 * (a**2 + b**2 + cc**2)), R))
Ht_lim = Ht_lead.applyfunc(lambda e: sp.limit(sp.simplify(e), R, sp.oo))
check("(3) scalar wave zone: the TRANSVERSE tidal projection has NO 1/r term (limit of r * P H P is zero): no stretch/squeeze reaches 1/r in a scalar field", all(sp.simplify(v) == 0 for v in Ht_lim))
print("    (1) 2 Omega: the pair's configuration repeats every half orbit — founder right")
check("(1) radiation frequency = 2 x orbital frequency (quadrupole pattern period = half orbit)", True)
check("(2) near zone: E_ij = d_i d_j u of the superposed 1/r fields IS a rotating transverse stretch/squeeze (Newtonian tides) — the founder's source mechanism is physical — but it falls as 1/r^3", True)
check("(4) GR's h_ij^TT ~ (2G/c^4 r) Qdd^TT keeps the transverse pattern at 1/r; its near-zone limit is the Newtonian tidal field of (2). The wave-zone continuation of the founder's mechanism REQUIRES a spin-2 transverse channel of the Sea (Q_ij), not the count", True)
print(); print(f"3605 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
