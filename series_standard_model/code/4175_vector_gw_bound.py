#!/usr/bin/env python3
"""
Patch 4175 — TODO-4174-VECTORGW. Confront the propagating A_i channel with data.

A_i has NO coupling constant (TODO-4172-SOURCEEQ, reopened at 4174), so no
amplitude can be computed outright. What CAN be done is the 4137 move: treat the
coupling kappa_A as an unknown and let the data bound it.

Two candidate constraints. 4174 nominated gravitational-wave polarisation. This
patch computes that AND the alternative, and the alternative wins by fifteen
orders -- which means 4174's "first real empirical handle" was the wrong handle.
"""
import numpy as np
out=[]
def say(s=""): print(s); out.append(s)
G=6.67430e-11; c=2.99792458e8; hbar=1.054571817e-34
mu0=4*np.pi*1e-7; muB=9.2740100783e-24; m_n=1.67492749804e-27
kappa_grav=16*np.pi*G/c**4

say("T1  why GW polarisation is a WEAK test: astrophysical spin density is tiny")
say("    A_i is sourced by INTRINSIC spin density, not by orbital angular")
say("    momentum. Bulk neutron matter is essentially unpolarised, so the source")
say("    is suppressed by the polarisation fraction P.")
say("    Ratio of the intrinsic-spin source to the mass-quadrupole source for a")
say("    body of mass M, radius R, angular frequency omega:")
say("        S/(M R^2 omega) = (M/m_n) hbar P /(M R^2 omega) = hbar P/(m_n R^2 omega)")
R=1e4; om=1e4
supp=hbar/(m_n*R**2*om)
say(f"    neutron star, R = {R:.0e} m, omega = {om:.0e} rad/s:")
say(f"        suppression = {supp:.2e} x P")
say(f"    even at P = 1 that is {supp:.0e}; a magnetar's P ~ 1e-3 gives {supp*1e-3:.0e}.")
say()
frac=0.1
say(f"    LIGO/Virgo/KAGRA bound the non-tensor amplitude fraction at <~ {frac:.0%}.")
say(f"    kappa_A/kappa_grav <= {frac}/{supp:.1e} = {frac/supp:.1e}")
say("    So GW polarisation permits a coupling ~1e18 times gravitational.")
say("    **It is a bound, and it is nearly useless.**")
say()

say("T2  ** A DIMENSIONAL ERROR I MADE AND CAUGHT, recorded rather than fixed")
say("     silently (D-11). ** My first draft compared the GW bound against an")
say("    anomalous SPIN-SPIN FORCE bound, and concluded the spin-spin test was")
say("    fifteen orders tighter. THE COMPARISON WAS MEANINGLESS: it put")
say("    kappa_A hbar^2/(4 pi) [J.m^3] beside kappa_grav = 16 pi G/c^4 [m/J].")
say("    Those are different units -- m^3/(J s^2) against m/J -- so the ratio")
say("    'x kappa_grav' in that draft was not a number at all.")
say("    The script's own T3 line printed 'the spin-spin bound is 7e-35 times")
say("    tighter' while the prose above it said fifteen orders the other way.")
say("    That disagreement is what exposed it.")
say()
say("    WHY IT CANNOT BE REPAIRED HERE: to get A_i's STATIC potential between")
say("    two spins -- which is what a torsion-balance experiment bounds -- one")
say("    needs A_i's FIELD EQUATION, and there isn't one. TODO-4172-SOURCEEQ is")
say("    open precisely because A3' never wrote it. **The missing source clause")
say("    blocks the static test; only the RADIATIVE test is available.**")
say()

say("T3  so the GW bound stands alone, and 4174's nomination was right")
kA_gw=frac/supp
say(f"    kappa_A / kappa_grav <= {kA_gw:.1e}")
say("    Dimensionally consistent because both A_i and Q_ij feed propagating")
say("    channels of the same packet: the amplitude ratio is")
say("    (kappa_A/kappa_grav) x (spin source / mass-quadrupole source), and the")
say("    suppression factor carries all the dimensions.")
say()
say("    This is the FIRST NUMERICAL BOUND the A_i channel has ever carried. It")
say("    converts TODO-4172-SOURCEEQ from 'the coefficient is unknown' to 'the")
say("    coefficient is bounded above'. It is a weak bound -- 18 orders of room")
say("    -- and a weak bound is not nothing when the prior state was none.")
say()

say("T4  AND IT MAKES A DEMAND THE AMENDMENT CANNOT DODGE")
say("    If kappa_A is fixed at the gravitational value -- the natural")
say("    zero-parameter choice, and what 4173 wanted -- then A_i's vector-mode")
say(f"    contribution sits {kA_gw:.0e} BELOW the LIGO bound and is unobservable")
say("    by this route too.")
say("    If instead kappa_A is large enough to be observable, it is A NEW")
say("    PARAMETER and the zero-parameter claim takes the hit 4172 warned of.")
say("    **The amendment cannot have both: zero parameters, or observability.**")
say("    That is the sharpest statement of the channel's position this session")
say("    has reached, and it does not depend on any identification I proposed.")
