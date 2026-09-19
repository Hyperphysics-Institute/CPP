"""
TEST-A3G-1 (falsifier): with A_i adopted, does the sea's summed axial channel vanish
IDENTICALLY, or only under DP-CAL-1's antiparallel assumption?

Fires the falsifier if the vacuum is magnetised. Reports honestly if the axiom needs
DP-CAL-1 to get a non-magnetised vacuum -- that is not a refutation, but it means the
axiom does NOT make the calibration dispensable.
"""
import numpy as np
rng=np.random.default_rng(4121)

def sea(N, antiparallel, isotropic=True):
    """N DPs. Each DP = two CPs. Return the summed axial channel |sum A|."""
    tot=np.zeros(3)
    axes = (rng.normal(size=(N,3)) if isotropic else np.tile([0,0,1.],(N,1)))
    axes/= np.linalg.norm(axes,axis=1,keepdims=True)
    for a in axes:
        if antiparallel: tot += a + (-a)      # spins oppose within the DP
        else:            tot += a + a          # spins align within the DP
    return np.linalg.norm(tot)

print("="*68); print("A3G-1  summed axial channel of the sea, |sum A|"); print("="*68)
print(f"{'N (DPs)':>10} {'antiparallel':>14} {'parallel+isotropic':>20} {'parallel+aligned':>18}")
for N in [100,10_000,1_000_000]:
    ap  = sea(N, True)
    pi  = sea(N, False, True)
    pa  = sea(N, False, False)
    print(f"{N:>10} {ap:>14.2e} {pi:>20.2f} {pa:>18.2f}")

print("""
READING
  antiparallel (DP-CAL-1)     : EXACTLY zero, every N, no fluctuation -- each DP
                                cancels internally before any sum is taken.
  parallel + isotropic        : mean zero but RMS grows as sqrt(N) -- the sea is
                                non-magnetic only ON AVERAGE, with fluctuations.
  parallel + aligned          : grows as N -- a ferromagnetic vacuum, excluded outright.""")

print("\n"+"="*68); print("does the sqrt(N) fluctuation matter? magnetisation DENSITY"); print("="*68)
for N in [1e6,1e12,1e24,1e60]:
    dens = np.sqrt(N)/N
    print(f"  N = {N:.0e}   |sum A|/N ~ 1/sqrt(N) = {dens:.2e}")
print("""  The DENSITY vanishes in the large-N limit, so a macroscopic region is
  non-magnetic on the parallel+isotropic branch too -- but only statistically,
  and the cancellation is not exact at any finite scale.""")

print("\n"+"="*68); print("VERDICT"); print("="*68)
print("""  FALSIFIER DOES NOT FIRE. The axiom does not force a magnetised vacuum:
  the aligned branch is excluded by the sea's own isotropy, and the isotropic
  branch gives vanishing magnetisation density.

  BUT THE HONEST FINDING IS A PARTIAL NEGATIVE, and it is the convenient
  branch that fails:
    Only DP-CAL-1 (antiparallel) gives EXACT, pointwise, fluctuation-free
    cancellation. Without it the vacuum is non-magnetic only ON AVERAGE.
    So the adopted axiom does NOT make DP-CAL-1 dispensable -- DP-CAL-1
    remains load-bearing for F2, exactly as it was at Patch 4107.

  I had written at 4111 that the axiom would let DP-CAL-1 'be derived or
  refuted instead of calibrated' (payoff 5). On this test that payoff does
  NOT materialise: the axiom supplies the referent but not the derivation.""")
