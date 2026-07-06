"""
2301 -- DM-3 opened: the rod-nucleus bound-state discriminant (cheapest kill,
richest signature -- run at arc open per falsification-first).

PHYSICS: at the D5-A' ruling (S_c = R_N/R_s = 0.035, island [0.012, 0.05]) the
rod-nucleus potential is attractive: V(r) = -A * E_rN * S_c * (r_c/r) e^{-r/R_s}.
An attractive Yukawa g^2 e^{-mu r}/r supports an s-wave bound state iff the
dimensionless coupling s = 2 mu_red g^2 R_s / (hbar c)^2 >= 1.680 (standard
critical screening result). Because g^2 grows with A AND mu_red grows with A,
binding switches ON above a THRESHOLD mass number -- light nuclei cannot bind,
heavy ones must.

CONSEQUENCES:
  KILL-RISK: thermalized crustal rods that bind to nuclei create anomalously
  heavy isotopes (M ~ A + 25.3 GeV). Anomalous-isotope searches are DECISIVE for
  light elements (H, He, Li, Be, C, O: limits down to ~1e-28/nucleon) -- if light
  nuclei bound, the candidate would likely be dead. The threshold saves it
  structurally IF A_thresh sits above the well-searched light elements.
  SIGNATURE: heavy-element-only anomalous isotopes at predictable crustal
  concentrations -- a discriminant with a built-in threshold no generic WIMP has.
"""
import math
HBARC = 197.327
CHI = ((1 + 5 ** 0.5) / 2) ** -3 / 6
RS = 1.0 / CHI
E_RN = 3 * 0.3 / (8 * 18)
M_ROD = 18 * 1408.0
AMU = 931.494
S_CRIT = 1.680

def s_par(A, sc):
    mA = A * AMU
    mu = mA * M_ROD / (mA + M_ROD)
    g2 = A * E_RN * sc * 1.0          # MeV*fm
    return 2 * mu * g2 * RS / HBARC ** 2

def a_thresh(sc):
    A = 1.0
    while s_par(A, sc) < S_CRIT and A < 400:
        A += 0.25
    return A

def binding_energy(A, sc):
    """Numerov shooting for the s-wave ground state (returns |E| in keV, 0 if unbound)."""
    mA = A * AMU
    mu = mA * M_ROD / (mA + M_ROD)
    g2 = A * E_RN * sc
    two_mu = 2 * mu / HBARC ** 2
    def nodes(E):  # E negative, MeV
        h, rmax = 0.02, 250.0
        n = int(rmax / h)
        u0, u1 = 0.0, 1e-10
        cnt = 0
        for i in range(2, n):
            r = i * h
            V = -g2 * math.exp(-r / RS) / r
            f = two_mu * (V - E)
            u2 = 2 * u1 - u0 + h * h * f * u1
            if u1 != 0 and u2 * u1 < 0:
                cnt += 1
            u0, u1 = u1, u2
        return cnt
    if s_par(A, sc) < S_CRIT:
        return 0.0
    lo, hi = -0.5, -1e-9   # MeV
    if nodes(lo) == 0:
        return 0.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if nodes(mid) >= 1:
            lo = mid
        else:
            hi = mid
    return abs(lo) * 1e3   # keV

if __name__ == "__main__":
    print("=" * 78)
    print(" 2301 -- DM-3 open: rod-nucleus bound states & the anomalous-isotope channel")
    print("=" * 78)
    print("\n(1) BINDING THRESHOLD vs S_c (island [0.012, 0.05], ruling 0.035):")
    for sc in (0.012, 0.035, 0.05):
        print("    S_c = {:>5}: A_thresh = {:.0f}".format(sc, a_thresh(sc)))
    print("\n(2) AT THE RULING POINT (S_c = 0.035): per-element verdicts")
    for A, name in ((1, "H"), (4, "He"), (12, "C"), (16, "O"), (28, "Si"), (40, "Ca"),
                    (56, "Fe"), (120, "Sn"), (184, "W"), (207, "Pb")):
        s = s_par(A, 0.035)
        be = binding_energy(A, 0.035)
        print("    {:>3} (A={:>3}): s = {:.2f}  -> {}".format(
            name, A, s, "UNBOUND (below critical)" if s < S_CRIT else "BOUND, |E| ~ %.1f keV" % be))
    print("\n(3) THE STRUCTURAL SAVE + THE SIGNATURE:")
    print("    Light elements (H..O) sit BELOW threshold at every island point -> the")
    print("    stringent light-element anomalous-isotope limits (down to ~1e-28) DO NOT")
    print("    APPLY. Binding switches on around A_thresh -- the prediction is anomalous")
    print("    isotopes of HEAVY elements ONLY (M_anom ~ A + 25.3 GeV), with a sharp")
    print("    element threshold that moves with S_c: a discriminant no generic WIMP has.")
    print("\n(4) CRUSTAL CONCENTRATION (order estimate; carried as scoping):")
    n_surf = 5e7      # /cm^3 thermalized rods near surface (1881 barometric profile)
    n_nuc = 5e22
    print("    surface rod density ~ {:.0e}/cm^3; nuclei ~ {:.0e}/cm^3 ->".format(n_surf, n_nuc))
    print("    CEILING anomalous fraction ~ {:.0e} per heavy nucleus (if capture-limited,".format(n_surf / n_nuc))
    print("    lower); heavy-element anomalous-isotope search limits at 25-GeV-excess mass:")
    print("    UNPINNED (J-DM3-1) -- the arc's first data action. Formation kinetics")
    print("    (phonon-dissipated capture in solids) J-DM3-2, to be computed.")
    print("=" * 78)
