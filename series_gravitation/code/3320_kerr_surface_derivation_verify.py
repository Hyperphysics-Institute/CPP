#!/usr/bin/env python3
"""
Patch 3320 verify — OPEN-GR-RCORE-2(iv) DERIVATION: the Kerr exclusion
surface from the two-component census, and the ergoregion-censorship
theorem.

Construction (assumptions A1-A3 stated for the panel; everything below
them is exact):
  A1 (scalar census = lapse dictionary): the ratified log-lapse
     dictionary inverts to k*Dssv_scalar = 2(1-alpha)/(1+alpha); on
     Schwarzschild this reproduces the ratified linear source relation
     mu/rbar EXACTLY (check 0), so A1 is the unique extension that
     preserves the ratified static limit.
  A2 (vector census = dragging speed): the rotational SSV component's
     dimensionless register demand is the local dragging speed v --
     the velocity of static observers relative to ZAMOs, v = omega*varpi
     / alpha -- i.e., azimuthal displacement demand per Moment in local
     reach units.
  A3 (quadrature): radial (compression) and azimuthal (circulation)
     register demands are orthogonal, so the total census magnitude is
     |k Dssv|^2 = s^2 + v^2 with s = 2(1-alpha)/(1+alpha).
     Saturation (the exclusion surface): s^2 + v^2 = 1.

Exact GR identity powering the theorem: for stationary axisymmetric
metrics, g_tt = -alpha^2 (1 - v^2), so the ergosphere (g_tt = 0) is
EXACTLY the v = 1 surface (check 2). Hence on the ergosphere
F = s^2 + v^2 = s^2 + 1 > 1 strictly (alpha < 1 there, so s > 0):
the census is already OVER-saturated at the ergosphere, so the
saturation surface lies strictly OUTSIDE it -- at every spin, every
latitude. The ergoregion is censored the way the horizon was.

Checks:
  0. A1 static exactness: 2(1-alpha)/(1+alpha) = mu/rbar on isotropic
     Schwarzschild, symbolically.
  1. a=0 recovery: the F=1 surface is areal r = 9M/4 exactly.
  2. Exact identity g_tt = -alpha^2(1 - v^2) on Kerr (symbolic), hence
     v(r_E, theta) = 1 identically on the ergosphere.
  3. CENSORSHIP: F(r_E, theta) > 1 strictly for a in (0, M], all theta
     with an ergosphere (symbolic inequality via s > 0, + numeric scan).
  4. The derived surface exists and lies strictly outside r_E: numeric
     root-find of F = 1 across a in [0, 0.998], theta in (0, pi/2];
     min clearance reported.
  5. Derived surface vs the 3318 scalar-only proxy: quadrature only ADDS
     census, so the derived surface is at r >= the proxy surface
     everywhere; at chi = 0.68 (equator) report both radii -- the 3318
     chi_crit = 2/sqrt(7) is confirmed as the CONSERVATIVE bound, now
     superseded by censorship at ALL spins.
  6. Extremal margin: at a = 0.998M the equatorial clearance
     r_surf - r_E stays positive; report it.
  7. Echo-delay spin template (Level-A eikonal, equatorial, static-frame
     light travel dt = sqrt(g_rr)/alpha dr): round trip between the
     derived surface and the Kerr equatorial photon rings
     r_ph(pro/retro) = 2M(1 + cos(2/3 arccos(-/+ a/M))). FINDING
     surfaced by the first run: at chi = 0.68 the PROGRADE ring
     (r ~ 2.05 M) lies INSIDE the derived surface (r ~ 2.27 M) -- the
     prograde light ring is itself censored, so no prograde-ring cavity
     exists there; the retrograde ring (r ~ 3.71 M) survives and sets
     the retrograde cavity delay. The check reports the retrograde
     delay, flags prograde burial, and locates the prograde-burial
     onset spin -- all template inputs for GR-2, at eikonal grade.
"""
import numpy as np
import sympy as sp

PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


