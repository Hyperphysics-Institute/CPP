#!/usr/bin/env python3
"""
Patch 0863 (UPDATE -- chaperoning suppresses glueball dilution; hinge potential target)
======================================================================================
Two Thomas updates that change the 0862 picture:

(1) DILUTION DEFANGED by a kinetic competition. A bare 4-wide ribbon can either
    (a) be chaperoned into a 4-wide CROSS by accreting hTetras onto its q:q center
        channel (rate R_cross), or
    (b) appose lengthwise with another ribbon and COLLAPSE to a glueball (rate R_appose).
    hDPs are ~50% of the DP-Sea population {eDP, qDP, hDP-A, hDP-B}, and virtually all
    hDPs become hTetras (zero activation barrier) => [hTetra] is huge, [ribbon] is a
    small transient. So R_cross/R_appose ~ [hTetra]/[ribbon] >> 1: the ribbon is crossed
    BEFORE it can appose. Glueball formation from the apposition channel is suppressed,
    NOT eliminated. Surviving mixture => TWO EXTENDED species: 4-wide CROSS + hTetra LOOP.
    => the 0862 dilution tax is paid down to a few-percent correction (checkable).

(2) hTetra hinge stiffness = "MEDIUM" (Thomas's charge geometry). Free vertices on a
    q:q edge repel (like e:e) when the chain bends, SCREENED by the two opposite charges
    of the bonded pair slightly farther away; pre-tensioned at sub-Planck separation;
    ~90 deg swing before non-hinge vertices superimpose; repulsed BOTH ways (a genuine
    restoring well). Two config types bracket it: 2-repulsive-1-attractive (stiffer)
    vs 2-attractive-1-repulsive (softer). This IS the form of the G1 hinge potential.

This file computes: (1) the glueball fraction vs the rate ratio and the [hTetra]/[ribbon]
threshold for <10% dilution, with the resulting sigma_eff; (2) the angular-spring target
kappa_theta the hinge must deliver to land l_p in [100,700] fm. NOTHING about the SSV
near-cancellation is asserted -- that magnitude is the SF-2/SF-5 substrate calc.

Run: python3 0863_chaperone_suppression_and_hinge_target.py
"""
import numpy as np

L_RUNG_FM = 1.0
LP_LO, LP_HI = 100.0, 700.0
SIG_GLUE = 0.11
SIG_BAND = (0.6, 2.0)

# ----------------------------------------- (1) glueball-suppression kinetics
def f_glue(rho):
    """Glueball mass-fraction = R_appose/(R_cross+R_appose) = 1/(1+rho),
    rho = R_cross/R_appose ~ ([hTetra]/[ribbon]) * (sigma_accrete/sigma_appose)."""
    return 1.0/(1.0+rho)

def rho_for_fglue(target_f):
    """rho needed to push glueball fraction down to target_f."""
    return (1.0-target_f)/target_f

def sigma_eff(sigma_ext, fg):
    return (1.0-fg)*sigma_ext + fg*SIG_GLUE

# ----------------------------------------- (2) hinge angular-spring target
def kappa_theta_over_kT(lp_fm, l_rung=L_RUNG_FM):
    """l_p/l_rung = kappa_theta/kT  =>  required angular spring in kT units."""
    return lp_fm/l_rung

def theta_rms_deg(lp_fm, l_rung=L_RUNG_FM):
    return np.degrees(np.sqrt(2.0*l_rung/lp_fm))   # total (2 DOF), matches 0862

