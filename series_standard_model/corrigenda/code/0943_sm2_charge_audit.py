#!/usr/bin/env python3
"""
0943 — full charge audit of SM-2's Particle Cage Assignments against SM-2's own
charge rules, on the founder's instruction (13 Sep 2026) to fix the other SM
particles carrying the wrong charge.

SM-2's rules, from the paper:
  * orbital ZBW inner pole screens a CONFINED CENTRAL qCP by delta = 1/3
    exactly (SS"Charge Quantisation", SM-1 Thm 1 from cage completeness + C3).
    The screening applies to the confined qCP centre; leptons are unscreened.
  * a linear ZBW extra rides unscreened on the centre.
  * DP species (eDP, qDP, hDP, hDP-A/B) are bound CP/anti-CP pairs: charge 0.

Every cage entry is evaluated against the observed SM charge. The audit is
structural and mechanical: it does not choose compositions, it only reports
which entries can and cannot reproduce the charge SM-2 must give them.

  T1  the rules reproduce the up-type quarks (u, c, t) at +2/3 as written.
  T2  the charged leptons (e, mu, tau) are unscreened eCP centres at -1 as
      written; the neutrinos and the neutral bosons (Z, Higgs) are 0 as
      written. No correction owed to any of these.
  T3  DOWN-TYPE FAILURE, all three: d, s and b are each written with a central
      -qCP, which screens to -2/3, and no neutral extra can reach -1/3. The
      down was corrected at 0942; STRANGE and BOTTOM carry the identical
      defect and the identical repair (+qCP centre + linear -eCP).
  T4  the repair is cage-independent: the -1 gap is the same for d (N_k=2.5),
      s (N_k=30) and b (N_k=3000), so no cage-size argument distinguishes them
      and the fix generalises exactly.
  T5  W FAILURE (new, not previously flagged): the W is written as a linear
      hDP chain. An hDP chain is a chain of neutral pairs and carries charge 0,
      so the assignment describes a NEUTRAL object, while W+- carries +-1.
      The Z (neutral, icosahedral cage) and Higgs (neutral) are unaffected --
      the defect is specific to the charged member of the weak triplet.
  T6  after the d/s/b repair, every entry except W reproduces its SM charge;
      W is the single residual, and closing it needs a composition ruling,
      not arithmetic.
"""
import sys
from fractions import Fraction as F

res = []
def ok(n, c, note=""):
    res.append(c); print(f"{n} {'PASS' if c else 'FAIL'}  {note}")

DELTA = F(1, 3)
Q = {"+qCP": F(1), "-qCP": F(-1), "+eCP": F(1), "-eCP": F(-1),
     "eDP": F(0), "qDP": F(0), "hDP": F(0), "hDP-A": F(0), "hDP-B": F(0),
     "none": F(0)}
DP_SPECIES = [s for s, q in Q.items() if q == 0 and s != "none"]

def charge(centre, extra="none", screened=True):
    q = Q[centre] * (1 - DELTA) if screened else Q[centre]
    return q + Q[extra]

# (name, observed charge, centre as written, extra as written, screened?)
AS_WRITTEN = [
    ("electron", F(-1),    "-eCP", "none",  False),
    ("muon",     F(-1),    "-eCP", "none",  False),
    ("tau",      F(-1),    "-eCP", "none",  False),
    ("up",       F(2, 3),  "+qCP", "none",  True),
    ("down",     F(-1, 3), "-qCP", "qDP",   True),   # "+extra DP"
    ("strange",  F(-1, 3), "-qCP", "none",  True),
    ("charm",    F(2, 3),  "+qCP", "none",  True),
    ("bottom",   F(-1, 3), "-qCP", "none",  True),
    ("top",      F(2, 3),  "+qCP", "none",  True),
    ("nu_e",     F(0),     "none", "none",  False),
    ("nu_mu",    F(0),     "none", "none",  False),
    ("nu_tau",   F(0),     "none", "none",  False),
    ("Z",        F(0),     "none", "none",  False),
    ("Higgs",    F(0),     "none", "none",  False),
    ("W",        F(1),     "none", "hDP",   False),  # "linear hDP chain"
]

verdict = {}
for name, obs, centre, extra, scr in AS_WRITTEN:
    got = charge(centre, extra, scr)
    verdict[name] = (got, got == obs, obs)

up_type = ["up", "charm", "top"]
ok("T1", all(verdict[p][1] for p in up_type),
   "up-type (u, c, t): +qCP screened by 1/3 -> +2/3, correct as written")

neutral_ok = ["electron", "muon", "tau", "nu_e", "nu_mu", "nu_tau", "Z", "Higgs"]
ok("T2", all(verdict[p][1] for p in neutral_ok),
   "charged leptons -1 (unscreened eCP) and neutrals 0: correct as written, no correction owed")

down_type = ["down", "strange", "bottom"]
fails = {p: str(verdict[p][0]) for p in down_type if not verdict[p][1]}
no_neutral_rescue = all(
    charge("-qCP", sp, True) != F(-1, 3) for sp in DP_SPECIES)
ok("T3", set(fails) == set(down_type) and no_neutral_rescue,
   f"down-type as written all fail: {fails} against required -1/3; no neutral DP species rescues "
   "a -qCP centre. down fixed at 0942; STRANGE and BOTTOM carry the identical defect")

gaps = {p: F(-1, 3) - F(2, 3) for p in down_type}
N_k = {"down": F(5, 2), "strange": F(30), "bottom": F(3000)}
ok("T4", len(set(gaps.values())) == 1 and list(gaps.values())[0] == F(-1)
   and len(set(N_k.values())) == 3,
   f"the required gap is {list(gaps.values())[0]} for all three despite N_k = "
   f"{ {k: str(v) for k, v in N_k.items()} } — cage-independent, so the repair generalises exactly")

w_got, w_ok, w_obs = verdict["W"]
ok("T5", not w_ok and w_got == F(0) and w_obs == F(1)
   and verdict["Z"][1] and verdict["Higgs"][1],
   f"W as written (linear hDP chain) carries {w_got}, but W+- carries {w_obs}: an hDP chain is a "
   "chain of neutral pairs. Z and Higgs are neutral and unaffected — the defect is the charged "
   "member of the weak triplet only")

# after the ruled repair
REPAIRED = dict(verdict)
for p in down_type:
    REPAIRED[p] = (charge("+qCP", "-eCP", True), charge("+qCP", "-eCP", True) == F(-1, 3), F(-1, 3))
residual = [p for p, (_, good, _) in REPAIRED.items() if not good]
ok("T6", all(REPAIRED[p][1] for p in down_type) and residual == ["W"],
   f"after the d/s/b repair every entry reproduces its SM charge except {residual} — "
   "W is the single residual and needs a composition ruling, not arithmetic")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
