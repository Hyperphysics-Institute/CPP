#!/usr/bin/env python3
"""
Patch 0896 -- ROUTE B step 1: reduce the E_bond make-or-break to ONE contact quench factor.
============================================================================================
The 4-model panel (0895) agreed the decisive question is whether the soft-eDP polarizability
is QUENCHED or ENHANCED at contact (a ~ DP size), and that Route B (or an explicit contact-scale
treatment) is the resolver. This is the first disciplined step: NOT the full SSV charge-sum, but
a reduction of the whole make-or-break to a single computable quantity, with the endpoints pinned
and an EXTERNAL (noble-gas) anchor for the part that standard damped-dispersion physics fixes.

  E_ee = Q * E_ee,free,  E_ee,free ~ 41 MeV (free-cloud London at contact, = construction 2),
  Q in [0,1] the net contact suppression. In-window [0.8 keV, 2 MeV] <=> Q <~ 0.05.

  Q factorizes:  Q = Q_damp * Q_stiff
    Q_damp  = net-well-depth / bare-dispersion-at-hard-core  (r-damping + exchange repulsion).
              Noble-gas anchor (Argon): Q_damp ~ 0.5 -- buys only ~2x. NOT a CPP derivation;
              an external sanity bound on what r-space damping alone delivers.
    Q_stiff = alpha_pol(contact)/alpha_pol(free-cloud)  (composite eDP internal stiffness quench).
              UN-COMPUTED. This is the OPEN-FP-SF-2-eta deliverable -- the one remaining number.

NO coupling/scale/fraction is fabricated: Q_stiff is left OPEN; the noble-gas Q_damp is labeled an
external analogy. The result is a reduction + an honest lean, not a closure.

Run: python3 0896_routeb_contact_quench_reduction.py
"""

import numpy as np
# ---- pinned corpus constants (CITED) ----
alpha   = 1/137.035999
phi     = (1+np.sqrt(5))/2
hbarc   = 197.3269804          # MeV*fm
E_eDP   = 88.0; E_qDP = 264.0  # MeV (E_qDP=3E_eDP)
f_color = 0.20
V0_color= f_color*E_qDP        # 52.8 MeV = E_qq
als_c   = 5/(8*phi)            # 0.3863
threea  = 3*alpha
r_c     = 1.0                  # fm, eDP-coat hard core (the contact radius), corpus
WIN=(0.8e-3,2.0)              # MeV

print("="*74)
print("ROUTE B, step 1: the make-or-break reduces to ONE contact quench factor Q")
print("="*74)

# --- the two endpoints already on the table ---
# construction 2 (free-cloud London at contact): f_e = f_color*(3a/a_s)^2*(E_qDP/E_eDP)^6
enh=(E_qDP/E_eDP)**6
f_e_free=f_color*(threea/als_c)**2*enh
E_free=f_e_free*E_eDP                     # MeV ~ construction 2 bare
E_c1  =V0_color*(threea/als_c)**2*1e3     # keV  construction 1 (coupling-ratio)
print(f"\n  construction 2 (free-cloud London @ contact)  E_ee,free = {E_free:.0f} MeV   (OUT of window)")
print(f"  construction 1 (coupling-ratio transfer)      E_ee,1    = {E_c1:.0f} keV    (IN window)")
print(f"  the gap between them is a single factor Q = E_ee/E_ee,free in [0,1]:")

# --- the quench parameterization ---
def Q_for(E_MeV): return E_MeV/E_free
Q_win = (Q_for(WIN[0]), Q_for(WIN[1]))    # Q band that lands E_ee in-window
Q_c1  = Q_for(E_c1/1e3)
print(f"    in-window  E_ee in [0.8 keV, 2 MeV]  <=>  Q in [{Q_win[0]:.1e}, {Q_win[1]:.1e}]")
print(f"    construction 1 (170 keV)             <=>  Q = {Q_c1:.1e}")
print(f"    => the WHOLE make-or-break is now: is Q <~ {Q_win[1]:.2f} (window top)?  Q~1 => falsification.")

# --- what standard damped-dispersion physics delivers (EXTERNAL anchor, not a CPP derivation) ---
# Noble-gas benchmark: net well depth eps vs bare dispersion at the hard-core radius sigma.
# Argon: eps=12.4 meV; C6=64.3 a.u.; sigma=3.40 A=6.43 a0 -> C6/sigma^6:
C6_Ar=64.3; sigma_Ar=6.43
bare_Ar=(C6_Ar/sigma_Ar**6)*27211.0   # meV  (1 a.u.=27.211 eV)
eps_Ar=12.4
Q_Ar=eps_Ar/bare_Ar
print(f"\n  EXTERNAL ANCHOR (noble-gas damped-dispersion, NOT a CPP derivation):")
print(f"    Argon: eps/(C6/sigma^6) = {eps_Ar:.1f}/{bare_Ar:.1f} meV = {Q_Ar:.2f}")
print(f"    => net well depth is ~{Q_Ar:.1f}x the bare dispersion at the hard core (r-damping+repulsion)")
print(f"    Applying Q_damp ~ {Q_Ar:.1f} to E_ee,free: {Q_Ar*E_free:.0f} MeV  -> STILL OUT of window")
print(f"    r-space damping/repulsion ALONE buys ~2x, not the ~{1/Q_win[1]:.0f}x needed for window top.")

# --- the residual suppression that must come from contact polarizability QUENCH (the CPP unknown) ---
Q_stiff_needed_top = Q_win[1]/Q_Ar       # extra factor beyond r-damping to reach window TOP
Q_stiff_for_c1     = Q_c1/Q_Ar           # extra factor to reach construction 1
print(f"\n  THE REMAINING UNKNOWN = contact polarizability quench Q_stiff (composite internal stiffness):")
print(f"    to reach window TOP (2 MeV):     Q_stiff <~ {Q_stiff_needed_top:.2f}   (~{1/Q_stiff_needed_top:.0f}x beyond r-damping)")
print(f"    to reach construction 1 (170keV): Q_stiff ~  {Q_stiff_for_c1:.3f}  (~{1/Q_stiff_for_c1:.0f}x beyond r-damping)")
print(f"    Q_stiff = alpha_pol(contact)/alpha_pol(free-cloud). This is the OPEN-FP-SF-2-eta deliverable.")

print("\n"+"="*74)
print("HONEST LEAN (face value): r-damping+repulsion alone -> E_ee ~ 20 MeV, OUT of window.")
print("IN-window survives ONLY if composite stiffness quenches the contact polarizability by")
print(f"a further ~{1/Q_stiff_needed_top:.0f}-{1/Q_stiff_for_c1:.0f}x (Q_stiff ~ 0.01-0.1). Plausible (composites ARE stiff,")
print("Review II) but UN-COMPUTED -- it is exactly OPEN-FP-SF-2-eta. So the falsification risk")
print("is MORE live than 0893/0895's 'leaning in-window' implied. Make-or-break = pin Q_stiff.")
print("="*74)
