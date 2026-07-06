"""
1872 -- CONFRONT-2: consistency of the DM-sector Sea response (eta = chi, R_s = 25.4 fm)
with the CC-sector correlation-length route (rho_Lambda ~ 1/xi^2, xi -> event horizon,
carried by the GAPLESS |SSV| mode -- SR-5d, Patches 1107-1108/1165-1166 adjudication).

The question: the DM capture channel requires the Sea's E_qq-residual response to be
SCREENED at R_s ~ 25 fm; the CC route requires the Sea's ground-state |SSV| coherence
to be MACROSCOPIC (xi ~ R_h ~ 1e26 m). Same Sea -- conflict?

Resolution tested here (channel decomposition):
  - Screened Yukawa e^{-r/R_s} <=> the color-residual response channel is GAPPED with
    effective mass m_s = hbar*c / R_s. At eta = chi = phi^-3/6: R_s = r_c/chi, so
        m_s = chi * (hbar c / r_c)  -- the gap, in rung-scale units, IS chi.
  - The CC coherence lives in the GAPLESS |SSV| scalar (icosahedral 5-design result,
    1107-1108): gapless => power-law correlations => xi set by the IR boundary (R_h),
    not by any microscopic mass. A gapped channel contributes only e^{-m_s r} terms,
    irrelevant at cosmological r.
  => The two sectors are consistent IFF the E_qq residual is NOT the gapless mode.
     Different quantum numbers (color-sector polarization vs |SSV| scalar): it is not.
  - D-FRAG spot check: do DM rods fragment the ground-state coherence? They are
    localized excesses (Step B: excesses gravitate; they do not decohere the ground
    state any more than baryons, which the arc already accommodates). Mean inter-rod
    spacing at the cosmic mean is computed below for scale.
"""
import math
HBARC = 197.327  # MeV fm
CHI = ((1 + 5 ** 0.5) / 2) ** -3 / 6
RC = 1.0
R_H = 1.6e26     # m, future event horizon scale (order)
if __name__ == "__main__":
    print("=" * 74)
    print(" 1872 -- CONFRONT-2: DM screening channel vs CC coherence channel")
    print("=" * 74)
    Rs = RC / CHI
    ms = HBARC / Rs
    print("\n(1) The DM gap: R_s = r_c/chi = {:.2f} fm  =>  m_s = hbar c/R_s = {:.3f} MeV".format(Rs, ms))
    print("    identically m_s = chi * (hbar c / r_c) = {:.3f} MeV".format(CHI * HBARC / RC))
    print("    Calibration band (1864-65, R_s ~ 8-32 fm): m_s ~ {:.1f}-{:.1f} MeV".format(HBARC/32, HBARC/8))
    print("\n(2) Scale hierarchy demanded of the Sea: xi / R_s = {:.1e}".format(R_H * 1e15 / Rs))
    print("    Reconciled iff channels are distinct: GAPPED color-residual response")
    print("    (this sector) vs GAPLESS |SSV| scalar (CC sector, 5-design result).")
    print("    Gapped channel's contribution at cosmological r: exp(-m_s r) -> 0. No leak.")
    print("\n(3) D-FRAG spot check: rod excesses vs ground-state coherence")
    rho_dm = 1265.0          # eV/cm^3 cosmic mean
    m_rod = 18 * 1408e6      # eV
    n_rod = rho_dm / m_rod
    spacing = (1.0 / n_rod) ** (1 / 3)
    print("    n_rod = {:.2e} /cm^3  => mean spacing ~ {:.0f} cm ~ localized excesses,".format(n_rod, spacing))
    print("    same footing as baryons (Step B) -- no new fragmentation channel.")
    print("\nVERDICT: NO CONFLICT -- channel decomposition consistent; the DM sector")
    print("SHARPENS the de-novo target: derive a chi * (hbar c / r_c) = 7.8 MeV gap in")
    print("the Sea's color-residual channel while the |SSV| scalar stays gapless.")
    print("NOT a derivation of either side; a consistency check with the target pinned.")
    print("=" * 74)
