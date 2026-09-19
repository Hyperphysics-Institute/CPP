"""
Founder correction (4122): DP-CAL-1 is a STRONG BIAS, not an exact constraint.
"The helical bit's orientation will be most strongly biased antiparallel by its pair,
 but it will not be exact because of the influence of the DI-bits from the DP Sea."
"vacuum-state magnetism should not be exactly zero on a finite scale because of charge motion"

So: antiparallel up to a sea-induced misalignment delta. Recompute F2 as a BOUNDED
residual rather than an exact cancellation, and invert the EM-parity bound to constrain delta.
"""
import numpy as np
rng=np.random.default_rng(4122)

def residual(delta, N=400_000):
    """Fraction of DPs whose two helicity bits FAIL to cancel, given misalignment delta."""
    A  = rng.normal(size=(N,3)); A/=np.linalg.norm(A,axis=1,keepdims=True)   # CP+ spin
    V  = rng.normal(size=(N,3)); V/=np.linalg.norm(V,axis=1,keepdims=True)   # arc direction
    # CP- spin: antiparallel to A, perturbed by a random kick of angular size delta
    kick = rng.normal(size=(N,3))*delta
    Am = -A + kick
    Am /= np.linalg.norm(Am,axis=1,keepdims=True)
    bp = np.sign(A@np.array([1,0,0])*0 + np.einsum('ij,ij->i',A,V))
    bm = np.sign(np.einsum('ij,ij->i',Am,-V))     # arcs opposed (forced, Patch 4107)
    return np.mean(bp!=bm)

print("="*66)
print("F2 residual vs sea-induced misalignment  (arcs opposed, spins ~antiparallel)")
print("="*66)
print(f"{'delta (rad)':>12} {'fraction b+ != b-':>20} {'~ delta/pi':>12}")
for d in [0.0, 1e-4, 1e-3, 1e-2, 0.1, 0.3]:
    f=residual(d)
    print(f"{d:>12.0e} {f:>20.2e} {d/np.pi:>12.2e}")
print("""
  The residual scales LINEARLY in delta, as delta/pi -- a misalignment only flips a
  bit when A.V sits within delta of zero, i.e. when the spin is nearly perpendicular
  to the arc direction. That measure is delta/pi.""")

print("\n"+"="*66)
print("INVERT: what misalignment does the EM-parity bound permit?")
print("="*66)
print("""  Intrinsic EM parity violation must sit below ~1e-10 (atomic parity violation is
  observed but fully accounted for by Z-exchange to ~0.3% of the SM value, and the
  weak contribution is itself ~1e-7 of the EM amplitude).

  Per-DP residual ~ delta/pi. Across N sea DPs contributing incoherently the net
  parity-violating response scales as (delta/pi)/sqrt(N), so the bound is WEAKER
  than the per-DP figure by sqrt(N). Taking the conservative coherent case:""")
bound=1e-10
print(f"    coherent   : delta < pi * {bound:.0e} = {np.pi*bound:.2e} rad")
for N in [1e12,1e24]:
    print(f"    incoherent, N = {N:.0e} : delta < pi * {bound:.0e} * sqrt(N) = {np.pi*bound*np.sqrt(N):.2e} rad"
          + ("  (exceeds pi -> UNCONSTRAINED)" if np.pi*bound*np.sqrt(N)>np.pi else ""))

print("""
VERDICT
  The founder's correction REPLACES an exact cancellation with a bounded one, and
  the bound is quantitative and falsifiable:

     per-DP misalignment  delta  <  ~3e-10 rad   (coherent, conservative)
     -- and far weaker, effectively unconstrained, if sea DPs contribute incoherently.

  So F2 does NOT require exact antiparallelism. It requires the sea-induced
  misalignment to be small in the coherent channel, OR incoherence across the sea.
  WHICH of those applies is now the open question, and it is decidable.""")
