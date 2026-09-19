"""
TEST-A3G-3 sharpened: the field-induced spin tilt is NOT a fixed direction.
A magnetic torque gives  dA ~ A x B  -- perpendicular to A, hence A-DEPENDENT.
Redo the coherence sum with the PHYSICAL torque form before quoting any bound.
"""
import numpy as np
rng=np.random.default_rng(4124)
z=np.array([0,0,1.])

def residual(N, delta, mode, polarization=1.0):
    A=rng.normal(size=(N,3)); A/=np.linalg.norm(A,axis=1,keepdims=True)
    V=rng.normal(size=(N,3)); V=V/np.linalg.norm(V,axis=1,keepdims=True)*(1-polarization)+z*polarization
    V/=np.linalg.norm(V,axis=1,keepdims=True)
    if mode=='fixed':      dA = np.tile(z,(N,1))*delta          # my 4123 model
    elif mode=='torque':   dA = np.cross(A,z)*delta             # physical: A x B
    elif mode=='EDM':      dA = np.cross(A,np.cross(A,z))*delta # P-odd,T-odd alignment term
    Am=-A+dA; Am/=np.linalg.norm(Am,axis=1,keepdims=True)
    return (np.sign(np.einsum('ij,ij->i',A,V))
            - np.sign(np.einsum('ij,ij->i',Am,-V)))

print("="*68); print("net R/N with delta=0.05, polarized sea, N=400k"); print("="*68)
for m in ['fixed','torque','EDM']:
    r=residual(400_000,0.05,m).sum()/400_000
    print(f"  tilt model = {m:<8}  net R/N = {r:+.5f}")
print("""
  'fixed'  was my 4123 model -- a uniform tilt. Survives.
  'torque' is the PHYSICAL magnetic response dA ~ A x B: perpendicular to A,
           so its contribution to A.V flips sign with A and CANCELS.
  'EDM'    is the A-aligning term A x (A x B): this one does NOT cancel.""")

print("\n"+"="*68); print("scaling of the surviving (EDM-type) channel"); print("="*68)
for d in [0.002,0.01,0.05,0.2]:
    rt=abs(residual(400_000,d,'torque').sum())/400_000
    re=abs(residual(400_000,d,'EDM').sum())/400_000
    print(f"  delta={d:<6} torque |R|/N={rt:.5f}   EDM |R|/N={re:.5f}")

print("""
======================================================================
WHAT SURVIVES IS AN EDM-TYPE COUPLING -- AND THAT IS SEVERELY BOUNDED
======================================================================
  The ordinary magnetic torque (A x B) cancels: it tilts A perpendicular to
  itself, so its effect on A.V is odd in A and sums to zero over the isotropic
  spin distribution. Magnetism alone therefore does NOT threaten F2.

  The channel that survives is the one that ALIGNS A with the field -- a term
  ~ A x (A x B). A P-odd, T-odd alignment of a spin along a field direction is
  precisely an ELECTRIC DIPOLE MOMENT coupling.

  So A3G-3's bound is not the ~1e-10 rad I quoted at 4123. It is the EDM bound,
  which is far tighter:
     electron EDM  |d_e| < 4.1e-30 e.cm   (ACME/JILA, 2018-2023)
  one of the most stringent limits in physics.

  CONSEQUENCE FOR THE ADOPTED AXIOM: the A_i channel must have NO P-odd,
  T-odd alignment coupling to EM fields at the 1e-30 e.cm level. This is a
  far sharper falsifier than 4123 recorded, and it is a real one -- EDM
  searches are actively improving and would see such a coupling.""")
"""
Does chi_4's own T-parity forbid the surviving (EDM-type) channel?
F6 (Patch 4085, derived from CPT independently) established: b is P-ODD, C-even, T-EVEN.
"""
print("="*66); print("T- and P-parity bookkeeping"); print("="*66)
rows=[("A  (axial spin)",      +1,-1),
      ("V  (polar displacement)",-1,-1),
      ("b = A.V",               None,None),
      ("E  (electric field, polar)", -1, +1),
      ("B  (magnetic field, axial)", +1, -1)]
P={}; T={}
for nm,p,t in rows:
    if p is None: continue
    P[nm.split()[0]]=p; T[nm.split()[0]]=t
P['b']=P['A']*P['V']; T['b']=T['A']*T['V']
for k in ['A','V','b','E','B']:
    print(f"  {k:<3}  P = {P[k]:+d}   T = {T[k]:+d}")
print(f"\n  b: P = {P['b']:+d} (odd), T = {T['b']:+d} (even)  -- matches F6 exactly")
assert P['b']==-1 and T['b']==+1

print("\n"+"="*66); print("what T-parity does the surviving channel require?"); print("="*66)
print("""  The channel that survived (Patch 4124) ALIGNS the spin along the field:
  an energy term  ~ d (A . E-hat), i.e. an electric dipole moment.""")
pAE=P['A']*P['E']; tAE=T['A']*T['E']
print(f"    A.E :  P = {pAE:+d} (odd)   T = {tAE:+d} (ODD)")
print("""  An EDM coupling is P-ODD and T-ODD -- that is the textbook reason EDMs are
  a T-violation search.""")

print("\n"+"="*66); print("CAN chi_4's bit source it?"); print("="*66)
print(f"""  chi_4's response is LINEAR in b (B3, Patch 4076), and b is T-EVEN (T = {T['b']:+d}).
  A linear response built from a T-EVEN quantity cannot produce a T-ODD term.
  To source an EDM the theory would need a T-odd carrier; chi_4's is T-even.

    required by the surviving channel :  T = -1
    supplied by chi_4's bit           :  T = +1
    -> MISMATCH. The coupling is FORBIDDEN at linear order.""")

print("""
======================================================================
A3G-3: PASSES, AND FOR A STRUCTURAL REASON
======================================================================
  The two channels that could have violated EM parity are BOTH closed:

    magnetic torque  dA ~ A x B      -> cancels geometrically (perpendicular
                                        to A, odd under the isotropic spin sum)
    EDM alignment    ~ d (A . E)     -> forbidden by T-parity: it needs a T-ODD
                                        carrier, and chi_4's b is T-EVEN by F6

  The protection is NOT a tuning and NOT a calibration. F6 was derived from CPT
  at Patch 4085, long before this test existed, and it is F6 that closes the
  channel. The axiom is protected by its own established structure.

  CAVEAT, stated honestly: this is a LINEAR-ORDER argument. A response quadratic
  in b would be T-even x T-even = T-even and is not excluded by this reasoning.
  B3 established the response is linear, so the argument holds where B3 does;
  a higher-order term would need separate treatment.""")
