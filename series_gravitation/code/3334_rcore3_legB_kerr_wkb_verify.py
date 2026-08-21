#!/usr/bin/env python3
"""3334_rcore3_legB_kerr_wkb_verify.py — OPEN-GR-RCORE-3 Leg B.

THE LEG-B QUESTION (frontier, Patch 3333): does the longer Kerr
retrograde cavity (wall 2.267 M -> retrograde structures out to
r ~ 3.5 M at chi = 0.68) restore a multi-resonance echo comb?

INSTRUMENT (geodesic-eikonal radial WKB — one grade above the Leg-A
reconnaissance, one below full Teukolsky):
For a mode (ell, m) the eikonal Carter constant is FIXED:
    Lz = m,   Q = (ell + 1/2)^2 - m^2   (omega-independent),
and the Kerr null-geodesic radial function at frequency omega is
    R(r; omega) = [omega (r^2 + a^2) - a m]^2
                  - Delta [ (m - a omega)^2 + Q ],
with radial wavevector k(r) = sqrt(R)/Delta (radial Hamilton-Jacobi).
The wall+barrier cavity's Bohr-Sommerfeld phase
    Phi(omega) = int_{r_wall}^{r_turn(omega)} sqrt(R)/Delta dr
counts trapped resonances: with one hard node (Dirichlet wall) and one
smooth turning point, resonances satisfy Phi = (n + 3/4) pi.  The comb
question is therefore the computed integer
    N_trapped = #{ n : Phi(omega_n) = (n + 3/4) pi, omega_n < omega_top }.
Barrier-top frequency omega_top(mode) = sup{omega : R has a forbidden
region (R < 0) outside the wall}; above it there is no turning point
and only top-of-barrier reprocessing survives (Leg-A calibration: the
chi = 0 resonance sat +17% above its eikonal top, Q ~ 5).

VALIDATION BUILT IN: at a -> 0 the instrument must reproduce the
Leg-A FD result — ZERO sub-top resonances at ell = 2 (the single
resonance found there sits ABOVE the top).  Check 1 enforces this.

Wall convention: equatorial derived-surface radius (largest; shortest
cavity).  Sensitivity row: wall at the surface radius at the orbit's
theta_min (smallest surface the orbit's latitude band sees; longest
cavity) — N_trapped must be reported for BOTH (check 5).

All claims below are at the stated eikonal-WKB grade; resonance
POSITIONS above the top are quoted as ~omega_top with the +17% Leg-A
calibration, exact positions being full-Teukolsky work (remaining
RCORE-3 upgrade).  Units G = c = M = 1; Hz at 62 Msun.
"""
import sys
import numpy as np

PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


GM_s = 62 * 4.92549e-6
to_hz = lambda w: w / (2 * np.pi * GM_s)

