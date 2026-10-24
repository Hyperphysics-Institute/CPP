"""Patch 4429 -- founder: the PSR at right angles to a fast electron's path is unchanged from rest (with 4428: forward -- ahead -- it shrinks
by the Lorentz factor; the same behind is Claude's reading).

Part 1. The moving PSR he has now described: 1/gamma along the motion, 1 across. Light round trips across an arm of rest length L
        (4409's light-sphere reaches, absolute frame): along, arm L/gamma: 2 (L/gamma) / (1 - v^2); across: 2 L / sqrt(1 - v^2).
        Equal for every v (the Michelson-Morley null). MM fixes only the RATIO (1/gamma along relative to across); a clock-rate change
        scales both arms alike and cannot rescue a ratio mismatch. 'Unchanged across' in absolute terms also needs the clock rate
        (Kennedy-Thorndike; 4408/4409).
Part 2. Candidate rule (Claude's): the along-motion PSR = rest PSR x sqrt(1 - (|SSV_net|/SSV_abs)^2) = rest PSR x M/S, using
        4425's bundle (f = |V|/S, M^2 = S^2 - V^2): the shortening is the CP's own rest value over its total. Checked against 1/gamma.
"""
import numpy as np
print("Part 1 (light round trips, arm of rest length 1):")
for v in (0.3, 0.6, 0.9):
    g = 1/np.sqrt(1 - v**2)
    along = 2*(1/g)/(1 - v**2); across = 2/np.sqrt(1 - v**2)
    across_wrong = 2*(1/g)/np.sqrt(1 - v**2)        # if the PSR also shrank sideways by 1/gamma
    print(f"  v {v}: along {along:.4f}  across {across:.4f}  (equal)   | if sideways also shrank: across {across_wrong:.4f}")
print("Part 2 (candidate: along-motion PSR = M/S with M^2 = S^2 - V^2, f = V/S):")
M = 1.0
for V in (0.25, 1.0, 4.0):
    S = np.sqrt(M**2 + V**2); f = V/S; g = 1/np.sqrt(1 - f**2)
    print(f"  V {V:4.2f}: f {f:.4f}  M/S {M/S:.4f}  1/gamma {1/g:.4f}")
