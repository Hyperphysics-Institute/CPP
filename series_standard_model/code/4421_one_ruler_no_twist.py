"""Patch 4421 -- founder: the plates and interplate DPs are one integrated system; the forces on them have the same effects in
that frame whatever the plates' orientation; it is the Michelson-Morley problem with the same resolution, contraction along the
motion through the absolute frame, mediated by the PSR contracting in the appropriate directions.

Claim tested (Lorentz's theorem of corresponding states, with the PSR as the common ruler): if EVERY pair force is a function
of the separation measured in the moving CP's PSR, and the PSR is shortened by 1/gamma along the motion (4409), every pair
potential becomes (1/gamma) U(|Lambda r|), Lambda = diag(gamma, 1) -- the form the census channel already gives the electric
force (4411: R(1 - n.v) = |Lambda r|/gamma; force -(1 - v^2) grad of the convection potential). Then the rest equilibrium s_i,
contracted to Lambda^-1 s_i, is an equilibrium of the moving structure at every tilt: zero force on every part, zero couple.

Model (2D, c = 1): a capacitor of two plates, 5 charges each (+1 and -1), neighbours in each plate joined by stiff springs,
the plates joined across the gap by stiff spacers and diagonal braces (a rigid frame); every charge interacts electrically with every other.
  Case A: every force (electric and binding) in PSR units (census form).
  Case B: electric force in census form, binding forces in absolute units (not contracted).
Reported at the contracted rest shape, for tilts 0..90 degrees: largest residual force on any charge, and the total couple
on the capacitor.
"""
import numpy as np
from scipy.optimize import minimize
N, gap, a, k, kspace = 5, 1.0, 0.5, 400.0, 400.0
q = 0.2*np.array([1.0]*N + [-1.0]*N)       # charges kept modest so the springs hold the shape
springs = [(i, i+1, a, k) for i in range(N-1)] + [(N+i, N+i+1, a, k) for i in range(N-1)] \
        + [(i, N+i, gap, kspace) for i in range(N)] + [(i, N+i+1, np.hypot(a, gap), k) for i in range(N-1)]
pairs = [(i, j) for i in range(2*N) for j in range(i+1, 2*N)]

def energy_and_forces(P, lam_e, lam_b, s_e, s_b):
    """P: (2N,2) positions. lam_*: diag scalings applied to separations; s_*: overall prefactors."""
    F = np.zeros_like(P); E = 0.0
    for i, j in pairs:
        d = P[i] - P[j]; dl = lam_e*d; r = np.linalg.norm(dl)
        E += s_e*q[i]*q[j]/r
        g = -s_e*q[i]*q[j]/r**3 * (lam_e*dl)          # gradient wrt P[i]
        F[i] -= g; F[j] += g
    for i, j, L, kk in springs:
        d = P[i] - P[j]; dl = lam_b*d; r = np.linalg.norm(dl)
        E += s_b*0.5*kk*(r - L)**2
        g = s_b*kk*(r - L)/r * (lam_b*dl)
        F[i] -= g; F[j] += g
    return E, F

# rest equilibrium
P0 = np.array([[x*a, 0.0] for x in range(N)] + [[x*a, gap] for x in range(N)], dtype=float)
one = np.array([1.0, 1.0])
fun = lambda z: energy_and_forces(z.reshape(-1, 2), one, one, 1.0, 1.0)[0]
jac = lambda z: -energy_and_forces(z.reshape(-1, 2), one, one, 1.0, 1.0)[1].ravel()
res = minimize(fun, P0.ravel(), jac=jac, method="BFGS", options={"gtol": 1e-10, "maxiter": 50000})
for _ in range(5):
    res = minimize(fun, res.x, jac=jac, method="BFGS", options={"gtol": 1e-11, "maxiter": 50000})
S = res.x.reshape(-1, 2); S -= S.mean(axis=0)
_, Frest = energy_and_forces(S, one, one, 1.0, 1.0)
print(f"rest equilibrium: largest residual force {np.abs(Frest).max():.1e}; gap {np.linalg.norm(S[N+2]-S[2]):.4f}")

v = 0.5; g = 1/np.sqrt(1 - v**2); Lam = np.array([g, 1.0])
print(f"moving at v = {v} (gamma = {g:.4f}); structure = rest shape rotated by the tilt, then contracted along the motion")
for case, lam_b, s_b, shape in (("A (every force in PSR units), contracted shape", Lam, 1/g, Lam),
                                ("B (binding in absolute units), contracted shape", one, 1.0, Lam),
                                ("B (binding in absolute units), uncontracted shape", one, 1.0, one)):
    print(f"  Case {case}:")
    for tilt in (0, 30, 45, 60, 90):
        t = np.radians(tilt); R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
        P = (S @ R.T)/shape                                # tilted rest structure, contracted or not
        _, F = energy_and_forces(P, Lam, lam_b, 1/g, s_b)
        torque = np.sum(P[:, 0]*F[:, 1] - P[:, 1]*F[:, 0])
        print(f"    tilt {tilt:2d} deg: largest force on a charge {np.abs(F).max():.2e}   total couple {torque:+.2e}")
print("  A: every part in equilibrium and no couple at every tilt (no twist, contraction along the motion only).")
print("  B (unrelaxed): neither shape is an equilibrium; couple ~0 at 0 and 90 degrees, peaking near 45.")

def relax(P, lam_b, s_b):
    f = lambda z: energy_and_forces(z.reshape(-1, 2), Lam, lam_b, 1/g, s_b)[0]
    j = lambda z: -energy_and_forces(z.reshape(-1, 2), Lam, lam_b, 1/g, s_b)[1].ravel()
    r = minimize(f, P.ravel(), jac=j, method="BFGS", options={"gtol": 1e-10, "maxiter": 50000})
    for _ in range(3):
        r = minimize(f, r.x, jac=j, method="BFGS", options={"gtol": 1e-11, "maxiter": 50000})
    Q = r.x.reshape(-1, 2)
    _, F = energy_and_forces(Q, Lam, lam_b, 1/g, s_b)
    gapvec = Q[N:].mean(axis=0) - Q[:N].mean(axis=0)
    return Q, np.abs(F).max(), np.degrees(np.arctan2(gapvec[1], gapvec[0]*g))  # gap-axis angle in PSR-scaled coordinates

print("Relaxed (the structure free to deform and turn); gap-axis angle measured in PSR-scaled coordinates:")
gap0 = np.degrees(np.arctan2(*(S[N:].mean(axis=0) - S[:N].mean(axis=0))[::-1]))
for case, lam_b, s_b, shape in (("A, every force in PSR units", Lam, 1/g, Lam),
                                ("A', PSR units but binding prefactor 1 (mismatched)", Lam, 1.0, Lam),
                                ("B, binding in absolute units", one, 1.0, one)):
    row = []
    for tilt in (30, 45, 60):
        t = np.radians(tilt); R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
        Q, fmax, ang = relax((S @ R.T)/shape, lam_b, s_b)
        row.append(f"start {tilt:2d}: tilt after relaxing {ang - gap0:6.2f} deg (0 = untilted, gap across the motion) (force {fmax:.0e})")
    print(f"  {case}:\n    " + "\n    ".join(row))
print("  A and A': the capacitor stays at whatever tilt it starts (no preferred orientation, no twist): with every force")
print("  a function of PSR-measured separation, the total energy depends only on Lambda x, which is rotation-free in PSR")
print("  units, whatever the prefactors. The common prefactor matters only for the shape to be exactly the contracted rest")
print("  shape. B: the capacitor turns to a preferred orientation -- the twist.")
