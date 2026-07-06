"""
1873 -- Formation-lane N (queue item 3, SCOPING): does reversible aggregation land
N ~ 15-20 naturally?  Isodesmic living-polymer equilibrium + kinetic freeze-out check.

Equilibrium (reversible linear aggregation, bond energy E_b):
    <N>(T) ~ sqrt(phi * exp(E_b/kT))   for <N> >> 1,
phi = element site-occupancy fraction ~ n_el(T) * v_el.  Comoving scaling
n_el(T) ~ n_el,0 * (T/T_0)^3 (entropy/g* factors O(1), flagged).  Inputs, all pinned:
E_b = E_ee = 0.9 MeV [1813 -- candidate growth bond; 0860 window 0.8 keV-2 MeV
flagged], m_el = 1408 MeV, v_el ~ d^3 with d = 1.0-1.3 fm (J8 pin, 1812/0835),
rho_DM,0 = 1265 eV/cm^3.

INVERSION: what kT_form gives <N> = 15-20?  Then the kinetic check: is the
aggregation reaction still fast (rate >> H) at that temperature?  If yes, equilibrium
TRACKS and N keeps growing as T falls -- the equilibrium inversion alone does not
freeze N, and the cap must be kinetic or collisional. Reported honestly either way.
"""
import math
E_B = 0.9e6          # eV
M_EL = 1408e6        # eV
T0 = 2.348e-4        # eV (CMB today)
RHO0 = 1265.0        # eV/cm^3
HBARC_CM = 197.327e6 * 1e-13   # eV cm
MPL = 1.22e28        # eV
C_CMS = 2.998e10

def phi(T_eV, d_fm):
    n = (RHO0 / M_EL) * (T_eV / T0) ** 3          # /cm^3
    return n * (d_fm * 1e-13) ** 3

def Nbar(T_eV, d_fm):
    return math.sqrt(max(phi(T_eV, d_fm), 1e-300) * math.exp(min(E_B / T_eV, 600)))

if __name__ == "__main__":
    print("=" * 74)
    print(" 1873 -- formation-lane N: equilibrium inversion + kinetic check")
    print("=" * 74)
    print("\n(1) INVERSION: kT_form for <N> = 15 / 18 / 20  (d_el spread 1.0-1.3 fm)")
    for d in (1.0, 1.15, 1.3):
        row = "    d={:.2f} fm: ".format(d)
        for Ntgt in (15, 18, 20):
            lo, hi = 1e3, 1e6
            for _ in range(200):
                mid = math.sqrt(lo * hi)
                if Nbar(mid, d) > Ntgt: lo = mid
                else: hi = mid
            row += "  N={}: kT = {:.1f} keV".format(Ntgt, math.sqrt(lo * hi) / 1e3)
        print(row)
    print("    <- compare: the 0860 ambient-thermal hook kT_amb <~ 19 keV.")
    print("\n(2) KINETIC CHECK at kT ~ 17 keV: rate vs Hubble")
    T = 17e3
    n = (RHO0 / M_EL) * (T / T0) ** 3
    v = math.sqrt(2 * T / M_EL)                       # units of c
    # element-element geometric-ish sigma at thermal v via coat radius:
    ke = 0.5 * (M_EL / 2) * v * v                     # eV
    b = 1.0
    for _ in range(200):                              # solve 0.9e6*(1/b)e^{-b} = ke
        f = 0.9e6 * math.exp(-b) / b
        b *= 1.05 if f > ke else 0.95
    sig = math.pi * (b * 1e-13) ** 2                  # cm^2
    rate = n * sig * v * C_CMS                        # 1/s
    H = 1.66 * math.sqrt(10.0) * T * T / MPL          # eV
    H_s = H / 6.582e-16                               # 1/s
    print("    n = {:.2e}/cm^3, v = {:.1e} c, b_eff = {:.1f} fm, sigma = {:.1e} cm^2".format(n, v, b, sig))
    print("    rate = {:.2e}/s vs H = {:.2e}/s  =>  rate/H = {:.1e}".format(rate, H_s, rate / H_s))
    print("\nREAD-OUT: the equilibrium inversion lands kT_form ~ 16-18 keV -- right at the")
    print("0860 <~19 keV hook (log-insensitive to phi: factor-10 in v_el shifts kT ~2%).")
    print("BUT rate/H >> 1 there: equilibrium TRACKS, so N does not freeze at 15-20 by")
    print("equilibrium alone -- growth continues until a kinetic/collisional cap. The")
    print("coincidence is REGISTERED, not claimed: the open thread is the cap mechanism")
    print("(candidates: bond-breaking re-equilibration shutoff at kT ~ E_bond_eff/ln(...),")
    print("collisional tail-pruning at virialization, or E_b << 0.9 MeV per 0860 window).")
    print("=" * 74)
