"""
1867 -- OPEN-SS-43 queue item 2 (post-1866): the sigma(v) SHAPE test at eta = chi,
N = 15-20. First assembly of the FULL curve -- elastic floor + capture -- against the
complete empirical anchor set. Prior cluster-safety claims (1858/1860/1865) quoted the
CAPTURE term only; the 1857 decomposition sigma(v) = s_floor + capture says the
velocity-independent elastic rod-bounce floor is also present. This script puts the two
together at the calibrated chi point for the first time.

MODEL (CONV-003 provenance):
  capture(v) = pi b_max^2 / m_rod, V(r) = (E_c r_c/r) e^{-r/R_s}, R_s = 1/chi = 25.42 fm
      [1858 pipeline; E_c = 0.3 MeV flat / 0.02*N additive, 1858-era anchors]
  floor      = eps * 0.11 * N cm^2/g, eps = 0.30, velocity-independent hard-capsule
      reading [1856 MC (sphere-validated eps -> 1.03); 1860 convention decision]
  total(v)   = floor + capture(v)   [1857 decomposition]

EMPIRICAL ANCHORS (1865 pin + corpus 1857 anchors + this session's bound set):
  dSph      v = 10-40   : fits 20-100 (Correa 2021), 20-40 (Roberts et al. 2024)
  dwarf pin v = 50      : [1, 5] central, [0.5, 10] extended (J3', Patch 1865)
  LSB       v = 200     : [0.7, 2.5] (corpus 1857 anchor)
  group     v = 1150    : 0.5 +/- 0.2 (Sagunski 2021) -> window [0.3, 0.7]
  cluster   v = 1500    : 0.19 +/- 0.09, < 0.35 95% (Sagunski); < 0.19 (Eckert X-COP);
                          < 0.13 (Andrade 2022, tightest)
  Bullet    v = 3500    : < 0.7 (corpus window)

DIAGNOSTICS (no mechanism invented -- founder-gated):
  (a) p(v) = d ln sigma_total / d ln v profile;
  (b) the floor value that would thread group AND cluster simultaneously (spoiler: none
      -- the data themselves demand sigma falling between 1150 and 1500 km/s);
  (c) required floor suppression at 1500 km/s per N, and the collision KE at 1150/1500
      km/s vs E_ee = 0.9 MeV -- the barrier scale any transmission-onset mechanism
      would need to hit.
"""
import math

C = 299792.458; MeV_g = 1.783e-27; RC = 1.0; M_EL = 1408.0
CHI = ((1 + 5 ** 0.5) / 2) ** -3 / 6
RS = 1.0 / CHI
EPS = 0.30
E_EE = 0.9  # MeV, pinned side-bond scale (1813)


def bmax(v, Ec, N):
    mu = N * M_EL / 2
    KE = 0.5 * mu * (v / C) ** 2
    V = lambda r: (Ec * RC / r) * math.exp(-r / RS)
    if V(RC) < KE: return RC
    lo, hi = RC, 3000.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if V(mid) > KE: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)


def capture(v, Ec, N):
    b = bmax(v, Ec, N)
    return math.pi * b * b * 1e-26 / (N * M_EL * MeV_g)


def floor(N):
    return EPS * 0.11 * N


def total(v, Ec, N):
    return floor(N) + capture(v, Ec, N)


def p_slope(v, Ec, N, h=1.02):
    s1, s2 = total(v / h, Ec, N), total(v * h, Ec, N)
    return (math.log(s2) - math.log(s1)) / (math.log(v * h) - math.log(v / h))


ANCHORS = [
    ("dSph-lo", 10, 20.0, 100.0), ("dSph-mid", 20, 20.0, 100.0),
    ("dSph-hi", 40, 20.0, 100.0), ("dwarf-pin", 50, 1.0, 5.0),
    ("LSB", 200, 0.7, 2.5), ("group", 1150, 0.3, 0.7),
    ("cluster", 1500, 0.0, 0.35), ("Bullet", 3500, 0.0, 0.7),
]
CLUSTER_BOUNDS = (("Sagunski<0.35", 0.35), ("Eckert<0.19", 0.19), ("Andrade<0.13", 0.13))

