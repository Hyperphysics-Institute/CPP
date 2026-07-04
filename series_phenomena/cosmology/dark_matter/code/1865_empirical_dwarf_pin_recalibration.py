"""
1865 -- OPEN-SS-43 queued action 1 (data-trumps mandate, TLA 3 July 2026): pin the
empirical dwarf coring sigma/m from published SIDM analyses, then rerun the 1864
calibration + chi verdict + CONFRONT-1 at the pinned band.

EMPIRICAL LEDGER (web-sourced 4 July 2026; provenance per CONV-003):
  FITS at dwarf/galaxy velocities (v ~ 30-100 km/s):
    Kaplinghat-Tulin-Yu 2016 (PRL 116, 041302; arXiv:1508.03339): preferred fit
        sigma/m ~ 2 cm^2/g on galaxy scales (falling to ~0.1 at clusters).
    Ren-Kwa-Kaplinghat-Yu 2019 (PRX 9, 031020; arXiv:1808.05695): ~3 cm^2/g fits the
        diversity of galactic rotation curves.
    Elbert et al. 2015 (MNRAS 453, 29; arXiv:1412.1477): at V_max ~ 40 km/s the FULL
        range sigma/m = 0.5-50 cm^2/g produces viable 300-1000 pc cores (TBTF-solving);
        LARGEST/lowest-density cores at sigma/m ~ 5-10; even 50 remains viable
        (mild core-collapse). Dwarf coring is a BROAD BAND, not a point.
  FITS at MW-dSph velocities (v ~ 10-40 km/s, LOWER than the 50 km/s pin):
    Correa 2021 (MNRAS 503, 920; arXiv:2007.02958): 30-50 cm^2/g (Carina/Fornax) up to
        70-100 cm^2/g (denser dSphs).
    Roberts-Kaplinghat-Valli-Yu 2024 (arXiv:2407.15005): 20-40 cm^2/g regime for LSB
        dwarf halos (gravothermal diversity amplification).
  BOUNDS at group/cluster velocities:
    Sagunski et al. 2021 (arXiv:2006.12515): groups (v ~ 1150) 0.5 +/- 0.2;
        clusters 0.19 +/- 0.09, < 0.35 (95% CL).
    Eckert et al. 2022 (A&A, X-COP): clusters < 0.19 (95% CL) at v ~ 1000.
    Andrade et al. 2022 (strong lensing): clusters < 0.13 (95% CL)  [tightest].

PIN ADOPTED (moves JUDGMENT-3):
  J3' central  : sigma/m(50 km/s) in [1, 5]  cm^2/g  (rotation-curve fits 2-3 bracket;
                 Elbert core-size optimum 5-10 straddles the upper edge)
  J3' extended : sigma/m(50 km/s) in [0.5, 10] cm^2/g (Elbert viability, low edge of
                 the dSph-regime fits mapped up to 50 km/s)
  The old corpus [1, 2] band was the LOW EDGE of the empirical window, not its center.

Pipeline identical to 1864 (V(r) = (E_c r_c / r) e^{-r/R_s}, r_c = 1 fm, capture
boundary V(b_max) = KE, sigma = pi b^2 / m_rod); this script only moves the target.
"""
import math

C = 299792.458; MeV_g = 1.783e-27; RC = 1.0; M_EL = 1408.0
CHI = ((1 + 5**0.5) / 2) ** -3 / 6      # 0.0393...
HBARC = 197.327

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
    lo, hi = 1.0, 400.0
    if som(v, Ec, lo, N) > target: return None
    if som(v, Ec, hi, N) < target: return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if som(v, Ec, mid, N) < target: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)

def confront1(N, Ec, lam):
    """Born-level NN observables under pairwise-additive qCP coupling (1864 model)."""
    mu_NN = 938.9 / 2.0
    pref = 2 * mu_NN / HBARC ** 2
    g2 = Ec / (8 * N) ** 2
    E_NN = 9 * g2
    da = pref * E_NN * RC * lam ** 2
    A = 200; pairs = A * (A - 1) / 2
    dB = pairs * (E_NN * RC / 4.0) * math.exp(-4.0 / lam)
    return E_NN, da, dB

