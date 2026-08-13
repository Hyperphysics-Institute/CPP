#!/usr/bin/env python
"""Patch 3107 -- THE SINGLE FINAL ASSEMBLY (per the 3068 freeze and the
3104 prereg use commitments). The factors multiply ONCE, here; the
verdict is stated in F-CLI-1's exact words.

STRUCTURE (committed lineage):
  3068/3076:  rho_L = (C4' alpha Phi / 2pi) * hbar c / (d^2 R_h^2)
  Li mapping (0723, reproduced at 3098):
      rho_L = 3 c_Li^2 M_p^2 / R_h^2,  M_p^2 = 1/(8 pi l_P^2)
  =>  c_Li = sqrt( (4/3) * C4' * alpha * Phi ) * (l_P / d_s)
  Check: at d = l_P, Phi = eta_z, C4' = 24.82 this gives
  c_Li = 0.4914 sqrt(eta_z) -- the 3068 committed coefficient, exact.

THE FOLDED FACTOR Phi (species-resolved; every mapping declared):
  Each weave unit carries one eDP + one qDP (A-1, phi_1 = 2 folded
  here as the two species terms). phi_2 = 1 (closed). The excursion
  statistic per species is the measured per-pair cycle average,
  gas/bound weighted (this REPLACES the phi_1 f_trans rider -- the
  transient population IS the pairs' stretched states; no extra
  dipoles; double-count excluded by construction):
      etabar_e = (1 - r_e) eta_e + r_e eta_gas
      etabar_q = (1 - r_q) (s_meas * eta_e) + r_q * eta_gas
  with r_q = r_e * x_q/(1 - x_q) (from the measured gas species
  split). Channel content: eDP -> 1; qDP -> C = (1 + k)^2 (AP-4b
  coherent; incoherent fork 1 + k^2 bracketed), k = sqrt(alpha_s/
  alpha) [O-2 PROPOSED]. delta = d_p/2 maps measured pair-separation
  eta to the formula's excursion eta: divide by 4.
      Phi = ( etabar_e + C * etabar_q ) / 4

INPUTS (3105 measured +/- SE, or declared brackets; nothing else):
  r_e      = 0.36 +/- 0.06          (measured)
  x_q      = 0.19 +/- 0.03          (measured)
  eta_e    = 0.055 +/- 0.011        (measured bound-state, E-cells)
  eta_gas  = 1.78 +/- 0.05          (measured)
  s_meas   = 0.52 +/- 0.09          (measured; RULED-NONPHYSICAL-
                                     REGULARIZATION provenance, 3106)
  C        in [53.9, 68.5]          (coherence fork, 3103)
  arrangement a in [0.78, 1.35]     (A-1 bracket; 3105 read-out
                                     pathological, prereg escape)
  C4'      = 25.338 * a
  d_s      in [3.0, 7.5] l_P        (3105 boundary disposition)
  alpha    = 1/137.035999
BAND (frozen 3060/3068): c_Li in [0.6, 0.9]; adjudicated reference
c_Li = 0.8 (0723). VERDICT RULE: the bracket's full range vs the
band; in band or F-CLI-1 FIRES in those words.
"""
import numpy as np
import itertools

ALPHA = 1/137.035999
BAND = (0.6, 0.9)

r_e   = (0.36, 0.06)
x_q   = (0.19, 0.03)
eta_e = (0.055, 0.011)
eta_g = (1.78, 0.05)
s_m   = (0.52, 0.09)
C_frk = (53.9, 68.5)
a_frk = (0.78, 1.35)
d_frk = (3.0, 7.5)

def phi(re, xq, ee, eg, s, C):
    rq = re*xq/(1.0-xq)
    ebar_e = (1-re)*ee + re*eg
    ebar_q = (1-rq)*(s*ee) + rq*eg
    return (ebar_e + C*ebar_q)/4.0, ebar_e, ebar_q

def cli(Phi, a, d):
    return np.sqrt((4.0/3.0)*25.338*a*ALPHA*Phi)/d

# ---- 3068 regression gate ------------------------------------------
c_check = np.sqrt((4.0/3.0)*24.82*ALPHA*1.0)/1.0
assert abs(c_check - 0.4914) < 0.002, "failed to reproduce the 3068 coefficient"
print(f"GATE: 3068 coefficient reproduced: c_Li(d=l_P, Phi=eta_z=1) = {c_check:.4f} [0.4914]")

# ---- central value -------------------------------------------------
Phi_c, ee_c, eq_c = phi(r_e[0], x_q[0], eta_e[0], eta_g[0], s_m[0], np.mean(C_frk))
print(f"\nCENTRAL: etabar_e = {ee_c:.4f}, etabar_q = {eq_c:.4f}, Phi = {Phi_c:.4f}")
for d in (3.0, 5.0, 7.4):
    print(f"  d_s = {d:3.1f} l_P: c_Li = {cli(Phi_c, 1.0, d):.4f}")

# ---- full-bracket extremes (all corners + measured 1-sigma) --------
best, worst = -1.0, 1e9
for re_, xq_, ee_, eg_, s_ in itertools.product(
        [r_e[0]-r_e[1], r_e[0]+r_e[1]], [x_q[0]-x_q[1], x_q[0]+x_q[1]],
        [eta_e[0]-eta_e[1], eta_e[0]+eta_e[1]],
        [eta_g[0]-eta_g[1], eta_g[0]+eta_g[1]],
        [s_m[0]-s_m[1], s_m[0]+s_m[1]]):
    for C_ in C_frk:
        P, _, _ = phi(re_, xq_, ee_, eg_, s_, C_)
        for a_ in a_frk:
            for d_ in d_frk:
                c = cli(P, a_, d_)
                best = max(best, c); worst = min(worst, c)
print(f"\nFULL DECLARED RANGE: c_Li in [{worst:.4f}, {best:.4f}]")
print(f"BAND (frozen 3060/3068): [{BAND[0]}, {BAND[1]}]; adjudicated reference 0.8")

shortfall_lo = (BAND[0]/best)**2
shortfall_hi = (BAND[0]/worst)**2
in_band = (best >= BAND[0]) and (worst <= BAND[1])
overlap = (best >= BAND[0]) and (worst <= BAND[1] or worst <= BAND[0] <= best)

print("\n" + "="*68)
if best < BAND[0]:
    print("VERDICT: the forward number falls OUTSIDE the band at every point")
    print("of the declared bracket. Per the frozen rule:  F-CLI-1 FIRES.")
    print(f"Shortfall in rho_Lambda: x{shortfall_lo:.1f} (best corner) to x{shortfall_hi:.0f} (worst).")
elif worst > BAND[1]:
    print("VERDICT: OVERSHOOT above the band everywhere. F-CLI-1 FIRES.")
else:
    print("VERDICT: the declared bracket reaches the band. IN BAND (bracketed).")
print("="*68)
print("\nPerspective, both facts with equal weight (the 3068 sentence):")
print("the bare catastrophe is ~10^123; the forward mechanism closes")
print("~122 orders from alpha and geometry alone -- and it misses the")
print("last factor. Both facts are the result. No rescue is attempted;")
print("the panel receives this record; the named residuals (D-STIFF-DYN,")
print("the boundary location pass, O-2 ratification, FQ-8) are the")
print("fired-state's open physics, reopenable only by founder ruling or")
print("panel adjudication -- never by post-hoc bracket widening.")
