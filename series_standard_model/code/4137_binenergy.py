#!/usr/bin/env python3
"""
Patch 4137 — TODO-4136-BINENERGY. Does whatever READS b contribute to a
structure's internal energy, and at what order?

WHY IT MATTERS
--------------
4136 closed three of four routes by which the A_i channel could break R-F3-ISO.
The fourth -- an A.V term (= b itself) in the internal energy -- is P-odd and
T-EVEN, so T-parity cannot touch it, and excluding it by assumption is circular
because such a term IS hadronic parity violation. This question sits upstream of
F3, A3G-2 and A3G-3 alike.

THE STRUCTURAL STEP (CPP-internal, and CONDITIONAL -- see the caveat)
---------------------------------------------------------------------
The corpus's own filter table (chirality_axiom_maturation 2aa) says only ONE
channel reads b linearly:

    weak   (W bracelet)  free partner       <b> != 0   LINEAR in b     P-odd
    EM     (sea exchange) confined partner  <b> = 0    magnitude only  P-even
    strong (cage hop)     confined partner  <b> = 0    cage SSV dom.   P-even

If that is right, a P-odd term in a NUCLEON's internal energy cannot arise
from the strong or EM channel at all: it must pass through bracelet formation.
That routes it through the weak scale instead of leaving it free.

THE SIZE (imported, NOT derived -- M_W is calibrated in CPP via eta_W, SF-2)
"""
import numpy as np

out = []
def say(s=""):
    print(s); out.append(s)

G_F = 1.1663787e-5          # GeV^-2, PDG
m_pi = 0.13957              # GeV
f_pi = 0.1302               # GeV
M_N = 0.9389                # GeV
W_MAG = 1.1654              # |W| for the SU(6) proton, Patch 4134
PV_BOUND = 1e-7             # observed hadronic parity violation scale

say("F1  the weak-channel suppression, the only channel that reads b")
for label, scale in (("G_F * m_pi^2", m_pi), ("G_F * f_pi^2", f_pi),
                     ("G_F * m_N^2 ", M_N)):
    say(f"    {label} = {G_F * scale**2:.3e}")
say("    The first two are the textbook hadronic-PV scale; the third is the")
say("    same estimate with the nucleon mass and is the conservative end.")
say()

say("F2  against the bound R-F3-ISO needs (Patch 4136)")
eps_bound = PV_BOUND / W_MAG
say(f"    4136: B_tot = eps * |W| = eps * {W_MAG:.4f} <= {PV_BOUND:.0e}")
say(f"          => eps <= {eps_bound:.2e}")
naive = G_F * m_pi ** 2
say(f"    weak-channel estimate for eps: {naive:.2e}")
say(f"    ratio estimate/bound = {naive / eps_bound:.2f}")
say()
say("    READ THIS HONESTLY: the naive weak-channel size runs a FACTOR ~2.6")
say("    ABOVE the bound, not comfortably below it. With O(1) coefficients")
say("    unknown on both sides this is agreement at order of magnitude, but it")
say("    is NOT slack. It says the unknown coefficient cannot be much larger")
say("    than 1 -- a real, if weak, constraint -- and it leaves no room for a")
say("    CPP-extra P-odd contribution on top of the weak admixture, which is")
say("    already what accounts for the observed hadronic PV.")
say()

say("F3  is the 1e-7 a CPP prediction? NO -- checked, and it is not.")
say("    SF-2 derives the RATIO m_Z/m_W = 1.1405 at zero parameters against")
say("    1.1344 observed, but m_W itself is CALIBRATED via eta_W (SF-2 Table,")
say("    'm_W = 80.377 GeV (calibrated via eta_W)'). The weak SCALE is an input")
say("    to CPP, not an output. So the suppression size is IMPORTED.")
say("    What is CPP-internal is the STRUCTURAL step: that only the bracelet")
say("    channel reads b, so the P-odd energy term is routed through the weak")
say("    scale rather than being free. That is the whole of the contribution.")
say()

say("F4  the caveat that limits this result, stated up front")
say("    The filter table is NOT established corpus. Its own status line reads")
say("    'Status: CONDITIONAL' and records the founder's response as 'I have no")
say("    explanation' (session 233). It is a worker proposal. So F1-F3 inherit")
say("    that conditionality: BINENERGY is answered CONDITIONAL ON the filter")
say("    table, not outright. Nothing here upgrades the table.")
say()

say("VERDICT")
say("  BINENERGY is answered conditionally, and the answer is YES-but-routed:")
say("  b DOES reach the internal energy, but -- if the filter table holds --")
say("  only through the one channel that reads it, so the P-odd term carries")
say("  the weak-scale suppression rather than being unconstrained. Size lands")
say("  at ~2e-7, the observed hadronic-PV scale, which is where it must land")
say("  and which leaves NO room for an additional CPP contribution.")
say()
say("  WHAT THIS IS WORTH: it converts route 4 from 'unbounded and circular'")
say("  to 'bounded by a channel argument, conditional on the filter table'.")
say("  WHAT IT IS NOT: a derivation. The 1e-7 is imported through a calibrated")
say("  m_W, the O(1) coefficient is unknown, and the estimate sits a factor")
say("  ~2.6 on the WRONG side of the bound it has to respect.")
say("  R-F3-ISO is therefore NOT independently secured, and F3 continues to")
say("  rest on the same empirical bound it is trying to explain.")

open("/tmp/4137_out.txt", "w").write("\n".join(out))
