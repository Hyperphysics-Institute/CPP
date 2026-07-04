"""
1868 -- D4 executed by J7 audit (founder-delegated best judgment, TLA 4 July 2026):
the hard-capsule floor idealization is replaced by the DERIVED coat-radius floor.

THE IDEA (no new physics, no new parameters):
  A rod has no material wall. Its elastic "geometric" cross-section is set by the
  effective interaction radius of the REGISTERED screened eCP-coat potential:
      V_coat(b) = E_ee * (r_c / b) * exp(-b / r_scr),   E_ee = 0.9 MeV [1813],
      r_c = 1 fm, r_scr = 1.0 fm [SF-5 anchor; 0.85 spread carried, J2]
  Two rods deflect strongly out to b_eff(v) where V_coat(b_eff) = KE(v); beyond, they
  slip past. The hard-capsule MC (1856) implicitly FROZE b_eff at its low-velocity
  value; the physical floor inherits b_eff(v):
      floor(v) = eps * 0.11 * N * [ b_eff(v) / b_eff(v_ref) ]^k
  v_ref = 50 km/s (the dwarf-coring context in which the 1860 convention was anchored);
  k = 2 (compact assembly, sigma ~ b^2) and k = 1 (long-rod, sigma ~ L*b) BOTH carried;
  encounter mass mu = m_el/2 (segment) and N*m_el/2 (whole rod) BOTH carried.

SELF-CONSISTENCY TEST (the make-or-break for this reading):
  The 1856 MC at capsule radius r gives sigma_T(A=4, N~16) = 23.72 r^2. Equating to the
  convention value eps*0.11*N cm^2/g at N=16 implies an effective capsule radius
  r_impl = sqrt(sigma_T,conv / 23.72). If r_impl matches b_eff(50 km/s) computed from
  the coat potential, then the convention's own normalization IS the low-velocity coat
  radius -- and the floor's velocity dependence follows with zero freedom.

Then: full anchor confrontation (1867 table) with floor(v) in place of the hard floor.
"""
import math

C = 299792.458; MeV_g = 1.783e-27; RC = 1.0; M_EL = 1408.0
CHI = ((1 + 5 ** 0.5) / 2) ** -3 / 6
RS = 1.0 / CHI
EPS = 0.30
E_EE = 0.9


def KE(v, mu_MeV):
    return 0.5 * mu_MeV * (v / C) ** 2


def b_eff(v, mu_MeV, r_scr=1.0):
    """Solve E_ee*(rc/b)e^{-b/r_scr} = KE(v); floor at rc if KE exceeds contact value."""
    ke = KE(v, mu_MeV)
    V = lambda b: E_EE * (RC / b) * math.exp(-b / r_scr)
    if V(RC) <= ke: return RC
    lo, hi = RC, 200.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if V(mid) > ke: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)


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


def floor_v(v, N, k, mu_mode, r_scr=1.0, v_ref=50.0):
    mu = M_EL / 2 if mu_mode == "seg" else N * M_EL / 2
    return EPS * 0.11 * N * (b_eff(v, mu, r_scr) / b_eff(v_ref, mu, r_scr)) ** k


ANCHORS = [
    ("dSph-lo", 10, 20.0, 100.0), ("dSph-hi", 40, 20.0, 100.0),
    ("dwarf-pin", 50, 1.0, 5.0), ("LSB", 200, 0.7, 2.5),
    ("group", 1150, 0.3, 0.7), ("cluster", 1500, 0.0, 0.35), ("Bullet", 3500, 0.0, 0.7),
]

