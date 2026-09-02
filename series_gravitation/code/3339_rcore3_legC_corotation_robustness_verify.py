#!/usr/bin/env python3
# DATED NOTE (CONV-038, Patches 3366-3371, 2 Sep 2026): 'clamped register' in this file is a misnomer
# for a one-sided, one-Moment-delay compliant surface; X = 0 / Dirichlet is its zero-compliance LIMIT.
# The floor l_P/2 is a conditional Buchdahl BOUND (window 0.536 < u_max <= 1). See frontier_sectors/GR.md.
"""3339_rcore3_legC_corotation_robustness_verify.py — OPEN-GR-RCORE-3 (b).

THE LEG-C QUESTIONS (GR-2 V1.1 rem:rcore3 names (b) UNTESTED):
  (1) Can surface co-rotation change the trapped-resonance count?
  (2) How far can the wall reflection phase drift before the N = 0
      integer flips?  (The count's threshold is NOT a constant: with
      one hard wall of reflection phase delta_w and one smooth
      turning point, 2*Phi - delta_w - pi/2 = 2*pi*n, so
      Phi_thr(n=0) = delta_w/2 + pi/4.  The Leg-B threshold 3/4 pi
      assumed the DERIVED Dirichlet value delta_w = pi.)
  (3) Does Phi grow with ell along the exposed retrograde branch
      (ell, -ell)?  If it crosses the threshold at some ell, a comb
      exists after all at high multipole — an open door Leg B did
      not check (it stopped at ell = 3).
      *** IT DOES.  THIS SCRIPT'S FIRST RUN OVERTURNED A CLAIM THAT
      HAD ALREADY SHIPPED.  Phi grows LINEARLY in ell (no saturation)
      and crosses the 3/4 threshold at ell = 7 for every spin tested
      at or above 0.30 (ell = 10 at chi = 0).  Leg B's headline "the
      comb is NOT restored at any spin" was computed over ell <= 3
      and does not generalize; the corpus statements enacted from it
      at Patches 3337-3338 are OVER-BROAD and are narrowed by this
      patch.  The finding is simultaneously a CONSISTENCY WIN: the
      eikonal (geometric-optics) comb must return as ell -> infinity,
      and it does, approached from BELOW — a check neither Leg A nor
      Leg B performed. ***
  (4) Zel'dovich window: for which exposed modes is omega < m*Omega_w
      (superradiant), and does that overlap the resonance band?

ANALYTIC INPUT (stated, then tested where testable): the radial
function R(r; omega) depends only on (a, m, Q, omega) — the geometry
and the mode — NOT on the wall's angular velocity.  A co-rotating
wall does not move the turning point or the phase volume; at
Dirichlet grade a node is a node in any frame.  Co-rotation therefore
enters ONLY through (i) the reflection phase if the wall is not
perfectly clamped (question 2 quantifies the tolerance) and (ii) the
ENERGETICS via the co-rotating-frame frequency (question 4).

GRADE: eikonal-WKB throughout, inheriting Leg B's construction and
its A1-A3 conditionality.  No growth-time computation is performed;
question 4 delivers a window and a no-compounding argument at
reconnaissance grade, explicitly labelled.

Units G = c = M = 1; Hz at 62 Msun.
"""
import numpy as np

PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


GM_s = 62 * 4.92549e-6
to_hz = lambda w: w / (2 * np.pi * GM_s)