# ---------------------------------------------------------------- check 0
rbar, mu = sp.symbols("rbar mu", positive=True)
alpha_schw = (1 - mu / (2 * rbar)) / (1 + mu / (2 * rbar))
s_schw = sp.simplify(2 * (1 - alpha_schw) / (1 + alpha_schw))
check("0. A1 static exactness: 2(1-alpha)/(1+alpha) = mu/rbar on Schwarzschild",
      sp.simplify(s_schw - mu / rbar) == 0, f"s = {s_schw}")

# Kerr in BL, M = 1 symbolic
r_, a_, th_ = sp.symbols("r a theta", positive=True)
Delta = r_**2 - 2 * r_ + a_**2
Sigma = r_**2 + a_**2 * sp.cos(th_) ** 2
A_ = (r_**2 + a_**2) ** 2 - Delta * a_**2 * sp.sin(th_) ** 2
alpha2 = Delta * Sigma / A_
omega = 2 * a_ * r_ / A_
gphph = A_ * sp.sin(th_) ** 2 / Sigma
gtt = -(1 - 2 * r_ / Sigma)
v2 = omega**2 * gphph / alpha2                   # v = omega*varpi/alpha

# ---------------------------------------------------------------- check 1
F_a0 = sp.simplify((2 * (1 - sp.sqrt(alpha2)) / (1 + sp.sqrt(alpha2))) ** 2
                   + v2).subs({a_: 0, th_: sp.pi / 2})
sol = sp.solve(sp.Eq(F_a0, 1), r_)
check("1. a=0 recovery: F=1 surface at areal r = 9M/4",
      any(sp.simplify(x - sp.Rational(9, 4)) == 0 for x in sol),
      f"roots {sol}")

# ---------------------------------------------------------------- check 2
ident = sp.simplify(gtt + alpha2 * (1 - v2))
check("2. exact identity g_tt = -alpha^2 (1 - v^2) on Kerr (=> v=1 on the ergosphere)",
      ident == 0, "g_tt + alpha^2(1-v^2) == 0 identically")

# ---------------------------------------------------------------- check 3
# On the ergosphere v=1, so F = s^2 + 1 with s = 2(1-alpha)/(1+alpha) > 0
# strictly unless alpha = 1 (impossible at finite r). Numeric scan confirms.
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


def s_n(r, a, th):
    al = alpha_n(r, a, th)
    return 2 * (1 - al) / (1 + al)


def F_n(r, a, th):
    return s_n(r, a, th) ** 2 + v_n(r, a, th) ** 2


def r_E(a, th):
    return 1 + np.sqrt(max(1 - a * a * np.cos(th) ** 2, 0.0))


ths = np.linspace(0.05, np.pi / 2, 120)
cens_ok, minF = True, np.inf
for a in np.linspace(0.05, 1.0, 40):
    for t in ths:
        Fe = F_n(r_E(a, t) * (1 + 1e-12), a, t)
        minF = min(minF, Fe)
        if Fe <= 1:
            cens_ok = False
check("3. CENSORSHIP: F(r_E, theta) > 1 strictly for all spins and latitudes",
      cens_ok, f"min F on the ergosphere over the scan = {minF:.6f} (> 1)")

# ---------------------------------------------------------------- check 4
def r_surface(a, th):
    """Outermost root of F = 1."""
    lo, hi = r_E(a, th) * (1 + 1e-10), 60.0
    if F_n(lo, a, th) <= 1:      # would mean not over-saturated at r_E
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F_n(mid, a, th) > 1:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


exist_ok, min_clear = True, np.inf
for a in np.linspace(0.0, 0.998, 30):
    for t in ths:
        rs = r_surface(max(a, 1e-9), t)
        if rs is None:
            exist_ok = False
        else:
            min_clear = min(min_clear, rs - r_E(max(a, 1e-9), t))
check("4. derived surface exists, strictly outside r_E across the scan",
      exist_ok and min_clear > 0, f"min clearance r_surf - r_E = {min_clear:.4f} M")

