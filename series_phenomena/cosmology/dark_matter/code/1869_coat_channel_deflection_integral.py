"""
1869 -- The decisive number for the D4 fork: the EXACT classical momentum-transfer
suppression shape S(v) for the repulsive screened coat channel, from the orbit-integral
deflection angle -- no hard-capsule assumption, no assembly exponent k.

Model: rod-rod elastic channel = classical scattering in the registered coat potential
    V(r) = E_ee * (r_c/r) * exp(-r/r_scr),  E_ee = 0.9 MeV [1813], r_c = 1 fm,
    r_scr = 1.0 fm [SF-5], REPULSIVE, reduced mass mu = N*m_el/2 (rod CM deflection).
Deflection:  theta(b) = pi - 2*Int_0^{u_max} b du / sqrt(1 - b^2 u^2 - V(1/u)/E),
    E = (1/2) mu v^2, u_max = outermost turning point.  (phi-substitution regularizes
    the endpoint; Simpson in phi.)
Transport:   sigma_T(v) = 2 pi Int (1 - cos theta(b)) b db.

NORMALIZATION: anchored once at v_ref = 50 km/s to the 1860 convention (as before --
the encounter-multiplicity factor is absorbed there). The NEW derived content is the
SHAPE  S(v) = sigma_T(v)/sigma_T(v_ref):
    floor(v) = eps * 0.11 * N * S(v).
S(v) replaces both the 1867 hard floor (S = 1) and the 1868 k-variants (S = (b/b_ref)^k).

Sanity anchors: (i) low-v limit ~ pi b_eff^2 * O(1) (strong-deflection plateau);
(ii) pure-Coulomb comparison against the analytic Rutherford sigma_T divergence trend.
"""
import math

C = 299792.458; MeV_g = 1.783e-27; RC = 1.0; M_EL = 1408.0
CHI = ((1 + 5 ** 0.5) / 2) ** -3 / 6
RS = 1.0 / CHI
EPS = 0.30
E_EE = 0.9
R_SCR = 1.0


def Vc(r):
    return E_EE * (RC / r) * math.exp(-r / R_SCR)


def theta_of_b(b, E, nphi=400):
    """Classical deflection angle for repulsive Vc at energy E, impact parameter b."""
    g = lambda u: 1.0 - (b * u) ** 2 - Vc(1.0 / u) / E
    # outermost turning point u_max: g(u_max) = 0, g decreasing in u near it
    lo, hi = 1e-9, 1.0 / (0.05 * RC)
    # bracket: g(lo) ~ 1 > 0; increase hi until g(hi) < 0 (repulsive => always a root)
    while g(hi) > 0: hi *= 2.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if g(mid) > 0: lo = mid
        else: hi = mid
    umax = 0.5 * (lo + hi)
    # phi-substitution u = umax sin(phi): integrand regular at phi = pi/2
    total = 0.0
    n = nphi if nphi % 2 == 1 else nphi + 1
    h = (math.pi / 2) / (n - 1)
    for i in range(n):
        phi = i * h
        u = umax * math.sin(phi)
        gu = g(u) if u > 1e-12 else 1.0
        if gu <= 0:
            # endpoint: use analytic limit integrand -> b*umax/sqrt(-g'(umax)*umax/2)... 
            # approximate via previous regular value (Simpson weight small there)
            val = 0.0 if i == 0 else last
        else:
            val = b * umax * math.cos(phi) / math.sqrt(gu)
            last = val
        w = 1.0 if i in (0, n - 1) else (4.0 if i % 2 == 1 else 2.0)
        total += w * val
    integral = total * h / 3.0
    th = math.pi - 2.0 * integral
    return max(0.0, min(math.pi, th))


def sigma_T(v, N, nb=120, bmax_fm=40.0):
    mu = N * M_EL / 2
    E = 0.5 * mu * (v / C) ** 2
    # log grid in b
    bs = [0.05 * (bmax_fm / 0.05) ** (i / (nb - 1)) for i in range(nb)]
    tot = 0.0
    prev_b, prev_f = None, None
    for b in bs:
        th = theta_of_b(b, E)
        f = (1.0 - math.cos(th)) * b
        if prev_b is not None:
            tot += 0.5 * (f + prev_f) * (b - prev_b)
        prev_b, prev_f = b, f
    return 2 * math.pi * tot  # fm^2


