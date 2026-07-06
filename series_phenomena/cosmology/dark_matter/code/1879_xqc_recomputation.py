"""
1879 -- CONFRONT-3 task 1: XQC recomputation for the CPP rod (light-mediator
composite), replacing the contact-interaction mapping with the actual scattering
problem. All experiment parameters from Erickcek et al. 2007 (PRD 76 042007),
fetched and pinned 5 July 2026.

WHY BORN FAILS / WHAT IS COMPUTED: the coherent Born scattering length on Hg
(~900 fm) exceeds the mediator range R_s = 25.4 fm -- the Born series diverges and
published contact-mapped boundaries cannot be trusted either way. We solve the
radial Schrodinger equation (Numerov) for the rod-nucleus potential and obtain
phase shifts, dsigma/dOmega -> dsigma/dE_R, folded through the XQC exposure.

MODEL (registered quantities only; J4 pairwise additivity carries this sector):
  V(r) = sign * A_nuc * E_rN * (r_c/r) e^{-r/R_s},  E_rN = 3 E_c/(8N), R_s = r_c/chi
  - rod extension folded at potential level (line source of length L = (N-1)*1.15 fm,
    orientation-averaged -> spherical shell smearing)  [carried vs point]
  - nuclear finite size via Helm |F(q)|^2 on dsigma/dOmega
  - sign: attractive (capture-channel heritage) AND repulsive both carried
XQC (pinned): 34 pixels; per-pixel layers (area cm^2 total, nuclei/cm^2 column):
  HgTe absorber 0.96um: 0.34, Hg 1.43e18 + Te 1.43e18
  Si substrate 14um:    0.34, Si 6.99e19
  Si pixel body 12um:   0.085, Si 5.99e19
  Si spacer 7um:        0.0204, Si 3.50e19
  entrance column 21.16 cm^2; N_dm = (rho/m)*2.5e10 cm^3 (their normalization);
  halo v0=220, vesc=584, v_det=233.8 km/s; exposure 100.7 s folded into N_dm.
  Observed bins (Table I) with sensitivity f: see BINS below; >4 keV rate = 60.
VERDICT CRITERION (conservative, transparent): a bin with predicted counts
  > observed + 5*sqrt(observed+1) => EXCLUDED-class tension (their X^2 90% CL is
  stricter); all bins under observed => XQC-SAFE (background unsubtracted).
"""
import math

HBARC = 197.327; RC = 1.0
CHI = ((1 + 5 ** 0.5) / 2) ** -3 / 6
RS = RC / CHI
M_EL = 1408.0; AMU = 931.494
N_ROD = 18; M_ROD = N_ROD * M_EL
E_C = 0.30
E_RN = 3.0 * E_C / (8 * N_ROD)          # MeV at r_c
L_ROD = (N_ROD - 1) * 1.15              # fm (J8 pin)
V0, VESC, VDET = 220.0, 584.0, 233.8    # km/s
CKMS = 299792.458
RHO = 0.3e3                             # MeV/cm^3
NDM = (RHO / M_ROD) * 2.5e10            # particles encountered (Erickcek norm.)
ENTR = 21.16                            # cm^2

TARGETS = {  # name: (A, mass MeV)
    "Hg": (200.6, 200.6 * AMU), "Te": (127.6, 127.6 * AMU), "Si": (28.09, 28.09 * AMU)}
LAYERS = [  # (target, area cm^2, column nuclei/cm^2)
    ("Hg", 0.34, 1.43e18), ("Te", 0.34, 1.43e18),
    ("Si", 0.34, 6.99e19), ("Si", 0.085, 5.99e19), ("Si", 0.0204, 3.50e19)]
BINS = [(29, 36, 0, 0.3815), (36, 128, 11, 0.5083), (128, 300, 129, 1.0),
        (300, 540, 80, 1.0), (540, 700, 90, 1.0), (700, 800, 32, 1.0),
        (800, 945, 48, 1.0), (945, 1100, 31, 1.0), (1100, 1310, 30, 1.0),
        (1310, 1500, 29, 1.0), (1500, 1810, 32, 1.0), (1810, 2505, 15, 1.0)]
SAT = (4000.0, 60)


def shell_pot(r, a, Rs):
    """Screened potential of a unit spherical shell radius a at distance r (x r_c)."""
    return (Rs / (2 * a * r)) * (math.exp(-abs(r - a) / Rs) - math.exp(-(r + a) / Rs))


def make_V(A, sign, folded=True, ngrid=24):
    C = sign * A * E_RN * RC
    if not folded:
        return lambda r: C * math.exp(-r / RS) / r
    aa = [(i + 0.5) * (L_ROD / 2) / ngrid for i in range(ngrid)]
    w = 1.0 / ngrid
    def V(r):
        s = 0.0
        for a in aa:
            s += w * shell_pot(r, a, RS)
        return C * s
    return V


