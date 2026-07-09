#!/usr/bin/env python3
"""Patch 2365 -- STAGE 1 of the F-DM3-4 rate computation:
overburden ceilings + visibility window at m_dimer = 2.8 GeV.

Model-independent CSDA (continuous slowing-down) estimator, pre-registered
conventions (hurting-direction where a choice exists):
  - Coherent SI scaling sigma_A = sigma_n * A^2 * (mu_A/mu_n)^2
    [hurting for visibility: maximizes stopping, LOWERS ceilings]
  - Mean fractional KE loss per scatter f = 2 m m_A/(m+m_A)^2 (isotropic CM)
  - Ceiling: sigma_n such that E_surface degrades to the minimum energy able
    to deposit E_th on the target: E_min = E_th (m+m_T)^2 / (4 m m_T)
  - CSDA estimator, order-of-magnitude class (Emken-Kouvaris showed CSDA can
    misestimate vs MC transport at O(1); registered residual, Stage-2 item)
Verify: (1) ceiling ~ 1/column monotonicity; (2) atmosphere-only ceiling in
the published 1e-28-class order (Mahdawi-Farrar surface analyses); (3) window
non-emptiness robust to +/-2 decades of floor placement.
"""
import json, math

GeV = 1.0
m_u = 0.9315 * GeV            # atomic mass unit
m_chi = 2.8 * GeV             # dimer mass (2 m_el, record: DM-3 F-DM3-4)
m_n   = 0.9383 * GeV          # nucleon
c_kms = 2.998e5

def mu(a, b): return a*b/(a+b)

# ---- media (column densities, g/cm^2) ----
ATM = 1013.0                  # full vertical atmosphere
sites = {                     # site: (rock column g/cm^2 [excl. atm], note)
  "surface (atm only)":            (0.0,     "CRESST-surface / nu-cleus class"),
  "MINOS-class (225 mwe)":         (2.25e4,  "SENSEI early-run class"),
  "LSM Modane (4800 mwe)":         (4.80e5,  "DAMIC-M class"),
  "SNOLAB (6010 mwe)":             (6.01e5,  "SuperCDMS / SENSEI-SNOLAB class"),
}
media = {"atm": (14.5,), "rock": (22.0,)}   # mean A; standard rock A=22

def stopping_sum(rock_col):
    """Sum_i N_i * A_i^2 * (mu_Ai/mu_n)^2 * f_i   (per unit sigma_n)"""
    tot = 0.0
    for col, (A,) in ((ATM, media["atm"]), (rock_col, media["rock"])):
        if col <= 0: continue
        m_A = A * m_u
        N   = col / (A * 1.6605e-24)                    # nuclei / cm^2
        coh = A**2 * (mu(m_chi, m_A)/mu(m_chi, m_n))**2
        f   = 2*m_chi*m_A/(m_chi+m_A)**2
        tot += N * coh * f
    return tot

def E_kin(v_kms):  # eV
    return 0.5 * m_chi*1e9 * (v_kms/c_kms)**2

# ---- brackets (fixed pre-run) ----
v0_bracket   = [220.0, 340.0, 540.0]        # incoming speed km/s (SHM mean..esc+earth)
Eth_bracket  = [10.0, 100.0, 1000.0]        # eV nuclear-recoil threshold class
m_T_Si       = 28*0.9315                    # Si target

results = {"m_chi_GeV": 2.8, "convention": "CSDA, coherent-SI (hurting), Si target",
           "sites": {}}
for site,(rock,note) in sites.items():
    S = stopping_sum(rock)
    grid = {}
    for v0 in v0_bracket:
        for Eth in Eth_bracket:
            E0 = E_kin(v0)
            Emin = Eth * (m_chi+m_T_Si)**2 / (4*m_chi*m_T_Si)
            if E0 <= Emin: sig = 0.0       # unreachable regardless of sigma
            else:          sig = math.log(E0/Emin) / S
            grid[f"v0={v0:.0f},Eth={Eth:.0f}eV"] = sig
    vals = [v for v in grid.values() if v > 0]
    results["sites"][site] = {
        "note": note, "rock_column_g_cm2": rock,
        "ceiling_sigma_n_cm2": grid,
        "ceiling_central": grid.get("v0=340,Eth=100eV"),
        "ceiling_range": [min(vals) if vals else 0.0, max(vals) if vals else 0.0]}

# ---- floors: published-class SI reach at ~3 GeV (bracketed; Stage-2 pins exact curves) ----
floor_bracket = [1e-42, 1e-38]
results["floor_class_cm2"] = floor_bracket
results["floor_note"] = ("CRESST-III/DarkSide-50/Migdal-class order at ~3 GeV; "
                         "bracketed 4 decades wide -- window verdict must be robust to this")

# ---- verify ----
cs = [results["sites"][s]["ceiling_central"] for s in sites]
v1 = all(cs[i] > cs[i+1] for i in range(len(cs)-1))            # monotone in depth
v2 = 1e-29 < cs[0] < 1e-27                                     # surface ceiling published-order
deepest = results["sites"]["SNOLAB (6010 mwe)"]["ceiling_range"][0]
v3 = deepest / floor_bracket[1] > 1e2                          # window >=2 decades at WORST floor
results["verify"] = {"1_monotone_in_depth": v1,
                     "2_surface_ceiling_published_order": v2,
                     "3_window_robust_2decades_worst_case": v3,
                     "passed": f"{sum([v1,v2,v3])}/3"}

# ---- window statement ----
results["window"] = {s: [floor_bracket[1], results["sites"][s]["ceiling_range"][0]]
                     for s in sites if results["sites"][s]["ceiling_range"][0] > floor_bracket[1]}

with open("2365_results.json","w") as f: json.dump(results, f, indent=1)
print(f"m_chi = 2.8 GeV   (coherent-SI hurting convention, Si target)")
for s in sites:
    r = results["sites"][s]
    print(f"{s:28s} ceiling(central) = {r['ceiling_central']:.2e} cm^2   range [{r['ceiling_range'][0]:.1e}, {r['ceiling_range'][1]:.1e}]")
print(f"floor class [1e-42, 1e-38] cm^2")
print(f"verify: {results['verify']}")
