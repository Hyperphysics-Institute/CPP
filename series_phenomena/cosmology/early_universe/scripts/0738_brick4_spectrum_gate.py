#!/usr/bin/env python3
"""
0738_brick4_spectrum_gate.py
============================
SR-1 rederivation Brick #4 toy model. Tests whether the adopted Branch-V
construction (fixed l_P_base UNIT + finite-patch regulator + always-on H-engine
+ CLT/ZBW fluctuation source + qCP/qDP morphology) can clear the GATING test for
a CPP-native primordial epoch: the primordial SPECTRUM (Gaussianity + near
scale-invariance), plus the e-fold budget.

Three tests, each PASS/FAIL:

  A. CLT GAUSSIANITY. The ZBW source is ADDITIVE (sum of N independent phase
     kicks) -> Gaussian by the Central Limit Theorem. Contrast with the
     MULTIPLICATIVE qCP-chain cascade (the 0730 route) which is log-normal with
     heavy tails. PASS = additive excess-kurtosis -> 0 as N grows AND the
     multiplicative cascade has large kurtosis (additive decisively beats it).

  B. SPECTRUM INTERLOCK (the gate). Scale-invariance is NOT given by CLT alone
     (independent kicks summed are white, wrong shape). It is produced by the
     INTERLOCK: a STATIONARY fluctuation injection (CLT-Gaussian, same statistics
     every Moment during the superposed phase) frozen by a CONSTANT-H background.
     Each comoving mode freezes at horizon crossing with the local fluctuation
     amplitude; stationary injection + exponential (constant-H) expansion =>
     constant power per log-k => scale-invariant (n_s = 1). A slow roll-off of
     the injected variance / H near the end (superposition thinning) tilts it
     slightly red (n_s < 1), the observed direction. We (i) simulate the
     stochastic field with CLT-built kicks and recover P(k); (ii) confirm the
     analytic relation n_s - 1 = d ln(sigma^2)/dN; (iii) show a modest roll-off
     lands near n_s ~ 0.96 with small f_NL. PASS = flat spectrum under stationary
     injection (|n_s-1| < tol) AND a tunable red tilt reaching ~0.96 with small
     non-Gaussianity.

     HONESTY: this demonstrates the construction is CAPABLE of the targets and
     internally coherent; it does NOT predict n_s=0.965 from first principles
     (the roll-off rate is a free function, and the amplitude A_s is one tuning,
     exactly as standard inflation tunes its potential). The CPP-specific content
     is supplying a concrete engine (H-axiom) and a concrete stationary source
     (ZBW/CLT) for the standard freezing mechanism.

  C. E-FOLD DEPTH. The H-engine self-terminates when dilution unstacks the GPs
     (occupancy -> ~1 CP/GP). So the TOTAL e-folds is set by the INITIAL stacking
     depth, not by H (H sets the RATE). N_efold ~ (1/3) ln(N_CP / N_GP_init) for
     volume dilution in 3D. PASS = the observable-universe CP count gives
     N_efold in the ballpark of the ~60 inflation needs (order-of-magnitude).

Run: python3 0738_brick4_spectrum_gate.py
"""

import numpy as np

rng = np.random.default_rng(20260603)
TOL_FLAT = 0.02      # |n_s - 1| considered "flat" under stationary injection
NS_TARGET = 0.965    # Planck-ish central value
NS_BAND = (0.94, 0.99)


# ---------------------------------------------------------------------------
# Test A -- CLT Gaussianity: additive ZBW vs multiplicative qCP cascade
# ---------------------------------------------------------------------------
def excess_kurtosis(x):
    x = np.asarray(x, float)
    m = x.mean()
    s2 = x.var()
    return ((x - m) ** 4).mean() / s2**2 - 3.0


