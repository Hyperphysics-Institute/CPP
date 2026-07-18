#!/usr/bin/env python3
"""Patch 2532 verify — the tetra neutrality-cancellation theorem.

Claims proved:
  1. Regular tetrahedron, vertices +e, -e, +q, -q (charges +qe, -qe, +qq, -qq symbolic, positive
     magnitudes): the four e-q cross edges' Coulomb sum vanishes IDENTICALLY (any qe, qq, edge length).
  2. Edge census at the symmetric point: 4 attractive, 2 repulsive (matches Part I §3).
  3. The cancellation is a property of the SYMMETRIC point only: at a generic asymmetric configuration
     (one vertex displaced), the cross sum is nonzero and can be repulsion-dominated — the barrier is a
     path property, consistent with the founder's activation picture.
  4. Consequence: DeltaE_b(eDP+qDP -> hTetra) at pure-electric, equal-length order is exactly the
     bond-repackaging term only (cross contribution = 0) — the reaction is near-threshold at leading order.
"""
import sympy as sp

ok = True
def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and cond

qe, qq, L = sp.symbols('q_e q_q L', positive=True)

# Regular tetra vertex coordinates (edge length L): scale (±1,±1,±1) alternating set by L/(2*sqrt2)
c = L / (2 * sp.sqrt(2))
V = {
    'pe': c * sp.Matrix([ 1,  1,  1]),   # +e
    'me': c * sp.Matrix([ 1, -1, -1]),   # -e
    'pq': c * sp.Matrix([-1,  1, -1]),   # +q
    'mq': c * sp.Matrix([-1, -1,  1]),   # -q
}
Q = {'pe': qe, 'me': -qe, 'pq': qq, 'mq': -qq}
def dist(a, b): return sp.sqrt(((V[a] - V[b]).T * (V[a] - V[b]))[0])

# All edges equal L
check("all six edges equal L (regular tetra)",
      all(sp.simplify(dist(a, b) - L) == 0 for a, b in
          [('pe','me'),('pq','mq'),('pe','pq'),('pe','mq'),('me','pq'),('me','mq')]))

# 1. Cross-edge Coulomb sum
cross_pairs = [('pe','pq'),('pe','mq'),('me','pq'),('me','mq')]
E_cross = sum(Q[a]*Q[b]/dist(a, b) for a, b in cross_pairs)
check("cross-interaction sum vanishes identically (neutrality x equal distances)", sp.simplify(E_cross) == 0)

# 2. Edge census
signs = {(a, b): sp.sign(Q[a]*Q[b]) for a, b in
         [('pe','me'),('pq','mq')] + cross_pairs}
attractive = sum(1 for v in signs.values() if v == -1)
repulsive = sum(1 for v in signs.values() if v == 1)
check(f"edge census: {attractive} attractive, {repulsive} repulsive (Part I §3)",
      attractive == 4 and repulsive == 2)

# 3. Asymmetric configuration: displace +e along the +e/+q direction by delta -> nonzero, repulsion-tilted
delta = sp.Rational(1, 5) * L
u = (V['pq'] - V['pe']) / dist('pe','pq')
V2 = dict(V); V2['pe'] = V['pe'] + delta * u
def dist2(a, b): return sp.sqrt(((V2[a] - V2[b]).T * (V2[a] - V2[b]))[0])
E_cross_asym = sp.simplify(sum(Q[a]*Q[b]/dist2(a, b) for a, b in cross_pairs))
val = sp.simplify(E_cross_asym.subs({qe: 1, qq: 1, L: 1}))
print(f"       asymmetric cross energy (qe=qq=L=1, delta=L/5): {sp.nsimplify(val, rational=False):.6f} > 0 (repulsion-dominated)"
      if val.is_number else "       symbolic")
check("cancellation fails off the symmetric point; displaced-toward-+q config is net repulsive (barrier = path property)",
      val.is_number and val > 0)

# 4. Consequence statement (structural, encoded): total tetra electric energy at the symmetric point
E_total = -qe*qe/L - qq*qq/L + E_cross   # eDP edge + qDP edge + cross(=0)
check("tetra electric energy = eDP bond + qDP bond at length L exactly (DeltaE_b is pure repackaging at this order)",
      sp.simplify(E_total - (-qe**2/L - qq**2/L)) == 0)

print("\nALL CHECKS PASS" if ok else "\nCHECK FAILURES PRESENT")
raise SystemExit(0 if ok else 1)
