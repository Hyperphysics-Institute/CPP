#!/usr/bin/env python3
"""
Patch 2855 - OPEN-K1-MEMORY-1B, Route 2 step 2.

Compute L_field for the bonded Sea: the correlation length of the residual
field seen by a DP after its own partner is subtracted, and the resulting
pair-centre drift suppression ratio

    R_drift = v_centre / v_CP = |E(+) - E(-)| / (2 * E_rms)

which is the quantity Patch 2853 estimated as ~ d_DP / L_field.

COMMITTED INPUTS (alpha1_s1_s2_record.md §3, verbatim 21 July 2026 run;
S4-N monotonic screening result alpha1_s4n_record.md):
    d_DP  = 0.3640220 fm      (= a)
    kappa = 5.4941731 /fm     (kappa * d_DP = 2.0000 exactly)
    n_DP  = 29.3178443 /fm^3
    n_CP  = 58.6356886 /fm^3
    screening: MONOTONIC exponential at l_phys = 1/kappa = d_DP/2 = 0.1820 fm

SOFT-CORE AXIS: {0.02, 0.04, 0.08} fm - NOT invented here; this is the
committed S4-N robustness axis, reused so the regulator is not a free
parameter chosen by this calculation.

Physics of the ratio (C19/C20/C25):
    Each CP displaces along its OWN perceived SSV_net with polarity sign.
    CP+ at +d/2 displaces along +E(+); CP- at -d/2 displaces along -E(-).
    Pair centre velocity  ∝ (1/2)[E(+) - E(-)]
    Individual CP speed   ∝ |E|
    => R_drift = |E(+) - E(-)| / (2 * E_rms).
    v_CP/c = |SSV_net|/SSV_abs <= 1 by C20, so v_centre/c <= R_drift.

No arc-inertia (C23/C24) specification is used anywhere in this script.
"""

import numpy as np

# ---------------- committed constants ----------------
D_DP_REF   = 0.3640220
KAPPA_REF  = 5.4941731
N_DP_REF   = 29.3178443
SOFT_AXIS  = [0.02, 0.04, 0.08]      # committed S4-N robustness axis
BAR        = 0.15                     # operative bar, v/c <= 0.15


def yukawa_E(dvec, kappa, a_soft):
    """Screened Coulomb field. dvec = (field point - charge position)."""
    r2 = np.einsum('...i,...i->...', dvec, dvec) + a_soft * a_soft
    r = np.sqrt(r2)
    pref = (1.0 + kappa * r) * np.exp(-kappa * r) / (r2 * r)
    return dvec * pref[..., None]


def sample_sphere(rng, n):
    v = rng.normal(size=(n, 3))
    return v / np.linalg.norm(v, axis=1, keepdims=True)


def run(n_real, kappa, n_DP, d_DP, a_soft, R_box, svals, rng):
    """Return (C_of_s, drift_ratios). C_of_s = <E(0).E(s)>/<|E(0)|^2>."""
    n_exp = n_DP * (4.0 / 3.0) * np.pi * R_box ** 3
    num = np.zeros(len(svals))
    den = 0.0
    ratios = np.empty(n_real)

    for it in range(n_real):
        npair = rng.poisson(n_exp)
        if npair < 1:
            npair = 1
        # pair centres uniform in sphere
        u = sample_sphere(rng, npair)
        rad = R_box * rng.random(npair) ** (1.0 / 3.0)
        ctr = u * rad[:, None]
        axis = sample_sphere(rng, npair)
        pos_p = ctr + 0.5 * d_DP * axis
        pos_m = ctr - 0.5 * d_DP * axis

        # ---- field points ----
        w = sample_sphere(rng, 1)[0]          # autocorrelation line direction
        pts_line = np.outer(svals, w)         # (ns,3)
        probe = sample_sphere(rng, 1)[0]      # probe pair axis
        pts_probe = np.array([+0.5 * d_DP * probe, -0.5 * d_DP * probe])
        pts = np.vstack([pts_line, pts_probe])

        # E = sum over all other pairs' CPs (+q at pos_p, -q at pos_m).
        # The probe pair is NOT in the list => its own partner is subtracted
        # by construction, which is exactly the residual field 1B asks about.
        dp = pts[:, None, :] - pos_p[None, :, :]
        dm = pts[:, None, :] - pos_m[None, :, :]
        E = (yukawa_E(dp, kappa, a_soft).sum(axis=1)
             - yukawa_E(dm, kappa, a_soft).sum(axis=1))

        E_line = E[:len(svals)]
        num += E_line @ E_line[0]
        den += E_line[0] @ E_line[0]

        Ep, Em = E[len(svals)], E[len(svals) + 1]
        E_rms = np.sqrt(0.5 * (Ep @ Ep + Em @ Em))
        ratios[it] = np.linalg.norm(Ep - Em) / (2.0 * E_rms)

    return num / den, ratios


def L_from_C(svals, C):
    """1/e crossing of the field autocorrelation, linear interp."""
    target = 1.0 / np.e
    for i in range(1, len(C)):
        if C[i] <= target:
            f = (C[i - 1] - target) / (C[i - 1] - C[i])
            return svals[i - 1] + f * (svals[i] - svals[i - 1])
    return float('nan')


