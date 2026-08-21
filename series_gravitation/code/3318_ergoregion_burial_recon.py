#!/usr/bin/env python3
"""
Patch 3318 verify — OPEN-GR-RCORE-2(iv) RECONNAISSANCE: is the would-be
ergoregion of a spinning CPP compact object buried inside the exclusion
surface?

Proxy surface criterion (dictionary-consistent, reconnaissance grade):
the ratified log-lapse dictionary N = -2 artanh(k Dssv / 2) makes
saturation (k Dssv = 1) EQUIVALENT to lapse = 1/3 at a = 0 (both routes
ratified, CONV-030 check 2). The reconnaissance surface for spinning
objects is therefore the Kerr ZAMO-lapse-1/3 surface, alpha = 1/3, with
the honest caveat that the true Kerr exclusion surface requires the
rotational-census source relation (GR-1f op:allorders territory) — the
proxy is exact at a = 0 and dictionary-motivated at a > 0.

Kerr (Boyer-Lindquist, G = c = 1):
  Delta = r^2 - 2 M r + a^2,   Sigma = r^2 + a^2 cos^2(th),
  A = (r^2 + a^2)^2 - Delta a^2 sin^2(th),
  ZAMO lapse: alpha^2 = Delta Sigma / A.
  Ergosphere (g_tt = 0): r_E(th) = M + sqrt(M^2 - a^2 cos^2 th).

Checks:
  0. a = 0 RECOVERY: alpha = 1/3 at areal r = 9M/4 exactly — the proxy
     reproduces F-R1's ratified static surface (consistency anchor).
  1. Lapse ON the equatorial ergosphere, closed form:
     alpha^2(r_E, eq) = a^2 / (2 (2 M^2 + a^2)) — symbolic.
  2. CRITICAL SPIN, exact: alpha(r_E, eq) = 1/3  ==>  a_crit = 2M/sqrt(7)
     (chi_crit = 2/sqrt(7) ~ 0.7559) — symbolic solve.
  3. EQUATOR IS THE BINDING CASE: on the ergosphere surface, the lapse is
     MAXIMIZED at the equator (it falls to zero at the poles, where the
     ergosphere touches the horizon) — exposure (alpha(r_E) > 1/3) thus
     strikes first at the equator, so equatorial burial implies burial
     at all latitudes.
  4. BURIAL BELOW a_crit: for chi in {0.3, 0.5, 0.68, 0.7559-eps} the
     alpha = 1/3 surface lies OUTSIDE r_E(th) for ALL th (numeric root
     find) — no exterior ergoregion, no negative-energy modes, no
     ergoregion instability. chi = 0.68 is the GW150914-class remnant.
  5. EXPOSURE ABOVE a_crit: for chi in {0.80, 0.95, 0.998} an exterior
     equatorial ergoregion BAND exists (r_surface < r_E near the
     equator); report the band's latitudinal extent — the instability
     question is live only there.
  6. MARGIN AT THE GW POPULATION: burial condition = alpha(r_E,eq) < 1/3
     (the lapse rises outward through 1/3 at r > r_E, putting the
     exclusion surface OUTSIDE the ergosphere). At chi = 0.68 report the
     margin-to-exposure 1/3 - alpha(r_E,eq) > 0 and the radial gap
     r_surf - r_E at the equator — how far the merger-remnant population
     sits from the exposure threshold.
"""
import numpy as np
import sympy as sp

PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


M = 1.0
r_, a_, th_ = sp.symbols("r a theta", positive=True)
Delta_s = r_**2 - 2 * r_ + a_**2
Sigma_s = r_**2 + a_**2 * sp.cos(th_) ** 2
A_s = (r_**2 + a_**2) ** 2 - Delta_s * a_**2 * sp.sin(th_) ** 2
alpha2_s = Delta_s * Sigma_s / A_s

# ---------------------------------------------------------------- check 0
alpha2_a0 = sp.simplify(alpha2_s.subs({a_: 0, th_: sp.pi / 2}))
r_sol = sp.solve(sp.Eq(alpha2_a0, sp.Rational(1, 9)), r_)
check("0. a=0 recovery: alpha=1/3 surface at areal r = 9M/4 exactly (F-R1 anchor)",
      sp.Rational(9, 4) in [sp.nsimplify(x) for x in r_sol],
      f"alpha^2(a=0) = {alpha2_a0}; roots {r_sol}")

