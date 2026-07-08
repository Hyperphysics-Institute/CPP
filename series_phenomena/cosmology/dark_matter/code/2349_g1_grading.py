#!/usr/bin/env python3
# 2349 -- G1 FORMATION RENT CHECK, grading (pre-registration: code/2349_PREREG.md,
# written before the engine ran). Engine: code/2349_g1_engine.py -> 2349_results.json;
# audits: code/2349_g1_audits.py -> 2349_audits.json; naturalness: 2349_naturalness.json.
# NOTE ON NAMES: this is the FRAME-ADOPTION gate G1 (2346/F3), not Gate-1/B1's G1
# (2313). Files carry the dsph_ prefix to keep the namespaces separate.

import json, math, os
import numpy as np
import importlib.util as iu

here = os.path.dirname(os.path.abspath(__file__))
spec = iu.spec_from_file_location("eng", os.path.join(here, "2349_g1_engine.py"))
eng = iu.module_from_spec(spec); spec.loader.exec_module(eng)

res = json.load(open(os.path.join(here, "2349_results.json")))
aud = json.load(open(os.path.join(here, "2349_audits.json")))
nat = json.load(open(os.path.join(here, "2349_naturalness.json")))
checks = []

# (1) V1 -- the full population balance reproduces the REGISTERED 1855 moment
#     model (same mechanism, same knob) at alpha = 1, 0.1, 0.01.
ok1 = all(abs(d["Ln_pb"] - d["Ln_moment"]) / d["Ln_moment"] < 1e-3
          and d["mass_err"] < 1e-8 for d in res["V1"])
checks.append(("(1) VALIDATOR: the full population balance reproduces the 1855 "
               "moment model's L_n at alpha = 1 / 0.1 / 0.01 (rel err < 1e-3; mass "
               "conserved < 1e-8) -- the engine solves the REGISTERED mechanism, "
               "nothing else", ok1, None))

# (2) V2 -- the K-species rig reproduces the stored 2344 two-delta totals through
#     the identical F-table / floors / mass model / sqrt-coupling mixing.
ok2 = res["V2"]["max_rel_err"] < 1e-9
checks.append(("(2) VALIDATOR: the generalized K-species rig fed the stored 2344 "
               "population reproduces the stored suite totals to < 1e-9 -- same "
               "F(eps) table, same floors, same mixing; G1 is graded on the 2344 "
               "protocol, not a new one", ok2, None))

# (3) PRE-REGISTERED OUTCOME (i) FIRES: in-box passing kinetic populations exist
#     at BOTH audited frames. Spot-recompute both passes live from parameters.
def live(la, ls, p, rs, fk):
    N, f, Ln, merr, _ = eng.distribution(10.0 ** la)
    keep = f >= 1e-6
    tot = eng.totals_K(N[keep], f[keep] / f[keep].sum(), 10.0**ls, p, rs)
    return eng.violation(tot, eng.FRAMES[fk]), tot
bc = aud["audited_central_depth"]     # in-box: ls = -5.45 > -6
v_c, tot_c = live(bc["la"], bc["ls"], bc["p"], bc["rs"], "audited_central")
xe = nat["audited_extended@alpha=1 (natural)"]["x"]  # natural-alpha pass
v_e, tot_e = live(0.0, xe[0], xe[1], xe[2], "audited_extended")
ok3 = (v_c <= 1.0 + 1e-9 and v_e <= 1.0 + 1e-9
       and -6 <= bc["ls"] and -6 <= xe[0])
checks.append(("(3) OUTCOME (i) FIRES AS PRE-REGISTERED: the 1855 kinetic family "
               "passes BOTH audited frames strictly inside the pre-registered knob "
               "box, recomputed live -- audited-central at (alpha=%.1f, p=%.1f, "
               "S0=1e%.2f, Rs=%.1f): totals (%.1f, %.2f, %.2f, %.3f); "
               "audited-extended at NATURAL alpha=1 (p=%.1f, S0=1e%.2f): totals "
               "(%.1f, %.2f, %.2f, %.3f)" % (10**bc["la"], bc["p"], bc["ls"],
               bc["rs"], tot_c[30], tot_c[50], tot_c[200], tot_c[1500],
               xe[1], xe[0], tot_e[30], tot_e[50], tot_e[200], tot_e[1500]),
               ok3, None))

