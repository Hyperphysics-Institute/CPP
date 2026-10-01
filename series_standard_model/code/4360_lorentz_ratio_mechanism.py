#!/usr/bin/env python3
"""4360 -- the founder's mechanism for alpha's invariance (founders_voice/4360), made quantitative.
Founder: the same number of DI-bits go to the PSR shell whatever the PSR's size; the GP computes PSR and V_i from the
DI-bits; alpha is a ratio, so every frame measures the same.
Model: under the registered relay (4355) a fixed-count source's signal at a GP, at fixed distance in PSRs, scales as
1/(GPs per PSR volume) ~ (a/R)^3.  A CP that responds to its GP's signal RELATIVE to the GP's SSV_abs (a ratio) sees
V/SSV_abs.  That ratio is invariant iff SSV_abs scales the same way: R^3 * SSV_abs = const ('each PSR sphere holds the
same total stress').  Compare with the ratified PSR law (R-PSR-LAW-LOG): PSR/l_P = 1 - eps + eps^2/2 + O(eps^3),
eps = k*Delta|SSV| (GR-1c: PSR = l_P/(1 + k Delta|SSV|) at first order), SSV_abs = S0 + Delta."""
import sympy as sp
eps, k, S0 = sp.symbols('epsilon k S0', positive=True)
Delta = eps / k
ratified = 1 - eps + eps**2 / 2
required = (1 + Delta / S0) ** sp.Rational(-1, 3)                 # R^3 * SSV_abs = const
d1 = sp.simplify(sp.series(required, eps, 0, 2).removeO().coeff(eps, 1))
print("first order: ratified coefficient -1; required", d1, "-> requires k*S0 =", sp.solve(sp.Eq(d1, -1), k)[0] * S0)
req2 = sp.series(required.subs(k, 1 / (3 * S0)), eps, 0, 3).removeO()
print("with k*S0 = 1/3, required law through second order:", sp.expand(req2), "  ratified:", ratified)
c2 = req2.coeff(eps, 2)
print(f"second-order coefficient: required {c2}, ratified 1/2 (Mercury-fixed)")
for name, phi in (("Earth surface", 7e-10), ("Sun surface", 2.1e-6), ("white dwarf", 1e-4), ("neutron star", 0.2)):
    print(f"  {name:14s} eps ~ {phi:.0e}: residual alpha shift ~ 3 x (2 - 1/2) eps^2 = {4.5*phi**2:.1e}")
# Annual swing at Earth from the second-order residual 4.5 eps^2 (eps ~ U; Sun + Earth potential at 1 au):
U = 9.87e-9 + 7e-10; dU = 3.30e-10                 # 4358: annual peak-to-peak swing of the Sun's potential
print(f"\nannual swing of the second-order residual at Earth: 9 eps d(eps) = {9*U*dU:.1e}  (Lange 2021 2-sigma: 1.2e-17)")
print("indicative only: assumes exact ratio invariance at first order, eps = U, and the ratified 1/2")