def main():
    rng = np.random.default_rng(20260728)
    svals = np.linspace(0.0, 0.60, 25)
    R_box = 1.10
    n_real = 4000

    print("=" * 68)
    print("PATCH 2855 - Route 2 step 2: L_field for the bonded Sea")
    print("=" * 68)
    print(f"committed: d_DP={D_DP_REF:.7f} fm  kappa={KAPPA_REF:.7f} /fm  "
          f"n_DP={N_DP_REF:.7f} /fm^3")
    print(f"           kappa*d_DP = {KAPPA_REF*D_DP_REF:.4f}")
    print(f"           1/kappa    = {1.0/KAPPA_REF:.4f} fm  (= d_DP/2)")
    print(f"           n_DP^(-1/3)= {N_DP_REF**(-1.0/3.0):.4f} fm  "
          f"(mean inter-pair spacing)")
    print(f"           R_ws       = {(3.0/(4*np.pi*N_DP_REF))**(1/3):.4f} fm")
    print()
    print("  NOTE: both candidate correlation lengths (screening 0.1820 fm,")
    print("        spacing 0.3243 fm) are SMALLER than d_DP = 0.3640 fm.")
    print()

    print("-" * 68)
    print("A. AT THE COMMITTED DENSITY - soft-core sensitivity")
    print("-" * 68)
    print(f"{'a_soft':>8} {'L_field(fm)':>12} {'d_DP/L':>9} "
          f"{'R_drift mean':>13} {'RMS':>8} {'median':>8}")
    for a in SOFT_AXIS:
        C, rat = run(n_real, KAPPA_REF, N_DP_REF, D_DP_REF, a, R_box,
                     svals, rng)
        L = L_from_C(svals, C)
        print(f"{a:8.3f} {L:12.4f} {D_DP_REF/L:9.3f} "
              f"{rat.mean():13.4f} {np.sqrt((rat**2).mean()):8.4f} "
              f"{np.median(rat):8.4f}")

    print()
    print("-" * 68)
    print("B. DILUTION SCAN - how dilute would the Sea have to be?")
    print("    kappa_D^2 = 4*pi*n_CP*q^2/theta  =>  kappa scales as sqrt(n)")
    print("    d_DP held fixed (it is a bond length, not a density scale)")
    print("-" * 68)
    print(f"{'n/n_ref':>9} {'spacing':>9} {'1/kappa':>9} {'L_field':>9} "
          f"{'RMS':>8} {'median':>8} {'<=0.15?':>8}")
    for f in [1.0, 0.3, 0.1, 0.03, 0.01, 3e-3, 1e-3, 3e-4]:
        n = N_DP_REF * f
        k = KAPPA_REF * np.sqrt(f)
        spacing = n ** (-1.0 / 3.0)
        Rb = max(3.5 * spacing, 4.5 / k)
        sv = np.linspace(0.0, min(4.0 * spacing, 3.0 / k), 25)
        C, rat = run(800, k, n, D_DP_REF, 0.04, Rb, sv, rng)
        L = L_from_C(sv, C)
        r = np.sqrt((rat ** 2).mean())
        print(f"{f:9.4g} {n**(-1/3):9.4f} {1/k:9.4f} {L:9.4f} "
              f"{r:8.4f} {np.median(rat):8.4f} "
              f"{'YES' if r <= BAR else 'no':>8}")

    print()
    print("-" * 68)
    print("C. VERDICT")
    print("-" * 68)
    C, rat = run(n_real, KAPPA_REF, N_DP_REF, D_DP_REF, 0.04, R_box,
                 svals, rng)
    L = L_from_C(svals, C)
    r = np.sqrt((rat ** 2).mean())
    ceiling = 1.0 / np.sqrt(2.0)
    print(f"  L_field   = {L:.4f} fm   (d_DP/L_field = {D_DP_REF/L:.3f})")
    print(f"  R_drift   = {r:.4f}  (RMS)")
    print(f"  ceiling   = {ceiling:.4f}  = 1/sqrt(2), the value R_drift takes")
    print(f"              when E(+) and E(-) are STATISTICALLY INDEPENDENT")
    print(f"  R/ceiling = {r/ceiling:.4f}   <-- saturated to within "
          f"{abs(r/ceiling-1)*100:.1f}%")
    print(f"  bar       = {BAR}")
    print(f"  margin    = {r/BAR:.2f}x the bar")
    print()
    print("  L_field is REGULATOR-SENSITIVE (0.059-0.152 fm across the")
    print("  committed soft-core axis) because the E^2-weighted correlation")
    print("  is dominated by close encounters. R_drift, the quantity it was")
    print("  a proxy FOR, is NOT: it is 0.71 at every soft-core value.")
    print("  So the proxy is discarded and the target computed directly.")
    print()
    print("  The gradient expansion v_centre/v_CP ~ d_DP/L_field REQUIRES")
    print("  d_DP << L_field. Here d_DP > L_field, so the expansion does not")
    print("  hold and the ratio SATURATES: the two CPs of a pair sample")
    print("  effectively uncorrelated environments, so the C19/C20 polarity")
    print("  cancellation that protects the pair centre does not operate.")
    print()
    print("  Route 2 does NOT close 1B at the committed Sea parameters.")


if __name__ == '__main__':
    main()