# =====================================================================
if __name__ == "__main__":
    print("="*72)
    print(" PATCH 0863 -- chaperone suppression of glueballs; hinge G1 target")
    print("="*72)

    # (1) suppression ----------------------------------------------------
    print("\n"+"-"*72)
    print(" (1) GLUEBALL SUPPRESSION (cross-conversion vs apposition-collapse)")
    print("-"*72)
    print(f"   glueball fraction f_glue = 1/(1+rho),  rho = R_cross/R_appose")
    print(f"   {'rho':>6s} | {'f_glue':>7s} | sigma_eff at sigma_ext=1.0")
    for rho in [0.5, 1, 3, 9, 30, 99]:
        fg = f_glue(rho)
        print(f"   {rho:6.1f} | {fg:7.3f} | {sigma_eff(1.0,fg):6.3f}")
    print(f"   to hold dilution <10% (f_glue<0.1) need rho > {rho_for_fglue(0.1):.0f}")
    print(f"   to hold dilution < 1% (f_glue<0.01) need rho > {rho_for_fglue(0.01):.0f}")
    print(f"   With sigma_accrete/sigma_appose ~ O(1), rho ~ [hTetra]/[ribbon].")
    print(f"   Thomas: [hTetra] ~ 50% of Sea, [ribbon] small/transient => rho >> 9")
    print(f"   plausibly => f_glue at the few-% level => sigma_eff ~ sigma_ext.")
    print(f"   => 0862 DILUTION TAX defanged to a small correction (rate-checkable,")
    print(f"      NOT asserted: it rides on [hTetra]/[ribbon] and the sigma ratio).")

    print("\n   surviving present-day mixture (Thomas): TWO EXTENDED species")
    print("     * 4-wide CROSS      (stiffest, collapse-resistant)")
    print("     * hTetra CHAIN->LOOP (medium stiffness, see (2))")
    print("   both sigma/m ~ N => no compact dilutant dominating the average.")

    # (2) hinge target ---------------------------------------------------
    print("\n"+"-"*72)
    print(" (2) HINGE ANGULAR-SPRING TARGET for l_p in [100,700] fm")
    print("     l_p/l_rung = kappa_theta/kT  (medium screened-repulsion well)")
    print("-"*72)
    print(f"   {'l_p [fm]':>9s} | {'kappa_theta/kT_form':>19s} | {'theta_rms/hinge':>15s}")
    for lp in [100, 300, 700]:
        print(f"   {lp:9d} | {kappa_theta_over_kT(lp):19.0f} | {theta_rms_deg(lp):13.1f} deg")
    print(f"   => the hinge must deliver kappa_theta ~ 1e2-7e2 * kT_form.")
    print(f"      Relative to covalent-deep (1e3-1e4 kT) that is 'MEDIUM'; relative")
    print(f"      to free (~kT) it is stiff. Thomas's 'medium' maps INTO the window")
    print(f"      rather than over/under-shooting -- encouraging, not confirmed.")
    print(f"   CAVEAT: kappa_theta is a NEAR-CANCELLATION (closer like-charge")
    print(f"      repulsion minus farther opposite-charge screening). Its magnitude")
    print(f"      cannot be eyeballed -- needs the SSV charge-sum at sub-Planck pre-")
    print(f"      tension. The two config types (2rep-1att stiffer / 2att-1rep softer)")
    print(f"      bracket it. The ~90 deg ceiling makes the well anharmonic at large")
    print(f"      bend -> suppresses TIGHT small loops -> pushes population to the")
    print(f"      larger loops the cross-section wants (mildly helpful).")

    print("\n"+"="*72)
    print(" NET (computed, not asserted):")
    print("  * glueball dilution is SUPPRESSED by chaperone-beats-apposition")
    print("    kinetics IF [hTetra]/[ribbon] >~ 9 (Thomas's 50%-Sea hDP argument")
    print("    makes this plausible). Surviving mixture = cross + hTetra loop,")
    print("    both extended => sigma_eff ~ sigma_ext. 0862 tax defanged.")
    print("  * G1 reduces to a NUMBER: kappa_theta ~ 1e2-7e2 kT_form, a screened")
    print("    near-cancellation the SF-2/SF-5 SSV calc must evaluate. 'Medium'")
    print("    is consistent with in-window but the cancellation decides it.")
    print("  * make-or-break reverts to G1+G2 (edge-bond SSV depth+curvature) for")
    print("    the two extended species; G3 dilution downgraded from likely-killer.")
    print("="*72)
