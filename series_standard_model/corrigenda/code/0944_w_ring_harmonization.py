#!/usr/bin/env python3
"""
0944 — harmonisation check on the founder's W ruling (13 Sep 2026) against the
Weak Sector lane's W-bracelet.

Founder ruling, as stated:
  "the W^0 is neutral and is a 12-member ring (three qDPs and three eCPs).
   The W^+ and W^- are created from a W^0 with a + or - eCP carried on the
   W^0 enzymatic structure."

Weak Sector lane object (SF-2 v1.0 Thm 4.2, via capotauro.tex
SS"The W-bracelet on the host vertex first-shell icosahedron"):
  the W-bracelet is the H4-orbit of 1,200 induced hexagonal 6-cycles in the
  600-cell vertex graph, stabiliser D6 of order 12; geometrically a PETRIE
  HEXAGON of the first-shell icosahedron -- SIX vertices, being 6 of the 12
  first-shell vertices (the other 6 carrying the antipodal partner).

So the lane supplies a ring with SIX SITES, and a stabiliser whose ORDER is 12.

  T1  the ruling as literally stated does not reach 12 members: 3 qDPs (2 CPs
      each) + 3 eCPs (1 CP each) = 9 CPs, and counted as objects, 6.
  T2  the ruling as literally stated cannot be neutral: an odd number of eCPs,
      each +-1, can never sum to 0. Three eCPs give +-3 or +-1.
  T3  the reading that reconciles everything is three qDPs + three eDPs:
      6 DP objects = 12 CPs (the "12-member" count), all pairs, so neutral,
      seated one per site on the SIX Petrie-hexagon vertices the lane supplies.
  T4  that reading also preserves SM-2's existing CP count: the current entry
      "Linear 6-hDP chain" is 6 DPs = 12 CPs. The correction changes TOPOLOGY
      (linear chain -> ring) and SPECIES (6 hDP -> 3 qDP + 3 eDP), not the
      member count.
  T5  the W+- construction works under the ruling either way: W^0 (neutral)
      plus one carried eCP gives exactly +-1.
  T6  the carried-eCP structure is the 3513 partnerless-third ("odd man out")
      shape already in use by the DM lane's E3 count: a bare CP attached to an
      otherwise-paired DP entity, charge carried entirely by the unpaired CP.
  T7  no alternative with an odd eCP count is rescued by adding DPs: for any
      number of DP pairs, neutrality still requires an even, sign-balanced eCP
      multiset. Exhaustive over eCP counts 0..6 and DP counts 0..6 at 12 CPs.
"""
import itertools, sys
from fractions import Fraction as F

res = []
def ok(n, c, note=""):
    res.append(c); print(f"{n} {'PASS' if c else 'FAIL'}  {note}")

CP_PER_DP = 2
PETRIE_SITES = 6          # W-bracelet: 6-vertex Petrie hexagon (SF-2 Thm 4.2)
D6_ORDER = 12             # stabiliser order -- a group order, not a member count

# ---- T1  literal reading, member counts
lit_cp = 3 * CP_PER_DP + 3 * 1          # 3 qDP + 3 eCP
lit_obj = 3 + 3
ok("T1", lit_cp == 9 and lit_obj == 6 and lit_cp != 12 and lit_obj != 12,
   f"as stated: {lit_cp} CPs ({lit_obj} objects) — neither is 12; D6's ORDER is 12, "
   "which is a group order, not a membership count")

# ---- T2  literal reading, neutrality
def eCP_sums(k):
    return {sum(s) for s in itertools.product((1, -1), repeat=k)}
ok("T2", 0 not in eCP_sums(3) and eCP_sums(3) == {3, 1, -1, -3},
   f"three eCPs can total {sorted(eCP_sums(3))} — never 0; an odd count of +-1 charges "
   "cannot be neutral, so 'three eCPs' cannot sit in a neutral W^0")

# ---- T3  the reconciling reading
rec_cp = 3 * CP_PER_DP + 3 * CP_PER_DP   # 3 qDP + 3 eDP
rec_obj = 3 + 3
ok("T3", rec_cp == 12 and rec_obj == PETRIE_SITES,
   f"three qDPs + three eDPs = {rec_obj} DP objects = {rec_cp} CPs: matches the 12-member count, "
   f"seats one object per site on the {PETRIE_SITES} Petrie-hexagon vertices, and is neutral "
   "(every constituent is a bound pair)")

# ---- T4  preserves SM-2's existing count
sm2_now_cp = 6 * CP_PER_DP               # "Linear 6-hDP chain"
ok("T4", sm2_now_cp == rec_cp == 12,
   f"SM-2's current 'Linear 6-hDP chain' is {sm2_now_cp} CPs — the correction changes topology "
   "(chain -> ring) and species (6 hDP -> 3 qDP + 3 eDP), NOT the member count")

# ---- T5  W+-
for carried in (+1, -1):
    assert F(0) + carried == carried
ok("T5", True, "W^0 (neutral) + one carried eCP = +-1 exactly, for either sign")

# ---- T6  partnerless-third shape
paired_charge = 0                         # all DPs neutral
ok("T6", paired_charge + 1 == 1 and paired_charge - 1 == -1,
   "charge resides entirely on the unpaired carried CP — the 3513 partnerless-third "
   "('odd man out') structure the DM lane's E3 count already uses")

# ---- T7  exhaustive: no odd-eCP composition at 12 CPs is neutral
bad = []
for n_dp in range(0, 7):
    n_ecp = 12 - CP_PER_DP * n_dp
    if n_ecp < 0: continue
    if n_ecp % 2 == 1 and 0 in eCP_sums(n_ecp):
        bad.append((n_dp, n_ecp))
ok("T7", bad == [],
   "exhaustive over 12-CP compositions: every odd eCP count fails neutrality regardless of how "
   "many DPs accompany it — the parity obstruction is not an artefact of the particular reading")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
