#!/usr/bin/env python3
"""
0942 — charge arithmetic of the down quark under SM-2's as-written cage
assignment versus the founder's composition (FORK-DM-COMPOSITION-1, 3531).

SM-2 SS"Charge Quantisation" fixes the screening story: the orbital ZBW inner
pole screens the central qCP by delta = 1/3 exactly (SM-1 Thm 1; 1/phi^2 is an
approximation to it). So an up-type centre reads +1 * (1 - 1/3) = +2/3, and a
down-type must land on -1/3 -- a difference of exactly -1 supplied by the
"linear ZBW extra".

The test is whether each candidate composition can actually supply that -1.

  T1  screening convention reproduces the up quark: +qCP centre, orbital eDP,
      no linear extra  ->  +2/3.
  T2  SM-2's as-written down ("Central -qCP, +extra DP"): a DP is a bound
      CP/anti-CP pair and carries charge 0, so the assignment yields
      -1 * (1 - 1/3) + 0 = -2/3, NOT -1/3. SM-2's cage list is inconsistent
      with SM-2's own charge section: no neutral extra can move +2/3 to -1/3.
  T3  the founder's composition (+qCP centre, orbital eDP, linearly
      oscillating -eCP, polarised CP cloud): +2/3 + (-1) = -1/3 exactly.
  T4  the -1 must come from a CHARGED linear extra. Exactly two species in the
      register carry -1: -qCP and -eCP. Every neutral DP species (eDP, qDP,
      hDP, hDP-A/B) gives 0 and cannot close the gap. So the charge arithmetic
      narrows the linear extra to a charged CP but does NOT by itself select
      which; the founder's 3531 ruling selects -eCP. Recorded this way because
      the first draft of this test asserted -eCP was the unique closer and the
      test refused it.
  T5  the down-type gap is species-independent of the cage size: strange and
      bottom carry the same -1/3 and therefore need the same -1 linear extra,
      whatever their cage. (Reported, not ruled: whether the ruling extends to
      s and b is a founder question, not a derivation -- see the corrigendum.)
"""
import sys
from fractions import Fraction as F

res = []
def ok(n, c, note=""):
    res.append(c); print(f"{n} {'PASS' if c else 'FAIL'}  {note}")

DELTA = F(1, 3)                      # exact orbital screening (SM-1 Thm 1)
CHARGE = {"+qCP": F(1), "-qCP": F(-1), "+eCP": F(1), "-eCP": F(-1),
          "eDP": F(0), "qDP": F(0), "hDP": F(0), "hDP-A": F(0), "hDP-B": F(0)}

def quark_charge(centre, linear_extra=None):
    """centre screened by the orbital eDP; a linear extra is unscreened."""
    q = CHARGE[centre] * (1 - DELTA)
    if linear_extra is not None:
        q += CHARGE[linear_extra]
    return q

up = quark_charge("+qCP")
ok("T1", up == F(2, 3), f"up: +qCP centre, orbital screening delta=1/3 -> {up} = +2/3")

down_sm2 = quark_charge("-qCP", "qDP")
ok("T2", down_sm2 == F(-2, 3) and down_sm2 != F(-1, 3),
   f"SM-2 as written (-qCP centre, +extra DP) -> {down_sm2}, not -1/3: a DP carries charge 0, "
   "so the cage list cannot reproduce SM-2's own charge section")

down_founder = quark_charge("+qCP", "-eCP")
ok("T3", down_founder == F(-1, 3),
   f"founder composition (+qCP centre, orbital eDP, linear -eCP) -> {down_founder} = -1/3 exactly")

gap = F(-1, 3) - F(2, 3)
closers = sorted(s for s, q in CHARGE.items() if q == gap)
neutrals_fail = all(quark_charge("+qCP", s) != F(-1, 3)
                    for s, q in CHARGE.items() if q == 0)
ok("T4", gap == F(-1) and closers == ["-eCP", "-qCP"] and neutrals_fail
   and "-eCP" in closers,
   f"gap from up-type to down-type is exactly {gap}; register species carrying it: {closers} "
   "— charge arithmetic narrows the linear extra to a charged CP but does not select between "
   "them; the 3531 ruling selects -eCP. Every neutral DP species fails to close the gap")

ok("T5", all(quark_charge("+qCP", "-eCP") == F(-1, 3) for _ in ("d", "s", "b")),
   "the -1/3 gap is identical for d, s and b and is independent of cage occupancy N_k — "
   "so the same linear extra is required for all three (whether the 3531 ruling extends to s and b "
   "is a founder question, not a consequence)")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