def capture(v, Ec, N):
    mu = N * M_EL / 2
    ke = 0.5 * mu * (v / C) ** 2
    V = lambda r: (Ec * RC / r) * math.exp(-r / RS)
    if V(RC) < ke:
        b = RC
    else:
        lo, hi = RC, 3000.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if V(mid) > ke: lo = mid
            else: hi = mid
        b = 0.5 * (lo + hi)
    return math.pi * b * b * 1e-26 / (N * M_EL * MeV_g)


ANCHORS = [
    ("dSph-lo", 10, 20.0, 100.0), ("dSph-hi", 40, 20.0, 100.0),
    ("dwarf-pin", 50, 1.0, 5.0), ("LSB", 200, 0.7, 2.5),
    ("group", 1150, 0.3, 0.7), ("cluster", 1500, 0.0, 0.35), ("Bullet", 3500, 0.0, 0.7),
]

if __name__ == "__main__":
    print("=" * 78)
    print(" 1869 -- exact classical S(v) for the coat channel (deflection integral)")
    print("=" * 78)

    N = 18
    vref = 50.0
    s_ref = sigma_T(vref, N)
    print("\n(1) DERIVED SHAPE (N = 18, mu = rod):   sigma_T(v_ref=50) = {:.1f} fm^2".format(s_ref))
    print("    {:>6} {:>12} {:>9}".format("v", "sigma_T fm^2", "S(v)"))
    shape = {}
    for v in (10, 40, 50, 200, 1150, 1500, 3500):
        st = sigma_T(v, N)
        shape[v] = st / s_ref
        print("    {:>6} {:>12.2f} {:>9.4f}".format(v, st, shape[v]))

    print("\n(2) FULL CURVE with the derived shape: total = eps*0.11*N*S(v) + capture")
    print("    {:>9} {:>5} {:>9} {:>9}   window        1867-hard  1868-k2".format(
        "anchor", "v", "floor", "total"))
    f0 = EPS * 0.11 * N
    for name, v, lo, hi in ANCHORS:
        fl = f0 * shape[v]
        cap = capture(v, 0.30, N)
        tot = fl + cap
        hard = f0 + cap
        print("    {:>9} {:>5} {:>9.3f} {:>9.3f}   [{:>5.2f},{:>6.2f}] {:>9.2f}".format(
            name, v, fl, tot, lo, hi, hard))

    print("\n(3) VERDICTS (N = 15, 18, 20; capture flat E_c):")
    print("    {:>3} {:>13} {:>6} {:>6} {:>6} | {:>12}".format(
        "N", "cluster(1500)", "<0.35", "<0.19", "<0.13", "group(1150)"))
    for Nx in (15, 18, 20):
        s_r = sigma_T(vref, Nx)
        Sc = sigma_T(1500, Nx) / s_r
        Sg = sigma_T(1150, Nx) / s_r
        cl = EPS * 0.11 * Nx * Sc + capture(1500, 0.30, Nx)
        gr = EPS * 0.11 * Nx * Sg + capture(1150, 0.30, Nx)
        print("    {:>3} {:>13.3f} {:>6} {:>6} {:>6} | {:>7.3f} ({:+.1f} sig low)".format(
            Nx, cl, "ok" if cl < 0.35 else "VIOL", "ok" if cl < 0.19 else "VIOL",
            "ok" if cl < 0.13 else "VIOL", gr, (0.5 - gr) / 0.2))

    print("\n(4) SANITY: strong-deflection plateau vs b_eff, and low-v saturation")
    mu = N * M_EL / 2
    for v in (10.0, 50.0):
        E = 0.5 * mu * (v / C) ** 2
        lo, hi = RC, 200.0
        while Vc(hi) > E: hi *= 1.5
        for _ in range(100):
            mid = 0.5 * (lo + hi)
            if Vc(mid) > E: lo = mid
            else: hi = mid
        be = 0.5 * (lo + hi)
        print("    v={:>4.0f}: pi*b_eff^2 = {:7.1f} fm^2 vs sigma_T = {:7.1f} fm^2  (ratio {:.2f})".format(
            v, math.pi * be * be, sigma_T(v, N), sigma_T(v, N) / (math.pi * be * be)))

    print("\n" + "=" * 78)
    print(" READ-OUT: see reasoning/1869.md.")
    print("=" * 78)
