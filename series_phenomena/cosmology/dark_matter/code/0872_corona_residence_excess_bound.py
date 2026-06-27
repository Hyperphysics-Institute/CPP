#!/usr/bin/env python3
"""
Patch 0872 (Q1 FIX from panel: the corona is NOT 'closed by reasoning' -- it reduces to an
explicit, computable bound on the spine->eDP residual surface potential V_surf. Two channels.)
==========================================================================================
Panel return on the v1.0 memo: Q1 (corona closure) = RESTATE-with-fix, 3 of 4 (ChatGPT, Gemini,
Copilot; Grok confirmed). Correct criticism: 'same chemical potential as bulk -> no accumulation'
does NOT follow unless the spine's residual SURFACE potential well V_surf is bounded. 'No deep
specific bond' (promiscuous ee-edge) != 'zero attractive well'. The reviewers named two thickening
mechanisms; this script makes BOTH explicit and computable, and reports the thresholds honestly.
It does NOT claim closure -- it converts 'closed by reasoning' into 'conditional on a stated bound',
and identifies exactly what SF must deliver.

The single deciding quantity is V_surf/kT: the residual, Sea-screened surface potential an ambient
eDP feels at the cross spine (orientation-averaged over the promiscuous ee/qq/qe/eq apposition).

CHANNEL 1 -- KINETIC TRAPPING (the 'slow Gyr deposition' worry; ChatGPT/Copilot):
  A coat eDP escapes its surface well by thermal activation: tau_res = tau_0 * exp(V_surf/kT).
  It becomes sigma/m-diluting DEAD MASS only if it stays bound over a halo time: tau_res >~ t_halo.
  Threshold:  (V_surf/kT)*_trap = ln(t_halo / tau_0).
  => trapping is AVOIDED unless V_surf exceeds ~ this many kT. With E_bond/kT >= 100 (0865 floor),
     this is a bound of V_surf as a FRACTION of a full hTetra bond.

CHANNEL 2 -- EQUILIBRIUM SURFACE EXCESS (the 'wetting layer' worry; Gemini):
  Even at steady state, a localized excess over uniform bulk gravitates WITH the aggregate:
     m_coat/m_spine = G * (<exp(V_surf/kT)>_orient - 1),
  G = geometric/density prefactor ~ (rho_Sea/rho_spine) * (perimeter * lambda_D / A_spine)  [SF-pending].
  Promiscuous-edge ORIENTATION CANCELLATION (attractive ~ repulsive orientations) makes the bracket
  second-order: <exp(V/kT)>-1 ~ (1/2)<(V/kT)^2> rather than <V/kT>, suppressing thin-coat mass.
  Need G*(<exp>-1) << 1.

HONEST STATUS: Channel 1 gives a robust, computed threshold (~60-93 kT). Channel 2's prefactor G is
SF/substrate-pending (Sea-vs-spine density, screening length). So the corona is BOUNDED and
CONDITIONAL, not closed -- exactly the panel's RESTATE-with-fix, now made explicit.

Run: python3 0872_corona_residence_excess_bound.py
"""
import numpy as np

print("="*86)
print("CORONA BOUND -- Q1 fix: the closure reduces to an explicit bound on V_surf/kT (Patch 0872)")
print("="*86)

# ---------- CHANNEL 1: kinetic trapping threshold ----------
print("\n(1) KINETIC TRAPPING: dilution needs tau_res = tau_0*exp(V/kT) >= t_halo")
t_halo = 10e9 * 3.156e7         # 10 Gyr in seconds
print(f"    t_halo = 10 Gyr = {t_halo:.2e} s;  threshold (V/kT)*_trap = ln(t_halo/tau_0):")
print(f"    {'tau_0 (s)':>12} | {'(V/kT)*_trap':>12} | {'V_surf/E_bond at trap (E_bond/kT=100)':>38}")
for tau0 in (1e-10,1e-15,1e-20,1e-23):
    thr = np.log(t_halo/tau0)
    print(f"    {tau0:>12.0e} | {thr:>12.1f} | {thr/100:>38.2f}")
print("    => over ANY plausible substrate attempt time tau_0, trapping needs V_surf/kT ~ 60-93,")
print("       i.e. V_surf >~ 0.6-0.9 * E_bond. The coat traps (dilutes) ONLY if an ambient eDP binds")
print("       to the spine at ~60-90% of a FULL hTetra bond depth. The promiscuous ee-edge (no deep")
print("       specific bond to a bare eDP) argues V_surf << E_bond -> trapping channel plausibly safe,")
print("       but this is now an EXPLICIT bound (V_surf/E_bond <~ 0.6), not an assertion.")

