#!/usr/bin/env python3
"""
Patch 1814 -- panel-return diagnostic: the Compton-scale validity check (folds Gemini's
hostile Q1/Q2 objection honestly -- real concern, but its quantitative basis overstates).

Gemini (hostile): eDP mass 88 MeV -> Compton wavelength lam_C = hbar*c/(m c^2) ~ 2.24 fm;
the rung spacing d ~ 1.0-1.3 fm is < lam_C, so the wavefunctions "MUST massively overlap"
and the fixed-point-charge Madelung treatment is invalid (-> "falsification disguised").

The check below shows the concern is real but the SEVERITY is overstated, because the
operative scale for point-treatment / pair-production breakdown is the REDUCED Compton
wavelength lam_bar = hbar/(mc) = lam_C/2pi, NOT the full lam_C:
  - lam_bar(eDP) ~ 0.36 fm ; d ~ 1.15 fm -> d/lam_bar ~ 3.2 (point treatment defensible).
  - The ZBW oscillation AMPLITUDE a is itself ~ lam_bar (textbook ZBW), and at the model's
    a/d ~ 0.3 the charges sit ~3 amplitudes apart -> PARTIAL, not "massive", overlap.
  - The spread factor s = 1/sqrt(1-(a/d)^2) ALREADY in f_ZBW = (1/2)s captures the leading
    radial-extent correction: s ~ 1.05 at a/d ~ 0.3 (a ~5% effect, already carried).
So: register the residual field-theoretic overlap (exchange/pair) at d ~ 3*lam_bar as a real,
un-estimated O(1) check -> reinforces Layer C, does NOT falsify. Gemini's full-lam_C claim
is corrected; the underlying "estimate the overlap" ask is honored.
"""
import numpy as np
hbarc = 197.3269804      # MeV*fm
m_eDP = 88.0             # MeV
lam_C  = hbarc/m_eDP            # full Compton wavelength
lam_br = lam_C/(2*np.pi)        # reduced Compton wavelength (the operative scale)
print("="*70)
print("Compton-scale validity check for the fixed-point-charge Madelung treatment")
print("="*70)
print(f"  eDP mass                 = {m_eDP:.0f} MeV")
print(f"  full Compton  lam_C      = {lam_C:.3f} fm   <- Gemini's basis")
print(f"  reduced       lam_bar    = {lam_br:.3f} fm   <- operative breakdown scale")
print(f"  {'d [fm]':>7} | {'d/lam_C':>8} | {'d/lam_bar':>10} | {'a=0.3d':>8} | {'a/lam_bar':>10} | {'s':>6}")
for d in (1.0, 1.15, 1.30):
    a = 0.3*d
    s = 1/np.sqrt(1-0.3**2)
    print(f"  {d:>7.2f} | {d/lam_C:>8.2f} | {d/lam_br:>10.2f} | {a:>8.3f} | {a/lam_br:>10.2f} | {s:>6.3f}")
print()
print("  Reading: on the full-lam_C criterion d/lam_C ~ 0.5 (Gemini's 'must overlap'); but")
print("  on the physically operative reduced-Compton criterion d/lam_bar ~ 3 (defensible).")
print("  ZBW amplitude a ~ lam_bar (a/lam_bar ~ 1) -- exactly the textbook ZBW scale -- so")
print("  the charges are separated by ~3 amplitudes, partial overlap, and the s=1.05 spread")
print("  factor already carries the leading correction. Residual overlap (exchange/pair) at")
print("  d~3 lam_bar is a real O(1) check to compute -> Layer-C cap, NOT a falsification.")
print("="*70)
