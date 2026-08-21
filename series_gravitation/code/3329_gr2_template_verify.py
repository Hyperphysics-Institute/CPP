#!/usr/bin/env python3
"""3329_gr2_template_verify.py — GR-2 "The Echo Falsifier" V0 verify.

Computation-before-claims for every number quoted in GR-2 V0:
the retrograde-keyed echo-delay template Dt(M, chi), its Schwarzschild
limit, the GW150914 benchmark, the mass/spin error-bar quantification
(the CONV-032 binding rider), the prograde-burial onset, and the
echo-comb frequency.

FAST MODE (CONV-032 adoption, first enactment): checks tagged [FAST]
run in seconds and emit their own count line, so a time-boxed review
seat can own-run the core identities without the full scan.
    python 3329_gr2_template_verify.py --fast
Full run appends the scan-grade checks and the final count line.

Machinery inherited from code/3320_kerr_surface_derivation_verify.py
(Boyer-Lindquist, G = c = M = 1; equatorial eikonal grade).
"""
import sys
import numpy as np

FAST_ONLY = "--fast" in sys.argv

PASS, FASTPASS = [], []


def check(name, ok, detail="", fast=False):
    (FASTPASS if fast else PASS).append(bool(ok))
    tag = "[FAST]" if fast else "      "
    print(f"{tag}[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


# ---------------------------------------------------------------- geometry
def alpha_n(r, a, th=np.pi / 2):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    Aa = (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2
    return np.sqrt(max(D * S / Aa, 0.0))


def v_n(r, a, th=np.pi / 2):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    Aa = (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2
    om = 2 * a * r / Aa
    gpp = Aa * np.sin(th) ** 2 / S
    al2 = D * S / Aa
    return om * np.sqrt(gpp / al2) if al2 > 0 else np.inf


def F_n(r, a, th=np.pi / 2):
    al = alpha_n(r, a, th)
    s = 2 * (1 - al) / (1 + al)
    return s * s + v_n(r, a, th) ** 2


def r_E(a, th=np.pi / 2):
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


def r_ph(a, prograde=True):
    sgn = -1 if prograde else +1
    return 2 * (1 + np.cos(2.0 / 3.0 * np.arccos(sgn * a)))


def delay(a, r_in, r_out, n=200_000):
    rs = np.linspace(r_in, r_out, n)
    grr = rs * rs / (rs * rs - 2 * rs + a * a)
    al = np.array([alpha_n(r, a) for r in rs])
    integ = np.sqrt(np.maximum(grr, 0)) / np.maximum(al, 1e-12)
    return 2 * np.trapezoid(integ, rs)


GM_c3_per_Msun = 4.92549e-6  # seconds
M0, dM = 62.0, 4.0           # GW150914 remnant, GR-1d V3 error-bar mandate
CHI0 = 0.68


def dt_ret(a, M=M0):
    rs = r_surface(max(a, 1e-9))
    return delay(max(a, 1e-9), rs, r_ph(max(a, 1e-9), prograde=False)) * M * GM_c3_per_Msun


# ============================== FAST GROUP ==============================
# F1: Schwarzschild closed form recovered
dt_schw_num = delay(1e-9, 2.25, 3.0)
dt_schw_exact = 1.5 + 8 * np.log(2)
check("F1. Schwarzschild limit: numeric eikonal = (3/2 + 8 ln 2) GM/c^3",
      abs(dt_schw_num - dt_schw_exact) < 0.01,
      f"{dt_schw_num:.4f} vs {dt_schw_exact:.4f}", fast=True)

# F2: GW150914 benchmark — the PRED-O-39 numbers
dt68_geo = delay(CHI0, r_surface(CHI0), r_ph(CHI0, False))
dt68_ms = dt68_geo * M0 * GM_c3_per_Msun * 1e3
spin_corr = dt68_geo / dt_schw_exact - 1
check("F2. GW150914 benchmark: Dt_ret(0.68) = 8.59 GM/c^3 = 2.62 ms; +22% spin correction",
      abs(dt68_geo - 8.59) < 0.02 and abs(dt68_ms - 2.62) < 0.02
      and abs(spin_corr - 0.22) < 0.005,
      f"{dt68_geo:.3f} GM/c^3; {dt68_ms:.3f} ms; +{100*spin_corr:.2f}%", fast=True)

# F3: censorship spot-check at the benchmark spin
rsurf68, rE68 = r_surface(CHI0), r_E(CHI0)
check("F3. censorship at chi=0.68: surface strictly outside the ergosphere; prograde ring buried",
      rsurf68 > rE68 and r_ph(CHI0, True) < rsurf68,
      f"r_surf={rsurf68:.3f} M > r_E={rE68:.3f} M; r_ph_pro={r_ph(CHI0, True):.3f} M inside",
      fast=True)

# F4: mass-linearity + the +/-6.5% mass error bar
lin = dt_ret(CHI0, M0 + dM) / dt_ret(CHI0, M0)
mass_frac = dM / M0
check("F4. mass linearity: Dt proportional to M; +/-4 Msun => +/-6.5%",
      abs(lin - (1 + mass_frac)) < 1e-6 and abs(mass_frac - 0.0645) < 0.001,
      f"ratio {lin:.5f} vs {1+mass_frac:.5f}; fractional {100*mass_frac:.2f}%", fast=True)

print(f"FAST: {sum(FASTPASS)}/{len(FASTPASS)} PASS")
if FAST_ONLY:
    raise SystemExit(0 if all(FASTPASS) else 1)

# ============================== FULL GROUP ==============================
# 5: the Dt(chi) template table quoted in GR-2 Table 1
table_chis = [0.0, 0.30, 0.55, 0.68, 0.80, 0.90, 0.95]
rows = []
for chi in table_chis:
    g = delay(max(chi, 1e-9), r_surface(max(chi, 1e-9)), r_ph(max(chi, 1e-9), False))
    rows.append((chi, g, g * M0 * GM_c3_per_Msun * 1e3))
    print(f"      table: chi={chi:.2f}  Dt_ret={g:7.3f} GM/c^3  = {rows[-1][2]:.3f} ms @ 62 Msun")
mono = all(rows[i + 1][1] > rows[i][1] for i in range(len(rows) - 1))
check("5. template table computed; Dt_ret monotone increasing in chi; chi=0 row = Schwarzschild",
      mono and abs(rows[0][1] - dt_schw_exact) < 0.01,
      f"chi=0 row {rows[0][1]:.4f} vs closed form {dt_schw_exact:.4f}")

# 6: spin error bar for the binding rider — dDt/dchi at the benchmark.
# FINDING (this script's own first run): the worker's prior expectation was a
# 3-10% band; the computed slope is 0.299 GM/c^3 per unit chi, i.e. +/-0.1 in
# chi moves Dt by only ~0.3% — the template SATURATES in spin above burial
# onset (table rows: 8.538 -> 8.632 across chi = 0.55 -> 0.95). The mass
# uncertainty (+/-6.5%) therefore DOMINATES the spin uncertainty by ~20x at
# the benchmark; the strong spin lever lives BELOW onset (2.151 -> 2.607 ms
# across chi = 0 -> 0.55). Check re-pointed to the computed behavior;
# original expectation recorded here per computation-before-claims.
eps = 0.02
slope = (delay(CHI0 + eps, r_surface(CHI0 + eps), r_ph(CHI0 + eps, False))
         - delay(CHI0 - eps, r_surface(CHI0 - eps), r_ph(CHI0 - eps, False))) / (2 * eps)
dchi = 0.10
spin_bar = slope * dchi / dt68_geo
check("6. spin error bar QUANTIFIED: template saturates above onset; +/-0.1 in chi => sub-percent band",
      0.05 < slope < 1.0 and spin_bar < 0.01,
      f"dDt/dchi = {slope:.3f} GM/c^3 per unit chi; +/-0.1 => +/-{100*spin_bar:.2f}% "
      f"(mass bar +/-6.5% dominates ~20x)")

# 7: prograde-burial onset
a_pb = None
for a in np.linspace(0.01, 0.998, 300):
    rs_ = r_surface(a)
    if rs_ is not None and r_ph(a, True) <= rs_:
        a_pb = a
        break
check("7. prograde-burial onset chi ~ 0.55 (retrograde keying begins)",
      a_pb is not None and abs(a_pb - 0.55) < 0.02, f"onset chi = {a_pb:.3f}")

# 8: echo-comb frequency in the LIGO band
f_echo = 1.0 / (dt68_ms * 1e-3)
check("8. echo-comb spacing f = 1/Dt ~ 380 Hz at the benchmark — IN the LIGO band",
      abs(f_echo - 380) < 10 and 20 < f_echo < 2000, f"f_echo = {f_echo:.1f} Hz")

# 9: pro/retro discriminator margin — the buried-ring counterfactual delay
dt_pro_cf = delay(CHI0, r_surface(CHI0), r_ph(CHI0, True) if r_ph(CHI0, True) > r_surface(CHI0)
                  else r_surface(CHI0) * 1.0001)
check("9. discriminator: the prograde-ring cavity is ABSENT (ring inside the wall) — "
      "a prograde-keyed comb at this spin is a falsifier, not a fit option",
      r_ph(CHI0, True) < r_surface(CHI0) and dt_pro_cf < 0.1,
      f"prograde ring {r_ph(CHI0, True):.3f} M vs wall {r_surface(CHI0):.3f} M; "
      f"no exterior prograde cavity exists")

allpass = FASTPASS + PASS
print(f"{sum(allpass)}/{len(allpass)} PASS")
raise SystemExit(0 if all(allpass) else 1)
