#!/usr/bin/env python3
"""Patch 4395 -- founder: the directional part is SSV_net (V_i); V_i is "squeezed as SSV_abs squeezes the PSR".

Reading of "squeezed as the PSR is squeezed": the advance per Moment, counted in PSRs, falls by the same
fraction as the PSR's grid size: s = p, with p = 1 - aU (b = a).  First order.
Columns: light speed on the grid; crystal size; CP clock (CP speed / crystal); light clock (light / crystal).
Targets: light 1 - 2U, crystal 1 - U, both clocks 1 - U (all clocks alike).
"""
import sympy as sp
U, a = sp.symbols('U a')
lin = lambda e: sp.expand(sp.series(e, U, 0, 2).removeO())
p = 1 - a*U
def row(label, light, cp, crystal):
    vals = [lin(light), lin(crystal), lin(cp/crystal), lin(light/crystal)]
    sol = sp.solve(sp.Eq(sp.Poly(vals[0], U).coeff_monomial(U), -2), a)
    av = sol[0] if sol else None
    sub = [sp.simplify(v.subs(a, av)) if av is not None else v for v in vals]
    ok = (sub[0] == 1-2*U, sub[1] == 1-U, sub[2] == 1-U, sub[3] == 1-U)
    print(f"{label}\n   bending fixes a = {av}:  light {sub[0]}, crystal {sub[1]}, CP clock {sub[2]}, "
          f"light clock {sub[3]}  -> {'ALL PASS' if all(ok) else 'fails: ' + ', '.join(n for n, o in zip(['bending','crystal','CP clock','light clock'], ok) if not o)}")
row("(i) squeeze on CPs AND light; crystal = n PSRs (his 4385 force picture)", p*p, p*p, p)
row("(i') squeeze on CPs AND light; crystal fixed on the grid (his 4390 'A and B fixed')", p*p, p*p, sp.Integer(1))
row("(ii) squeeze on CPs only; light exactly one PSR per Moment; crystal = n PSRs", p, p*p, p)
row("(iv) no squeeze; light and CPs one PSR per Moment; crystal shrinks half (4389 (b))", p, p, sp.sqrt(p))
print("\nUnder 'squeezed in the same proportion' the bending fixes a = 1 uniquely when light is squeezed too.")
