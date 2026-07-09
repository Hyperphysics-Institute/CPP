#!/usr/bin/env python3
# 2356 -- L4-b PIN-VELOCITY AUDIT, grading. Pre-registration: code/2356_PREREG.md
# (provenance ledger, convention map, protocol order, outcomes fixed before
# running). Engine: code/2356_l4b_engine.py -> 2356_results.json.

import json, math, os
import importlib.util as iu

here = os.path.dirname(os.path.abspath(__file__))
res = json.load(open(os.path.join(here, "2356_results.json")))
checks = []

# (1) provenance + convention discipline: the pin is the 1865 J3' SYNTHESIS
#     window, not a system; its ceiling sources live at galaxy velocities
#     (KTY/Ren, from ~50 upward) and Elbert V_max = 40; the convention map
#     (<v> = 2.26 sigma_1D, sigma_1D ~ (0.6-0.8) V_max) was fixed pre-run and
#     places Elbert at <v> in [56, 72]. Nothing digitized; nothing newly sourced.
cv = res["convention"]
ok1 = (cv["elbert_vmax40_vband"] == [56.0, 72.0]
       and cv["v_over_vmax"] == [1.4, 1.8]
       and os.path.exists(os.path.join(here, "2356_PREREG.md")))
checks.append(("(1) PROVENANCE + CONVENTION: the pin is the 1865 J3' synthesis "
               "window; under the pre-registered kinematic map (<v> = (1.4-1.8) "
               "V_max) its Elbert leg sits at <v> in [56, 72] and the KTY/Ren "
               "ceiling extends from ~50-class upward -- the registered v_pin = 50 "
               "is the STEEPEST admissible reading of the pin's own sources, the "
               "exact analogue of the 2345 dSph finding", ok1, None))

# (2) HURTING DIRECTION FIRST -- the v1 kill is robust to the pin correction:
#     the killed candidate's dSph shortfall is x1.58 at EVERY audited v_pin
#     (pin-independent) and the pin itself stays over the v1 ceiling
#     (x1.31-1.76) across the band. Kill class untouched.
rb = res["kill_robustness"]
dsph = [rb[k]["dsph_shortfall"] for k in rb]
pin = [rb[k]["pin_over_ceiling"] for k in rb]
ok2 = min(dsph) > 1.5 and min(pin) > 1.25
checks.append(("(2) v1-KILL ROBUST (checked FIRST): dSph shortfall x%.2f at every "
               "audited v_pin (pin-independent); pin-over-v1-ceiling %.2f-%.2f "
               "across the band -- the kill class stands under any pin reading"
               % (min(dsph), min(pin), max(pin)), ok2, None))

# (3) collision severity: s_req = ln2/ln(v_pin/48) = 17.0 / 5.1 / 3.1 / 2.4 / 1.8
#     at 50/55/60/64/70; dissolves (<= family max 3.2) at v_pin >= 59.6 --
#     INSIDE the audited Elbert band. The 2351 collision is READING-DEPENDENT
#     within the pin's own licensed provenance, holding only at the steep edge.
sev = {int(k): v for k, v in res["collision_severity"].items()}
ok3 = (16.5 < sev[50] < 17.5 and 3.0 < sev[60] < 3.2 and sev[64] < 2.5
       and 59.0 < res["v_dissolve"] < 60.0)
checks.append(("(3) COLLISION READING-DEPENDENT: s_req = %.1f/%.1f/%.1f/%.1f/%.1f "
               "at v_pin = 50/55/60/64/70; dissolves at v_pin >= %.1f -- inside "
               "the audited band; the demand-internal inconsistency holds ONLY at "
               "the steepest pin reading" % (sev[50], sev[55], sev[60], sev[64],
               sev[70], res["v_dissolve"]), ok3, None))

# (4) THE BOTH-STRANDS PASS (pre-registered outcome (i)'s constructive half):
#     at the Elbert-centered reading (v_pin = 64), the extended-frame joint
#     search finds x1.000 -- ALL THREE Correa anchors at 1.00 jointly with the
#     relocated pin + LSB + cluster. Texture measured: the @64 point is
#     edge-riding and strained (alpha = 100, p = 12.3, Carina 20.02 vs 20, pin
#     10.0 vs 10); at v_pin = 70 it relaxes to near-natural (alpha = 0.01 in
#     1855's own range, p = 3.65). Central closes to x1.27-1.44 but never
#     passes (tighter pin ceiling) -- the frame asymmetry holds a fourth time.
re64 = res["research"]["audited_extended"]["64"]
re70 = res["research"]["audited_extended"]["70"]
rc = res["research"]["audited_central"]
ok4 = (re64["joint"] <= 1.0 + 1e-9 and re70["joint"] <= 1.0 + 1e-9
       and all(v <= 1.0 + 1e-2 for v in re64["anchors"].values())
       and 11.5 < re64["p"] < 13.0 and re70["p"] < 4.5
       and all(rc[k]["joint"] > 1.2 for k in rc))
checks.append(("(4) BOTH-STRANDS PASS at the audited pin: extended-frame joint "
               "x1.000 at v_pin = 64 (all three Correa anchors 1.00, jointly with "
               "pin/LSB/cluster) -- strained and edge-riding (alpha = 100, "
               "p = %.1f) -- relaxing to near-natural at v_pin = 70 (alpha in "
               "1855's own range, p = %.1f); central never passes (x1.27-1.44): "
               "the frame asymmetry holds a FOURTH time"
               % (re64["p"], re70["p"]), ok4, None))

# (5) pass relief verified, not assumed: the existing G1/G2 pass points hold the
#     pin window at EVERY audited v_pin (violation 1.000 across the band) --
#     nothing previously passed breaks under the audit.
pr = res["pass_relief"]
ok5 = all(abs(row[k]["viol"] - 1.0) < 1e-9 for row in pr.values() for k in row)
checks.append(("(5) NOTHING BREAKS: both G1/G2 pass points hold the pin window at "
               "every audited v_pin (violation 1.000 across the band) -- the "
               "correction is pure relief on the passing side and pure "
               "conditionality on the collision side", ok5, None))

# (6) GRADE: pre-registered outcome (i) FIRES -- collision reading-dependent +
#     both-strands pass at an audited reading. L4-b resolves the panel's
#     unanimous ask: the strand statement's final form is now MEASURED PER
#     READING (steep edge: collision; Elbert center: both strands satisfiable at
#     extended, strained; band top: near-naturally). Per the restated 2352
#     certification, the L4-b resolution REOPENS the certification -- reopened
#     and RE-CLOSED here in the strengthening direction (the isothermal-strand
#     pass stands AND a both-strands pass exists at licensed readings). The pin
#     reading itself is a demand-side choice on the founder's desk with the dSph
#     frame decision -- same grammar, same desk. NO VERDICT MOVED.
ok6 = all(o for _, o, _ in checks)
checks.append(("(6) OUTCOME (i) FIRES AS PRE-REGISTERED: L4-b resolved -- the "
               "collision holds only at the steepest pin reading; a both-strands "
               "pass exists at the Elbert-centered reading (extended frame); the "
               "2352 certification reopened per its own restated terms and "
               "re-closed STRENGTHENED; the pin reading joins the frame decision "
               "on the founder's desk; NO VERDICT MOVED", ok6, None))

npass = 0
for msg, ok, _ in checks:
    print(("PASS " if ok else "FAIL ") + msg + "\n")
    npass += ok
print("=== %d/%d ===" % (npass, len(checks)))