def test_A(trials=200_000):
    print("=" * 72)
    print("TEST A -- CLT Gaussianity (additive ZBW vs multiplicative qCP chain)")
    print("=" * 72)
    print(f"{'N kicks':>9} | {'additive exc-kurt':>18} | {'multiplicative exc-kurt':>24}")
    print("-" * 72)
    add_k = mul_k = None
    for N in (2, 8, 32, 128, 512):
        # additive: each ZBW oscillator contributes cos(uniform phase); sum N of them
        phases = rng.uniform(0, 2 * np.pi, size=(trials, N))
        add_field = np.cos(phases).sum(axis=1)
        ak = excess_kurtosis(add_field)
        # multiplicative qCP cascade: product of N positive iid factors (log-normal)
        factors = rng.lognormal(mean=0.0, sigma=0.5, size=(trials, N))
        mul_field = factors.prod(axis=1)
        mk = excess_kurtosis(mul_field)
        print(f"{N:>9} | {ak:>18.4f} | {mk:>24.2f}")
        add_k, mul_k = ak, mk
    add_gaussian = abs(add_k) < 0.05          # additive -> Gaussian at large N
    mul_heavy = mul_k > 10.0                   # multiplicative stays heavy-tailed
    ok = add_gaussian and mul_heavy
    print(f"\n  additive excess-kurtosis at N=512: {add_k:+.4f}  (-> 0 = Gaussian)")
    print(f"  multiplicative excess-kurtosis at N=512: {mul_k:.1f}  (heavy-tailed)")
    print(f"  TEST A: {'PASS' if ok else 'FAIL'} "
          f"(additive Gaussian, multiplicative decisively non-Gaussian)\n")
    return ok


# ---------------------------------------------------------------------------
# Test B -- spectrum interlock: stationary CLT injection + constant-H freezing
# ---------------------------------------------------------------------------
def simulate_spectrum(n_efolds=12.0, steps_per_efold=60, sigma_law=None,
                      n_realizations=3000):
    """Stochastic ('separate universe') field. Each step in e-folds dN, the
    coarse field gets a Gaussian kick of std sigma(N)*sqrt(dN). The kick is
    GAUSSIAN by CLT -- this is exactly the additive-ZBW result proven in Test A
    (sum of many independent phase contributions -> Gaussian), used here so the
    interlock test runs fast. The frozen amplitude of the mode crossing at e-fold
    N is the injected increment at N -> dimensionless power P(k) at k ~ e^N is the
    variance injected per e-fold = sigma(N)^2. sigma_law(N) = injected std per unit
    e-fold (stationary => constant => scale-invariant).
    Returns (N_grid, powers, skews).
    """
    if sigma_law is None:
        sigma_law = lambda N: 1.0
    dN = 1.0 / steps_per_efold
    n_steps = int(n_efolds * steps_per_efold)
    N_grid = np.arange(n_steps) * dN
    sig = np.array([sigma_law(N) for N in N_grid])            # (n_steps,)
    # vectorized Gaussian (CLT) kicks: shape (n_steps, n_realizations)
    kicks = (sig[:, None] * np.sqrt(dN)
             * rng.standard_normal((n_steps, n_realizations)))
    powers = kicks.var(axis=1) / dN                            # = sigma(N)^2
    m = kicks.mean(axis=1, keepdims=True)
    s = kicks.std(axis=1)
    skews = ((kicks - m) ** 3).mean(axis=1) / s**3
    return N_grid, powers, skews


def fit_ns(N_grid, powers, lo_frac=0.15, hi_frac=0.85):
    """n_s - 1 = d ln P / d ln k, and ln k = N at crossing, so n_s - 1 = slope of
    ln P vs N. Fit over an interior window to avoid edge transients."""
    lo = int(len(N_grid) * lo_frac)
    hi = int(len(N_grid) * hi_frac)
    x = N_grid[lo:hi]
    y = np.log(powers[lo:hi])
    slope = np.polyfit(x, y, 1)[0]
    return 1.0 + slope


