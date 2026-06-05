#!/usr/bin/env python3
"""
0748_launch_lane_test.py
========================
Tests Copilot's "crowded launch lane" mechanism for the H-engine depth law.
Proposal: n CPs stacked on a GP all launch along the SSV direction; random order,
finite reach PSR_base, no passing, no double occupancy. CLAIM: the order statistics
give a HARMONIC progression -> PSR_base(n) ~ ln n -> n_s = 0.9649.

Hold the same standard we held the earlier rules to: SIMULATE the mechanism and
MEASURE PSR_base(n). Do not accept "plausibly harmonic" on faith.

Map to spectrum (0742/0746): if PSR_base(n) ~ g(n), the per-tick boost is
H_eff ~ d ln(scale)/dtick ~ g(nbar); n_s - 1 = 2 d ln g(nbar)/dN, nbar = nbar_init
e^{-3N}, pivot N_rem ~ 57. Need g(n) ~ ln n for 0.9649.
"""

import numpy as np

N_CP, N_GP_INIT = 1e80, 13
N_star = (1.0/3.0)*np.log(N_CP/N_GP_INIT)
Np = N_star - 57.0
nbar_pivot = (N_CP/N_GP_INIT)*np.exp(-3.0*Np)


def ns_for_growth(g, n_at_pivot, dlnn_dN=-3.0):
    """n_s = 1 + 2 d ln g(nbar)/dN; d ln g/dN = (g'(n) n / g(n)) * dlnn_dN."""
    n = n_at_pivot
    h = max(n*1e-6, 1.0)
    dlng_dlnn = (np.log(g(n+h)) - np.log(g(n-h)))/(np.log(n+h)-np.log(n-h))
    return 1.0 + 2.0*dlng_dlnn*dlnn_dN


# ---- 1D no-passing lane: simulate ----
def sim_1d_lane(n, L):
    """n CPs launch from 0 along a lane of L sites; random order; no passing, no
    double occupancy; each reaches as far as it can (blocked by occupied ahead)."""
    occupied = np.zeros(L+1, dtype=bool)
    order = np.random.permutation(n)
    positions = []
    for _ in order:
        # march from L inward to find farthest free site reachable without passing
        # (no-passing from origin => farthest free site below the nearest occupied)
        pos = L
        while pos >= 1 and occupied[pos]:
            pos -= 1
        if pos >= 1:
            occupied[pos] = True
            positions.append(pos)
    return np.array(positions)


# ---- 3D radial fill: simulate ----
def sim_3d_fill(n):
    """n CPs launch in random directions from origin; each occupies the first free
    integer-radius GP along its ray. Returns max radius reached."""
    occ = set()
    maxr = 0
    for _ in range(n):
        d = np.random.randn(3); d /= np.linalg.norm(d)
        r = 1
        while True:
            cell = tuple(np.round(r*d).astype(int))
            if cell not in occ:
                occ.add(cell); maxr = max(maxr, r); break
            r += 1
    return maxr


