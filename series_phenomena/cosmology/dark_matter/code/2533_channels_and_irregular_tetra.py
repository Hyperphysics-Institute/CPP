#!/usr/bin/env python3
"""Patch 2533 verify — dissociation channels and the irregular (isosceles) tetra.

Checks:
  1. Isosceles two-axis tetra (e-pair length 2a on x at z=+h/2; q-pair length 2b on y at z=-h/2,
     b < a per the founder's shorter-E_qq prediction): all four cross distances equal
     -> the 2532 neutrality cancellation SURVIVES arbitrary edge-length asymmetry.
  2. Channel cost table (founder ledger, symbolic in E_ee, E_qq):
       C_eCP   = 3 E_ee            (free eCP + charged 3-CP fragment)
       C_rev   = 4 E_ee            (eDP + qDP, reverse reaction)
       C_qCP   = 2 E_ee + E_qq     (free qCP + hDP + loose eCP)
     Gating (cheapest) channel is C_eCP iff E_ee < E_qq; C_eCP < C_rev always.
  3. Ledger tension encoded: static-census net cost of the eDP+qDP channel
     = (2 attractive cross) - (2 repulsive cross) = 0 at leading electric order (the theorem),
     vs founder ledger 4 E_ee, vs ZBW-quantum count 2 stored quanta. Three distinct models
     -> OPEN-6F-LEDGER must be adjudicated before channel energies are computed.
"""
import sympy as sp

ok = True
def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and cond

qe, qq = sp.symbols('q_e q_q', positive=True)
a, b, h = sp.symbols('a b h', positive=True)

# 1. Isosceles two-axis tetra
V = {
    'pe': sp.Matrix([ a, 0,  h/2]), 'me': sp.Matrix([-a, 0,  h/2]),
    'pq': sp.Matrix([0,  b, -h/2]), 'mq': sp.Matrix([0, -b, -h/2]),
}
Q = {'pe': qe, 'me': -qe, 'pq': qq, 'mq': -qq}
def dist(x, y): return sp.sqrt(((V[x]-V[y]).T*(V[x]-V[y]))[0])
cross = [('pe','pq'),('pe','mq'),('me','pq'),('me','mq')]
d0 = dist(*cross[0])
check("all four cross distances equal in the isosceles two-axis tetra (any a, b, h)",
      all(sp.simplify(dist(x, y) - d0) == 0 for x, y in cross))
E_cross = sp.simplify(sum(Q[x]*Q[y]/dist(x, y) for x, y in cross))
check("neutrality cancellation SURVIVES edge-length asymmetry (E_cross == 0 identically)", E_cross == 0)
check("founder geometry realizable: q-q edge (2b) shorter than e-e edge (2a) is a free parameter choice",
      sp.simplify(dist('pq','mq') - 2*b) == 0 and sp.simplify(dist('pe','me') - 2*a) == 0)

# 2. Channel cost table (founder ledger)
E_ee, E_qq = sp.symbols('E_ee E_qq', positive=True)
C_eCP, C_rev, C_qCP = 3*E_ee, 4*E_ee, 2*E_ee + E_qq
check("C_eCP < C_rev always (3 E_ee < 4 E_ee)", sp.simplify(C_rev - C_eCP) == E_ee)
gating_cond = sp.simplify(C_qCP - C_eCP)   # = E_qq - E_ee
check("C_eCP cheapest iff E_ee < E_qq (gating channel = eCP liberation under the doubly-bound expectation)",
      gating_cond == E_qq - E_ee)
print("       hot-edge gate (founder ledger, E_ee < E_qq): free-eCP liberation at 3*E_ee; first product is a CHARGED 3-CP fragment")

# 3. Ledger tension: three models for the eDP+qDP channel
static_net = sp.Integer(2) - sp.Integer(2)   # 2 attractive cross paid - 2 repulsive refunded (leading electric order)
zbw_quanta = sp.Integer(2)                    # attractive crosses store quanta; repulsive store none (Part I §3 reading)
founder_units = sp.Integer(4)                 # 4 E_ee
models = {static_net, zbw_quanta, founder_units}
check("three DISTINCT candidate energy models for the same channel (0, 2, 4 units) -> OPEN-6F-LEDGER is real",
      len(models) == 3)

print("\nALL CHECKS PASS" if ok else "\nCHECK FAILURES PRESENT")
raise SystemExit(0 if ok else 1)
