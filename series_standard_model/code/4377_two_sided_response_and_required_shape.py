#!/usr/bin/env python3
"""Patch 4377 - the founder's answer (3 Oct 2026): the deeper-filled shell makes clocks run SLOWER, through a
two-sided response of the neighbouring CPs/DPs (opposite charges drawn in, like charges pushed out).

  1. Erratum to 4373: the required extra clock factor, written exactly, is X = 1 - rho^2 with
     rho = k Delta / 2 (half the local stress excess, the census itself), NOT 1 - c (dg)^2 in the fill
     increase dg; the two agree only near ordinary space.  Table from ordinary space to the cap.
  2. The founder's two-sided response, schematically: a neutral pair (+q, -q) of separation d in a field E;
     the net push on the pair cancels at first order, and the induced-dipole (polarisation) remainder is
     second order in E.  This is the cancel-at-first-order, square-remainder shape Einstein's factor has,
     if the field that polarises is proportional to the stress excess rho.
"""
import sympy as sp
print(__doc__)

rho = sp.symbols('rho', positive=True)
XE = 1 - rho ** 2
g = (1 + rho) ** 6                                        # fill relative to ordinary space (Einstein's rulers)
dg = g - 1
print("1. rho        fill f     X_E = 1-rho^2    1 - dg^2/36 (4373's small-fill form)")
for rv in (0.0, 0.05, 0.1, 0.2, 1 / (2 * (1 + sp.sqrt(3) / 2)), sp.Rational(1, 3), sp.sqrt(2) - 1):
    print(f"   {float(rv):.4f}    {float(g.subs(rho, rv))/8:6.3f}      {float(XE.subs(rho, rv)):.4f}            "
          f"{float((1 - dg**2/36).subs(rho, rv)):.4f}")
print("   rows: ordinary space ... photon sphere (rho = 0.268) ... AP-5 cap (1/3) ... sphere full (0.414).")
print("   The small-fill form fails by the photon sphere (0.72 vs 0.93): the requirement is in the STRESS, not the fill.")

# 2. neutral pair in a field E (1D schematic): positions +-d/2 about x0, field E(x) = E0 + E1 x
q, d, E0, E1, x0, alpha = sp.symbols('q d E0 E1 x0 alpha', real=True)
E = lambda x: E0 + E1 * x
F_rigid = sp.simplify(q * E(x0 + d / 2) - q * E(x0 - d / 2))           # rigid pair: net force q d E1
# polarisable pair: separation responds to the local field, d = d0 + alpha*q*E(x0)
d0 = sp.Symbol('d0', positive=True)
F_pol = sp.expand(F_rigid.subs(d, d0 + alpha * q * E(x0)))
print("\n2. neutral pair, net push in a field gradient: rigid", F_rigid, "; polarisable", F_pol)
print("   With no permanent alignment (d0 averaging to zero over random orientation), the surviving push is")
print("   alpha q^2 E E1 = (alpha q^2 / 2) d(E^2)/dx: second order in the field. The first-order pulls on the")
print("   + and - members cancel; the remainder goes as the square of the field (the founder's 'opposite drawn in,")
print("   like pushed out'). If E is proportional to rho, the extra slowing goes as rho^2: Einstein's shape.")
