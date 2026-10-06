#!/usr/bin/env python3
"""Patch 4385 -- the founder: rulers are a fixed number of PSRs (forces act over PSR units), so
clocks, rulers and light share one PSR (X = 1); and "use Einstein as the calibration for now".
Within X = 1 (g00 = -q^2, gij = q^-2 delta, q = PSR/l_P as a function of the census eps = m/r),
which PSR curve q(eps) makes the exterior agree with Einstein as far as it can?

Choice: match Einstein's clock rate as a function of AREAL radius, q^2 = 1 - 2m/R with R = r/q.
Part 1: closed form q = sqrt(1+eps^2) - eps = exp(-asinh eps); series; floor q = 1/2.
Part 2: what it reproduces exactly (redshift vs area, photon sphere, shadow, eikonal pitch).
Part 3: what differs: the radial ruler g_RR, hence the damping (eikonal, and l = 2 WKB).
Part 4: the conversion slope the curve requires, as a function of the shell fill f = 1/(8q^3).
Part 5: weak field and background residual.
"""
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import minimize_scalar

e, R, r = sp.symbols('epsilon R r', positive=True)
q = sp.sqrt(1 + e**2) - e
print("Part 1: q(eps) = sqrt(1+eps^2) - eps")
print("  series:", sp.series(q, e, 0, 6))
for ev in (0.1, 0.5, 2.0):
    print(f"  check ln q = -asinh(eps) at eps={ev}: {float(sp.log(q.subs(e, ev)) + sp.asinh(ev)):.1e}")
print("  floor q = 1/2 at eps =", sp.solve(sp.Eq(q, sp.Rational(1, 2)), e), "-> areal R = r/q = (4m/3)/(1/2) = 8m/3")
print("  q > 0 above the floor: no horizon there; the exterior ends at the floor.")

print("\nPart 2: exact agreements with Einstein")
qr = sp.sqrt(1 + 1/r**2) - 1/r                     # m = 1
print("  g_tt - (1 - 2m/R) with R = r/q:", sp.simplify(qr**2 - (1 - 2*qr/r)))
print("  photon sphere (max of g_tt/R^2) depends on g_tt(R) only: areal 3m, shadow 3*sqrt(3) m,")
print("  eikonal pitch 1/(3 sqrt3 m): all exactly Einstein's.  Redshift vs areal radius: Einstein's.")

print("\nPart 3: what differs -- the radial ruler")
f = 1 - 2/R
h = (R - 1)**2/(R**2*f**2)                         # g_RR from r = R sqrt(f), q^2 = f
print("  g_RR / g_RR(Einstein) =", sp.simplify(h*f), " = 1 + m^2/R^2 + ...")
V = f/R**2
lam = sp.sqrt(-(f/h).subs(R, 3)*sp.diff(V, R, 2).subs(R, 3)/(2*V.subs(R, 3)))
print("  eikonal damping / Einstein =", sp.nsimplify(lam*3*sp.sqrt(3)), "=", f"{float(lam*3*sp.sqrt(3)):.4f}",
      "-> -13.4%; pitch 0%")

def wkb(v, A=0.5):
    V0, V2, V3, V4, V5, V6 = v[0], v[2], v[3], v[4], v[5], v[6]; s_ = (-2*V2)**0.5
    Lam = (1/s_)*((1/8)*(V4/V2)*(0.25+A*A) - (1/288)*(V3/V2)**2*(7+60*A*A))
    Om = (1/(-2*V2))*((5/6912)*(V3/V2)**4*(77+188*A*A) - (1/384)*(V3**2*V4/V2**3)*(51+100*A*A)
         + (1/2304)*(V4/V2)**2*(67+68*A*A) + (1/288)*(V3*V5/V2**2)*(19+28*A*A) - (1/288)*(V6/V2)*(5+4*A*A))
    return ((V0 + s_*Lam) - 1j*A*s_*(1 + Om))**0.5