def phase_shifts(V, mu, k, lmax, rmax=180.0, h=0.08):
    """Numerov, numpy-vectorized over l; match to Riccati-Bessel at two radii."""
    import numpy as np
    two_mu = 2 * mu / HBARC ** 2
    n = int(rmax / h)
    rs = np.arange(1, n + 1) * h
    Vg = np.array([V(r) for r in rs])
    ls = np.arange(lmax + 1)
    # f(l, r) = l(l+1)/r^2 + 2mu V - k^2   shape (L, n)
    F = ls[:, None] * (ls[:, None] + 1) / rs[None, :] ** 2 + two_mu * Vg[None, :] - k * k
    W = 1 - h * h / 12 * F
    u_prev = np.zeros(lmax + 1)
    u_cur = np.full(lmax + 1, 1e-20)
    r1i, r2i = n - 40, n - 5
    u1 = np.zeros(lmax + 1); u2 = np.zeros(lmax + 1)
    for i in range(1, n):
        u_next = ((12 - 10 * W[:, i - 1 + 0]) * u_cur - W[:, i - 2 + 0] * u_prev) / W[:, i]
        # note: index shift -- W[:, i-1] multiplies u_cur at r_i; use standard numerov indexing
        u_prev, u_cur = u_cur, u_next
        big = np.abs(u_cur) > 1e250
        if big.any():
            u_cur = np.where(big, u_cur * 1e-250, u_cur)
            u_prev = np.where(big, u_prev * 1e-250, u_prev)
        if i == r1i - 1: u1 = u_cur.copy()
        if i == r2i - 1: u2 = u_cur.copy()
    r1, r2 = r1i * h, r2i * h
    x1, x2 = k * r1, k * r2
    # Riccati-Bessel via upward recursion (stable enough for l << x here; cap lmax ~ k*rmax/2)
    def rb(l_arr, x):
        j = np.zeros(len(l_arr)); nn = np.zeros(len(l_arr))
        j0, j1 = math.sin(x) / x, math.sin(x) / x ** 2 - math.cos(x) / x
        n0, n1 = -math.cos(x) / x, -math.cos(x) / x ** 2 - math.sin(x) / x
        jj = [j0, j1]; nnn = [n0, n1]
        for l in range(1, int(l_arr[-1]) + 1):
            jj.append((2 * l + 1) / x * jj[l] - jj[l - 1])
            nnn.append((2 * l + 1) / x * nnn[l] - nnn[l - 1])
        return np.array(jj[:len(l_arr)]), np.array(nnn[:len(l_arr)])
    j1a, n1a = rb(ls, x1); j2a, n2a = rb(ls, x2)
    G = np.where(u2 != 0, (u1 * r2) / (np.where(u2 == 0, 1, u2) * r1), 1e30)
    num = G * j2a - j1a
    den = G * n2a - n1a
    d = np.arctan2(num, den)
    # kill unconverged high-l (upward recursion of j unstable for l >> x): zero where l > x2+8
    d = np.where(ls > x2 + 8, 0.0, d)
    return d.tolist()


def dsig_dcos(delts, k, cth):
    """|f(theta)|^2 in fm^2/sr from phase shifts."""
    # Legendre recursion
    fre = fim = 0.0
    Pm, P = 1.0, cth
    for l, d in enumerate(delts):
        Pl = 1.0 if l == 0 else (cth if l == 1 else P)
        if l >= 2:
            Pl = ((2 * l - 1) * cth * P - (l - 1) * Pm) / l
            Pm, P = P, Pl
        elif l == 1:
            Pm, P = 1.0, cth
        amp = (2 * l + 1) * math.sin(d)
        fre += amp * math.cos(d) * Pl
        fim += amp * math.sin(d) * Pl
    return (fre * fre + fim * fim) / (k * k)


def helm2(q, A):
    R = math.sqrt(max((1.23 * A ** (1 / 3) - 0.6) ** 2 + 0.631 * math.pi ** 2 - 5 * 0.81, 0.1))
    s = 0.9
    x = q * R / HBARC
    if x < 1e-4: return 1.0
    j1 = (math.sin(x) - x * math.cos(x)) / (x * x)
    return (3 * j1 / x) ** 2 * math.exp(-(q * s / HBARC) ** 2)


def speed_pdf():
    """Flux-weighted speed distribution relative to detector (truncated shifted Maxwellian)."""
    vs, ws = [], []
    nv = 12
    vmax = VESC + VDET
    for i in range(nv):
        v = (i + 0.5) * vmax / nv
        p = (v / (VDET * V0 * math.sqrt(math.pi))) * (
            math.exp(-((v - VDET) / V0) ** 2) - math.exp(-(min(v + VDET, 2 * vmax) / V0) ** 2))
        if v > vmax: p = 0.0
        ws.append(max(p, 0.0) * v)   # flux weight ~ v * f(v)
        vs.append(v)
    tot = sum(ws)
    return [(vs[i], ws[i] / tot) for i in range(nv) if ws[i] > 0]


