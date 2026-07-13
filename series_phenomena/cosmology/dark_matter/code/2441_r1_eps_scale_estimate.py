"""
OPEN-DM-FLOQUET-1  R1 scoping: order-level eps = (w_A/w_sw)^2 scale estimate for
geometry #3, to locate which fragmentation branch / switching-hop corner falls in
the method-(a) stability window eps in ~[0.18, 0.43].    Patch 2441 (Opus).

THIS IS A SCALE ESTIMATE, NOT THE R1 SOLVE. Inputs are order-level (E_qq is a scale
estimate; s ~ d; w_sw taken as the constituent Compton/ZBW-hop clock). The full R1
self-consistent driven-equilibrium solve must replace these with pinned values and a
DERIVED fragmentation branch (R6/G6) and effective switching rate. The point here is
only to show the sign question is BRANCH-DEPENDENT and to size the favorable corner.
"""
import numpy as np
hbar_c = 197.327  # MeV*fm

# --- pinned / order-level geometry-#3 inputs (repo) ---
d = 1.15                      # fm, uniform axial spacing (E_qq-set) [reasoning/2434]
s = d                         # bond separation ~ d (leading)
E_qq  = 66.0                  # MeV, DEEP core branch (alpha_s scale)   [order estimate]
E_ee  = 0.490                 # MeV, SHALLOW coat branch (registered ~490 keV) [2424]
m_qDP = 264.0                 # MeV, qDP constituent (color-factor-3 scale) [0703/0833]
lambdabar_eDP = 0.357         # fm, eDP reduced Compton wavelength [reasoning/1814]
m_eDP = hbar_c/lambdabar_eDP  # MeV  (mc^2 = hbar c / lambdabar) ~ 553 MeV

WINDOW = (0.179, 0.428)       # method-(a) stable eps band at delta=3/7 (Patch 2440)


def hbar_wA(E_bond, m):
    """Transverse bond-oscillation quantum: (hbar w_A)^2 = hbar^2 A/m, A = 2 E_bond/s^2."""
    recoil = hbar_c**2 / (m * s**2)      # MeV
    return np.sqrt(2 * E_bond * recoil)  # MeV


def classify(eps):
    lo, hi = WINDOW
    if lo <= eps <= hi:
        return "IN-WINDOW"
    return "unstable (too fast)" if eps < lo else "unstable (too slow)"


def main():
    print(f"eDP constituent scale (from lambdabar=0.357 fm): m_eDP c^2 = {m_eDP:.1f} MeV")
    print(f"method-(a) stable window (delta=3/7): eps in [{WINDOW[0]:.3f}, {WINDOW[1]:.3f}]\n")
    print(f"{'bond branch':16s} {'switch hop':10s} {'hbar_wA[MeV]':>12s} "
          f"{'hbar_wsw[MeV]':>13s} {'eps':>10s}   verdict")
    print("-" * 78)
    rows = [("deep core E_qq", E_qq, m_qDP, "qDP-hop", m_qDP),
            ("deep core E_qq", E_qq, m_qDP, "eDP-hop", m_eDP),
            ("shallow E_ee",  E_ee, m_eDP, "qDP-hop", m_qDP),
            ("shallow E_ee",  E_ee, m_eDP, "eDP-hop", m_eDP)]
    for lab, E, m_bond, swlab, m_sw in rows:
        hw = hbar_wA(E, m_bond)
        eps = (hw / m_sw) ** 2
        print(f"{lab:16s} {swlab:10s} {hw:12.2f} {m_sw:13.1f} {eps:10.2e}   {classify(eps)}")

    print("\nSensitivity of the favorable corner (deep core + qDP-hop) to E_qq:")
    for E in [40, 50, 66, 80, 100]:
        eps = (hbar_wA(E, m_qDP) / m_qDP) ** 2
        print(f"  E_qq={E:3d} MeV -> eps={eps:.3f}  ({classify(eps)})")
    print("  => favorable corner is PLAUSIBLE, not established: +-30% in E_qq spans")
    print("     unstable <-> comfortably in-window. R1 must pin E_qq, s, and w_sw.")

    print("\nDecisive R1 sub-questions (both must be DERIVED, not assumed):")
    print("  1. R6/G6: which bond fragments -- deep E_qq core or shallow E_ee coat?")
    print("            Only the deep-core branch is even in the stability window.")
    print("  2. effective w_sw: qDP-hop (favorable), eDP-hop (unstable), or a slower")
    print("            residence-suppressed rate? Compton-fast vs duty-cycle-suppressed.")
    print("  ...and R5/G4 netting vs the recomputed geom-#3 ponderomotive tensor still")
    print("     looms behind both and can flip the sign regardless.")


if __name__ == "__main__":
    main()
