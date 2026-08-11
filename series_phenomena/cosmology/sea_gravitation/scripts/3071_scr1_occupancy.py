#!/usr/bin/env python
"""Patch 3071 -- SCR-1 (pair density / occupancy) forward resolution.

Frozen question (3068, oblcc2_assembly_record.md SS3): the forward
assembly's lattice sum took ONE PAIR PER FCC SITE. The founder's
registered picture (3059, quoted at 3067) is EVERY GP A CP, a DP's two
CPs on ADJACENT GPs. Under that picture the emitting dipoles are the
matched nearest-neighbour DIMERS of the fully occupied FCC lattice:
N_pairs = N_sites/2, located at nn-edge midpoints of a matching that
RESHUFFLES every ZBW cycle (partner switching, FQ-1).

Computed here, by direct summation over a sphere + exact analytic tail
(4*pi*density/R for a 1/r^4 sum):

  (A0) C4_3067  : the 3067 committed convention reproduced EXACTLY
                  (integer cube n in [-40,40], no tail) = 24.8225.
  (A)  C4_inf   : the CONVERGED one-pair-per-site sum. The 3067 cube
                  truncation undercounts by ~2% -- recorded as a small
                  forward numerical erratum, separate from SCR-1.
  (B)  S4_mf    : cycle-averaged pair-centre sum, DYNAMIC matching,
                  mean-field: every nn-edge midpoint carries weight
                  1/12 (each site in exactly one of its 12 edges;
                  charge eligibility halves eligible edges and doubles
                  the conditional weight -- product unchanged). Edges
                  incident to the origin CP are its OWN pairing ->
                  excluded as self.
  (C)  S4_par   : bracketing extreme -- fully ORDERED matching, all
                  dimers parallel along one nn direction, origin's
                  dimer excluded.

Output: phi_1 = S4_pair / C4_inf. phi_1 multiplies rho_Lambda;
sqrt(phi_1) multiplies c_Li. No verdict is recomputed here -- per the
3068 freeze the factors (SCR-1/2/3, D-COMP-WEIGHT) multiply once, at
the end. Anti-extraction: no reference to the band anywhere below.
"""
import numpy as np

# ---------- (A0) reproduce the 3067 committed convention exactly ----
n = np.arange(-40, 41)
Pi = np.stack(np.meshgrid(n, n, n, indexing="ij"), -1).reshape(-1, 3).astype(float)
Pi = Pi[(Pi.sum(1) % 2) == 0]
Pi = Pi[np.any(Pi != 0, 1)]
C4_3067 = 4 * float(np.sum(1.0 / np.sum(Pi**2, 1) ** 2))
print(f"(A0) C4 per 3067 convention (cube +/-40, no tail) = {C4_3067:.4f}")
assert abs(C4_3067 - 24.8225) < 0.01, "failed to reproduce the 3067 number"

# ---------- FCC sites, nn = 1, sphere ------------------------------
R, RCHK = 36.0, 28.0
M = int(np.ceil(R * np.sqrt(2))) + 3
g = np.arange(-M, M + 1)
I, J, K = np.meshgrid(g, g, g, indexing="ij")
mask = ((I + J + K) % 2 == 0)
S = np.stack([I[mask], J[mask], K[mask]], axis=1).astype(float)
Sint = S.copy()                      # integer rep (nn = sqrt(2))
S = S / np.sqrt(2.0)                 # physical rep (nn = 1)
r2 = np.einsum("ij,ij->i", S, S)
keep = r2 <= (R + 2.0) ** 2
S, Sint, r2 = S[keep], Sint[keep], r2[keep]
n_sites = np.sqrt(2.0)               # FCC density at nn = 1
tail = lambda dens, Rc: 4.0 * np.pi * dens / Rc

def c4_converged(Rc):
    sel = (r2 > 1e-12) & (r2 <= Rc**2)
    return float(np.sum(r2[sel] ** -2)) + tail(n_sites, Rc)

C4, C4c = c4_converged(R), c4_converged(RCHK)
print(f"(A)  C4_inf (converged, sphere+tail)              = {C4:.4f}  (R={RCHK:g}: {C4c:.4f})")
print(f"     3067-truncation erratum factor on rho        = {C4 / C4_3067:.4f}")

# ---------- nn vectors: 6 positive-half representatives ------------
NNh = np.array([(1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1),
                (0, 1, 1), (0, 1, -1)], float) / np.sqrt(2.0)
assert np.allclose(np.linalg.norm(NNh, axis=1), 1.0)

# ---------- (B) mean-field dynamic matching ------------------------
def s4_meanfield(Rc):
    total = 0.0
    for v in NNh:
        mid = S + 0.5 * v
        m2 = np.einsum("ij,ij->i", mid, mid)
        t2 = np.einsum("ij,ij->i", S + v, S + v)
        sel = (r2 > 1e-12) & (t2 > 1e-12) & (m2 <= Rc**2)   # not incident to origin
        total += float(np.sum(m2[sel] ** -2)) / 12.0
    return total + tail(n_sites / 2.0, Rc)

S4mf, S4mfc = s4_meanfield(R), s4_meanfield(RCHK)
print(f"(B)  S4_meanfield (dynamic matching)              = {S4mf:.4f}  (R={RCHK:g}: {S4mfc:.4f})")

# ---------- (C) ordered parallel matching along (1,1,0)/sqrt2 ------
def s4_parallel(Rc):
    Ii, Jj, Kk = Sint.astype(int).T
    s_ij = Ii + Jj                                  # parity fixed per chain (= parity of k)
    m = np.where(s_ij % 2 == 0, s_ij // 2, (s_ij - 1) // 2)
    lower = (m % 2 == 0)                            # lower member of its dimer
    mids = S[lower] + 0.5 * np.array([1.0, 1.0, 0.0]) / np.sqrt(2.0)
    m2 = np.einsum("ij,ij->i", mids, mids)
    own = (np.abs(mids[:, 0] - 0.5 / np.sqrt(2)) < 1e-9) & \
          (np.abs(mids[:, 1] - 0.5 / np.sqrt(2)) < 1e-9) & \
          (np.abs(mids[:, 2]) < 1e-9)               # origin's own dimer midpoint
    assert own.sum() == 1
    sel = (~own) & (m2 <= Rc**2)
    return float(np.sum(m2[sel] ** -2)) + tail(n_sites / 2.0, Rc)

S4par, S4parc = s4_parallel(R), s4_parallel(RCHK)
print(f"(C)  S4_parallel (ordered bracket)                = {S4par:.4f}  (R={RCHK:g}: {S4parc:.4f})")

phi_mf, phi_par = S4mf / C4, S4par / C4
print(f"\nphi_1 (mean-field, ADOPTED)  = {phi_mf:.4f}   sqrt = {np.sqrt(phi_mf):.4f}")
print(f"phi_1 (ordered bracket)      = {phi_par:.4f}   sqrt = {np.sqrt(phi_par):.4f}")
print("far-field density ratio      = 0.5000 (pairs = sites/2)")

ok = (abs(C4 - C4c) < 0.05 and abs(S4mf - S4mfc) < 0.05 and abs(S4par - S4parc) < 0.05)
print(f"\nconvergence: {'PASS' if ok else 'FAIL'}")
print("SCR-1 enters rho_Lambda multiplicatively as phi_1; verdict NOT")
print("recomputed here (factors multiply once, at the end).")
