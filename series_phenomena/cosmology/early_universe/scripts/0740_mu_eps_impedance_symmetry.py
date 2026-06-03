#!/usr/bin/env python3
"""
0740_mu_eps_impedance_symmetry.py
=================================
Resolves the residual of the Delta-c / LPI filter (0739): is the DP-Sea response
to SSV mu<->eps SYMMETRIC (asymmetry A ~ 0), so that a density-dependent c_eff is
purely gravitational (alpha fixed) and survives the varying-constants bounds?

THE CLEAN REDUCTION. Two defining relations fix mu_0 and eps_0:
    c   = 1/sqrt(mu_0 eps_0)      (broadcast/null-trajectory speed)  -> PRODUCT
    Z_0 = sqrt(mu_0/eps_0)        (impedance of free space)          -> RATIO
Solving:  mu_0 = Z_0/c ,  eps_0 = 1/(Z_0 c).  With alpha ~ sqrt(mu/eps):

    d_mu = dZ - dc ,  d_eps = -dZ - dc   (fractional changes under an SSV step)
    Delta c/c = -1/2 (d_mu+d_eps) = dc
    Delta a/a = +1/2 (d_mu-d_eps) = dZ          <-- ALPHA VARIATION = IMPEDANCE VARIATION
    A = (d_mu-d_eps)/(d_mu+d_eps) = -dZ/dc

So the ENTIRE danger collapses to ONE quantity: does the impedance Z_0 change
under SSV?  Delta a/a = Delta ln Z_0, exactly. If Z_0 is a fixed GEOMETRIC
constant of the lattice, alpha is fixed (A=0) and the c_eff variation is pure
gravity. If Z_0 inherits the SSV-variable stiffness, alpha tracks the potential
and the picture is falsified.

CORPUS GROUNDING that Z_0 is geometric (not stiffness-dependent):
  1. c06: the photon's magnetic component is "the curl of the propagating SSV
     pattern" -- B is NOT an independent susceptibility; it is geometrically
     locked to the electric/polarization pattern by the curl over the GP network.
     So mu and eps are two views of ONE ZDC propagation, not two free knobs.
  2. Brick #2 / SR-1: GPs are FIXED and ETERNAL. The curl/broadcast geometry that
     sets the E<->B locking (hence Z_0) is a property of the fixed lattice, while
     SSV changes the stiffness C and the reach c. Fixed-lattice ratio => Z_0 fixed;
     variable reach => c (the product) varies.
  3. c06: "all four DP types participate equally" in ZDC formation -- no
     species-selective channel to split the E vs B response with composition.

CONDITIONAL on the explicit derivation of mu_0(C,c), eps_0(C,c) -- a task ALREADY
registered in c06 ("express mu_0 and eps_0 in terms of the 600-cell stiffness C
and the shell-broadcast speed c") -- the prediction is: Z_0 in lattice units is a
PURE 600-cell geometric constant, with NO dependence on the SSV-variable C.
That single outcome IS the mu<->eps symmetry proof (A=0) AND a falsifiable
internal-consistency test.
"""

import numpy as np

K_ALPHA_CLOCK = 1e-6   # tight LPI bound on Delta_alpha/alpha per unit dPhi (0739)


