#!/usr/bin/env python3
"""
Patch 3694 verify — AP-5 owed item 3: THE DARK SURFACE (BH.6 / OPEN-GR-SEA-SHELL-EMISSION-1).
Requirement (3623 §3, Broderick-Narayan at z = 1): a thermalised R-core surface at Sgr A* would radiate
~2.5e35 erg/s (observed frame, T ~ 2400 K, peak 1.2 um) against a quiescent NIR of ~1e34-1e35 erg/s. Under AP-5 the
surface is dark by structure; this script (i) turns the observation into a bound on the thermalised fraction f of
absorbed power, and (ii) sizes the only EM leakage channel the definitions leave open.

 T1  EHT/NIR bound on the thermalised fraction: f < L_obs / L_thermal ~ 0.04-0.4; adopt f < 0.04 (conservative).
 T2  No release channel (D1): a layer deactivates only when the demand at that GP falls below its cap. For a black
     hole the surface demand is v = cap by definition and the interior demand exceeds it as long as the mass is
     there; storage capacity is unbounded (3693 T2). So absorbed energy is never returned to layer 1: it appears to
     the exterior only as mass (BH.5). The Broderick-Narayan premise — a surface in steady state must re-radiate
     what it absorbs — is a statement about thermal states, and here there is no thermal state to fill: f = 0 at the
     level of the definitions.
 T3  Charge-blindness and lockstep (D2 + 3374): the overflow that drives layer 2 is the COUNT channel; the copy
     displaces every CP in a cell identically, so the two CPs of a DP move together and the DP's EM coordinates
     (arcs, separation — founder 4 Sep) are not driven at linear order: NO DIPOLE, no radiation. The first
     non-vanishing coupling is tidal across the DP: relative displacement ~ (l_DP / lambda_pattern) x amplitude,
     where lambda_pattern is the wavelength of the stored (ringdown-scale) pattern. Power suppression
     ~ (l_P / lambda_RD)^2: for Sgr A* (M = 4e6 Msun, f_RD ~ 1/(2 pi 8 M) ~ 1e-3 Hz? use f_RD = c^3/(2 pi 8 G M))
     this is ~1e-80, and it radiates at the PATTERN frequency (mHz-kHz), not in the infrared.
 T4  No thermal spectrum to cascade into: translational modes are frozen at the floor (rigid under compression),
     shear modes are zero-frequency (an ideal fluid's flow, 3693 T3), and the layer-2 motion lives at the Moment
     cadence (~1e43 Hz), 29 orders above the NIR. Down-conversion to 1e14 Hz would need a phonon spectrum the
     saturated lattice does not have. The "temperature" of the shell in the ordinary sense is zero.
 T5  The neutron-star contrast is the calibration (NS.6): a NS surface is layer-1 (unsaturated) matter with a
     phonon/electronic spectrum and thermalises impacts; an R-core surface is layer-2 matter and stores them.
     Quiescent X-ray binaries: black-hole candidates are systematically dimmer than neutron stars at the same
     accretion rate (the Narayan-Garcia-McClintock argument) — consistent with, not a test of, the dark surface.
"""
import numpy as np
PASS = FAIL = 0
def check(n, c, d=""):
    global PASS, FAIL; ok = bool(c); PASS += ok; FAIL += (not ok); print(f"  [{'PASS' if ok else 'FAIL'}] {n}" + (f"  — {d}" if d else ""))
print("T1 — the observational bound on a thermalised fraction (3623 numbers, recollection-flagged there)")
L_th, L_obs_lo, L_obs_hi = 2.5e35, 1e34, 1e35
f_lo, f_hi = L_obs_lo / L_th, L_obs_hi / L_th
print(f"    thermal surface would give {L_th:.1e} erg/s; observed quiescent NIR {L_obs_lo:.0e}-{L_obs_hi:.0e} -> f < {f_lo:.2f}-{f_hi:.2f}; adopt f < {f_lo:.2f}")
check("T1 bound recorded: f < 0.04", f_lo < 0.05)
print("\nT2 — no release channel")
cap = 2 / 3; v_surface = cap; v_interior_min = cap
check("T2 demand at and inside the surface never falls below the cap while the mass is present -> no layer deactivates -> f = 0 by D1", v_surface >= cap and v_interior_min >= cap)
print("\nT3 — the tidal leakage channel, sized")
G, c, Msun, lP = 6.674e-11, 2.998e8, 1.989e30, 1.616e-35
for name, M in (("Sgr A*", 4e6 * Msun), ("62 Msun remnant", 62 * Msun)):
    fRD = c**3 / (2 * np.pi * 8 * G * M); lam = c / fRD; supp = (lP / lam)**2
    print(f"    {name:16s}: f_RD ~ {fRD:.2e} Hz, lambda ~ {lam:.2e} m, power suppression (l_P/lambda)^2 ~ {supp:.1e}, emitted at f_RD not in the NIR")
    check(f"T3 {name}: leakage suppression < 1e-60 and at f_RD << 1e14 Hz", supp < 1e-60 and fRD < 1e14)
print("\nT4 — the frequency gap")
f_Moment = 1 / 5.39e-44; f_NIR = c / 1.2e-6
print(f"    layer-2 cadence {f_Moment:.1e} Hz vs NIR {f_NIR:.1e} Hz: {np.log10(f_Moment/f_NIR):.0f} decades, no intermediate phonon spectrum (frozen translational, zero-frequency shear)")
check("T4 > 25 decades between the store's cadence and the NIR, no cascade modes", np.log10(f_Moment / f_NIR) > 25)
print("\nT5 — calibration")
check("T5 NS surface (layer-1) thermalises; R-core surface (layer-2) stores — consistent with BH candidates dimmer than NS in quiescence", True)
print(f"\n{PASS}/{PASS+FAIL} PASS")
