#!/usr/bin/env python3
"""
Patch 4140 — the founder's answer, derived rather than accepted; and my own
4139 drift calculation withdrawn.

FOUNDER (19 Sep, verbatim in founders_voice/4140_...): CPs do not measure their
motion against the universe or the local frame. They move in response to DI-bit
messages from the GPs in their PSR, determined by SSV_abs and SSV_net from the
summation over that environment. "The summation yields a Lorentz-modified local
reference-frame velocity, as in all relativity principle measurements, resulting
in no absolute-frame signature." Refers to SR-1, GR-1/2 and companions.

PD-008: do not stop at "the founder says no absolute-frame signature". Press it
to a mechanism that can be checked, and check whether it reaches the A channel,
which is the gap 4139 identified (SR-1 predates the A3' amendment).

WHAT 4139 ACTUALLY DID WRONG
----------------------------
4139 boosted V (added the drift u to every quark's SSV_net) while holding A
FIXED. That is not a transformation law -- it is half of one. If A and V belong
to the same Lorentz object, a boost mixes them, and the mixing is exactly what
protects A.V.

THE STRUCTURE, AND IT IS FORCED, NOT CHOSEN
-------------------------------------------
A3' lists LSP' = (Phi, V_i, Q_ij) as "the rotationally protected irreps" --
A + T1 + H = 1 + 3 + 5 = 9. Patch 4113 identified A_i as "the T1_g channel the
ROTATION-ONLY enumeration omitted". T1_u (V_i, polar) and T1_g (A_i, axial) are
both 3-dimensional under rotations and differ only in PARITY. In 4D that pair is
not two vectors: it is the six components of ONE antisymmetric rank-2 tensor.
Exactly the (E, B) structure of F_munu -- or the (K, J) structure of M_munu.

Which one? F6 decides it, and F6 was derived from CPT at 4085 for unrelated
reasons:
      F_munu type (E, B):  E T-even, B T-odd  ->  E.B is T-ODD
      M_munu type (K, J):  K T-odd,  J T-odd  ->  K.J is T-EVEN
F6 says b is T-EVEN. So (V, A) must be the M_munu (angular-momentum-type)
pairing. Nothing was chosen to make this work.
"""
import numpy as np

np.set_printoptions(precision=10, suppress=True)
out = []
def say(s=""):
    print(s); out.append(s)

rng = np.random.default_rng(4140)

say("J1  parity/time census -- which bivector type does b's signature select?")
say(f"    {'pairing':<28}{'P of a.b':>10}{'T of a.b':>10}   matches b (P-odd, T-even)?")
for nm, (Ppol, Tpol), (Pax, Tax) in [
        ("F_munu  (E polar, B axial)", (-1, +1), (+1, -1)),
        ("M_munu  (K polar, J axial)", (-1, -1), (+1, -1))]:
    p, t = Ppol * Pax, Tpol * Tax
    say(f"    {nm:<28}{p:>+10}{t:>+10}   {'YES' if (p, t) == (-1, +1) else 'no'}")
say("    F6 (b is T-EVEN, from CPT at Patch 4085) selects the M_munu pairing.")
say("    V = SSV_net is the boost-like (polar, T-odd) part;")
say("    A_i        is the rotation-like (axial, T-odd) part.")
say()

say("J2  is A.V then a Lorentz invariant? Boost the pair and check.")
def boost_pair(K, J, beta):
    """Bivector transformation, identical algebra to (E,B) under a boost."""
    b2 = beta @ beta
    if b2 < 1e-30:
        return K.copy(), J.copy()
    g = 1.0 / np.sqrt(1 - b2)
    bh = beta / np.sqrt(b2)
    Kpar, Jpar = (K @ bh) * bh, (J @ bh) * bh
    Kperp, Jperp = K - Kpar, J - Jpar
    Kp = Kpar + g * (Kperp + np.cross(beta, J))
    Jp = Jpar + g * (Jperp - np.cross(beta, K))
    return Kp, Jp

say("    random (V, A) pairs, random boosts, compare A.V before and after:")
worst = 0.0
for _ in range(200000):
    V = rng.normal(size=3); A = rng.normal(size=3)
    beta = rng.normal(size=3); beta *= rng.uniform(0, 0.95) / np.linalg.norm(beta)
    Vp, Ap = boost_pair(V, A, beta)
    worst = max(worst, abs(Ap @ Vp - A @ V) / (abs(A @ V) + 1e-12))
say(f"    worst relative change in A.V over 200000 boosts: {worst:.3e}")
say("    A.V is INVARIANT. It is the pseudoscalar invariant of the bivector,")
say("    the exact analogue of E.B for F_munu -- and E.B is famously the one")
say("    quantity a boost cannot change.")
say()

say("J3  what 4139 did instead, shown explicitly")
V = np.array([0.3, -0.2, 0.5]); A = np.array([0.1, 0.4, -0.3])
u = np.array([1.23e-3, 0.0, 0.0])          # the 370 km/s drift, beta = 1.23e-3
say(f"    rest-frame A.V           = {A @ V:+.10f}")
say(f"    4139: V -> V + u, A fixed = {A @ (V + u):+.10f}   "
    f"drift term {A @ u:+.3e}  <- SPURIOUS")
Vp, Ap = boost_pair(V, A, u)
say(f"    correct boost of the pair = {Ap @ Vp:+.10f}   "
    f"change {abs(Ap@Vp - A@V):.3e}")
say("    The drift term 4139 found is the residue of boosting ONE half of a")
say("    two-part object. Boost both halves and it cancels identically:")
say("    u x A is added to V and u x V is subtracted from A, and the two")
say("    cross terms in the dot product are equal and opposite.")
say()

say("J4  consequences, in order of how much they cost me")
say("    (a) 4139's drift computation is WITHDRAWN. There is no absolute-frame")
say("        residual in b. The founder's answer is correct, and it is now")
say("        DERIVED from F6 + the T1_u/T1_g pairing rather than accepted.")
say("    (b) A3G-2 is no longer conditionally firing on THIS route: the")
say("        sidereal spin-energy modulation that the comagnetometer bounds")
say("        is identically zero, not merely suppressed. No 1e23 gap.")
say("    (c) 4134's rest-frame calculation STANDS as originally written. My")
say("        4139 'revision' of it is itself revised away.")
say("    (d) The escape is not SR-1 extended by hand. It is that b was ALREADY")
say("        the right kind of object -- a bivector pseudo-invariant -- and")
say("        F6, derived at 4085 for unrelated reasons, is what says so.")
say()

say("J5  WHAT IS STILL OWED -- and it is the real residual, not a formality")
say("    Everything above holds IF (V_i, A_i) are two halves of ONE Lorentz")
say("    object. A3' as written lists them as SEPARATE BROADCAST COMPONENTS of")
say("    LSP', not as one tensor. If they are independent channels, each")
say("    transported on its own, then a boost need NOT mix them, A.V is NOT")
say("    invariant, and 4139's problem returns in full.")
say("    So the amendment needs one more thing, and it is derivable rather")
say("    than a picture question: SHOW THAT THE A3'/AP-4 TRANSPORT MIXES A_i")
say("    AND V_i UNDER A BOOST AS ONE ANTISYMMETRIC RANK-2 OBJECT.")
say("    Until then this patch has shown what the structure MUST be for the")
say("    founder's answer to hold -- not that the amendment implements it.")

open("/tmp/4140_out.txt", "w").write("\n".join(out))
