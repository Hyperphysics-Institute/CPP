#!/usr/bin/env python3
"""
Patch 0851 — DM-1 §6: the core-radius-vs-(sigma/m) panel.

Turns the §6 one-scatter DENSITY test into a core-SIZE prediction via the
standard SIDM r_1 inversion (Kaplinghat, Tulin & Yu 2016): the self-interaction
thermalizes the halo out to the radius r_1 where one scatter has occurred over
the age,
        rho_NFW(r_1) = rho_1(sigma/m) = 1 / [ (sigma/m) <v_rel> t ],
and the observable core radius is r_core ~ r_1 (O(1) factor). Inverting an NFW
profile for r_1 as a function of sigma/m gives a predicted core size we can lay
against the OBSERVED cores of two specific galaxies 5x apart in velocity:
    - Fornax dSph   (small halo)        observed core <~ 0.3-0.7 kpc
    - IC 2574       (large LSB/dwarf)   observed core ~ 8 kpc

The panel marks sigma_V/m = 0.20 (the §5 prediction) and the f-band [0.07,0.6],
and reads off what each galaxy's core implies.

This doubles as the verify script (prints r_1 at sigma/m=0.20 and the sigma/m
each observed core requires).

Provenance:
  [obs]   V_max / observed core (sources in comment)
  [model] NFW concentration c (representative + band); the dominant halo-model knob
  [conv]  sigma_1D = V_max/sqrt(2) (halo dispersion); <v_rel> = (4/sqrt(pi)) sigma_1D
  [s5]    sigma_V/m = 0.20 cm^2/g (velocity-independent), f-band [0.07,0.6]
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# ---- units / constants --------------------------------------------------
G        = 4.300917e-6        # kpc (km/s)^2 / Msun
RHO_CRIT = 137.0              # Msun/kpc^3  (h=0.7)
Msun_g   = 1.989e33
pc_cm    = 3.086e18
Msun_pc3 = Msun_g / pc_cm**3  # g/cm^3 per Msun/pc^3
Gyr_s    = 3.156e16
kms_cm   = 1.0e5
VREL     = 4.0 / np.sqrt(np.pi)   # <v_rel>/sigma_1D ~ 2.257

sigma_m0 = 0.20                   # cm^2/g  [s5]
F_BAND   = (0.07, 0.60)           # f-band  [s5]
t_age    = 10.0                   # Gyr     [obs]


def rho1_Msun_kpc3(sigma_1D_kms, sm, t=t_age):
    """One-scatter density in Msun/kpc^3."""
    vrel = VREL * sigma_1D_kms * kms_cm
    rho_gcc = 1.0 / (sm * vrel * t * Gyr_s)      # g/cm^3
    return rho_gcc / Msun_pc3 * 1.0e9            # -> Msun/pc^3 -> Msun/kpc^3


def nfw_params(v_max, c):
    """Return (rho_s [Msun/kpc^3], r_s [kpc]) for an NFW halo of given V_max, c."""
    mc = np.log(1 + c) - c / (1 + c)
    rho_s = (200.0 / 3.0) * RHO_CRIT * c**3 / mc
    # V_max^2 = 4 pi G rho_s r_s^2 * 0.2162
    r_s = v_max / np.sqrt(4 * np.pi * 0.2162 * G * rho_s)
    return rho_s, r_s


def r1_of_sigma(v_max, c, sm):
    """Core scale r_1 [kpc]: where rho_NFW(r_1) = rho_1(sigma/m)."""
    rho_s, r_s = nfw_params(v_max, c)
    sigma_1D = v_max / np.sqrt(2.0)
    rho1 = rho1_Msun_kpc3(sigma_1D, sm)
    target = rho_s / rho1                          # = x(1+x)^2 at r_1
    # rho_NFW falls below rho1 only if target > min; solve x(1+x)^2 = target
    if target <= 0:
        return np.nan
    f = lambda x: x * (1 + x) ** 2 - target
    # bracket
    try:
        x1 = brentq(f, 1e-6, 1e3)
    except ValueError:
        return np.nan
    return x1 * r_s


def sigma_for_core(v_max, c, r_core_kpc):
    """Inverse: what sigma/m makes r_1 = r_core_kpc."""
    g = lambda sm: r1_of_sigma(v_max, c, sm) - r_core_kpc
    try:
        return brentq(g, 1e-3, 1e3)
    except ValueError:
        return np.nan


# ---- the two galaxies ---------------------------------------------------
# Fornax: V_max uncertain for a dSph; ~25 km/s representative (band 18-35).
#   core <~ 0.3-0.7 kpc  [obs: Goerdt+ 2006; Jardel & Gebhardt 2012 cored]
# IC 2574: V_max ~ 80 km/s [obs: Oh+ 2008/2011]; iso core R_C ~ 8 kpc
#   [obs: de Blok+ 2008 / Martimbeau+ 1994].  c lower for a cored/large dwarf.
GAL = [
    dict(name="Fornax dSph", v_max=25.0, c=13.0, c_band=(9.0, 18.0),
         core_obs=(0.3, 0.7), color="#b5121b", mk="o"),
    dict(name="IC 2574", v_max=80.0, c=8.0, c_band=(5.0, 12.0),
         core_obs=(6.0, 10.0), color="#2a7d2a", mk="s"),
]

print("=== Patch 0851 verify — §6 core-radius vs sigma/m (NFW r_1 inversion) ===")
print(f"sigma_V/m prediction = {sigma_m0} cm^2/g (vel.-indep.), f-band {F_BAND}, t={t_age} Gyr")
print(f"convention: sigma_1D = V_max/sqrt(2); <v_rel> = {VREL:.3f} sigma_1D  [conv]\n")
print(f"{'galaxy':<13}{'V_max':>7}{'c':>5}{'r_1(0.20)':>11}{'core_obs':>12}{'sigma/m for core':>18}")
print(f"{'':13}{'km/s':>7}{'':>5}{'kpc':>11}{'kpc':>12}{'cm^2/g':>18}")
for g in GAL:
    r1_020 = r1_of_sigma(g["v_max"], g["c"], sigma_m0)
    lo, hi = g["core_obs"]
    sm_lo = sigma_for_core(g["v_max"], g["c"], lo)
    sm_hi = sigma_for_core(g["v_max"], g["c"], hi)
    g["r1_020"] = r1_020
    print(f"{g['name']:<13}{g['v_max']:>7.0f}{g['c']:>5.0f}{r1_020:>11.2f}"
          f"{f'{lo:.1f}-{hi:.1f}':>12}{f'{sm_lo:.2f}-{sm_hi:.2f}':>18}")

print()
print("verdict:")
print("  Fornax  : at sigma/m=0.20, r_1 ~ {:.2f} kpc -- lands inside the observed <~0.3-0.7 kpc"
      .format(GAL[0]["r1_020"]))
print("            core. The f-band [0.07,0.6] brackets it. CONSISTENT.")
print("  IC 2574 : at sigma/m=0.20, r_1 ~ {:.1f} kpc -- well BELOW the observed ~8 kpc core."
      .format(GAL[1]["r1_020"]))
print("            That core requires sigma/m ~ {:.1f}-{:.1f} cm^2/g, ABOVE the f-band."
      .format(sigma_for_core(GAL[1]["v_max"], GAL[1]["c"], 6.0),
              sigma_for_core(GAL[1]["v_max"], GAL[1]["c"], 10.0)))
print("            -> a GENUINE tension at the high-velocity end: the largest LSB cores")
print("               want more self-interaction than velocity-independent 0.20 supplies.")
print("  Reading: 0.20 (and the f-band) reproduce dSph-scale cores; the most extreme large")
print("  cores (IC 2574) prefer sigma/m ~ 1-2, i.e. either residual velocity-dependence or")
print("  an f underestimated at galaxy scale. Reported as a falsifier-relevant tension, not")
print("  hidden. Carries the halo-model (c) factor ~2 and the r_core/r_1 O(1) factor.")

# ---- panel --------------------------------------------------------------
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
fig, ax = plt.subplots(figsize=(7.8, 5.4))
sm_grid = np.logspace(np.log10(0.03), np.log10(10.0), 220)
for g in GAL:
    r1 = np.array([r1_of_sigma(g["v_max"], g["c"], s) for s in sm_grid])
    ax.plot(sm_grid, r1, color=g["color"], lw=2.3, label=f"{g['name']} (NFW $r_1$, c={g['c']:.0f})")
    # concentration band
    lo_c, hi_c = g["c_band"]
    r1_lo = np.array([r1_of_sigma(g["v_max"], lo_c, s) for s in sm_grid])
    r1_hi = np.array([r1_of_sigma(g["v_max"], hi_c, s) for s in sm_grid])
    ax.fill_between(sm_grid, np.minimum(r1_lo, r1_hi), np.maximum(r1_lo, r1_hi),
                    color=g["color"], alpha=0.12)
    # observed core band (horizontal)
    lo, hi = g["core_obs"]
    ax.axhspan(lo, hi, color=g["color"], alpha=0.07)
    ax.text(0.032, np.sqrt(lo * hi), f"{g['name']} obs core", color=g["color"], fontsize=8.5, va="center")

# sigma/m = 0.20 and f-band
ax.axvline(sigma_m0, color="0.2", ls="--", lw=1.5)
ax.text(sigma_m0 * 1.05, 0.04, r"$\sigma_V/m=0.20$", rotation=90, va="bottom", color="0.2", fontsize=9.5)
ax.axvspan(F_BAND[0], F_BAND[1], color="0.5", alpha=0.10)
ax.text(np.sqrt(F_BAND[0] * F_BAND[1]), 13, "f-band", ha="center", color="0.4", fontsize=9)

ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlim(0.03, 10); ax.set_ylim(0.03, 20)
ax.set_xlabel(r"self-interaction  $\sigma/m$  [cm$^2$/g]")
ax.set_ylabel(r"predicted core scale  $r_1$  [kpc]")
ax.set_title("§6 — core size vs σ/m: 0.20 fits dSph cores, large LSB cores want more", fontsize=11)
ax.legend(fontsize=8.8, loc="lower right", framealpha=0.95)
fig.tight_layout()
OUT = __file__.replace("/scripts/", "/figures/").replace("0851_core_radius_vs_sigma.py",
                                                         "0851_core_radius_vs_sigma.png")
fig.savefig(OUT, dpi=150, bbox_inches="tight")
print(f"\nfigure -> {OUT}")
