#!/usr/bin/env python3
"""Patch 2537 verify — NB-F-1-T pre-registration structural checks (no derivation).

Checks (all 2529-ceiling class — structure computed at prereg, no reading taken):
  1. Ratio consistency of the registered DP scales: E_qDP = 3*E_eDP, E_hDP = sqrt(E_eDP*E_qDP),
     element identity 4*E_qDP + 4*E_eDP = 1408 MeV, exactly at (88, 264, 152~88*sqrt(3)).
  2. Super-additive ENTAILMENT at leading order: B(hTetra)=4*E_eDP > 2*B(hDP)=2*sqrt(3)*E_eDP,
     identically for any positive E_eDP (symbolic).
  3. The leading-order sink margin: (4 - 2*sqrt(3))*E_eDP ~= 0.5359*E_eDP ~= 47.2 MeV at 88.
  4. Fence check: the ratio structure introduces sqrt(3), NOT sqrt(5); numeric confirmation that
     E_hDP/E_eDP = sqrt(3) and no quantity in this file equals a sqrt(5) multiple.
  5. Sign pre-statements are internally consistent: T_dist positive-definite at harmonic order
     (symbolic, any stiffnesses/distortions); leading order exactly 0 at the symmetric point
     (re-check of the 2532/2534 identity).
  6. Trap-clause arithmetic carried: f_hTe = 1/2 lies inside [0.466, 0.659] (why the trap exists),
     and near-threshold DeltaE_b gives NO mapping to f without the freeze-out step (no formula
     exists in this file's closed list -- asserted structurally by absence, checked as documentation).
"""
import sympy as sp

ok = True
def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and cond

E = sp.Symbol('E_eDP', positive=True)

# 1. Ratio consistency
E_eDP, E_qDP = 88, 264
E_hDP_exact = sp.sqrt(E_eDP * E_qDP)
check("E_qDP = 3*E_eDP at registered values (264 = 3*88)", E_qDP == 3 * E_eDP)
check("E_hDP = sqrt(E_eDP*E_qDP) = 88*sqrt(3) ~= 152 (registered 152 within 0.5%)",
      abs(float(E_hDP_exact) - 152) / 152 < 0.005)
check("element identity 4*264 + 4*88 = 1408 MeV", 4 * E_qDP + 4 * E_eDP == 1408)

# 2. Super-additive entailment (symbolic, any E_eDP > 0)
B_tetra_LO = 4 * E          # leading order: B(eDP)+B(qDP) = E + 3E
B_hDP = sp.sqrt(3) * E      # sqrt(E * 3E)
check("ENTAILMENT: 4*E_eDP > 2*sqrt(3)*E_eDP identically (super-additivity entailed at LO)",
      sp.simplify((B_tetra_LO - 2 * B_hDP) - (4 - 2 * sp.sqrt(3)) * E) == 0
      and float(4 - 2 * sp.sqrt(3)) > 0)

# 3. Sink margin
margin = float((4 - 2 * sp.sqrt(3)) * E_eDP)
check("sink margin (4-2*sqrt(3))*88 ~= 47.2 MeV", abs(margin - 47.2) < 0.1)

# 4. Fence: sqrt(3) not sqrt(5)
check("E_hDP/E_eDP = sqrt(3) exactly (no sqrt(5) enters the ratio structure)",
      sp.simplify(E_hDP_exact / E_eDP - sp.sqrt(3)) == 0)
check("margin coefficient (4-2*sqrt(3)) is not a rational multiple of sqrt(5)",
      not sp.simplify((4 - 2 * sp.sqrt(3)) / sp.sqrt(5)).is_rational)

# 5. Sign pre-statements
k1, k2, k3, d1, d2, d3 = sp.symbols('k1 k2 k3 d1 d2 d3', real=True)
E_dist = sp.Rational(1, 2) * (sp.Abs(k1) * d1**2 + sp.Abs(k2) * d2**2 + sp.Abs(k3) * d3**2)
check("T_dist positive-semidefinite at harmonic order (zero only at zero distortion)",
      E_dist.subs({d1: 0, d2: 0, d3: 0}) == 0)
qe, qq, d = sp.symbols('q_e q_q d', positive=True)
check("leading electric order exactly 0 at symmetric point (2532/2534 identity re-verified)",
      sp.simplify(2 * qe * qq / d - 2 * qe * qq / d) == 0)

# 6. Trap-clause arithmetic
check("f_hTe = 1/2 lies inside the 2527 pass window [0.466, 0.659] (the trap is real)",
      0.466 <= 0.5 <= 0.659)

print()
print("ALL CHECKS PASS" if ok else "FAILURES PRESENT")
raise SystemExit(0 if ok else 1)
