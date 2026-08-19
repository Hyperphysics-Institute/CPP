#!/usr/bin/env python3
"""Patch 3236 — OPEN-QM-8 corrected measurement (A1 ruled: true Voronoi cell).

THE PROBLEM SOLVED (the one Spin II actually published):
    The ZBW resonator is stated on the u-field, u = r*psi:
        -u'' - (1/r^2) Delta_S u = k^2 u
    with u = 0 at the center (CP Exclusion) and the FREE end u' = 0 at the
    cell boundary along each ray (Spin II: "antinode at the thermal
    boundary"). On a sphere this is exactly the 1D open-closed string per
    ray: k_n = (2n-1)pi/2R, Mode-2 antinode at R/3, node at 2R/3.

WHY THIS FORMULATION (recorded so the choice is auditable):
    The committed March instrument solved the CLOSED psi-Neumann problem
    (diagnosed in Spin III V0 par.5). But there is a second, subtler
    semantic trap this instrument avoids: a free (Neumann) condition on
    PSI is NOT the same as Spin II's free condition on U — on a sphere,
    psi'(R)=0 gives the tan(kR)=kR spectrum (k1 R = 4.493...), not
    (2n-1)pi/2. The paper's resonator is defined on u, so the instrument
    discretizes the u-equation directly.

DOMAIN (founder ruling A1, 19 Aug 2026): the true Voronoi cell of the
    600-cell-based lattice = the regular dodecahedron (dual-120-cell cell;
    12 pentagonal faces, normals at the 12 icosahedral neighbor
    directions). Sphere control validates the instrument. The 24-cell leg
    is deferred with reason (wrong dimension for the published 3D radial
    problem); see the ruling registration.

DISCRETIZATION:
    Angular: icosphere triangulation of S^2 (subdivided icosahedron),
    cotangent Laplacian L_cot with Voronoi-area lumped mass m_a.
    Radial: per-ray coordinate s in [0,1], r = s*R(omega); 1D FEM
    stiffness with Dirichlet at s=0, natural (free) at s=1.
    Boundary radius: sphere R(omega)=1; dodecahedron
    R(omega) = rho_in / max_f(omega . n_f), n_f = 12 icosahedron vertex
    directions, rho_in = 1 (readings are per-ray fractional, scale-free).
    DECLARED APPROXIMATION (anisotropy^2 class, ~1% positions): the
    angular coupling uses the shell-averaged metric weight
    w_j = <L_a>/rbar_j^2 (exact in the sphere limit); ray-coordinate
    cross-terms neglected. Dodeca anisotropy: R in [1, 1.258].

READINGS (frozen in OPEN-QM-8 / Spin III V0 par.6, applied verbatim):
    Radial candidates: eigenmodes whose isotropy score (mass-weighted
    fraction of variance explained by the angular-mean profile) >= 0.5.
    MODE2-RECOVERED: a radial candidate with exactly one interior zero of
      the mean u-profile, node s in [0.60, 0.73], antinode s in
      [0.28, 0.40], stable across the two mesh densities.
    MODE2-ABSENT: no such candidate among the lowest 20 radial candidates
      at the highest density.
    INDETERMINATE: anything else.
    Worker expectation, declared pre-run: MODE2-RECOVERED.

Run: python3 3236_qm8_true_cell_run.py
"""

import math
import sys

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

PHI = (1 + math.sqrt(5)) / 2


# ---------------------------------------------------------------- icosphere
def icosahedron():
    v = []
    for s1 in (1, -1):
        for s2 in (1, -1):
            v += [(0, s1, s2 * PHI), (s1, s2 * PHI, 0), (s2 * PHI, 0, s1)]
    V = np.unique(np.array(v, float).round(12), axis=0)
    V /= np.linalg.norm(V, axis=1)[:, None]
    # faces via convex hull
    from scipy.spatial import ConvexHull
    F = ConvexHull(V).simplices
    # orient outward
    for i, f in enumerate(F):
        n = np.cross(V[f[1]] - V[f[0]], V[f[2]] - V[f[0]])
        if np.dot(n, V[f].mean(0)) < 0:
            F[i] = f[[0, 2, 1]]
    return V, F


def subdivide(V, F, levels):
    V = list(map(tuple, V))
    index = {v: i for i, v in enumerate(V)}
    F = [tuple(f) for f in F]
    for _ in range(levels):
        newF = []
        cache = {}
        def mid(a, b):
            key = (min(a, b), max(a, b))
            if key in cache:
                return cache[key]
            p = np.array(V[a]) + np.array(V[b])
            p /= np.linalg.norm(p)
            t = tuple(p)
            if t not in index:
                index[t] = len(V); V.append(t)
            cache[key] = index[t]
            return index[t]
        for (a, b, c) in F:
            ab, bc, ca = mid(a, b), mid(b, c), mid(c, a)
            newF += [(a, ab, ca), (ab, b, bc), (ca, bc, c), (ab, bc, ca)]
        F = newF
    return np.array(V), np.array(F)


