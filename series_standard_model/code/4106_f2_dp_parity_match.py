"""
F2 (EM stays P-even under chi_4) reduced to DP internal kinematics.

Inputs already fixed in the corpus:
  - A DP is "a bound pair of OPPOSITE-POLARITY CPs" (master_glossary).
  - F6 / polarity clause (Patch 4085): b is P-odd, C-even, T-even => CPT-odd,
    so any LINEAR response to b carries a C-ODD (polarity) coefficient.
    Response of a CP  ~  polarity x b,   b = sign(omega . v_arcs).
  - v_arcs is the DP ARC COHORT direction (founder ruling, Patch 4097).

So the DP's net chi_4 response is   R = (+q)*b_plus + (-q)*b_minus = q*(b_plus - b_minus).
R = 0  => EM stays P-even (F2 holds).
R != 0 => every sea DP carries an O(1) P-odd EM response => EM parity violation => chi_4 REFUTED.

Free structural choices, neither fixed by the corpus:
  (S) spins parallel (omega_+ = +omega_-) or antiparallel (omega_+ = -omega_-)
  (V) arc direction common/drift (v_+ = +v_-) or internal/orbital (v_+ = -v_-)
"""
import numpy as np, itertools
rng=np.random.default_rng(4106)

def R(spin_par, vel_common, trials=20000):
    """net DP response q*(b_+ - b_-), in units of q. Returns (mean |R|, max |R|)."""
    out=[]
    for _ in range(trials):
        w=rng.normal(size=3); w/=np.linalg.norm(w)      # omega_+
        v=rng.normal(size=3); v/=np.linalg.norm(v)      # v_+ (arc direction of + CP)
        w2 =  w if spin_par  else -w                     # omega_-
        v2 =  v if vel_common else -v                    # v_-
        bp, bm = np.sign(w@v), np.sign(w2@v2)
        out.append(bp-bm)
    out=np.abs(out)
    return out.mean(), out.max()

print("="*70)
print("F2 DECISION TABLE — net chi_4 response of one sea DP (units of q)")
print("="*70)
print(f"{'spins':>14} {'arc direction':>16} {'mean |R|':>10} {'max |R|':>9}   verdict")
rows=[]
for sp,spl in [(True,"parallel"),(False,"antiparallel")]:
    for vc,vcl in [(True,"common / drift"),(False,"internal / orbital")]:
        m,M=R(sp,vc)
        ok = (M==0.0)
        rows.append((spl,vcl,m,M,ok))
        print(f"{spl:>14} {vcl:>16} {m:10.4f} {M:9.1f}   "
              f"{'F2 HOLDS (exact cancellation)' if ok else 'chi_4 REFUTED by EM parity'}")

print("""
READING THE TABLE
  The two SURVIVING cases are the ones where b_+ = b_- :
      spins parallel     AND arc direction common
      spins antiparallel AND arc direction internal/orbital   (both signs flip, b is even)
  The two FATAL cases are where exactly one of the two flips.

  So F2 does NOT reduce to 'are DP spins paired?' alone. It reduces to a PARITY
  MATCH between two independent structural facts:

      F2 holds  <=>  (spin relative orientation) == (arc relative orientation)

  A mismatch is not a small correction. R = 2q for EVERY sea DP: an O(1) P-odd
  electromagnetic response from the vacuum itself.""")

print("="*70)
print("HOW BADLY WOULD A MISMATCH FAIL?")
print("="*70)
print("""  Atomic parity violation is observed and is accounted for by Z-exchange
  admixture to ~0.3% agreement with the SM. Intrinsic EM parity violation must
  therefore sit far below the weak contribution, itself ~1e-7 of the EM
  amplitude => intrinsic EM PV bound of order 1e-10 (relative).

  A mismatched DP sea gives R/q = 2 per DP -- order unity, not 1e-10.""")
print(f"  overshoot factor ~ {2/1e-10:.0e}")
print("""
  This is not a filter chi_4 can pass conditionally. On a mismatch chi_4 is
  REFUTED outright by electromagnetic parity conservation.""")

print("="*70)
print("CONTROL — is the cancellation exact, or only on average?")
print("="*70)
m,M=R(True,True,50000)
print(f"  parallel+common, 50000 random (omega, v):  mean |R| = {m:.1f}, max |R| = {M:.1f}")
print("  Exact and pointwise, not statistical: b_+ - b_- = 0 identically.")
print("  Same for antiparallel+internal (both arguments negate; sign() is even in that case).")
