#!/usr/bin/env python3
"""4356 -- founder (4356): one DI-bit per GP holds for any PSR down to maximum compression (the black hole), where the
GPs inside the PSR equal the DI-bit count.  Corpus: the R-core surface is where the PSR reaches its floor l_P/2
(lapse 1/2; R-PSR-LAW-LOG, AP-5 cap).  So N = GPs inside a ball of radius PSR_0/2 = 1/8 of the flat PSR ball.
Consequences computed: (i) the flat-space band depth (continuum and lattice); (ii) the band in a well;
(iii) alpha's far-field LPI under 4355 with that N."""
import numpy as np
from itertools import product
print("continuum: band fills the outer 1/8 of the PSR ball volume -> inner edge (7/8)^(1/3) = %.4f PSR, "
      "depth %.2f%% of the PSR" % ((7/8)**(1/3), 100*(1-(7/8)**(1/3))))
for R0 in (16.0, 24.0, 32.0):
    n = int(R0) + 1
    g = np.array(list(product(range(-n, n + 1), repeat=3)), float); r = np.sort(np.linalg.norm(g, axis=1))
    ball = (r <= R0).sum(); N = (r <= R0 / 2).sum()
    inner = np.sort(r[r <= R0])[::-1][N - 1]
    out = [f"lattice R0={R0:.0f}: ball {ball}, N = ball(R0/2) = {N} (ratio {N/ball:.4f}); band inner edge {inner/R0:.4f} PSR"]
    for kap in (0.1, 0.5):
        Rw = R0 / (1 + kap); bw = (r <= Rw).sum(); inw = np.sort(r[r <= Rw])[::-1][min(N, bw) - 1]
        out.append(f"  well 1+k={1+kap}: ball {bw}, band inner edge {inw/Rw:.4f} PSR")
    print("\n".join(out))
print("\nfar field (4355): Q = N fixed and N < ball for every PSR above the floor -> well/flat = (1+kappa)^3: k_alpha = -3")
print("at the floor itself the ball is full (N = ball), the only place 4355's invariant case is reached")