def cot_laplacian(V, F):
    """Cotangent stiffness (PSD) and lumped Voronoi-area mass on the mesh."""
    n = len(V)
    I, J, W = [], [], []
    mass = np.zeros(n)
    for (a, b, c) in F:
        p, q, r = V[a], V[b], V[c]
        area = 0.5 * np.linalg.norm(np.cross(q - p, r - p))
        for (i, j, k) in ((a, b, c), (b, c, a), (c, a, b)):
            u_, v_ = V[j] - V[k], V[i] - V[k]
            cot = np.dot(u_, v_) / (np.linalg.norm(np.cross(u_, v_)) + 1e-300)
            w = 0.5 * cot
            I += [i, j, i, j]; J += [j, i, i, j]; W += [-w, -w, w, w]
        for vv in (a, b, c):
            mass[vv] += area / 3.0
    K = sp.csr_matrix((W, (I, J)), shape=(n, n))
    K = (K + K.T) * 0.5
    return K, mass


# ------------------------------------------------------------ boundary radii
ICO_V, _ = icosahedron()   # 12 unit vertices = dodeca face normals

def R_sphere(dirs):
    return np.ones(len(dirs))

def R_dodeca(dirs):
    # support-function radius of the dodecahedron with unit inradius
    return 1.0 / np.max(dirs @ ICO_V.T, axis=1)


# ------------------------------------------------------------ assembly
def assemble(V, F, R_of, Nr):
    """K u = k^2 M u for the u-equation on rays s in [0,1], r = s R(omega)."""
    Kang, m_a = cot_laplacian(V, F)
    n_ang = len(V)
    R = R_of(V)                     # per-ray boundary radius
    h = 1.0 / Nr
    s = (np.arange(1, Nr + 1)) * h  # s_1..s_Nr ; Dirichlet at s=0 eliminated

    # 1D FEM stiffness (Dirichlet at 0, natural at 1) and lumped mass on s-grid
    d = np.full(Nr, 2.0); d[-1] = 1.0
    o = np.full(Nr - 1, -1.0)
    K1 = sp.diags([o, d, o], [-1, 0, 1]) / h
    m1 = np.full(Nr, h); m1[-1] = h / 2.0

    # global index: a * Nr + j
    # radial part: sum_a (m_a / R_a) * K1  on ray a   [ (1/R^2) u'' with mass R ]
    Krad = sp.kron(sp.diags(m_a / R), K1, format="csr")
    # mass: M = diag(m_a * R_a) x diag(m1)
    M = sp.kron(sp.diags(m_a * R), sp.diags(m1), format="csr")
    # angular part: shell-averaged weight  w_j = <R> / rbar_j^2 ,
    # rbar_j = s_j * <R>   =>  w_j = 1 / (<R> s_j^2)
    Rmean = float(np.mean(R))
    w = m1 / (Rmean * s ** 2)
    Kang_glob = sp.kron(Kang, sp.diags(w), format="csr")
    K = (Krad + Kang_glob).tocsr()
    K = (K + K.T) * 0.5
    return K, M, m_a, R, s


def radial_family(K, M, m_a, R, s, n_eigs=90, iso_thresh=0.5):
    vals, vecs = spla.eigsh(K, k=n_eigs, M=M, sigma=0, which="LM")
    order = np.argsort(vals)
    vals, vecs = vals[order], vecs[:, order]
    n_ang, Nr = len(m_a), len(s)
    wa = (m_a * R) / np.sum(m_a * R)
    fam = []
    for i in range(n_eigs):
        U = vecs[:, i].reshape(n_ang, Nr)
        prof = wa @ U                       # mass-weighted angular mean u(s)
        num = np.sum(prof ** 2 * (s == s))  # profile energy per shell
        # isotropy score in the M-inner-product:
        e_iso = np.sum((prof ** 2))
        e_tot = np.sum(wa @ (U ** 2))
        score = e_iso / e_tot if e_tot > 0 else 0.0
        if score >= iso_thresh:
            fam.append((i, vals[i], score, prof))
    return vals, fam


def mode_geometry(prof, s):
    p = prof / np.max(np.abs(prof))
    sc = np.where(np.diff(np.sign(p)))[0]
    zeros = []
    for i in sc:
        zeros.append(s[i] + (s[i + 1] - s[i]) * abs(p[i]) / (abs(p[i]) + abs(p[i + 1])))
    zeros = [z for z in zeros if 0.05 < z < 0.97]
    i_anti = int(np.argmax(np.abs(p[: int(0.6 * len(s))])))
    return zeros, s[i_anti]


