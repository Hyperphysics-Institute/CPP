"""
1866 -- OPEN-SS-43 queued action 1 (reordered queue, Patch 1865): refine the CONFRONT-1
heavy-nucleus binding shift dB with a proper nuclear density integral, and test how much
of dB the semi-empirical mass formula (SEMF) can absorb into its fitted coefficients.
This number now GATES the chi-revival claim (1865): the crude 1864 estimate
(pairs x <V> at 4 fm) held the chi point by only a factor ~1.3-2 against the ~1 MeV
mass-fit sensitivity.

MODEL (unchanged from 1864/1865, CONV-003 provenance):
  Residual NN potential  V(r) = (E_NN * r_c / r) * exp(-r/lambda),  r_c = 1 fm,
  E_NN = 9 * E_c / (8N)^2   [pairwise-additive qCP coupling: rod core 8N qCPs, nucleon 3],
  lambda = calibrated R_s (N-flat screening), E_c = 0.3 MeV (flat) or 0.02*N (additive).

REFINEMENT 1 -- density integral:
  dB = (1/2) Int Int n(r1) n(r2) V(|r1-r2|) d3r1 d3r2
  computed with the exact shell-shell angular average of the Yukawa kernel:
      <V>(r1,r2) = g * lambda/(2 r1 r2) * [exp(-|r1-r2|/lambda) - exp(-(r1+r2)/lambda)]
  (limit lambda->inf reproduces 1/max(r1,r2), the Coulomb check).
  Densities: (a) uniform sphere, R = 1.2 A^(1/3) fm, n0 = 3A/(4 pi R^3);
             (b) Woods-Saxon, R_ws = 1.1 A^(1/3) fm, a = 0.55 fm, n0 normalized to A.

REFINEMENT 2 -- SEMF absorption:
  A smooth dB(A) along the valley of stability is partially degenerate with the SEMF
  basis; the DETECTABLE quantity is the residual after refitting, not raw dB.
  Fit dB(A) over A in [50, 250] (valley Z(A) = A / (1.98 + 0.0155 A^(2/3))) to the basis
  {A, A^(2/3), Z(Z-1)/A^(1/3), (A-2Z)^2/A, 1} by least squares (stdlib normal equations);
  report the RMS and max residual as the detectable part.

SANITY ANCHORS: lambda -> inf Coulomb check against the analytic uniform-sphere
self-energy <1/r> = 6/(5R); crude-1864 estimate reproduced for comparison.
"""
import math

RC = 1.0
HBARC = 197.327
MU_NN = 938.9 / 2.0
PREF = 2 * MU_NN / HBARC ** 2          # Born prefactor, MeV^-1 fm^-2
CHI = ((1 + 5 ** 0.5) / 2) ** -3 / 6   # 0.03934
RS_CHI = 1.0 / CHI                     # 25.42 fm


def e_nn(N, Ec):
    return 9.0 * Ec / (8 * N) ** 2


def kernel(r1, r2, lam):
    """Shell-shell angular average of exp(-s/lam)/s (g factored out)."""
    return (lam / (2.0 * r1 * r2)) * (
        math.exp(-abs(r1 - r2) / lam) - math.exp(-(r1 + r2) / lam))


def simpson_weights(n):
    """n odd number of points."""
    w = [1.0] * n
    for i in range(1, n - 1):
        w[i] = 4.0 if i % 2 == 1 else 2.0
    return w


def dB_density(A, g, lam, profile="uniform", npts=201):
    """dB = 1/2 * IntInt 4pi r1^2 n1 * 4pi r2^2 n2 * g*kernel dr1 dr2  (MeV)."""
    if profile == "uniform":
        R = 1.2 * A ** (1.0 / 3.0)
        rmax = R
        n = lambda r: 3.0 * A / (4.0 * math.pi * R ** 3) if r <= R else 0.0
    else:  # woods-saxon
        Rws = 1.1 * A ** (1.0 / 3.0)
        a = 0.55
        rmax = Rws + 10.0 * a
        raw = lambda r: 1.0 / (1.0 + math.exp((r - Rws) / a))
        # normalize numerically
        h = rmax / (npts - 1)
        w = simpson_weights(npts)
        norm = sum(w[i] * 4 * math.pi * (i * h) ** 2 * raw(i * h)
                   for i in range(npts)) * h / 3.0
        n0 = A / norm
        n = lambda r: n0 * raw(r)
    h = rmax / (npts - 1)
    w = simpson_weights(npts)
    rs = [max(i * h, 1e-9) for i in range(npts)]
    f = [4 * math.pi * r * r * n(r) for r in rs]     # radial shell weight
    total = 0.0
    for i in range(npts):
        if f[i] == 0.0:
            continue
        row = 0.0
        for j in range(npts):
            if f[j] == 0.0:
                continue
            row += w[j] * f[j] * kernel(rs[i], rs[j], lam)
        total += w[i] * f[i] * row
    total *= (h / 3.0) ** 2
    return 0.5 * g * total


