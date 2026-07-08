#!/usr/bin/env python3
# 2335 -- ELASTIC-CHANNEL REGISTRY CHECK (founder-approved sequence, item 2):
# the one route to the anchor suite that does not touch TAMB-1(b).
#
# QUESTION: with capture killed (2333), can the ELASTIC channel alone --
# specifically the never-evaluated attractive-residual elastic transport
# (focused-but-not-captured deflection through the screened E_qq residual) --
# realize the anchor suite?
#
# FINDINGS: (A) GAP CONFIRMED -- the 1870-71 floor MC potential is
# repulsive-coat-only; the attractive channel's elastic transport is genuinely
# unevaluated (the founder's "something else we haven't looked at" was real).
# (B) CLOSED IN-PRIOR by ratio arithmetic on the anchor windows: the suite
# admits NO monotone single-wing sigma(v) -- the dSph/pin bar demands local
# log-slope s >= 2.71 while the pin/LSB bar demands s <= 1.42 over adjacent
# decades; the attractive-elastic channel's maximal wings are s = 2 (classical
# focusing = quantum unitarity) and s = 4 (resonant Sommerfeld), and BOTH fail
# (s=2 fails both bars; s=4 fails LSB x36). Same spectral bar as 2324, now
# evaluated in-prior for the elastic side. The route fails on SHAPE, with
# magnitude available -- so no OPEN-SS-43 resolution can rescue it.
# NO VERDICT MOVED. One refinement + one disclosure registered.

import math, re, os

HBARC = 197.327          # MeV fm
M_EL  = 1408.0           # MeV per Cross-Rod element
N_LO, N_HI = 5, 60       # registered rod band
E_C   = 0.3              # MeV, capture-energy scale at R_s (DM-1 v1.1 notice)
RS_SCR_LO, RS_SCR_HI = 15.0, 30.0   # fm, screening length band (OPEN-SS-43)
C_KMS = 2.998e5

# anchor windows (DM-1 sec xsec item iv; 2324)
PIN   = (1.0, 5.0)       # sigma_T/m at 50 km/s
LSB   = (0.7, 2.5)       # at 200 km/s
DSPH  = (20.0, 100.0)    # heterogeneous, 10-40 km/s; evaluate at 30
V_DSPH, V_PIN, V_LSB = 30.0, 50.0, 200.0
# measured elastic floor (1870-71 MC, repulsive coat): velocity-DEPENDENT
FLOOR = {50: (0.09, 0.15), 200: (0.06, 0.06), 1150: (0.037, 0.05),
         1500: (0.027, 0.044), 3500: (0.02, 0.02)}

checks = []

# (1) REGISTRY FINDING -- programmatic: scan the 1870 MC source for the
#     potential. Assert the repulsive coat form is present and NO attractive
#     term (no negative-well, no E_qq/capture potential) exists in the force
#     law. The elastic transport of the attractive screened residual is
#     therefore UNEVALUATED in the floor measurement.
src_path = os.path.join(os.path.dirname(__file__), "1870_soft_rod_mc.py")
src = open(src_path).read()
has_repulsive = ("E_EE * np.exp(-rs) / rs" in src) and ("repulsive" in src)
has_attractive = bool(re.search(r"E_?QQ|attract|-\s*E_EE\s*\*\s*np\.exp", src, re.I))
ok1 = has_repulsive and not has_attractive
checks.append(("(1) registry finding CONFIRMED: 1870 MC force law is the repulsive "
               "coat potential E_ee e^(-r)/r ONLY -- no attractive screened-residual "
               "term anywhere in the source; the focused-deflection elastic channel "
               "was never in the measured floor. Genuine gap, now registered", ok1, None))

# (2) THE MEASURED FLOOR IS ALREADY VELOCITY-DEPENDENT (mild): 0.09-0.15 (50)
#     -> 0.02 (3500), local slope s ~ 0.35-0.5 -- NOT the flat 0.046 the 2324
#     KILL branch used (0.046 is the ~1150-1500 km/s value). REFINEMENT to the
#     KILL-branch dwarf numbers (verdict class unchanged): with the measured
#     dwarf-velocity floor, dSph fails x130-1100 (was x435-2174), pin fails
#     x6.7-11 (was x22), LSB fails x11.7 (was x15).
s_floor = math.log(0.12/0.02)/math.log(3500/50)
pin_fail  = (PIN[0]/FLOOR[50][1],  PIN[1]/FLOOR[50][0])
lsb_fail  = LSB[0]/FLOOR[200][0]
dsph_fail = (DSPH[0]/0.15, DSPH[1]/0.09)   # floor at 30 km/s ~ 50 km/s value band
ok2 = 0.2 < s_floor < 0.7 and pin_fail[0] > 5 and lsb_fail > 10 and dsph_fail[0] > 100
checks.append(("(2) measured floor is mildly velocity-dependent (s ~ %.2f), not flat "
               "0.046 -- KILL-branch numbers REFINED (class unchanged): pin fails "
               "x%.1f-%.0f, LSB x%.1f, dSph x%.0f-%.0f" %
               (s_floor, pin_fail[0], pin_fail[1], lsb_fail,
                dsph_fail[0], dsph_fail[1]), ok2, None))

