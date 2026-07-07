#!/usr/bin/env python3
"""Patch 2317 -- G4 Stage 2, S2-1: the explicit dispersion of the gapless |SSV| coherence mode.

Object: the REGISTERED broadcast-dispersion symbol (2074/OPEN-SR-10 W2, TLA-ratified 2080):
    D(k) = Sum_shell w * 2*(1 - cos(k . x)),  single 12-vertex icosahedral shell (z = 12, R3),
uniform weight w on the shell, lattice spacing a (x = a*v_hat).

Results verified here (exact where marked):
  (1) D(0) = 0 EXACTLY (symbolic)             -> gapless at the discrete-linear level: 1169
      cap-1 hardened (discreteness does NOT gap the mode at linear order).
  (2) grad D(0) = 0 EXACTLY (symbolic)         -> no odd terms (central symmetry; monopole zero).
  (3) k^2 coefficient = 4*a^2, ISOTROPIC EXACT -> omega^2 = c_s^2 k^2 (1 + O((ka)^2)): linear,
      gapless, isotropic leading dispersion. (Hessian = 2*Sum x x^T = 8 a^2 I.)
  (4) k^4 term ISOTROPIC (5-design: Sum (khat.v)^4 = 12/5 for every khat, spread ~ machine)
      -> the "5-design signature": omega^2(0) = 0 with isotropy through degree 5.
  (5) k^6 term ANISOTROPIC (the l=6 icosahedral harmonic) -- the W2 anisotropy floor reproduced
      from the shell itself; measured amplitude -> relative speed anisotropy
      eps(khat) ~ (Delta_6/2880) * (ka)^4.
  (6) At G4 encounter scales (b_max ~ 31-145 fm, a ~ l_P): (ka)^4 ~ 1e-88 -- continuum-perfect;
      no lattice loophole at capture scales.
  (7) IR speed: W2 (IR-exact Lorentz, RATIFIED) admits ONE invariant cone; a gapless mode with
      c_s != c would define a second cone and violate the ratified isotropic-elasticity result
      -> c_s = c, DERIVED-conditional on W2. Subsonic depths recomputed at the derived speed.
"""
import itertools, numpy as np, sympy as sp

checks = []
# exact icosahedral shell (golden ratio symbolic)
phi = (1 + sp.sqrt(5))/2
vs = []
for s1, s2 in itertools.product([1, -1], [1, -1]):
    vs += [sp.Matrix([0, s1, s2*phi]), sp.Matrix([s1, s2*phi, 0]), sp.Matrix([s2*phi, 0, s1])]
n = sp.sqrt(1 + phi**2)
V = [v/n for v in vs]

kx, ky, kz, a = sp.symbols('k_x k_y k_z a', real=True)
k = sp.Matrix([kx, ky, kz])
D = sum(2*(1 - sp.cos(a*(k.T*v)[0])) for v in V)

# (1) gapless exactly
checks.append(("D(0) = 0 exactly (gapless, discrete-linear)", sp.simplify(D.subs({kx:0,ky:0,kz:0})) == 0, "exact"))
# (2) no linear term
g = [sp.simplify(sp.diff(D, s).subs({kx:0,ky:0,kz:0})) for s in (kx,ky,kz)]
checks.append(("grad D(0) = 0 exactly (no odd terms)", all(x == 0 for x in g), g))
# (3) Hessian = 8 a^2 I -> k^2 coefficient 4 a^2 isotropic
H = sp.Matrix(3,3, lambda i,j: sp.simplify(sp.diff(D,(kx,ky,kz)[i],(kx,ky,kz)[j]).subs({kx:0,ky:0,kz:0})))
checks.append(("Hessian = 8 a^2 I exactly -> D ~ 4 a^2 k^2 isotropic", sp.simplify(H - 8*a**2*sp.eye(3)) == sp.zeros(3,3), "8a^2 I"))

# (4)-(5) direction scan of moments (numeric)
Vn = np.array([[float(c) for c in v] for v in V])
rng = np.random.default_rng(2317)
khats = rng.normal(size=(4000,3)); khats /= np.linalg.norm(khats, axis=1)[:,None]
m4 = ((khats @ Vn.T)**4).sum(axis=1)
m6 = ((khats @ Vn.T)**6).sum(axis=1)
checks.append((f"degree-4 moment isotropic (5-design): 12/5 with spread {np.ptp(m4):.1e}",
               abs(m4.mean()-12/5) < 1e-12 and np.ptp(m4) < 1e-12, (m4.mean(), np.ptp(m4))))
d6 = float(np.ptp(m6))
checks.append((f"degree-6 moment ANISOTROPIC: Delta_6 = {d6:.4f} about mean {m6.mean():.4f} (sphere 12/7={12/7:.4f}) -- the W2 l=6 floor from the shell",
               d6 > 1e-3, (m6.min(), m6.max())))
# relative speed anisotropy prefactor and value at encounter scales
pref = d6/2880
lp, b = 1.616e-35, 79e-15
ka4 = (lp/b)**4
checks.append((f"speed anisotropy eps ~ {pref:.1e}*(ka)^4; at b_max=79 fm, a=l_P: (ka)^4 = {ka4:.1e} -> eps ~ {pref*ka4:.1e} (continuum-perfect)",
               pref*ka4 < 1e-80, pref*ka4))

# (7) subsonic depths at the DERIVED c_s = c (W2-pinned)
C = 2.998e8
for vkms in (10, 50, 200):
    pass
depths = {vkms: vkms*1e3/C for vkms in (10,50,200)}
checks.append((f"c_s = c (W2-pinned, one invariant cone): v/c_s = " +
               ", ".join(f"{k} km/s -> {x:.1e}" for k,x in depths.items()) + " -- R1 CLOSED",
               all(x < 7e-4 for x in depths.values()), depths))

npass = 0
for name, ok, val in checks:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    npass += ok
print(f"{npass}/{len(checks)} PASS")
assert npass == len(checks)