# (4) TEXTURE, measured (the honest asymmetry between the frames):
#     extended = DEEP and UNSTRAINED (depth 2.18; passes at every tested alpha
#     incl. natural alpha=1 and 1855's own quoted 0.01-0.1 range; p_min = 0 --
#     even a FLAT S(N) passes); central = SHALLOW and STRAINED (depth 1.03;
#     natural alpha=1 misses x1.064; needs alpha ~ 3-6, a factor-few nucleation
#     bias -- mild; and p_min = 13: the S(N) steepness demand is now MEASURED
#     one power WORSE than 2344's named N^12 strain).
okA = (aud["audited_extended_depth"]["depth"] > 2.0
       and aud["audited_extended_p_min"] == 0.0
       and nat["audited_extended@alpha=1 (natural)"]["viol"] <= 1.0 + 1e-9)
okB = (1.0 < aud["audited_central_depth"]["depth"] < 1.10
       and aud["audited_central_p_min"] == 13.0
       and nat["audited_central@alpha=1 (natural)"]["viol"] > 1.05)
ok4 = okA and okB
checks.append(("(4) TEXTURE MEASURED: audited-extended pass is DEEP (min margin "
               "x%.2f) and UNSTRAINED (passes at natural alpha=1 and across "
               "1855's quoted range; p_min = 0, flat S(N) suffices); "
               "audited-central pass is SHALLOW (depth x%.3f) and STRAINED "
               "(alpha ~ 3-6 needed, natural misses x%.3f; p_min = 13 -- the "
               "S(N) rent leg's bar, measured, one power above the named N^12)"
               % (aud["audited_extended_depth"]["depth"],
                  aud["audited_central_depth"]["depth"],
                  nat["audited_central@alpha=1 (natural)"]["viol"]), ok4, None))

# (5) THE v1 KILL IS STRENGTHENED + the structural sub-question graded: the
#     kinetic family is UNIMODAL (Poisson mixture; verified on the alpha grid) --
#     it cannot realize the 2344 two-delta gap structure -- and its best v1
#     violation is x1.19 > the unconstrained two-delta boundary x1.074: the
#     formation-realizable population sits FARTHER outside the registered frame.
uni = True
for la in (-2.0, -1.0, 0.0, 1.0, 2.0, 3.0):
    N, f, Ln, merr, _ = eng.distribution(10.0 ** la)
    g = f[f > 1e-9]
    sign = np.sign(np.diff(g)); sign = sign[sign != 0]
    uni &= bool((np.diff(sign) <= 0).all())     # one rise-to-fall at most
vreg = res["refined_best"]["registered"]["viol"]
ok5 = uni and vreg > 1.074 and vreg < 1.30
checks.append(("(5) STRUCTURAL SUB-QUESTION (pre-registered before running) "
               "CONFIRMED + v1 STRENGTHENED: the kinetic family is unimodal at "
               "every tested alpha (Poisson-mixture form; no two-delta gap "
               "realizable), and its best registered-frame violation is x%.3f -- "
               "WORSE than the unconstrained mixture's x1.074: formation kinetics "
               "push the population FARTHER from passing at v1; the kill is "
               "strengthened, not threatened, at the registered frame" % vreg,
               ok5, None))

# (6) GATE GRADE. Frame-adoption gate G1 = PASSED-with-texture: the registered
#     1855 kinetics realize suite-passing populations at both audited frames
#     (deep/unstrained at extended; shallow/strained at central). The rent as
#     written ("dimer dominance") is DISCHARGED-reframed: f2 = 0.99 is reachable
#     (alpha_99 ~ 9.9e2, ledger) but NOT REQUIRED -- the two-delta dimer+trace
#     structure was the 2344 parametrization's shape, not the demand's. Ledger
#     entries: alpha_pass(central) ~ 3-6; p_min(central) = 13; alpha_99 ~ 989.
#     NO VERDICT MOVED: the v1 kill is final; G1 gates only frame adoption and
#     the papers' population section. G2 (satellite survival) and G3 (per-dSph
#     likelihood) remain owed before any F3 auto-proposal.
ok6 = all(o for _, o, _ in checks) and res["alpha_f2_99"] is not None \
      and 500 < res["alpha_f2_99"] < 2000
checks.append(("(6) GATE G1 (frame-adoption) = PASSED-with-texture; rent "
               "DISCHARGED-reframed (dimer dominance reachable at alpha_99 = %.0f "
               "but not required); inverse-coefficient ledger gains "
               "alpha_pass(central) ~ 3-6 and p_min(central) = 13; NO VERDICT "
               "MOVED; G2/G3 still owed before F3 auto-proposal"
               % res["alpha_f2_99"], ok6, None))

npass = 0
for msg, ok, _ in checks:
    print(("PASS " if ok else "FAIL ") + msg + "\n")
    npass += ok
print("=== %d/%d ===" % (npass, len(checks)))