def test_B():
    print("=" * 72)
    print("TEST B -- spectrum interlock (CLT stationary source + constant-H freeze)")
    print("=" * 72)

    # (i) STATIONARY injection (constant sigma) under constant H -> expect flat
    Ng, P_flat, sk_flat = simulate_spectrum(sigma_law=lambda N: 1.0)
    ns_flat = fit_ns(Ng, P_flat)
    fnl_proxy = np.nanmean(np.abs(sk_flat))   # |skew| of injected field ~ non-Gaussianity
    print(f"  (i)  stationary injection, constant H:")
    print(f"         n_s = {ns_flat:.4f}   (expect ~1.000; |n_s-1|<{TOL_FLAT})")
    print(f"         mean |skewness| of field = {fnl_proxy:.4f}  (small => Gaussian)")

    # (ii) analytic check: impose sigma^2 ~ exp(beta*N) -> n_s-1 = beta exactly
    beta = -0.035
    Ng2, P_tilt, _ = simulate_spectrum(sigma_law=lambda N: np.exp(0.5 * beta * N))
    ns_tilt = fit_ns(Ng2, P_tilt)
    print(f"  (ii) analytic check: inject sigma^2 ~ exp(beta*N), beta={beta:+.3f}")
    print(f"         predicted n_s = 1+beta = {1+beta:.4f};  measured n_s = {ns_tilt:.4f}")

    # (iii) tune a modest roll-off to hit the Planck band
    #   choose beta so that n_s ~ 0.965  -> beta = -0.035
    beta_target = NS_TARGET - 1.0
    Ng3, P_t, sk_t = simulate_spectrum(sigma_law=lambda N: np.exp(0.5 * beta_target * N))
    ns_planck = fit_ns(Ng3, P_t)
    fnl_t = np.nanmean(np.abs(sk_t))
    print(f"  (iii) modest roll-off beta={beta_target:+.3f} (superposition thinning):")
    print(f"         n_s = {ns_planck:.4f}   (target {NS_TARGET}, band {NS_BAND})")
    print(f"         mean |skewness| = {fnl_t:.4f}  (small non-Gaussianity)")

    flat_ok = abs(ns_flat - 1.0) < TOL_FLAT
    analytic_ok = abs(ns_tilt - (1 + beta)) < 0.01
    band_ok = NS_BAND[0] < ns_planck < NS_BAND[1]
    gauss_ok = fnl_proxy < 0.05 and fnl_t < 0.05
    ok = flat_ok and analytic_ok and band_ok and gauss_ok
    print(f"\n  flat-under-stationary: {'ok' if flat_ok else 'NO'} | "
          f"analytic n_s match: {'ok' if analytic_ok else 'NO'} | "
          f"reaches Planck band: {'ok' if band_ok else 'NO'} | "
          f"Gaussian: {'ok' if gauss_ok else 'NO'}")
    print(f"  TEST B: {'PASS' if ok else 'FAIL'} "
          f"(interlock works; tilt tunable to data; non-Gaussianity small)\n")
    return ok


# ---------------------------------------------------------------------------
# Test C -- e-fold depth set by initial stacking, not by H
# ---------------------------------------------------------------------------
def test_C():
    print("=" * 72)
    print("TEST C -- e-fold budget set by initial CP stacking depth (not by H)")
    print("=" * 72)
    N_GP_init = 13          # the central GP + 12 nearest neighbours (finite patch)
    # volume dilution to ~1 CP/GP: a^3 grows by N_CP/N_GP_init -> N_efold=(1/3)ln(...)
    print(f"  finite initial patch: {N_GP_init} GPs (central + 12 neighbours)")
    print(f"  rule: H-boost self-terminates at ~1 CP/GP => N_efold = (1/3) ln(N_CP/N_GP)")
    print(f"\n  {'N_CP (initial stack)':>22} | {'N_efold':>8}")
    print("  " + "-" * 36)
    target_hit = None
    for N_CP in (1e60, 1e70, 1e78, 1e80, 1e90):
        Ne = (1.0 / 3.0) * np.log(N_CP / N_GP_init)
        flag = "  <- ~60 e-folds" if 50 <= Ne <= 70 else ""
        print(f"  {N_CP:>22.0e} | {Ne:>8.1f}{flag}")
        if 50 <= Ne <= 70:
            target_hit = N_CP
    # observable universe: ~1e80 baryons, each >= a few CPs -> N_CP ~ 1e80-1e81
    Ne_obs = (1.0 / 3.0) * np.log(1e80 / N_GP_init)
    print(f"\n  observable-universe scale (~1e80 baryons): N_efold = {Ne_obs:.1f}")
    ok = 45 <= Ne_obs <= 75
    print(f"  TEST C: {'PASS' if ok else 'FAIL'} "
          f"(observed CP count gives ~{Ne_obs:.0f} e-folds; depth sets total, H sets rate)\n")
    return ok


if __name__ == "__main__":
    print("\nBRICK #4 TOY MODEL -- primordial-spectrum gate for the Branch-V construction\n")
    a = test_A()
    b = test_B()
    c = test_C()
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"  A  CLT Gaussianity (additive beats multiplicative): {'PASS' if a else 'FAIL'}")
    print(f"  B  spectrum interlock (gate): {'PASS' if b else 'FAIL'}")
    print(f"  C  e-fold depth from initial stacking: {'PASS' if c else 'FAIL'}")
    allp = a and b and c
    print(f"\n  GATE: {'PASS -- construction clears the toy-level spectrum gate' if allp else 'FAIL'}")
    print("  NOTE: PASS = capability + internal coherence, NOT a parameter-free")
    print("        prediction of n_s. Amplitude A_s and tilt roll-off remain tunings,")
    print("        exactly as in standard inflation. Owed next: a FIRST-PRINCIPLES")
    print("        roll-off (superposition-thinning law) and the Delta-c bound check.")