if __name__ == "__main__":
    print("=" * 78)
    print(" 1867 -- FULL sigma(v) shape test at eta = chi (R_s = %.1f fm)" % RS)
    print("=" * 78)

    # (1) Full curve vs anchors ------------------------------------------------------
    print("\n(1) TOTAL sigma/m(v) = floor + capture at the chi point (floor in brackets)")
    for N in (15, 18, 20):
        for lbl, Ec in (("flat", 0.30), ("additive", 0.02 * N)):
            print("\n    N={:>2} {:>9}  [floor = {:.2f} cm^2/g]".format(N, lbl, floor(N)))
            for name, v, lo, hi in ANCHORS:
                s = total(v, Ec, N)
                cap = capture(v, Ec, N)
                verdict = "PASS" if lo <= s <= hi else ("HIGH" if s > hi else "LOW")
                print("      {:>9} v={:>4}: total={:8.2f} (cap {:7.3f})  window [{:>5.2f},{:>6.2f}]  {}".format(
                    name, v, s, cap, lo, hi, verdict))

    # (2) Cluster bound ladder at the floor -------------------------------------------
    print("\n(2) CLUSTER BOUND LADDER vs the velocity-independent floor:")
    for N in (15, 18, 20):
        f = floor(N)
        line = "    N={:>2}: floor = {:.2f}".format(N, f)
        for bname, b in CLUSTER_BOUNDS:
            line += "   {}: x{:.1f} {}".format(bname, f / b, "VIOL" if f > b else "ok")
        print(line)
    print("    (capture at 1500 km/s adds only 0.002-0.004 -- the floor dominates)")

    # (3) The group/cluster squeeze: NO flat floor threads both -----------------------
    print("\n(3) THE SQUEEZE: group (1150 km/s) wants >= 0.3; Andrade cluster (~1500) wants < 0.13.")
    print("    A velocity-INDEPENDENT floor cannot satisfy both: the DATA demand sigma")
    print("    falling by >~ 2.3x between 1150 and 1500 km/s. Any model threading both")
    print("    needs velocity dependence in exactly that window.")
    print("    Flat-floor compromise scan (satisfy cluster only): floor < 0.13")
    print("      => eps*0.11*N < 0.13 => N < {:.1f} at eps = 0.30".format(0.13 / (EPS * 0.11)))
    print("      -- collides head-on with the np-channel requirement N >~ 15 (Patch 1866).")

    # (4) What a suppression mechanism must deliver ------------------------------------
    print("\n(4) REQUIRED floor suppression at cluster velocities (diagnostic, mechanism")
    print("    founder-gated -- nothing is invented here):")
    for N in (15, 18, 20):
        f = floor(N)
        for bname, b in (("<0.35", 0.35), ("<0.13", 0.13)):
            print("    N={:>2}: to meet {} need floor /{:.1f} at v >= 1500".format(N, bname, f / b))
    print("    Collision KE (whole-rod CM, 1859 machinery) vs E_ee = 0.9 MeV barrier scale:")
    for N in (15, 20):
        for v in (1150.0, 1500.0, 3500.0):
            KE = 0.5 * (N * M_EL / 2) * (v / C) ** 2
            print("      N={:>2} v={:>4.0f}: KE = {:6.3f} MeV  (KE/E_ee = {:5.2f})".format(
                N, v, KE, KE / E_EE))
    print("    -> a transmission/soften onset tied to E_ee turns ON near ~3500-4000 km/s")
    print("       (KE ~ E_ee), NOT at 1150-1500. A cluster-velocity floor cutoff needs a")
    print("       barrier scale ~0.06-0.13 MeV -- ~7-15x below E_ee. No corpus basis yet.")

    # (5) p(v) profile of the total curve ----------------------------------------------
    print("\n(5) p(v) = d ln sigma_total / d ln v at the chi point (N = 18, flat):")
    for v in (10, 20, 40, 50, 100, 200, 400, 800, 1150, 1500, 3000):
        print("      v={:>5}: sigma = {:8.2f}   p = {:+.2f}".format(
            v, total(v, 0.30, 18), p_slope(v, 0.30, 18)))
    print("    (floor flattens p -> 0 wherever it dominates: everything above ~400 km/s)")

    print("\n" + "=" * 78)
    print(" READ-OUT: see reasoning/1867.md for verdicts and founder decision points.")
    print("=" * 78)
