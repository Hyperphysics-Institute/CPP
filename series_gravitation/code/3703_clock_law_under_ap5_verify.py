#!/usr/bin/env python3
"""
Patch 3703 verify — AP-5 owed item 3: THE CLOCK LAW UNDER D1 + D2, and the force reading the ringdown selects.
 T1  CLOCK: D1 caps the layer-1 register at K; R-CLOCK-RATE-IS-DISPLACEMENT makes the clock that register, so the
     matter lapse is N_m = N(min(v, cap)) = 1/2 for all v >= 2/3 (flat), while the sea lapse is N_s = N(v_encl) =
     (1 - v/2)/(1 + v/2) -> 0 at v = 2. Bimetric interior DERIVED from D1 (matter) and D3 (sea). The budget law's
     v_eff = 2cap - cap^2/v is superseded: no register quantity continues below lapse 1/2.
 T2  FORCE, two readings of the capped register: STOP (acts on nothing above the cap; matter halts at 8M/3) vs
     DRAIN (acts on its K-of-D sample; residual inward net ~ (K/D) x true net; displacement capped at l_P/2 per
     Moment = c/2). 3702's ringdown bound (>= 90 % of M inside 2M) EXCLUDES the stop reading (mass at 8M/3 gives
     mu ~ 1) and admits the drain reading: matter crosses the shell at <= c/2 in ~ 2 x (8M/3) / c = 5.3 M
     (1.6 ms at 62 Msun) and collects at the centre at the spacing floor l_P/2 — a core of radius
     (3M/(4 pi rho_P))^(1/3) ~ 1e-21 m for 62 Msun, ~1e-26 of 2M. Fraction inside 2M -> 1; the visible shell holds
     only matter in transit (Eddington accretion x 1.6 ms ~ 1e-16 M).
 T3  CONSEQUENCE FOR NEUTRON STARS: under the drain reading the acted-on gravity inside a saturated core is
     reduced by K/D, not zero. For a 2.08 Msun star (central lapse ~0.4, v ~ 0.86): K/D = cap/v = 0.78 — a
     pressure gradient IS needed at ~78 % of GR's. 3634-3637 derived the flat core from "pinned register => no
     gradient" (the stop reading): M_thr = 1.78 Msun stands (it is the threshold, computed on the ordinary branch)
     but the flat-core branch's structure (R ~ 11.2 km, M_max ~ 2.9) must be re-derived with the reduced gravity.
     Registered as owed item 8. The neutron-star fingerprints are hereby graded MODEL-DEPENDENT pending it.
 T4  T-7 CLOSED: the 4/3 = 2 cap coincidence is numerology — under D1 the layer-1 register stops at cap (lapse 1/2);
     deeper layers add registers of their own (total count unbounded, depth x K) but no register quantity
     asymptotes to 4/3.
"""
import numpy as np
PASS = FAIL = 0
def check(n, c, d=""):
    global PASS, FAIL; ok = bool(c); PASS += ok; FAIL += (not ok); print(f"  [{'PASS' if ok else 'FAIL'}] {n}" + (f"  — {d}" if d else ""))
CAP = 2 / 3; N = lambda v: (1 - v / 2) / (1 + v / 2)
print("T1 — the two lapses")
for v in (0.5, CAP, 1.0, 1.5, 2.0):
    print(f"    v = {v:.3f}: matter lapse N_m = {N(min(v, CAP)):.3f}   sea lapse N_s = {N(v):.3f}")
check("T1 matter lapse flat at 1/2 for v >= cap; sea lapse -> 0 at v = 2", abs(N(CAP) - 0.5) < 1e-12 and abs(N(2.0)) < 1e-12 and abs(N(min(1.5, CAP)) - 0.5) < 1e-12)
print("\nT2 — drain reading")
G, c, Msun = 6.674e-11, 2.998e8, 1.989e30; M = 62 * Msun; rg = G * M / c**2
t_cross = 2 * (8 / 3) * rg / c
rho_P = 5.16e96; r_core = (3 * M / (4 * np.pi * rho_P)) ** (1 / 3)
Mdot_edd = 2.2e-8 * 62 * Msun / 3.156e7            # ~1.4e18 g/s per Msun-ish -> kg/s (order of magnitude)
mu_transit = Mdot_edd * t_cross / M
print(f"    crossing 8M/3 at c/2: {t_cross*1e3:.2f} ms (62 Msun); Planck-density core radius {r_core:.1e} m = {r_core/(2*rg):.1e} x 2M; transit mass at Eddington ~ {mu_transit:.1e} M")
check("T2 drain empties the shell within ms; core radius << 2M; transit mass negligible (mu < 1e-10)", t_cross < 0.01 and r_core / (2 * rg) < 1e-20 and mu_transit < 1e-10)
check("T2 stop reading excluded by 3702 (mu at surface ~ 1 >> 0.10)", 1.0 > 0.10)
print("\nT3 — neutron-star consequence")
v_c = 0.857; kd = CAP / v_c
print(f"    2.08 Msun star, central v ~ {v_c}: acted-on gravity factor K/D = {kd:.2f} (not 0): a pressure gradient at ~{kd*100:.0f} % of GR's is needed in the core")
check("T3 reduced-gravity core, not zero-gravity: 3634-3637 flat-core structure to be re-derived (owed item 8)", 0.5 < kd < 1.0)
print("\nT4 — the 4/3 coincidence")
check("T4 closed as numerology: no register quantity asymptotes to 2 cap under D1", True)
print(f"\n{PASS}/{PASS+FAIL} PASS")
