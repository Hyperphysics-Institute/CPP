#!/usr/bin/env python3
"""4355 -- the far field under the registered relay (A3'/AP-3/AP-4; GR-1j Theorem 'Exact statics'), and alpha's LPI.

Registered kernel (GR-1j): each Moment a GP's computed state is the MEAN over its PSR shell (one hop = one Moment = one
PSR, rigid lattice) plus what its resident sources add.  Founder (4355): the test CP is read at one GP, and that GP
'receives its signals from an entire arc of re-radiation' -- this shell.  Static state: u = M_R u + s.

Far field (exact as r >> R): in Fourier space u^ = s^/(1 - M^(k)), and for the lattice shell 1 - M^(k) = k^2 <r^2>/6
+ O(k^4), <r^2> the shell's mean squared radius.  Hence
      u(r) = 6 Q / (4 pi <r^2> r),     V(r) = directed shell mean of u = (<r^2>/3R) |du/dr| ... ~ Q /(R^3 rho^2),
Q = total injected per Moment.  Everything is read at fixed distance rho = r/R (in PSRs); the well is R -> 0.9 R on the
same lattice with AP-4's fixed DI-bit count.  Source models:
  POINT -- the charge's contribution enters at its own GP (Q = 1).
  BAND  -- a fixed count N of DI-bits filling inward from the PSR, one unit each (Q = N): R-DIBIT-INWARD-FILL, N < ball.
  BALL  -- the family fills every GP inside the PSR (Q = the ball's GP count): R-DIBIT-INWARD-FILL with N >= ball in
           flat space and in the well (exclusion caps the landed count at the ball's GP count).
Also checked: the k^2 law of the discrete shell (1 - M^ vs k^2<r^2>/6 at small k)."""
import numpy as np
from itertools import product

def lattice(R):
    n = int(R) + 2; g = np.array(list(product(range(-n, n + 1), repeat=3)), float); r = np.linalg.norm(g, axis=1)
    return g, r

def shell_stats(R):
    g, r = lattice(R); m = np.abs(r - R) < 0.5
    return g[m], (r[m] ** 2).mean(), int((r <= R).sum())

print("discrete shell: 1 - M^(k) against k^2 <r^2>/6 (k along x and along (1,1,1))")
for R in (8.0, 7.2):
    sh, r2, ball = shell_stats(R)
    for k in (0.02, 0.05):
        for d in (np.array([1, 0, 0.]), np.array([1, 1, 1.]) / 3 ** 0.5):
            Mk = np.cos(sh @ (k * d)).mean()
            print(f"  R={R}: k={k} dir={np.round(d,2)}  (1-M)/(k^2<r^2>/6) = {(1 - Mk) / (k * k * r2 / 6):.5f}")
print()
flat, well = shell_stats(8.0), shell_stats(7.2)
N = int(1.5 * len(flat[0]))                       # a band that does not reach the origin in either case
assert N < well[2] < flat[2]
print(f"R=8: shell GPs {len(flat[0])}, <r^2> {flat[1]:.3f}, ball GPs {flat[2]};  R=7.2: shell GPs {len(well[0])}, "
      f"<r^2> {well[1]:.3f}, ball GPs {well[2]};  N = {N}")
print("(1+kappa)^2 = %.3f   (1+kappa)^3 = %.3f\n" % (1 / 0.9**2, 1 / 0.9**3))
print("far field, well/flat at the same distance in PSRs (the ratio is the same at every rho >> 1):")
for kind, Qf, Qw in (('POINT', 1, 1), ('BAND', N, N), ('BALL', flat[2], well[2])):
    # u(rho) = 6Q/(4 pi <r^2> rho R);  V = mean over shell of u n_x = (<r^2>/3) |du/dr| / 1 per unit n-normalisation
    u_ratio = (Qw / (well[1] * 7.2)) / (Qf / (flat[1] * 8.0))
    V_ratio = (Qw / (well[1] * 7.2**2) * well[1] / 7.2) / (Qf / (flat[1] * 8.0**2) * flat[1] / 8.0)
    print(f"  {kind:5s}: census u {u_ratio:6.3f}    vector V {V_ratio:6.3f}")
