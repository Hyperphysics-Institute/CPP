#!/usr/bin/env python3
"""
Patch 0850 — DM-1 §6: confront the velocity-independent sigma_V/m ~ 0.20 cm^2/g
prediction against TWO specific, well-measured galaxies at very different
velocity scales:
    - Fornax dSph   (dispersion-supported, sigma_1D ~ 11 km/s)   [classical dSph]
    - IC 2574       (rotation-supported,  v_max ~ 80 km/s)       [large-core LSB/dwarf]

§6 machinery (already [FILLED] in the draft): a self-interaction forms a core of
central density ~ rho_1, the "one-scatter" density at which one scatter happens
over the halo age:
        rho_1(v) = 1 / [ (sigma_V/m) * <v_rel> * t ]
A core develops where the halo density would exceed rho_1; the cored central
density saturates at ~ rho_1. So the falsifiable test is: does rho_1 at each
galaxy's velocity scale match its OBSERVED central dark-matter density?

This doubles as the verify script (prints the table + an honest verdict).

Provenance tags:
  [obs]  observed value (source in comment)
  [conv] velocity convention: <v_rel> = (4/sqrt(pi)) * sigma_1D ~ 2.26 sigma_1D
         (Maxwellian mean relative speed); for the rotation-supported galaxy
         sigma_1D ~ v_max/sqrt(2). Carries a factor ~2 convention sensitivity.
  [s4]   the prediction under test: sigma_V/m from §5 (=0.20 cm^2/g)
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- units --------------------------------------------------------------
Msun_g   = 1.989e33
pc_cm    = 3.086e18
Msun_pc3 = Msun_g / pc_cm**3          # = 6.77e-23 g/cm^3
Gyr_s    = 3.156e16
kms_cm   = 1.0e5

# ---- the prediction under test ------------------------------------------
sigma_m = 0.20      # cm^2/g  velocity-INDEPENDENT self-interaction (§5)     [s4]
t_age   = 10.0      # Gyr                                                     [obs]
VREL    = 4.0 / np.sqrt(np.pi)        # <v_rel> / sigma_1D  ~ 2.26          [conv]


def rho1(sigma_1D_kms, sm=sigma_m, t=t_age):
    """One-scatter (core) density in M_sun/pc^3 for a 1D dispersion in km/s."""
    vrel = VREL * sigma_1D_kms * kms_cm           # cm/s
    rho_gcc = 1.0 / (sm * vrel * (t * Gyr_s))     # g/cm^3
    return rho_gcc / Msun_pc3


# ---- the two galaxies ---------------------------------------------------
# Fornax dSph:
#   sigma_1D ~ 11 km/s         [obs: Walker+; central sigma ~10-11.7 km/s]
#   central DM density 0.016-0.07 M_sun/pc^3
#     [obs: Mateo+ 0.07+/-0.03 (isotropic); Jardel & Gebhardt 2012 cored 0.016]
#   core radius <~ 0.3-0.7 kpc [obs: Goerdt+ 2006 upper limits; >1 kpc implausible]
# IC 2574:
#   v_max ~ 80 km/s            [obs: Oh+ 2008/2011 THINGS]
#   pseudo-isothermal core: rho_0 ~ 0.006 M_sun/pc^3, R_C ~ 8 kpc
#     [obs: de Blok+ 2008 / Martimbeau+ 1994]
GAL = [
    dict(name="Fornax dSph", kind="dSph (dispersion)", sig1D=11.0,
         rho_obs=(0.016, 0.07), rcore_obs="<~0.3-0.7 kpc"),
    dict(name="IC 2574", kind="LSB/dwarf (rotation)", sig1D=80.0 / np.sqrt(2.0),
         rho_obs=(0.006, 0.006), rcore_obs="~8 kpc"),
]

print("=== Patch 0850 verify — §6 specific-dwarf confrontation ===")
print(f"prediction under test: sigma_V/m = {sigma_m} cm^2/g (velocity-INDEPENDENT), t = {t_age} Gyr")
print(f"convention: <v_rel> = {VREL:.2f} * sigma_1D  [conv, factor ~2 sensitivity]\n")
print(f"{'galaxy':<14}{'sigma_1D':>9}{'<v_rel>':>9}{'rho_1 pred':>12}{'rho_obs':>16}{'pred/obs':>10}")
print(f"{'':14}{'km/s':>9}{'km/s':>9}{'Msun/pc^3':>12}{'Msun/pc^3':>16}{'':>10}")
for g in GAL:
    r1 = rho1(g["sig1D"])
    vrel = VREL * g["sig1D"]
    lo, hi = g["rho_obs"]
    mid = np.sqrt(lo * hi)
    ratio = r1 / mid
    obs_str = f"{lo:.3f}-{hi:.3f}" if lo != hi else f"{lo:.3f}"
    print(f"{g['name']:<14}{g['sig1D']:>9.1f}{vrel:>9.1f}{r1:>12.3f}{obs_str:>16}{ratio:>9.1f}x")
    g["rho1"] = r1

print()
print("verdict:")
print("  Both galaxies: rho_1(0.20) sits a SIMILAR factor (~3x) above the observed central")
print("  density -- 2.8x at Fornax (sigma_1D=11) and 3.1x at IC 2574 (sigma_1D=57). Two reads,")
print("  both honest:")
print("   (1) velocity-INDEPENDENCE is supported: the offset is ~flat across a 5x span in")
print("       sigma_1D. A velocity-DEPENDENT sigma/m (rising toward dwarfs) would instead")
print("       give a Fornax offset much larger than the IC 2574 offset -- not seen.")
print("   (2) the common ~3x is within the factor-few (f x halo-model) uncertainty; if real")
print("       it mildly favors a normalization a bit below the nominal 0.20 line (cores a")
print("       touch more developed than the bare one-scatter estimate), still vel.-flat.")
print("  Cores DO form in both (rho_obs < rho_1 in both) -- consistent with observed cores.")
print("  Caveat: this is the DENSITY test (what rho_1 gives directly). A full core-RADIUS")
print("  confrontation -- esp. IC 2574's large ~8 kpc core -- needs the NFW r_1 inversion,")
print("  deferred to the core-radius-vs-sigma/m panel. Net: the velocity-INDEPENDENT 0.20")
print("  prediction passes a 5x-velocity-baseline density test at the factor-few level, and")
print("  the flatness is the distinctive, falsifiable signature vs velocity-dependent SIDM.")

# ---- figure: velocity-independent prediction vs the two galaxies --------
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
fig, ax = plt.subplots(figsize=(7.4, 5.0))
vv = np.logspace(np.log10(6), np.log10(120), 200)      # sigma_1D range, km/s
ax.plot(vv, rho1(vv), color="#1b3a6b", lw=2.3,
        label=r"predicted core density $\rho_1(\sigma_{1D})$, $\sigma_V/m=0.20$ (vel.-indep.)")
ax.fill_between(vv, rho1(vv, sm=0.20 / 3), rho1(vv, sm=0.20 * 3),
                color="#1b3a6b", alpha=0.10, label=r"$f$ band ($\sigma_V/m \in [0.07,0.6]$)")
mk = {"Fornax dSph": ("o", "#b5121b"), "IC 2574": ("s", "#2a7d2a")}
for g in GAL:
    m, c = mk[g["name"]]
    lo, hi = g["rho_obs"]
    mid = np.sqrt(lo * hi)
    ax.plot([g["sig1D"]], [mid], m, color=c, ms=10, zorder=5,
            label=f"{g['name']} (obs central $\\rho$)")
    if lo != hi:
        ax.plot([g["sig1D"], g["sig1D"]], [lo, hi], color=c, lw=2.2, zorder=4)
    ax.annotate(g["name"], xy=(g["sig1D"], mid), xytext=(g["sig1D"] * 1.08, mid * 1.7),
                color=c, fontsize=10)
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel(r"velocity dispersion  $\sigma_{1D}$  [km/s]")
ax.set_ylabel(r"central DM density  [$M_\odot\,\mathrm{pc}^{-3}$]")
ax.set_title("§6 — velocity-independent core prediction vs two specific galaxies", fontsize=11.5)
ax.legend(fontsize=8.6, loc="upper right", framealpha=0.95)
ax.text(7, 2.5e-3,
        "both sit a similar factor (~3×) below the line\n"
        "→ flat across 5× in σ → supports velocity-independence\n"
        "(offset within the f × halo-model band)",
        fontsize=8.8, color="0.25")
fig.tight_layout()
OUT = __file__.replace("/scripts/", "/figures/").replace("0850_specific_dwarf_fit.py",
                                                         "0850_specific_dwarf_fit.png")
fig.savefig(OUT, dpi=150, bbox_inches="tight")
print(f"\nfigure -> {OUT}")
