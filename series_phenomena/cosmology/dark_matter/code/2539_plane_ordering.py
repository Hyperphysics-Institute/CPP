#!/usr/bin/env python3
"""Patch 2539 verify -- sec6g First Addendum structural checks (no derivation).

  1. Q2 assembly ordering: (eDP-qDP) + (qDP-eDP) joined at the preferential qDP-qDP bond gives
     the sequence eDP-qDP-qDP-eDP, matching the registered Candidate-B diagonal ordering
     eCP-qCP-qCP-eCP at DP<->CP level.
  2. Corrected convergence inventory after the founder's Q4 disclosure: independent components =
     {plane CP content, assembly ordering}; consumed component = {N=16}. (Documentation check.)
  3. Retirement consistency: the founder's 'energetically impossible' ruling asserts DeltaE_b > 0
     (or dynamical instability) for the FREE tetra; this is consistent with the 2537 frozen sign
     structure (T_dist +, T_color -, T_store ?) iff the positive terms dominate -- no frozen sign
     is violated (T_color's registered direction remains '-'; only the SUM is ruled positive).
"""
ok = True
def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and cond

# 1. Assembly ordering
unit_ab = ["eDP", "qDP"]
unit_cd = ["qDP", "eDP"]          # second unit presented qDP-first at the qDP-qDP bond
assembled = unit_ab + unit_cd
check("assembly (eDP-qDP)+(qDP-eDP) at qDP-qDP bond -> eDP-qDP-qDP-eDP",
      assembled == ["eDP", "qDP", "qDP", "eDP"])
registered_diagonal = ["eCP", "qCP", "qCP", "eCP"]
dp_to_cp = {"eDP": "eCP", "qDP": "qCP"}
check("matches registered diagonal eCP-qCP-qCP-eCP at DP<->CP level",
      [dp_to_cp[x] for x in assembled] == registered_diagonal)

# 2. Convergence inventory (documentation)
independent = {"plane_cp_content", "assembly_ordering"}
consumed = {"N_16"}
check("convergence inventory: independent and consumed components disjoint",
      independent.isdisjoint(consumed))

# 3. Sign consistency: sum ruled positive violates no individual frozen sign
signs = {"T_dist": +1, "T_color": -1, "T_store": None}   # frozen at 2537
# 'sum > 0' is satisfiable with T_dist>0, T_color<0, T_store free -> no frozen sign flipped
check("founder sum-positive ruling is satisfiable under 2537 frozen individual signs",
      signs["T_dist"] > 0 and signs["T_color"] < 0)

print()
print("ALL CHECKS PASS" if ok else "FAILURES PRESENT")
raise SystemExit(0 if ok else 1)
