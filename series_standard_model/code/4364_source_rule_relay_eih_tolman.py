#!/usr/bin/env python3
"""Patch 4364 - the source rule: how a source's per-Moment injection into the relay must scale
with the local PSR, one rule for mass and charge (TODO-4359-SOURCERULE).

Parts
  A. Lattice-relay (radial) solve of GR-1j's statics, u = M_{R(x)}[u] + sigma, with a PSR
     profile R(r) that differs at the source and far away.  Gather (GR-1j's registered kernel)
     versus scatter (the corpus's emission picture).  Far and near coefficients.
  B. Local invariance.  With rulers and clocks both scaling with q = PSR/PSR_inf (4362, one PSR),
     the census of a source of injection S ~ R_s^p, read at n local PSRs, scales as q_s^(p-3):
     p = 3 makes it invariant.  Gravity's observable is the lapse, whose sensitivity under the
     ratified law is d ln q/d eps = -1 + eps^2/2, so G_loc keeps a residual (1 - eps0^2/2).
  C. GR's 1PN N-body (EIH) static cross term: |a| = (1 - 5 U0) m_b/r^2 in GR
     (2beta+2gamma = 4 at the test body, 2beta-1 = 1 at the source).  CPP with the
     assembled metric g00 = -q^2, g_ij = q^-2 delta gives q0^4 * q0^(p-2): needs p = 3.
     (4364 critic: for a uniform U0 this is B restated in coordinates, not an independent test.)
  D. Tolman: the exact static Einstein R_00 equation, D^i D_i N = 4 pi G N (rho + 3p),
     evaluated on the CPP metric ansatz, is  lap_flat ln q = 4 pi G q rho_lat  for dust:
     the lapse factor q is the extra power of R beyond GR-1j's R^2.  (A CHECK, not the
     derivation: GR-1j's claim discipline bars positing Einstein's equations.)
  E. Receiver-side compensation (the reading divides by a function of the receiver's state,
     w = q_rec^j) instead of source-side: shifts the single-body second-order coefficient,
     beta_eff = 1 + j/2.  j = 3 (exact receiver-side invariance) gives beta = 5/2,
     reproducing 4361's critic result independently.
"""
import numpy as np
import sympy as sp

print(__doc__)

# ---------------------------------------------------------------- A. radial relay solve
def build(R_of_r, h=0.025, rmax=90.0, b=0.2, S=1.0):
    n = int(rmax / h)
    edges = np.arange(n + 1) * h
    r = 0.5 * (edges[:-1] + edges[1:])
    R = R_of_r(r)
    M = np.zeros((n, n))
    for i in range(n):
        lo, hi = abs(r[i] - R[i]), r[i] + R[i]
        a = np.clip(edges[:-1], lo, hi)
        c = np.clip(edges[1:], lo, hi)
        M[i, :] = 0.5 * (c**2 - a**2) / (2 * r[i] * R[i])   # mean over sphere of a radial fn
    vol = 4 * np.pi / 3 * (np.minimum(edges[1:], b)**3 - np.minimum(edges[:-1], b)**3)
    cellvol = 4 * np.pi / 3 * (edges[1:]**3 - edges[:-1]**3)
    sigma = S * vol / cellvol / (4 * np.pi / 3 * b**3)
    return r, M, sigma, cellvol

def fit(r, u, lo, hi):
    sel = (r > lo) & (r < hi)
    A = np.vstack([1 / r[sel], np.ones(sel.sum())]).T
    C, D = np.linalg.lstsq(A, u[sel], rcond=None)[0]
    resid = np.max(np.abs(A @ [C, D] - u[sel])) / np.max(np.abs(u[sel]))
    return C, resid

def solve_relay(R_of_r, kernel="gather", near=False):
    """gather: u(x) = mean of u over the sphere of radius R(x) (GR-1j L208-216, T-1 §2-3).
       scatter: each origin y sends its value to its own PSR shell R(y) (c01; founder payload
       spec 2026-08-06 'deposits exactly once, at its origin's PSR shell'): the volume-transpose."""
    r, M, sigma, cv = build(R_of_r)
    K = M if kernel == "gather" else (M.T * cv[None, :] / cv[:, None])   # n_i = sum_j M_ji n_j cv_j / cv_i
    u = np.linalg.solve(np.eye(len(r)) - K, sigma)
    return fit(r, u, 3.0, 7.0) if near else fit(r, u, 24, 45)

def profile(Rs, Rf, r1=9.0, r2=16.0):
    def f(r):
        t = np.clip((r - r1) / (r2 - r1), 0, 1)
        s = t * t * (3 - 2 * t)
        return Rs + (Rf - Rs) * s
    return f