# ---------------------------------------------------------------- check 1
rE_eq = 2  # equatorial ergosphere, M=1
alpha2_on_ergo_eq = sp.simplify(alpha2_s.subs({r_: 2, th_: sp.pi / 2}))
closed = a_**2 / (2 * (2 + a_**2))
check("1. lapse on the equatorial ergosphere: alpha^2 = a^2/(2(2M^2+a^2)) exact",
      sp.simplify(alpha2_on_ergo_eq - closed) == 0,
      f"alpha^2(r=2M, eq) = {sp.simplify(alpha2_on_ergo_eq)}")

# ---------------------------------------------------------------- check 2
a_crit_sol = sp.solve(sp.Eq(closed, sp.Rational(1, 9)), a_)
a_crit = [x for x in a_crit_sol if x.is_positive][0]
check("2. critical spin exact: a_crit = 2M/sqrt(7)  (chi_crit ~ 0.7559)",
      sp.simplify(a_crit - 2 / sp.sqrt(7)) == 0,
      f"a_crit = {a_crit} = {float(a_crit):.6f} M")


def alpha2_num(r, a, th):
    Delta = r * r - 2 * r + a * a
    Sigma = r * r + a * a * np.cos(th) ** 2
    A = (r * r + a * a) ** 2 - Delta * a * a * np.sin(th) ** 2
    return Delta * Sigma / A


def r_ergo(a, th):
    return 1 + np.sqrt(max(1 - a * a * np.cos(th) ** 2, 0.0))


def r_lapse_third(a, th):
    """Outermost root of alpha^2 = 1/9 (bisection from far field inward)."""
    lo, hi = r_ergo(a, th) * 1.0000001, 50.0
    f = lambda r: alpha2_num(r, a, th) - 1.0 / 9.0
    if f(lo) > 0:      # alpha already > 1/3 just outside the ergosphere:
        # the 1/9 surface lies INSIDE the ergosphere at this latitude
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------- check 3
ths = np.linspace(1e-3, np.pi / 2, 200)
binding_ok = True
for a in [0.3, 0.6, 0.756, 0.9, 0.998]:
    lapses = [np.sqrt(alpha2_num(r_ergo(a, t), a, t)) for t in ths]
    if np.argmax(lapses) != len(ths) - 1:  # MAXIMUM must sit at equator
        binding_ok = False
    if lapses[0] > 1e-2:                   # -> 0 at the pole (touches horizon)
        binding_ok = False
check("3. equator is the binding case: ergosphere lapse MAXIMIZED at th=pi/2, -> 0 at poles",
      binding_ok, "max over theta lands at the equator for all scanned spins; polar lapse -> 0")

# ---------------------------------------------------------------- check 4
buried_ok = True
detail4 = []
for a in [0.3, 0.5, 0.68, float(a_crit) - 1e-6]:
    worst_gap = np.inf
    for t in ths:
        rs = r_lapse_third(a, t)
        if rs is None:
            buried_ok = False
            worst_gap = -1
            break
        worst_gap = min(worst_gap, rs - r_ergo(a, t))
    detail4.append(f"chi={a:.4f}: min gap {worst_gap:+.4f} M")
check("4. burial below a_crit: alpha=1/3 surface OUTSIDE the ergosphere at ALL latitudes "
      "(incl. chi=0.68, the GW150914-class remnant)",
      buried_ok, "; ".join(detail4))

# ---------------------------------------------------------------- check 5
exposure_ok = True
detail5 = []
for a in [0.80, 0.95, 0.998]:
    exposed = [t for t in ths if r_lapse_third(a, t) is None]
    if not exposed:
        exposure_ok = False
        detail5.append(f"chi={a}: NO exposure (unexpected)")
    else:
        lat_deg = 90 - np.degrees(min(exposed))
        detail5.append(f"chi={a}: exposed band within {lat_deg:.1f} deg of the equator")
check("5. exposure above a_crit: an exterior equatorial ergoregion band opens",
      exposure_ok, "; ".join(detail5))

# ---------------------------------------------------------------- check 6
a68 = 0.68
alpha_ergo_68 = np.sqrt(alpha2_num(2.0, a68, np.pi / 2))
rs68 = r_lapse_third(a68, np.pi / 2)
margin = 1.0 / 3.0 - alpha_ergo_68        # burial margin: > 0 means buried
check("6. GW-population margin at chi=0.68: burial margin 1/3 - alpha(r_E,eq) > 0; radial gap reported",
      margin > 0 and rs68 is not None and rs68 > 2.0,
      f"alpha(r_E,eq) = {alpha_ergo_68:.4f} < 1/3 (burial margin {margin:+.4f}); "
      f"surface at r = {rs68:.4f} M vs ergosphere 2 M (gap {rs68-2:.4f} M)")

print()
print(f"{sum(PASS)}/{len(PASS)} PASS")
raise SystemExit(0 if all(PASS) else 1)
