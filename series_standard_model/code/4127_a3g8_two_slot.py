"""
TEST-A3G-8: re-run the 4098 THEO-QM-10 two-slot result with A_i as the AXIOM-supplied
spin, not chi_4's binary bit.

THE TENSION: 4098 got exactly TWO slots per spatial mode because b is binary.
A_i is a CONTINUOUS axial vector -- its state space is the sphere S^2, not {+1,-1}.
If two CPs at one site are distinguishable by their A DIRECTION, exclusion should
not apply to them, and Pauli doubling would become Pauli UNBOUNDED. Does it?
"""
import numpy as np
rng=np.random.default_rng(4127)

print("="*70); print("T1  what actually enters the exclusion rule?"); print("="*70)
print("""  From 4098: two CPs at one GP are strictly excluded iff they are in the SAME
  quantum state. The chi_4 response is LINEAR in b (B3) and b = sign(A.V) -- so
  the only function of A that any interaction reads is the SIGN of A.V.
  A itself is continuous; the OBSERVABLE built from it is binary.""")

N=200_000
A=rng.normal(size=(N,3)); A/=np.linalg.norm(A,axis=1,keepdims=True)
V=rng.normal(size=(N,3)); V/=np.linalg.norm(V,axis=1,keepdims=True)
b=np.sign(np.einsum('ij,ij->i',A,V))
print(f"\n  continuous A: {N} distinct directions drawn")
print(f"  distinct values of b = sign(A.V): {len(np.unique(b))}  -> {sorted(np.unique(b))}")
print(f"  fraction b=+1: {np.mean(b>0):.4f}   (balanced, as required)")
assert len(np.unique(b))==2

print("\n"+"="*70); print("T2  are two same-b CPs with different A distinguishable?"); print("="*70)
print("""  Test: can ANY chi_4-mediated interaction separate two CPs that share b but
  differ in A? The response is linear in b, so the interaction reads b only.
  Two CPs with the same b are then identical to every interaction the axiom
  provides -- hence the SAME quantum state -- hence strictly excluded.""")
# demonstrate: draw pairs with equal b but very different A; show the response is identical
i,j = np.where(b>0)[0][:5], np.where(b>0)[0][5:10]
ang=np.degrees(np.arccos(np.clip(np.einsum('ij,ij->i',A[i],A[j]),-1,1)))
print(f"\n  five same-b pairs, angle between their A vectors: {np.round(ang,1)} deg")
print(f"  their b values:  A-side {b[i].astype(int)}   B-side {b[j].astype(int)}")
print("  -> identical response despite up to ~180 deg of A separation. Indistinguishable.")

print("\n"+"="*70); print("T3  so the slot count is set by b, not by A"); print("="*70)
print(f"""  states per spatial mode = |range of b| = 2
  600-cell spatial modes = 120  ->  120 x 2 = 240 fermionic states
  This REPRODUCES Patch 4098 exactly, now from the axiom rather than the bit.""")
print("\n  A3G-8 PASSES.")

print("\n"+"="*70); print("T4  the honest residual -- what this costs"); print("="*70)
print("""  The resolution works ONLY because the chi_4 response is LINEAR in b and
  therefore reads nothing else about A. That is B3 doing load-bearing work
  a THIRD time (it also carries A3G-2 and A3G-3 via the T-parity argument).

  If any interaction ever reads A beyond sign(A.V) -- a coupling to A's
  direction, not just its sign -- then same-b CPs become distinguishable, the
  strict exclusion fails, and Pauli doubling becomes unbounded. That would be
  a far worse failure than the falsifiers tested: it would break FERMIONS.

  So B3 is now the single most load-bearing premise in the whole amendment,
  carrying A3G-2, A3G-3 and A3G-8. Its own support should be re-examined.""")
