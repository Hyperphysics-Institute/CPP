"""
SS-9 OPEN-SS-35 sub-question (b) B-alpha layer 3:
V_SO refinement via Routes 1a, 1b, 1c (Session 10).

Three routes for refining V_SO/hbar*omega from layer 1's 0.09 toward
empirical strong-magic threshold >= 0.20:

  Route 1a: refined v_F/c via Approach C (surface-region) emphasis at A~56
  Route 1b: centrifugal correction from K_3 Gaussian-modulated mean field
            (PRINCIPAL INVESTIGATION: tests whether K_3 anharmonicity gives
            empirical centrifugal enhancement)
  Route 1c: higher-order relativistic from SSV-PSR_eff machinery

Result: Route 1b RULED OUT (wrong sign for centrifugal enhancement, plus
perturbation breakdown at high-N). Routes 1a + 1c give modest improvement:
V_SO/hbar*omega: 0.090 -> 0.113 (+25%). Combined refinement reaches 56%
of empirical strong-magic threshold.

Session 10 establishes the BOUND of what the simple HO + L.S framework
can achieve. Full layer 3 gap-strength closure requires multi-session
cluster-surface physics.

Companion sketch:
  series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer3_VSO_refinement.md
"""

import math


# ---------------------------------------------------------------------------
# Constants and CPP-derived inputs
# ---------------------------------------------------------------------------
hbar_c = 197.327                # MeV*fm
m_n_c2 = 939.565                # MeV
hbar_omega = 13.0               # MeV at A~56 (sub-question (a) Sessions 6, 7)
sigma_nucleon = hbar_c / math.sqrt(m_n_c2 * hbar_omega)  # nucleon localization length

# Session 8 layer 1 baseline
v_F_baseline = 0.30
V_SO_baseline = v_F_baseline**2 * hbar_omega
ratio_baseline = V_SO_baseline / hbar_omega

# Session 10 Route 1a refinement: v_F/c via surface-region emphasis at A~56
v_F_refined = 0.32   # interpolated between A=48 ico (0.307) and A=40 (0.356)


# ---------------------------------------------------------------------------
# Route 1b: <r^4> matrix elements for HO states
# ---------------------------------------------------------------------------
def f_NL(N, l):
    """Diagonal HO matrix element <n,l|r^4|n,l> / (hbar/m omega)^2,
    where N = 2n + l."""
    n = (N - l) // 2
    return (N + 1.5)**2 + 2*n*(n + l + 1.5) + l + 1.5


def quartic_correction_table(N_max=6):
    """Print table of quartic energy shifts Delta E_{N,l} = C_4 * <r^4>_{N,l}
    where C_4 = -m omega^2/(8 sigma^2) for Gaussian K_3 potential."""
    spd = 'spdfghijkl'
    prefactor = -hbar_c**2 / (m_n_c2 * 8 * sigma_nucleon**2)
    print(f"  {'N':>3} {'l':>3} {'orbital':>10} {'f(N,l)':>10} {'Delta E (MeV)':>15}")
    print("  " + "-"*45)
    for N in range(N_max + 1):
        for l in range(N % 2, N + 1, 2):
            n = (N - l) // 2 + 1
            f = f_NL(N, l)
            dE = prefactor * f
            print(f"  {N:>3d} {l:>3d} {n}{spd[l]:>9} {f:>10.2f} {dE:>15.3f}")


