#!/usr/bin/env python3
"""Patch 3936 — OPEN-EU-PHOTON-GENESIS-1: the pass-band for C-5's adiabaticity condition.

Inputs (all corpus, none new):
  S     = delta ln(n_q/n_e) at Hubble coarse-graining = 1.36e-4   (3908)
  zeta  = 4.5e-5                                                    (3908 design value)
  beta_max = 0.04  ('a few percent', 3908; beta = S_B^2/(S_B^2+zeta^2))
  q     = n_q/(n_q+n_e) = 1/2   (eDP:qDP = 1:1 lock, founders_vision register 0672a §6c, equilibrium statement)
  eps   = e_q/e_e, energy released per CP on the q side over the e side; corpus-anchored value
          alpha_s(M_Pl)/alpha = 0.01970/0.007297 = 2.70   (3902 coupling structure)
Unknown, NOT computed here (NB-S3a-1 blocks the kinetics): p, with n_B ∝ n_q^p.
Output: the band of p that passes, as a function of eps; the corpus-anchored point; two endpoints.
"""
import math
S, zeta, beta_max, q = 1.36e-4, 4.5e-5, 0.04, 0.5
alpha, alpha_s = 0.007297, 0.01970
eps0 = alpha_s/alpha
Rmax = math.sqrt(beta_max/(1-beta_max))          # max |S_B|/zeta
W = Rmax*zeta/S                                   # half-width of the pass band in the bracket
def cE_linear(eps, q=q):   # E ∝ n_e e_e + n_q e_q ; returns delta ln E / S
    return q*(1-q)*(eps-1)/((1-q)+q*eps)
def cE_pairs(eps, q=q):    # Q-Q at alpha_s only when both partners are q (random pairing, q^2)
    return 2*q*q*(1-q)*(eps-1)/(1+q*q*(eps-1))
def SB_over_zeta(p, eps, cE):
    return ((1-q)*p - 0.75*cE(eps))*S/zeta
def band(eps, cE):
    c = 0.75*cE(eps)/(1-q); return (c - W/(1-q), c + W/(1-q))
checks = []
def T(name, cond, msg): checks.append((name, bool(cond), msg)); print(f"{'PASS' if cond else 'FAIL'} {name}: {msg}")
T("T1", abs(eps0-2.70)<0.01, f"eps0 = alpha_s/alpha = {eps0:.3f} (3902)")
T("T2", abs(Rmax-0.204)<0.002, f"beta_max=0.04 => |S_B|/zeta <= {Rmax:.3f}; W = {W:.4f}")
# 3908 reproduction: S_B = S (p=1, no energy compensation) gives beta ~ 0.9
b3908 = (S/zeta)**2/(1+(S/zeta)**2)
T("T3", abs(b3908-0.90)<0.01, f"3908 reproduced: S/zeta={S/zeta:.2f} => beta={b3908:.2f}")
for label, cE in (("linear", cE_linear), ("pair-statistics", cE_pairs)):
    lo, hi = band(eps0, cE); c = cE(eps0)
    print(f"  [{label}] cE(eps0)={c:.3f}; pass band p in [{lo:.3f}, {hi:.3f}], centre {(lo+hi)/2:.3f}")
    for p in (0.0, 1.0):
        r = SB_over_zeta(p, eps0, cE); b = r*r/(1+r*r)
        print(f"     p={p:.0f}: S_B/zeta={r:+.3f}, beta={b:.2f}, fails by {abs(r)/Rmax:.1f}x on S_B/zeta")
    z_comp = 0.25*c*S
    print(f"     composition contribution to zeta: {z_comp:.2e} = {100*z_comp/zeta:.0f}% of design zeta")
loA, hiA = band(eps0, cE_linear); loB, hiB = band(eps0, cE_pairs)
T("T4", 0.0 < loA and hiA < 1.0, f"linear band excludes both p=0 and p=1: [{loA:.3f},{hiA:.3f}]")
T("T5", 0.0 < loB and hiB < 1.0, f"pair band excludes both p=0 and p=1: [{loB:.3f},{hiB:.3f}]")
r0 = SB_over_zeta(0.0, eps0, cE_linear)
T("T6", 2.0 < abs(r0)/Rmax < 4.0, f"p=0 (density-independent freeze-out) fails by {abs(r0)/Rmax:.1f}x (linear), not 30x")
lo1, hi1 = band(1.0, cE_linear)
T("T7", lo1 < 0 < hi1 and hi1 < 0.2, f"eps=1 (e side releases equal energy) requires p <= {hi1:.3f}")
lo_inf, hi_inf = band(1e6, cE_linear)
T("T8", 0.5 < lo_inf < hi_inf < 1.0, f"eps->inf (e side negligible) requires p in [{lo_inf:.3f},{hi_inf:.3f}]")
print(f"\n{sum(c for _,c,_ in checks)}/{len(checks)} checks pass")
