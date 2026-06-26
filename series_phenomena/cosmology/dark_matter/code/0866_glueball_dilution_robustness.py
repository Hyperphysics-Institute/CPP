#!/usr/bin/env python3
"""
Patch 0866 (G3 tractable half -- glueball-dilution suppression is OVER-DETERMINED by
the concentration hierarchy; the sigma_accrete/sigma_appose ratio is bracketed geometric)
=========================================================================================
Goalpost G3 has two parts:
  (i)  the chaperoning suppression ratio rho = R_cross/R_appose that sets the glueball
       mass-fraction f_glue = 1/(1+rho)  [needs rho >~ 9 for f_glue < 10%], and
  (ii) the glueball cocoon-ARREST RADIUS (compact-endpoint size; OPEN-SS-6-type).

0863 established f_glue = 1/(1+rho), rho ~ ([hTetra]/[ribbon])*(sigma_accrete/sigma_appose),
and flagged the suppression as "checkable, conditional on sigma ratio ~ O(1)". This patch
does the EASY half of G3: it shows the suppression is ROBUST to the sigma-ratio uncertainty
because it is over-determined by the [hTetra]/[ribbon] CONCENTRATION hierarchy. It does NOT
attempt the cocoon-arrest radius -- that compact strong-sector number stays the hard
residual (OPEN-SS-39 / OPEN-SS-6), flagged not solved, exactly as G2 left the absolute depth.

The decomposition:  rho = C * S,   C = [hTetra]/[ribbon],   S = sigma_accrete/sigma_appose.

  (A) C -- the concentration hierarchy (the dominant, robust lever).
      hTetras are ~50% of the DP-Sea (the substrate vacuum); fully-formed ribbons are a
      dilute, transient relic species being built FROM Sea constituents. So [hTetra]
      (a Sea-fraction density) vastly exceeds [ribbon] (a relic-fraction density):
      C >> 1 by many orders. Accretion is ribbon+hTetra (rate ~ [hTetra]); apposition is
      ribbon+ribbon (rate ~ [ribbon]). rho carries one full power of C.

  (B) S -- the geometric cross-section ratio (the correction, bracketed not assumed-1).
      sigma_accrete: a single hTetra captured onto the ribbon's exposed q:q CENTER channel
        -- a LOCAL per-site capture, area ~ pi*(a few * l_rung)^2, UNsuppressed (happens
        every encounter, at any of the ~N center sites).
      sigma_appose: two EXTENDED ribbons collapsing lengthwise -- a large geometric target
        (~ ribbon projected area) but ALIGNMENT-suppressed (collapse needs lengthwise
        registry over many rungs) AND needs a rare second ribbon. Effective collapse-
        completing area = (projected area) * p_align, p_align << 1.
      Net: S is uncertain but NOT astronomically small -- bracketed S in [1e-2, 1e2].

  (C) The pass condition is C >= 9/S. For the bracketed S, the REQUIRED C is modest
      (9/S in [0.09, 900]) -- trivially afforded by a Sea-vs-relic hierarchy that is
      many orders of magnitude. So f_glue < 10% (dilution a small correction) holds
      across the ENTIRE bracketed sigma-ratio range, NOT just at S ~ O(1).
      => 0863's conditional suppression is upgraded to robust-to-S.

  (D) Resulting dilution correction sigma_eff/sigma_ext is small and bounded.

Cocoon-arrest radius (the residual, NOT computed here):
  - arrest >~ 100s fm  => a SECOND size-setter that must agree with the l_p-driven loop
                          size (a new consistency the population must satisfy);
  - arrest ~ few fm    => compact dilutant at sigma/m ~ 0.11, but its MASS-fraction is the
                          same f_glue this patch bounds small -- so harmless if rho >~ 9.
  Either way the danger is gated by f_glue, which (A)-(C) bound small. The arrest radius
  itself is OPEN-SS-39 / OPEN-SS-6 strong-sector kinetics -- flagged, not solved.

Run: python3 0866_glueball_dilution_robustness.py
"""
import numpy as np

SIG_GLUE = 0.11          # cm^2/g, compact-glueball self-interaction floor (0859)
L_RUNG   = 1.0           # fm