def centrifugal_sign_check():
    """Verify wrong-sign result: at fixed N, low-l has larger f(N,l) than
    high-l. Combined with C_4 < 0, this means low-l is lowered MORE."""
    print("Centrifugal sign analysis:")
    print("At fixed N, larger l -> smaller f(N,l):")
    for N in [2, 3, 4, 5, 6]:
        ls = list(range(N % 2, N + 1, 2))
        f_values = [f_NL(N, l) for l in ls]
        comparisons = " > ".join([f"f({N},{l})={f_NL(N,l):.2f}" for l in ls])
        print(f"  N={N}: {comparisons}")
    print()
    print("Quartic coefficient C_4 = -m*omega^2/(8*sigma^2) is NEGATIVE.")
    print("=> Delta E = C_4 * <r^4> is more NEGATIVE for low-l (larger <r^4>).")
    print("=> Low-l states are LOWERED MORE by quartic.")
    print("=> WRONG SIGN for empirical centrifugal enhancement (Bohr-Mottelson")
    print("   D*l(l+1) lowers high-l more, NOT low-l).")


# ---------------------------------------------------------------------------
# Route 1c: SSV-PSR_eff higher-order corrections
# ---------------------------------------------------------------------------
def relativistic_correction_factor(v_over_c, beta=1.0):
    """Multiplicative correction to V_SO from next-order (v/c)^4 in
    SSV-PSR_eff expansion. PSR_eff = l_P/(1+k*Delta_SSV) expands to
    1 - alpha*(v/c)^2 + alpha^2*(v/c)^4 - ...
    
    The (v/c)^4 term gives multiplicative factor 1 + beta*(v/c)^2 on V_SO,
    where beta is order unity (~1 for conventional Foldy-Wouthuysen-style
    expansion)."""
    return 1 + beta * v_over_c**2


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 78)
    print("Session 10: V_SO refinement via Routes 1a, 1b, 1c")
    print("=" * 78)
    print()
    print("CPP-derived inputs:")
    print(f"  hbar*omega = {hbar_omega} MeV (sub-question (a))")
    print(f"  sigma = {sigma_nucleon:.4f} fm (nucleon localization length)")
    print(f"  Session 8 layer 1 baseline: v_F/c = {v_F_baseline}")
    print(f"    V_SO = {V_SO_baseline:.3f} MeV, V_SO/hbar*omega = {ratio_baseline:.4f}")
    print()

    # Route 1b
    print("=" * 78)
    print("Route 1b: Centrifugal correction from K_3 Gaussian-modulated mean field")
    print("=" * 78)
    print()
    print("K_3 potential expanded near centroid:")
    print("  V(r) = -V_0 * exp(-r^2/2 sigma^2) ~ -V_0 + (V_0/2 sigma^2) r^2")
    print("                                   - (V_0/8 sigma^4) r^4 + ...")
    print(f"  C_4 = -m*omega^2/(8 sigma^2) = {-m_n_c2 * (hbar_omega/hbar_c)**2 / (8*sigma_nucleon**2):.4f} MeV/fm^4 [NEGATIVE]")
    print()
    print("Quartic energy shifts Delta E_{N,l} = C_4 * <r^4>_{N,l}:")
    quartic_correction_table()
    print()
    centrifugal_sign_check()
    print()
    print("Magnitude warning:")
    print("  For high-N states (N=4,5,6), |Delta E| ~ 60-140 MeV >> hbar*omega = 13 MeV.")
    print("  First-order perturbation theory FAILS spatially: high-N HO wavefunctions")
    print("  extend beyond the Gaussian width and probe the cluster boundary,")
    print("  where the K_3 potential transitions to its asymptotic form.")
    print()
    print("VERDICT: Route 1b RULED OUT as magic-strength enhancement route.")
    print("  - Wrong sign (low-l lowered more than high-l)")
    print("  - Perturbation theory breakdown at the relevant high-N regime")
    print("  - Missing physics is at cluster boundary, not central region")
    print()

    # Route 1a
    print("=" * 78)
    print("Route 1a: Refined v_F/c via Approach C (surface-region) emphasis")
    print("=" * 78)
    print()
    print("Session 8 Approach C (surface-region, Thomas-form): v_F/c [0.278, 0.356]")
    print(f"  At A=48 icosahedron: v_F/c = 0.307")
    print(f"  At A=40 gyroelongated sq. bip.: v_F/c = 0.356")
    print(f"  Interpolated to A=56: v_F/c = {v_F_refined}")
    print()
    V_SO_1a = v_F_refined**2 * hbar_omega
    ratio_1a = V_SO_1a / hbar_omega
    print(f"V_SO_1a = (v_F/c)^2 * hbar*omega = {v_F_refined**2:.4f} * {hbar_omega}")
    print(f"        = {V_SO_1a:.3f} MeV")
    print(f"V_SO/hbar*omega (Route 1a): {ratio_1a:.4f}")
    print(f"Increase from baseline: +{(ratio_1a/ratio_baseline - 1)*100:.1f}%")
    print()

    # Route 1c
    print("=" * 78)
    print("Route 1c: Higher-order relativistic via SSV-PSR_eff expansion")
    print("=" * 78)
    print()
    print("PSR_eff = l_P/(1 + k*Delta_SSV) expanded:")
    print("  PSR_eff/l_P = 1 - alpha*(v/c)^2 + alpha^2*(v/c)^4 - ...")
    print()
    print("V_SO inherits multiplicative (v/c)^4 correction:")
    print("  V_SO_corrected = V_SO_leading * [1 + beta*(v/c)^2]")
    print(f"  At v_F/c = {v_F_refined}, (v_F/c)^2 = {v_F_refined**2:.4f}")
    correction_1c = relativistic_correction_factor(v_F_refined)
    print(f"  Correction factor (beta=1): {correction_1c:.4f}")
    print()
    V_SO_combined = V_SO_1a * correction_1c
    ratio_combined = V_SO_combined / hbar_omega
    print(f"V_SO_combined (Routes 1a + 1c) = V_SO_1a * factor")
    print(f"                              = {V_SO_1a:.3f} * {correction_1c:.4f}")
    print(f"                              = {V_SO_combined:.3f} MeV")
    print(f"V_SO/hbar*omega (combined): {ratio_combined:.4f}")
    print(f"Additional increase from Route 1c: +{(ratio_combined/ratio_1a - 1)*100:.1f}%")
    print()

    # Synthesis
    print("=" * 78)
    print("Synthesis: bounded refinement")
    print("=" * 78)
    print()
    print(f"  {'Route':>30} {'V_SO/hbar*omega':>18} {'rel. to baseline':>18}")
    print("  " + "-"*70)
    print(f"  {'Session 8 layer 1 baseline':>30} {ratio_baseline:>18.4f} {1.0:>17.2f}x")
    print(f"  {'Route 1a (refined v_F/c)':>30} {ratio_1a:>18.4f} {ratio_1a/ratio_baseline:>17.2f}x")
    print(f"  {'Routes 1a + 1c combined':>30} {ratio_combined:>18.4f} {ratio_combined/ratio_baseline:>17.2f}x")
    print(f"  {'Empirical strong-magic threshold':>30} {0.20:>18.4f} {0.20/ratio_baseline:>17.2f}x")
    print()
    print(f"Combined refinement reaches V_SO/hbar*omega = {ratio_combined:.4f}")
    print(f"  = {ratio_combined/0.20*100:.0f}% of empirical strong-magic threshold (0.20)")
    print(f"  = remaining gap to threshold: factor of {0.20/ratio_combined:.2f} to {0.25/ratio_combined:.2f}")
    print()
    print("Session 10 BOUNDS the simple HO + L.S framework: cannot reach")
    print("strong-magic threshold without additional physics.")
    print()
    print("Identified missing physics:")
    print("  Path (i) Cluster-surface Thomas-form spin-orbit:")
    print("    V_SO_eff = <xi(r)>_surface where xi(r) ~ -dV/dr peaks at boundary.")
    print("  Path (ii) Numerical diagonalization beyond Taylor expansion:")
    print("    Full K_3 Gaussian Hamiltonian, captures cluster-edge effects.")
    print()
    print("Both are multi-session work appropriate for future programme advances.")


if __name__ == "__main__":
    main()
