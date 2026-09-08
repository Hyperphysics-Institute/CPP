#!/usr/bin/env python3
"""
Patch 3692 verify — DOES THE LAYER-COPY'S OWN CENSUS RESTORE A CP DISPLACED INSIDE ITS FLOOR CELL?
Model: the copy's PSR shell is the 12 vertices of an icosahedron (unit radius = the layer's cell scale); a CP
displaced by delta from the centre receives count intensity ~ |r_i - delta|^-p from each neighbour, directed
toward it (the CPP net-vector rule); net F(delta) = sum d_hat |d|^-p.
 T1  p = 2 (the CPP PSR law): linear term VANISHES (shell theorem; icosahedral symmetry kills l = 1..5), first
     surviving term ~ delta^5 with NEGATIVE sign -> restoring but QUINTIC (zero stiffness at small amplitude).
 T2  p = 1: linear restoring (F/delta -> -4);  p = 3: linear ANTI-restoring (+4). So the sign at linear order is
     set by whether the count law is shallower or steeper than 1/r^2; exactly 1/r^2 is neutral.
 T3  Generic direction: same quintic law (|F|/|delta|^5 ~ 10), isotropic to this order.
Conclusion: the founder's "movement within a progressively tinier cell" restores, but geometry alone gives no
linear spring; a finite stiffness (needed for k2 and flat-core stability) must come from the layer's register
cap, the collective lockstep response (3374/3637), or a fine-scale departure from 1/r^2. Opus's 3691 phrase "the
restoring force appears for free" is CORRECTED to "restoring at fifth order; stiffness owed".
"""
import numpy as np
PASS = FAIL = 0
def check(n, c, d=""):
    global PASS, FAIL; ok = bool(c); PASS += ok; FAIL += (not ok); print(f"  [{'PASS' if ok else 'FAIL'}] {n}" + (f"  — {d}" if d else ""))
phi = (1 + 5**0.5) / 2; verts = []
for s1 in (1, -1):
    for s2 in (1, -1):
        verts += [(0, s1, s2 * phi), (s1, s2 * phi, 0), (s2 * phi, 0, s1)]
V = np.array(verts, float); V /= np.linalg.norm(V[0])
def net(delta, p):
    F = np.zeros(3)
    for r in V:
        d = r - delta; n = np.linalg.norm(d); F += d / n * n**(-p)
    return F
print("T1 — p = 2 (CPP PSR law)")
r5 = []
for eps in (0.1, 0.03, 0.01):
    F = net(np.array([eps, 0, 0]), 2); r5.append(F[0] / eps**5)
    print(f"    delta = {eps:.2f}: F_x/delta = {F[0]/eps:+.2e}   F_x/delta^5 = {F[0]/eps**5:+.3f}")
check("T1 no linear term (|F/delta| < 1e-3 at delta = 0.01)", abs(net(np.array([0.01, 0, 0]), 2)[0] / 0.01) < 1e-3)
check("T1 quintic and restoring: F/delta^5 -> -9.9 (constant to 1 %)", np.std(r5) / abs(np.mean(r5)) < 0.01 and np.mean(r5) < 0, f"{np.mean(r5):+.2f}")
print("T2 — sign at linear order vs count law")
k1 = net(np.array([0.01, 0, 0]), 1)[0] / 0.01; k3 = net(np.array([0.01, 0, 0]), 3)[0] / 0.01
print(f"    p = 1: F/delta = {k1:+.3f} (restoring);  p = 3: F/delta = {k3:+.3f} (anti-restoring)")
check("T2 p = 1 restoring, p = 3 anti-restoring", k1 < 0 < k3)
print("T3 — generic direction")
d = np.array([0.05, 0.03, -0.02]); F = net(d, 2); q = np.linalg.norm(F) / np.linalg.norm(d)**5
check("T3 quintic law isotropic (|F|/|delta|^5 within 5 % of 9.9)", abs(q / 9.9 - 1) < 0.05, f"{q:.2f}")
print(f"\n{PASS}/{PASS+FAIL} PASS")
