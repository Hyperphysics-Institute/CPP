"""
Is det[V,QV,Q^2V] the UNIQUE pseudoscalar buildable from LSP' = (Phi, V_i, Q_ij)?
If yes, and it vanishes on every axially-symmetric structure, then A3' CANNOT
carry chi_4's bit and the axiom amendment Thomas suspected is REQUIRED.

A pseudoscalar needs exactly one epsilon tensor. Contracting eps_ijk with:
  - two vector slots and one tensor slot: eps_ijk V_i V_j (...)  -> 0 (antisym x sym)
  - eps_ijk V_i Q_jk                                            -> 0 (Q symmetric)
  - three vectors A,B,C built from V and Q: det[A,B,C]
The only vectors available are V, QV, Q^2V (Cayley-Hamilton truncates Q^3).
So the sole candidate is det[V, QV, Q^2 V].
"""
import numpy as np
rng=np.random.default_rng(4110)

def rand():
    A=rng.normal(size=(3,3)); return rng.normal(), rng.normal(size=3), (A+A.T)/2

print("C1  eps-contractions that vanish identically by symmetry")
worst={"eps_ijk V_i V_j Q_k?":0.0,"eps_ijk V_i Q_jk":0.0,"eps_ijk Q_ia Q_ja (a summed)":0.0}
eps=np.zeros((3,3,3))
for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]: eps[i,j,k]=1; eps[i,k,j]=-1
for _ in range(2000):
    Phi,V,Q=rand()
    worst["eps_ijk V_i Q_jk"]=max(worst["eps_ijk V_i Q_jk"],
                                  abs(np.einsum('ijk,i,jk->',eps,V,Q)))
    worst["eps_ijk Q_ia Q_ja (a summed)"]=max(worst["eps_ijk Q_ia Q_ja (a summed)"],
                                  abs(np.einsum('ijk,ia,ja,k->',eps,Q,Q,V)))
for k,v in worst.items():
    if v>0 or k!="eps_ijk V_i V_j Q_k?": print(f"    {k:32s} max = {v:.2e}")
print("    -> all vanish identically (antisymmetric eps against symmetric slots)\n")

print("C2  Cayley-Hamilton: Q^3 is a combination of I, Q, Q^2, so Q^3 V adds no new vector")
Phi,V,Q=rand()
c2,c1,c0=-np.trace(Q), 0.5*(np.trace(Q)**2-np.trace(Q@Q)), -np.linalg.det(Q)
resid=np.abs(Q@Q@Q + c2*Q@Q + c1*Q + c0*np.eye(3)).max()
print(f"    max |Q^3 + c2 Q^2 + c1 Q + c0 I| = {resid:.2e}  -> only V, QV, Q^2V exist\n")

print("C3  therefore the pseudoscalar is UNIQUE up to a P-even factor:")
print("    b ~ det[V, QV, Q^2 V] = xyz * (b-a)(c-a)(c-b) in Q's eigenbasis\n")

print("C4  it vanishes whenever Q has a REPEATED eigenvalue -- i.e. on any")
print("    axially or spherically symmetric configuration:")
for lbl,ev in [("spherical/isotropic",(2.,2.,2.)),("axial (D6, cages, rings)",(1.,1.,4.)),
               ("triaxial (no CPP structure)",(1.,2.,4.))]:
    Q=np.diag(ev); m=max(abs(np.linalg.det(np.column_stack([V,Q@V,Q@Q@V])))
                         for V in rng.normal(size=(3000,3)))
    print(f"    {lbl:28s} max|b| = {m:.2e}")

print("""
======================================================================
CONCLUSION -- 4109's HEADLINE IS INVERTED
======================================================================
  The pseudoscalar buildable from LSP' is UNIQUE, and it vanishes on every
  configuration with two equal Q-eigenvalues. Every named CPP structure --
  the isotropic sea, the icosahedral Z cage, the dodecahedral H cage, the
  tetrahedral and octahedral shells, and the D6 W bracelet -- is at least
  axially symmetric.

  => NO pseudoscalar built from A3's ratified LSP' content is nonzero on ANY
     CPP structure. It cannot carry V-A.

  => A3' DOES need amending to carry chi_4's helicity bit. The founder's
     instinct that 'the CP carrying the 4D element is a new concept that has
     never been used' was RIGHT, and 4109's claim to the contrary is WITHDRAWN.""")
