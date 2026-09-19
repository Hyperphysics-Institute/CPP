#!/usr/bin/env python3
"""
Patch 4141 — TODO-4140-BIVECTOR pressed, and it does NOT discharge. What it
turns up instead is a role conflation in SSV_net that predates the amendment.

WHAT 4140 CLAIMED
-----------------
That T1_u (V_i, polar) and T1_g (A_i, axial) are the six components of one
antisymmetric rank-2 tensor, so b = A.V is that tensor's pseudoscalar invariant
and no absolute-frame signature can appear. I called the structure "forced".

WHAT THE AXIOM TEXT ACTUALLY SAYS
---------------------------------
master_glossary, LSP' entry, verbatim: "nine dynamical components -- scalar
Phi = |SSV|_abs (icosahedral irrep A, l=0; g_tt), vector V_i = SSV_net (T1,
l=1; spatial curvature/gravitomagnetism), and the symmetric-traceless Q_ij
(H, l=2; the radiative tensor / gravitational-wave sector) -- exactly the
lattice's rotationally protected representation content."

Phi = g_tt. V_i = g_ti. Q_ij = the radiative tensor. 1 + 3 + 5 = 9 is the
traceless symmetric rank-2 tensor h_munu -- THE METRIC PERTURBATION.

A component of a SYMMETRIC rank-2 tensor cannot also be half of an
ANTISYMMETRIC one. So V_i is not available to be A_i's bivector partner, and
4140's "forced" is too strong.
"""
import numpy as np

out = []
def say(s=""):
    print(s); out.append(s)

say("K1  component census -- is there room for A_i inside LSP' as written?")
say(f"    {'object':<34}{'components':>12}   content")
say(f"    {'traceless symmetric h_munu':<34}{9:>12}   Phi(1) + V_i(3) + Q_ij(5)")
say(f"    {'antisymmetric rank-2 (bivector)':<34}{6:>12}   3 polar + 3 axial")
say(f"    {'general rank-2 in 4D':<34}{16:>12}   10 symmetric + 6 antisymmetric")
say()
say("    LSP' as written = the 9 of the traceless SYMMETRIC sector, and the")
say("    glossary says so twice over ('g_tt', 'gravitomagnetism', 'radiative")
say("    tensor', 'no fourth rung'). A_i is an ADDITION to that, not a member.")
say("    Patch 4113's own words: the T1_g channel 'the ROTATION-ONLY")
say("    enumeration omitted' -- omitted because l = 1 cannot distinguish")
say("    T1_u from T1_g, not because it was hiding among the nine.")
say()
say("    => 4140 needed V_i to sit in the antisymmetric sector. It sits in the")
say("       symmetric one. **4140's 'forced' is WITHDRAWN.**")
say()

say("K2  what a genuine bivector partner for A_i would have to be")
say("    A_i is axial, 3 components. Its partner is a POLAR 3-vector that")
say("    transforms into it under a boost. In the GR sector that object exists")
say("    and is standard: the gravito-electromagnetic field tensor, built from")
say("    Phi and V_i the way F_munu is built from the EM potentials --")
say("        E^G = -grad Phi - d_t V ,   B^G = curl V .")
say("    E^G is polar, B^G is axial, and (E^G, B^G) IS an antisymmetric rank-2")
say("    object with an invariant E^G . B^G.")
say()
say("    But then A_i's partner is E^G, NOT V_i. And b would have to be")
say("    A . E^G, not A . V. Those are different quantities: E^G is built from")
say("    DERIVATIVES of the potentials, V_i is the potential itself.")
say()

say("K3  and this exposes something older than the amendment")
say("    The corpus uses SSV_net in TWO roles and b = A.V does not say which:")
say("      role 1  the CP's local DISPLACEMENT INSTRUCTION -- 'every CP")
say("              executes one Displace step per its GP's computed SSV_net'")
say("              (master_glossary, A1' division of labor). Velocity-like.")
say("      role 2  the l=1 BROADCAST COMPONENT V_i = g_ti, the gravitomagnetic")
say("              POTENTIAL (master_glossary, LSP' entry). Potential-like.")
say()
say("    These transform differently and are not interchangeable:")
say("      - a potential is gauge-dependent; A . (potential) is not even")
say("        gauge-invariant, let alone Lorentz-invariant;")
say("      - a velocity is frame-dependent in the ordinary way and needs its")
say("        bivector partner to be protected, which is 4140's argument.")
say("    **The role conflation predates the amendment.** It did not matter")
say("    while nothing contracted V_i with an axial vector. b = A.V is the")
say("    first construction that does, which is why it surfaces here.")
say()

say("K4  status of the three results that depended on 4140")
rows = [("4140's 'F6 forces the M_munu pairing'",
         "WITHDRAWN as stated -- F6 fixes the PARITIES the partner must have,"),
        ("", "  which is real, but does not supply a partner from LSP' as written."),
        ("b = A.V is Lorentz-invariant",
         "UNPROVEN, not disproven -- true IF the partner exists and is what"),
        ("", "  b contracts A with. Both are now open."),
        ("4139's drift term",
         "STAYS WITHDRAWN -- that calculation boosted one half of a two-part"),
        ("", "  object, which is wrong under EITHER reading. Independent of this.")]
for a, b in rows:
    say(f"    {a:<38}{b}")
say()

say("VERDICT")
say("  TODO-4140-BIVECTOR does NOT discharge. Pressing it found that the")
say("  partner 4140 assumed is not available in the axiom text, and that the")
say("  reason is a two-role use of SSV_net older than the amendment.")
say("  A3G-2 remains NOT FIRING and NOT PASSING, for a sharper reason than")
say("  yesterday: not 'the transport law is unstated' but 'the object b")
say("  contracts A with is ambiguous between a velocity and a potential'.")
say("  That ambiguity is the thing to fix, and fixing it is upstream of the")
say("  amendment -- it touches SR-1/GR-1 usage, not just chi_4.")

open("/tmp/4141_out.txt", "w").write("\n".join(out))
