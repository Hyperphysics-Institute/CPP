#!/usr/bin/env python3
"""
Patch 3315 verify — QM-3 (Bell inequality and entanglement) machine
verification, written 5 months post-ship to bring the paper up to the
corpus's computation-before-claims standard ahead of its first
five-seat CONV round (CONV-031).

Checks (all exact-symbolic unless noted):
  0. NON-SEPARABILITY (Thm nonsep): the singlet's coefficient matrix has
     Schmidt rank 2 (det = +1/2 != 0); a product state has rank 1.
  1. CORRELATOR (input to Thm chsh): E(a,b) = <psi| (a.sigma)x(b.sigma)
     |psi> = -cos(theta) exactly, for symbolic unit vectors.
  2. CHSH AT OPTIMAL ANGLES (Thm chsh): S = E(a,b) - E(a,b') + E(a',b)
     + E(a',b') = 2*sqrt(2) exactly at the standard 0/45/22.5/67.5 deg
     settings.
  3. TSIRELSON CEILING (numeric): a dense scan over coplanar settings
     never exceeds 2*sqrt(2) (tolerance 1e-9) and attains it.
  4. NO-SIGNALING (Thm nosig): Alice's marginal P(+1|a) = 1/2 exactly,
     symbolically independent of Bob's setting b (and vice versa).
  5. DETERMINISTIC-LHV BOUND (the corrected-away argument): exhaustive
     enumeration of all 16 deterministic local strategies gives
     max |S| = 2 — the shared-bit-pool model QM-3 v1 used, and v3
     explicitly retracted, is an LHV and could never have produced
     2*sqrt(2). The retraction was mathematically forced.
  6. HELIX-PHASE ENCODING CONSISTENCY (FI-QMRG-1 hook): the same-basis
     anticorrelation P(same outcome | theta=0) = 0 exactly, and the
     singlet is basis-invariant (U x U |psi> = det(U)^... -> state
     invariant up to phase for U in SU(2)); checked symbolically for a
     general SU(2) rotation.
"""
import itertools

import numpy as np
import sympy as sp

PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


# Pauli matrices, symbolic
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
I2 = sp.eye(2)

# Singlet |psi> = (|01> - |10>)/sqrt(2)
psi = sp.Matrix([0, 1, -1, 0]) / sp.sqrt(2)

# ---------------------------------------------------------------- check 0
C = sp.Matrix([[0, 1], [-1, 0]]) / sp.sqrt(2)     # coefficient matrix c_ij
detC = sp.simplify(C.det())
prod = sp.Matrix([1, 0]) * sp.Matrix([[1, 0]])    # any product state: rank 1
check("0. non-separability: Schmidt rank 2 (det C = 1/2 != 0); product rank 1",
      detC == sp.Rational(1, 2) and C.rank() == 2 and prod.rank() == 1,
      f"det C = {detC}")


def n_sigma(theta, phi):
    return (sp.sin(theta) * sp.cos(phi) * sx
            + sp.sin(theta) * sp.sin(phi) * sy
            + sp.cos(theta) * sz)


def kron(A, B):
    return sp.Matrix(sp.kronecker_product(A, B))


def E_ab(ta, pa, tb, pb):
    Op = kron(n_sigma(ta, pa), n_sigma(tb, pb))
    return sp.simplify((psi.T.conjugate() * Op * psi)[0, 0])


# ---------------------------------------------------------------- check 1
ta, tb = sp.symbols("theta_a theta_b", real=True)
E_general = E_ab(ta, 0, tb, 0)                    # coplanar; general phi below
val = sp.simplify(E_general + sp.cos(ta - tb))
# full generality: symbolic phis too
pa, pb = sp.symbols("phi_a phi_b", real=True)
E_full = E_ab(ta, pa, tb, pb)
# a.b for the two unit vectors:
adotb = (sp.sin(ta) * sp.cos(pa) * sp.sin(tb) * sp.cos(pb)
         + sp.sin(ta) * sp.sin(pa) * sp.sin(tb) * sp.sin(pb)
         + sp.cos(ta) * sp.cos(tb))
val_full = sp.simplify(E_full + adotb)
check("1. correlator E(a,b) = -a.b = -cos(theta) exactly (symbolic, general)",
      val == 0 and val_full == 0,
      "E + a.b == 0 identically")

