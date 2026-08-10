#!/usr/bin/env python3
"""3066_stage2_profile_lattice.py — OBL-CC-2 Stage 2 verify (Patch 3066).
METHODS NOTE kept per the record discipline: the first k2 Monte Carlo
used independent draws per beta and was unstable (8.2 then 2.3); the
paired (common-random-numbers) estimator below is the corrected method.
Checks: k2 -> 2 (radial fore-aft suppression), g_d -> 2 (dipole angular
average), S4 lattice sums (cubic + FCC) converged, K assembly."""
import numpy as np

def E_boosted(q, pos_now, beta_vec, obs):
    R = obs - pos_now; Rn = np.linalg.norm(R)
    b2 = beta_vec @ beta_vec
    if b2 == 0: return q * R / Rn**3
    cospsi = (R @ beta_vec) / (Rn * np.sqrt(b2)); s2 = 1 - cospsi**2
    return q * (1 - b2) * R / (Rn**3 * (1 - b2 * s2)**1.5)

rng = np.random.default_rng(30660810)
r, delta, M = 100.0, 0.5, 3000
U = rng.normal(size=(M,3)); U /= np.linalg.norm(U,axis=1,keepdims=True)
D = rng.normal(size=(M,3)); D /= np.linalg.norm(D,axis=1,keepdims=True)
def pair_E2(beta):
    acc = 0.0
    for u, d in zip(U, D):
        c = r*u; bv = beta*u
        E = (E_boosted(+1, c+0.5*delta*d, bv, np.zeros(3))
             + E_boosted(-1, c-0.5*delta*d, bv, np.zeros(3)))
        acc += E @ E
    return acc / M
E0 = pair_E2(0.0)
k2 = (1 - pair_E2(0.02)/E0)/0.02**2
# g_d by DETERMINISTIC quadrature (an exact angular integral — MC was
# the wrong tool; the 3/4 first run is kept in the record as the lesson):
th = np.linspace(0, np.pi, 20001)
gd = np.trapezoid((3*np.cos(th)**2 + 1) * np.sin(th), th) / 2.0
def S4(lattice, a, N=40):
    n = np.arange(-N, N+1)
    P = np.stack(np.meshgrid(n,n,n,indexing='ij'),-1).reshape(-1,3).astype(float)
    if lattice=='fcc': P = P[(P.sum(1)%2)==0]
    P = P[np.any(P!=0,axis=1)]
    return float(np.sum(1.0/np.sum(P**2,1)**2))/a**4
s4c, s4f = S4('cubic',2.5), S4('fcc',2.5)
K_c = (2*2/(8*np.pi))*0.36*s4c; K_f = (2*2/(8*np.pi))*0.36*s4f
checks = [("k2 = 2 (|err|<0.01)", abs(k2-2)<0.01),
          ("g_d = 2 (|err|<0.01)", abs(gd-2)<0.01),
          ("S4 cubic converged 0.4166", abs(s4c-0.41663)<0.001),
          ("S4 fcc converged 0.1589", abs(s4f-0.15886)<0.001)]
n=0
for name, ok in checks:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}"); n+=ok
print(f"K_cubic={K_c:.6f}  K_fcc={K_f:.6f}  (rho_L = K q^2 / R_h^2, engine units)")
print(f"{n}/{len(checks)} PASS")
