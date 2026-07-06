"""
1887 -- SI-1 verify: implements the forward-map system F1-F7 (SI-1_unknowns_and_
forward_maps.md), performs the CONV-004 counting, extracts the pre-scan substrate
inferences (X2, X3, D_st), and runs the crude task-2 preview MC existence scan
(kappa in [1/3,3], log-priors of SI-1 section 2). All tags per CONV-004.
"""
import math, random
HBARC = 197.327
CHI = ((1 + 5 ** 0.5) / 2) ** -3 / 6
MS = CHI * HBARC / 1.0            # M1 MEASURED, 7.764 MeV (r_c = a units, J-SI-1)
SC_LO, SC_C, SC_HI = 0.005, 0.035, 0.05   # M2 MEASURED
E_EE, E_C, E_HDP = 0.9, 0.3, 150.0        # M3, M4, M6 PINNED
A_LO, A_HI = 1.0, 1.3                     # M5 PINNED
RN, RS = 0.9, 1.0 / CHI

random.seed(41)
def loguni(lo, hi): return math.exp(random.uniform(math.log(lo), math.log(hi)))

if __name__ == "__main__":
    print("=" * 78)
    print(" 1887 -- SI-1: forward maps, counting, pre-scan inferences, existence preview")
    print("=" * 78)
    print("\n(1) PRE-SCAN SUBSTRATE INFERENCES (kappa-band O(1) uncertainties):")
    print("    alpha_e/alpha_q = (k3/k2) E_ee/E_hDP  = {:.1e} x O(1)".format(E_EE / E_HDP))
    print("    C_r (cancellation residual) = (k3/8k4) E_c/E_hDP = {:.1e} x O(1)".format(E_C / (8 * E_HDP)))
    print("      -> the quiescent Sea cancels the colour channel to ~2.5 parts in 1e4")
    print("    D_st = S_c/(k5 R_N/R_s): center {:.2f} -> D_st = O(1): the confined singlet".format(SC_C / (RN / RS)))
    print("      presents an essentially fully STATIC leading moment [MEASURED-inference]")
    print("\n(2) COUNTING: 8 unknowns / 6 hard targets -> under-determined by 2;")
    print("    pinned COMBINATIONS X1 = a_q n C_r S_p/E_z, X2 = a_q/a, X3 = C_r, D_st.")
    print("\n(3) EXISTENCE PREVIEW (MC, 200k samples, accept iff ALL hard targets in-band):")
    NTRY = 200000
    acc = []
    for _ in range(NTRY):
        aq = loguni(1e-4, 10); ae = loguni(1e-4, 10)
        n = loguni(1e-3, 10); Ez = loguni(1e-3, 1e3)     # MeV
        Cr = loguni(1e-6, 1); Sp = loguni(1e-2, 1)
        Dst = loguni(1e-3, 1); a = loguni(A_LO, A_HI)
        k = [loguni(1 / 3, 3) for _ in range(5)]
        ok = True
        # F3: E_hDP
        if not (1 / 3 < (k[2] * aq * HBARC / a) / E_HDP < 3): ok = False
        # F2: E_ee
        if ok and not (1 / 3 < (k[1] * ae * HBARC / a) / E_EE < 3): ok = False
        # F4: E_c
        if ok and not (1 / 3 < (k[3] * Cr * 8 * aq * HBARC / a) / E_C < 3): ok = False
        # F1: m_s^2
        if ok:
            ms2 = k[0] * 4 * math.pi * aq * HBARC ** 3 * n * Cr * Sp / Ez
            if not (1 / 9 < ms2 / MS ** 2 < 9): ok = False
        # F5: S_c
        if ok and not (SC_LO < k[4] * Dst * RN / RS < SC_HI): ok = False
        if ok:
            acc.append((aq, ae, n, Ez, Cr, Sp, Dst, a))
    print("    accepted: {} / {}  ({:.2e})".format(len(acc), NTRY, len(acc) / NTRY))
    if acc:
        names = ["alpha_q", "alpha_e", "n [fm^-3]", "E_z [MeV]", "C_r", "S_p", "D_st", "a [fm]"]
        print("    EXISTENCE: NON-EMPTY. Accepted-region marginals (min / median / max):")
        for i, nm in enumerate(names):
            v = sorted(x[i] for x in acc)
            print("      {:>10}: {:.2e} / {:.2e} / {:.2e}".format(nm, v[0], v[len(v) // 2], v[-1]))
        fo = sorted(x[2] * x[7] ** 3 for x in acc)
        print("      {:>10}: {:.2e} / {:.2e} / {:.2e}   (occupancy n a^3)".format(
            "f_occ", fo[0], fo[len(fo) // 2], fo[-1]))
        nsz = sorted(x[2] * x[5] / x[3] for x in acc)
        print("      {:>10}: {:.2e} / {:.2e} / {:.2e}   (n S_p/E_z, the X1 core)".format(
            "nSp/Ez", nsz[0], nsz[len(nsz) // 2], nsz[-1]))
    else:
        print("    EXISTENCE: EMPTY at this resolution -- structural-falsification flag.")
    print("=" * 78)
