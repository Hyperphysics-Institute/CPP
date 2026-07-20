#!/usr/bin/env python3
"""
PATCH 2607 -- N2-A-GAMMA EXECUTION under n2a_gamma_prereg.md (2606) ONLY.
The eta gamma-re-derivation: controls C1/C2 gate; routes R-A1-gamma (exact CM
two-body period by quadrature; Newtonian anharmonic column on the same grid) and
R-A2-gamma (half-return floor with relativistic KE(p)). Verdicts are read from the
prereg against raw outputs (the 2579 rule); this script prints observables only.
Citations: potential = 2582/2596 engine verbatim; H-gamma kinematics = 2601;
lag formula + compounding = the 2596 R-A1 convention, pinned by control C1.
"""
import numpy as np
from scipy.optimize import brentq, minimize_scalar
from scipy.integrate import quad

AHC = 197.3
PHI_G = (1 + np.sqrt(5)) / 2
ALPHA_S = 5 / (8 * PHI_G)
A_QQ = AHC / 264.0            # electric softening length [fm]
D = 1.15
EQQ = ALPHA_S * AHC / D       # 66.25 MeV [1812]
M = 132.0                     # kappa_q = m, per-CP [MeV/c^2]
TAUC = 2 * np.pi * AHC / 264.0  # substrate Sea clock [fm/c] -- NOT dilated (prereg S1)

def U(r, w):
    """Registered pair potential, 2582/2596 verbatim."""
    e = np.exp(-(w / D) * (r - D))
    return -ALPHA_S * AHC / np.sqrt(r * r + A_QQ * A_QQ) + EQQ * ((1 - e) ** 2 - 1)

def req_of(w):
    res = minimize_scalar(lambda r: U(r, w), bounds=(0.6, 2.0), method='bounded',
                          options={'xatol': 1e-10})
    return res.x

def k_of(w, req, h=1e-5):
    return (U(req + h, w) - 2 * U(req, w) + U(req - h, w)) / h ** 2

def f_lag(x):
    """Per-bond-period first-order-lag loss (2596 R-A1)."""
    return 2 * np.pi * x / (1 + x * x)

def eta_A1_from_omega(om):
    """Moment-cycle compounding at bond frequency om (2596 convention, C1-pinned).
    GUARD FIRST (2600 structural adoption): the lag formula is a small-loss
    expression; f_per >= 1 is outside its domain (saturation) -- the evaluator
    returns valid=False and NO value rather than a complex artifact."""
    x = om * TAUC
    f = f_lag(x)
    if f >= 1.0:
        return None, x, False
    return 1 - (1 - f) ** (x / (2 * np.pi)), x, True

def turning_points(E, w, req):
    """r-/r+ with DU(r) = E, DU = U - U(req)."""
    U0 = U(req, w)
    g = lambda r: (U(r, w) - U0) - E
    rin = brentq(g, 0.35, req)
    rout = brentq(g, req, 60.0)
    return rin, rout

def period_newton(E, w, req):
    """Anharmonic Newtonian period, reduced mass mu = M/2."""
    U0 = U(req, w)
    mu = M / 2
    rin, rout = turning_points(E, w, req)
    def integrand(r):
        arg = 2 * (E - (U(r, w) - U0)) / mu
        return 1.0 / np.sqrt(max(arg, 1e-14))
    eps = 1e-7 * (rout - rin)
    val, _ = quad(integrand, rin + eps, rout - eps, limit=400)
    return 2 * val

def period_gamma(E, w, req):
    """Exact relativistic CM two-body period: 2(gamma(r)-1)M + DU(r) = E;
    p(r) = sqrt((M + (E - DU)/2)^2 - M^2); v_rel = 2p/sqrt(M^2 + p^2)."""
    U0 = U(req, w)
    rin, rout = turning_points(E, w, req)
    def integrand(r):
        ke_per = (E - (U(r, w) - U0)) / 2.0     # per-CP kinetic energy
        p = np.sqrt(max((M + ke_per) ** 2 - M * M, 1e-14))
        vrel = 2 * p / np.sqrt(M * M + p * p)
        return 1.0 / max(vrel, 1e-14)
    eps = 1e-7 * (rout - rin)
    val, _ = quad(integrand, rin + eps, rout - eps, limit=400)
    return 2 * val

def KE(p):
    return np.sqrt(M * M + p * p) - M

