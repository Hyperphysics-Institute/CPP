#!/usr/bin/env python3
"""
3259_fterm_reconciliation_verify.py — resolution of OPEN-GR-FE1-FTERM.

Establishes, symbolically and exactly (sympy), the reconciliation of the
Patch-3258 HALT finding:

  C1  The log-lapse N = ln((1-p)/(1+p)) = ln sqrt(-g_tt/c^2) is EXACTLY
      Box_g-harmonic on the exact isotropic Schwarzschild background
      (generic branch; the Eq(a,2r) Piecewise branch is the
      horizon-coordinate surface, measure zero, noted).
  C2  The corrected compensator: Box_g(Dssv) + F_true = 0 EXACTLY, with
          F_true = (k^2 Dssv / 2)/(1 - (k Dssv/2)^2) * |grad Dssv|_g^2 .
      Structure: O(u) * (grad u)^2 — NOT the stated GR-1c O(u^2) * Box ln
      form.
  C3  THE EQUIVALENCE (radial, generic non-harmonic v): with the metric
      built pointwise from v,
          Box_g atanh(k v/2) = [32 k / ((2-kv)(2+kv)^5)] * flatLap v .
      Pure algebraic factor, no derivative terms => Box_g phi = 0 iff
      flatLap v = 0 (kv != 2): the measured-frame log-lapse equation and
      the lattice-frame flat Laplace equation are THE SAME EQUATION.
  C4  FULL-3D coefficient identity: for pointwise A(u), B(u) and
      f = atanh(k u/2),   f''/f' + d/du ln( sqrt(A) B^(1/2) ) = 0 ,
      which is the necessary and sufficient condition for
      Box_g f(u) = [f'(u)/B(u)] flatLap u in three dimensions with no
      spherical assumption (all (grad u)^2 terms cancel identically).
  C5  Weak field: phi'(0) = k/2 and N = -k u + O(u^3): linearised
      consistency with the Patch-3258 normalisation.
  C6  Localisation of the GR-1c sketch slip: the radial identity
      Box ln(1+k u) = k Box u/(1+ku) - k^2 (grad u)^2/(1+ku)^2 shows the
      sketch's building block DOES contain the (grad u)^2 structure, but
      the stated prefactor 2k u^2/(1+ku)^2 carries one power of u too
      many: leading orders O(u^2)*(grad u)^2 (stated) vs O(u)*(grad u)^2
      (required). No constant rescaling can repair it.

All claims exact-symbolic except where series orders are the claim.
"""
import sympy as sp

PASS = []
def check(name, ok, detail=""):
    PASS.append(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))

r, a, k = sp.symbols('r a k', positive=True)
p = a/(2*r)
u = a/(k*r)                                  # exact profile: k u = 2 p
A = ((1-p)/(1+p))**2; B = (1+p)**4
sqrtg = sp.sqrt(A)*B**sp.Rational(3,2)*r**2
def Box(f):
    return sp.piecewise_fold(sp.cancel(sp.together(
        sp.diff(sqrtg*(1/B)*sp.diff(f, r), r)/sqrtg)))
def generic(expr):
    """Extract the generic (a != 2r) branch of a Piecewise, else identity."""
    e = sp.simplify(expr)
    if isinstance(e, sp.Piecewise):
        for val, cond in e.args:
            if cond == True:
                return sp.simplify(val)
    return e

print("== C1: log-lapse exactly Box_g-harmonic ==")
N = sp.log((1-p)/(1+p))
c1 = generic(Box(N))
check("Box_g ln((1-p)/(1+p)) == 0 (generic branch)", c1 == 0, f"residual: {c1}")

print("== C2: corrected compensator exact ==")
Ftrue = (k**2*u/2)/(1-(k*u/2)**2) * (1/B)*sp.diff(u, r)**2
c2 = generic(Box(u) + Ftrue)
check("Box_g u + F_true == 0 (exact)", c2 == 0, f"residual: {c2}")

