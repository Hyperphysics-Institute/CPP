#!/usr/bin/env python3
"""Patch 2541 verify -- OPEN-DM-RODCLOSE-1 pre-registration structural checks (no derivation).

  1. Closure geometry: theta_L = 2*pi/L; R(L) = L*D/(2*pi); at L=16, D=1.15 fm: theta = 22.5 deg,
     R ~= 2.93 fm. (Stated for later comparison; not consumed as input.)
  2. Harmonic bend scaling: E_bend(L) = L * (1/2) * kappa * (2*pi/L)**2 = 2*pi**2*kappa/L --
     monotonically decreasing in L (symbolic derivative < 0) -> two-sided window structurally
     entailed when combined with growing end inertia (founder Q5 picture consistency).
  3. Mass echoes from pinned inertias: plane = 4*132+4*44 = 704 MeV; element = 1408; L=16 ring =
     11.264 GeV (consistency echo, consumed not derived).
  4. Blindness-protocol documentation check: N=16 absent from the closed input list (inputs are
     geometry/stiffness-lineage/depth-band/inertias/kT; L symbolic).
  5. Fence: no sqrt(5) in any quantity defined here (theta, R, E_bend shape are rational/pi algebra).
"""
import sympy as sp

ok = True
def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and cond

L, kappa = sp.symbols('L kappa', positive=True)
D = 1.15

theta = 2 * sp.pi / L
R = L * D / (2 * sp.pi)
check("theta(16) = 22.5 deg", abs(float(theta.subs(L, 16)) - sp.pi/8) < 1e-12)
check("R(16) ~= 2.93 fm", abs(float(R.subs(L, 16)) - 2.928) < 0.005)

E_bend = L * sp.Rational(1, 2) * kappa * theta**2
E_bend_simplified = sp.simplify(E_bend)
check("E_bend(L) = 2*pi^2*kappa/L exactly",
      sp.simplify(E_bend_simplified - 2 * sp.pi**2 * kappa / L) == 0)
check("E_bend monotonically decreasing in L (dE/dL < 0 for kappa, L > 0)",
      sp.simplify(sp.diff(E_bend_simplified, L)) == -2 * sp.pi**2 * kappa / L**2)

check("plane mass 4*132+4*44 = 704 MeV; element 1408; L=16 ring 11.264 GeV",
      4*132 + 4*44 == 704 and 2*704 == 1408 and abs(16*704/1000 - 11.264) < 1e-9)

closed_inputs = {"geometry", "bend_stiffness_lineage_2450", "endbond_depth_band",
                 "inertias_2496_2452", "kT_form_16.5keV", "precommitments"}
check("N=16 not in closed input list (blindness protocol)", "N_16" not in closed_inputs)

for expr in (theta, R, E_bend_simplified):
    pass
check("no sqrt(5) in defined quantities", all(
    not expr.has(sp.sqrt(5)) for expr in (theta, R, E_bend_simplified)))

print()
print("ALL CHECKS PASS" if ok else "FAILURES PRESENT")
raise SystemExit(0 if ok else 1)
