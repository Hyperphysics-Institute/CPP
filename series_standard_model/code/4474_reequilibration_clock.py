"""Patch 4474 -- founder: a discharging arc changes its separation, so its distance and angle to every neighbour change; the
neighbours feel new forces, are displaced and rotated, and re-equilibrate, so that part of each newly rotated arc lies along the
discharge direction.

Question taken up: does "re-equilibrate" give the same realignment time every time, as the cloud empties?
Toy models (not CPP dynamics), in units where the confinement gives a single particle angular frequency 1.

Part 1 -- one coordinate, settling into a new equilibrium after a step shift of size s.
  Linear restoring force: the swing period is the same for every s.  Nonlinear (a cubic term): it depends on s.
  Overdamped: no swing at all -- it creeps in, no wave per realignment.
Part 2 -- a cloud of N equal charges with 1/r^2 mutual repulsion, held by a confinement, in 2D.
  The small-oscillation frequencies (normal modes) are found from the curvature of the energy at equilibrium.
  Then 63% of the particles (one e-fold of energy, if energy goes with number) are removed, 37% kept, the rest re-settled, and the
  frequencies found again.  Printed: the centre-of-mass mode, and the median and highest internal modes, before and after.
  Harmonic confinement: the centre-of-mass mode stays exactly at 1 (a known theorem for identical particles: the mutual forces
  cancel in the sum; the ion-trap "centre-of-mass mode"; Dobson's harmonic potential theorem, PRL 73, 2244, 1994).  The internal
  modes shift.  With a little non-harmonic confinement the centre-of-mass mode shifts too.
Part 3 -- mixed signs (+ and - in each arc): the algebra of why the theorem fails, printed.
"""
import numpy as np
from scipy.optimize import minimize
from scipy.integrate import solve_ivp
rng = np.random.default_rng(1)

print("Part 1: period of the swing into a new equilibrium, step size s (linear k=1; nonlinear adds 0.5 x^3)")
for s in (0.01, 0.1, 0.3, 1.0):
    out = []
    for c3 in (0.0, 0.5):
        f = lambda t, y: [y[1], -(y[0] - 0) - c3*y[0]**3]      # starts displaced by s from the new equilibrium at 0
        sol = solve_ivp(f, (0, 60), [s, 0], rtol=1e-11, atol=1e-13, dense_output=True)
        t = np.linspace(0, 60, 60001); x = sol.sol(t)[0]
        i = np.where((x[:-1] < 0) & (x[1:] >= 0))[0]
        up = t[i] - x[i]*(t[i+1]-t[i])/(x[i+1]-x[i])          # interpolated upward zero crossings
        out.append(np.mean(np.diff(up)))
    print(f"  s = {s:<5}: linear period {out[0]:.6f} (2 pi = {2*np.pi:.6f}); nonlinear period {out[1]:.6f}")
g = 3.0
f = lambda t, y: [y[1], -y[0] - g*y[1]]
sol = solve_ivp(f, (0, 30), [1.0, 0], max_step=0.01); x = sol.y[0]
print(f"  overdamped (drag 3): sign changes of the displacement = {int(np.sum(np.diff(np.sign(x[np.abs(x)>1e-9])) != 0))} (creeps in; no swing)")

def energy(flat, q, k4):
    r = flat.reshape(-1, 2)
    e = 0.5*np.sum(r**2) + 0.25*k4*np.sum(np.sum(r**2, 1)**2)
    d = r[:, None, :] - r[None, :, :]
    dist = np.sqrt(np.sum(d**2, -1) + np.eye(len(r)))
    qq = np.outer(q, q)
    iu = np.triu_indices(len(r), 1)
    return e + 0.02*np.sum(qq[iu]/dist[iu])
def settle(r, q, k4):
    res = minimize(energy, r.ravel(), args=(q, k4), jac=num_grad, method="BFGS", options={"gtol": 1e-12, "maxiter": 50000})
    return res.x
def hessian(x, q, k4, h=1e-6):
    n = x.size; H = np.zeros((n, n))
    for i in range(n):
        e = np.zeros(n); e[i] = h
        gp = num_grad(x+e, q, k4); gm = num_grad(x-e, q, k4)
        H[:, i] = (gp-gm)/(2*h)
    return 0.5*(H+H.T)
def num_grad(x, q, k4, h=None):
    """analytic gradient of energy()"""
    r = x.reshape(-1, 2)
    rr = np.sum(r**2, 1)
    g = r + k4*rr[:, None]*r
    d = r[:, None, :] - r[None, :, :]
    dist2 = np.sum(d**2, -1) + np.eye(len(r))
    qq = np.outer(q, q)*(1-np.eye(len(r)))
    g += -0.02*np.sum((qq/dist2**1.5)[:, :, None]*d, 1)
    return g.ravel()
for label, k4 in (("Part 2, harmonic hold", 0.0), ("Part 2, slightly non-harmonic hold (quartic 0.05)", 0.05)):
    N = 30
    r0 = rng.normal(0, 0.5, (N, 2)); q = np.ones(N)
    keep = rng.permutation(N)[:int(round(N*0.37))]
    res = []
    for rr, qq in ((r0, q), (r0[keep], q[keep])):
        x = settle(rr, qq, k4); H = hessian(x, qq, k4); n = len(qq)
        com = np.zeros(2*n); com[0::2] = 1/np.sqrt(n)               # every particle moved equally in x
        w = np.sqrt(np.clip(np.linalg.eigvalsh(H), 0, None)); wi = w[w > 0.05]   # drop the rotation (zero) mode
        res.append((np.sqrt(com @ H @ com), np.linalg.norm(H @ com - (com @ H @ com)*com), np.median(wi), wi.max()))
    (a, ra, ma, la), (b, rb, mb, lb) = res
    print(f"{label}: N {N} -> {len(keep)} (63% removed: one e-fold if the energy goes with the number)")
    print(f"  centre-of-mass mode: {a:.7f} -> {b:.7f} (change {abs(b-a)/a:.1e}; is it an exact mode? residual {ra:.0e}, {rb:.0e})")
    print(f"  internal modes (rotation excluded): median {ma:.4f} -> {mb:.4f} (change {abs(mb-ma)/ma:.0%}); highest {la:.4f} -> {lb:.4f}")
print("Part 3: d2/dt2 of sum(q_i r_i) = sum_i (q_i/m) F_i; a mutual pair force F_ij = -F_ji contributes (q_i - q_j) F_ij / m,")
print("  which is zero for like charges (Part 2) but 2 F_ij / m for a + and - pair: in arcs the mutual forces do move the radiating sum,")
print("  so the theorem does not carry over; the clock would then depend on the arc-arc forces and on how many arcs are left.")
print("Required for Lyman-alpha: the radiating mode's frequency fixed to ~4e-8 per e-fold (4473 3).")
