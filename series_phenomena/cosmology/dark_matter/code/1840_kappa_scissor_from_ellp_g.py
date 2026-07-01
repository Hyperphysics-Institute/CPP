#!/usr/bin/env python3
"""
Patch 1840 -- cross-lane partial G1b: kappa_scissor from ell_p x g (honest kT_form-units result + flag-back).
============================================================================================================
The SF return handover proposed a DM-side partial G1b: 0861's ell_p in [105,702] fm is (via WLC
ell_p = B/kT_form, B = kappa_bend*ell_rung) an absolute kappa_bend, which x SF's g ~ 0.02 backs out an
absolute kappa_scissor "without waiting on the FP root-blocker." Checking against 0861's actual WLC
assumptions (ell_rung = 1.0 fm; kT_form NOT absolutely pinned -- 0861: "absolute scales need the substrate
thermal history -- SF-input", only kT_form/kT_present >~ 7 fixed) surfaces a subtlety:

  ell_p is an absolute kappa_bend ONLY IN UNITS OF kT_form. Converting to absolute MeV needs kT_form,
  which is the SAME OPEN-FP-SF-2-eta root-blocker. So the route does NOT fully escape the blocker.

What it DOES deliver (two genuine, kT_form-handled results):
 (A) kappa_scissor / kT_form = g * ell_p/ell_rung ~ 2-14  -> the junction hinge is a few-to-~14x the
     formation thermal scale: BOUND and thermally stable, but soft. (Absolute MeV still needs kT_form.)
 (B) kappa_scissor / E_bond -- kT_form CANCELS (both in kT_form units via 0861's E_bond/kT_form ~ 13.8 for
     <N>~10^3) -> a kT_form-FREE ratio: the scissor angular stiffness is a SIZABLE FRACTION of, but does
     NOT exceed, the bond depth. Quantifies "the softer of two STIFF modes, not a fragile joint" against
     the very bond that holds it, and gives a thermal-stability cross-check via the bend-break angle.
"""
import numpy as np
# --- corpus inputs (consumed, not recomputed) ---
g = 0.02                      # SF OPEN-SS-40 (ponderomotive, screened); physical band 0.000-0.025
ell_p_lo, ell_p_hi = 105.0, 702.0   # 0861 (fm)
ell_rung = 1.0                # 0861 L_RUNG_FM (fm)
EbondkT_N1e3 = 2*np.log(1e3)  # 0861: <N> ~ exp(E_bond/2kT_form) -> E_bond/kT_form for <N>~10^3
EbondkT_N28  = 2*np.log(28)   # for the sigma/m mean population <N>~28 (bracketing)

kbend_lo, kbend_hi = ell_p_lo/ell_rung, ell_p_hi/ell_rung   # kappa_bend / kT_form
ks_lo, ks_hi = g*kbend_lo, g*kbend_hi                       # kappa_scissor / kT_form

print("(A) kappa in UNITS OF kT_form (absolute MeV blocked -- needs kT_form = OPEN-FP-SF-2-eta):")
print(f"    kappa_bend/kT_form    = ell_p/ell_rung         ~ {kbend_lo:.0f} - {kbend_hi:.0f}")
print(f"    kappa_scissor/kT_form = g*ell_p/ell_rung       ~ {ks_lo:.1f} - {ks_hi:.1f}")
print(f"    -> junction hinge is ~{ks_lo:.0f}-{ks_hi:.0f}x the formation thermal scale: bound, thermally stable, soft.")

print("\n(B) kappa_scissor / E_bond  (kT_form CANCELS -> kT_form-FREE, absolute ratio):")
for lbl,EbkT in [("<N>~10^3 (loop pop, 0861)",EbondkT_N1e3), ("<N>~28 (sigma/m pop)",EbondkT_N28)]:
    r_lo, r_hi = ks_lo/EbkT, ks_hi/EbkT
    print(f"    E_bond/kT_form={EbkT:.1f} [{lbl:24s}]: kappa_scissor/E_bond ~ {r_lo:.2f} - {r_hi:.2f}")
print("    -> scissor angular stiffness is a SIZABLE FRACTION of, but does NOT exceed, the bond depth.")
print("       (kappa_scissor <~ E_bond: an angular stiffness cannot exceed the bond that provides it -- consistent.)")

print("\n(B-cross-check) bend-break angle: theta_max = sqrt(2 E_bond/kappa_bend), thermal theta_rms~3-8deg (0861):")
for EbkT in (EbondkT_N1e3,):
    th_lo = np.degrees(np.sqrt(2*EbkT/kbend_hi)); th_hi = np.degrees(np.sqrt(2*EbkT/kbend_lo))
    print(f"    theta_max(bend) ~ {th_lo:.0f}-{th_hi:.0f} deg  >> theta_rms 3-8 deg -> ribbon thermally stable (consistent w/ 0861).")

print("\nFLAG BACK TO SF (do NOT edit OPEN-SS-40; DM-side note): the ell_p x g route delivers kappa in kT_form")
print("units + the kT_form-free kappa_scissor/E_bond ratio, NOT an absolute MeV kappa_scissor. The absolute")
print("normalization still needs kT_form -> it does NOT escape OPEN-FP-SF-2-eta (0861: absolute scales = SF-input).")
print("The handover's 'absolute kappa_bend ... without waiting on the FP root-blocker' is absolute only in kT_form")
print("units; the MeV value shares the same blocker as the exact floor and G1b. Partial close stands as (A)+(B).")
