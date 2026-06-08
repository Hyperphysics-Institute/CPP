#!/usr/bin/env python3
"""
0806_zbw_bound_gradient_control.py  --  DM-2 Step 2(a): the load-bearing check.

Does the ZBW-scale value of k*Delta|SSV| force evaluation of F in the strong-
AMPLITUDE regime (= c08 Open Problem 1)? Established c08 facts used:
  * k*Delta|SSV| = GM/rc^2  (exact shell-broadcast source, c08 eq. source)
  * CP Exclusion: k*Delta|SSV| in [0,1], saturating at 1 at the Planck core.
  * F = [2k u^2/(1+ku)^2] * box(ln(1+ku)),  u := Delta|SSV|.

Verdict (detail in dm2_step2a_zbw_bound.md): condition (a) PASSES. The uniform
Sea's O(1) absolute amplitude does NOT trigger OP1, because F is GRADIENT-
controlled, not amplitude-controlled.
"""
import sympy as sp

print("="*70)
print("BOUND: at the ZBW (Compton r=hbar/mc) scale, k*Delta|SSV| = GM/rc^2 = (m/m_P)^2")
m_P_GeV = 1.22089e19
rows = [("electron",0.000511),("up quark~",0.0022),("proton",0.9383),
        ("GeV DM constituent",1.0),("100 GeV",100.0),("Planck mass",m_P_GeV)]
for name,m in rows:
    val=(m/m_P_GeV)**2
    reg = "WEAK (<<1)" if val<1e-6 else ("O(1) STRONG" if val>0.1 else "intermediate")
    print(f"  {name:20s} m={m:11.4g} GeV -> k*Delta|SSV|={val:.3e}   {reg}")
print("  => every sub-Planck constituent (all matter/DM) is weak-field by >=35 orders.")
print("  => only the Planck-scale Sea ground state itself is O(1) (ceiling = 1).")

print("="*70)
print("GRADIENT-CONTROL: is the O(1) ground-state amplitude dangerous? (does it need OP1?)")
x = sp.symbols('x', real=True)
k,u0,a,q = sp.symbols('k u0 a q', positive=True)
u = u0 + a*sp.sin(q*x)                      # O(1) background u0 + a slow fluctuation
F = 2*k*u**2/(1+k*u)**2 * sp.diff(sp.log(1+k*u), x, 2)
F_lin = sp.simplify(sp.series(F, a, 0, 2).removeO().coeff(a,1))
print("  leading fluctuation source F_lin =")
sp.pprint(F_lin)
carries_q2 = sp.simplify(F_lin / (q**2 * sp.sin(q*x)))
print("\n  F_lin / (q^2 sin(qx)) =")
sp.pprint(sp.simplify(carries_q2))
print("\n  => F_lin ~ q^2 (gradient^2). The background u0 enters ONLY via the bounded")
print("     combo below; it multiplies the gradient, it does not amplify by itself.")

print("="*70)
print("PREFACTOR / BACKGROUND FACTOR IS BOUNDED on k*Delta|SSV| in [0,1]")
w = sp.symbols('w', nonnegative=True)            # w = k*u0
pref = 2*w**2/(1+w)**3                            # the u0-dependent factor in F_lin/(k^2..)
crit = sp.solve(sp.diff(pref,w), w)
cand = [c for c in crit if c.is_real and 0<=c<=1] + [sp.Integer(0), sp.Integer(1)]
vals = [(float(c), float(pref.subs(w,c))) for c in cand]
mx = max(vals, key=lambda t:t[1])
print(f"  factor 2w^2/(1+w)^3 on w in [0,1]: max = {mx[1]:.4f} at w = {mx[0]:.3f}  (finite, no blowup)")
print("  => even at the CP-exclusion ceiling w=1 the source factor is bounded (=1/4).")

print("="*70)
print("VERDICT: condition (a) PASSES -- separability ROBUST, OP1 NOT triggered.")
print("  Gravitation is gradient-controlled: F = [bounded factor of amplitude] x [q^2 gradient].")
print("  * Uniform Sea ground state: O(1) amplitude but ~0 gradient -> sources ~0. OP1 (a")
print("    strong-AMPLITUDE statement) never enters. (Curvature ~ d^2(metric), not |SSV|.)")
print("  * The only large-GRADIENT sources are sub-Planck localized excesses (matter, DM")
print("    swirls), weak-field by (m/m_P)^2 ~ 1e-39 -- F-truncation + Step-1 parity hold there.")
print("  Residual (narrow, NOT OP1): whether the discrete Planck-scale zero-point has a net")
print("  parity-broken gradient surviving coarse-graining = net-broadcast lemma cond.(b),")
print("  pursued in the residual<->Lambda identification (0807).")
