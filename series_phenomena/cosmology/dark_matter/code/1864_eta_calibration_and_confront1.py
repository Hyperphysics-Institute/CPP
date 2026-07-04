"""
1864 -- OPEN-SS-43 Phase 1: calibrate the Sea's residual-channel response eta from the
dwarf-coring requirement (founder-directed inversion, TLA 3 July 2026), and run
CONFRONT-1: does the calibrated residual survive nucleon-nucleon empirics?

Framework: eta = residual-channel response amplitude relative to the color channel;
R_s = r_color / eta under linear (Debye-like, N-flat) screening. r_color = 1.0 fm
[SF-5 confinement anchor; JUDGMENT-2 tags the 0.85-1.0 fm spread]. Capture model = 1858
pipeline. Calibration target: sigma/m(dwarf, v=50 km/s) in [1, 2] cm^2/g central
(corpus v1.1), [0.6, 3] wide. Both D2 E_c-scalings carried (flat 0.3 MeV; additive
0.02*N MeV, both tagged as 1858-era anchors pending mechanism derivation).

CONFRONT-1 model: residual coupling pairwise-additive in qCP count (rod core 8N qCPs,
nucleon 3 qCPs) => per-qCP-pair strength g2 = E_c(N)/(8N)^2; NN contact strength
E_NN = 9*g2; same N-flat screening length. Born-level observables: shift in np
scattering length; coherent binding shift in heavy nuclei.
"""
import math

C = 299792.458; MeV_g = 1.783e-27; RC = 1.0; M_EL = 1408.0
CHI = ((1 + 5**0.5) / 2) ** -3 / 6
HBARC = 197.327  # MeV fm

def bmax(v, Ec, Rs, N):
    mu = N * M_EL / 2
    KE = 0.5 * mu * (v / C) ** 2
    V = lambda r: (Ec * RC / r) * math.exp(-r / Rs)
    if V(RC) < KE: return RC
    lo, hi = RC, 3000.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if V(mid) > KE: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)

def som(v, Ec, Rs, N):
    b = bmax(v, Ec, Rs, N)
    return math.pi * b * b * 1e-26 / (N * M_EL * MeV_g)

def calibrate_Rs(target, Ec, N, v=50.0):
    """Solve som(v)=target for R_s by bisection (som is monotonic in R_s)."""
    lo, hi = 1.0, 200.0
    if som(v, Ec, lo, N) > target: return None      # over-cores even at 1 fm
    if som(v, Ec, hi, N) < target: return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if som(v, Ec, mid, N) < target: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)

if __name__ == "__main__":
    print("=" * 78)
    print(" 1864 -- eta calibration (founder-directed inversion) + CONFRONT-1")
    print("=" * 78)

    # Phase 1: eta(N) calibration -------------------------------------------------
    print("\n(1) CALIBRATION: R_s and eta = 1fm/R_s such that sigma/m(50 km/s) hits target")
    print("    E_c model 'flat' = 0.3 MeV;  'additive' = 0.02*N MeV  [D2 both carried]")
    print(f"    {'N':>3} {'model':>9} {'Rs(sig=1)':>10} {'Rs(sig=2)':>10} "
          f"{'eta(sig=1)':>11} {'eta(sig=2)':>11}  cluster sig/m @Rs(sig=1)")
    results = {}
    for N in (5, 8, 12, 15, 20):
        for label, Ec in (("flat", 0.30), ("additive", 0.02 * N)):
            r1 = calibrate_Rs(1.0, Ec, N); r2 = calibrate_Rs(2.0, Ec, N)
            if r1 is None or r2 is None:
                print(f"    {N:>3} {label:>9}   -- no solution in [1,200] fm (over/under-cores) --")
                continue
            e1, e2 = 1.0 / r1, 1.0 / r2
            cl = som(1500, Ec, r1, N)
            results[(N, label)] = (r1, r2, e1, e2)
            print(f"    {N:>3} {label:>9} {r1:>9.1f}f {r2:>9.1f}f {e1:>11.4f} {e2:>11.4f}      {cl:8.4f}")
    print(f"    chi = phi^-3/6 = {CHI:.4f}  (eta = chi would mean R_s = {1/CHI:.1f} fm)")

    # Phase 2: CONFRONT-1 ---------------------------------------------------------
    print("\n(2) CONFRONT-1: nucleon-scale residual under pairwise-additive qCP coupling")
    print("    per-qCP-pair g2 = E_c/(8N)^2; E_NN = 9*g2; same lambda (N-flat screening)")
    mu_NN = 938.9 / 2.0
    pref = 2 * mu_NN / HBARC ** 2          # MeV^-1 fm^-2 (Born prefactor)
    print(f"    {'N':>3} {'model':>9} {'lambda':>8} {'E_NN(keV)':>10} {'d a_np (fm)':>12}"
          f" {'dB(A=200) MeV':>14}")
    for (N, label), (r1, r2, e1, e2) in sorted(results.items()):
        Ec = 0.30 if label == "flat" else 0.02 * N
        for lam in (r1, r2):
            g2 = Ec / (8 * N) ** 2
            E_NN = 9 * g2                              # MeV at 1 fm contact
            # Born shift in scattering length: da ~ (2mu/hbar^2) * Int V r^2 dr
            #   Int (E_NN*rc/r) e^(-r/lam) r^2 dr = E_NN * rc * lam^2
            da = pref * E_NN * RC * lam ** 2           # fm
            # coherent heavy-nucleus shift: pairs * <V> at typical separation ~4 fm
            A = 200; pairs = A * (A - 1) / 2
            Vtyp = (E_NN * RC / 4.0) * math.exp(-4.0 / lam)
            dB = pairs * Vtyp
            print(f"    {N:>3} {label:>9} {lam:>7.1f}f {E_NN*1e3:>10.3f} {da:>12.2e} {dB:>14.3f}")
    print("    Empirical sensitivity anchors [JUDGMENT-5, order-of-magnitude]:")
    print("      a_np triplet = 5.424(3) fm -> |da| detectable ~3e-3 fm")
    print("      heavy-nucleus mass fits good to ~0.5-1 MeV -> |dB| detectable ~1 MeV")

    print("\n" + "=" * 78)
    print(" READ-OUT: see reasoning/1864.md for the verdicts and judgment ledger.")
    print("=" * 78)