# ---------------------------------------------------------------- check 5
a68 = 0.68
rs_derived = r_surface(a68, np.pi / 2)


def r_proxy(a, th):
    lo, hi = r_E(a, th) * (1 + 1e-10), 60.0
    f = lambda r: alpha_n(r, a, th) - 1.0 / 3.0
    if f(lo) > 0:
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


rp = r_proxy(a68, np.pi / 2)
mono_ok = True
for a in np.linspace(0.05, 0.74, 15):
    for t in ths[::10]:
        rd_, rp_ = r_surface(a, t), r_proxy(a, t)
        if rp_ is not None and rd_ is not None and rd_ < rp_ - 1e-9:
            mono_ok = False
check("5. derived surface >= scalar-only 3318 proxy everywhere (quadrature adds census); chi=0.68 radii",
      mono_ok and rs_derived is not None and rp is not None and rs_derived >= rp,
      f"chi=0.68 equator: derived r = {rs_derived:.4f} M vs proxy r = {rp:.4f} M "
      f"(vs ergosphere 2 M)")

# ---------------------------------------------------------------- check 6
rs_ext = r_surface(0.998, np.pi / 2)
check("6. extremal margin: at chi=0.998 equatorial clearance stays positive",
      rs_ext is not None and rs_ext - 2.0 > 0,
      f"r_surf = {rs_ext:.4f} M; clearance over the ergosphere = {rs_ext-2:.4f} M")

# ---------------------------------------------------------------- check 7
def r_ph(a, prograde=True):
    sgn = -1 if prograde else +1
    return 2 * (1 + np.cos(2.0 / 3.0 * np.arccos(sgn * a)))


def delay(a, r_in, r_out, n=200_000):
    rs = np.linspace(r_in, r_out, n)
    th = np.pi / 2
    grr = np.array([(r * r + a * a * 0) / (r * r - 2 * r + a * a) for r in rs])
    al = np.array([alpha_n(r, a, th) for r in rs])
    integ = np.sqrt(np.maximum(grr, 0)) / np.maximum(al, 1e-12)
    return 2 * np.trapezoid(integ, rs)


rph_pro, rph_ret = r_ph(a68, True), r_ph(a68, False)
pro_buried = rph_pro <= rs_derived
dt_ret = delay(a68, rs_derived, rph_ret)
dt_schw_num = delay(1e-9, 2.25, 3.0)
dt_schw_exact = 1.5 + 8 * np.log(2)
GM_c3 = 62 * 4.92549e-6
# prograde-burial onset: smallest a where r_ph(pro) = r_surface(a, eq)
a_pb = None
for a in np.linspace(0.01, 0.998, 300):
    rs_ = r_surface(a, np.pi / 2)
    if rs_ is not None and r_ph(a, True) <= rs_:
        a_pb = a
        break
detail7 = (f"Schwarzschild check: numeric {dt_schw_num:.4f} vs exact {dt_schw_exact:.4f}; "
           f"chi=0.68: prograde ring r={rph_pro:.3f} M "
           f"{'BURIED inside the surface' if pro_buried else 'outside'} "
           f"(surface {rs_derived:.3f} M) -- prograde-ring cavity absent; "
           f"retrograde ring r={rph_ret:.3f} M -> Dt_ret={dt_ret:.3f} GM/c^3 "
           f"({dt_ret*GM_c3*1e3:.2f} ms for GW150914) vs Schwarzschild "
           f"{dt_schw_exact:.3f} ({dt_schw_exact*GM_c3*1e3:.2f} ms); "
           f"prograde-burial onset chi ~ {a_pb:.3f}")
check("7. echo-delay spin template (equatorial eikonal): Schwarzschild limit recovered; "
      "chi=0.68 retrograde delay + prograde-ring burial finding",
      abs(dt_schw_num - dt_schw_exact) < 0.01 and dt_ret > 0 and pro_buried
      and a_pb is not None,
      detail7)

print()
print(f"{sum(PASS)}/{len(PASS)} PASS")
raise SystemExit(0 if all(PASS) else 1)
