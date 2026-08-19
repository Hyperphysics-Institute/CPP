#!/usr/bin/env python3
"""Patch 3228 verify script — GR-1 V0 classical-tests summary table.

Purpose. c08 (strong-field companion) claims the CPP shell-broadcast PSR
mechanism yields EXACTLY the Schwarzschild metric in isotropic coordinates.
GR-1 V0 therefore claims the four classical tests at exactly the GR values:
the tests discriminate CPP from Newtonian gravity, not from GR. This script
(1) verifies the isotropic form used in c08 is the Schwarzschild metric
    (coordinate-transformation identity, machine precision),
(2) computes the classical-test numbers that populate GR-1 Table 1, the two
    dynamical ones by numeric geodesic integration cross-checked against the
    closed form, so every number in the table traces to this script.

No free parameters; no CPP-specific inputs beyond "the metric is exactly
Schwarzschild" — which is precisely the claim being surfaced.

Numerical notes (learned on first run, kept for the record):
- phi is accumulated as i*dphi (integer step count), not phi += dphi; naive
  accumulation over ~10^7 steps injects ~1e-6 rad of rounding drift, which is
  percent-level against a per-orbit advance of 5e-7 rad.
- Zero crossings (perihelion passages, outgoing photon asymptote) are located
  by linear interpolation; taking the first post-crossing grid point overshoots
  by up to dphi, which is 10%-level against a deflection of 8.5e-6 rad.

Run: python3 3228_classical_tests_verify.py
"""

import math

# ---------------------------------------------------------------- constants
G       = 6.67430e-11        # m^3 kg^-1 s^-2 (CODATA 2018)
c       = 2.99792458e8       # m/s (exact)
M_sun   = 1.98892e30         # kg
R_sun   = 6.957e8            # m (IAU nominal solar radius)
AU      = 1.495978707e11     # m (exact)
g_earth = 9.80665            # m/s^2 (standard)

GM = G * M_sun
rs = 2 * GM / c**2           # Schwarzschild radius of the Sun

ARCSEC = math.pi / (180 * 3600)
JULIAN_CENTURY_DAYS = 36525.0

