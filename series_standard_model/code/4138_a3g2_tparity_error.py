#!/usr/bin/env python3
"""
Patch 4138 — A3G-2's T-parity argument is WRONG, and its own verify script
says so. Found while working TODO-4137-FILTERTABLE.

WHAT 4125 CLAIMED
-----------------
"The spin-dependent forces that torsion balances and comagnetometers actually
bound are the T-odd ones -- monopole-dipole A.r-hat and spin-velocity A.v.
chi_4's b is T-even (F6) and the response is linear in b (B3), so a T-even
carrier cannot source a T-odd potential.  A3G-2 PASSES."

WHAT ITS OWN SCRIPT COMPUTES
----------------------------
`code/4125_a3g2_spin_dependent_force.py` sets T = {'A': -1, 'V': -1, 'r': +1,
'v': -1} and prints, in its own output table:

    A.v   spin-velocity    Axv    -1  +1   chi_4 CAN source (matches b)

T = +1. T-EVEN. The prose two paragraphs below the table asserts the opposite.
The table was printed and not read.

THE ARGUMENT DOES NOT NEED NEW INPUT -- IT FOLLOWS FROM F6
----------------------------------------------------------
F6 (from CPT, Patch 4085): b = A.V is T-EVEN.
A is the ZBW spin (Patch 4112: the spin half of <L + 2S>), so A is T-ODD.
Therefore V must be T-ODD -- which is also what V is physically, the
displacement-per-Moment (master_glossary: "every CP executes one Displace step
per its GP's computed SSV_net").
But then A.v -- the same contraction with the same T-parities -- is T-EVEN too.

A.v and A.V are NOT two different objects. b IS a spin-velocity pseudoscalar.
So "comagnetometers bound A.v, and chi_4 cannot source it" is self-refuting:
the thing bounded and the thing chi_4 is built on are the same invariant.
"""
import itertools

out = []
def say(s=""):
    print(s); out.append(s)

# parities exactly as 4125's own script sets them
P = {'A': +1, 'V': -1, 'r': -1, 'v': -1, 'E': -1, 'B': +1}
T = {'A': -1, 'V': -1, 'r': +1, 'v': -1, 'E': +1, 'B': -1}

def cls(parts):
    p = t = 1
    for q in parts:
        p *= P[q]; t *= T[q]
    return p, t

say("G1  recompute 4125's own table with 4125's own parities")
rows = [("A1.A2      spin-spin", ['A', 'A']),
        ("(A1.r)(A2.r) tensor", ['A', 'r', 'A', 'r']),
        ("A.r        monopole-dipole", ['A', 'r']),
        ("A.v        spin-velocity", ['A', 'v']),
        ("(A x v).r", ['A', 'v', 'r']),
        ("A.V        = the bit b", ['A', 'V'])]
claimed = {"A.r        monopole-dipole": (-1, -1),
           "A.v        spin-velocity": (-1, -1),      # 4125 prose + doc table
           "(A x v).r": (+1, -1),                      # 4125 doc table
           "A.V        = the bit b": (-1, +1)}
say(f"    {'potential':<28}{'computed':>12}{'4125 doc':>12}   agree?")
bad = []
for nm, parts in rows:
    p, t = cls(parts)
    c = claimed.get(nm)
    ok = "-" if c is None else ("yes" if c == (p, t) else "** NO **")
    if ok == "** NO **":
        bad.append(nm)
    cs = "" if c is None else f"P{c[0]:+d} T{c[1]:+d}"
    say(f"    {nm:<28}{f'P{p:+d} T{t:+d}':>12}{cs:>12}   {ok}")
say(f"    mismatches: {len(bad)} -> {', '.join(n.split()[0] for n in bad)}")
say()

say("G2  the finding does not rest on my parity choices -- it follows from F6")
say("    F6 (CPT, Patch 4085): b = A.V is T-EVEN.")
say("    A is the ZBW spin (Patch 4112) -> A is T-ODD.")
say("    => V must be T-ODD, which is also what V is physically: the")
say("       displacement per Moment (master_glossary, A1' division of labor).")
say("    => A.v, the same contraction with the same parities, is T-EVEN.")
say()
say("    So A.v and A.V are the SAME INVARIANT, not two rows of a table.")
say("    b IS a spin-velocity pseudoscalar. 'Comagnetometers bound A.v and")
say("    chi_4 cannot source it' is self-refuting: the bounded object and the")
say("    carrier are the same thing.")
say()
say("    To make A.v T-odd you would need A.V T-odd as well -- i.e. NOT-F6.")
say("    F6 and A3G-2's stated protection cannot both hold.")
say()

say("G3  what survives, checked term by term")
say("    A3G-3 (EM parity, Patch 4124): its protection is that an EDM is P-odd")
say("      AND T-ODD. EDM ~ A.E with E T-EVEN, so A.E is T-ODD. Genuinely T-odd,")
say(f"      recomputed here: A.E -> P{cls(['A','E'])[0]:+d} T{cls(['A','E'])[1]:+d}. **A3G-3 STANDS.**")
say("    A3G-2 monopole-dipole row: A.r-hat with r-hat T-even is genuinely")
say(f"      T-ODD (P{cls(['A','r'])[0]:+d} T{cls(['A','r'])[1]:+d}). That row's protection STANDS.")
say("    A3G-2 spin-velocity row: T-EVEN. **That row's protection FAILS.**")
say()

say("G4  does A3G-2 FIRE? Not shown here, and I am not going to pretend it is.")
say("    Firing requires the predicted spin-velocity coupling to EXCEED the")
say("    comagnetometer bound. This patch establishes only that the argument")
say("    recorded for the pass is invalid. A3G-2 returns to UNRUN, not FAILED.")
say("    The magnitude test is a separate bounded calculation and is filed.")
say()
say("    ONE CANDIDATE RESCUE, and note where it routes: if the filter table")
say("    holds and ONLY the transient bracelet channel reads b, there is no")
say("    LONG-RANGE spin-dependent potential between separated masses at all,")
say("    and comagnetometer bounds -- which constrain long-range couplings --")
say("    do not apply. That would save A3G-2 on structure rather than T-parity.")
say("    It is a candidate, not a closure, and it is CONDITIONAL ON THE VERY")
say("    FILTER TABLE that TODO-4137-FILTERTABLE was opened to derive.")
say()

say("VERDICT")
say("  A3G-2's T-parity protection is WITHDRAWN. Its own verify script printed")
say("  the refutation in its own output table and the prose beneath it asserted")
say("  the opposite; four patches and one session cited the prose.")
say("  A3G-3 STANDS -- its T-odd term is genuinely T-odd.")
say("  Suite status drops: FOUR of nine stand, not five.")
say("  And the premise concentration inverts: the problem was never that F6")
say("  carried too much. F6 is FINE. The problem is that a step was recorded")
say("  as following from F6 which in fact CONTRADICTS F6.")

open("/tmp/4138_out.txt", "w").write("\n".join(out))
