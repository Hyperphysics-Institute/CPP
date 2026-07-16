#!/usr/bin/env python3
"""Patch 2515 verify: OPEN-DM-RELIC-1 campaign-open targets.

Computes, from registered/pinned inputs only:
  (1) the Planck dark-to-baryon density ratio with propagated uncertainty;
  (2) the candidate-(B) mass identities (element = 8*(132+44) MeV; ring = 8 elements);
  (3) target T1: required n_ring/n_b (and per-element, per-qCP equivalents);
  (4) the adverse naive-ADM checks (n_ring=n_b and n_element=n_b both fail);
  (5) the pre-registered branch windows (D-strong, D-weak/K1 boundary).
No derivation is attempted. No free parameters. G7: kappa pinned (132/44), never fit.
"""

import math

# --- Registered / external pins ---------------------------------------------
omega_c_h2, s_omega_c = 0.1200, 0.0012      # Planck 2018 TT,TE,EE+lowE+lensing
omega_b_h2, s_omega_b = 0.02237, 0.00015
m_p = 0.93827                                # GeV (proton; He-binding ~0.8% effect noted, below tolerance)
kappa_q, kappa_e = 132.0, 44.0               # MeV/c^2, pinned Patch 2496 (G7)
n_q_per_element, n_e_per_element = 8, 8      # geometry #3: 2 planes x 2 crosses x (eCP-qCP-qCP-eCP)
elements_per_ring = 8                        # N_planes = 16
m_ring_registered = 11.26                    # GeV, Patch 2383 (DD-ladder-selected)

# --- (1) Planck ratio --------------------------------------------------------
R = omega_c_h2 / omega_b_h2
s_R = R * math.sqrt((s_omega_c/omega_c_h2)**2 + (s_omega_b/omega_b_h2)**2)
print(f"(1) Omega_DM/Omega_b = {R:.4f} +/- {s_R:.4f}")
assert abs(R - 5.364) < 0.01

# --- (2) Mass identities ------------------------------------------------------
m_element = (n_q_per_element*kappa_q + n_e_per_element*kappa_e) / 1000.0   # GeV
m_ring = elements_per_ring * m_element
print(f"(2) element = 8*({kappa_q:.0f}+{kappa_e:.0f}) MeV = {m_element*1000:.0f} MeV; "
      f"ring = 8 x {m_element:.3f} = {m_ring:.3f} GeV (registered {m_ring_registered})")
assert abs(m_element - 1.408) < 1e-9
assert abs(m_ring - 11.264) < 1e-9
assert abs(m_ring - m_ring_registered) / m_ring_registered < 5e-4   # 11.264 vs 11.26 rounding

# --- (3) Target T1 -----------------------------------------------------------
n_ring_over_nb = R * m_p / m_ring
s_target = n_ring_over_nb * (s_R / R)        # mass pins carry no quoted error here
n_elem_over_nb = n_ring_over_nb * elements_per_ring
n_qcp_over_nb = n_ring_over_nb * elements_per_ring * n_q_per_element
print(f"(3) T1: n_ring/n_b = {n_ring_over_nb:.4f} +/- {s_target:.4f}; "
      f"n_element/n_b = {n_elem_over_nb:.3f}; n_qCP(DM)/n_b = {n_qcp_over_nb:.1f}")
assert abs(n_ring_over_nb - 0.4468) < 0.001

# --- (4) Adverse naive-ADM checks ---------------------------------------------
naive_ring = m_ring / m_p          # predicted Omega ratio if n_ring = n_b
naive_elem = m_element / m_p       # predicted Omega ratio if n_element = n_b
print(f"(4) naive n_ring=n_b  -> Omega ratio {naive_ring:.2f} (x{naive_ring/R:.2f} OVER observed)")
print(f"    naive n_elem=n_b  -> Omega ratio {naive_elem:.2f} (x{R/naive_elem:.2f} UNDER observed)")
assert naive_ring/R > 2.2 and R/naive_elem > 3.5   # both fail; counting factor is the campaign's subject

# --- (5) Pre-registered branch windows ----------------------------------------
d_strong = (n_ring_over_nb - 2*s_target, n_ring_over_nb + 2*s_target)
d_weak = (n_ring_over_nb/1.5, n_ring_over_nb*1.5)
print(f"(5) Branch D-strong window: [{d_strong[0]:.3f}, {d_strong[1]:.3f}]")
print(f"    Branch D-weak / K1 boundary: [{d_weak[0]:.2f}, {d_weak[1]:.2f}]")

print("ALL CHECKS PASS — targets registered at campaign open; no derivation attempted.")