# ---------------------------------------------------------------- check 2
deg = sp.pi / 180
S_opt = sp.simplify(
    E_ab(0, 0, 45 * deg, 0) - E_ab(0, 0, 135 * deg, 0)
    + E_ab(90 * deg, 0, 45 * deg, 0) + E_ab(90 * deg, 0, 135 * deg, 0))
check("2. CHSH at optimal angles = 2*sqrt(2) exactly (Tsirelson attained)",
      sp.simplify(sp.Abs(S_opt) - 2 * sp.sqrt(2)) == 0,
      f"S = {S_opt}")

# ---------------------------------------------------------------- check 3
angles = np.linspace(0, np.pi, 61)
maxS = 0.0
for a1 in angles:
    for a2 in angles:
        for b1 in angles:
            for b2 in angles:
                S = (-np.cos(a1 - b1) + np.cos(a1 - b2)
                     - np.cos(a2 - b1) - np.cos(a2 - b2))
                maxS = max(maxS, abs(S))
check("3. Tsirelson ceiling: dense scan max |S| <= 2*sqrt(2), attained",
      maxS <= 2 * np.sqrt(2) + 1e-9 and maxS > 2 * np.sqrt(2) - 1e-3,
      f"scan max = {maxS:.9f} vs 2*sqrt(2) = {2*np.sqrt(2):.9f}")

# ---------------------------------------------------------------- check 4
# Alice's marginal for outcome +1 along a, jointly with Bob measuring b:
Pa_plus = sp.simplify(
    (psi.T.conjugate()
     * kron((I2 + n_sigma(ta, pa)) / 2, I2)
     * psi)[0, 0])
Pb_plus = sp.simplify(
    (psi.T.conjugate()
     * kron(I2, (I2 + n_sigma(tb, pb)) / 2)
     * psi)[0, 0])
check("4. no-signaling: both marginals = 1/2 exactly, setting-independent",
      Pa_plus == sp.Rational(1, 2) and Pb_plus == sp.Rational(1, 2),
      f"P_A(+) = {Pa_plus}, P_B(+) = {Pb_plus}")

# ---------------------------------------------------------------- check 5
# Deterministic LHV: A(a) in {+-1} for each of 2 settings; same for B.
settings_a = [0.0, np.pi / 2]
settings_b = [np.pi / 4, 3 * np.pi / 4]
best = 0.0
for Amap in itertools.product([1, -1], repeat=2):
    for Bmap in itertools.product([1, -1], repeat=2):
        S = (Amap[0] * Bmap[0] - Amap[0] * Bmap[1]
             + Amap[1] * Bmap[0] + Amap[1] * Bmap[1])
        best = max(best, abs(S))
check("5. deterministic-LHV bound: max |S| over all 16 strategies = 2 "
      "(the retracted shared-bit-pool model could never reach 2*sqrt(2))",
      abs(best - 2.0) < 1e-12, f"LHV max = {best}")

# ---------------------------------------------------------------- check 6
# Same-basis perfect anticorrelation + SU(2) invariance of the singlet.
P_same = sp.simplify(
    (psi.T.conjugate()
     * (kron((I2 + sz) / 2, (I2 + sz) / 2)
        + kron((I2 - sz) / 2, (I2 - sz) / 2))
     * psi)[0, 0])
al, be = sp.symbols("alpha beta", real=True)
U = sp.Matrix([[sp.cos(al) + sp.I * sp.sin(al) * sp.cos(be),
                sp.I * sp.sin(al) * sp.sin(be)],
               [sp.I * sp.sin(al) * sp.sin(be),
                sp.cos(al) - sp.I * sp.sin(al) * sp.cos(be)]])
UU_psi = sp.simplify(kron(U, U) * psi)
diff = sp.simplify(UU_psi - psi * sp.simplify((U.det())))
# For SU(2), det U = 1 and U x U |singlet> = |singlet>:
detU = sp.simplify(U.det())
invariant = all(sp.simplify(x) == 0 for x in (UU_psi - psi))
check("6. helix-encoding hooks: P(same|theta=0) = 0 exact; singlet SU(2)-invariant",
      P_same == 0 and sp.simplify(detU - 1) == 0 and invariant,
      f"P_same = {P_same}; det U = {detU}; U x U singlet == singlet: {invariant}")

print()
print(f"{sum(PASS)}/{len(PASS)} PASS")
raise SystemExit(0 if all(PASS) else 1)