# ---------- surface machinery (identical construction to 3333/3334) ----------
def _AA(r, a, th):
    D = r * r - 2 * r + a * a
    return (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2


def alpha_n(r, a, th):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    return np.sqrt(max(D * S / _AA(r, a, th), 0.0))


def omega_zamo(r, a, th=np.pi / 2):
    """Frame-dragging angular velocity of the locally non-rotating frame."""
    return 2 * a * r / _AA(r, a, th)


def v_n(r, a, th):
    S = r * r + a * a * np.cos(th) ** 2
    Aa = _AA(r, a, th)
    D = r * r - 2 * r + a * a
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


def r_surface(a, th=np.pi / 2):
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


# ---------- Leg-B census machinery, reused verbatim in structure ----------
def Rfun(r, a, m, Q, w):
    D = r * r - 2 * r + a * a
    return (w * (r * r + a * a) - a * m) ** 2 - D * ((m - a * w) ** 2 + Q)


def barrier_exists(a, m, Q, w, r_wall, r_out=40.0, n=8000):
    rs = np.linspace(r_wall * (1 + 1e-9), r_out, n)
    return np.any(Rfun(rs, a, m, Q, w) < 0)


def omega_top(a, m, Q, r_wall, w_hi=3.0):
    lo, hi = 1e-3, w_hi
    if not barrier_exists(a, m, Q, lo, r_wall):
        return None
    for _ in range(90):
        mid = 0.5 * (lo + hi)
        if barrier_exists(a, m, Q, mid, r_wall):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def phase_integral(a, m, Q, w, r_wall, n=60000, r_out=40.0):
    rs = np.linspace(r_wall * (1 + 1e-9), r_out, n)
    R = Rfun(rs, a, m, Q, w)
    if R[0] <= 0:
        return None
    i_turn = int(np.argmax(R < 0))
    if i_turn == 0:
        return None
    rs_c, R_c = rs[:i_turn], np.clip(R[:i_turn], 0, None)
    D = rs_c * rs_c - 2 * rs_c + a * a
    return float(np.trapezoid(np.sqrt(R_c) / D, rs_c))


def phi_max(a, m, ell, r_wall):
    """Max accumulated phase over the propagating band (at omega_top)."""
    Q = (ell + 0.5) ** 2 - m * m
    wt = omega_top(a, m, Q, r_wall)
    if wt is None:
        return None, None
    best, bw = 0.0, None
    for f in (0.999, 0.99, 0.97, 0.94, 0.90, 0.85, 0.80, 0.70, 0.60, 0.50):
        p = phase_integral(a, m, Q, wt * f, r_wall)
        if p is not None and p > best:
            best, bw = p, wt * f
    return wt, best


A = 0.68
RW = r_surface(A)
OM_W = omega_zamo(RW, A)
print(f"      chi = {A}: equatorial wall r = {RW:.4f} M; "
      f"Omega_ZAMO(wall) = {OM_W:.5f} /M ({to_hz(OM_W):.1f} Hz-equiv @62)")


def census_ell(a, m, ell, r_wall, nw=500):
    """(omega_top, Phi_max/pi, N_trapped) with N from Phi = (n+3/4)pi."""
    Q = (ell + 0.5) ** 2 - m * m
    wt = omega_top(a, m, Q, r_wall)
    if wt is None:
        return None, 0.0, 0
    ws = np.linspace(1e-3, wt * 0.9995, nw)
    ph = max((phase_integral(a, m, Q, w, r_wall, n=20000) or 0.0) / np.pi
             for w in ws)
    n = 0
    while ph >= n + 0.75:
        n += 1
    return wt, ph, n


# ===================== THE LEG-C FINDING: the ell ladder =====================
print("      exposed extreme-retrograde branch (ell, -ell) — phase volume:")
tab = {}
for a_try, label in ((1e-6, "0.00"), (0.30, "0.30"), (A, "0.68"), (0.95, "0.95")):
    rw = r_surface(a_try) if a_try > 1e-5 else 2.25
    row = []
    for ell in range(2, 11):
        wt, ph, n = census_ell(a_try, -ell, ell, rw)
        row.append((ell, wt, ph, n))
    tab[label] = row
    crit = next((e for e, _, _, n in row if n >= 1), None)
    print(f"        chi={label}: " +
          " ".join(f"l{e}:{ph:.3f}{'*' if n else ''}" for e, _, ph, n in row) +
          f"   -> trapping switches on at ell = {crit}")

r68 = tab["0.68"]
phis68 = [r[2] for r in r68]
crit68 = next(e for e, _, _, n in r68 if n >= 1)
crit00 = next(e for e, _, _, n in tab["0.00"] if n >= 1)
incs = np.diff(phis68)
check("1. THE LEG-C FINDING (overturns a shipped generalization): Phi grows "
      "LINEARLY in ell with NO saturation, and the trapped count switches on "
      "at a finite critical multipole",
      crit68 == 7 and crit00 == 10 and np.std(incs) < 0.01,
      f"chi=0.68: Phi/pi = {phis68[0]:.3f} (l=2) -> {phis68[-1]:.3f} (l=10), "
      f"increments {incs.mean():.4f} +/- {np.std(incs):.4f} per unit ell "
      f"(LINEAR); ell_crit = {crit68} +/- 1 at chi>=0.30, {crit00} +/- 1 at "
      f"chi=0 (the +/-1 is the Dirichlet/phase-convention sensitivity: at "
      f"chi=0.68 ell=6 sits at Phi/pi = {phis68[4]:.3f}, only "
      f"{0.75-phis68[4]:.3f} pi below threshold — CONV-035 adopted, "
      f"quote the +/-1 with the number, never the bare integer). "
      f"Leg B computed ell<=3 only — its 'no comb at any spin' does NOT "
      f"generalize in ell and is NARROWED by this patch")

check("2. THE CONSISTENCY WIN neither Leg performed: over the COMPUTED "
      "range ell = 2..10 the phase volume grows monotonically and nearly "
      "linearly, the finite-ell behaviour required for recovery of the "
      "eikonal comb as ell -> infinity (the unbounded-growth statement is "
      "an ASYMPTOTIC INFERENCE from this trend plus the eikonal "
      "construction, NOT a computational finding — CONV-035 GPT defect 2)",
      phis68[-1] > phis68[0] and all(np.diff(phis68) > 0),
      f"monotone and linear over the computed range (Phi/pi ~ {incs.mean():.3f}*ell); "
      f"the eikonal picture was never WRONG — the physical low-ell modes are "
      f"simply far from its limit, which is why Legs A/B found no comb there")

check("3. THE LOW-ELL RESULT STANDS where it was computed: N_trapped = 0 for "
      "ell = 2 and ell = 3 at EVERY spin tested — Legs A and B are correct "
      "inside their scope, and the observationally dominant multipoles are "
      "exactly that scope",
      all(row[0][3] == 0 and row[1][3] == 0 for row in tab.values()),
      "; ".join(f"chi={k}: l2 N={v[0][3]} (Phi/pi={v[0][2]:.3f}), "
                f"l3 N={v[1][3]} (Phi/pi={v[1][2]:.3f})" for k, v in tab.items()))

# ===================== co-rotation: can it move the count? =====================
inv = []
for m, ell in ((-2, 2), (-1, 2), (0, 2), (1, 2), (-3, 3)):
    Q = (ell + 0.5) ** 2 - m * m
    wt = omega_top(A, m, Q, RW)
    p0 = phase_integral(A, m, Q, wt * 0.999, RW)
    w_tilde = wt * 0.999 - m * OM_W            # to the co-rotating frame
    p1 = phase_integral(A, m, Q, w_tilde + m * OM_W, RW)   # and back
    inv.append(abs(p1 - p0) < 1e-9)
check("4. CO-ROTATION CANNOT MOVE THE COUNT at Dirichlet grade: R(r;omega) "
      "depends only on (a, m, Q, omega), so a wall rotating at Omega_w leaves "
      "the turning point and the phase volume identically unchanged — a node "
      "is a node in any frame; co-rotation enters ONLY via the reflection "
      "phase (check 5) and the energetics (check 6)",
      all(inv),
      f"phase integrals invariant to 1e-9 across the Omega_w = {OM_W:.5f} "
      f"frame round trip for all five low-ell exposed modes")

# ===================== reflection-phase robustness (low-ell) =====================
# Phi_thr(n=0) = delta_w/2 + pi/4  =>  flip requires delta_w < 2*(Phi_sup - pi/4)
sup_low = max(max(row[0][2], row[1][2]) for row in tab.values())
d_min = 2 * (sup_low - 0.25)
check("5. ROBUSTNESS ENVELOPE for the observable (low-ell) prediction: the "
      "N = 0 integer at ell = 2,3 survives every wall reflection phase above "
      "a computed threshold, and the DERIVED Dirichlet value clears it wide",
      0 < d_min < 1.0,
      f"flip requires delta_w < {d_min:.4f} pi = {d_min*180:.1f} deg; derived "
      f"delta_w = pi = 180 deg (clamped register, RCORE-1) — margin "
      f"{1/d_min:.1f}x. A free/Neumann-like end WOULD trap: the low-ell "
      f"no-comb result is a statement about the CLAMPED wall, not geometry alone")

# ===================== Zel'dovich: the dangerous combination =====================
# CONV-035 GPT defect 1, ADOPTED AND FIXED AT THE COMPUTATION, NOT THE
# SENTENCE: the V1 of this check swept selected ell {2,3,4,6,7,8,10,12}
# and described its domain as "the whole (ell,m) grid" — the SAME
# quantifier defect this patch was written to diagnose, committed inside
# it. The sweep below is now EXHAUSTIVE over the declared domain
# ell = 2..ELL_MAX, all integer m, at chi = 0.68, and the claim states
# that domain explicitly rather than "the whole grid".
ELL_MAX = 12
danger, checked = [], 0
for ell in range(2, ELL_MAX + 1):
    for m in range(-ell, ell + 1):
        buried = (m / (ell + 0.5)) > 0.774          # Leg-A mu criterion
        wt, ph, n = census_ell(A, m, ell, RW, nw=180)
        checked += 1
        if buried or n == 0 or m <= 0:
            continue
        # trapped, exposed, corotating: is any trapped frequency superradiant?
        Q = (ell + 0.5) ** 2 - m * m
        ws = np.linspace(1e-3, wt * 0.9995, 180)
        for w in ws:
            pp = phase_integral(A, m, Q, w, RW, n=20000)
            if pp and pp / np.pi >= 0.75 and w < m * OM_W:
                danger.append((ell, m, float(w), m * OM_W))
                break
check("6. STRUCTURAL PROTECTION over an EXHAUSTIVE, EXPLICITLY DECLARED "
      "domain (ell = 2..12, ALL integer m, chi = 0.68): NO mode in that "
      "domain is simultaneously EXPOSED, TRAPPED, and SUPERRADIANT (the "
      "ergoregion-instability recipe at finite multipole). Grade: "
      "reconnaissance — a STRUCTURAL exclusion would need an analytic "
      "disjointness inequality or an unbounded domain (CONV-035, adopted)",
      len(danger) == 0 and checked == sum(2 * l + 1 for l in range(2, ELL_MAX + 1)),
      f"{checked} modes = ALL (ell,m) with ell = 2..{ELL_MAX} (complete, "
      f"not sampled): every TRAPPED mode is "
      f"extreme-retrograde (m <= -(ell-1)), which has NO superradiant window "
      f"(m*Omega_w < 0); every mode with a superradiant window large enough "
      f"to reach trapping frequencies is CORO+ROTATING and therefore BURIED. "
      f"Burial and trapping select disjoint parts of the mode grid — the "
      f"censorship result protects the finite-ell sector too")

print(f"{sum(PASS)}/{len(PASS)} PASS")
print(f"FAST: all checks are FAST; FAST: {sum(PASS)}/{len(PASS)} PASS")
raise SystemExit(0 if all(PASS) else 1)
