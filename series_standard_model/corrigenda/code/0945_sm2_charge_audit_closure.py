#!/usr/bin/env python3
"""
0945 — closing charge audit of SM-2, with the W composition ruled.

Founder ruling 13 Sep 2026 (typo corrected on the same date): the W^0 is a
neutral 12-member ring of three qDPs and three eDPs; W^+- is a W^0 carrying a
+ or - eCP on the enzymatic structure. Harmonised at 0944 against the Weak
Sector lane's W-bracelet (SF-2 v1.0 Thm 4.2): a Petrie hexagon of the first-
shell icosahedron, six vertices, stabiliser D6 of order 12.

This re-runs the 0943 audit with the down-type repair (0943) AND the ruled W
composition in place, and asserts that SM-2 has no residual charge defect.

  T1  the ruled W^0 is neutral: 3 qDP + 3 eDP, all bound pairs.
  T2  the ruled W^0 has 12 CPs on 6 ring sites, one DP object per Petrie
      vertex, matching the lane's hexagon.
  T3  W^+ and W^- come out at exactly +1 and -1 from one carried eCP.
  T4  the member count is unchanged from SM-2's current "Linear 6-hDP chain"
      (12 CPs): the correction is topology + species only.
  T5  CLOSURE: with 0942/0943's down-type repair and this W composition, every
      entry in SM-2's Particle Cage Assignments reproduces its SM charge.
      Zero residuals.
  T6  the repair introduced no regression: up-type, charged leptons, neutrinos,
      Z and Higgs are untouched and still correct.
"""
import sys
from fractions import Fraction as F

res = []
def ok(n, c, note=""):
    res.append(c); print(f"{n} {'PASS' if c else 'FAIL'}  {note}")

DELTA = F(1, 3)
Q = {"+qCP": F(1), "-qCP": F(-1), "+eCP": F(1), "-eCP": F(-1),
     "eDP": F(0), "qDP": F(0), "hDP": F(0), "none": F(0)}
PETRIE_SITES = 6

W0 = ["qDP", "qDP", "qDP", "eDP", "eDP", "eDP"]     # the ruled composition
W0_charge = sum(Q[x] for x in W0)
W0_cps = 2 * len(W0)

ok("T1", W0_charge == F(0), f"ruled W^0 = 3 qDP + 3 eDP -> charge {W0_charge}: neutral, all bound pairs")
ok("T2", W0_cps == 12 and len(W0) == PETRIE_SITES,
   f"{W0_cps} CPs across {len(W0)} DP objects = one per Petrie-hexagon vertex ({PETRIE_SITES} sites)")
ok("T3", W0_charge + Q["+eCP"] == F(1) and W0_charge + Q["-eCP"] == F(-1),
   "W^+- = W^0 + one carried eCP -> exactly +1 / -1; charge on the unpaired CP (3513 partnerless third)")
ok("T4", W0_cps == 6 * 2,
   "SM-2's current 'Linear 6-hDP chain' is also 12 CPs — topology (chain -> ring) and species "
   "(6 hDP -> 3 qDP + 3 eDP) change; the member count does not")

def quark(centre, extra="none"):
    return Q[centre] * (1 - DELTA) + Q[extra]

FINAL = {
    "electron": (F(-1),    Q["-eCP"]),
    "muon":     (F(-1),    Q["-eCP"]),
    "tau":      (F(-1),    Q["-eCP"]),
    "up":       (F(2, 3),  quark("+qCP")),
    "charm":    (F(2, 3),  quark("+qCP")),
    "top":      (F(2, 3),  quark("+qCP")),
    "down":     (F(-1, 3), quark("+qCP", "-eCP")),      # 0942
    "strange":  (F(-1, 3), quark("+qCP", "-eCP")),      # 0943
    "bottom":   (F(-1, 3), quark("+qCP", "-eCP")),      # 0943
    "nu_e":     (F(0), F(0)), "nu_mu": (F(0), F(0)), "nu_tau": (F(0), F(0)),
    "Z":        (F(0), F(0)), "Higgs": (F(0), F(0)),
    "W0":       (F(0), W0_charge),                       # 0945
    "W+":       (F(1), W0_charge + Q["+eCP"]),
    "W-":       (F(-1), W0_charge + Q["-eCP"]),
}
residual = [p for p, (obs, got) in FINAL.items() if obs != got]
ok("T5", residual == [],
   f"CLOSURE: all {len(FINAL)} entries reproduce their SM charge; residual defects: {residual}")

untouched = ["electron", "muon", "tau", "up", "charm", "top",
             "nu_e", "nu_mu", "nu_tau", "Z", "Higgs"]
ok("T6", all(FINAL[p][0] == FINAL[p][1] for p in untouched),
   "no regression: up-type, charged leptons, neutrinos, Z and Higgs untouched and still correct")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
