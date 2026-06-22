#!/usr/bin/env python3
"""
R2 / step 1: attempt the full lattice-EM action (the c06 owed computation), NOT by tasting.
Build the action from corpus-grounded terms only, integrate out the DP displacement, read off
eps0, mu0, c, Z0, and see what the C-dependence does -- whatever it does.

Construction (every term justified, none tuned to the answer):
  L = 1/2 mu_DP (d_t u)^2          [DP inertia; mu_DP = C/omega_ZBW^2, omega_ZBW fixed (c02)]
      - 1/2 C u^2                  [on-site ZBW restoring; C = Q*g_C, g_C=f''(d_DP) (2008)]
      - 1/2 K a^2 (grad u)^2       [inter-site Coulomb coupling; K = Q*g_K, g_K=f''(a) (2008)]
      + q u . E                    [polarization couples to field; P = n q u]
Integrate out u -> eps0, and the transverse propagating mode -> c, mu0 = 1/(eps0 c^2), Z0.

HONESTY FLAGS baked in:
 * the photon here is taken as the gapless TRANSVERSE collective mode (the on-site C gaps the
   longitudinal/ZBW mode). Whether c06's EM EMERGENCE works this way is NOT verified here -- it
   is the construction's load-bearing assumption, flagged, not tasted.
 * 'eps0 emergent vs bare' is treated in the Sea-as-vacuum limit; a bare sub-Sea permittivity
   would change the absolute normalization (not attempted).
"""
import numpy as np

omega_ZBW = 1.0          # fixed by the Absolute Moment (c02) -- geometric
a, n, q   = 1.0, 1.0, 1.0
g_C, g_K  = 2.3, 0.7     # geometric curvature factors f''(d_DP), f''(a) (fixed lattice)

def observables(Q, psr=1.0):
    """psr = an INDEPENDENT kinematic stepping-rate factor (the 0738 VSL channel), separate
       from the stiffness. Default 1 = stiffness-only. We test both channels."""
    C   = Q*g_C
    K   = Q*g_K
    mu_DP = C/omega_ZBW**2
    eps0 = n*q**2/C                              # on-site polarizability (static)
    c2   = (K*a**2/mu_DP) * psr**2               # transverse propagation; PSR boosts reach kinematically
    mu0  = 1.0/(eps0*c2)
    Z0   = np.sqrt(mu0/eps0)
    return dict(C=C,K=K,eps0=eps0,c=np.sqrt(c2),mu0=mu0,Z0=Z0)

print("="*70); print("R2 / lattice-EM action attempt -- what does C do in Z0?"); print("="*70)

# ---- CHANNEL A: VSL varies the STIFFNESS (vary Q; psr fixed). This is the 2002 c~sqrt(C) channel.
print("\n[CHANNEL A] VSL via stiffness: sweep Q (=> C,K both scale), psr=1")
print(f"  {'Q':>6} {'C':>8} {'c':>8} {'eps0':>9} {'mu0':>10} {'Z0':>10}")
Z0s=[]
for Q in [0.5,1.0,2.0,4.0]:
    o=observables(Q); Z0s.append(o['Z0'])
    print(f"  {Q:>6.2f} {o['C']:>8.3f} {o['c']:>8.4f} {o['eps0']:>9.4f} {o['mu0']:>10.4f} {o['Z0']:>10.5f}")
Z0s=np.array(Z0s)
print(f"  -> Z0 variation across 8x Q: {(Z0s.max()-Z0s.min())/Z0s.mean():.2e}  (Z0 ~ Q, NOT flat)")
print(f"  -> c variation across 8x Q : {[round(observables(Q)['c'],3) for Q in [0.5,4.0]]}  (c FIXED)")
print("  READING (what the numbers show, NOT what I expected): Z0 ~ Q -- the explicit")
print("  stiffness does NOT cancel in this construction; AND c does not move. So the naive")
print("  acoustic-photon construction reproduces NEITHER the 2002/2008 geometric Z0 NOR the")
print("  VSL c-variation. The pair-potential/virial cancellation does NOT survive into this")
print("  action -- exactly ChatGPT's warning. (Most likely the naive 'photon = transverse")
print("  acoustic mode of the DP lattice' is the WRONG EM-emergence; a phonon is not a photon.)")

# ---- CHANNEL B: VSL varies the KINEMATIC stepping rate PSR (vary psr; Q fixed). The 0738 channel.
print("\n[CHANNEL B] VSL via kinematic PSR: sweep psr (0738 'PSR_base x(1+H)'), Q=1")
print(f"  {'psr':>6} {'c':>8} {'eps0':>9} {'mu0':>10} {'Z0':>10}")
for psr in [1.0,1.5,2.0,3.0]:
    o=observables(1.0,psr=psr)
    print(f"  {psr:>6.2f} {o['c']:>8.4f} {o['eps0']:>9.4f} {o['mu0']:>10.4f} {o['Z0']:>10.5f}")
o1,o3=observables(1.0,1.0),observables(1.0,3.0)
A_psr = np.log(o3['Z0']/o1['Z0'])/np.log(o3['c']/o1['c'])
print(f"  -> c MOVES with psr (this IS the VSL). d ln Z0/d ln c = {A_psr:+.2f}")
print(f"  READING: in THIS naive construction psr enters only mu0 (propagation), NOT eps0")
print(f"  (static polarizability) -> Z0 ~ 1/c -> A = {A_psr:+.0f} -> would FAIL. This is the")
print(f"  d_eps=0,d_mu!=0 maximal-asymmetry case.")

print("\n"+"="*70); print("VERDICT (action attempt, honest, NOT tasted -- a NEGATIVE result):")
print(" 1. The naive lattice-EM action (photon = transverse acoustic mode) does NOT")
print("    reproduce the established heuristics: it gives Z0 ~ Q (stiffness does NOT cancel,")
print("    contra 2002/2008) AND c geometric (no VSL, contra 0738). So this construction is")
print("    WRONG/insufficient -- a DP-lattice acoustic mode is a phonon, not the photon.")
print(" 2. The PSR channel (the actual 0738 VSL) does move c, but in this construction enters")
print("    only mu0 -> Z0~1/c -> A=-1 -> FAIL. That too reflects the wrong emergence (psr")
print("    should enter eps0 and mu0 together if EM emerges correctly).")
print(" 3. CONSEQUENCE: the action-level closure CANNOT be completed without the actual c06")
print("    EM-EMERGENCE construction -- the mechanism by which a GAPLESS photon (not a phonon)")
print("    emerges from the DP Sea, how its c varies (the VSL channel), and whether that")
print("    channel enters eps0 and mu0 symmetrically. This is DEEPER than the stiffness ratio")
print("    (2008) and the screening (ChatGPT #1): it is the EM-emergence mechanism itself.")
print(" 4. HONEST NET: this attempt does NOT confirm R2 PASS. It confirms ChatGPT's REVISE and")
print("    shows WHY the closure is owed to the c06 action -- and that the 2002/2008 geometric-")
print("    Z0 is a HEURISTIC the correct action must still be shown to reproduce, which a naive")
print("    construction does not. R2's full PASS is genuinely blocked on the c06 EM-emergence")
print("    construction, which is not specified at the needed level. NOT tasted past this point.")
