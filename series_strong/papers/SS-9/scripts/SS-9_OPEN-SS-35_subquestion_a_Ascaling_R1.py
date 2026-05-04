"""
SS-9 OPEN-SS-35 sub-question (a) A-scaling — R1 ruled out (Session 12).

Tests Resolution R1 (R_alpha scale-dependence as A-scaling closure)
registered in the Session 7 Phase 1 A-scaling sketch §3.3.  R1
hypothesizes that internal-contact DP-sea Coulomb screening (vs full
Coulomb at the isolated ^8Be contact that fixed R_alpha = 2.37 fm)
compresses R_alpha at large clusters, and that this compression could
close the empirical hbar*omega proportional-to A^{-1/3} scaling.

Three findings, all robust:

  Finding 1.  Force-balance gives R_alpha COMPRESSION inward, not
              expansion.  Empirical match requires expansion (lower
              hbar*omega = larger R_c = larger R_alpha at fixed shape).
              R1 has wrong sign.  Sign is robust across all reasonable
              K_3 well parametrizations (sigma in [1.0, 2.5] fm).

  Finding 2.  Inverting CPP/empirical hbar*omega ratios to ask "what
              R_alpha(A) would close the gap" gives a U-shape, not a
              power law: endpoints (regular polytopes N=4, 12) need
              ~no change; mid-range J-solids (N=5-10) need 7-23%
              expansion peaking at N=10.  No monotonic R_alpha(A) law
              produces this pattern.  Discrepancy is shape-driven.

  Finding 3.  Decoupling Theorem: V_SO/hbar*omega = (v_F/c)^2 is
              independent of hbar*omega magnitude in the CPP B-alpha
              layer 1 framework.  A-scaling closure does not touch
              layer-3 gap-strength deficit.

Companion sketch:
    series_strong/papers/SS-9/sketches/
        SS-9_OPEN-SS-35_subquestion_a_Ascaling_R1_RULED_OUT.md
Companion script (Session 7 Phase 1 A-scaling extension):
    series_strong/papers/SS-9/scripts/
        SS-9_OPEN-SS-35_subquestion_a_Ascaling.py

Verdict: R1 RULED OUT.  5th programme-level negative result on
OPEN-SS-35 closure programme.  R2 (cluster-scale vs alpha-scale mean
field interpretation) becomes the only remaining A-scaling closure
candidate.  Forward pointer: U-shape diagnostic structurally
resembles SS-7 OPEN-SS-32 J-solid regime; investigation registered
as future sub-sub-question.
"""

import math
import numpy as np
from scipy.optimize import brentq


# ---------------------------------------------------------------------------
# Constants (CPP, SS-5/SS-7 anchored)
# ---------------------------------------------------------------------------
phi      = (1 + math.sqrt(5)) / 2
M_0      = 3.790                   # MeV (SS-7/SS-8 z*m_e/phi mass scale)
B_pair   = M_0 / phi               # 2.342 MeV (SS-5 K_3 collective contribution)
hbar_c   = 197.327                 # MeV*fm
alpha_em = 1/137.036
R_8Be    = 2.37                    # fm (SS-7 inversion from ^8Be 92 keV)
R_RMS    = 1.68                    # fm (alpha-particle RMS radius)


# ---------------------------------------------------------------------------
# Coulomb piece: V_Coul(R) = +4 alpha_em hbar_c / R
# (Z_alpha = 2, so e^2 Z^2 = 4 alpha_em hbar_c with hbar c in MeV*fm)
# ---------------------------------------------------------------------------
def V_Coul(R):
    return 4 * alpha_em * hbar_c / R

def Vp_Coul(R):
    return -4 * alpha_em * hbar_c / R**2

def Vpp_Coul(R):
    return +8 * alpha_em * hbar_c / R**3


# ---------------------------------------------------------------------------
# K_3 well parametrization: V_K3(R) = -V0 * exp(-((R-R0)/sigma)^2)
#
# Two constraints at R = R_8Be:
#   (A) V_K3(R_8Be) = -B_pair
#   (B) V_K3'(R_8Be) = -V_Coul'(R_8Be) = +1.0255 MeV/fm  (force balance)
#
# These fix V0 and R0 given sigma.  Sigma is a physical parameter
# scanned over [1.0, 2.5] fm to probe sign robustness.
# ---------------------------------------------------------------------------
target_slope = -Vp_Coul(R_8Be)        # +1.0255 MeV/fm
target_depth = -B_pair                # -2.3424 MeV
SLOPE_RATIO  = target_slope / (2 * B_pair)  # = (R_8Be - R0)/sigma^2 = 0.21908 fm^-1


