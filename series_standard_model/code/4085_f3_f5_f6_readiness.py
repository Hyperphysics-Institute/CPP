"""4085 (EW lane) -- the remaining panel-readiness filters: F3 (strong stays P-even), F6 (CPT), F5 (CP).
F6 turns out to FORCE the polarity clause that 4072 left optional.

M1  TRANSFORMATION PROPERTIES of the helicity bit b = sign(omega . v):
      P: omega axial (unchanged), v polar (flips)   => b flips        -> P-ODD
      C: charge conjugation does not act on space   => b unchanged    -> C-EVEN
      T: omega flips, v flips                       => b unchanged    -> T-EVEN
M2  CPT CONSEQUENCE. A term LINEAR in b is P-odd, C-even, T-even, hence CPT-ODD. In a CPT-invariant theory
    that is forbidden ON ITS OWN. It is allowed only if the coefficient is itself C-odd -- i.e. if the
    sign FLIPS WITH POLARITY. So the polarity clause drafted at 4072 (and left "open whether necessary")
    is NOT optional: CPT REQUIRES it.
M3  WITH the polarity clause: P violated, C violated, CP conserved, CPT conserved. Verified as a table.
    => F5 stands: chi4 conserves CP EXACTLY, so the small observed CP violation needs a separate source.
       Candidate: the corpus's own T-odd sign(delta) (TARROW-1/2, W3). NOT circular in the way K4 was
       (4082), because delta is independently motivated and does not presuppose baryogenesis.
       Magnitudes checked below -- and they do not obviously work.
M4  F3 (strong sector). The requirement is the same shape as F2 (4075): the strong response must be EVEN
    in b. Stated honestly, that is a CLAUSE, not a result -- unless something distinguishes the weak
    interaction structurally. Candidate distinction recorded, untested.
"""
import numpy as np
phi=(1+5**.5)/2

print("M1  transformation properties of b = sign(omega . v)")
rows=[("omega (angular momentum, axial)", +1, +1, -1),
      ("v (velocity, polar)",             -1, +1, -1),
      ("b = sign(omega . v)",             -1, +1, +1)]
print(f"    {'quantity':34s}  P     C     T    CPT")
for name,p,c,t in rows:
    print(f"    {name:34s} {p:+d}    {c:+d}    {t:+d}    {p*c*t:+d}")
b_cpt = -1*1*1
print(f"    => b is P-ODD, C-EVEN, T-EVEN, and therefore CPT-{'ODD' if b_cpt<0 else 'EVEN'}.")
assert b_cpt == -1

print("\nM2  CPT consequence: is a bare linear term allowed?")
print("    a term  c * b  with c a constant is CPT-odd  => FORBIDDEN in a CPT-invariant theory.")
print("    it is allowed only if c is itself C-ODD, i.e. the sign FLIPS WITH POLARITY.")
print("    => the polarity clause (4072 section 3, left 'open whether necessary') is REQUIRED BY CPT.")

print("\nM3  the full table with the polarity clause  (c = kappa * polarity)")
def obeys(pol, hand): return pol == hand
base=(+1,+1)
for name, op in (("P ", lambda p,h:(p,-h)), ("C ", lambda p,h:(-p,h)),
                 ("CP", lambda p,h:(-p,-h)), ("CPT", lambda p,h:(-p,-h))):
    q=op(*base)
    print(f"    under {name}: polarity {q[0]:+d}, hand {q[1]:+d} -> rule {'HOLDS' if obeys(*q) else 'BROKEN'}")
print("    => P violated, C violated, CP conserved, CPT conserved. Matches the Standard Model's pattern.")

print("\nM4  F5: chi4 conserves CP exactly, so the observed CP violation needs another source.")
print("    Candidate: the corpus's T-odd sign(delta). Magnitude check:")
d=phi**-3
for label, val in (("delta = phi^-3", d), ("delta^3 (TARROW-2 current onset)", d**3), ("delta^9", d**9)):
    print(f"      {label:34s} = {val:.3e}")
print(f"      observed Jarlskog invariant J        = 3.08e-05")
print("    => delta^3 = 1.3e-02 is ~400x too large; delta^9 = 2.3e-06 is ~13x too small. Neither lands.")
print("    HONEST STATUS: a source EXISTS in the corpus and is not circular (unlike K4, 4082), but no")
print("    power of delta reproduces J. F5 is NOT satisfied -- it is an open quantitative problem.")

print("\nM5  F3 (strong sector stays P-even)")
print("    Requirement is the same shape as F2 (4075): the strong response must be EVEN in b.")
print("    As stated that is a CLAUSE, not a result: nothing yet explains why ONLY the weak response is")
print("    linear. Candidate structural distinction, UNTESTED: the W-bracelet mechanism CAPTURES a CP at")
print("    its centroid (SF-2 section 5) and so reads that CP's own register; EM and the strong force act")
print("    through DP-sea polarisation and exchange, which read displacement MAGNITUDES, not the captured")
print("    particle's bit. If that distinction holds, linearity in b follows from capture and F3/F2 stop")
print("    being clauses. Registered as the most valuable open item.")