def demo():
    print("=" * 72)
    print("mu<->eps SYMMETRY: alpha-variation = impedance-variation (Delta a/a = dZ)")
    print("=" * 72)

    print("\nFrom c=1/sqrt(mu*eps) and Z0=sqrt(mu/eps):  mu0=Z0/c,  eps0=1/(Z0 c).")
    print("Under an SSV step (dc = fractional change in reach/speed, dZ = in impedance):")
    print("   Delta c/c = dc            (the PRODUCT mu*eps moves with the speed)")
    print("   Delta a/a = dZ            (the RATIO mu/eps moves with the impedance)")
    print("   A = -dZ/dc                (response asymmetry)")
    print("=> The whole question is ONE number: does Z0 move under SSV?\n")

    # numerical confirmation of the algebra (no physics assumed, just identities)
    rng = np.random.default_rng(7)
    ok = True
    for _ in range(5):
        dc = rng.uniform(-0.1, 0.1)     # some SSV-induced fractional speed change
        dZ = rng.uniform(-0.1, 0.1)     # some impedance change (the unknown)
        d_mu = dZ - dc
        d_eps = -dZ - dc
        dcc = -0.5 * (d_mu + d_eps)
        daa = 0.5 * (d_mu - d_eps)
        A = (d_mu - d_eps) / (d_mu + d_eps)
        ok &= np.isclose(dcc, dc) and np.isclose(daa, dZ) and np.isclose(A, -dZ/dc)
    print(f"  identity check (Delta c/c=dc, Delta a/a=dZ, A=-dZ/dc): "
          f"{'CONFIRMED' if ok else 'FAILED'}")

    print("\n--- The two outcomes for Z0 (the registered c06 derivation will decide) ---")
    print(f"{'Z0 character':>34} | {'dZ under SSV':>12} | {'Delta a/a':>10} | verdict")
    print("-" * 72)
    # geometric Z0: fixed-lattice ratio, no stiffness dependence -> dZ = 0
    print(f"{'PURE 600-cell geometry (predicted)':>34} | {0.0:>12.0e} | {0.0:>10.0e} | "
          f"A=0, alpha FIXED -> SURVIVES (c-var=gravity)")
    # stiffness-inheriting Z0: tracks the SSV-variable stiffness -> dZ ~ dc, so
    # k_alpha = |Delta a/a per unit dPhi| = |dZ/dc| ~ 1 (full tracking)
    dc_gal = 1e-6   # galactic metric Delta c/c ~ gravitational potential ~ dPhi
    daa_fail = dc_gal            # Delta a/a = dZ ~ dc (impedance fully tracks)
    k_alpha_fail = daa_fail / dc_gal   # = 1 (per unit dPhi)
    margin = k_alpha_fail / K_ALPHA_CLOCK
    print(f"{'inherits stiffness C (failure mode)':>34} | {dc_gal:>12.0e} | {daa_fail:>10.0e} | "
          f"k_alpha~{k_alpha_fail:.0f} -> FAILS by ~{margin:.0e}x vs clock bound")

    print("\n--- Experimental headroom on the impedance ---")
    print(f"  clock LPI |Delta a/a| <~ {K_ALPHA_CLOCK:.0e}  ==>  |Delta ln Z0| <~ {K_ALPHA_CLOCK:.0e}")
    print("  i.e. the impedance must be geometric (SSV-independent) to ~1 ppm.")
    print("  The 'B = curl of the polarization pattern over FIXED, ETERNAL GPs'")
    print("  structure (c06 + Brick #2) makes Z0 a fixed-lattice ratio => dZ = 0")
    print("  structurally, comfortably inside the ppm headroom.")

    print("\n" + "=" * 72)
    print("RESULT")
    print("=" * 72)
    print("  The mu<->eps symmetry residual reduces EXACTLY to: is Z0 geometric?")
    print("  Delta a/a = Delta ln Z0. Three corpus facts (B=curl; fixed/eternal GPs;")
    print("  equal DP participation) all point to Z0 = pure 600-cell geometry => A=0")
    print("  => density-dependent c_eff is purely gravitational => SURVIVES.")
    print("  CONDITIONAL on the explicit Z0(C,c) derivation (already registered in")
    print("  c06). Sharp test: Z0 in lattice units must come out C-independent.")
    print("  If it does: symmetry proven, Delta-c residual CLOSED. If it depends on")
    print("  the SSV-variable C: revisit. This derivation also feeds c06's emission")
    print("  envelope / linewidth (Dnu ~ nu^3), so it is not make-work.")


if __name__ == "__main__":
    demo()