def fit_two_constraints(sigma):
    """Given sigma, return (V0, R0) satisfying constraints (A) and (B).

    From V_K3'(R_8Be)/B_pair = 2*(R_8Be - R0)/sigma^2 = SLOPE_RATIO * 2:
        R0 = R_8Be - SLOPE_RATIO * sigma^2
    From V_K3(R_8Be) = -B_pair = -V0 * exp(-((R_8Be-R0)/sigma)^2):
        V0 = B_pair * exp(+((R_8Be-R0)/sigma)^2)
    """
    R0 = R_8Be - SLOPE_RATIO * sigma**2
    V0 = B_pair * math.exp(((R_8Be - R0) / sigma)**2)
    return V0, R0


def V_K3(R, V0, R0, sigma):
    return -V0 * np.exp(-((R - R0) / sigma)**2)


def Vp_K3(R, V0, R0, sigma):
    """dV_K3/dR = +V0 * exp(...) * 2*(R - R0) / sigma^2
    (positive past R0, the well center)."""
    return +V0 * np.exp(-((R - R0) / sigma)**2) * 2 * (R - R0) / sigma**2


def find_R_eq(f_eff, V0, R0, sigma):
    """Find equilibrium R_alpha at screening f_eff in [0, 1].

    Equilibrium: V_K3'(R) + f_eff^2 * V_Coul'(R) = 0.
    Returns None if no root exists in (R0, 5.0).
    """
    def force(R):
        return Vp_K3(R, V0, R0, sigma) + f_eff**2 * Vp_Coul(R)
    lo = max(R0 + 0.001, 0.5)
    if force(lo) * force(5.0) > 0:
        return None
    return brentq(force, lo, 5.0)


# ---------------------------------------------------------------------------
# Finding 1: Sign robustness across K_3 well width sigma
# ---------------------------------------------------------------------------
def finding_1_sigma_scan():
    """Sigma-scan demonstrating R_alpha COMPRESSION is robust."""
    print("=" * 76)
    print("FINDING 1: Sign of R_alpha(f_eff) compression — sigma-scan")
    print("=" * 76)
    print()
    print(f"Target at R_8Be = {R_8Be} fm:")
    print(f"  V_K3(R_8Be)  = {target_depth:+.4f} MeV   (constraint A: depth at contact)")
    print(f"  V_K3'(R_8Be) = {target_slope:+.4f} MeV/fm  (constraint B: force balance)")
    print()
    print(f"{'sigma':>6} {'V0':>7} {'R0':>7}  {'R(f=0.5)':>9} {'R(f=0.2)':>9} "
          f"{'R(f=0.1)':>9} {'R(f=0)':>9}")
    print("-" * 70)
    for sigma in [1.00, 1.20, 1.50, 1.68, 2.00, 2.50]:
        V0, R0 = fit_two_constraints(sigma)
        rs = []
        for f_eff in [0.5, 0.2, 0.1, 0.0]:
            R = find_R_eq(f_eff, V0, R0, sigma)
            rs.append(R if R is not None else float('nan'))
        print(f"{sigma:>6.2f} {V0:>7.3f} {R0:>7.3f}  {rs[0]:>9.4f} {rs[1]:>9.4f} "
              f"{rs[2]:>9.4f} {rs[3]:>9.4f}")
    print()
    print("All cases: R_alpha(f_eff < 1) < R_8Be = 2.37 fm.")
    print("=> COMPRESSION is universal across the K_3 well parametrization family.")
    print("=> SIGN OF R1 IS ROBUST.  R_alpha contracts inward; never expands.")
    print()


# ---------------------------------------------------------------------------
# Sign-of-required-direction analysis
# ---------------------------------------------------------------------------
def empirical_match_sign():
    """Show that empirical match requires R_alpha to EXPAND, not compress."""
    print("=" * 76)
    print("SIGN-OF-REQUIRED-DIRECTION:  empirical match requires expansion")
    print("=" * 76)
    print()
    print("In the Session 6 / Session 7 framework: hbar*omega ~ 1/R_c^2,")
    print("where R_c is the cluster centroid-to-vertex distance.")
    print("With polytope geometry R_c proportional R_alpha at fixed shape,")
    print("hbar*omega ~ 1/R_alpha^2.")
    print()
    print("Empirical hbar*omega = 41/A^{1/3} DECREASES with A.")
    print("=> R_alpha must INCREASE with A (to push hbar*omega down).")
    print()
    print("R1 (energetic Coulomb screening) gives R_alpha DECREASING with A.")
    print("=> WRONG SIGN.  R1 cannot resolve the A-scaling discrepancy.")
    print()


