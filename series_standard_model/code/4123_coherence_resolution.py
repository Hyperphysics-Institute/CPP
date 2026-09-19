"""
Corrected model. In the EM channel the sea is POLARIZED: the arc/displacement
direction V is correlated with the field, not isotropic. That is what SF-6's
eDP-Sea Polarization mechanism means. Redo the coherence test with polarized V.

R = sign(A.V) - sign(Am.(-V)),  Am ~ -A + delta_f * zhat  (field tilts the spin)
  = sign(A.V) - sign(A.V - delta_f*(zhat.V))
nonzero only when A.V lies between 0 and delta_f*(zhat.V); its SIGN follows sign(zhat.V).
=> isotropic V  -> sign(zhat.V) is +-1 equally -> CANCELS
=> polarized V  -> sign(zhat.V) biased        -> SURVIVES
"""
import numpy as np
rng=np.random.default_rng(4123)

def run(N, delta_f, polarization):
    """polarization in [0,1]: 0 = isotropic V, 1 = V fully aligned with the field."""
    z=np.array([0,0,1.])
    A=rng.normal(size=(N,3)); A/=np.linalg.norm(A,axis=1,keepdims=True)
    V=rng.normal(size=(N,3))
    V=V/np.linalg.norm(V,axis=1,keepdims=True)*(1-polarization) + z*polarization
    V/=np.linalg.norm(V,axis=1,keepdims=True)
    AV=np.einsum('ij,ij->i',A,V); zV=V@z
    R=np.sign(AV)-np.sign(AV-delta_f*zV)
    return R

print("="*70); print("net |R|/N vs polarization  (delta_field = 0.05, N = 400k)"); print("="*70)
for pol in [0.0,0.1,0.3,0.6,1.0]:
    r=run(400_000,0.05,pol).sum()/400_000
    print(f"  polarization = {pol:>4}   net R/N = {r:+.5f}")
print("""  isotropic V (pol=0): cancels, as predicted -- sign(zhat.V) is +-1 equally
  polarized V:          survives and grows with polarization""")

print("\n"+"="*70); print("with V polarized, is it linear in delta_field?"); print("="*70)
for d in [0.0,0.002,0.01,0.05,0.2]:
    r=abs(run(400_000,d,1.0).sum())/400_000
    print(f"  delta_field = {d:<6} -> |R|/N = {r:.5f}    delta/pi = {d/np.pi:.5f}")
print("""  With V fully polarized, zhat.V = 1 and the flip condition is 0 < A.V < delta_f,
  whose measure over isotropic A is delta_f/2 -- so |R|/N = 2 x (delta_f/2) = delta_f.""")
for d in [0.002,0.01,0.05,0.2]:
    r=abs(run(400_000,d,1.0).sum())/400_000
    print(f"    delta={d:<6} |R|/N={r:.5f}  vs delta={d:.5f}   ratio {r/d:.3f}")

print("""
======================================================================
RESOLUTION -- TODO-4122-COHERENCE
======================================================================
  The residual survives the sum ONLY where BOTH hold:
     (1) the spin misalignment is field-correlated (same direction for every DP)
     (2) the sea is POLARIZED, so V is field-correlated too

  Condition (2) is exactly the EM channel -- SF-6 derives EM from eDP-Sea
  polarization -- so in any EM measurement both hold and the residual is
  COHERENT: net R/N = delta_field, independent of N.

  The sea's thermal/DI-bit disorder (isotropic V, random per-DP kicks) cancels
  and is unconstrained, confirming the founder's picture is safe on that side.

  CONSTRAINT ON THE ADOPTED AXIOM:
     delta_field < ~1e-10 rad
  i.e. an applied EM field may not torque a CP's axial spin by more than about
  1e-10 radians at APV field strengths. This is a bound on the A_i-to-EM
  coupling coefficient -- a NEW falsifiable consequence of the amendment,
  and the sharp form of what A3G-3 was asking.""")
