#!/usr/bin/env python3
"""
1855 -- DM formation length from kinetic aggregation (the La-Mer-class re-frame).
Mechanism (Thomas, closed this window): fixed monomer pool (burst formation then cessation);
barrierless dimer nucleation ("every monomer is a seed"), irreversible; monomer-addition growth
at 2 E_qq ends; rod-rod coalescence off (rotational gate); reversible E_ee side bonds are a buffer.
Single knob alpha = k_n/k_g (nucleation vs growth per-end). Result: La Mer square-root law
L_n = C*alpha^(-1/2). Natural alpha~1 ("all E_qq ends alike") -> L_n~3; alpha~0.01-0.1 -> ~10-16.
=> at the short observable target (N~tens, see 1856) formation is trivial and un-tuned; no barrier needed.

Fast exact moment model for L_n: c1=free monomer, R=rod count (kg=1, c1(0)=1, k_n=alpha):
  dc1/dt = -2*alpha*c1^2 - 2*c1*R      dR/dt = alpha*c1^2 ;  L_n(rods) = (1-c1)/R at full conversion.
"""
import numpy as np
from scipy.integrate import solve_ivp

def Ln_of_alpha(alpha, tmax=None):
    if tmax is None: tmax = 50.0/alpha + 500.0
    def rhs(t, y):
        c1, R = y
        return [-2*alpha*c1*c1 - 2*c1*R, alpha*c1*c1]
    s = solve_ivp(rhs, (0, tmax), [1.0, 0.0], method="Radau",
                  rtol=1e-10, atol=1e-12, t_eval=[tmax])
    c1, R = s.y[0, -1], s.y[1, -1]
    return (1 - c1)/R if R > 0 else np.inf

if __name__ == "__main__":
    alphas = [3, 1, 0.3, 0.1, 0.03, 0.01, 3e-3, 1e-3, 3e-4, 1e-4, 3e-5, 1e-5]
    print(f"{'alpha=kn/kg':>12} {'L_n(rods)':>11}")
    L = {}
    for a in alphas:
        L[a] = Ln_of_alpha(a)
        print(f"{a:>12.1e} {L[a]:>11.1f}")
    al = np.array([1e-3, 3e-4, 1e-4, 3e-5, 1e-5])
    Ln = np.array([L[a] for a in al])
    slope, inter = np.polyfit(np.log(al), np.log(Ln), 1)
    print(f"\n  fit: L_n = {np.exp(inter):.2f} * alpha^({slope:.3f})   (La Mer square-root, expect -0.5)")
    print(f"  natural alpha~1  -> L_n = {L[1]:.1f}   |   alpha~0.01-0.1 -> L_n = {L[0.1]:.1f}-{L[0.01]:.1f}")
    print("  => short observable target (N~tens) is hit at modest E_bond/kT~4, no nucleation barrier.")