print("A. Far-field coefficient C versus the PSR at the source (R_s) and far away (R_f)")
print("   prediction (gather) C = (6/4pi) S / R_s^2, independent of R_f")
C0, res0 = solve_relay(profile(1.0, 1.0))
print(f"   uniform R=1: C = {C0:.5f}   (6/4pi = {6/(4*np.pi):.5f})   fit resid {res0:.1e}")
rows = [(1.0, 1.0), (0.9, 1.0), (0.8, 1.0), (1.0, 1.2), (0.9, 1.2), (1.0, 0.85)]
Cgn0, _ = solve_relay(profile(1.0, 1.0), near=True)
print("   R_s    R_f   | gather far   R_s^-2  | scatter far  R_f^-2 | gather near  scatter near  R_s^-2")
for Rs, Rf in rows:
    Cg, _ = solve_relay(profile(Rs, Rf))
    Cs, _ = solve_relay(profile(Rs, Rf), "scatter")
    Cgn, _ = solve_relay(profile(Rs, Rf), near=True)
    Csn, _ = solve_relay(profile(Rs, Rf), "scatter", near=True)
    print(f"   {Rs:4.2f}  {Rf:4.2f}  |  {Cg/C0:8.5f}   {Rs**-2:7.5f} |  {Cs/C0:8.5f}   {Rf**-2:7.5f} |"
          f"  {Cgn/Cgn0:8.5f}    {Csn/Cgn0:8.5f}     {Rs**-2:7.5f}")
print("   -> gather (GR-1j's registered kernel): the far field is set by R at the source.")
print("      scatter (the corpus's emission picture, c01/AP-4c): the far coefficient follows R_f instead")
print("      (the vacuum is then not exactly Laplace across a PSR gradient: D(x)u, D ~ R^2, is harmonic).")
print("      NEAR the source, inside a region of uniform PSR, both kernels give (6/4pi) S / R_s^2:")
print("      the local field of a source in a uniform background -- what B and C test -- is kernel-independent.")
print("      Caveat (4364 critic): with the PSR changing within ~1 PSR of the source, C uses R averaged there.")

# ---------------------------------------------------------------- B. local invariance
print("\nB. Local reading of a source's field, source deep in a uniform background q0")
q0, p, k, S0, n_ = sp.symbols('q0 p k S0 n', positive=True)
R_inf = sp.Symbol('R_inf', positive=True)
Rs = q0 * R_inf
S = S0 * q0**p                                   # injection per Moment ~ R_s^p
C = sp.Rational(6, 1) / (4 * sp.pi) * S / Rs**2  # A: coordinate coefficient
r_coord = n_ * Rs                                # n local PSRs away (rulers ~ PSR)
du_local = sp.simplify(C / r_coord)              # census at n local PSRs; d(ln q) = -k du
print("   d(ln q) at n local PSRs  =", sp.simplify(-k * du_local))
print("   dependence on q0         =", sp.simplify(du_local / du_local.subs(q0, 1)))
print("   -> census invariant iff p = 3 (fixed count, p = 0, gives q0^-3 = (1+3U): the 4359 critic's k_G = -3;")
print("      GR-1j read with fixed coordinate GM, p = 2, gives q0^-1 = (1+U)).")
eps = sp.Symbol('epsilon', positive=True)
lnq = sp.log(1 - eps + eps**2 / 2)                    # ratified R-PSR-LAW-LOG
sens = sp.series(sp.diff(lnq, eps), eps, 0, 4).removeO()
print("   ratified law: d ln q / d eps =", sens)
print("   -> gravity's local field is the lapse gradient, so G_loc carries (1 - eps0^2/2) at p = 3 (4364 critic).")
print("      The census itself (and a metric-coupled charge reading, which has no lapse-sensitivity factor)")
print("      is invariant exactly; whether alpha is free of eps0^2/2 rests on that reading -- inferred, owed.")

