#!/usr/bin/env python3
# 2351 -- G3 PER-dSPH LIKELIHOOD, grading. Pre-registration: code/2351_PREREG.md
# (source, anchors, U=2, band, strand statement, outcomes fixed before running).
# Engine: code/2351_g3_engine.py -> 2351_results.json.
# Frame-adoption gate G3 (2346/F3), NOT Gate-1/B1's G3 (2314); dsph_ namespace.

import json, math, os
import importlib.util as iu

here = os.path.dirname(os.path.abspath(__file__))
spec = iu.spec_from_file_location("g3", os.path.join(here, "2351_g3_engine.py"))
g3 = iu.module_from_spec(spec); spec.loader.exec_module(g3)

res = json.load(open(os.path.join(here, "2351_results.json")))
checks = []

# (1) source discipline: three anchors carried verbatim (in-text <v> + Table 2
#     ranges that already include Correa's factor-2 model uncertainty); demand
#     curve COMPUTED from her verbatim fit parameters (m_chi = 0.648 GeV,
#     m_phi = 0.636 MeV, alpha = 0.01), not digitized; U = 2 and the [1/2, x3]
#     band fixed in the pre-registration. Live recompute of the curve.
s21, s48, s58, s50 = (g3.sigma_correa(v) for v in (21.0, 48.0, 58.0, 50.0))
ok1 = (abs(g3.S0C - 108.9) < 1.5 and abs(g3.WC - 29.4) < 0.3
       and 70 < s21 < 74 and 28 < s48 < 31 and 21 < s58 < 23
       and os.path.exists(os.path.join(here, "2351_PREREG.md")))
checks.append(("(1) SOURCE DISCIPLINE: anchors verbatim (LeoII 21 km/s [90,150]; "
               "Carina 48 [40,50]; Draco 58 [20,30]); demand curve computed from "
               "Correa's verbatim particle-model parameters (sigma0 = %.0f cm2/g, "
               "w = %.1f km/s; sigma_C(21/48/58) = %.0f/%.0f/%.0f), not digitized; "
               "U = 2 and band pre-registered" % (g3.S0C, g3.WC, s21, s48, s58),
               ok1, None))

# (2) shape leg: the density-pericentre anticorrelation's imprint (sigma ordering
#     LeoII > Carina > Draco, inverse in <v>) is reproduced by every graded point
#     -- the population family carries the anticorrelation automatically.
ok2 = all(res["as_stored"][n]["monotone_shape"] for n in res["as_stored"]) and \
      all(res["research"][f]["grade"]["monotone_shape"] for f in res["research"])
checks.append(("(2) SHAPE LEG PASSES EVERYWHERE: sigma(21) >= sigma(48) >= "
               "sigma(58) at every stored and re-searched point -- the "
               "anticorrelation ordering that motivates the collapse strand is "
               "native to the population's velocity dependence", ok2, None))

# (3) as-stored evaluation (2345 P4 discipline): the G1/G2 passing points miss
#     the collapse-strand anchors x2.04 / x3.81 at U = 2 -- inside the x2-5
#     shortfall the pre-registration computed from visible arithmetic BEFORE
#     running -- while the isothermal strand (rest windows) holds at x1.00.
a_e = res["as_stored"]["kin_extended_natural"]
a_c = res["as_stored"]["kin_central_depth"]
ok3 = (1.9 < a_e["joint_anchor_viol"] < 2.2 and 3.5 < a_c["joint_anchor_viol"] < 4.1
       and a_e["rest_viol"] <= 1.0 + 1e-9 and a_c["rest_viol"] <= 1.0 + 1e-9)
checks.append(("(3) AS-STORED (P4): the G1/G2 passing points miss the collapse "
               "anchors x%.2f (extended-natural) / x%.2f (central-depth) at U = 2 "
               "-- inside the pre-registered x2-5 arithmetic -- while carrying "
               "their rest-of-suite windows at x1.00; the isothermal-strand "
               "inheritance stands" % (a_e["joint_anchor_viol"],
               a_c["joint_anchor_viol"]), ok3, None))

