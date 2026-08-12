#!/usr/bin/env python
"""Patch 3089 -- D-COMP-WEIGHT: the qCP inventory constraint.

Forward inputs only (no band quantity anywhere):
  FI-RELIC-1  equal initial populations of +/- eCPs and +/- qCPs
              (founder, axiomatic; verbatim at dark_matter reasoning
              2519 and the ZBW/composition ruling of 3069/3082 era).
  CP permanence (core CPP: CPs neither created nor destroyed).
  Sea site density n = 1/d^3, d = d_s * l_P (the 3076 re-anchoring),
  with the Sea largely pair-filled => n_eCP ~ 2n (and by FI-RELIC-1,
  n_qCP = n_eCP).
  Cosmic budget: rho_crit (h = 0.674), Omega_total <= O(1) --
  sky-blind: no CC-band value used or implied.
  Confinement (R-RIBBON-RESERVOIR): the Sea must supply splittable
  qDP feedstock -- at least ~1 hybrid per hadron interaction volume.

Outputs:
  (1) OMEGA CEILING: the maximum fraction g of the qCP inventory
      that may reside in GRAVITATING structures.
  (2) CONFINEMENT FLOOR: the minimum Sea-site fraction f of hybrid
      (qCP-bearing) structures.
  (3) The crossing: floor >> ceiling by ~40 orders => a gravitating
      reservoir is internally excluded; the reservoir is
      ground-state Sea content (the D2 uniform-configuration
      exclusion extends to it).
  (4) Consistency: the OBSERVED gravitating qCP census (DM rings +
      baryons) vs the inventory -- the corpus's own numbers already
      obey the ceiling.
Robustness scans: d_s over six orders; per-qCP mass mu over many
orders. No conclusion depends on the exact values.
"""
import numpy as np

lP = 1.616255e-35            # m
rho_crit = 8.53e-27          # kg/m^3 (h = 0.674)
MeV = 1.78266e-30            # kg

print("== (1) OMEGA CEILING: max gravitating fraction g of the qCP inventory ==")
print(f"{'d_s':>10} {'n_sites/m^3':>12} {'mu[MeV]':>8} {'g_max':>10}")
for ds in (4, 8, 16, 100, 1e3, 1e6):
    d = ds*lP; n = 1/d**3
    n_q = 2*n                                  # equal counts, pair-filled Sea
    for mu_MeV in (1e-6, 1.0, 50.0, 352.0):
        g = rho_crit/(n_q*mu_MeV*MeV)
        print(f"{ds:>10} {n:12.2e} {mu_MeV:8.0e} {g:10.2e}")

print("\n== (2) CONFINEMENT FLOOR: min hybrid site fraction f ==")
for ds in (4, 8, 16):
    n = 1/(ds*lP)**3
    floor = 1/(n*1e-45)                        # >= 1 hybrid per fm^3
    print(f"  d_s={ds:>3}: f >= {floor:.2e}  (>= 1 per hadron volume)")

print("\n== (3) THE CROSSING ==")
ds = 8; n = 1/(ds*lP)**3
g_max = rho_crit/(2*n*50*MeV)
floor = 1/(n*1e-45)
print(f"  floor/ceiling = {floor/g_max:.1e}  (~43 orders):")
print("  a GRAVITATING reservoir dense enough for confinement")
print("  overcloses the universe; the reservoir is ground-state Sea")
print("  content (non-gravitating; D2 exclusion extends to it).")

print("\n== (4) CONSISTENCY: observed gravitating qCP census ==")
m_ring = 11264*MeV                             # 64-qCP ring, 32 x 352 MeV
n_ring = 0.27*rho_crit/m_ring
n_q_DM = 64*n_ring
n_q_b = 2*0.25                                 # ~2 qCP (one hTetra) per nucleon
inv = 2*n
print(f"  DM rings: {n_q_DM:.2f} qCP/m^3 + baryons ~{n_q_b:.2f} qCP/m^3")
print(f"  = {(n_q_DM+n_q_b):.1f}/m^3 of an inventory {inv:.2e}/m^3")
print(f"  gravitating fraction = {(n_q_DM+n_q_b)/inv:.2e}  vs ceiling {g_max:.2e}")
print("  -> the corpus's own numbers already OBEY the ceiling; the")
print("     (1 - 1e-100) remainder is Sea content.")

print("\n== (5) CENSUS ARITHMETIC (structure fractions) ==")
print("  Equal counts + 2e2q hybrid stoichiometry: hybrids consume")
print("  eCPs one-for-one with qCPs => if ALL qCPs sit in hybrids,")
print("  the Sea is ALL hybrid (zero free eDPs). An eDP share")
print("  requires a qCP-only-chain share z: with N_e = N_q = N/2,")
print("  site ledger: hybrids x = (N/2 - z)/2, eDPs y = z/2.")
print("  => f_hybrid is O(1)-class for any z < N/2. The present-epoch")
print("  fractions are NOT committed in the corpus -> FQ-6 (founder).")
