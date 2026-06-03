#!/usr/bin/env python3
"""
0741_rolloff_law.py
===================
The make-or-break: does the H-axiom's superposition-thinning roll-off PREDICT the
observed spectral tilt n_s ~ 0.965, or only get TUNED to it? (Brick #4 / 0738
left n_s as a free tuning; this derives the roll-off from first principles.)

THE FIRST-PRINCIPLES ROLL-OFF.
  * H-axiom (Thomas): a GP boosts its PSR_base by (1+H) each tick it is in
    superposition (>=2 CPs on it), factor 1 otherwise. So the BACKGROUND
    expansion rate is set by the fraction of GPs still superposed:
        H_eff(N) = H0 * f(N),   f = fraction of GPs with occupancy >= 2.
  * Dilution: the scale factor a = e^N; occupied-GP volume ~ a^3, so the mean
    occupancy dilutes as  n_bar(N) = n_bar_init * exp(-3N),  n_bar_init = N_CP/N_GP_init.
  * Poisson occupancy statistics => f(N) = 1 - e^{-n_bar}(1 + n_bar)  (P(k>=2)).
  * Spectrum: each mode freezes at horizon crossing with amplitude ~ H_eff, so
        n_s - 1 = 2 * d ln H_eff / dN = 2 * d ln f / dN     (evaluated at crossing).
    The observable CMB window is ~7-8 e-folds of scales that crossed ~50-60
    e-folds before the end of inflation.

THE TEST: compute n_s(N) across the observable window from these dynamics ALONE
(no tuning) and compare to Planck (n_s = 0.9649 +- 0.0042, small running).
"""

import numpy as np

NS_PLANCK = 0.9649
NS_ERR = 0.0042
N_CP = 1e80          # observable-universe CP count (Brick #4 Test C)
N_GP_INIT = 13       # finite initial patch
n_bar_init = N_CP / N_GP_INIT


def n_bar(N):
    return n_bar_init * np.exp(-3.0 * N)


def f_superposed(N):
    """Poisson fraction of GPs with occupancy >= 2. Stable for large n_bar."""
    nb = n_bar(N)
    # for large nb, e^{-nb}(1+nb) underflows -> f = 1
    with np.errstate(over='ignore', under='ignore'):
        tail = np.exp(-nb) * (1.0 + nb)
    return 1.0 - tail


def ns_of_N(N, h=1e-4):
    """n_s = 1 + 2 d ln f/dN (central difference)."""
    lnf = lambda x: np.log(np.clip(f_superposed(x), 1e-300, None))
    dlnf = (lnf(N + h) - lnf(N - h)) / (2 * h)
    return 1.0 + 2.0 * dlnf


def main():
    print("=" * 72)
    print("ROLL-OFF LAW: does superposition-thinning PREDICT n_s ~ 0.965?")
    print("=" * 72)
    print(f"  n_bar_init = N_CP/N_GP = {N_CP:.0e}/{N_GP_INIT} = {n_bar_init:.2e}")

    # locate end of inflation: f drops through 0.5 (graceful exit underway)
    Ngrid = np.linspace(0, 70, 700001)
    fvals = f_superposed(Ngrid)
    N_end = Ngrid[np.argmin(np.abs(fvals - 0.5))]
    print(f"  end of inflation (f=0.5) at N_end = {N_end:.2f} e-folds  "
          f"(n_bar there = {n_bar(N_end):.2f})")

    # where is the gentle-tilt region n_s ~ 0.965? find N with n_s in Planck band
    print(f"\n  Planck target: n_s = {NS_PLANCK} +- {NS_ERR}")
    print(f"\n  {'N (e-folds)':>12} | {'n_bar':>12} | {'f':>10} | {'n_s':>10}")
    print("  " + "-" * 52)
    for N in [N_end - 55, N_end - 40, N_end - 20, N_end - 10, N_end - 5,
              N_end - 2, N_end - 1, N_end - 0.5, N_end]:
        nb = n_bar(N)
        f = f_superposed(N)
        ns = ns_of_N(N)
        flag = "  <- Planck band" if abs(ns - NS_PLANCK) < 5 * NS_ERR else ""
        print(f"  {N:>12.2f} | {nb:>12.2e} | {f:>10.6f} | {ns:>10.4f}{flag}")

    # the observable window: ~55 e-folds before end (largest scale) to ~47 (smallest)
    print("\n--- The observable CMB window (crossed ~47-55 e-folds before end) ---")
    obs = []
    for dN in (55, 53, 51, 49, 47):
        N = N_end - dN
        obs.append(ns_of_N(N))
        print(f"   N_end-{dN}: n_bar={n_bar(N):.2e}, n_s={ns_of_N(N):.6f}")
    obs = np.array(obs)
    print(f"\n  n_s across observable window: min={obs.min():.6f}, max={obs.max():.6f}")
    print(f"  => observable n_s ~ {obs.mean():.4f} (Harrison-Zel'dovich, n_s=1)")

    # where does the tilt actually live?
    N_tilt = N_end - 1.0
    print(f"\n--- Where the red tilt actually lives ---")
    print(f"  n_s reaches ~{NS_PLANCK} only near N_end-1 (n_bar~{n_bar(N_tilt):.0f}),")
    print(f"  i.e. in the LAST ~1 e-fold = the very smallest (sub-observable) scales,")
    print(f"  NOT across the observable window. And there it is RUNNING fast, not flat.")

    print("\n" + "=" * 72)
    print("VERDICT")
    print("=" * 72)
    obs_flat = abs(obs.mean() - 1.0) < 0.01
    print(f"  The first-principles superposition-thinning roll-off PREDICTS")
    print(f"  n_s ~ 1.000 (Harrison-Zel'dovich) across observable scales, because the")
    print(f"  superposed fraction f stays = 1 while occupancy n_bar >> 1 -- which holds")
    print(f"  for all but the final ~1 e-fold. Planck EXCLUDES n_s=1 at ~8 sigma.")
    print(f"  The graceful-exit roll-off is too SHARP (confined to the last ~1 e-fold,")
    print(f"  the smallest scales) to produce the observed gentle red tilt across the")
    print(f"  observable window.")
    print(f"\n  => n_s is NOT delivered as a prediction; the SIMPLEST roll-off is in")
    print(f"     TENSION with data (predicts HZ). Getting n_s=0.965 needs a SUSTAINED")
    print(f"     gentle decline d ln H_eff/dN ~ -0.017 over the full observable window")
    print(f"     (~50 e-folds), which Poisson dilution does NOT supply (it gives ~0")
    print(f"     until the sharp end). This is now the sharpest open problem in the")
    print(f"     early-universe sector. HONEST RESULT: a found problem, not a fit.")


if __name__ == "__main__":
    main()
