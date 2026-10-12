"""Patch 4403 -- founder (on 4402): gravity comes from the difference between the outer-limb and inner-limb SSV_abs;
the test CP's DI-bits come from the GPs one PSR away; his hydrostatic analogy (unbalanced 'pressure').  Is it adequate?

Part 1  the sign: SSV_abs (the census u = sum m/r) is LARGER on the inner limb.  A pressure-like push from the side with
        more DI-bits would push the CP AWAY from the mass.  The response must be toward the side with more: attraction.
Part 2  the size: Newton's g needs, per Moment, a change of the CP's drift (in PSRs per Moment) equal to the census
        difference across ONE PSR:  dv/c per Moment = g t_P / c = (g/c^2) l_P = |grad u| l_P.
Part 3  his 'smaller PSR on the inner limb', read as the PSR at the inner limb vs at the outer limb (GR-1a:
        PSR_eff = l_P/(1 + k u)), differs by ~ grad u: inverse square, right direction.
Part 4  a body at rest: refraction of its internal oscillation by the clock gradient builds momentum m g t.
Part 5  one picture: the river's acceleration is -grad(beta^2/2) = -grad(u): the step rule and the shifted sphere of
        4397 are the same gravity.
Part 6  (removed after critique: the pair-force comparison at the core does not support a gradient argument)
"""
import numpy as np
import sympy as sp

G, c, hbar = 6.674e-11, 2.998e8, 1.055e-34
lP = np.sqrt(hbar*G/c**3); tP = lP/c; mP = np.sqrt(hbar*c/G)

print("Part 1: census on the two limbs of a CP at Earth's surface (u = GM/(r c^2))")
Me, Re = 5.972e24, 6.371e6
u = lambda r: G*Me/(r*c**2)
d_limbs = 2*G*Me*lP/(Re**2*c**2)      # u(R - lP) - u(R + lP) to first order
print(f"  u at the CP = {u(Re):.6e}; inner limb minus outer limb = {d_limbs:.3e} > 0  -> the inner limb has MORE")
print("  a push from the side with more DI-bits points away from the Earth: the response must be a pull toward it")

print("\nPart 2: the size")
g = G*Me/Re**2
dv = g*tP/c
du = d_limbs/2
print(f"  g t_P / c (change of drift per Moment, in light units) = {dv:.4e}")
print(f"  census difference across one PSR, (u_in - u_out)/2     = {du:.4e}   ratio {dv/du:.6f}")
print("  -> each Moment the CP's drift toward the mass grows by the SSV_abs (census) difference across one PSR")
print(f"  (after one second, {1/tP:.2e} Moments, the drift is {dv/tP:.3e} c = {g:.2f} m/s)")

print("\nPart 3: his 'smaller PSR on the inner limb' read as a gradient (GR-1a: PSR_eff = l_P/(1 + k u))")
r, M, k = sp.symbols('r M k', positive=True)
uu = M/r
psr = 1/(1 + k*uu)
d = sp.series(psr.subs(r, r + 1) - psr.subs(r, r - 1), M, 0, 2).removeO()   # outer limb minus inner limb, limbs 1 PSR away
print("  PSR(outer) - PSR(inner) to first order in M:", sp.simplify(d), " ~ grad u: inverse square, pointing to the mass")
print("  (only if the 4397 shift beta = sqrt(2u) is substituted for the PSR would a sqrt law appear)")

print("\nPart 4: a body released at rest -- refraction of its internal oscillation by the clock gradient")
m, c_, hb, t, g_ = sp.symbols('m c hbar t g', positive=True)
x = sp.symbols('x')
u_x = g_*x/c_**2                       # census rising toward the mass along +x (weak field)
omega = m*c_**2/hb*(1 - u_x)           # internal rate slowed by the clock factor (1 - u)
kvec = -t*sp.diff(omega, x)            # wavenumber built up by the phase lag: k = -t d(omega)/dx
p = sp.simplify(hb*kvec)
print("  internal rate omega = (m c^2/hbar)(1 - u); momentum after time t: p =", p, "-> m g t toward the mass")
print("  the momentum grows steadily (acceleration, not drift), and depends only on the clock factor: no polarity")
print("  (the matter-wave version of GR-FE-1's refraction; measured in neutron interferometry, COW 1975)")

print("\nPart 5: one picture")
v = sp.sqrt(2*M/r)
print("  river acceleration v dv/dr =", sp.simplify(v*sp.diff(v, r)), " = -d(u)/dr: exact for radial infall (proper time,")
print("  areal r); a hovering observer needs M/r^2/sqrt(1-2M/r); no perihelion term; light needs the space half too")