def floor_gamma(g):
    """R-A2-gamma half-return floor: 1 - <KE(p|cos phi|)>/KE(p), phi uniform."""
    p = M * np.sqrt(g * g - 1)
    num, _ = quad(lambda ph: KE(p * abs(np.cos(ph))), 0, np.pi / 2, limit=200)
    R = (num / (np.pi / 2)) / KE(p)
    return 1 - R

print("=" * 78)
print("PATCH 2607 -- N2-A-GAMMA: eta re-derivation (prereg 2606; verdicts read there)")
print("=" * 78)

WIDTHS = {"soft": 2.0, "steep": 4.0}
REQ_REF = {"soft": 1.0752, "steep": 1.1305}

# ---------- C1: convention pin ----------
print("\n[C1] convention pin (must reproduce registered 0.74 soft / 0.68 steep)")
req = {}
for name, w in WIDTHS.items():
    r0 = req_of(w)
    req[name] = r0
    k = k_of(w, r0)
    om_red = np.sqrt(k / (M / 2))     # registered candidate: reduced mass
    om_pcp = np.sqrt(k / M)           # alternative: per-CP mass (must fail)
    eta_red, x_red, _ = eta_A1_from_omega(om_red)
    eta_pcp, x_pcp, _ = eta_A1_from_omega(om_pcp)
    print(f"  {name}: r_eq={r0:.4f} (ref {REQ_REF[name]}) k={k:.1f} MeV/fm^2 | "
          f"REDUCED: x={x_red:.2f} eta_A1={eta_red:.3f} | "
          f"perCP: x={x_pcp:.2f} eta_A1={eta_pcp:.3f}")

# ---------- C2 + routes: declared grid ----------
print("\n[grid] gamma_char in {1.02,1.05,1.1,1.2,1.3,1.4,1.45}, truncated at gamma_cap")
for name, w in WIDTHS.items():
    r0 = req[name]
    depth = U(1e4, w) - U(r0, w)     # DU(inf): dissociation depth of the pair
    gcap = 1 + depth / (2 * M)
    print(f"\n  --- {name} width (w={w}): depth={depth:.2f} MeV, gamma_cap={gcap:.4f} ---")
    print(f"  {'g_char':>7} {'E_osc':>7} {'T_harm':>7} {'T_Nanh':>8} {'T_gam':>8} "
          f"{'etaA1_Nanh':>10} {'etaA1_gam':>10} {'d_gam':>7} {'floor_gam':>9}")
    k = k_of(w, r0)
    T_harm = 2 * np.pi / np.sqrt(k / (M / 2))
    for g in (1.02, 1.05, 1.1, 1.2, 1.3, 1.4, 1.45):
        if g >= gcap:
            print(f"  {g:>7.2f}  -- above gamma_cap: no bound pair oscillation "
                  f"(reported physics; transit regime -> capture-edge cell)")
            continue
        E = 2 * (g - 1) * M
        Tn = period_newton(E, w, r0)
        Tg = period_gamma(E, w, r0)
        eN, xN, vN = eta_A1_from_omega(2 * np.pi / Tn)
        eG, xG, vG = eta_A1_from_omega(2 * np.pi / Tg)
        fl = floor_gamma(g)
        sN = f"{eN:.3f}" if vN else "SAT-DOM"
        sG = f"{eG:.3f}" if vG else "SAT-DOM"
        sD = f"{eG - eN:+.3f}" if (vN and vG) else "  --  "
        print(f"  {g:>7.2f} {E:>7.2f} {T_harm:>7.3f} {Tn:>8.3f} {Tg:>8.3f} "
              f"{sN:>10} {sG:>10} {sD:>7} {fl:>9.4f}  (x_gam={xG:.2f})")

# ---------- C2 NR-limit spot checks ----------
print("\n[C2] NR limits")
for name, w in WIDTHS.items():
    r0 = req[name]
    k = k_of(w, r0)
    g = 1.0005
    E = 2 * (g - 1) * M
    eH, _, _ = eta_A1_from_omega(np.sqrt(k / (M / 2)))
    eG, _, _ = eta_A1_from_omega(2 * np.pi / period_gamma(E, w, r0))
    print(f"  {name}: eta_A1gamma(g->1)={eG:.4f} vs harmonic {eH:.4f} "
          f"(|d|={abs(eG - eH):.4f})")
print(f"  floor(g->1) = {floor_gamma(1.0005):.5f} (must -> 0.5000)")
print(f"  floor UR asymptote check: floor(g=50) = {floor_gamma(50.0):.5f} "
      f"(1 - 2/pi = {1 - 2 / np.pi:.5f})")
print("\nDone. Verdicts are read in n2a_gamma_record.md against the prereg.")
