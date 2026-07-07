#!/usr/bin/env python3
"""Patch 2315 -- G2: equivalence-principle sub-item (Gate-1/B1; named at the DM-2 v1.0 panel).

Structure:
  (A) CPP prediction: eta = 0 identically under the one-ledger structure (symbolic identity) --
      m_grav and m_inertial read the SAME ledger (constituents + binding[signed] + field/coat +
      kinetic), and the A3' metric assembly with C5-only coupling (THEO-SR-EIN-4) gives universal
      response. Composition-dependence could enter ONLY through a form-dependent |SSV| conversion
      efficiency (named condition C-d).
  (B) Teeth calibration (counterfactuals): wrong-sign binding and EM-field-energy miscount give
      eta ~ 1e-3 -- excluded by MICROSCOPE/Eot-Wash by 10-12 ORDERS. The one-ledger structure is
      load-bearing, not decorative.
  (C) Derived bound EP-C-1: any form-dependent conversion efficiency eps_form is bounded by
      eps <= |eta|_bound / Delta f_form -- at the 1e-12 level for the EM form. Pre-kills any
      future substrate refinement with form-dependent sourcing above it.
  (D) DM side: the rod's coat is in-ledger (L1, Patch 1895; unledgered residual <= 3.4e-5 of
      m_rod) vs percent-level astrophysical DM-EP constraints -> margin >= ~300.

Composition inputs (standard values, stated in-line):
  B/A [MeV]: Be-9 = 6.4628, Ti-48 = 8.7229, Pt-195 = 7.9266 (AME-class binding per nucleon).
  Coulomb fraction from the SEMF term a_C*Z*(Z-1)/A^(1/3), a_C = 0.711 MeV; u = 931.494 MeV.
Experimental bounds (conservative 2-sigma-scale):
  MICROSCOPE final (Ti,Pt): |eta| < 5e-15   [reported (-1.5 +/- 2.7)e-15]
  Eot-Wash (Be,Ti):        |eta| < 4e-13   [reported (0.3 +/- 1.8)e-13]
"""
import sympy as sp

checks = []

# ---- (A) one-ledger identity --------------------------------------------------------------
mc, B, Ecoat, K = sp.symbols('m_c B E_coat K', positive=True)   # constituents, binding, field, kinetic
ledger = mc - B + Ecoat + K                                      # ONE ledger, binding signed
m_i, m_g = ledger, ledger
eta_cpp = sp.simplify(2*(m_g - m_i)/(m_g + m_i))
checks.append(("CPP one-ledger: eta = 0 identically (all forms, binding signed)", eta_cpp == 0, eta_cpp))

# ---- composition fractions ------------------------------------------------------------------
u, aC = 931.494, 0.711
iso = {"Be9": (4, 9, 6.4628), "Ti48": (22, 48, 8.7229), "Pt195": (78, 195, 7.9266)}
fB, fC = {}, {}
for k, (Z, A, BA) in iso.items():
    fB[k] = BA / u
    fC[k] = aC*Z*(Z-1)/A**(1/3) / (A*u)
ok = all(0.005 < fB[k] < 0.011 for k in iso) and all(1e-4 < fC[k] < 6e-3 for k in iso)
checks.append(("composition fractions in expected ranges", ok,
               {k: (round(fB[k], 6), round(fC[k], 6)) for k in iso}))

MICRO, EOTWASH = 5e-15, 4e-13
dfB_TiPt = abs(fB["Ti48"] - fB["Pt195"]);  dfB_BeTi = abs(fB["Be9"] - fB["Ti48"])
dfC_TiPt = abs(fC["Ti48"] - fC["Pt195"]);  dfC_BeTi = abs(fC["Be9"] - fC["Ti48"])

# ---- (B) counterfactual teeth ----------------------------------------------------------------
eta_wrongsign_TiPt = 2*dfB_TiPt          # m_g = m_c + B instead of m_c - B
eta_wrongsign_BeTi = 2*dfB_BeTi
eta_emmiss_TiPt    = dfC_TiPt            # EM field energy absent from the gravitational ledger
x1 = eta_wrongsign_TiPt / MICRO
x2 = eta_wrongsign_BeTi / EOTWASH
x3 = eta_emmiss_TiPt / MICRO
checks.append((f"wrong-sign binding excluded x{x1:.1e} (MICROSCOPE) / x{x2:.1e} (Eot-Wash)",
               x1 > 1e10 and x2 > 1e9, (eta_wrongsign_TiPt, eta_wrongsign_BeTi)))
checks.append((f"EM-field-energy miscount excluded x{x3:.1e} (MICROSCOPE)",
               x3 > 1e10, eta_emmiss_TiPt))

# ---- (C) derived bound EP-C-1 on form-dependent conversion ----------------------------------
eps_EM   = MICRO / dfC_TiPt
eps_B_mu = MICRO / dfB_TiPt
eps_B_ew = EOTWASH / dfB_BeTi
checks.append((f"EP-C-1: eps_EM <= {eps_EM:.1e}; eps_B <= {eps_B_mu:.1e} (MICRO) / {eps_B_ew:.1e} (EW)",
               eps_EM < 1e-11 and eps_B_mu < 1e-11, (eps_EM, eps_B_mu, eps_B_ew)))

# ---- (D) DM side ------------------------------------------------------------------------------
coat_resid, astro_bound = 3.4e-5, 1e-2   # L1 unledgered residual; percent-level DM-EP constraints
margin = astro_bound / coat_resid
checks.append((f"rod coat in-ledger: worst-case eta_DM <= 3.4e-5 vs ~1e-2 astro bound (margin x{margin:.0f})",
               margin > 100, margin))

npass = 0
for name, ok, val in checks:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  ({val})")
    npass += ok
print(f"{npass}/{len(checks)} PASS")
assert npass == len(checks)