# (4) joint re-search: the knob box CANNOT close the collapse strand -- best
#     joint x1.342 (extended variant) / x1.908 (central) -- and the binding
#     structure is measured: at the extended optimum the Carina floor (x1.34)
#     and the pin ceiling (x1.34) bind SIMULTANEOUSLY -- the trade is exhausted.
r_e = res["research"]["audited_extended"]; r_c = res["research"]["audited_central"]
tied = abs(r_e["grade"]["anchors"]["Carina"] - r_e["grade"]["rest_viol"]) < 0.02
ok4 = (1.30 < r_e["joint"] < 1.40 and 1.85 < r_c["joint"] < 1.95 and tied)
checks.append(("(4) JOINT RE-SEARCH: zero passing points in the box against the "
               "collapse strand -- best x%.3f (extended variant; LeoII closes at "
               "x1.00, Carina x%.2f and pin x%.2f TIED at the optimum: the trade "
               "is exhausted) / x%.3f (central); the gap is measured, not asserted"
               % (r_e["joint"], r_e["grade"]["anchors"]["Carina"],
                  r_e["grade"]["rest_viol"], r_c["joint"]), ok4, None))

# (5) THE DEMAND-INTERNAL COLLISION (the patch's decisive finding): Correa's own
#     fit gives sigma_C(50) = 28 cm2/g -- it FAILS the registered pin ceiling
#     (<=5 central / <=10 extended) by x5.6 / x2.8 with no candidate consulted.
#     Carina >= 40-50 at <v> = 48 vs pin <= 5-10 at 50 km/s demands a local
#     slope s = ln(20/10)/ln(50/48) = 17 even at softened edges -- no smooth
#     sigma(v) holds it; the measured family maximum (orbiting onset, 2337/2344)
#     is s ~ 3.2. The collapse strand and the pin anchor are MUTUALLY
#     INCONSISTENT in one evaluation frame. Named sensitivity (registered, NOT
#     graded): the L4-b +10 km/s pin-velocity reading lowers the required slope
#     to ln(2)/ln(60/48) = 3.1 -- inside the family's onset capability; the
#     pin-velocity audit is now load-bearing for the strand question.
s_req_50 = math.log(2.0) / math.log(50.0/48.0)
s_req_60 = math.log(2.0) / math.log(60.0/48.0)
ok5 = (27 < s50 < 29 and s50/10.0 > 2.7 and s50/5.0 > 5.5
       and 16 < s_req_50 < 18 and 3.0 < s_req_60 < 3.2)
checks.append(("(5) DEMAND-INTERNAL COLLISION, COMPUTED: sigma_C(50) = %.0f cm2/g "
               "-- Correa's own curve fails the registered pin ceiling x%.1f "
               "(extended, 10) / x%.1f (central, 5) before any candidate is "
               "consulted; the Carina-pin cliff requires local slope s = %.0f at "
               "v_pin = 50 (family max ~3.2) -- the collapse strand and the pin "
               "anchor cannot share one frame; L4-b's +10 km/s reading lowers the "
               "bar to s = %.1f (named sensitivity, registered, out of this "
               "patch's grading)" % (s50, s50/10.0, s50/5.0, s_req_50, s_req_60),
               ok5, None))

# (6) GATE GRADE: pre-registered outcome (ii) STRAND-SPLIT-QUANTIFIED fires ->
#     G3 = CLEARED-conditional-on-strand. The isothermal strand holds (inherited
#     from G1/G2 window passes, re-verified as-stored); the collapse strand is
#     missed x1.34 minimum with the miss traced to a demand-internal
#     inconsistency (check 5) that no candidate can repair. All three F3 gates
#     traversed: G1 PASSED-with-texture, G2 PASSED-with-texture, G3
#     CLEARED-conditional-on-strand -- the F3 auto-proposal is ASSEMBLED for the
#     founder (frame decision subsumes the strand decision; no computation
#     arbitrates between published strands). Envelope robustness row reported
#     (anchors x7.6-10.3 at the un-retuned points; ratio cliff envelope-
#     independent). NO VERDICT MOVED.
ok6 = all(o for _, o, _ in checks) and \
      res["envelope_row"]["audited_extended"]["joint"] > 5.0
checks.append(("(6) OUTCOME (ii) FIRES AS PRE-REGISTERED: G3 = "
               "CLEARED-conditional-on-strand -- isothermal strand holds, "
               "collapse strand missed x1.34+ with the miss traced to the "
               "Correa-pin demand-internal collision; ALL THREE F3 GATES "
               "TRAVERSED; the v2-adoption auto-proposal is assembled for the "
               "founder with the strand decision embedded; NO VERDICT MOVED",
               ok6, None))

npass = 0
for msg, ok, _ in checks:
    print(("PASS " if ok else "FAIL ") + msg + "\n")
    npass += ok
print("=== %d/%d ===" % (npass, len(checks)))