print("== C3: the equivalence identity (generic v, radial) ==")
v = sp.Function('v')(r)
pv = k*v/2
Av = ((1-pv)/(1+pv))**2; Bv = (1+pv)**4
sqrtgv = sp.sqrt(Av)*Bv**sp.Rational(3,2)*r**2
phiv = sp.atanh(k*v/2)
Boxv_phi = sp.cancel(sp.together(sp.diff(sqrtgv*(1/Bv)*sp.diff(phiv, r), r)/sqrtgv))
flat_lap_v = sp.cancel(sp.together(sp.diff(r**2*sp.diff(v, r), r)/r**2))
ratio = sp.simplify(sp.cancel(Boxv_phi/flat_lap_v))
target = 32*k/((2 - k*v)*(2 + k*v)**5)
check("Box_g atanh(kv/2) / flatLap v == 32k/((2-kv)(2+kv)^5) — pure algebraic",
      sp.simplify(ratio - target) == 0, f"ratio = {ratio}")
w = sp.symbols('w')
poly = sp.expand((w-2)*(w+2)**5)
check("factorisation (kv-2)(kv+2)^5 of the denominator polynomial",
      sp.expand(poly - (w**6 + 8*w**5 + 20*w**4 - 80*w**2 - 128*w - 64)) == 0)

print("== C4: full-3D coefficient identity (no spherical assumption) ==")
uu = sp.symbols('u_')
pA = ((1 - k*uu/2)/(1 + k*uu/2))**2
pB = (1 + k*uu/2)**4
f = sp.atanh(k*uu/2)
lhs = sp.diff(f, uu, 2)/sp.diff(f, uu)
rhs = -sp.diff(sp.log(sp.sqrt(pA)*sp.sqrt(pB)), uu)
c4 = sp.simplify(lhs - rhs)
check("f''/f' + d/du ln(sqrt(A) B^(1/2)) == 0  (=> 3D equivalence)",
      c4 == 0, f"residual: {c4}")

print("== C5: weak field ==")
phi_u = sp.atanh(k*uu/2)
c5a = sp.simplify(sp.diff(phi_u, uu).subs(uu, 0) - k/2) == 0
Nser = sp.series(sp.log((1 - k*uu/2)/(1 + k*uu/2)), uu, 0, 3).removeO()
c5b = sp.simplify(Nser + k*uu) == 0
check("phi'(0) = k/2 and N = -k u + O(u^3) (linearised consistency)", c5a and c5b,
      f"N series = {Nser}")

print("== C6: localisation of the GR-1c sketch slip ==")
# radial identity for the sketch's building block:
lnT = sp.log(1 + k*v)
lhs6 = sp.cancel(sp.together(sp.diff(r**2*sp.diff(lnT, r), r)/r**2))
rhs6 = sp.cancel(sp.together(k*flat_lap_v/(1 + k*v) - k**2*sp.diff(v, r)**2/(1 + k*v)**2))
check("Box ln(1+kv) == k Box v/(1+kv) - k^2 (v')^2/(1+kv)^2 (flat radial identity)",
      sp.simplify(lhs6 - rhs6) == 0)
# leading orders on the exact profile: stated prefactor vs required prefactor
pref_stated = 2*k*u**2/(1 + k*u)**2      # literal GR-1c prefactor
pref_required = (k**2*u/2)/(1 - (k*u/2)**2)
lo_stated = sp.degree(sp.numer(sp.cancel(sp.series(pref_stated, a, 0, 4).removeO().as_poly(a).as_expr())), a) if True else None
s_st = sp.expand(sp.series(pref_stated, a, 0, 4).removeO())
s_rq = sp.expand(sp.series(pref_required, a, 0, 4).removeO())
lo_st = min([n for n in range(0, 5) if sp.simplify(s_st.coeff(a, n)) != 0])
lo_rq = min([n for n in range(0, 5) if sp.simplify(s_rq.coeff(a, n)) != 0])
check("stated prefactor is O(u^2)-class (a^2) vs required O(u)-class (a^1): one power of u too many",
      lo_st == 2 and lo_rq == 1, f"stated leading a^{lo_st}, required a^{lo_rq}")

print(f"\n{sum(PASS)}/{len(PASS)} checks pass")
raise SystemExit(0 if all(PASS) else 1)
