#!/usr/bin/env python3
"""Patch 2313 -- G1 reduction audit: independent recompute of the load-bearing identities.

Re-executes (independently of the 1107/1108 scripts) the three facts the audit rests on:
  (1) icosahedral monopole annihilation: Sum v_hat = 0 exactly (odd/central symmetry; 5-design)
      -> the absolute-|SSV| term (any uniform ground-state value, however large) contributes
         nothing to the first-moment (displacement) response;
  (2) isotropic quadrupole: Sum v_hat (x) v_hat = 4*I exactly -> continuum operator = Laplacian
      acting on Delta|SSV| alone;
  (3) 1107 route closures: (b1) the nonlinear source prefactor 2k D^2/(1+kD)^2 is O(D^2)
      (pure excess; vanishes with all first derivatives at D=0); (b2) R = 2(-Om*Om'' + Om'^2)/Om^4
      vanishes for constant Om (uniform absolute |SSV| = flat background).
Demonstration (4): a uniform field of magnitude 1e42 (the portrait's budget ceiling in rho_Lambda
units) times the shell monopole = 0 to machine precision -- the budget never enters.
"""
import itertools, numpy as np, sympy as sp

checks = []

# icosahedron: 12 unit vertices, cyclic permutations of (0, +-1, +-phi)/sqrt(1+phi^2)
phi = (1 + 5**0.5) / 2
vs = []
for a, b in itertools.product([1, -1], [1, -1]):
    vs += [(0, a, b*phi), (a, b*phi, 0), (b*phi, 0, a)]
V = np.array(vs) / np.sqrt(1 + phi**2)
assert V.shape == (12, 3) and np.allclose(np.linalg.norm(V, axis=1), 1)

# (1) monopole
m1 = np.linalg.norm(V.sum(axis=0))
checks.append(("monopole Sum v = 0 (exact/machine)", m1 < 1e-12, m1))

# (2) quadrupole
Q = sum(np.outer(v, v) for v in V)
m2 = np.abs(Q - 4*np.eye(3)).max()
checks.append(("quadrupole Sum v(x)v = 4*I (exact)", m2 < 1e-12, m2))

# (3b1) prefactor is O(D^2): value, 1st derivative vanish at D=0; 2nd nonzero
D, k = sp.symbols('D k', positive=True)
pref = 2*k*D**2 / (1 + k*D)**2
ser = sp.series(pref, D, 0, 3).removeO()
c0, c1, c2 = [sp.simplify(ser.coeff(D, n)) for n in (0, 1, 2)]
checks.append(("b1 prefactor O(D^2): c0=c1=0, c2=2k", c0 == 0 and c1 == 0 and sp.simplify(c2 - 2*k) == 0, str((c0, c1, c2))))

# (3b2) R = 2(-Om Om'' + Om'^2)/Om^4 -> 0 for constant Om
Om, Op, Opp = sp.symbols('Om Op Opp')
R = 2*(-Om*Opp + Op**2) / Om**4
checks.append(("b2 R=0 at Om'=Om''=0 (flat background)", sp.simplify(R.subs({Op: 0, Opp: 0})) == 0, "R->0"))

# (4) EXACT arithmetic: symbolic icosahedron (phi = golden ratio, exact) -- both moments
# algebraically zero, so ANY uniform ground-state magnitude (the portrait's 1e42) times the
# monopole is identically zero: annihilated, not suppressed.
sphi = (1 + sp.sqrt(5)) / 2
svs = []
for a, b in itertools.product([1, -1], [1, -1]):
    svs += [sp.Matrix([0, a, b*sphi]), sp.Matrix([a, b*sphi, 0]), sp.Matrix([b*sphi, 0, a])]
sn = sp.sqrt(1 + sphi**2)
SV = [v/sn for v in svs]
S1 = sp.simplify(sum(SV, sp.zeros(3, 1)))
S2 = sp.simplify(sum((v*v.T for v in SV), sp.zeros(3, 3)) - 4*sp.eye(3))
exact = (S1 == sp.zeros(3, 1)) and (S2 == sp.zeros(3, 3))
checks.append(("EXACT symbolic: Sum v = 0 and Sum vv^T = 4I identically (budget never enters)", exact, "algebraic zero"))

npass = 0
for name, ok, val in checks:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  ({val})")
    npass += ok
print(f"{npass}/{len(checks)} PASS")
assert npass == len(checks)