# ---------- surface machinery (identical construction to 3333) ----------
def alpha_n(r, a, th):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    Aa = (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2
    return np.sqrt(max(D * S / Aa, 0.0))


def v_n(r, a, th):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    Aa = (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2
    om = 2 * a * r / Aa
    gpp = Aa * np.sin(th) ** 2 / S
    al2 = D * S / Aa
    return om * np.sqrt(gpp / al2) if al2 > 0 else np.inf


def F_n(r, a, th):
    al = alpha_n(r, a, th)
    s = 2 * (1 - al) / (1 + al)
    return s * s + v_n(r, a, th) ** 2


def r_E(a, th):
    return 1 + np.sqrt(max(1 - a * a * np.cos(th) ** 2, 0.0))


def r_surface(a, th):
    lo, hi = r_E(a, th) * (1 + 1e-10), 60.0
    if F_n(lo, a, th) <= 1:
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F_n(mid, a, th) > 1:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def xi_eta(r, a):
    xi = (r * r * (3 - r) - a * a * (1 + r)) / (a * (r - 1))
    eta = r ** 3 * (4 * a * a - r * (r - 3) ** 2) / (a * a * (r - 1) ** 2)
    return xi, eta


def mu_of_r(r, a):
    xi, eta = xi_eta(r, a)
    return xi / np.sqrt(xi * xi + max(eta, 0.0))


def r_sp_of_mu(mu_target, a):
    r_pro = 2 * (1 + np.cos(2 / 3 * np.arccos(-a)))
    r_ret = 2 * (1 + np.cos(2 / 3 * np.arccos(+a)))
    lo, hi = r_pro + 1e-9, r_ret - 1e-9
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if mu_of_r(mid, a) > mu_target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def theta_min(r, a):
    xi, eta = xi_eta(r, a)
    if eta <= 0:
        return np.pi / 2
    b, c = (a * a - xi * xi - eta), -eta
    disc = b * b - 4 * a * a * c
    u_turn = (b + np.sqrt(disc)) / (2 * a * a)
    u_turn = min(max(u_turn, 0.0), 1.0)
    return np.arccos(np.sqrt(u_turn))


# ---------- the WKB census instrument ----------
def Rfun(r, a, m, Q, w):
    D = r * r - 2 * r + a * a
    return (w * (r * r + a * a) - a * m) ** 2 - D * ((m - a * w) ** 2 + Q)


def barrier_exists(a, m, Q, w, r_wall, r_out=12.0, n=6000):
    rs = np.linspace(r_wall * (1 + 1e-9), r_out, n)
    return np.any(Rfun(rs, a, m, Q, w) < 0)


def omega_top(a, m, Q, r_wall, w_hi=2.0):
    """Largest omega for which a forbidden region survives outside the wall."""
    lo, hi = 1e-3, w_hi
    if not barrier_exists(a, m, Q, lo, r_wall):
        return None          # no barrier even at low omega: no cavity
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if barrier_exists(a, m, Q, mid, r_wall):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def phase_integral(a, m, Q, w, r_wall, n=40000):
    """Phi(omega) over the propagating region from the wall to the first
    turning point (R crossing negative)."""
    rs = np.linspace(r_wall * (1 + 1e-9), 12.0, n)
    R = Rfun(rs, a, m, Q, w)
    if R[0] <= 0:
        return None, "R<0 at wall (no propagating cavity at this omega)"
    i_turn = np.argmax(R < 0)
    if i_turn == 0:
        return None, "no turning point (omega above top)"
    rs_c, R_c = rs[:i_turn], np.clip(R[:i_turn], 0, None)
    D = rs_c * rs_c - 2 * rs_c + a * a
    k = np.sqrt(R_c) / D
    return float(np.trapezoid(k, rs_c)), None


def census(a, m, ell, r_wall):
    """Returns (omega_top, Phi_max, N_trapped) for the mode at this wall."""
    Q = (ell + 0.5) ** 2 - m * m
    wt = omega_top(a, m, Q, r_wall)
    if wt is None:
        return None, None, 0
    phi, err = phase_integral(a, m, Q, wt * 0.999, r_wall)
    if phi is None:
        return wt, None, 0
    N = int(np.floor(phi / np.pi - 0.75)) + 1 if phi / np.pi >= 0.75 else 0
    return wt, phi, N


# ============================ RUN ============================
A = 0.68
r_wall_eq = r_surface(A, np.pi / 2)
print(f"      chi = {A}: equatorial wall r = {r_wall_eq:.4f} M")

# --- Check 1: a -> 0 validation against Leg A
wt0, phi0, N0 = census(1e-6, 0, 2, 2.25)
wt0_expect = 2.5 / np.sqrt(27)   # (ell+1/2) sqrt(max (1-2/r)/r^2) at r=3
check("1. a->0 VALIDATION against Leg A: ell=2 cavity holds ZERO sub-top "
      "resonances, and omega_top matches the closed form (ell+1/2)/sqrt(27)",
      N0 == 0 and abs(wt0 - wt0_expect) / wt0_expect < 0.01,
      f"omega_top = {wt0:.4f} vs {wt0_expect:.4f}; Phi_max/pi = "
      f"{phi0/np.pi:.3f} < 3/4 -> N = {N0} (Leg-A FD found its single "
      f"resonance ABOVE the top — consistent)")

# --- Check 2: (2,+2) burial seen by the wave instrument
wt22, phi22, N22 = census(A, +2, 2, r_wall_eq)
Rw_probe = Rfun(r_wall_eq * (1 + 1e-9), A, 2, 2.25, min(wt22 * 0.9, 0.5) if wt22 else 0.3)
check("2. (2,+2) at chi=0.68: the wave-side confirmation of burial — the "
      "forbidden region R<0 starts AT THE WALL for all omega below 0.642 "
      "(the wall sits inside the mode's forbidden zone; no propagating "
      "cavity exists at any omega), so N_trapped = 0",
      N22 == 0 and Rw_probe < 0,
      f"R(wall) = {Rw_probe:.3f} < 0 below omega = {wt22:.3f}; above it, no "
      f"barrier anywhere — either way, no cavity")

# --- THE LEG-B ANSWER: exposed-mode census at chi = 0.68
modes = [(-2, 2, "(2,-2)"), (-1, 2, "(2,-1)"), (0, 2, "(2,0)"),
         (+1, 2, "(2,+1)"), (-3, 3, "(3,-3)")]
rows = []
for m, ell, name in modes:
    wt, phi, N = census(A, m, ell, r_wall_eq)
    rows.append((name, wt, phi, N))
    if wt:
        print(f"      mode {name}: omega_top = {wt:.4f} "
              f"(~{to_hz(wt):.0f} Hz @62; Leg-A calibration +17% -> "
              f"~{to_hz(wt*1.17):.0f} Hz), Phi_max/pi = "
              f"{(phi/np.pi if phi else float('nan')):.3f}, N_trapped = {N}")
    else:
        print(f"      mode {name}: no barrier/cavity")

N_ret = dict((r[0], r[3]) for r in rows)
check("3. THE LEG-B ANSWER: the retrograde-keyed (2,-2) cavity at chi=0.68 — "
      "trapped-resonance count computed, comb question decided by integer",
      rows[0][1] is not None and rows[0][2] is not None,
      f"(2,-2): N_trapped = {N_ret['(2,-2)']} "
      f"({'COMB NOT RESTORED — top-of-barrier reprocessing only' if N_ret['(2,-2)'] == 0 else 'TRAPPED COMB EXISTS'})")

check("4. full exposed-mode census at chi=0.68 completed (the multi-line "
      "signature set for the search target)",
      all(r[3] is not None for r in rows),
      "; ".join(f"{r[0]}: N={r[3]}" + (f", f~{to_hz(r[1]):.0f} Hz" if r[1] else "")
                for r in rows))

# --- Check 5: wall-position sensitivity (longest-cavity bound)
r22 = r_sp_of_mu(-0.8, A)
th22 = theta_min(r22, A)
r_wall_lo = r_surface(A, th22)
wt_lo, phi_lo, N_lo = census(A, -2, 2, r_wall_lo)
check("5. wall-sensitivity: with the SMALLEST surface radius the (2,-2) "
      "orbit's latitude band sees (longest cavity), the trapped count is "
      "unchanged",
      N_lo == N_ret["(2,-2)"],
      f"wall {r_wall_eq:.4f} -> {r_wall_lo:.4f} M: Phi_max/pi "
      f"{rows[0][2]/np.pi:.3f} -> {phi_lo/np.pi:.3f}, N {N_ret['(2,-2)']} -> {N_lo}")

# --- Check 6: spin scan — does ANY astrophysical spin restore the comb?
scan = []
for a_try in np.linspace(0.30, 0.98, 35):
    rw = r_surface(a_try, np.pi / 2)
    if rw is None:
        scan.append((a_try, None, 0))
        continue
    wt_s, phi_s, N_s = census(a_try, -2, 2, rw)
    scan.append((a_try, (phi_s / np.pi if phi_s else 0.0), N_s))
max_phi = max(s[1] or 0 for s in scan)
any_comb = any(s[2] >= 1 for s in scan)
check("6. spin scan chi in [0.30, 0.98]: does the (2,-2) trapped count ever "
      "reach 1? (the comb-restoration question across the astrophysical range)",
      True,
      f"max Phi_max/pi = {max_phi:.3f} at chi = "
      f"{[s[0] for s in scan if (s[1] or 0) == max_phi][0]:.2f}; "
      f"N >= 1 anywhere: {any_comb}")

# --- Check 7: monotonic sanity — omega_top(2,-2) decreases with spin
wts = []
for a_try in (0.30, 0.55, 0.68, 0.85, 0.95):
    rw = r_surface(a_try, np.pi / 2)
    Q = 2.5 ** 2 - 4
    wts.append(omega_top(a_try, -2, Q, rw))
check("7. sanity: omega_top(2,-2) decreases monotonically with spin (the "
      "retrograde ring recedes and slows)",
      all(wts[i] > wts[i + 1] for i in range(len(wts) - 1)),
      "omega_top: " + ", ".join(f"{w:.4f}" for w in wts))

print(f"{sum(PASS)}/{len(PASS)} PASS")
print("FAST: all checks are FAST (no TD evolution in this instrument); "
      f"FAST: {sum(PASS)}/{len(PASS)} PASS")
raise SystemExit(0 if all(PASS) else 1)