# ---------- CHANNEL 2: equilibrium surface excess ----------
print("\n(2) EQUILIBRIUM SURFACE EXCESS: m_coat/m_spine = G * (<exp(V/kT)>_orient - 1)")
print("    orientation models for the promiscuous edge (V flips sign across orientations):")
print(f"    {'V_surf/kT':>10} | {'aligned exp-1':>13} | {'half+/half- exp-1':>18} | {'(2nd-order) (1/2)(V/kT)^2':>26}")
for x in (0.1,0.3,1.0,2.0,4.0):
    aligned = np.exp(x)-1
    balanced = 0.5*(np.exp(x)+np.exp(-x))-1          # cosh(x)-1, symmetric +/- orientations
    second = 0.5*x*x
    print(f"    {x:>10.2f} | {aligned:>13.3f} | {balanced:>18.3f} | {second:>26.3f}")
print("    => a PROMISCUOUS edge (balanced +/- orientations) gives cosh(V/kT)-1 ~ (1/2)(V/kT)^2:")
print("       the excess is SECOND-order in V/kT, not first -- orientation cancellation suppresses it.")
print("    geometric/density prefactor G (SF/substrate-pending):")
print(f"    {'rho_Sea/rho_spine':>17} | {'lambda_D/a':>11} | {'G ~ (rho_Sea/rho_spine)*(4 lambda_D/a)':>40}")
for rr in (0.01,0.1,1.0):
    for ld in (0.5,1.0):
        G = rr*(4*ld)
        print(f"    {rr:>17.2f} | {ld:>11.1f} | {G:>40.3f}")
print("    => m_coat/m_spine = G*(cosh(V/kT)-1). For the coat to be subdominant (<<1) one needs e.g.")
print("       G~0.4 (rho_Sea/rho_spine~0.1) and V/kT<~1 -> m_coat/m_spine ~ 0.4*0.54 ~ 0.2 (marginal);")
print("       or rho_Sea/rho_spine<~0.1 AND V/kT<~1 -> safe. The PREFACTOR G (Sea-vs-spine density,")
print("       screening length) is the SF/substrate input the closure now explicitly requires.")

# ---------- the consolidated conditional ----------
print("\n(3) THE CONSOLIDATED BOUND (what replaces 'closed by reasoning')")
print("    The corona is sigma/m-safe iff BOTH:")
print("      (1) V_surf/kT < ~60-90    (no Gyr kinetic trapping) -- robust, computed;")
print("      (2) G*(cosh(V_surf/kT)-1) << 1   (thin equilibrium excess) -- needs SF prefactor G.")
print("    Both are controlled by the SAME residual V_surf/kT. The promiscuous-edge + Sea-screening")
print("    + orientation-cancellation arguments make small V_surf/kT PLAUSIBLE, but the binding")
print("    constraint (2) also needs the Sea-vs-spine density ratio. So the honest status is:")
print("    CONDITIONAL on (V_surf/kT, rho_Sea/rho_spine) -- both SF/substrate-pending -- NOT closed.")

print("\n"+"="*86)
print("CORONA VERDICT (Q1 fix, Layer C -- panel RESTATE-with-fix INCORPORATED, honestly): the §7")
print("closure is downgraded from 'closed by reasoning' to an EXPLICIT CONDITIONAL BOUND. The coat")
print("dilutes sigma/m only via (1) kinetic trapping -- robustly bounded away unless V_surf >~ 0.6 E_bond")
print("(computed threshold ~60-90 kT) -- or (2) a thick equilibrium excess -- second-order in V_surf/kT")
print("by orientation cancellation, but scaled by an SF-pending Sea-vs-spine density prefactor G. The")
print("clean-spine result HOLDS iff V_surf/kT is small (plausible: promiscuous edge, no deep eDP bond,")
print("Sea screening) AND G is modest (rho_Sea/rho_spine not large). Two explicit SF/substrate numbers")
print("now decide it -- V_surf/kT and rho_Sea/rho_spine -- replacing the uncomputed assertion. This")
print("is the panel's requested fix: the corona is BOUNDED and PLAUSIBLE, not CLOSED.")
print("="*86)