def predicted_bins(sign, folded, verbose=False):
    """Predicted counts in each Table-I bin + >4keV, single-scatter layer model."""
    counts = [0.0] * len(BINS)
    sat = 0.0
    SP = speed_pdf()
    # aggregate area*column per target (dsigma identical across same-target layers)
    agg = {}
    for tname, area, col in LAYERS:
        agg[tname] = agg.get(tname, 0.0) + area * col
    for tname, acol in agg.items():
        A, mT = TARGETS[tname]
        mu = mT * M_ROD / (mT + M_ROD)
        V = make_V(A, sign, folded)
        for v_kms, wv in SP:
            v = v_kms / CKMS
            k = mu * v / HBARC
            lmax = min(max(int(k * 180 * 0.6), 10), 70)
            delts = phase_shifts(V, mu, k, lmax)
            Emax = 2 * mu * mu * v * v / mT * 1e6   # eV
            nc = 120
            for j in range(nc):
                c = -1 + 2 * (j + 0.5) / nc
                ER = 0.5 * Emax * (1 - c)           # eV
                q = math.sqrt(2 * mT * ER * 1e-6)   # MeV
                ds = dsig_dcos(delts, k, c) * helm2(q, A) * 2 * math.pi * (2.0 / nc)  # fm^2
                w = NDM * (acol / ENTR) * ds * 1e-26 * wv
                if ER >= SAT[0]:
                    sat += w
                else:
                    for b, (lo, hi, obs, f) in enumerate(BINS):
                        if lo <= ER < hi:
                            counts[b] += w * f
                            break
    return counts, sat


if __name__ == "__main__":
    print("=" * 78)
    print(" 1879 -- XQC recomputation: partial-wave solve for the rod-nucleus system")
    print(" N=18, E_rN=%.2e MeV, R_s=%.2f fm (m_s=7.76 MeV), L=%.1f fm" % (E_RN, RS, L_ROD))
    print("=" * 78)
    # (0) Born-limit validation: scale coupling down x1e-3, compare to Born sigma
    mu = TARGETS["Si"][1] * M_ROD / (TARGETS["Si"][1] + M_ROD)
    v = 300.0 / CKMS; k = mu * v / HBARC
    global E_RN_SAVE
    import sys
    mod = sys.modules[__name__]
    save = mod.E_RN; mod.E_RN = save * 1e-3
    d = phase_shifts(make_V(28.09, +1, False), mu, k, 20)
    sig_pw = sum(4 * math.pi / (k * k) * (2 * l + 1) * math.sin(dd) ** 2 for l, dd in enumerate(d))
    aB = (2 * mu / HBARC ** 2) * 28.09 * mod.E_RN * RC * RS ** 2
    # Born sigma for Yukawa at finite k (integrated):
    sigB = 4 * math.pi * aB * aB / (1 + 4 * (k * RS) ** 2)  # exact finite-k Born total for Yukawa
    print("\n(0) WEAK-COUPLING CHECK (x1e-3, Si, 300 km/s, kR_s = %.2f):" % (k * RS))
    print("    partial-wave sigma = %.4e fm^2 vs exact Born 4pi a^2/(1+4k^2R_s^2) = %.4e"
          "  ratio %.3f" % (sig_pw, sigB, sig_pw / sigB))
    mod.E_RN = save
    # (1) Full predictions, four model variants
    print("\n(1) PREDICTED XQC COUNTS vs OBSERVED (Table I bins + >4 keV):")
    for sign, sn in ((-1, "attractive"), (+1, "repulsive")):
        for folded, fn in ((True, "line-folded"), (False, "point")):
            counts, sat = predicted_bins(sign, folded)
            tot = sum(counts)
            nviol = 0
            for b, (lo, hi, obs, f) in enumerate(BINS):
                if counts[b] > obs + 5 * math.sqrt(obs + 1): nviol += 1
            satv = sat > SAT[1] + 5 * math.sqrt(SAT[1])
            print("\n  --- sign={:>10}, rod={:>11} ---".format(sn, fn))
            print("    {:>12} {:>9} {:>9}".format("bin (eV)", "pred", "obs"))
            for b, (lo, hi, obs, f) in enumerate(BINS):
                flag = "  <-- VIOLATION" if counts[b] > obs + 5 * math.sqrt(obs + 1) else ""
                print("    {:>5}-{:<6} {:>9.1f} {:>9}{}".format(lo, hi, counts[b], obs, flag))
            print("    {:>12} {:>9.1f} {:>9}{}".format(">4000", sat, SAT[1],
                  "  <-- VIOLATION" if satv else ""))
            print("    TOTAL in-band pred = {:.0f} vs obs = 527 ; violated bins = {}{}".format(
                tot, nviol, " + sat" if satv else ""))
            print("    VERDICT: {}".format(
                "EXCLUDED-class (XQC)" if (nviol > 0 or satv) else "XQC-SAFE at this variant"))
    print("\n" + "=" * 78)