# (3) THE TWO RATIO BARS (window arithmetic, no model): any sigma(v) holding
#     the suite must satisfy r1 = sigma(30)/sigma(50) >= dSph_lo/pin_hi = 4.0
#     AND r2 = sigma(50)/sigma(200) <= pin_hi/LSB_lo = 7.14. A power law v^-s:
#     r1 bar => s >= ln4/ln(5/3) = 2.71; r2 bar => s <= ln7.14/ln4 = 1.42.
#     CONTRADICTION: no power law exists; and a mixture of components each of
#     slope <= s_max cannot exceed r1 = (5/3)^s_max -- the steepest component
#     bounds the mixture. (Independent reproduction of 2324's no-stable-
#     resting-point result, on the elastic side.)
r1_req = DSPH[0]/PIN[1]
r2_max = PIN[1]/LSB[0]
s_min = math.log(r1_req)/math.log(V_PIN/V_DSPH)
s_max = math.log(r2_max)/math.log(V_LSB/V_PIN)
ok3 = s_min > s_max and abs(s_min - 2.71) < 0.02 and abs(s_max - 1.42) < 0.01
checks.append(("(3) ratio bars: dSph/pin demands s >= %.2f between 30-50 km/s; "
               "pin/LSB demands s <= %.2f between 50-200 km/s -- contradiction; "
               "NO monotone single-wing shape holds the suite (mixtures bounded "
               "by their steepest component)" % (s_min, s_max), ok3, None))

# (4) THE ELASTIC CHANNEL'S MAXIMAL WINGS, against the bars:
#     - classical focusing sigma = pi b_max^2 = pi R^2 (1 + v_esc^2/v^2):
#       deep-wing slope s = 2 EXACTLY (energy conservation); quantum s-wave
#       unitarity 4pi/k^2 has the same s = 2. Fails r1 (2.78 < 4, x1.44 short)
#       AND r2 (16 > 7.14, x2.24 over).
#     - resonant Sommerfeld ceiling s = 4: passes r1 (7.72) but fails r2
#       (256 > 7.14, x36 over) -- LSB parks on the floor, the 2324 pattern.
#     Quantum regime confirmed at dwarf velocities: lambda_dB(mu, 50 km/s) =
#     336 fm (N=5) to 28 fm (N=60) vs R_scr 15-30 fm -- so the unitarity/
#     Sommerfeld framing is the RIGHT maximal case, and it still fails.
r1_s2, r2_s2 = (V_PIN/V_DSPH)**2, (V_LSB/V_PIN)**2
r1_s4, r2_s4 = (V_PIN/V_DSPH)**4, (V_LSB/V_PIN)**4
mu_lo, mu_hi = N_LO*M_EL/2.0, N_HI*M_EL/2.0
lam_lo = HBARC/(mu_lo*(50.0/C_KMS))
lam_hi = HBARC/(mu_hi*(50.0/C_KMS))
ok4 = r1_s2 < r1_req and r2_s2 > r2_max and r1_s4 > r1_req and r2_s4 > r2_max \
      and lam_lo > RS_SCR_HI
checks.append(("(4) maximal wings excluded: s=2 (focusing/unitarity) fails BOTH bars "
               "(r1 = %.2f < 4 x1.44 short; r2 = %.0f > 7.14 x2.2 over); s=4 "
               "(resonant Sommerfeld) fails LSB x%.0f. lambda_dB(50 km/s) = %.0f-%.0f "
               "fm vs R_scr 15-30 fm: quantum framing is the correct ceiling and "
               "still fails" % (r1_s2, r2_s2, r2_s4/r2_max, lam_hi, lam_lo), ok4, None))

# (5) SHAPE, NOT MAGNITUDE: v_esc(R_scr) = sqrt(2 E_c/mu) = 1130-3910 km/s --
#     all suite velocities sit in the deep wing, and the wing MAGNITUDE reaches
#     the windows (sigma/m at pin ~ O(10) cm^2/g at N=5). So the route fails on
#     shape alone: no resolution of OPEN-SS-43 (R_s(N)) can rescue a channel
#     whose maximal log-slope is below the dSph bar and above the LSB bar --
#     R_s moves magnitude, not slope.
vesc_lo = math.sqrt(2*E_C/mu_hi)*C_KMS
vesc_hi = math.sqrt(2*E_C/mu_lo)*C_KMS
sig_pin = math.pi*(2*RS_SCR_HI)**2*(vesc_hi/50.0)**2      # fm^2, N=5, maximal
sig_per_m = sig_pin*1e-26/(N_LO*M_EL*1.783e-27)            # cm^2/g
ok5 = vesc_lo > V_LSB and sig_per_m > PIN[0]
checks.append(("(5) shape-only failure: v_esc(R_scr) = %.0f-%.0f km/s puts the whole "
               "suite in one wing, and the wing reaches sigma/m ~ %.0f cm^2/g at the "
               "pin -- magnitude is AVAILABLE; the kill is the slope, which no "
               "OPEN-SS-43 outcome moves" % (vesc_lo, vesc_hi, sig_per_m), ok5, None))

# (6) VERDICT: elastic route CLOSED-in-prior (ratio arithmetic on registered
#     windows; the same spectral bar that excluded the 2324 flat branch).
#     Registered: (i) DM-1 errata-level disclosure -- the measured floor is
#     repulsive-coat-only, attractive-elastic channel unevaluated (moot for
#     the suite by this patch, but the floor's own small numbers could shift
#     upward if ever needed); (ii) KILL-branch refinement per check 2.
#     Honest caveat: this closure is in-prior window arithmetic on the maximal
#     wing -- the MC-with-attraction remains a bounded one-session measurement
#     if the founder prefers a measured exclusion to an arithmetic one.
#     NO VERDICT MOVED: G4 = KILL-on-suite-conditional stands (2333/2334).
ok6 = all(o for _, o, _ in checks)
checks.append(("(6) verdict: the one gate-independent route to the suite is CLOSED-"
               "in-prior on two ratio bars; gap registered as DM-1 disclosure; "
               "KILL-branch numbers refined; no verdict moved", ok6, None))

npass = 0
for msg, ok, _ in checks:
    print(("PASS " if ok else "FAIL ") + msg + "\n")
    npass += ok
print("=== %d/%d ===" % (npass, len(checks)))
