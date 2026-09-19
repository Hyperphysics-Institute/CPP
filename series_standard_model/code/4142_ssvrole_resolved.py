#!/usr/bin/env python3
"""
Patch 4142 — TODO-4141-SSVROLE resolved, from the corpus's own force equation.
It relocates the 4140 bivector question rather than closing it.

THE DECISIVE QUOTATION (GR-1a, Newtonian gravity from SSV), verbatim:
    "The force on a second mass m' in this SSV gradient is
         F = m' c^2 . k . grad(Delta SSV_grav)"
and, in the same paper: "A test particle in free fall moves along the local
SSV GRADIENT".

So in CPP's own gravity derivation the broadcast quantity is POTENTIAL-LIKE and
what a body responds to is its GRADIENT -- a derived field. That settles the
two-role question by the corpus's own construction, not by analogy.
"""
out = []
def say(s=""):
    print(s); out.append(s)

say("L1  the two objects, named by what the corpus does with them")
say(f"    {'':<8}{'object':<34}{'kind':<12}{'evidence'}")
say(f"    {'role 2':<8}{"LSP' component V_i = g_ti":<34}{'POTENTIAL':<14}"
    "glossary: 'g_tt', 'gravitomagnetism'")
say(f"    {'':<8}{'(and Phi = |SSV|_abs = g_tt)':<34}{'':<14}"
    "GR-1a: force = k.grad(Delta SSV)")
say(f"    {'role 1':<8}{'what a CP displaces by':<34}{'FIELD':<14}"
    "A1': 'one Displace step per its")
say(f"    {'':<8}{'':<34}{'':<14}"
    " GP's computed SSV_net'")
say()
say("    A potential and its gradient are not the same object -- they differ by")
say("    a derivative and they transform differently. GR-1a uses BOTH and")
say("    distinguishes them correctly in the scalar sector. The vector sector")
say("    inherits the same structure: V_i = g_ti is the gravitomagnetic")
say("    POTENTIAL, and what a body responds to is built from its derivatives,")
say("    E^G = -grad Phi - d_t V and B^G = curl V.")
say()
say("    => **TWO OBJECTS, ONE NAME.** 'SSV_net' in the A1' Displace clause is")
say("       NOT the LSP' component V_i. The corpus has been using the same")
say("       token for a potential and for a field.")
say()

say("L2  proposed disambiguation (terminology ruling; founder should see it)")
say("    SSV_net^pot   := the LSP' l=1 broadcast component, V_i = g_ti.")
say("                     Potential-like. What GPs broadcast.")
say("    SSV_net^disp  := the vector a CP actually displaces by in one Moment,")
say("                     built from derivatives of the broadcast potentials.")
say("                     Field-like. What the A1' Displace clause means.")
say("    Every corpus use of 'SSV_net' should resolve to one of these. Existing")
say("    text is NOT rewritten by this patch -- the audit is separate work.")
say()

say("L3  which one does b = A.V contract A with?")
say("    The corpus never says. But b is a statement about the CP's OWN motion")
say("    (4097, founder: a free particle's arcs persist, a confined quark's are")
say("    severed), so the intended object is **SSV_net^disp** -- the thing the")
say("    CP moves by. I record that as STRONGLY INDICATED, NOT PROVEN, and it")
say("    is exactly the kind of step I overstated at 4140.")
say()

say("L4  what this does to the 4140/4141 pair -- it RELOCATES, not closes")
say("    4141's objection was correct AGAINST ROLE 2: V_i = g_ti sits in the")
say("    traceless SYMMETRIC rank-2 tensor and cannot be half of an")
say("    antisymmetric one. That still stands.")
say("    But under role 1 the objection does not apply, because SSV_net^disp is")
say("    not a component of h_munu at all. It is an attribute OF THE CP --")
say("    and so is A_i. Two attributes of one object, one polar/boost-like and")
say("    one axial/rotation-like, is precisely the M_munu shape 4140 wanted.")
say()
say("    So the bivector question MOVES from the broadcast sector, where 4141")
say("    killed it, to the CP's own attributes, where it is live again.")
say("    **It is not thereby answered.** Whether the CP's (A, SSV_net^disp)")
say("    actually transform as one antisymmetric object under a boost is the")
say("    SAME unproven step as at 4140, now correctly located. I will not")
say("    write 'forced' a second time.")
say()

say("VERDICT")
say("  TODO-4141-SSVROLE: RESOLVED. Two objects, one name, distinguished by")
say("  the corpus's own force equation; disambiguation proposed; corpus audit")
say("  registered separately.")
say("  TODO-4140-BIVECTOR: still open, RELOCATED to the CP's attributes.")
say("  A3G-2: still not firing, not passing. Unchanged by this patch.")
