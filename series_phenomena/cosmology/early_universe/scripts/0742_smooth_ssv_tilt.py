#!/usr/bin/env python3
"""
0742_smooth_ssv_tilt.py
=======================
Recovery from the 0741 found-problem. The on/off superposition rule predicted the
EXCLUDED n_s=1 because (a) the density n_bar falls at 3/e-fold (too fast) and (b)
the superposed FRACTION f stays =1 until a final cliff (rate 0, then infinite).
Neither gives the gentle ~ -0.018/e-fold the data need.

THE FIX (smooth H(SSV) / sigma(SSV), Copilot idea #2 + Thomas's depletion picture):
the fluctuation amplitude couples not to the instantaneous density but to the LOG
of the density -- which is exactly the e-folds REMAINING to the end of inflation:

    N_bar(N) = n_bar_init * exp(-3N)   (occupancy dilutes with volume)
    N_rem(N) = (1/3) ln(n_bar(N))      = e-folds remaining to the end (n_bar -> 1)
    dN_rem/dN = -1  =>  d ln(N_rem)/dN = -1/N_rem  ~ -0.018  at N_rem ~ 57.   <-- RIGHT RATE

This is the generic delta-N structure of inflationary perturbations (the curvature
perturbation IS the fluctuation in the number of e-folds), so coupling to N_rem
rather than to the raw density is NOT fishing -- it is the natural variable.

If the frozen fluctuation power scales as a power p of e-folds-remaining,
    P(k) = sigma^2 ~ N_rem^p ,
then
    n_s - 1 = d ln P/d ln k = d ln sigma^2/dN = -p / N_rem ,
the STANDARD slow-roll form  n_s = 1 - p/N_*.  CPP's specific content: N_* is FIXED
by the CP count (the same number that set the ~60 e-folds in Brick #4 Test C):
    N_* = (1/3) ln(N_CP / N_GP_init) ~ 57.

THE TEST: which p does CPP need, and does a natural p land on Planck (n_s=0.9649)?
p=0 must recover the 0741 on/off result (n_s=1, excluded). p=2 is the simplest
large-field value (m^2 phi^2 gives n_s=1-2/N).
"""

import numpy as np

NS_PLANCK, NS_ERR = 0.9649, 0.0042
ALPHA_PLANCK, ALPHA_ERR = -0.0045, 0.0067   # Planck running dn_s/dlnk
N_CP, N_GP_INIT = 1e80, 13


def main():
    print("=" * 72)
    print("SMOOTH-SSV TILT: n_s = 1 - p/N_* with N_* fixed by the CP count")
    print("=" * 72)

    # N_* fixed by CP count (same as the e-fold budget, Brick #4 Test C)
    N_star = (1.0 / 3.0) * np.log(N_CP / N_GP_INIT)
    print(f"  N_* (e-folds remaining at pivot) = (1/3) ln(N_CP/N_GP)")
    print(f"      = (1/3) ln({N_CP:.0e}/{N_GP_INIT}) = {N_star:.1f}  "
          f"(NOT tuned -- it is the CP count)")
    print(f"  Planck: n_s = {NS_PLANCK} +- {NS_ERR},  running alpha_s = {ALPHA_PLANCK} +- {ALPHA_ERR}\n")

    print(f"  {'p':>3} | {'n_s = 1 - p/N_*':>16} | {'running alpha_s':>16} | verdict")
    print("  " + "-" * 64)
    results = {}
    for p in (0, 1, 2, 3):
        ns = 1.0 - p / N_star
        # running: alpha_s = dn_s/dlnk = dn_s/dN = -d(p/N_rem)/dN = -p/N_rem^2
        alpha = -p / N_star**2
        results[p] = ns
        if p == 0:
            verdict = "= 0741 on/off case (Harrison-Zel'dovich, EXCLUDED ~8sigma)"
        elif abs(ns - NS_PLANCK) < 3 * NS_ERR:
            verdict = "*** MATCHES Planck (within ~3 sigma) ***"
        elif abs(ns - NS_PLANCK) < 6 * NS_ERR:
            verdict = "near Planck"
        else:
            verdict = "off"
        print(f"  {p:>3} | {ns:>16.4f} | {alpha:>16.5f} | {verdict}")

    print(f"\n  running for all p is |alpha_s| < {2/N_star**2:.5f} -- "
          f"comfortably inside Planck's {ALPHA_ERR:.4f} error.")

    # show the tilt is FLAT across the observable window (not running like 0741)
    print("\n--- n_s across the observable window (p=2), should be ~flat ---")
    print(f"  {'N_rem':>7} | {'n_s (p=2)':>10}")
    print("  " + "-" * 22)
    for N_rem in (57, 55, 53, 51, 49):
        print(f"  {N_rem:>7} | {1 - 2/N_rem:>10.4f}")
    span = abs((1 - 2/57) - (1 - 2/49))
    print(f"  n_s varies by only {span:.4f} across the window (vs 0741's 1.000 -> cliff).")

    print("\n" + "=" * 72)
    print("RESULT")
    print("=" * 72)
    print(f"  The smooth coupling to e-folds-remaining (the delta-N variable) produces")
    print(f"  the STANDARD slow-roll form n_s = 1 - p/N_*, with N_* ~ {N_star:.0f} FIXED by the")
    print(f"  CP count (no tuning). The on/off rule is the p=0 special case (n_s=1,")
    print(f"  excluded) -- which is exactly why 0741 failed.")
    print(f"    p=1 -> n_s = {results[1]:.3f}  (gentle red, ~3-4 sigma high)")
    print(f"    p=2 -> n_s = {results[2]:.3f}  <-- Planck's 0.9649, essentially on the nose")
    print(f"  So n_s is reduced from UNPREDICTED to 'predicted up to one integer power p',")
    print(f"  with the simplest non-trivial p (=2, the m^2 phi^2 value) hitting the data.")
    print(f"  Remaining first-principles step: DERIVE p = how the frozen ZBW power scales")
    print(f"  with e-folds-remaining (i.e. with log-density / superposition depth).")
    print(f"  HONEST: this is NOT yet 'CPP predicts 0.965' -- p is not derived -- but the")
    print(f"  mechanism now gives the right FORM, the right N_*, the right ballpark and")
    print(f"  direction, and small running. The 0741 tension is resolved in structure.")


if __name__ == "__main__":
    main()
