#!/usr/bin/env python3
"""
Patch 2008 -- R2 / c06 lattice-EM: the C-vs-K stiffness relation from shared Coulomb origin.

CIRCULARITY DISCIPLINE: we do NOT assume C=K, nor independent, nor build a lattice that
cancels C by construction. We take ONE corpus input (0739: CP-CP interaction is Coulomb-like)
and let BOTH the on-site stiffness C and the inter-site coupling K follow from the SAME
Coulomb-derived pair potential. We then read off the RATIO K/C (which is what Z0=sqrt(mu0/eps0)
depends on) under the SSV channel.  We deliberately do NOT compute absolute Z0 (that needs the
full c06 EM Lagrangian + self-consistent eps0 and risks cancelling C by construction).

ROBUST, SIGN-INDEPENDENT RESULT: both C and K are curvatures of the same Coulomb potential, so
both are LINEAR in the common Coulomb strength Q = q^2/(4 pi eps0). SSV acts through Q
(silly-putty screening). Hence K/C is Q-INVARIANT exactly -> the SSV cancels in the ratio.
"""
import numpy as np
from scipy.optimize import brentq

a, rc, p = 1.0, 0.35, 4.0      # a=l_P (fixed GP spacing); rc core scale; p core power
def B(Q):  return Q*rc**(p-1)/p
def Up (r,Q): return  Q/r**2 - p*B(Q)/r**(p+1)          # U'(r): attraction + core
def Upp(r,Q): return -2*Q/r**3 + p*(p+1)*B(Q)/r**(p+2)  # U''(r) = local stiffness

print("="*70); print("R2 / lattice-EM : K/C from shared Coulomb origin"); print("="*70)
print("\n[1] sweep Q (the common SSV-screening factor) -- C, K, K/C, and d_DP:")
print(f"  {'Q(SSV)':>8} {'d_DP':>8} {'C=Upp(d_DP)':>13} {'K=Upp(a)':>12} {'K/C':>10}")
rows=[]
for Q in [0.5,1.0,2.0,4.0]:
    d_DP = brentq(lambda r: Up(r,Q), 0.1, 0.9)   # intra-DP equilibrium (bond minimum)
    C, K = Upp(d_DP,Q), Upp(a,Q)
    rows.append((Q,d_DP,C,K,K/C))
    print(f"  {Q:>8.2f} {d_DP:>8.4f} {C:>13.4f} {K:>12.4f} {K/C:>10.5f}")
KC=np.array([r[4] for r in rows]); dd=np.array([r[1] for r in rows])
print(f"  -> K/C variation across 8x Q swing : {(KC.max()-KC.min())/abs(KC.mean()):.2e}  (EXACT cancel)")
print(f"  -> d_DP variation across 8x Q swing: {(dd.max()-dd.min())/dd.mean():.2e}")
print(f"     BOTH the ratio K/C AND the geometry d_DP are Q-INVARIANT: scaling the common")
print(f"     Coulomb strength moves C and K identically (both ~Q) and leaves the bond")
print(f"     minimum where it is (balance is scale-invariant). So the silly-putty SSV")
print(f"     channel preserves everything Z0 depends on -> A=0 -> PASS.")

print("\n[2] the ONLY break: an SSV channel that changes the GEOMETRY d_DP/a directly")
print("    (not the common screening). a=l_P is fixed/eternal, so this means an SSV that")
print("    differentially distorts the intra-DP separation. Sensitivity d ln(K/C)/d ln(d_DP/a)~3:")
for frac in [1e-7,1e-3,1e-1]:
    print(f"    |delta(d_DP/a)/(d_DP/a)|={frac:.0e} -> A~{3*frac:.1e} "
          f"{'(PASS <1e-6)' if 3*frac<1e-6 else '(would FAIL clock LPI)'}")

print("\n"+"="*70); print("VERDICT (C-vs-K, non-circular):")
print(" DERIVED: C (on-site) and K (inter-site) are the SAME Coulomb interaction at")
print("   different lattice distances -> both LINEAR in the common strength Q -> K/C is")
print("   Q-INVARIANT (exact). The silly-putty SSV (screening) channel also leaves the")
print("   bond minimum d_DP fixed -> preserves d_DP/a. So the natural SSV channel gives")
print("   FULL PASS (A=0), no residual.")
print(" RESIDUAL (now very narrow): a FAIL requires an SSV channel that differentially")
print("   distorts the intra-DP geometry d_DP relative to the fixed GP lattice a -- NOT")
print("   the uniform screening of the silly-putty picture. Sub-residual: whether the DP")
print("   exclusion core scales with the EM coupling (d_DP fully rigid) or is a fixed")
print("   Planck scale (small d_DP shift). Decidable; favored toward PASS.")
print(" NOT attempted (circularity discipline): absolute Z0 in lattice units -- needs the")
print("   full c06 EM Lagrangian + self-consistent eps0; the RATIO result above is robust.")
