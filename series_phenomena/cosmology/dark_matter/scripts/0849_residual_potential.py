#!/usr/bin/env python3
"""
Patch 0849 — DM-1 §4: the residual interaction V(r) and the
saturation-vs-confinement density comparison (glueball-avoidance).

Generates the §4 [TO FILL] figure AND doubles as a verify script: it prints the
derived well depth / minimum location and the saturation/confinement densities,
confirming they match the §4 prose (V0 ~ 53 MeV at r ~ 1 fm; rho_sat < rho_conf).

Physics (all from §4 of DM-1_draft_manuscript.md; constituent physics cited there
to SF-3 / SF-5):
  Between two color-SINGLET qDPs a single gluon (hDP) cannot be exchanged, so the
  leading residual is a TWO-gluon color van der Waals interaction: a short-range
  attractive well screened at range lambda, sitting outside a hard core set by the
  eDP "coat". We model it with a screened Lennard-Jones form, which reproduces all
  three quoted scales (hard core r_c, screening range lambda, depth V0):

      V(r) = V0 * [ (r_c/r)^12 - 2 (r_c/r)^6 ] * exp(-(r - r_c)/lambda)

  - r -> 0      : (r_c/r)^12 dominates -> V -> +inf            (hard core)
  - r  = r_c    : [1 - 2]*1 = -1       -> V = -V0              (well depth V0)
  - r >> r_c    : -2 V0 (r_c/r)^6 exp(-(r-r_c)/lambda)         (screened vdW tail)

Provenance tags on inputs:
  [s4]  = stated in §4 (color-polarizability estimate / eDP-coat scale)
  [sf3] = quark-sector flagship (m_qDP, constituent scale)        [abshier2026sf3]
  [est] = representative value; the argument needs only the inequality noted
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- §4 inputs ----------------------------------------------------------
r_c    = 1.0     # fm   hard-core radius (eDP coat)                       [s4]
lam    = 1.3     # fm   attractive Yukawa / screening range              [s4]
V0     = 53.0    # MeV  well depth = f * E_qDP, f ~ 0.2                   [s4]
E_qDP  = 264.0   # MeV  qDP constituent energy/mass                      [sf3]
f      = V0 / E_qDP                                                    # ~0.20
# representative constituent scale for the confinement-onset spacing.
# The glueball-avoidance argument requires ONLY r_qDP < r_c; 0.5 fm is a
# representative sub-fermi constituent size, NOT a derived number.
r_qDP  = 0.5     # fm                                                     [est]


def V(r):
    """Screened-LJ residual potential, MeV. r in fm (array-safe)."""
    x = r_c / r
    return V0 * (x**12 - 2.0 * x**6) * np.exp(-(r - r_c) / lam)


def n_density(d):
    """Number density (fm^-3) for inter-particle spacing d (simple-cubic, n=1/d^3)."""
    return 1.0 / d**3


# ---- derived quantities (verify block) ----------------------------------
rr = np.linspace(0.55, 6.0, 20000)
Vr = V(rr)
imin = int(np.argmin(Vr))
r_min, V_min = rr[imin], Vr[imin]

# density comparison: saturation onset at spacing ~ r_c; confinement onset ~ r_qDP
rho_sat  = n_density(r_c)             # fm^-3  (cores touch -> medium stops compressing)
rho_conf = n_density(r_qDP)           # fm^-3  (spacing at which confinement would set in)
ratio    = rho_sat / rho_conf         # = (r_qDP / r_c)^3 < 1

print("=== Patch 0849 verify — §4 residual interaction ===")
print(f"inputs:  r_c = {r_c} fm [s4]   lambda = {lam} fm [s4]   "
      f"V0 = {V0} MeV [s4]   E_qDP = {E_qDP} MeV [sf3]   f = V0/E_qDP = {f:.3f}")
print(f"well:    minimum V = {V_min:.1f} MeV at r = {r_min:.2f} fm "
      f"(target: ~ -{V0:.0f} MeV near r_c = {r_c} fm)")
ok_depth = abs(V_min + V0) < 6.0 and abs(r_min - r_c) < 0.4
print(f"         depth/location consistent with §4: {ok_depth}")
print(f"density: rho_sat(r_c)   = {rho_sat:.3f} fm^-3   (saturation onset)")
print(f"         rho_conf(r_qDP)= {rho_conf:.3f} fm^-3   (confinement onset, r_qDP={r_qDP} fm [est])")
print(f"         rho_sat/rho_conf = {ratio:.3f} = (r_qDP/r_c)^3  -> rho_sat < rho_conf: {rho_sat < rho_conf}")
print("         => the medium saturates BELOW the confinement density => glueball-avoidance holds")
print("         (the conclusion follows for ANY r_qDP < r_c; the value above is representative)")

# ---- figure -------------------------------------------------------------
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.4))

# Panel A: V(r)
rp = np.linspace(0.62, 5.5, 2000)
axL.axhline(0, color="0.7", lw=0.8)
axL.plot(rp, V(rp), color="#1b3a6b", lw=2.2)
axL.set_ylim(-1.6 * V0, 1.8 * V0)
axL.set_xlim(0.6, 5.0)
axL.set_xlabel("separation  r  [fm]")
axL.set_ylabel("V(r)  [MeV]")
axL.set_title("(a)  residual two-gluon color van der Waals potential", fontsize=11)
# annotate the well
axL.plot([r_min], [V_min], "o", color="#b5121b", ms=6)
axL.annotate(f"well depth $V_0 \\approx {V0:.0f}$ MeV\n(min {V_min:.0f} MeV at {r_min:.2f} fm)",
             xy=(r_min, V_min), xytext=(2.0, -1.15 * V0),
             arrowprops=dict(arrowstyle="->", color="#b5121b", lw=1.1), color="#b5121b")
# hard core marker
axL.axvline(r_c, color="0.55", ls=":", lw=1.2)
axL.annotate(f"hard core $r_c \\approx {r_c:.1f}$ fm", xy=(r_c, 0.95 * V0),
             xytext=(1.45, 1.45 * V0), color="0.35", fontsize=9.5,
             arrowprops=dict(arrowstyle="->", color="0.55", lw=1.0))
# screening range bar
axL.annotate("", xy=(r_c + lam, 0.35 * V0), xytext=(r_c, 0.35 * V0),
             arrowprops=dict(arrowstyle="<->", color="#2a7d2a", lw=1.3))
axL.text(r_c + lam / 2, 0.45 * V0, f"$\\lambda \\approx {lam:.1f}$ fm",
         ha="center", color="#2a7d2a", fontsize=10)

# Panel B: saturation-vs-confinement density
dd = np.linspace(0.30, 2.2, 600)
axR.loglog(dd, n_density(dd), color="#1b3a6b", lw=2.2)
axR.set_xlabel("inter-particle spacing  d  [fm]")
axR.set_ylabel(r"number density  $n = 1/d^{3}$  [fm$^{-3}$]")
axR.set_title("(b)  saturation density sits below confinement", fontsize=11)
# confinement region (d < r_qDP): forbidden / would confine
axR.axvspan(0.30, r_qDP, color="#b5121b", alpha=0.12)
# saturated diffuse region (d > r_c): where the medium actually lives
axR.axvspan(r_c, 2.2, color="#2a7d2a", alpha=0.10)
for d0, lab, col in [(r_qDP, f"$r_{{qDP}}\\approx{r_qDP:.1f}$ fm\n(confinement onset)", "#b5121b"),
                     (r_c,   f"$r_c\\approx{r_c:.1f}$ fm\n(saturation onset)", "#2a7d2a")]:
    axR.axvline(d0, color=col, ls="--", lw=1.4)
    axR.plot([d0], [n_density(d0)], "o", color=col, ms=6)
axR.annotate(f"$\\rho_{{sat}}/\\rho_{{conf}}=(r_{{qDP}}/r_c)^3\\approx{ratio:.2f}$",
             xy=(r_c, n_density(r_c)), xytext=(1.15, n_density(r_c) * 4.0),
             color="0.2", fontsize=10,
             arrowprops=dict(arrowstyle="->", color="0.4", lw=1.0))
axR.text(0.34, n_density(0.34) * 0.5, "would confine", color="#b5121b", fontsize=9)
axR.text(1.25, n_density(2.0) * 1.4, "saturated,\ndiffuse", color="#2a7d2a", fontsize=9)

fig.suptitle("DM-1 §4 — the residual interaction of color-neutral qDP/hTetra aggregates",
             fontsize=12, y=1.02)
fig.tight_layout()
OUT = __file__.replace("/scripts/", "/figures/").replace("0849_residual_potential.py",
                                                          "0849_residual_potential.png")
fig.savefig(OUT, dpi=150, bbox_inches="tight")
print(f"figure -> {OUT}")
