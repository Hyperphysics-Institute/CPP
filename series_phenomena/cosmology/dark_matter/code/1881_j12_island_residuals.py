"""
1881 -- J12 pins: does Island I (S_c in [~0.005, 0.05], ruling point 0.035) survive the
surface-detector and Dewar ladder at m_rod = 25.3 GeV?  Sources fetched/pinned
5 July 2026 (CONV-003): Xu & Farrar arXiv:2112.00707 (Dewar/NBN19 interpretation,
full text); NFM18 ApJ 866 111; NBN19 ApJ 877 8; CRESST surface EPJC 77 637;
Mahdawi-Farrar JCAP 1712.004 / 1810.007.

CHANNELS AND VERDICTS AT 25.3 GeV:
 1. Dewar/NBN19 (+ NFM18 HST-drag, LHC-beam): source-stated reach m_X ~ 0.5-10 GeV;
    beyond, "the DM density is too low ... requiring a cross section that cannot be
    reached" (2112.00707 Sec.3.4). Quantified below: capture is EFFICIENT for our
    mass-matched rod but the barometric profile concentrates 25-GeV DM toward
    Earth's center, collapsing the surface density that drives all NFM18/NBN19
    channels. -> NOT CONSTRAINING at 25.3 GeV (pinned).
 2. CRESST 2017 surface run: gram-scale calorimeter targeting MeV-scale-to-few-GeV
    DM (EPJC 77 637 title/scope; used by MF18/XF21 for the low-mass window).
    -> not the operative probe at 25.3 GeV (pinned scope); no published high-mass
    surface analysis found to pin -- residual flag, not a live exclusion.
 3. DAMIC shallow (106.7 m, ~2.8e4 g/cm^2): shielding scales with overburden;
    computed below across the island.
 4. Earth heating: captured-KE power vs 44 TW geothermal budget.
 5. XQC thermalization-efficiency caveat (eps_th 0.01-1, MF18): affects the island's
    TOP edge (the S_c >~ 0.1 kill could soften for substrate-channel events); the
    HgTe-absorber channel (thermal calorimetry, eps_th ~ 1) carries multi-keV events
    at S_c = 1 regardless. Island itself unthreatened; flagged.
"""
import math
GEV = 1.0
M_ROD = 25.344       # GeV
RHO = 0.3            # GeV/cm^3
VREL = 2.3e7         # cm/s
RE = 6.371e8         # cm
TE_AGE = 4.55e9 * 3.156e7
KB_T300 = 2.585e-11  # GeV (300 K)

if __name__ == "__main__":
    print("=" * 78)
    print(" 1881 -- J12: island-I residual channels at m_rod = 25.3 GeV")
    print("=" * 78)
    # (1) Captured-atmosphere estimate (NFM18 machinery, our mass)
    mA = 20.0  # GeV, crust/atmosphere effective nucleus
    fKE = 2 * M_ROD * mA / (M_ROD + mA) ** 2
    N0 = math.log((11.2 / 230.0) ** 2) / math.log(1 - fKE)
    fcap = 2 / math.sqrt(math.pi) / math.sqrt(N0)
    nbar = 3 * fcap * RHO * VREL * TE_AGE / (4 * RE * M_ROD)
    H_km = (KB_T300 / (M_ROD * 1.09e-18)) * 1e-5  # kT/(m g), g in GeV/cm units -> km
    print("\n(1) DEWAR/NFM18 channels: f_KE = %.2f (mass-matched!), N0 = %.1f, f_cap = %.2f" % (fKE, N0, fcap))
    print("    volume-average captured density n_bar ~ %.1e /cm^3" % nbar)
    print("    BUT barometric scale height at 300 K: H ~ %.0f km << R_E -- 25-GeV DM" % H_km)
    print("    settles toward the center; surface density collapses by orders (2112.00707")
    print("    Fig 4 contours; source-stated reach 0.5-10 GeV). VERDICT: NOT CONSTRAINING.")
    # (4) Earth heating
    P = RHO * VREL * math.pi * RE ** 2 * 0.5 * (VREL / 3e10) ** 2 * fcap   # GeV/s
    print("\n(4) EARTH HEATING: captured-KE power ~ %.1e GeV/s = %.2f GW vs 44,000 GW" % (P, P * 1.602e-10 / 1e9))
    print("    geothermal budget. VERDICT: negligible.")
    # (3) DAMIC shielding across the island (scaling from the 1880 rock-collision solve)
    print("\n(3) DAMIC-SHALLOW SHIELDING (2.8e4 g/cm^2 = 0.065 x LZ overburden);")
    print("    collisions scale from the 1880 partial-wave rock numbers:")
    ref = {0.035: 1250.0, 0.01: 100.0, 0.005: 25.0}   # LZ-column collisions (1880)
    for sc, cLZ in sorted(ref.items()):
        cD = cLZ * 0.065
        print("    S_c = {:>6}: LZ collisions {:>6.0f} -> DAMIC {:>5.1f}  => {}".format(
            sc, cLZ, cD, "SHIELDED" if cD >= 10 else "unshielded (DAMIC applies)"))
    q = 20.0; ms = 7.764
    for sc in (0.01, 0.005):
        a = 0.188 * sc * ms ** 2 / (ms ** 2 + q ** 2)
        sn = 4 * math.pi * (a * 1e-13) ** 2
        print("    unshielded sigma_n(q~20 MeV) at S_c={:>5}: {:.1e} cm^2".format(sc, sn))
    print("    DAMIC-shallow floor at 25 GeV: UNPINNED (MF17/18 band digitization needed).")
    print("    => island BOTTOM EDGE (S_c <~ 0.01) carries the residual; the RULING POINT")
    print("       S_c = 0.035 is DAMIC-shielded (81 collisions) regardless.")
    print("\nSUMMARY: Island I survives every pinned channel at the ruling point 0.035.")
    print("Residual flags (J12'): (a) DAMIC floor pin for the island's bottom edge;")
    print("(b) no published high-mass surface-run analysis (CRESST scope is low-mass);")
    print("(c) XQC eps_th caveat affects the island's top edge only. Signature-space note")
    print("for DM-3: a deep-Earth thermalized rod population (n_bar ~ %.0e /cm^3," % nbar)
    print("center-concentrated) is predicted -- exotic-isotope/borehole phenomenology.")
    print("=" * 78)
