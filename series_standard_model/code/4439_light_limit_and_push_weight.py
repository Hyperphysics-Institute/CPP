"""Patch 4439 -- founder: near light speed nearly all of the electron's polarized cloud carries KE as DP arc-separation pairs;
only the central unpaired CP does not; so it bends like light.

Part 1. Rest share of the energy, m/E = 1/gamma, and the KE-carrying share, 1 - 1/gamma, by speed.
Part 2. Which push weight W (4436 step rule: across W + 2 v^2, along W - 2 v^2) his picture allows. Every W that goes to 0 at c
        meets light at the end point; only W = (m/E)^2 = 1/gamma^2 matches GR at every speed (given full Snell-rate turning).
        W = m/E (push on the rest share alone, linear) overshoots across and along.
Part 3. ILLUSTRATION, not a check: one candidate split of 4438's W = (m/E)^2 into two factors of 1/gamma (any two 1/gamma stories
        multiply to it, so the match is fitted, not tested):
        (i) only the rest share is pushed (his); (ii) the rest part, a moving clock, takes the push once per beat of its own rhythm,
        slowed by 1/gamma (Claude's). This is 4438's dropped per-beat delivery with equal resistance gamma m in every direction in place
        of 4424's gamma m sideways and gamma^3 m along; it needs a fast CP's f to respond equally in all directions.
"""
import numpy as np
print("Part 1 (rest share m/E and KE-carrying share):")
for v in (0.1, 0.5, 0.9, 0.99, 0.9999):
    g = 1/np.sqrt(1 - v**2)
    print(f"  v {v}: gamma {g:8.2f}  rest share {1/g:.4f}  KE-carrying share {1 - 1/g:.4f}")
print("Part 2 (toward the mass, / g; GR across 1 + v^2, along 1 - 3 v^2):")
for v in (0.5, 0.9, 0.99, 1.0):
    g = 1/np.sqrt(1 - v**2) if v < 1 else np.inf
    rows = []
    for name, W in (("(m/E)^2", 1/g**2), ("m/E", 1/g), ("1 (no fade)", 1.0)):
        rows.append(f"{name}: {W + 2*v**2:.3f} {W - 2*v**2:+.3f}")
    print(f"  v {v}: GR {1 + v**2:.3f} {1 - 3*v**2:+.3f} | " + " | ".join(rows))
print("Part 3 (illustration: candidate factors; fitted, not tested):")
for v in (0.5, 0.9, 0.99):
    g = 1/np.sqrt(1 - v**2)
    print(f"  v {v}: rest share {1/g:.4f} x rest-clock rate {1/g:.4f} = {1/g**2:.4f} = (m/E)^2")
