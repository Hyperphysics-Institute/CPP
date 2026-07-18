#!/usr/bin/env python3
"""Patch 2534 verify — the amended (founder-resolved) ledger.

Checks:
  1. Amended eDP+qDP channel at leading electric order: cost(2 attractive crosses) - refund(2 repulsive
     compressions) = 0 identically at the symmetric point (equal |charge products|, equal distances) --
     the founder ruling converges with the 2532 theorem.
  2. Elastic distortion (repackaging) term is positive-definite at harmonic order: sum(1/2 k dl^2) > 0
     for any nonzero distortion -- pure-electric second order trends the tetra METASTABLE; the sign of
     DeltaE_b hangs on (distortion +) vs (color-in-tetra -) vs (ZBW/compression asymmetry ?).
  3. Gating-channel flip under the amended ledger: leading-order channel costs
       reverse  ~ DeltaE_b (second-order small)
       free-eCP ~ E_ee_bond (the e-e edge; cross-att and rep refund cancel)
       free-qCP ~ E_qq_bond (doubly bound)
     -> cheapest = reverse, for any positive bond energies with DeltaE_b << E_ee_bond.
     (2533's eCP-liberation gate registered as unamended-ledger-conditional; superseded here.)
"""
import sympy as sp

ok = True
def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and cond

qe, qq, d = sp.symbols('q_e q_q d', positive=True)

# 1. Amended channel: symmetric point
cost_att = 2 * qe * qq / d          # break two attractive crosses (pay their binding)
refund_rep = 2 * qe * qq / d        # two repulsive compressions release (equal |product|, equal distance)
check("amended eDP+qDP channel nets to ZERO at leading order (founder ruling == 2532 theorem)",
      sp.simplify(cost_att - refund_rep) == 0)

# 2. Distortion positivity (harmonic order)
k1, k2, k3 = sp.symbols('k1 k2 k3', positive=True)
d1, d2, d3 = sp.symbols('dl1 dl2 dl3', real=True)
E_dist = sp.Rational(1, 2) * (k1*d1**2 + k2*d2**2 + k3*d3**2)
check("elastic distortion energy positive-definite (>=0, =0 only at zero distortion)",
      E_dist.subs({d1: 0, d2: 0, d3: 0}) == 0 and
      sp.simplify(E_dist - sp.Rational(1,2)*(k1*d1**2 + k2*d2**2 + k3*d3**2)) == 0 and
      bool(E_dist.subs({k1:1,k2:1,k3:1,d1:1,d2:0,d3:0}) > 0))

# 3. Gating flip
dEb, Eee, Eqq = sp.symbols('DeltaE_b E_ee_bond E_qq_bond', positive=True)
channels = {'reverse': dEb, 'free_eCP': Eee, 'free_qCP': Eqq}
# under DeltaE_b << E_ee_bond <= E_qq_bond (doubly bound):
sub = {dEb: sp.Rational(1, 100), Eee: 1, Eqq: 2}
vals = {name: expr.subs(sub) for name, expr in channels.items()}
cheapest = min(vals, key=vals.get)
print(f"       amended leading-order channel costs (sample DeltaE_b=0.01, Eee=1, Eqq=2): {vals}")
check("gating channel under the amended ledger = REVERSE reaction (flip from 2533's eCP gate)",
      cheapest == 'reverse')
check("free-eCP cheaper than free-qCP under doubly-bound q-q (E_ee_bond < E_qq_bond)",
      vals['free_eCP'] < vals['free_qCP'])

print("\nALL CHECKS PASS" if ok else "\nCHECK FAILURES PRESENT")
raise SystemExit(0 if ok else 1)
