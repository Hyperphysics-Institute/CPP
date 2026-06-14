#!/usr/bin/env python3
"""C5 pre-registration band — numerical checks (CPP Patch 1208).

Verifies the EU-1 spectral-index prediction values and the Simons-Observatory
survival-band logic used in C5_ns_pre-registration_band.md. Pure-stdlib; no deps.
"""

Ns = 57
ns = 1 - 2 / Ns                 # scalar spectral index, pivot N* = 57
alpha = -2 / Ns ** 2            # running dn_s/dln k
planck_sigma = 0.0042          # Planck 2018 sigma(n_s)
theory_band = 5e-4             # EU-1 leading-correction theory band

# --- core prediction values ---
assert abs(ns - 0.9649) < 1e-3, ns
assert abs(alpha + 0.00062) < 1e-4, alpha
assert abs(theory_band / planck_sigma - 0.12) < 0.02, theory_band / planck_sigma
print(f"n_s(N*=57)      = {ns:.6f}   (Planck 2018 central 0.9649 -> postdiction)")
print(f"alpha_s(N*=57)  = {alpha:.6f}  (Planck running 0.0011 +/- 0.0099 -> not yet resolved)")
print(f"theory band     = {theory_band:.1e}  = {theory_band/planck_sigma:.3f} sigma_Planck")

# --- point vs band: derived N*=57 gives a point; free [55,60] gives a band ---
print("\nn_s across N* (derived 57 => point; free range => band):")
vals = {N: 1 - 2 / N for N in (55, 57, 60, 60.5)}
for N, v in vals.items():
    print(f"  N*={N:>5}: n_s={v:.6f}")
band_width = max(vals[55], vals[60]) - min(vals[55], vals[60])
print(f"  band width if N* free in [55,60] ~ {band_width:.4f} (>> theory band {theory_band:.0e})")

# --- survival band vs measured sigma (Grok^Copilot converged criteria) ---
def legs(sigma_meas):
    return dict(
        two_x_tighter=sigma_meas <= planck_sigma / 2,      # >= 2x tighter than Planck?
        consistency_halfwindow=0.5 * sigma_meas,           # |n_s_meas - 0.9649| must be <= this
        falsify_if_dev_gt=3 * sigma_meas,                  # 3-sigma tension falsifies
    )

print("\nsurvival band vs forecast sigma(n_s):")
for sm in (0.0030, 0.0026, 0.0020, 0.0015):                 # SO+Planck ~ 0.0020
    L = legs(sm)
    print(f"  sigma_meas={sm:.4f}: 2x-tighter={L['two_x_tighter']!s:>5} "
          f"consistency=+/-{L['consistency_halfwindow']:.4f} "
          f"falsify if |dev|>{L['falsify_if_dev_gt']:.4f}")

# SO+Planck (~0.0020) must satisfy the 2x-tighter leg
assert legs(0.0020)["two_x_tighter"] is True
print("\nSO+Planck (sigma~0.0020) satisfies the 2x-tighter leg: confirmed-beyond-postdiction reachable.")
print("ALL CHECKS PASS")
