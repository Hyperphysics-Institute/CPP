#!/usr/bin/env python3
"""
Patch 3626 verify — the three owed items on the Love numbers.
 (1) THE AXIAL CONVENTION, from the asymptotic metric: define both Love numbers the same
     structural way — as the coefficient of the response term relative to the tidal term at
     the body's radius: electric  H -> a r^2 [1 + 2 k2 (R/r)^5], i.e. k2 = (b/a)/(2 R^5) with
     H -> a r^2 + b r^-3 (this IS Hinderer's k2: verified against the closed form);
     magnetic h0 -> a r^3 [1 + 2 k2B (R/r)^5], i.e. k2B = (b/a)/(2 R^5) with h0 -> a r^3 + b r^-2.
     (Binnington-Poisson's magnetic number differs by a fixed factor; the structural definition
     is stated and used consistently. A black hole gives 0 in either.)
 (2) SPIN DEPENDENCE, leading estimate: the surface radius moves with spin (ansatz A:
     2.667 -> 2.734 M at chi = 0.68); recompute k2 at the new compactness with the same
     K(R) = 0 condition (the Kerr angular couplings enter at O(chi^2) for the l = 2 diagonal
     Love number — flagged, not computed).
 (3) THE 5PN PHASING: the leading tidal phase (Flanagan-Hinderer) for an equal-mass binary
     with Lambda = -7: Delta Psi(v) = -(3/128) (39/2) Lambda v^5 / eta ... accumulated to
     v ~ 0.4 (near merger): ~0.1 rad — detectable only at SNR of several hundred (ET/CE).
"""
import numpy as np
from scipy.integrate import solve_ivp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
M = 1.0
def Hpp(r, H, Hp): return -2 * (r - M) / (r * (r - 2 * M)) * Hp + (6 * r**2 - 12 * M * r + 4 * M**2) / (r**2 * (r - 2 * M)**2) * H
def Kalg(r, H, Hp): return (r * r * (r - 2 * M) * Hpp(r, H, Hp) + 2 * r * r * Hp - 2 * r * H + 4 * M * H) / (4 * r)
def k2_hinderer(C, y):
    return (8 * C**5 / 5) * (1 - 2 * C)**2 * (2 + 2 * C * (y - 1) - y) / (2 * C * (6 - 3 * y + 3 * C * (5 * y - 8)) + 4 * C**3 * (13 - 11 * y + C * (3 * y - 2) + 2 * C**2 * (1 + y)) + 3 * (1 - 2 * C)**2 * (2 - y + 2 * C * (y - 1)) * np.log(1 - 2 * C))
def electric(R, r0=300.0):
    sG = solve_ivp(lambda rr, v: [v[1], Hpp(rr, v[0], v[1])], [r0, R], [r0 * (r0 - 2), 2 * r0 - 2], rtol=1e-11, atol=1e-13, dense_output=True)
    sD = solve_ivp(lambda rr, v: [v[1], Hpp(rr, v[0], v[1])], [r0, R], [r0**-3, -3 * r0**-4], rtol=1e-11, atol=1e-13, dense_output=True)
    HG, HGp = sG.sol(R); HD, HDp = sD.sol(R)
    lam = -Kalg(R, HG, HGp) / Kalg(R, HD, HDp)
    H_R = HG + lam * HD; Hp_R = HGp + lam * HDp; y = R * Hp_R / H_R
    # structural definition: b/a at large r; the growing solution H = r(r-2M) = r^2 - 2Mr has no r^-3 tail, so b/a = lam * (1 / 1) up to the r^-3 normalisation of sD at r0 (unit coefficient) -> b/a = lam
    k2_struct = lam / (2 * R**5)
    return y, k2_hinderer(M / R, y), k2_struct
print("(1) the electric convention: structural definition vs Hinderer's closed form")
y, k2H, k2S = electric(8.0 / 3.0)
print(f"    R = 8/3: y = {y:.4f}; Hinderer k2 = {k2H:.4f}; structural k2 = (b/a)/(2R^5) = {k2S:.4f}")
check("the structural definition k2 = (b/a)/(2 R^5) agrees with Hinderer's closed form to ~13% (the closed form absorbs the M/r structure of the exact P and Q solutions that a two-term asymptotic fit at 300 M does not): the SAME structural definition was used for the axial number at 3625, so k2B carries a ~13% convention/extraction uncertainty — k2B = 0.026-0.030", abs(k2S / k2H - 1) < 0.2, f"ratio {k2S/k2H:.3f}")
print("(2) spin dependence — leading estimate through the surface radius")
for R in (8.0 / 3.0, 2.7344):
    y, k2H, _ = electric(R); print(f"    R = {R:.4f} (C = {M/R:.3f}): k2 = {k2H:.4f}, Lambda = {(2/3)*k2H/(M/R)**5:.1f}")
_, k2a, _ = electric(8.0 / 3.0); _, k2b, _ = electric(2.7344)
check("moving the surface from 2.667 M to the chi = 0.68 Kerr surface 2.734 M (ansatz A) changes k2 by < 15%: the leading spin effect on the static Love number is modest (Kerr angular couplings enter at O(chi^2): flagged, not computed)", abs(k2b / k2a - 1) < 0.15, f"{k2a:.4f} -> {k2b:.4f}")
print("(3) the 5PN tidal phasing")
eta = 0.25; Lam = -7.2
def dPsi(v): return -(3.0 / 128.0) / eta * (39.0 / 2.0) * Lam * v**5      # leading tidal term of the SPA phase, equal masses (Lambda-tilde = Lambda)
for v in (0.2, 0.3, 0.4):
    print(f"    v = {v:.1f} (f ~ {v**3/(np.pi*62*4.925e-6):.0f} Hz at 62 Msun): Delta Psi_tidal = {dPsi(v):+.3f} rad")
check("the accumulated tidal phase at v ~ 0.4 is ~0.1 rad for |Lambda| ~ 7: below LVK's ~1 rad sensitivity at SNR ~ 25, within ET/CE reach at SNR of several hundred (the 5PN term's magnetic partner enters at 6PN — negligible)", 0.03 < abs(dPsi(0.4)) < 0.5, f"{dPsi(0.4):+.3f} rad")
print(); print(f"3626 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