def main():
    print("="*78)
    print("TEST: does Copilot's 'crowded launch lane' give harmonic ln(n)?")
    print("="*78)
    print(f"  pivot nbar ~ {nbar_pivot:.1e}; target n_s = 0.9649 needs PSR_base(n) ~ ln n.\n")

    # 1D lane
    print("--- 1D no-passing lane (simulated) ---")
    L = 200000
    for n in (100, 1000, 10000):
        pos = sim_1d_lane(n, L)
        print(f"   n={n:>6}: max reach = {pos.max()} (= L, constant); "
              f"mean reach = {pos.mean():.0f} (= L-(n-1)/2, LINEAR in n)")
    print("   => outermost reach is CONSTANT (=L) -> PSR_base(n)=const -> n_s=1 (cliff).")
    print("      mean reach is LINEAR-decreasing. Neither is ln n. And a lane cannot")
    print("      even hold n~1e79 CPs. NOT harmonic.\n")

    # 3D fill
    print("--- 3D radial fill (simulated): measure R(n) scaling ---")
    ns_list = [200, 800, 3200, 12800]
    Rs = []
    for n in ns_list:
        R = np.mean([sim_3d_fill(n) for _ in range(3)])
        Rs.append(R)
        print(f"   n={n:>6}: max radius R = {R:.1f}")
    # fit exponent: R ~ n^beta
    beta = np.polyfit(np.log(ns_list), np.log(Rs), 1)[0]
    print(f"   fitted exponent: R ~ n^{beta:.3f}  (expect 1/3 = 0.333 for 3D fill)")
    print("   => PSR_base(n) ~ n^(1/3), a POWER LAW, not ln n.\n")

    # map each to n_s
    print("--- spectrum each growth law gives (pivot nbar~1e74) ---")
    laws = [
        ("1D lane: PSR_base ~ const",      lambda n: 1.0 + 0*n),
        ("3D fill: PSR_base ~ n^(1/3)",    lambda n: n**(1.0/3.0)),
        ("(target) PSR_base ~ ln n",       lambda n: np.log(n)),
    ]
    print(f"   {'growth law':>30} | {'n_s':>9} | verdict")
    print("   "+"-"*60)
    for label, g in laws:
        if "const" in label:
            val = 1.0
        else:
            val = ns_for_growth(g, nbar_pivot)
        v = ("*** 0.965 ***" if abs(val-0.9649)<0.02 else
             "n_s=1 cliff -- EXCLUDED" if abs(val-1)<1e-3 else
             f"EXCLUDED" if val<0.5 else "off")
        print(f"   {label:>30} | {val:>9.4f} | {v}")

    print("\n" + "="*78)
    print("VERDICT")
    print("="*78)
    print("""  The 'crowded launch lane' mechanism does NOT give harmonic ln(n):
    - 1D no-passing lane: outermost reach is CONSTANT (the first CP always reaches L)
      -> PSR_base ~ const -> n_s = 1 (the HZ cliff). And a 1D lane cannot hold ~1e79
      CPs anyway.
    - 3D radial fill: PSR_base ~ n^(1/3) (a POWER LAW) -> n_s = -1, EXCLUDED. (This is
      the same k^(-2/3) increment Thomas's own shell argument found -- geometric, not
      harmonic.)

  WHY the 'order statistics -> harmonic' claim is wrong: the POSITIONS / gaps of n
  points packed in a lane or ball are UNIFORM (gaps ~ L/n) or power-law (R ~ n^(1/d)),
  NEVER harmonic. The harmonic series 1+1/2+1/3+... appears in probability only in
  RECORDS / coupon-collector counts (expected #records in n trials = sum 1/k) and in
  the entropic derivative d/dn ln(n!) ~ ln n -- NOT in where particles physically land
  under packing/exclusion. This mechanism is packing, so it gives power laws.

  So this is another EXCLUDED candidate, reported straight. The good news in the
  transcript stands: Copilot correctly ruled out geometry (k^-2/3), diffusion
  (Gaussian, not harmonic), linear (n), and (n-1)/n (cliff) -- all consistent with the
  0747 audit. But the new launch-lane mechanism joins the excluded list.

  PATTERN (the real lesson): mechanical, geometric, and packing/exclusion primitives
  ALL give power laws or constants -> all excluded. The log appears ONLY from genuinely
  STATISTICAL-COMBINATORIAL sources -- the configurational chemical potential
  (d ln(n!)/dn ~ ln n) or records/coupon-collector counting. CPP's geometric/dynamical
  primitives keep returning power laws; getting ln n looks to require a genuinely
  entropic (microstate-counting) ingredient, not a placement/launch rule. That is the
  honest open tension: the data want ln n, CPP's placement primitives keep giving
  power laws.

  STATUS UNCHANGED: architecture right (0746); organic ln(n) mechanism still NOT found;
  the launch-lane route is now also excluded. n_s=0.9649 remains viable & favored, not
  derived.""")


if __name__ == "__main__":
    np.random.seed(0)
    main()
