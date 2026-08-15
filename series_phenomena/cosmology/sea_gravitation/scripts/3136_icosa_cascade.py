#!/usr/bin/env python
"""Patch 3136 -- D-SUBPSR-FIELD PASS 4: the cascade on the founder's
ICOSAHEDRAL twelve, off-lattice.

WHY OFF-LATTICE: icosahedral point symmetry is incompatible with 3D
translational periodicity (no Bravais lattice carries it) -- the
corpus's substrate is the 600-cell projection, whose VERTEX FIGURE is
the icosahedron. The physically decisive content for the gate is the
DIRECTION SET; so pass 4 propagates walkers in continuum space along
the twelve icosahedral unit vectors under R-OUTWARD-FANOUT (equal
split among outward-component directions = uniform random choice per
walker, which reproduces the even-split measure exactly), and runs
the IDENTICAL instrument on the FCC/cuboctahedral twelve as the
control. GATE (registered prediction, 3135): the icosahedral set
suppresses the degree-4 anisotropy that the cuboctahedral set shows
at the +/-10% class, leaving a small degree-6 residual (FACT G1 /
AUTOMATON-2 +/-0.4% class).

Measurements:
 (1) THE GATE: spherical-harmonic anisotropy power (l = 4 and l = 6)
     of the pulse shell at large N, icosa vs cubocta.
 (2) THE BAND: sigma_r/<r> vs N under the icosahedral set
     (geometry-robustness of the founder's ~10%).
 (3) the radial profile: r^2-compensated density under continuous
     injection (small-s kernel class).
"""
import numpy as np

PHI = (1 + 5**0.5)/2

def icosa_dirs():
    v = []
    for a in (1.0, -1.0):
        for b in (PHI, -PHI):
            v += [(0, a, b), (a, b, 0), (b, 0, a)]
    v = np.array(v)/np.sqrt(1 + PHI**2)
    return v

def fcc_dirs():
    v = [(a, b, 0) for a in (1, -1) for b in (1, -1)] + \
        [(a, 0, b) for a in (1, -1) for b in (1, -1)] + \
        [(0, a, b) for a in (1, -1) for b in (1, -1)]
    return np.array(v, float)/np.sqrt(2.0)

def cascade(dirs, M, N, rng):
    """M walkers, N hops, R-OUTWARD-FANOUT: uniform choice among
    outward-component directions (all 12 at the origin)."""
    X = np.zeros((M, 3))
    for t in range(N):
        dots = X @ dirs.T                      # (M, 12)
        ok = dots > 1e-12
        ok[np.abs(X).sum(1) < 1e-12] = True    # origin: all 12
        # uniform choice among allowed: sample by normalized cumsum
        w = ok.astype(float)
        w /= w.sum(1, keepdims=True)
        c = np.cumsum(w, 1)
        u = rng.random((M, 1))
        pick = (u > c).sum(1)                  # index of chosen direction
        X += dirs[pick]
    return X

def sph_harm_power(X, l):
    """Anisotropy power at degree l for unit directions of X (real
    Y_lm sum over m, normalized so an isotropic ensemble -> ~0)."""
    from scipy.special import sph_harm_y
    r = np.linalg.norm(X, axis=1)
    u = X/r[:, None]
    th = np.arccos(np.clip(u[:, 2], -1, 1))
    ph = np.arctan2(u[:, 1], u[:, 0])
    tot = 0.0
    for m in range(-l, l+1):
        Y = sph_harm_y(l, m, th, ph)
        tot += np.abs(Y.mean())**2
    return 4*np.pi*tot / (2*l + 1)

if __name__ == "__main__":
    rng = np.random.default_rng(7)
    M, N = 4_000_000, 30
    print(f"walkers M = {M:,}, hops N = {N}")
    out = {}
    for name, dirs in (("ICOSA", icosa_dirs()), ("CUBOCTA", fcc_dirs())):
        X = cascade(dirs, M, N, rng)
        r = np.linalg.norm(X, axis=1)
        mean_r, sig = float(r.mean()), float(r.std())
        p4 = sph_harm_power(X, 4)
        p6 = sph_harm_power(X, 6)
        # convert power to an equivalent fractional flux modulation:
        # delta f/f ~ sqrt((2l+1) * P_l) (order-of-magnitude convention,
        # same convention both sets -> ratio is the clean statement)
        a4 = np.sqrt(9*p4); a6 = np.sqrt(13*p6)
        out[name] = (mean_r, sig, a4, a6)
        print(f"[{name:7}] <r> = {mean_r:6.3f}  sigma_r/<r> = {sig/mean_r:6.4f}  "
              f"aniso(l=4) ~ {100*a4:6.3f}%  aniso(l=6) ~ {100*a6:6.3f}%")
    print(f"\nGATE: l=4 suppression, icosa vs cubocta = "
          f"{out['CUBOCTA'][2]/max(out['ICOSA'][2],1e-12):8.1f}x")
    print("[prediction registered in 3135: icosa suppresses degree-4;")
    print(" residual anisotropy at the degree-6 / AUTOMATON-2 class]")

    print("\n(2) THE BAND vs N (icosahedral):")
    for Nb in (6, 10, 14, 18, 22, 30, 40):
        Xb = cascade(icosa_dirs(), 400_000, Nb, rng)
        rb = np.linalg.norm(Xb, axis=1)
        print(f"   N = {Nb:3d}: <r> = {rb.mean():7.3f}  "
              f"sigma_r/<r> = {rb.std()/rb.mean():6.4f}")

    print("\n(3) radial profile class (continuous injection, icosa):")
    # superpose pulses of ages 1..N: density(r) ~ sum_t hist_t(r);
    # flux ~ density * radial speed; report r^2-compensated density
    rng2 = np.random.default_rng(11)
    Mi = 300_000
    acc = np.zeros(60)
    edges = np.linspace(0.5, 24.5, 61)
    for age in range(1, 31):
        Xa = cascade(icosa_dirs(), Mi, age, rng2)
        ra = np.linalg.norm(Xa, axis=1)
        h, _ = np.histogram(ra, bins=edges)
        acc += h/Mi
    ctr = 0.5*(edges[:-1] + edges[1:])
    shell = 4*np.pi*ctr**2*(edges[1]-edges[0])
    dens = acc/shell
    norm = np.mean((ctr**2*dens)[(ctr > 10) & (ctr < 14)])
    for i in range(0, 26, 3):
        print(f"   r = {ctr[i]:5.2f}: (r^2 dens)/norm = {ctr[i]**2*dens[i]/norm:6.3f}")