# ---------------------------------------------------------------------------
# Finding 2: U-shape pattern from inversion
# ---------------------------------------------------------------------------
SESSION_7_DATA = [
    # (N_alpha, A, hbar_omega_CPP_fixed_R_alpha = 2.37 fm)
    # Source: Session 7 Phase 1 A-scaling sketch Table §3.1
    ( 4, 16, 14.60),
    ( 5, 20, 17.19),
    ( 6, 24, 18.06),
    ( 7, 28, 19.15),
    ( 8, 32, 18.94),
    ( 9, 36, 18.56),
    (10, 40, 18.05),
    (12, 48, 11.13),
]


def finding_2_ushape():
    """Compute required R_alpha(A) to close the empirical gap; show U-shape."""
    print("=" * 76)
    print("FINDING 2: Required R_alpha(A) for empirical match — U-shape pattern")
    print("=" * 76)
    print()
    print(f"{'N':>3}  {'A':>3}  {'hw_CPP':>8}  {'hw_emp':>8}  {'CPP/emp':>8}  "
          f"{'R_req':>7}  {'change':>7}")
    print(f"{'':3}  {'':3}  {'(MeV)':>8}  {'(MeV)':>8}  {'ratio':>8}  "
          f"{'(fm)':>7}  {'%':>7}")
    print("-" * 70)
    R_required_data = []
    for N, A, hw_cpp in SESSION_7_DATA:
        hw_emp = 41.0 / A**(1/3)
        ratio = hw_cpp / hw_emp
        R_required = R_8Be * math.sqrt(ratio)  # to scale CPP -> emp
        pct = (R_required - R_8Be) / R_8Be * 100
        print(f"{N:>3}  {A:>3}  {hw_cpp:>8.2f}  {hw_emp:>8.2f}  {ratio:>8.3f}  "
              f"{R_required:>7.3f}  {pct:>+6.1f}%")
        R_required_data.append((N, A, R_required, pct))
    print()
    print("Pattern is NON-MONOTONIC and U-shaped:")
    print("  Endpoints (N=4, N=12 — regular polytopes, full 3D symmetry):")
    print("    Match empirical to within 1-10%; ~no change required.")
    print("  Mid-range (N=5-10 — J-solid deltahedra, axial symmetry):")
    print("    Need 7-23% expansion; peaks at N=10 (+22.7%).")
    print()
    print("=> No monotonic R_alpha(A) law produces this shape.")
    print("=> Discrepancy is SHAPE-DRIVEN (J-solid mid-range overshoot),")
    print("   not radius-driven.")
    print()
    print("Structural interpretation: regular polytopes (full 3D symmetry, no")
    print("symmetry-breakable belts/seams) give CPP/emp near 1; J-solid mid-")
    print("range deltahedra (axial symmetry, with belts and seams that activate")
    print("OPEN-SS-32-style oblate deformation modes in SS-7) over-bind the")
    print("centroid in the K_3 mean field.")
    print()
    return R_required_data