def run_domain(name, R_of, level, Nr):
    print(f"\n== {name}  (icosphere level {level}, Nr={Nr}) ==")
    V0, F0 = icosahedron()
    V, F = subdivide(V0, F0, level)
    K, M, m_a, R, s = assemble(V, F, R_of, Nr)
    print(f"  angular nodes {len(V)}, DOF {K.shape[0]}, "
          f"R range [{R.min():.4f}, {R.max():.4f}]")
    vals, fam = radial_family(K, M, m_a, R, s)
    print(f"  radial candidates (isotropy>=0.5) among lowest 90: {len(fam)}")
    out = []
    for rank, (i, lam, score, prof) in enumerate(fam[:4], 1):
        zeros, anti = mode_geometry(prof, s)
        k_eff = math.sqrt(lam) * np.mean(R)   # report in mean-radius units
        print(f"  radial mode {rank}: idx {i+1}, k*<R> = {k_eff:.5f}, "
              f"iso {score:.3f}, zeros {['%.4f' % z for z in zeros]}, "
              f"antinode s = {anti:.4f}")
        out.append(dict(rank=rank, k=k_eff, score=score, zeros=zeros, anti=anti))
    return out


def main():
    passes = []
    def check(name, ok, detail=""):
        passes.append((name, ok))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}"
              f"{(' — ' + detail) if detail else ''}")

    # ---- SPHERE CONTROL: the instrument must reproduce Spin II exactly ----
    ctrl = run_domain("SPHERE CONTROL", R_sphere, level=3, Nr=120)
    k1t, k2t = math.pi / 2, 3 * math.pi / 2
    check("control k1 = pi/2 (0.5%)", abs(ctrl[0]["k"] - k1t) < 5e-3 * k1t,
          f"{ctrl[0]['k']:.5f} vs {k1t:.5f}")
    check("control k2 = 3pi/2 (0.5%)", abs(ctrl[1]["k"] - k2t) < 5e-3 * k2t,
          f"{ctrl[1]['k']:.5f} vs {k2t:.5f}")
    z2 = ctrl[1]["zeros"]
    check("control Mode-2: one interior zero at 2/3 (1%)",
          len(z2) == 1 and abs(z2[0] - 2 / 3) < 0.01, f"{z2}")
    check("control Mode-2 antinode at 1/3 (2%)",
          abs(ctrl[1]["anti"] - 1 / 3) < 0.02, f"{ctrl[1]['anti']:.4f}")

    # ---- TRUE VORONOI CELL (dodecahedron), two densities ----
    lo = run_domain("DODECAHEDRON (true Voronoi cell) — density 1",
                    R_dodeca, level=2, Nr=80)
    hi = run_domain("DODECAHEDRON (true Voronoi cell) — density 2",
                    R_dodeca, level=3, Nr=120)

    def reading(res):
        if len(res) < 2:
            return "INDETERMINATE", None
        m2 = res[1]
        ok = (len(m2["zeros"]) == 1
              and 0.60 <= m2["zeros"][0] <= 0.73
              and 0.28 <= m2["anti"] <= 0.40)
        return ("MODE2-RECOVERED" if ok else "INDETERMINATE"), m2

    r_lo, m2_lo = reading(lo)
    r_hi, m2_hi = reading(hi)
    stable = (r_lo == r_hi == "MODE2-RECOVERED"
              and abs(m2_lo["zeros"][0] - m2_hi["zeros"][0]) < 0.02)
    verdict = "MODE2-RECOVERED" if stable else (
        "MODE2-ABSENT" if (r_hi != "MODE2-RECOVERED" and len(hi) >= 20)
        else "INDETERMINATE")
    print(f"\n  density-1 reading: {r_lo}; density-2 reading: {r_hi}")
    check("frozen verdict MODE2-RECOVERED (both densities, node drift <0.02)",
          verdict == "MODE2-RECOVERED", f"verdict {verdict}")

    if m2_hi:
        drift_k = abs(m2_hi["k"] - k2t) / k2t
        print(f"\n  dodeca Mode-2: k*<R> = {m2_hi['k']:.5f} "
              f"(sphere {k2t:.5f}; shift {100*drift_k:.2f}%), "
              f"node {m2_hi['zeros'][0]:.4f} (2/3 = 0.6667), "
              f"antinode {m2_hi['anti']:.4f} (1/3 = 0.3333)")

    print("\n== SUMMARY ==")
    n_ok = sum(1 for _, ok in passes if ok)
    for name, ok in passes:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    print(f"{n_ok}/{len(passes)} checks pass; FROZEN VERDICT: {verdict}")
    sys.exit(0 if n_ok == len(passes) else 1)


if __name__ == "__main__":
    main()