# ---------------------------------------------------------------- C. EIH cross term
print("\nC. EIH (1PN N-body; tested by lunar laser ranging)")
U0, dU, x = sp.symbols('U0 dU x', real=True)
r = sp.Symbol('r', positive=True)
mb, kk = sp.symbols('m_b k', positive=True)
# CPP assembled metric: g00 = -q^2, g_ij = q^-2 delta, q = exp(-k u);   slow test particle:
# a^i = -Gamma^i_00 = -(1/2) g^ij d_j(-g00) ... = -q^3 d_i q = -q^4 d_i ln q
pp = sp.Symbol('p')
u0 = U0 / kk
qs0 = sp.exp(-U0)
Cc = mb * qs0**(pp - 2) / kk                      # source coefficient ~ S/R_s^2 ~ q_s^(p-2)
u = u0 + Cc / r
q = sp.exp(-kk * u)
a_r = sp.simplify(-q**4 * sp.diff(sp.log(q), r))  # radial coordinate acceleration
lead = sp.series(sp.simplify(a_r * r**2 / mb), mb, 0, 1).removeO()
lin = -sp.series(lead, U0, 0, 2).removeO()        # magnitude (attractive: a_r < 0)
print("   CPP |coordinate acceleration| x r^2/m_b, first order in U0:", sp.expand(sp.simplify(lin)))
print("   GR (EIH, beta = gamma = 1):  1 - (2b+2g) U0 - (2b-1) U0 = 1 - 5 U0")
sol = sp.solve(sp.Eq(sp.expand(lin).coeff(U0), -5), pp)
print("   -> required p =", sol, "   (reading supplies 4 via q^4; the source rule supplies 2b-1 = 1 via q_s^(p-2))")
for pv in (0, 2, 3):
    c1 = sp.expand(lin.subs(pp, pv)).coeff(U0)
    print(f"      p = {pv}: 1 + ({c1}) U0  -> departure from GR {c1 + 5} U0")

# ---------------------------------------------------------------- D. Tolman check
print("\nD. Tolman's static source on the CPP metric ansatz (check only)")
X, Y, Z = sp.symbols('X Y Z', real=True)
Q = sp.Function('Q')(X, Y, Z)
coords = (X, Y, Z)
sqrt_h = Q**-3                                   # h_ij = Q^-2 delta
lap_g = (1 / sqrt_h) * sum(sp.diff(sqrt_h * Q**2 * sp.diff(Q, c), c) for c in coords)
lap_ln = sum(sp.diff(sp.log(Q), c, 2) for c in coords)
print("   D^i D_i q  -  q^3 lap_flat(ln q)  =", sp.simplify(lap_g - Q**3 * lap_ln))
print("   D^i D_i q = 4 pi G q rho_prop, rho_prop = q^3 rho_lat (bodies shrink with the PSR)")
print("   => lap_flat(ln q) = 4 pi G q rho_lat:  with ln q = -k u and GR-1j's u - M_R u = s,")
print("      s = (R_s^2/6)(4 pi G/k) q_s rho_lat  ~  R_s^3 per CP.  Same exponent as B and C.")

# ---------------------------------------------------------------- E. receiver-side compensation
print("\nE. Receiver-side compensation w = q_rec^j applied to the read field (single source)")
j = sp.Symbol('j')
Us = sp.Symbol('U', positive=True)
# single source, CPP: a = q^4 k du/dr * w(q) with ln q = -U;  GR: a = (1 - 2(beta+gamma) U) dU/dr
factor = sp.series(sp.exp(-4 * Us) * sp.exp(-j * Us), Us, 0, 2).removeO()
beta_eff = sp.solve(sp.Eq(-factor.coeff(Us), 2 * (sp.Symbol('beta') + 1)), sp.Symbol('beta'))
print("   coefficient of U:", sp.expand(factor).coeff(Us), " -> beta_eff =", beta_eff)
print("   j = 3 (exact invariance done at the receiver):", [b.subs(j, 3) for b in beta_eff],
      " = 4361's beta = 5/2.  Source-side (factor of the source's own q) leaves beta = 1:")
print("   the source's factor is a constant absorbed into the measured GM of a single body.")

# ---------------------------------------------------------------- numbers
print("\nNumbers")
U_sun_1AU = 9.87e-9
dU_annual = 2 * 0.0167 * U_sun_1AU
U_gal = 1.0e-6        # order of the Milky Way's potential at the Sun (|Phi|/c^2 ~ 1e-6)
bound = 1.2e-17       # 4352/4360: Lange 2021 annual-amplitude bound used in this arc
print(f"   annual dU at Earth (peak-to-peak) = {dU_annual:.2e}")
for name, e0 in (("eps0 = U_sun", U_sun_1AU), ("eps0 = U_gal (if eps is absolute)", U_gal)):
    print(f"   {name:36s}: 4360 receiver-side 9*eps*deps = {9*e0*dU_annual:.1e} ({9*e0*dU_annual/bound:6.1f}x);"
          f"  p=3 lapse residual eps*deps = {e0*dU_annual:.1e} ({e0*dU_annual/bound:5.2f}x)")
print("   The lapse residual is certain for G (unobservable: LLR is far coarser); for alpha it applies only if the")
print("   charge reading carries the lapse's sensitivity. 'Absolute or relative eps' is a PSR-law question (owed).")
