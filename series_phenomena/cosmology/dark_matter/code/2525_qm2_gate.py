#!/usr/bin/env python3
"""Patch 2525: the Q-m2 gate (pre-registered, Patch 2524). SM-A's decisive number.

Question: interior dilation factor of a shell of k bare -qCPs, from REGISTERED physics.
Registered normalization: CPP's SSV_abs machinery DERIVES GR (SR-1/c05, registered claim);
therefore the registered magnitude of clock-rate depression from a shell of total mass M at
radius R is the GR interior value  delta = GM/(R c^2).  (A hypothetical extra loading of
clocks by strong-force signals BEYOND their stress-energy is (i) unregistered and (ii) would
be composition-dependent clock physics of the kind equivalence-principle tests constrain to
~1e-13 at macro scales; the GR-matched normalization is the registered reading.)

Every assumption below is tilted MAXIMALLY IN SM-A's FAVOR:
  - smallest packable radius R = l_unit = 0.589 fm (registered lattice unit);
  - largest k the founder's own equilibrium can hold (Coulomb self-energy vs the E_qq
    window TOP, 170 MeV), then a x1000 grace factor on top.
"""
import math

G = 6.674e-11                 # SI
c2 = 8.988e16
MeV_kg = 1.783e-30
kappa_q = 132.0               # MeV/c^2, pinned 2496
R = 0.589e-15                 # m, l_unit (glossary)
alpha_hbar_c = 1.44           # MeV*fm
q2 = (2.0/3.0)**2

def dilation(k):
    M = k * kappa_q * MeV_kg
    return G * M / (R * c2)

# Founder-equilibrium k bound: Coulomb self-energy <= max strong binding (E_qq window TOP)
E_qq_top = 170.0              # MeV (registry condition 3 window top -- favors SM-A)
R_fm = 0.589
U_C_coeff = 0.5 * q2 * alpha_hbar_c / R_fm      # MeV per k^2
k_eq = E_qq_top / U_C_coeff                      # 0.5*q2*a/R * k^2 = E_top * k  ->  k = E_top/coeff
print(f"equilibrium bound: U_C = {U_C_coeff:.3f} k^2 MeV vs binding <= {E_qq_top} k MeV -> k_max ~ {k_eq:.0f}")

for k, label in [(k_eq, "k_max (equilibrium bound)"), (1e3 * k_eq, "x1000 grace"), (3.4e33, "k needed for delta=1e-6")]:
    d = dilation(k)
    print(f"  k = {k:.3g} ({label}): delta = GM/(Rc^2) = {d:.3e}")

d_eq = dilation(k_eq)
k_needed = 1e-6 / dilation(1)
orders_short = math.log10(k_needed / k_eq)
print(f"even a 1e-6 slow-down needs k = {k_needed:.2e} -- {orders_short:.0f} orders beyond the equilibrium bound")
print(f"(that k in one fm shell: M ~ {k_needed*kappa_q*MeV_kg:.1e} kg; Coulomb self-energy ~ "
      f"{U_C_coeff*k_needed**2:.1e} MeV -- the founder's own equilibrium forbids it)")

assert d_eq < 1e-30
print()
print("Q-m2 READING (pre-registered): the slow-down is NEGLIGIBLE at registered magnitudes")
print("(~1e-37 at the equilibrium bound; >= 28 orders below any relevance threshold under")
print(" maximally favorable assumptions). SM-A (the trap) FAILS its gate.")
print("Pre-registered consequence: SM-B (direct screened capture) is evaluated next, on its")
print("own pre-registered terms. No blending. ALL CHECKS PASS")
