"""PATCH 2900 — TWO PRE-REGISTERED TESTS ON THE B1 CURVATURE.

TEST 1: is the curvature coefficient exactly 1/5?
  Same integral as 2884/2897 (retarded-distance response, static Sea),
  fit D/beta = k(1 - c b^2 - c4 b^4). The 2897 fits omitted the beta^4
  term and used beta up to 0.2; hypothesis: 0.20129 was beta^4-
  contaminated and c is the exact rational 1/5.

TEST 2 (founder direction, 31 Jul 2026; 2898 direction (A)):
  does Sea entrainment reduce the curvature?
  Each DP is displaced toward the CP's RETARDED position (the induced
  response is attraction) with dimensionless strength eps:
      delta = eps * (1/d_out^2) * u_hat
  The force on the CP then points toward the DISPLACED DP position with
  magnitude (1/d_out^2)/|y'|^m.

  PRE-REGISTERED VERDICTS (recorded in chat before execution):
    c(eps) decreasing with a zero-crossing eps* -> direction (A) LIVE
    c(eps) flat or increasing                   -> direction (A) DEAD
    k(eps) -> 0 before c(eps) does              -> entrainment kills
                                                   coasting itself

RESULTS (this run):
  TEST 1: c = 0.200008 (=1/5 to 4e-5), invariant across m in {1,2,3} and
          four r-ranges; c4 = 0.02916 also invariant (candidate 7/240,
          NOT claimed).
  TEST 2: c(eps) falls steeply and crosses zero at eps* = 0.0589 with
          k(eps*) = -16.96 (healthy). Residual c4(eps*) = -0.373 (sign
          FLIPPED: beta^4 runaway, not drag). Direction (A) LIVE; one
          dial kills beta^2 only -- full self-consistency is the target.
"""
import numpy as np


def geometry(v, m, rmin, rmax, nr, nth, c=1.0):
    r = np.linspace(rmin, rmax, nr)
    th = np.linspace(0, np.pi, nth)
    R, TH = np.meshgrid(r, th, indexing='ij')
    yx, yp = R * np.cos(TH), R * np.sin(TH)
    w = (R ** 2) * np.sin(TH) * (r[1] - r[0]) * (th[1] - th[0]) * 2 * np.pi
    y = np.hypot(yx, yp)
    t2 = -y / c
    A = yx - v * t2
    disc = A * A * v * v + (c * c - v * v) * (A * A + yp * yp)
    s = (A * v + np.sqrt(disc)) / (c * c - v * v)
    d_out = c * s
    t1 = t2 - s                       # CP emission time
    cx = v * t1                       # CP retarded position (x; y = 0)
    return yx, yp, w, d_out, cx


def drive(v, eps, m=2.0, rmin=1.0, rmax=12.0, nr=480, nth=720):
    yx, yp, w, d_out, cx = geometry(v, m, rmin, rmax, nr, nth)
    amp = 1.0 / d_out ** 2
    ux, up = (cx - yx) / d_out, (0.0 - yp) / d_out   # DP -> retarded CP
    ypx, ypp = yx + eps * amp * ux, yp + eps * amp * up
    ynew = np.hypot(ypx, ypp)
    return float(np.sum((amp / ynew ** m) * (ypx / ynew) * w))


BETAS = np.array([0.01, 0.02, 0.03, 0.05, 0.08, 0.10, 0.15, 0.20])
X = np.column_stack([np.ones_like(BETAS), BETAS ** 2, BETAS ** 4])


def cfit(eps, m=2.0, rmin=1.0, rmax=12.0):
    y = np.array([drive(b, eps, m, rmin, rmax) for b in BETAS]) / BETAS
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    return coef[0], -coef[1] / coef[0], -coef[2] / coef[0]


if __name__ == '__main__':
    print("TEST 1 -- exact-1/5 hypothesis, robustness grid")
    for (m, rmin, rmax) in [(2.0, 1, 12), (2.0, 1, 20), (2.0, 2, 12),
                            (2.0, 0.5, 12), (1.0, 1, 12), (3.0, 1, 12)]:
        k, c2, c4 = cfit(0.0, m, rmin, rmax)
        print(f"  m={m} r=[{rmin},{rmax}]  k={k:9.4f}  c={c2:.6f}  "
              f"c4={c4:.5f}")
    print("  hypothesis: c = 1/5 = 0.200000 exactly "
          "(2897 value 0.20129 was beta^4-contaminated)")

    print("\nTEST 2 -- entrainment scan")
    print(f"{'eps':>6} | {'k':>10} | {'c':>10} | {'c4':>9}")
    for eps in [0.0, 0.05, 0.1, 0.2, 0.4]:
        k, c2, c4 = cfit(eps)
        print(f"{eps:6.2f} | {k:10.4f} | {c2:10.6f} | {c4:9.5f}")

    lo, hi = 0.05, 0.10
    for _ in range(25):
        mid = 0.5 * (lo + hi)
        _, c2, _ = cfit(mid)
        lo, hi = (mid, hi) if c2 > 0 else (lo, mid)
    eps_star = 0.5 * (lo + hi)
    k, c2, c4 = cfit(eps_star)
    print(f"\n  eps* = {eps_star:.6f}   k = {k:.4f}   c = {c2:.2e}   "
          f"c4(eps*) = {c4:.5f}")
