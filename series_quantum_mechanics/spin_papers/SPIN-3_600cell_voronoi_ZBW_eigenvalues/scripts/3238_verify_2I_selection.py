#!/usr/bin/env python3
"""Patch 3238 verify script — OPEN-QM-8 ANALYTIC LEG (icosahedral selection).

Turns every arithmetic claim of the Spin III analytic-leg theorems into a
checked computation:

  1. CHARACTER COUNTS (Lemma: invariant content of I). The multiplicity of
     the trivial irrep of the icosahedral rotation group I in the spin-l
     representation of SO(3), by the exact character formula
         m_l = (1/60) * sum_classes |C| * sin((l+1/2)theta_C)/sin(theta_C/2),
     over the classes {E(1), C5(12, 72deg), C5^2(12, 144deg), C3(20, 120deg),
     C2(15, 180deg)}. Claim: m_l = 0 for l = 1..5; m_6 = 1; m_10 = 1;
     m_12 = 1. (Parity/inversion in I_h then kills odd l for the even
     boundary function; m_15 = 1 for I is computed and noted as
     parity-excluded.)

  2. HARMONIC CONTENT OF THE TRUE CELL. Project the dodecahedron support
     function R(omega) = 1/max_f(omega . n_f) onto real spherical harmonics
     on a Gauss-Legendre x uniform-phi product grid. Claim: relative
     amplitudes eps_l = sqrt(sum_m a_lm^2)/(sqrt(4 pi) Rbar) vanish (to
     quadrature error) for l = 1..5 and every odd l, and the first
     nonzero channel is l = 6; report eps_6, eps_10, eps_12.

  3. THE l=6 GAP (selection). Lowest eigenvalue of the l=6 radial u-problem
         -u'' + (42/r^2) u = k^2 u,  u(0)=0, u'(R)=0,
     by FD. Claim: k_{6,1} R > 3 pi / 2, so within the trivial irrep the
     second mode of the true cell is the deformed radial Mode 2 — the
     anchoring mode — for the actual cell's anisotropy. Also computes the
     l=1 and l=2 lowest eigenvalues and checks the INTERLOPER ACCOUNTING:
     exactly l=1 (3 states) + l=2 (5 states) = 8 non-invariant modes sit
     between radial Modes 1 and 2, matching the 3236 run's global indices
     (radial modes at 1 and 10).

  4. PROTECTION ORDER (consistency with the 3236 measurement). The
     perturbative claim is that fractional positions shift at O(eps_6^2)
     and the (mean-normalized) eigenvalue at O(eps_6^2). Reports
     eps_6^2 against the measured residuals (|dk|/k = 0.31%, node shift
     0.05%) — an order-of-magnitude consistency check, stated as such
     (the 3236 instrument's own declared approximation enters at the same
     order, so this is consistency, not decomposition).

Run: python3 3238_verify_2I_selection.py
"""

import math
import sys

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.special import lpmv

PHI = (1 + math.sqrt(5)) / 2

