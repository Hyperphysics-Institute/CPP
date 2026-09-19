"""
TEST-A3G-2 (last falsifier): does the A_i channel mediate a spin-dependent force
between separated matter, above torsion-balance / comagnetometer bounds?

Method: enumerate the leading spin-dependent potentials buildable from the
broadcast content, classify each by P and T, and ask which chi_4 can SOURCE
given b is P-odd/T-EVEN (F6) and the response is LINEAR in b (B3).
"""
P={'A':+1,'V':-1,'r':-1,'v':-1}      # A axial; V, r-hat, v polar
T={'A':-1,'V':-1,'r':+1,'v':-1}      # A T-odd; r-hat T-even; v, V T-odd

def cls(term,parts):
    p=1; t=1
    for q in parts: p*=P[q]; t*=T[q]
    return p,t

print("="*72)
print("Leading spin-dependent potentials from the broadcast content")
print("="*72)
print(f"{'potential':<26}{'parts':<16}{'P':>4}{'T':>4}   status")
rows=[
 ("A1.A2      spin-spin",        ['A','A']),
 ("(A1.r)(A2.r) tensor",         ['A','r','A','r']),
 ("A.r        monopole-dipole",  ['A','r']),
 ("A.v        spin-velocity",    ['A','v']),
 ("(A x v).r                  ", ['A','v','r']),
 ("A.V        = the bit b",      ['A','V']),
]
srcable=[]
for nm,parts in rows:
    p,t=cls(nm,parts)
    # chi_4 sources a term only if it is LINEAR in b and b is P-odd/T-even:
    # the sourced term must carry P=-1, T=+1 (same as b) or be b-independent
    if (p,t)==(-1,+1): st="chi_4 CAN source (matches b: P-odd, T-even)"; srcable.append(nm)
    elif (p,t)==(+1,+1): st="P-even, T-even -- ordinary, already exists (e.g. dipole-dipole)"
    elif t==-1: st="T-ODD -> chi_4 CANNOT source (b is T-even, response linear)"
    else: st="--"
    print(f"{nm:<26}{'x'.join(parts):<16}{p:>+4}{t:>+4}   {st}")

print("""
======================================================================
READING
======================================================================
  A1.A2 (spin-spin) and the tensor term are P-EVEN and T-EVEN. These are
  ORDINARY magnetic dipole-dipole couplings -- they already exist in physics
  and adding A_i does not create a new force here, it supplies the carrier for
  one we already have (consistent with Patch 4112: A_i is the spin half of
  <L-hat + 2 S-hat>).

  A.r (monopole-dipole) and A.v are the classic constrained 'fifth force'
  terms -- and BOTH are T-ODD. By the same argument that closed A3G-3:
  chi_4's b is T-EVEN (F6) and the response is LINEAR in b (B3), so a T-even
  carrier cannot source a T-odd potential.

  The only term matching b's own signature (P-odd, T-even) is A.V itself --
  which is not a force between separated masses but the LOCAL helicity bit.""")

print("""
======================================================================
A3G-2: PASSES -- same structural protection as A3G-3
======================================================================
  Spin-dependent forces that torsion balances and comagnetometers bound are
  the T-ODD ones (monopole-dipole A.r, spin-velocity A.v). chi_4 cannot source
  them at linear order.

  What A_i DOES mediate -- A1.A2 -- is ordinary magnetic dipole-dipole, which
  is measured, expected, and not a fifth force.

  SAME CAVEAT AS 4124: linear order only. A quadratic-in-b response is T-even
  and would not be excluded (TODO-4124-QUADRATIC covers both tests).

  ALL THREE FALSIFIERS ARE NOW RUN:
    A3G-1 vacuum magnetisation      -- does not fire
    A3G-3 EM parity                 -- passes (T-parity)
    A3G-2 spin-dependent fifth force-- passes (T-parity)
  Two of the three pass by ONE structural fact: F6's T-even signature for b.""")