if __name__ == "__main__":
    print("=" * 78)
    print(" 1865 -- empirical dwarf pin -> recalibration, chi verdict, CONFRONT-1 rerun")
    print("=" * 78)

    # (1) Recalibration at the pinned band -----------------------------------------
    print("\n(1) RECALIBRATION at pinned targets sigma/m(50 km/s) = 1, 2, 5, 10 cm^2/g")
    print("    (old corpus band was [1,2]; pinned central [1,5]; extended [0.5,10])")
    targets = (1.0, 2.0, 5.0, 10.0)
    hdr = "    {:>3} {:>9}".format("N", "model")
    for t in targets: hdr += "  Rs(s={:<4g})  eta(s={:<4g})".format(t, t)
    print(hdr)
    cal = {}
    for N in (5, 8, 12, 15, 20):
        for label, Ec in (("flat", 0.30), ("additive", 0.02 * N)):
            row = "    {:>3} {:>9}".format(N, label)
            for t in targets:
                r = calibrate_Rs(t, Ec, N)
                if r is None:
                    row += "   {:>8}   {:>9}".format("--", "--")
                else:
                    cal[(N, label, t)] = r
                    row += "   {:>7.1f}f   {:>9.4f}".format(r, 1.0 / r)
            print(row)

    # (2) chi verdict under the pin -------------------------------------------------
    print("\n(2) CHI VERDICT: sigma/m(50 km/s) delivered by eta = chi (R_s = %.1f fm)" % (1/CHI))
    print("    vs pinned bands: central [1,5], extended [0.5,10]")
    Rs_chi = 1.0 / CHI
    for N in (5, 8, 12, 15, 20):
        for label, Ec in (("flat", 0.30), ("additive", 0.02 * N)):
            s50 = som(50.0, Ec, Rs_chi, N)
            in_c = "IN-CENTRAL" if 1.0 <= s50 <= 5.0 else (
                   "IN-EXTENDED" if 0.5 <= s50 <= 10.0 else "OUT")
            cl = som(1500.0, Ec, Rs_chi, N)
            print("    N={:>2} {:>9}: sigma_dwarf = {:6.2f}  [{}]   cluster = {:.4f}".format(
                N, label, s50, in_c, cl))

    # (3) CONFRONT-1 rerun at the widened calibration --------------------------------
    print("\n(3) CONFRONT-1 at pinned-band calibrations (dB(A=200) in MeV; bound ~1 MeV)")
    print("    {:>3} {:>9} {:>7} {:>9} {:>12} {:>10}".format(
        "N", "model", "target", "lambda", "d a_np (fm)", "dB(A=200)"))
    for (N, label, t) in sorted(cal.keys()):
        Ec = 0.30 if label == "flat" else 0.02 * N
        lam = cal[(N, label, t)]
        E_NN, da, dB = confront1(N, Ec, lam)
        flag = "  <-- TENSION" if dB > 1.0 else ""
        print("    {:>3} {:>9} {:>7g} {:>6.1f}f {:>12.2e} {:>10.3f}{}".format(
            N, label, t, lam, da, dB, flag))

    # (4) Cluster-safety check vs tightest bound --------------------------------------
    print("\n(4) CLUSTER PREDICTION vs tightest bound (Andrade 2022: < 0.13 cm^2/g, 95%)")
    worst = 0.0
    for (N, label, t), lam in cal.items():
        Ec = 0.30 if label == "flat" else 0.02 * N
        cl = som(1500.0, Ec, lam, N)
        worst = max(worst, cl)
    print("    max cluster sigma/m over ALL pinned-band calibrations = {:.4f}  ({})".format(
        worst, "PASSES < 0.13" if worst < 0.13 else "FAILS"))

    print("\n" + "=" * 78)
    print(" READ-OUT: see reasoning/1865.md for verdicts and the updated judgment ledger.")
    print("=" * 78)