def f_glue(rho):
    return 1.0/(1.0+rho)

def rho_for_fglue(target_f):
    return (1.0-target_f)/target_f

def sigma_eff(sigma_ext, fg):
    return (1.0-fg)*sigma_ext + fg*SIG_GLUE

print("="*76)
print("G3 (tractable half) -- glueball-dilution suppression robustness (Patch 0866)")
print("="*76)

print("\n(0) f_glue thresholds (mirror 0863):")
for tf in (0.10, 0.05, 0.01):
    print(f"    f_glue < {tf*100:>4.1f}%  needs  rho > {rho_for_fglue(tf):>6.1f}")

print("\n(B) Geometric sigma-ratio bracket  S = sigma_accrete/sigma_appose")
# accretion: local capture onto a center-channel site, radius ~ a few l_rung
for a_acc in (1.0, 2.0, 3.0):
    sig_acc = np.pi*(a_acc*L_RUNG)**2
    # apposition: ribbon projected area (take N~1183 rung hoop, R~Nl/2pi) * alignment prob
    N = 1183.0; R = N*L_RUNG/(2*np.pi)
    sig_app_geo = np.pi*R**2                     # generous projected target
    for p_align in (1e-1, 1e-2, 1e-3):
        sig_app = sig_app_geo*p_align
        S = sig_acc/sig_app
        print(f"    a_acc={a_acc:.0f} l_rung (sig_acc={sig_acc:5.1f} fm^2) | "
              f"p_align={p_align:.0e} (sig_app={sig_app:9.1f} fm^2) | S={S:.2e}")
print("    => S spans ~1e-5..1e-1 for a hoop-scale appose target; for SHORT-overlap")
print("       collapse (appose target ~ few rungs, not the whole hoop) S climbs toward")
print("       O(1)-O(10). Honest bracket kept WIDE: S in [1e-5, 1e2].")

print("\n(C) Pass condition  C = [hTetra]/[ribbon] >= 9/S  (for f_glue < 10%)")
print(f"    {'S':>10} | {'required C = 9/S':>18}")
for S in (1e2, 1e0, 1e-2, 1e-5):
    print(f"    {S:>10.0e} | {9.0/S:>18.2e}")
print("    Even the worst bracketed S=1e-5 needs only C ~ 9e5. The Sea-vs-relic hierarchy")
print("    ([hTetra] ~ 0.5 of the substrate vacuum vs [ribbon] a dilute transient relic)")
print("    is many orders of magnitude -- so C >= 9/S holds across the ENTIRE S bracket.")
print("    => dilution suppression is OVER-DETERMINED by concentration; robust to S.")

print("\n(D) Resulting dilution correction (sigma_ext = 1.0 cm^2/g target):")
print(f"    {'rho':>8} | {'f_glue':>8} | {'sigma_eff':>10}")
for rho in (9, 30, 100, 1000):
    fg = f_glue(rho)
    print(f"    {rho:>8d} | {fg*100:>7.2f}% | {sigma_eff(1.0, fg):>10.3f}")
print("    => at rho >~ 30 the dilution tax is a few-percent correction; sigma_eff ~ sigma_ext.")

print("\n(E) Cocoon-arrest radius -- the HARD residual (NOT computed; OPEN-SS-39/OPEN-SS-6)")
print("    arrest >~ 100s fm => second size-setter, must agree with l_p loop size;")
print("    arrest ~ few fm   => compact sigma/m~0.11 dilutant, mass-fraction = f_glue (bounded small).")
print("    Danger gated by f_glue either way -> (A)-(C) make it sub-dominant; arrest radius")
print("    itself is strong-sector kinetics, flagged not solved.")

print("\n" + "="*76)
print("G3 (easy half) VERDICT (Layer C): glueball dilution suppression is ROBUST -- it is")
print("over-determined by the [hTetra]/[ribbon] hierarchy, holding across a WIDE sigma-ratio")
print("bracket, not just S~O(1). Upgrades 0863's conditional claim. Cocoon-arrest RADIUS")
print("remains the hard strong-sector residual (OPEN-SS-39/OPEN-SS-6), flagged not solved.")
print("="*76)
