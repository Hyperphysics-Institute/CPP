#!/usr/bin/env python3
"""4192 — the mixing pull from a COHERENTLY POLARISED body, against the 4170 caps.

Mechanism computed on (Patch 4184, from the founder's relay correction; linearity from 4186/GR-1j):
    register at a GP  =  self-term (cut off at one grid spacing a)  +  sum_j  s_j * (a / r_j)
    stamp             =  normalise(own A + register)
so the per-Moment pull toward the environment is   pull = a * | sum_j s_hat_j / r_j |.
4184 compared ONE nearest spin (a/r) with 4170's cap. 4170's caps were set in POLARISED MEDIA,
where theta = (eps*P)*n; the quantity to compare with `pull` is therefore eps*P, not eps.
Linearity (4186) forces N aligned spins to add as N, not sqrt(N).
"""
import math
l_P, t_P = 1.616e-35, 5.391e-44
a = l_P / 1e30                                   # grid spacing (c01; founder correction 0733)
n_Fe = 7.87e3 / 55.85e-3 * 6.022e23              # iron atoms per m^3
s_Fe = 2.2 * n_Fe                                # net aligned electron spins per m^3 (saturated)

caps = {                                         # 4170 section 2:  eps_cap, P  ->  eps*P
    'nuclear spin in a ferromagnet': (1.1e-45, 0.5),
    'muon g-2 storage ring':         (5.4e-47, 0.01),
}
def inside_sphere(L):  return a * 2 * math.pi * s_Fe * L**2      # integral of s/r over a ball, at centre
def lump(mass_kg, r):  return a * (mass_kg / 7.87e3 * s_Fe) / r  # a magnetised lump at distance r

rows = [
  ('single spin at 1 fm (what 4184 checked)',           a / 1e-15,           'muon g-2 storage ring'),
  ('nuclear spin at centre of a 5 mm iron domain-ball', inside_sphere(5e-3), 'nuclear spin in a ferromagnet'),
  ('1 g of magnetised iron at 1 m',                     lump(1e-3, 1.0),     'muon g-2 storage ring'),
  ('1 kg of magnetised iron at 0.5 m',                  lump(1.0, 0.5),      'muon g-2 storage ring'),
  ('g-2 yoke, 680 t at ~1 m, 99.9% cancelled by geometry', 1e-3 * lump(6.8e5, 1.0), 'muon g-2 storage ring'),
]
print(f"a = {a:.3e} m   aligned spins in iron = {s_Fe:.2e} /m^3\n")
print(f"{'source':58s} {'pull/Moment':>12s} {'cap eps*P':>10s} {'pull/cap':>9s} {'align time':>11s}")
for name, pull, c in rows:
    e, P = caps[c]; cap = e * P
    print(f"{name:58s} {pull:12.2e} {cap:10.1e} {pull/cap:9.1e} {t_P/pull:9.1e} s")