if __name__ == "__main__":
    print("=" * 78)
    print(" 1868 -- derived coat-radius floor(v): J7 audit, zero new parameters")
    print("=" * 78)

    # (1) SELF-CONSISTENCY: convention normalization vs coat radius at low v -----------
    print("\n(1) SELF-CONSISTENCY: does the convention's normalization equal the")
    print("    low-velocity coat radius?")
    N16 = 16
    sigmaT_conv = EPS * 0.11 * N16 * (N16 * M_EL * MeV_g)          # cm^2
    r_impl = math.sqrt(sigmaT_conv / (23.72 * 1e-26))              # fm (MC: 23.72 r^2 at A=4)
    print("    convention sigma_T(N=16) = {:.3e} cm^2 ; 1856 MC = 23.72 r^2".format(sigmaT_conv))
    print("    => implied capsule radius r_impl = {:.2f} fm".format(r_impl))
    for mu_mode, mu in (("segment", M_EL / 2), ("whole-rod(N=16)", N16 * M_EL / 2)):
        for r_scr in (1.0, 0.85):
            print("    b_eff(50 km/s | mu={:>15}, r_scr={:.2f}) = {:6.2f} fm   (r_impl/b_eff = {:.2f})".format(
                mu_mode, r_scr, b_eff(50, mu, r_scr), r_impl / b_eff(50, mu, r_scr)))

    # (2) b_eff(v) table ---------------------------------------------------------------
    print("\n(2) b_eff(v) [fm], r_scr = 1.0:")
    print("    {:>6} {:>12} {:>12}".format("v", "mu=segment", "mu=rod(N=18)"))
    for v in (10, 50, 200, 1150, 1500, 3500):
        print("    {:>6} {:>12.2f} {:>12.2f}".format(v, b_eff(v, M_EL / 2), b_eff(v, 18 * M_EL / 2)))

    # (3) Full anchor confrontation, all four variants, N = 18 -------------------------
    print("\n(3) FULL CURVE at chi (N = 18, E_c flat): total = floor(v) + capture")
    variants = [("seg", 2), ("seg", 1), ("rod", 2), ("rod", 1)]
    print("    {:>9} {:>5}".format("anchor", "v") +
          "".join("  {:>5}k={}".format(m, k) for m, k in variants) + "   window     hard-1867")
    for name, v, lo, hi in ANCHORS:
        cap = capture(v, 0.30, 18)
        row = "    {:>9} {:>5}".format(name, v)
        for m, k in variants:
            row += "  {:>8.3f}".format(floor_v(v, 18, k, m) + cap)
        hard = EPS * 0.11 * 18 + cap
        row += "   [{:.2f},{:.2f}]  {:>7.2f}".format(lo, hi, hard)
        print(row)

    # (4) Verdict grid: bounds + group, per variant, N = 15/18/20 ----------------------
    print("\n(4) VERDICTS (cluster ladder + group point), capture included:")
    print("    variant      N   cluster(1500)  <0.35  <0.19  <0.13 | group(1150) vs 0.5+/-0.2")
    for m, k in variants:
        for N in (15, 18, 20):
            cl = floor_v(1500, N, k, m) + capture(1500, 0.30, N)
            gr = floor_v(1150, N, k, m) + capture(1150, 0.30, N)
            devs = (0.5 - gr) / 0.2
            print("    mu={:>3} k={}  {:>2}   {:>10.3f}     {:>4} {:>5} {:>5} |  {:>6.3f}  ({:+.1f} sigma low)".format(
                m, k, N, cl,
                "ok" if cl < 0.35 else "VIOL", "ok" if cl < 0.19 else "VIOL",
                "ok" if cl < 0.13 else "VIOL", gr, devs))

    # (5) The falsifier this reading buys ----------------------------------------------
    print("\n(5) DISCRIMINATOR: the derived floor predicts NO cliff between 1150 and 1500;")
    print("    instead group-scale sigma/m ~ 0.04-0.25 (variant-dependent). If future")
    print("    group-scale analyses CONFIRM 0.5 at high significance, this reading dies;")
    print("    if the group value relaxes to <~0.25, it stands. Clean, near-term data test.")

    # (6) STRESS TEST: MC-informed geometric assembly (the k_eff question) -------------
    print("\n(6) STRESS TEST -- MC-informed assembly: rerun the suppression with r = b_eff(v)")
    print("    fed through the 1856 MC's own f(A) = sigma_T/r^2 table (A = L/2r), with L")
    print("    fixed structurally (L from A_ref = N/4 at r_ref = r_impl; element spacing")
    print("    thus ~4.7 fm at N=18 -- UNPINNED in-session, flagged J8).")
    MC_A = [1.0, 2.0, 4.0, 8.0, 16.0, 32.0]
    MC_F = [5.37, 10.30, 23.72, 74.01, 203.51, 729.70]

    def f_of_A(A):
        lA = math.log(A)
        xs = [math.log(a) for a in MC_A]; ys = [math.log(f) for f in MC_F]
        if lA <= xs[0]: i = 0
        elif lA >= xs[-1]: i = len(xs) - 2
        else:
            i = max(j for j in range(len(xs) - 1) if xs[j] <= lA)
        t = (lA - xs[i]) / (xs[i + 1] - xs[i])
        return math.exp(ys[i] + t * (ys[i + 1] - ys[i]))

    N = 18
    r_ref = 9.46
    L = 2 * r_ref * (N / 4.0)          # A_ref = N/4 at the reference radius
    mu = M_EL / 2
    b_ref = b_eff(50.0, mu)
    s_ref = b_ref ** 2 * f_of_A(L / (2 * b_ref))
    print("    {:>6} {:>8} {:>7} {:>9} {:>7}".format("v", "b_eff", "A", "SUPP_MC", "k_eff"))
    for v in (200, 1150, 1500, 3500):
        b = b_eff(v, mu)
        supp = (b ** 2 * f_of_A(L / (2 * b))) / s_ref
        keff = math.log(supp) / math.log(b / b_ref)
        print("    {:>6} {:>8.2f} {:>7.1f} {:>9.3f} {:>7.2f}".format(v, b, L / (2 * b), supp, keff))
    cl_mc = EPS * 0.11 * N * ((b_eff(1500, mu) ** 2 * f_of_A(L / (2 * b_eff(1500, mu)))) / s_ref) \
        + capture(1500, 0.30, N)
    gr_mc = EPS * 0.11 * N * ((b_eff(1150, mu) ** 2 * f_of_A(L / (2 * b_eff(1150, mu)))) / s_ref) \
        + capture(1150, 0.30, N)
    print("    => MC-assembled cluster(1500) = {:.3f}  [<0.35 {} | <0.13 {}]   group = {:.3f}".format(
        cl_mc, "ok" if cl_mc < 0.35 else "VIOL", "ok" if cl_mc < 0.13 else "VIOL", gr_mc))
    print("    HONEST SPREAD: the suppression exponent k_eff spans ~0.4 (MC-assembled,")
    print("    hard contacts within b_eff) to 2 (compact soft assembly). The cluster")
    print("    verdict swings across the ladder over that span. The hard-contact-inside-")
    print("    b_eff reading double-counts hardness at high v (contacts inside b_eff also")
    print("    soften as KE grows); the truth sits between. DECIDABLE by a soft-potential")
    print("    rerun of the 1856 MC (screened coat force law replacing hard contacts).")

    print("\n" + "=" * 78)
    print(" READ-OUT: see reasoning/1868.md for the D4 resolution and honest accounting.")
    print("=" * 78)