def dB_crude(A, g, lam):
    pairs = A * (A - 1) / 2.0
    return pairs * (g / 4.0) * math.exp(-4.0 / lam)


def valley_Z(A):
    return A / (1.98 + 0.0155 * A ** (2.0 / 3.0))


def lstsq(X, y):
    """Solve normal equations (X^T X) b = X^T y, Gaussian elimination (stdlib)."""
    m = len(X[0])
    XtX = [[sum(X[k][i] * X[k][j] for k in range(len(X))) for j in range(m)]
           for i in range(m)]
    Xty = [sum(X[k][i] * y[k] for k in range(len(X))) for i in range(m)]
    M = [row[:] + [Xty[i]] for i, row in enumerate(XtX)]
    for c in range(m):
        p = max(range(c, m), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]
        for r in range(m):
            if r != c and M[c][c] != 0.0:
                fac = M[r][c] / M[c][c]
                for k in range(c, m + 1):
                    M[r][k] -= fac * M[c][k]
    return [M[i][m] / M[i][i] for i in range(m)]


if __name__ == "__main__":
    print("=" * 78)
    print(" 1866 -- dB density-integral refinement + SEMF absorption (CONFRONT-1)")
    print("=" * 78)

    # (0) Coulomb sanity check ------------------------------------------------------
    A = 200
    R = 1.2 * A ** (1.0 / 3.0)
    g = 1.0
    dB_num = dB_density(A, g, 1e6, "uniform")
    dB_ana = 0.5 * A * A * g * 6.0 / (5.0 * R)
    print("\n(0) SANITY (lambda -> inf, uniform sphere, A=200):")
    print("    numeric {:.4f} vs analytic (A^2/2)(6/5R) {:.4f}  ratio {:.5f}".format(
        dB_num, dB_ana, dB_num / dB_ana))

    # (1) Refined dB at the 1865 corners + chi point --------------------------------
    print("\n(1) REFINED dB(A=200), MeV: uniform / Woods-Saxon / crude-1864 (ratio ref/crude)")
    corners = []
    # 1865 calibrated corners (N, model, target, lambda) -- from 1865 output table
    cal = [(5, "flat", 1, 3.5), (5, "flat", 5, 9.1), (8, "flat", 1, 5.0),
           (8, "additive", 2, 8.8), (12, "flat", 2, 10.8), (12, "additive", 5, 20.5),
           (15, "flat", 2, 13.1), (15, "flat", 5, 23.7), (20, "flat", 5, 31.5),
           (20, "additive", 5, 28.6)]
    # chi point rows
    for N in (12, 15, 20):
        for lbl, Ec in (("flat", 0.30), ("additive", 0.02 * N)):
            cal.append((N, lbl + "*CHI", "chi", RS_CHI))
    print("    {:>3} {:>13} {:>6} {:>7} {:>9} {:>9} {:>9} {:>7}".format(
        "N", "model", "target", "lambda", "uniform", "WS", "crude", "ratio"))
    for N, lbl, tgt, lam in cal:
        Ec = 0.30 if lbl.startswith("flat") else 0.02 * N
        g = e_nn(N, Ec) * RC
        du = dB_density(200, g, lam, "uniform")
        dw = dB_density(200, g, lam, "ws")
        dc = dB_crude(200, g, lam)
        flag = "  <-- TENSION(raw)" if du > 1.0 else ""
        print("    {:>3} {:>13} {:>6} {:>6.1f}f {:>9.3f} {:>9.3f} {:>9.3f} {:>7.2f}{}".format(
            N, lbl, str(tgt), lam, du, dw, dc, du / dc if dc else float("nan"), flag))
        corners.append((N, lbl, tgt, lam, Ec, du))

    # (2) SEMF absorption -------------------------------------------------------------
    print("\n(2) SEMF ABSORPTION: fit dB(A) along the valley (A=50..250) to SEMF basis;")
    print("    residual = detectable part.  Shown for representative lambda values.")
    for lam_show, tag in ((8.5, "band low edge"), (RS_CHI, "chi point"), (31.5, "band high edge")):
        g = 1.0  # scale-free; residual fraction independent of g
        As = list(range(50, 251, 5))
        y = [dB_density(a, g, lam_show, "uniform", npts=121) for a in As]
        X = []
        for a in As:
            Z = valley_Z(a)
            X.append([a, a ** (2.0 / 3.0), Z * (Z - 1) / a ** (1.0 / 3.0),
                      (a - 2 * Z) ** 2 / a, 1.0])
        b = lstsq(X, y)
        res = [y[k] - sum(X[k][i] * b[i] for i in range(5)) for k in range(len(As))]
        rms = math.sqrt(sum(r * r for r in res) / len(res))
        mx = max(abs(r) for r in res)
        yA200 = y[As.index(200)]
        print("    lambda = {:>5.1f} fm ({:>13}):  raw dB(200)/g = {:9.1f}   "
              "residual: RMS {:6.2%} of raw, max {:6.2%}".format(
                  lam_show, tag, yA200, rms / yA200, mx / yA200))

    # (2b) Coefficient shifts: is the absorption PHYSICALLY allowed? -----------------
    print("\n(2b) COEFFICIENT SHIFTS under absorption (chi point, N=15, physical g):")
    print("     the smooth dB is absorbed by shifting fitted SEMF coefficients; the")
    print("     shifts must hide inside each coefficient's independent determination.")
    g_phys = e_nn(15, 0.30) * RC
    As = list(range(50, 251, 5))
    y = [dB_density(a, g_phys, RS_CHI, "uniform", npts=121) for a in As]
    X = [[a, a ** (2.0 / 3.0), valley_Z(a) * (valley_Z(a) - 1) / a ** (1.0 / 3.0),
          (a - 2 * valley_Z(a)) ** 2 / a, 1.0] for a in As]
    b = lstsq(X, y)
    res = [y[k] - sum(X[k][i] * b[i] for i in range(5)) for k in range(len(As))]
    rms = math.sqrt(sum(r * r for r in res) / len(res))
    frac = max(abs(r) for r in res) / y[As.index(200)]
    names = ("d a_V (vol)", "d a_S (surf)", "d a_C (Coul)", "d a_A (asym)", "d const")
    refs = ("a_V ~ 15.75 MeV, known ~1%", "a_S ~ 17.8 MeV, known ~few %",
            "a_C ~ 0.711 MeV, mirror-nuclei-pinned ~1% => tol ~0.007",
            "a_A ~ 23.7 MeV, known ~few %", "--")
    for i in range(5):
        print("     {:>13} = {:+.4e} MeV   [{}]".format(names[i], b[i], refs[i]))
    print("     residual after fit: RMS {:.2e} MeV, max/raw(200) = {:.2e}".format(rms, frac))
    print("     CAVEAT: basis strongly collinear over A=[50,250]; individual shifts are")
    print("     fit-unstable even though the residual is robustly ~0. Read the shift")
    print("     MAGNITUDES as scale indicators only.")

    # (3) Verdicts: per-channel ------------------------------------------------------
    print("\n(3) PER-CHANNEL VERDICTS at the chi point (R_s = 25.4 fm):")
    print("    channel A: heavy-nucleus dB -- raw-refined (no absorption credit) vs ~1 MeV")
    print("    channel B: np scattering length d a_np vs ~3e-3 fm  [UNABSORBABLE]")
    print("    {:>3} {:>9} {:>12} {:>14} {:>12} {:>14}".format(
        "N", "model", "raw dB(MeV)", "chA verdict", "da_np(fm)", "chB verdict"))
    for N in (12, 15, 20):
        for lbl, Ec in (("flat", 0.30), ("additive", 0.02 * N)):
            g = e_nn(N, Ec) * RC
            du = dB_density(200, g, RS_CHI, "uniform")
            da = PREF * e_nn(N, Ec) * RC * RS_CHI ** 2
            va = "TENSION" if du > 1.0 else ("edge" if du > 0.8 else "safe")
            vb = "TENSION" if da > 3e-3 else ("edge" if da > 2.5e-3 else "safe")
            print("    {:>3} {:>9} {:>12.3f} {:>14} {:>12.2e} {:>14}".format(
                N, lbl, du, va, da, vb))
    print("    sensitivity anchors [J5]: dB ~1 MeV; |d a_np| ~3e-3 fm")
    print("    (a_t = 5.4194(20) fm, a_s = -23.7148(43) fm -> ~2-4e-3 fm is the right scale)")

    print("\n" + "=" * 78)
    print(" READ-OUT: see reasoning/1866.md for verdicts and the updated ledger.")
    print("=" * 78)
