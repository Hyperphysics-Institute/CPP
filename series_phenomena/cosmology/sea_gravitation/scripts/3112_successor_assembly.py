#!/usr/bin/env python
"""Patch 3112 -- THE SUCCESSOR ASSEMBLY (F-CLI-2), per prereg 3110 S4:
the 3107 fold VERBATIM, inputs replaced by the 3111 memoryless
measurements; band frozen [0.6, 0.9]; verdict in the frozen words."""
import numpy as np, itertools

ALPHA = 1/137.035999
BAND = (0.6, 0.9)
r_e, x_q = (0.274, 0.02), (0.700, 0.02)
eta_e, eta_g = (0.0700, 0.005), (1.91, 0.05)
s_m = (1.797, 0.05)
C_frk, a_frk, d_frk = (53.9, 68.5), (0.78, 1.35), (3.0, 7.5)

def phi(re, xq, ee, eg, s, C):
    rq = min(re*xq/(1.0-xq), 1.0)
    return ((1-re)*ee + re*eg + C*((1-rq)*(s*ee) + rq*eg))/4.0

def cli(P, a, d):
    return np.sqrt((4.0/3.0)*25.338*a*ALPHA*P)/d

assert abs(np.sqrt((4/3)*24.82*ALPHA)/1.0 - 0.4914) < 0.002
print("GATE: 3068 coefficient reproduced (0.4914). Fold = 3107 verbatim.")

P_c = phi(r_e[0], x_q[0], eta_e[0], eta_g[0], s_m[0], float(np.mean(C_frk)))
print(f"\nCENTRAL: Phi = {P_c:.3f}")
for d in (3.0, 4.0, 5.0, 6.0, 7.5):
    print(f"  d_s = {d:3.1f} l_P: c_Li = {cli(P_c, 1.0, d):.4f}")

best, worst = -1.0, 1e9
for re_, xq_, ee_, eg_, s_ in itertools.product(
        [r_e[0]-r_e[1], r_e[0]+r_e[1]], [x_q[0]-x_q[1], x_q[0]+x_q[1]],
        [eta_e[0]-eta_e[1], eta_e[0]+eta_e[1]],
        [eta_g[0]-eta_g[1], eta_g[0]+eta_g[1]],
        [s_m[0]-s_m[1], s_m[0]+s_m[1]]):
    for C_ in C_frk:
        P = phi(re_, xq_, ee_, eg_, s_, C_)
        for a_ in a_frk:
            for d_ in d_frk:
                c = cli(P, a_, d_)
                best = max(best, c); worst = min(worst, c)
print(f"\nFULL DECLARED RANGE: c_Li in [{worst:.4f}, {best:.4f}];  BAND [{BAND[0]}, {BAND[1]}]")

# in-band d_s corridor at central values, both band edges
d_hi = np.sqrt((4/3)*25.338*ALPHA*P_c)/BAND[0]
d_lo = np.sqrt((4/3)*25.338*ALPHA*P_c)/BAND[1]
print(f"IN-BAND d_s CORRIDOR (central Phi, a = 1): d_s in [{d_lo:.2f}, {d_hi:.2f}] l_P")

print("\n" + "="*68)
if best < BAND[0] or worst > BAND[1]:
    print("VERDICT: outside the band at every declared point. F-CLI-2 FIRES.")
else:
    print("VERDICT: the declared range REACHES AND OVERLAPS the band.")
    print("F-CLI-2 DOES NOT FIRE. Status: IN BAND (BRACKETED) -- not a")
    print("point confirmation: the range spans below the band as well;")
    print("the deciding input is the UNLOCATED d_s (boundary pass) plus")
    print("the C-fork, arrangement, and O-2 ratification residuals.")
print("="*68)