passes = []
def check(name, ok, detail=""):
    passes.append((name, ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")

# ---------------------------------------------------- 0. metric identity
print("== 0. Isotropic form (c08 Eq. isotropic_schw) IS Schwarzschild ==")
# c08: with varrho = GM/(2 c^2 r_iso),
#   g_tt = -[(1-varrho)/(1+varrho)]^2 ; standard r = r_iso (1+varrho)^2,
#   g_tt = -(1 - rs/r).
worst = 0.0
for r_iso in [1e9, 1e10, 1e11, AU, 10 * AU]:
    vr = GM / (2 * c**2 * r_iso)
    gtt_iso = -((1 - vr) / (1 + vr))**2
    r_std = r_iso * (1 + vr)**2
    gtt_std = -(1 - rs / r_std)
    worst = max(worst, abs(gtt_iso - gtt_std) / abs(gtt_std))
print(f"  max relative g_tt mismatch over 5 radii: {worst:.3e}")
check("isotropic == standard Schwarzschild g_tt (machine precision)",
      worst < 1e-14, f"max rel {worst:.1e}")

# ------------------------------------------- 1. Mercury perihelion advance
print("\n== 1. Perihelion precession of Mercury ==")
a_merc = 5.7909050e10        # m
e_merc = 0.205630
P_merc_days = 87.9691

dphi_cf = 6 * math.pi * GM / (a_merc * (1 - e_merc**2) * c**2)  # per orbit

# Independent route: relativistic Binet equation
#   u'' + u = GM/h^2 + (3GM/c^2) u^2
L = a_merc * (1 - e_merc**2)
h2 = GM * L
u = (1 + e_merc) / L         # start at perihelion (u max, u'=0)
up = 0.0
dphi = 2e-5
n_orbits = 30
n_steps = int(2 * math.pi * (n_orbits + 0.5) / dphi)

def deriv_m(u_, up_):
    return up_, GM / h2 - u_ + (3 * GM / c**2) * u_ * u_

crossings = []               # up sign change - -> + (interpolated)
last_up = up
for i in range(1, n_steps + 1):
    k1u, k1p = deriv_m(u, up)
    k2u, k2p = deriv_m(u + 0.5 * dphi * k1u, up + 0.5 * dphi * k1p)
    k3u, k3p = deriv_m(u + 0.5 * dphi * k2u, up + 0.5 * dphi * k2p)
    k4u, k4p = deriv_m(u + dphi * k3u, up + dphi * k3p)
    u  += dphi / 6 * (k1u + 2 * k2u + 2 * k3u + k4u)
    up += dphi / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
    if last_up < 0.0 and up >= 0.0:
        frac = last_up / (last_up - up)      # in [0,1]
        crossings.append((i - 1 + frac) * dphi)
    last_up = up

# Telescoping estimator: interior interpolation errors cancel.
N = len(crossings) - 1
dphi_num = (crossings[-1] - crossings[0]) / N - 2 * math.pi

orbits_per_century = JULIAN_CENTURY_DAYS / P_merc_days
adv_cf  = dphi_cf  / ARCSEC * orbits_per_century
adv_num = dphi_num / ARCSEC * orbits_per_century
print(f"  closed form : {adv_cf:.4f} arcsec/century")
print(f"  numeric     : {adv_num:.4f} arcsec/century ({N} orbit intervals)")
check("perihelion numeric vs closed form (0.1%)",
      abs(adv_num - adv_cf) <= 1e-3 * adv_cf,
      f"{adv_num:.4f} vs {adv_cf:.4f}")
check("perihelion vs observed 42.98 +/- 0.04 \"/cy",
      abs(adv_cf - 42.98) <= 0.04, f"{adv_cf:.4f}")

# ------------------------------------------------- 2. Light deflection
print("\n== 2. Light deflection at the solar limb ==")
b = R_sun
defl_cf = 4 * GM / (c**2 * b)

# Photon Binet: u'' + u = (3GM/c^2) u^2, ICs u(0)=0, u'(0)=1/b
u, up = 0.0, 1.0 / b
dphi = 1e-6
u_prev = u
i = 0
def deriv_p(u_, up_):
    return up_, -u_ + (3 * GM / c**2) * u_ * u_
while True:
    i += 1
    k1u, k1p = deriv_p(u, up)
    k2u, k2p = deriv_p(u + 0.5 * dphi * k1u, up + 0.5 * dphi * k1p)
    k3u, k3p = deriv_p(u + 0.5 * dphi * k2u, up + 0.5 * dphi * k2p)
    k4u, k4p = deriv_p(u + dphi * k3u, up + dphi * k3p)
    u_prev = u
    u  += dphi / 6 * (k1u + 2 * k2u + 2 * k3u + k4u)
    up += dphi / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
    if i > 10 and u <= 0.0:
        frac = u_prev / (u_prev - u)
        phi_end = (i - 1 + frac) * dphi
        break
defl_num = phi_end - math.pi
print(f"  closed form : {defl_cf / ARCSEC:.4f} arcsec")
print(f"  numeric     : {defl_num / ARCSEC:.4f} arcsec")
check("deflection numeric vs closed form (0.2%)",
      abs(defl_num - defl_cf) <= 2e-3 * defl_cf,
      f"{defl_num/ARCSEC:.4f} vs {defl_cf/ARCSEC:.4f}")
check("deflection vs 1.75 arcsec (0.5%)",
      abs(defl_cf / ARCSEC - 1.75) <= 0.005 * 1.75,
      f"{defl_cf/ARCSEC:.4f}")

# ------------------------------------------------- 3. Shapiro delay
print("\n== 3. Shapiro delay (Earth-Venus superior conjunction, grazing) ==")
r_venus = 1.0821e11
delay = (4 * GM / c**3) * math.log(4 * AU * r_venus / R_sun**2)
print(f"  round-trip excess delay: {delay * 1e6:.1f} microseconds")
check("Shapiro delay in the ~200 us class (leading log)",
      200e-6 <= delay <= 260e-6, f"{delay*1e6:.1f} us")

# ------------------------------------------------- 4. Gravitational redshift
print("\n== 4. Gravitational redshift ==")
h_tower = 22.5               # m, Pound-Rebka-Snider
z_pr = g_earth * h_tower / c**2
print(f"  Pound-Rebka 22.5 m tower: dnu/nu = {z_pr:.3e}")
check("Pound-Rebka dnu/nu ~ 2.46e-15", abs(z_pr - 2.46e-15) <= 0.02 * 2.46e-15,
      f"{z_pr:.3e}")
R_e = 6.371e6
GM_e = 3.986004418e14
r_gps = R_e + 2.0200e7
grav = (GM_e / c**2) * (1 / R_e - 1 / r_gps) * 86400 * 1e6    # us/day
v_gps = math.sqrt(GM_e / r_gps)
sr = -0.5 * (v_gps / c)**2 * 86400 * 1e6                       # us/day
print(f"  GPS: grav +{grav:.1f} us/day, SR {sr:.1f} us/day, net {grav+sr:.1f} us/day")
check("GPS net offset ~ 38.5 us/day (3%)",
      abs((grav + sr) - 38.5) <= 0.03 * 38.5, f"{grav+sr:.1f}")

# ---------------------------------------------------------------- verdict
print("\n== SUMMARY ==")
n_ok = sum(1 for _, ok in passes if ok)
for name, ok in passes:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"{n_ok}/{len(passes)} checks pass")
raise SystemExit(0 if n_ok == len(passes) else 1)
