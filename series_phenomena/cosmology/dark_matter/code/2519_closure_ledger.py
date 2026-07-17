#!/usr/bin/env python3
"""Patch 2519 verify: the closure theorem + common-precursor consistency checks + S3 target.

Closure: with initial per-species sign symmetry and CP conservation, solve the four
species-sign ledger equations symbolically; show the Sea's sign-balanced content and
n_ring drop out, forcing hDP-B excess = 2 n_b and free -qCP = 1 n_b.
"""
from sympy import symbols, Eq, solve

n_b, n_r, Q, E = symbols('n_b n_r Q E', positive=True)          # baryons, rings, initial +q(=-q), +e(=-e)
P, L, h, a, b, c = symbols('P L h a b c', nonnegative=True)     # Sea qDP, eDP, hTetra, hDP-A, hDP-B, free -qCP

# Gross per-baryon neutral-matter content (S1): 4 +q, 1 -q, 1 +e, 3 -e (uud + hTetra scaffold + electron)
eq_pq = Eq(4*n_b + 32*n_r + P + h + a, Q)        # +qCP ledger
eq_mq = Eq(1*n_b + 32*n_r + P + h + b + c, Q)    # -qCP ledger
eq_pe = Eq(1*n_b + 32*n_r + L + h + b, E)        # +eCP ledger
eq_me = Eq(3*n_b + 32*n_r + L + h + a, E)        # -eCP ledger

sol = solve([eq_pq, eq_mq, eq_pe, eq_me], [b, c, Q, E], dict=True)[0]
assert sol[b] == a + 2*n_b, sol
assert sol[c] == n_b, sol
print(f"FORCED: hDP-B excess b - a = {sol[b] - a};  free -qCP c = {sol[c]}")
print("n_r absent from both -> rings asymmetry-blind at ledger level (confirms S1)")

# Charge balance of the forced reservoirs: hDP-B charge +1/3 each, cloud qCP -2/3 each
from fractions import Fraction
q_reservoirs = Fraction(1, 3) * 2 + Fraction(-2, 3) * 1   # per baryon
assert q_reservoirs == 0
print("reservoir charge per baryon: 2*(+1/3) + 1*(-2/3) = 0  (globally neutral, locally separated)")

# Founder total-conversion sub-scenario: N(+q)=N(-e)=Q0, all +q into baryons
Q0 = symbols('Q0', positive=True)
nb2 = Q0 / 3                                   # 3 +q per baryon
minus_e_left = Q0 - 2*nb2                      # 2 -e consumed per baryon
plus_e_left, minus_q_left = Q0, Q0             # untouched species (E0 = Q0 assumed by founder)
edp = minus_e_left                             # leftover -e pair into eDPs with +e
b_hdp = plus_e_left - edp                      # remaining +e bind -q as hDP-B
clouds = minus_q_left - b_hdp
assert b_hdp == 2*nb2 and clouds == nb2
print("total-conversion framing: same sinks, same magnitudes (2 n_b, 1 n_b) -> framing-independent")

# Common-precursor consistency: hTetra = hDP-A + hDP-B
htetra = {'+q': 1, '-q': 1, '+e': 1, '-e': 1}
element = {k: 4*v for k, v in htetra.items()}
assert element == {'+q': 4, '-q': 4, '+e': 4, '-e': 4}          # 2435: 4+/4- in both species
m_htetra = 2*132 + 2*44
assert 4*m_htetra == 1408                                        # registered element mass, exact
ring = {k: 8*v for k, v in element.items()}
assert ring == {'+q': 32, '-q': 32, '+e': 32, '-e': 32}
print(f"element = 4 hTetras: composition OK, mass 4*{m_htetra} = 1408 MeV OK, ring = 32 hTetras OK")

# S3 target in precursor terms
T1, sT1 = 0.4468, 0.0054
ratio, sratio = 32*T1, 32*sT1
frac = ratio / (ratio + 1)
print(f"S3 target: ring-bound/baryon-bound hTetras = {ratio:.2f} +/- {sratio:.2f} "
      f"({100*frac:.2f}% ring-bound); D-strong ratio window [{32*0.436:.2f}, {32*0.458:.2f}]; "
      f"D-directional [{32*0.30:.1f}, {32*0.67:.1f}]")
print("ALL CHECKS PASS")