passes = []
def check(name, ok, detail=""):
    passes.append((name, ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


# ------------------------------------------------------------- 1. characters
print("== 1. Trivial-irrep multiplicities of I in spin-l (exact characters) ==")
classes = [  # (size, rotation angle in radians)
    (1, 0.0),
    (12, 2 * math.pi / 5),
    (12, 4 * math.pi / 5),
    (20, 2 * math.pi / 3),
    (15, math.pi),
]
def chi_l(l, theta):
    if abs(theta) < 1e-12:
        return 2 * l + 1
    return math.sin((l + 0.5) * theta) / math.sin(theta / 2)

def mult_trivial(l):
    s = sum(size * chi_l(l, th) for size, th in classes)
    m = s / 60.0
    return m

expect = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0, 8: 0, 9: 0,
          10: 1, 11: 0, 12: 1, 15: 1}
all_ok = True
for l in sorted(expect):
    m = mult_trivial(l)
    ok = abs(m - expect[l]) < 1e-9
    all_ok &= ok
    print(f"    l={l:>2}: m = {m:+.6f}  (expected {expect[l]})")
check("m_l = 0 for l=1..5; first invariant channel l=6 (exact)", all_ok)
print("    (m_15 = 1 for the rotation group I; excluded for the even boundary")
print("     function by the inversion in I_h — odd l carries odd parity.)")


# --------------------------------------------------- 2. cell harmonic content
print("\n== 2. Harmonic content of the true Voronoi cell's support function ==")
def icosa_vertices():
    v = []
    for s1 in (1, -1):
        for s2 in (1, -1):
            v += [(0, s1, s2 * PHI), (s1, s2 * PHI, 0), (s2 * PHI, 0, s1)]
    V = np.unique(np.array(v, float).round(12), axis=0)
    return V / np.linalg.norm(V, axis=1)[:, None]

ICO = icosa_vertices()

n_t, n_p = 240, 480
x_gl, w_gl = np.polynomial.legendre.leggauss(n_t)   # x = cos(theta)
phi = (np.arange(n_p) + 0.5) * 2 * math.pi / n_p
w_p = 2 * math.pi / n_p
ct = x_gl[:, None] * np.ones(n_p)[None, :]
st = np.sqrt(1 - ct ** 2)
X = st * np.cos(phi)[None, :]
Y = st * np.sin(phi)[None, :]
Z = ct
dirs = np.stack([X, Y, Z], axis=-1)                  # (n_t, n_p, 3)
R = 1.0 / np.max(dirs @ ICO.T, axis=-1)              # support radius, rho_in=1
W = w_gl[:, None] * w_p * np.ones(n_p)[None, :]      # quadrature weights

Rbar = float(np.sum(R * W) / (4 * math.pi))

def real_Ylm(l, m, ct2, phi1):
    # orthonormal real spherical harmonics
    mm = abs(m)
    norm = math.sqrt((2 * l + 1) / (4 * math.pi)
                     * math.factorial(l - mm) / math.factorial(l + mm))
    P = lpmv(mm, l, ct2)
    if m > 0:
        return math.sqrt(2) * norm * P * np.cos(mm * phi1)[None, :]
    if m < 0:
        return math.sqrt(2) * norm * P * np.sin(mm * phi1)[None, :]
    return norm * P * np.ones_like(phi1)[None, :]

eps = {}
for l in range(0, 13):
    p2 = 0.0
    for m in range(-l, l + 1):
        Y_ = real_Ylm(l, m, x_gl[:, None], phi)
        a = float(np.sum(R * Y_ * W))
        p2 += a * a
    eps[l] = math.sqrt(p2) / (math.sqrt(4 * math.pi) * Rbar)

print(f"    mean radius <R> = {Rbar:.6f} (inradius units)")
for l in range(0, 13):
    tag = "  <-- first anisotropy channel" if l == 6 else ""
    print(f"    eps_{l:<2} = {eps[l]:.3e}{tag}")

quad_floor = 5e-4   # support function has edge kinks; quadrature is algebraic
forbidden = max(eps[l] for l in (1, 2, 3, 4, 5, 7, 8, 9, 11))
check("eps_l at the quadrature floor for l=1..5,7,8,9,11",
      forbidden < quad_floor, f"max forbidden {forbidden:.1e}")
check("l=6 is the leading anisotropy channel",
      eps[6] > 10 * forbidden and eps[6] > eps[10] > 0,
      f"eps_6 = {eps[6]:.3e}, eps_10 = {eps[10]:.3e}, eps_12 = {eps[12]:.3e}")


# ------------------------------------------------------------- 3. the l=6 gap
print("\n== 3. The l=6 gap and the interloper accounting ==")
def lowest_k(l, N=20000, R1=1.0):
    h = R1 / N
    r = (np.arange(1, N + 1)) * h
    d = np.full(N, 2.0) / h**2 + l * (l + 1) / r**2
    d[-1] = 1.0 / h**2 + l * (l + 1) / r[-1] ** 2
    o = np.full(N - 1, -1.0) / h**2
    K = sp.diags([o, d, o], [-1, 0, 1], format="csr")
    b = np.ones(N); b[-1] = 0.5
    B = sp.diags(b, format="csr") * 1.0
    v = spla.eigsh(K, k=1, M=B, sigma=0, which="LM",
                   return_eigenvectors=False)
    return math.sqrt(float(v[0]))

k2 = 3 * math.pi / 2
k6 = lowest_k(6)
k1l = lowest_k(1)
k2l = lowest_k(2)
k3l = lowest_k(3)
print(f"    k(l=1,n=1) = {k1l:.4f}, k(l=2,n=1) = {k2l:.4f}, "
      f"k(l=3,n=1) = {k3l:.4f}")
print(f"    k(l=6,n=1) = {k6:.4f}   vs   radial Mode 2: 3pi/2 = {k2:.4f}")
check("l=6 gap: k(6,1) > 3pi/2 (selection within the trivial irrep)",
      k6 > k2, f"{k6:.4f} > {k2:.4f}")
between = [("l=1", k1l, 3), ("l=2", k2l, 5), ("l=3", k3l, 7)]
count = sum(mult for _, kv, mult in between if math.pi / 2 < kv < k2)
names = [nm for nm, kv, _ in between if math.pi / 2 < kv < k2]
check("interloper accounting: exactly 8 non-invariant modes between radial "
      "Modes 1 and 2 (l=1 + l=2)", count == 8 and names == ["l=1", "l=2"],
      f"{names} -> {count} states (3236 run: radial modes at global "
      f"indices 1 and 10)")


# ------------------------------------------------- 4. protection consistency
print("\n== 4. Protection order vs the 3236 measured residuals ==")
e6sq = eps[6] ** 2
meas_dk = 0.0031     # |k shift| / k, mean-radius-normalized (3236 record)
meas_node = 0.0005   # node position shift (0.6670 vs 0.6667)
print(f"    eps_6 = {eps[6]:.4f}  =>  eps_6^2 = {e6sq:.5f}")
print(f"    measured: |dk|/k = {meas_dk:.4f}, node shift = {meas_node:.4f}")
check("measured residuals are O(eps_6^2)-sized (order consistency: "
      "0.1x-3x window)", 0.1 * e6sq < meas_dk < 3 * e6sq,
      f"eps_6^2 = {e6sq:.4f} vs |dk|/k = {meas_dk:.4f}")
check("node shift <= eps_6^2 class", meas_node < 3 * e6sq,
      f"{meas_node:.4f} <= {3*e6sq:.4f}")

print("\n== SUMMARY ==")
n_ok = sum(1 for _, ok in passes if ok)
for name, ok in passes:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"{n_ok}/{len(passes)} checks pass")
sys.exit(0 if n_ok == len(passes) else 1)