# ---------------------------------------------------------------------------
# Finding 3: Decoupling Theorem
# ---------------------------------------------------------------------------
def finding_3_decoupling():
    """Decoupling Theorem: V_SO/hbar_omega = (v_F/c)^2 is independent of hbar_omega."""
    print("=" * 76)
    print("FINDING 3: Decoupling Theorem")
    print("=" * 76)
    print()
    print("Theorem.  In the CPP B-alpha layer 1 framework where")
    print("              V_SO = (v_F/c)^2 * hbar_omega                    (5)")
    print("the dimensionless ratio V_SO/hbar_omega = (v_F/c)^2 is")
    print("INDEPENDENT of hbar_omega magnitude.  Therefore A-scaling")
    print("closure (R1 or R2) does not affect layer-3 gap-strength.")
    print()

    # Session 8 layer 1 inputs at A = 56:
    hbar_omega_CPP_56  = 13.0
    v_F_over_c         = 0.30
    V_SO_CPP_56        = v_F_over_c**2 * hbar_omega_CPP_56  # = 1.17 MeV
    ratio_CPP          = V_SO_CPP_56 / hbar_omega_CPP_56    # = 0.090

    # Empirical:
    hbar_omega_emp_56  = 41.0 / 56**(1/3)                   # ≈ 10.72 MeV
    V_SO_emp_56        = 1.5
    ratio_emp          = V_SO_emp_56 / hbar_omega_emp_56    # ~ 0.140

    print("At A = 56:")
    print(f"  CPP:  hbar*omega = {hbar_omega_CPP_56:.2f} MeV, "
          f"V_SO = {V_SO_CPP_56:.3f} MeV, ratio = {ratio_CPP:.3f}")
    print(f"  emp:  hbar*omega = {hbar_omega_emp_56:.2f} MeV, "
          f"V_SO ~ {V_SO_emp_56:.2f} MeV, ratio = {ratio_emp:.3f}")
    print()
    print(f"Strong-magic threshold:  V_SO/hbar*omega in [0.20, 0.25]")
    print(f"CPP ratio 0.090 is below empirical 0.140 — both are below threshold.")
    print()
    print("Hypothetical: if A-scaling closure shifted CPP hbar*omega from 13 to")
    print(f"the empirical {hbar_omega_emp_56:.2f} MeV, then by Eq. (5):")
    hw_after = hbar_omega_emp_56
    V_SO_after = v_F_over_c**2 * hw_after
    ratio_after = V_SO_after / hw_after
    print(f"  Adjusted V_SO_CPP = (0.30)^2 * {hw_after:.2f} = {V_SO_after:.3f} MeV")
    print(f"  Adjusted ratio    = {ratio_after:.3f}  (UNCHANGED)")
    print()
    print("=> The dimensionless ratio that determines magic-number gap strength")
    print("   is INVARIANT under A-scaling adjustment.")
    print("=> A-scaling closure (R1 or R2) does NOT close the layer-3 gap-")
    print("   strength deficit.")
    print()
    print("Implication: the pathway to gap-strength closure is via v_F/c (or")
    print("via additional CPP physics modifying Eq. 5), not via hbar*omega.")
    print("Either v_F/c in CPP must be larger (~0.37 to match empirical 0.14)")
    print("or the layer-1 relationship V_SO = (v_F/c)^2 * hbar*omega itself is")
    print("modified.  This is the gap-strength-closure programme identified in")
    print("Session 11 Phase 1, NOT the A-scaling-closure programme.")
    print()
    return ratio_CPP, ratio_emp


# ---------------------------------------------------------------------------
# Verdict and programme summary
# ---------------------------------------------------------------------------
def verdict():
    print("=" * 76)
    print("VERDICT:  R1 (R_alpha scale-dependence as A-scaling closure) RULED OUT")
    print("=" * 76)
    print()
    print("Three independent findings:")
    print()
    print("  (1) Sign of energetic mechanism is wrong.")
    print("      Force-balance R1 compresses R_alpha inward.")
    print("      Empirical match requires expansion.")
    print("      Robust across all K_3 well parametrizations.")
    print()
    print("  (2) Pattern is non-monotonic, U-shaped — not power law.")
    print("      Endpoints (regular polytopes N=4, 12) match empirical.")
    print("      Mid-range J-solids (N=5-10) need 7-23% expansion.")
    print("      No monotonic R_alpha(A) produces this shape.")
    print("      Discrepancy is shape-driven, not radius-driven.")
    print()
    print("  (3) Decoupling Theorem.")
    print("      V_SO/hbar*omega = (v_F/c)^2 is hbar*omega-independent.")
    print("      A-scaling closure does not touch layer-3 gap strength.")
    print()
    print("Programme effects:")
    print("  - R1 status: candidate -> RULED OUT.")
    print("  - 5th programme-level negative result on OPEN-SS-35 closure.")
    print("  - R2 (cluster-scale interpretation) is the only remaining")
    print("    A-scaling closure candidate.")
    print("  - Decoupling Theorem narrows gap-strength closure candidate")
    print("    list by removing A-scaling fixes.")
    print("  - U-shape diagnostic registers a forward pointer to OPEN-SS-32")
    print("    J-solid regime as future-session investigation.")
    print()
    print("Six programme-level OPEN-SS-35 stages preserved; first qualitative")
    print("cross-paradigm consilience claim (Session 9) intact; Pattern 6 K_3")
    print("scale-recurrence at 7 confirmed instances unchanged.")


def main():
    finding_1_sigma_scan()
    empirical_match_sign()
    finding_2_ushape()
    finding_3_decoupling()
    verdict()


if __name__ == "__main__":
    main()
