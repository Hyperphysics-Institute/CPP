#!/usr/bin/env python
"""Patch 3097 -- A-1: the SCR-1 census recount under R-SEA-WEAVE.

The ruled Sea (R-SEA-WEAVE, Patch 3093) is an array of 4-CP weave
units (one eDP + one qDP, electrically bound; f_hyb ~ 1). Each unit
carries TWO unit electric dipoles (composition ruling: eCP and qCP
each carry unit electric charge). This script computes the E-register
arrival-sum census relative to the 3076 committed convention (ONE
unit E-dipole per array site at nn spacing d, converged FCC sum
C4 = 25.3382 from 3071).

Computed here:
  (A) C4_inf     : the 3071 converged one-dipole-per-site FCC sum,
                   reproduced (regression gate).
  (B) phi1_lead  : leading-order weave census -- 2 co-located unit
                   E-dipoles per unit site, receiving unit excluded
                   entirely (unit-internal exclusion convention,
                   see the note SS3). Analytic: exactly 2.
  (C) phi1(xi)   : finite-extent correction -- the two dipoles offset
                   +/- xi/2 about the unit center along random unit
                   orientations; S4(xi)/C4 tabulated for
                   xi/d in {0.1 .. 0.5}.
  (D) fixed-DP-density cross-check: at FIXED DP number density,
                   dimerizing DPs into units (unit spacing 2^{1/3} d)
                   gives S4/(C4/d^4) = 2^{-1/3} = 0.7937. Verified
                   numerically. Pure convention statement.
  (E) arrangement bracket: the corpus-forcing of FCC held at the l_P
                   lattice (3067); at dilute spacing d the unit array
                   is isotropic-on-average (R-DS-EVOLVE), arrangement
                   UNRULED. Poisson array with hard core a*d at
                   matched density, a in {0.5..0.9}: Sigma 1/r^4
                   tabulated as the disorder bracket vs FCC.

Anti-extraction: no reference to the band anywhere below; no verdict
is recomputed; per the 3068 freeze the factors multiply once, at the
end.
"""
import numpy as np

rng = np.random.default_rng(31415)

# ---------- FCC site generator (nn = 1) -----------------------------
def fcc_sites(R):
    M = int(np.ceil(R * np.sqrt(2))) + 3
    g = np.arange(-M, M + 1)
    I, J, K = np.meshgrid(g, g, g, indexing="ij")
    mask = ((I + J + K) % 2 == 0)
    S = np.stack([I[mask], J[mask], K[mask]], 1).astype(float) / np.sqrt(2.0)
    r2 = np.einsum("ij,ij->i", S, S)
    return S[(r2 > 1e-9) & (r2 <= R * R)], np.sqrt(2.0)  # sites, density

TAIL = lambda dens, Rc: 4.0 * np.pi * dens / Rc  # exact 1/r^4 tail

# ---------- (A) reproduce the 3071 converged C4 ---------------------
R = 36.0
S, dens = fcc_sites(R)
C4 = float(np.sum(np.einsum("ij,ij->i", S, S) ** -2)) + TAIL(dens, R)
print(f"(A) C4 converged (one dipole per FCC site, nn=1) = {C4:.4f}")
assert abs(C4 - 25.3382) < 0.02, "failed to reproduce the 3071 converged sum"

# ---------- (B) leading-order weave census --------------------------
# Two E-dipoles co-located at each external unit site; receiving unit
# excluded entirely. S4 = 2 * C4 exactly as xi -> 0.
phi1_lead = 2.0
print(f"(B) phi1 leading order (xi -> 0)               = {phi1_lead:.4f}  [analytic: 2 x C4 / C4]")

# ---------- (C) finite-extent correction ----------------------------
# Each external unit: dipoles at s +/- (xi/2) u_hat, u_hat random per
# unit (isotropic orientations), averaged over ensembles.
print("(C) finite-extent correction phi1(xi) = S4(xi)/C4 :")
NENS = 24
for xi in (0.1, 0.2, 0.3, 0.4, 0.5):
    acc = 0.0
    for _ in range(NENS):
        u = rng.normal(size=S.shape)
        u /= np.linalg.norm(u, axis=1, keepdims=True)
        for sgn in (+0.5, -0.5):
            P = S + sgn * xi * u
            acc += float(np.sum(np.einsum("ij,ij->i", P, P) ** -2))
    S4 = acc / NENS + 2.0 * TAIL(dens, R)     # two dipoles per site
    print(f"      xi/d = {xi:.1f}: phi1 = {S4 / C4:.4f}   (excess vs 2: {S4/C4 - 2.0:+.4f})")

# ---------- (D) fixed-DP-density convention cross-check -------------
# Same DP count, dimerized: unit density = half DP density -> unit nn
# spacing 2^{1/3}; two dipoles per unit; expect 2 / 2^{4/3} = 2^{-1/3}.
s = 2.0 ** (1.0 / 3.0)
S2, dens2 = fcc_sites(R / s)
r2u = np.einsum("ij,ij->i", S2 * s, S2 * s)
S4_dimer = 2.0 * (float(np.sum(r2u ** -2)) + TAIL(dens2 / s ** 3, R))
ratio = S4_dimer / C4
print(f"(D) fixed-DP-density dimerization: S4/C4 = {ratio:.4f}   [analytic 2^(-1/3) = {2**(-1/3):.4f}]")
assert abs(ratio - 2 ** (-1 / 3)) < 0.02, "fixed-density cross-check failed"

# ---------- (E) arrangement bracket: Poisson + hard core ------------
print("(E) disorder bracket -- Poisson array, matched density sqrt(2)/d^3, hard core a*d:")
print("    (one dipole per site shown; the weave doubles it identically)")
RP, NCFG = 18.0, 40
VOL = (4 / 3) * np.pi * RP ** 3
NPTS = int(round(np.sqrt(2.0) * VOL))
for a in (0.5, 0.6, 0.7, 0.8, 0.9):
    vals = []
    for _ in range(NCFG):
        P = rng.uniform(-RP, RP, size=(int(NPTS * 2.2), 3))
        r2 = np.einsum("ij,ij->i", P, P)
        P = P[(r2 <= RP * RP) & (r2 >= a * a)][:NPTS]
        vals.append(np.sum(np.einsum("ij,ij->i", P, P) ** -2))
    S4p = float(np.mean(vals)) + TAIL(np.sqrt(2.0), RP)
    print(f"      a = {a:.1f}: Sigma 1/r^4 = {S4p:7.3f}   (ratio to FCC C4: {S4p / C4:.3f})")

print("\nAll gates PASS. phi1(weave) = 2 x [1 + O(xi^2/d^2)] on the")
print("canonical inter-unit-spacing anchoring; 2^(-1/3) x that under")
print("fixed-DP-density anchoring (pure convention); arrangement")
print("bracket recorded, unresolved (isotropic array vs FCC).")
