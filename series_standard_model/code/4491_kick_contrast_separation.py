#!/usr/bin/env python3
"""Patch 4491 illustration script: one shared kick, the path separation, and the blur.

The founder (4491) explains the blurring of atom fringes by scattered light as momentum kicks that change the atom's
KE/DP-arcs, which go through both slits and guide where the atom lands. The standard account (Chapman et al., PRL 75,
3783, 1995) is the same kick with one addition: the kick multiplies the atom's guiding wave in BOTH arms by
exp(i q.x), so the two arms pick up a phase difference q.d that depends on how far apart the arms are (d) where the
photon hits. Averaged over photon directions, the fringe contrast is C(d) = |<exp(i q.d)>|. This script shows:

  K1  C(d) for one scattered photon (dipole emission, axis perpendicular to d): falls as d grows, reaches zero near
      d = lambda/2 and partly revives beyond -- the loss-and-revival Chapman et al. observed. A kick felt on one side
      only would give a loss that does not depend on d.
  K2  Long wavelength (lambda = 10 d): one photon leaves C close to 1; N photons give C^N (independent scatterings):
      faint kicks add up.
  K3  Sorting: atoms whose scattered photon went into a narrow cone keep sharp fringes (contrast near 1, shifted), as
      Chapman et al. recovered by correlating atoms with photon direction.

Checked against the closed form for this model, C = j0(kd) - j2(kd)/2 (first zero 0.4367 lambda; revival 0.3355 at 0.6737 lambda;
the value at the minimum is Monte-Carlo noise, the true value 0). numpy only; these are illustrations of the standard formula, not tests of CPP. Exit 0 if every check holds.
"""
import numpy as np

rng = np.random.default_rng(4491)


def sample_dipole(n):
    """Photon emission directions for a dipole along z: density ~ sin^2(theta). Rejection sampling."""
    out = []
    while len(out) < n:
        v = rng.normal(size=(n, 3))
        v /= np.linalg.norm(v, axis=1)[:, None]
        sin2 = 1 - v[:, 2] ** 2
        keep = rng.random(n) < sin2
        out.extend(v[keep])
    return np.array(out[:n])


N = 400000
dirs = sample_dipole(N)
k = 2 * np.pi  # wavelength = 1
k_in = np.array([0.0, 1.0, 0.0])  # incident photon along y; d along x
q = k * (k_in[None, :] - dirs)     # momentum given to the atom
qx = q[:, 0]

rows = []
d_grid = np.linspace(0, 1.5, 301)
C = np.array([abs(np.mean(np.exp(1j * qx * d))) for d in d_grid])
i_min = int(np.argmin(C[: int(0.9 / 1.5 * 300)]))
d_min, C_min = d_grid[i_min], C[i_min]
after = C[i_min:]
C_rev = after.max()
d_rev = d_grid[i_min + int(np.argmax(after))]
rows.append(("K1 C(0)", "d = 0", f"{C[0]:.4f}", abs(C[0] - 1) < 1e-9))
rows.append(("K1 first minimum", f"d = {d_min:.3f} lambda", f"{C_min:.4f}", C_min < 0.05 and abs(d_min - 0.4367) < 0.006))
rows.append(("K1 revival", f"d = {d_rev:.3f} lambda", f"{C_rev:.4f}", abs(C_rev - 0.3355) < 0.005 and abs(d_rev - 0.6737) < 0.006))

d_long = 0.1  # lambda = 10 d


def closed_form(x):
    """Dipole emission, axis perpendicular to d: C = j0(x) - j2(x)/2, x = k d."""
    j0 = np.sin(x) / x
    j2 = (3 / x ** 2 - 1) * np.sin(x) / x - 3 * np.cos(x) / x ** 2
    return j0 - j2 / 2


C1 = abs(np.mean(np.exp(1j * qx * d_long)))
C1_exact = closed_form(k * d_long)
for n in (1, 10, 100):
    mc, ex = C1 ** n, C1_exact ** n
    rows.append((f"K2 {n} photon(s), lambda = 10 d", f"exact {ex:.4g}", f"{mc:.4f}", abs(mc - ex) < 0.01 * max(ex, 1e-3) + 2e-4))

d_s = round(float(d_min), 3)  # at the first minimum of K1
cone = dirs[:, 0] > np.cos(np.radians(10))  # photons scattered within 10 degrees of +x
C_all = abs(np.mean(np.exp(1j * qx * d_s)))
C_cone = abs(np.mean(np.exp(1j * qx[cone] * d_s)))
rows.append(("K3 all atoms", f"d = {d_s} lambda", f"{C_all:.4f}", C_all < 0.1))
rows.append(("K3 sorted by photon in 10-deg cone", f"d = {d_s} lambda", f"{C_cone:.4f}", C_cone > 0.9))

print("KICK-CONTRAST TABLE (Patch 4491)  contrast C = |<exp(i q.d)>|, dipole emission, 400000 photons")
for name, scope, val, ok in rows:
    print(f"{name:38s} {scope:20s} C = {val:8s} {'PASS' if ok else 'FAIL'}")
n_ok = sum(r[3] for r in rows)
print(f"{n_ok}/{len(rows)} PASS")
raise SystemExit(0 if n_ok == len(rows) else 1)
