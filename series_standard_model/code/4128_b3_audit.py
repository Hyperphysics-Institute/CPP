"""
TODO-4127-B3AUDIT: does B3 support the weight A3G-8 put on it?
"""
print("="*70); print("WHAT B3 ACTUALLY SAYS (Patch 4076, verbatim)"); print("="*70)
print("""  'Let a process rate be R(b). Parity violation appears in observables IFF R
   depends on b linearly. An even response (R ~ b^2) gives asymmetry exactly 0
   even when b is P-odd... The response must be odd -- linear -- in the spin bit.'

  READ CAREFULLY: B3 is a NECESSARY CONDITION for parity violation. It says
  'to get V-A, the PARITY-VIOLATING response must be odd in b'.
  It does NOT say 'no interaction may read anything else about A'.""")

print("\n"+"="*70); print("WHAT A3G-8 NEEDED IT TO SAY"); print("="*70)
print("""  A3G-8 (Patch 4127) concluded: 'the only function of A that any interaction
  reads is sign(A.V)', therefore same-b CPs are indistinguishable, therefore
  strict exclusion holds, therefore exactly two slots.

  That is a MUCH stronger claim than B3 licenses. B3 constrains the P-ODD
  sector only. It is silent on P-EVEN couplings.""")

print("\n"+"="*70); print("AND A P-EVEN COUPLING THAT READS A ALREADY EXISTS"); print("="*70)
print("""  Patch 4125 (A3G-2) itself established that A1.A2 is P-EVEN, T-EVEN and is
  ORDINARY MAGNETIC DIPOLE-DIPOLE -- a real coupling the amendment supplies
  the carrier for. A1.A2 depends on the DIRECTIONS of A1 and A2, not on
  sign(A.V).

  So two CPs sharing b but differing in A ARE distinguishable -- by their
  mutual magnetic dipole interaction. They are NOT in the same quantum state.
  Strict exclusion does not apply to them.

  -> A3G-8's resolution FAILS. The two-slot result is NOT recovered from the
     amendment as written.""")

print("\n"+"="*70); print("WHY REAL QM GETS TWO SLOTS AND THIS DOES NOT"); print("="*70)
print("""  In quantum mechanics an electron's spin direction is continuous, yet Pauli
  gives exactly 2 states per orbital -- because spin-1/2 lives in a
  2-DIMENSIONAL HILBERT SPACE. The continuum of directions is a continuum of
  SUPERPOSITIONS of two basis states, not a continuum of independent states.

  A_i as the amendment states it is a CLASSICAL axial 3-vector. A classical
  3-vector direction has a CONTINUUM of independent values, not two.

    classical axial vector : states = S^2, a continuum
    spin-1/2              : states = 2 (directions are superpositions)

  These are different objects, and only the second gives Pauli doubling.""")

print("""
======================================================================
B3AUDIT VERDICT -- the gap is real, and A3G-8 must be withdrawn
======================================================================
  B3 does NOT carry A3G-8. It constrains the parity-violating sector; the
  two-slot argument needed a prohibition on ALL other readings of A, which
  B3 never gave and which A3G-2 actively contradicts.

  A3G-8 (Patch 4127): WITHDRAWN. The two-slot result does not follow from the
  amendment as written.

  WHAT THE AMENDMENT NEEDS: A_i must be QUANTIZED -- a two-state spin-1/2
  object, not a classical axial vector. That is an ADDITIONAL requirement not
  presently in A1'/A3'/AP-4, and it must be added for Pauli doubling to hold.

  EFFECT ON A3G-2 AND A3G-3: those used B3 only for the T-PARITY argument
  (a T-even carrier cannot source a T-odd term at linear order), which IS
  what B3 licenses. They STAND. The concentration flagged at 4127 was real,
  but it broke in exactly one of the three places -- the one where B3 was
  being stretched beyond its statement.""")