SREF = 0.4832 - 0.0968j                            # Schwarzschild scalar l = 2, same WKB order
def l2(Sf, dSdQ, l=2, m=1.0, hmax=1.2, deg=24):
    def rhs(x, y):
        rr, Q = y; q2 = np.exp(2*Q); return [q2, q2*Sf(Q)*m/rr**2]
    stop = lambda x, y: y[1] - np.log(0.5); stop.terminal = True
    s = solve_ivp(rhs, [0, -600], [400.0, -np.arcsinh(m/400.0)], dense_output=True, rtol=1e-12, atol=1e-14,
                  max_step=0.05, events=stop)
    def Vx(x):
        rr, Q = s.sol(x); S = Sf(Q); Qr = S*m/rr**2; Qrr = -2*S*m/rr**3 + (m/rr**2)*dSdQ(Q)*Qr
        RR = rr*np.exp(-Q); q2 = np.exp(2*Q)
        return q2*l*(l+1)/RR**2 + q2*np.exp(Q)*(Qr*(1 - rr*Qr) - Qr - rr*Qrr)/RR
    xs = np.linspace(s.t[-1] + 0.02, -5, 8000); vs = np.array([Vx(x) for x in xs]); i = int(np.argmax(vs))
    x0 = minimize_scalar(lambda x: -Vx(x), bracket=(xs[i-1], xs[i], xs[i+1]), tol=1e-12).x
    gap = x0 - s.t[-1]; hw = min(hmax, 0.9*gap); t = np.linspace(-hw, hw, 801)
    P = np.polynomial.chebyshev.Chebyshev.fit(t, np.array([Vx(x0 + u) for u in t]), deg).convert(kind=np.polynomial.Polynomial)
    w = wkb([P.deriv(k)(0) if k else P(0) for k in range(7)])
    return 100*(w.real/SREF.real - 1), 100*(abs(w.imag)/abs(SREF.imag) - 1), gap
print("  l = 2 SCALAR potential (a proxy for the gravitational one), 3rd-order WKB, fit window/degree varied:")
for name, S, dS in (("steady curve (4374 check: -4.06/-4.57)", lambda Q: 1.0, lambda Q: 0.0),
                    ("Einstein-calibrated curve", lambda Q: 1/np.cosh(Q), lambda Q: -np.tanh(Q)/np.cosh(Q))):
    res = [l2(S, dS, hmax=hw, deg=dg) for hw, dg in ((1.2, 24), (0.8, 20), (0.5, 16))]
    a = [x[0] for x in res]; b = [x[1] for x in res]
    print(f"   {name}: freq {np.mean(a):+.3f}% (spread {np.ptp(a):.3f})  damp {np.mean(b):+.3f}% "
          f"(spread {np.ptp(b):.3f})  peak {res[0][2]:.2f} tortoise units outside the floor")
print("  Fit-window stability is not accuracy: 4384 found WKB unreliable ~1.6-2 tortoise units from the")
print("  floor, and this peak is at 1.33.  Only the eikonal sqrt(3)/2 is robust.")
print("  GW250114 box (conv042 L8), in damping RATE gamma220 (221 +39/-32 Hz): -14.5%/+17.6%; freq +/-2.4%.")
print("  -> consistent with, not a fit to: non-spinning (chi_f = 0.68), scalar proxy, WKB near the floor,")
print("     and M_f inferred with GR inspiral dynamics (this curve departs from GR at 2PN in g_RR).")

print("\nPart 4: the conversion the curve requires.  d ln q/d eps = -S, S = 1/sqrt(1+eps^2)")
print("  In terms of Claude's fill mapping f = 1/(8q^3) (unratified; 4384): u = 2 f^(1/3) = 1/q, S = 2u/(1+u^2)")
for lab, ev in (("ordinary space", 0.0), ("Mercury-scale", 1e-7), ("neutron-star surface-ish", 0.2),
                ("photon sphere", 1/np.sqrt(3)), ("floor", 0.75)):
    qq = np.sqrt(1 + ev**2) - ev; ff = 1/(8*qq**3); S = 1/np.sqrt(1 + ev**2)
    print(f"   {lab:26s} eps={ev:.3g}  fill={ff:.3f}  S={S:.4f}  (PSR shrinks {100*(1-S):.1f}% slower per unit stress)")
print("  The calibration needs the PSR to RESIST shrinking as the shell fills (S < 1), never to shrink faster.")

print("\nPart 5: weak field and background")
print("  q = 1 - eps + eps^2/2 + 0*eps^3 - eps^4/8: Mercury's 1/2 kept (R-PSR-LAW-LOG); X = 1.  g00 = -q^2 and")
print("  gamma = 1 additionally need 3386's proper-length reading (unratified).  Earliest weak-field departure")
print("  from GR: the spatial metric at 2PN, g_RR ratio 1 + m^2/R^2.")
print("  Third-order coefficient 0 (the ruling left it open; e^-eps has -1/6).  4365's background residual")
print("  1 - (3*gamma3 + 1/2) eps0^2 -> 1 - eps0^2/2: unobservable for G; for alpha it matters only if alpha")
print("  carries the lapse's sensitivity (TODO-4364-EPSABS), where it would be ~2x 4381's kappa = 1 estimate.")
