#!/usr/bin/env python3
"""
Patch 1200 — DM-candidate consistency consolidation: verify script.

Re-derives, from the published Step-1 and Step-3 numbers, the two falsification
margins being consolidated, and runs the *discrimination* test that fixes the
grade of the consolidated result.

This script computes NOTHING new physically. It re-checks the arithmetic of
  - step1_sigma_over_m_SIDM.md   (Patch 0703)
  - step3_coldness.md            (Patch 0706)
and then demonstrates the load-bearing point for the grade call: a generic cold,
collisionless CDM candidate of the same GeV mass scale passes BOTH gates
identically, so neither gate discriminates qDP/hTetra from the CDM field.

Run: python3 1200_consolidation_check.py
"""

import math

# ---- constants (as used in the source docs) -------------------------------
GeV_to_g   = 1.783e-24      # g per GeV/c^2
r0_fm      = 0.26           # Cornell crossover; conservative residual range (c14)
fm2_to_cm2 = 1.0e-26        # 1 fm^2 = 1e-26 cm^2
SIDM_bound = 1.0            # cm^2/g, cluster-scale SIDM ceiling (Bullet Cluster)
warm_keV   = 3.0            # thermal-relic warm-DM lower bound, keV
keV_in_GeV = 1.0e-6

# qDP / hTetra constituent-mass *estimates* (QCD / charm-baryon brackets)
masses_GeV = {"qDP (light bracket)": 0.30, "hTetra (charm frame)": 1.50}

# ---- Gate 1: residual self-interaction sigma/m vs SIDM --------------------
sigma_cm2 = math.pi * r0_fm**2 * fm2_to_cm2     # geometric residual cross-section
print("=== Gate 1: sigma/m vs SIDM (cluster bound ~1 cm^2/g) ===")
print(f"  sigma (geometric) = pi*r0^2 = {sigma_cm2:.3e} cm^2")
gate1 = {}
for name, m in masses_GeV.items():
    som = sigma_cm2 / (m * GeV_to_g)
    margin = SIDM_bound / som
    gate1[name] = som
    status = "PASS" if som < SIDM_bound else "FAIL"
    print(f"  {name:24s}: sigma/m = {som:.2e} cm^2/g  ->  {margin:6.0f}x below bound  [{status}]")
    assert som < SIDM_bound, f"{name} violates SIDM bound"

# ---- Gate 3: coldness via mass vs warm-DM boundary ------------------------
print("\n=== Gate 3: coldness (mass vs ~3 keV thermal-relic warm bound) ===")
gate3 = {}
for name, m in masses_GeV.items():
    ratio = m / (warm_keV * keV_in_GeV)
    gate3[name] = ratio
    status = "COLD" if ratio > 1.0 else "WARM/HOT"
    print(f"  {name:24s}: m / m_warm = {ratio:.1e}x above warm bound  [{status}]")
    assert ratio > 1.0e4, f"{name} not decisively cold"

# ---- The discrimination test (fixes the grade) ----------------------------
# A generic structureless CDM candidate of the same mass + a geometric residual
# cross-section <= the qDP value passes both gates identically. Neither gate
# uses any qDP/hTetra-specific structure (confinement scale, 600-cell geometry,
# DP-pairing); both are necessary-not-sufficient survival tests.
print("\n=== Discrimination test (grade-determining) ===")
generic_m = 1.0  # GeV, a plain WIMP-like CDM placeholder
generic_som = sigma_cm2 / (generic_m * GeV_to_g)
generic_cold = generic_m / (warm_keV * keV_in_GeV)
print(f"  generic {generic_m} GeV CDM: sigma/m = {generic_som:.2e} cm^2/g (PASS), "
      f"coldness = {generic_cold:.1e}x (COLD)")
print("  => Both gates are passed by a generic GeV-scale CDM candidate.")
print("  => Surviving them is necessary, NOT sufficient, for IDENTIFICATION.")
print("  => They do not distinguish qDP/hTetra from the CDM field.")

print("\nRESULT: Step 1 + Step 3 consolidate to a CONSISTENCY-grade result")
print("        (compatible-with, not identifying). Identification-grade would")
print("        require a positive discriminant unique to qDP/hTetra. None is")
print("        supplied by these two gates. Grade call -> Thomas sign-off.")
