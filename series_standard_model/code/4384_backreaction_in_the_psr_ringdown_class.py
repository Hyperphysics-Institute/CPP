#!/usr/bin/env python3
"""Patch 4384 -- founder's answers to 4383 §6.
 (1) the attracted CP is closer, so its hold exceeds the repelled CP's help;
 (2) the chance a DP's CPs sit in the DI-bit shell grows with SSV_abs (shell thickness);
 (3) light = one PSR per Moment; the DPs' presence/movement acts back on the PSR itself
     (and is probably the source of mu0*eps0).
Part 1: closer-is-stronger makes the net hold second order in the shell's push.
Part 2: the shell fill (Claude's proxy for the landing chance), R-DIBIT-COUNT-AT-FLOOR f = 1/(8q^3).
Part 3: if the back-reaction acts on the PSR, clocks, rulers and light share one PSR (X = 1).
        Ringdown (eikonal, non-spinning) for conversion curves that steepen or soften with fill:
        d ln q/d eps = -(1 + a*g^p),  g = (f - 1/8)/(7/8).
Part 4: weak-field and background order of the fill term.
"""
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import minimize_scalar

print("Part 1: shell push F moves the attracted CP to d-x, the repelled one to d+x (x ~ F)")
F, d, x, c = sp.symbols('F d x c', positive=True)
hold = F*d**2/(d - x)**2; help_ = F*d**2/(d + x)**2
net = sp.series(hold - help_, x, 0, 3).removeO()
print("  net hold =", sp.simplify(net), "; with x = c*F:", sp.expand(net.subs(x, c*F)))
print("  -> net hold ~ 4cF^2/d: second order in the push, always a hold (the 'added spring' branch of 4383).")

print("\nPart 2: shell fill f = 1/(8 q^3) (R-DIBIT-COUNT-AT-FLOOR); steady curve q = e^-eps, eps = m/r")
for lab, e in (("ordinary space", 0.0), ("photon sphere, steady curve", 0.5), ("floor/cap, eps = ln 2", np.log(2))):
    q = np.exp(-e); print(f"  {lab:30s} q={q:.3f}  fill={1/(8*q**3):.3f}")
print("  The chance is ~1/8 in ordinary space (not tiny, but constant there); it grows to ~0.56 at the")
print("  photon sphere and 1 at the floor.  (Taking the landing chance = fill is Claude's mapping.)")

print("\nPart 3: one PSR for clocks, rulers and light (X = 1): N = q, A = 1/q^2")
def qcurve(a, p, emax=3.0):
    def rhs(e, y):
        q = np.exp(y[0]); f = 1/(8*q**3); g = max(0.0, (f - 0.125)/0.875)**p
        return [-(1 + a*g)]
    def floor(e, y): return y[0] - np.log(0.5)
    floor.terminal = True
    s = solve_ivp(rhs, [0, emax], [0.0], dense_output=True, events=floor, rtol=1e-11, atol=1e-13, max_step=0.01)
    ecap = s.t_events[0][0] if len(s.t_events[0]) else emax
    return (lambda e: np.exp(s.sol(e)[0])), ecap
def eik(qf, ecap, m=1.0):
    V = lambda r: qf(m/r)**4/r**2                      # f/R^2 with f = q^2, R = r/q
    rs = np.linspace(m/ecap*1.0001, 20, 4000); vs = np.array([V(r) for r in rs]); i = int(np.argmax(vs))
    if i == 0: return None
    rc = minimize_scalar(lambda r: -V(r), bracket=(rs[i-1], rs[i], rs[i+1]), tol=1e-12).x
    Vc = V(rc); h = 1e-4*rc; Vrr = (V(rc+h) - 2*Vc + V(rc-h))/h**2
    q = qf(m/rc); lam = np.sqrt(-q**4*Vrr/(2*Vc))       # f/h = q^4
    return rc/q, np.sqrt(Vc), lam
GR = 1/(3*np.sqrt(3))
# validation: a = 0 is the exponential exterior (4365/4372: -4.42%, -4.42%)
print("  a = 0 (steady curve):", "freq %+.2f%%  damp %+.2f%%" % tuple(100*(v/GR - 1) for v in eik(*qcurve(0, 2))[1:]))
print("  GW250114 box (conv042 L8): freq +/-2.4%, damping -14.5%/+17.6%")
print("  a > 0: the PSR shrinks FASTER as it fills;  a < 0: it resists shrinking")
for p in (2, 3, 4):
    for a in (-0.3, -0.2, -0.1, 0.5, 1, 2, 5):
        r = eik(*qcurve(a, p))
        if r is None: print(f"   p={p} a={a:+.1f}: no light ring"); continue
        print(f"   p={p} a={a:+.1f}: light ring areal {r[0]:.3f} m  freq {100*(r[1]/GR-1):+6.2f}%  damp {100*(r[2]/GR-1):+6.2f}%")
inbox, best = False, None
for p in (1.5, 2, 3, 4, 6, 8):
    for a in np.linspace(-0.45, 1.0, 59):
        r = eik(*qcurve(a, p))
        if r is None: continue
        df, dg = 100*(r[1]/GR-1), 100*(r[2]/GR-1)
        dist = max(0, abs(df)-2.4)/2.4 + max(0, -14.5-dg)/14.5 + max(0, dg-17.6)/17.6
        inbox |= dist == 0
        if best is None or dist < best[0]: best = (dist, p, a, df, dg)
print(f"  Scan p in (1.5..8), a in [-0.45, 1.0]: any curve in the box? {inbox}")
print(f"  Closest: p={best[1]} a={best[2]:+.3f}: freq {best[3]:+.2f}%  damp {best[4]:+.2f}%")

print("\nPart 4: order of the fill term.  f - 1/8 ~ (3/8) eps, so a*g^p ~ a*(3 eps/7)^p:")
print("  p = 1 changes the PSR's eps^2 coefficient: beta = 1 + 3a/14, so |a| < ~5e-4.")
print("  p = 2 enters at eps^3 (Mercury safe) but shifts the third-order coefficient, so the")
print("        background residual (3*gamma3 + 1/2)*eps0^2 of 4365 returns.")
print("        (gamma3 shifts by -3a/49; residual -(9a/49) eps0^2.)")
print("  p > 2: residual of order a*eps0^p, negligible; p = 1.5 is non-analytic, residual ~ eps0^1.5.")

print("\nPart 5: l = 2 scalar mode, 3rd-order WKB (Iyer-Will), Schwarzschild reference 0.4832 - 0.0968i")
def make2(a,p,bump=None):
    # S(eps-state): dQ/deps = -S, S = 1 + a g^p (+ bump)
    def Sfun(Q):
        g=max(0.0,(np.exp(-3*Q)-1)/7)
        s=1+a*g**p; ds=a*p*g**(p-1) if (g>0 and a!=0) else 0.0
        if bump:
            A,g0,w=bump; e=np.exp(-((g-g0)/w)**2); s+=A*e; ds+=A*e*(-2*(g-g0)/w**2)
        return s, ds, g
    return Sfun
def wkb_l2(Sfun,l=2,m=1.0):
    def rhs(x,y):
        r,Q=y; q2=np.exp(2*Q); S,_,_=Sfun(Q)
        return [q2, q2*S*m/r**2]          # dr/dx=q^2, dQ/dx = q^2 dQ/dr
    ev=lambda x,y: y[1]-np.log(0.5); ev.terminal=True
    r0=400.0; Q0=-m/r0
    s=solve_ivp(rhs,[0,-600],[r0,Q0],dense_output=True,rtol=1e-12,atol=1e-14,max_step=0.05,events=ev)
    def V(x):
        r,Q=s.sol(x); S,dS_dg,g=Sfun(Q)
        Qr=S*m/r**2
        dg_deps=(3/7)*np.exp(-3*Q)*S
        dS_dr=dS_dg*dg_deps*(-m/r**2)
        Qrr=-2*S*m/r**3+(m/r**2)*dS_dr
        R=r*np.exp(-Q); q2=np.exp(2*Q)
        DDR=q2*np.exp(Q)*(Qr*(1-r*Qr)-Qr-r*Qrr)
        return q2*l*(l+1)/R**2+DDR/R
    xs=np.linspace(s.t[-1]+0.05,-5,6000); vs=np.array([V(x) for x in xs]); i=int(np.argmax(vs))
    if i==0: return None, xs[i]-s.t[-1]
    x0=minimize_scalar(lambda x:-V(x),bracket=(xs[i-1],xs[i],xs[i+1]),tol=1e-12).x
    h=min(1.2,0.9*(x0-s.t[-1])); t=np.linspace(-h,h,801)
    c=np.polynomial.chebyshev.Chebyshev.fit(t,np.array([V(x0+u) for u in t]),24)
    P=c.convert(kind=np.polynomial.Polynomial); d=[P.deriv(k)(0) if k else P(0) for k in range(7)]
    return d, x0-s.t[-1]
def wkb(v,A=0.5):
    V0,V2,V3,V4,V5,V6=v[0],v[2],v[3],v[4],v[5],v[6]; s_=(-2*V2)**0.5
    Lam=(1/s_)*((1/8)*(V4/V2)*(0.25+A*A)-(1/288)*(V3/V2)**2*(7+60*A*A))
    Om=(1/(-2*V2))*((5/6912)*(V3/V2)**4*(77+188*A*A)-(1/384)*(V3**2*V4/V2**3)*(51+100*A*A)+(1/2304)*(V4/V2)**2*(67+68*A*A)+(1/288)*(V3*V5/V2**2)*(19+28*A*A)-(1/288)*(V6/V2)*(5+4*A*A))
    return ((V0+s_*Lam)-1j*A*s_*(1+Om))**0.5

SREF = 0.4832 - 0.0968j
def run_l2(a, p):
    d, gap = wkb_l2(make2(a, p))
    if d is None: return None
    om = wkb(d); return 100*(om.real/SREF.real - 1), 100*(abs(om.imag)/abs(SREF.imag) - 1), gap
print("  a = 0 check (4374: -4.06% / -4.57%):", "freq %+.2f%%  damp %+.2f%%  (peak %.2f tortoise units outside the floor)" % run_l2(0, 2))
for p in (2, 3, 4):
    for a in (-0.3, -0.2, -0.15, -0.1, 0.1, 0.5):
        r = run_l2(a, p)
        if r is None: print(f"   p={p} a={a:+.2f}: the l = 2 peak merges with the floor (no WKB)"); continue
        tag = "  IN BOX" if (abs(r[0]) <= 2.4 and -14.5 <= r[1] <= 17.6) else ""
        print(f"   p={p} a={a:+.2f}: freq {r[0]:+6.2f}%  damp {r[1]:+7.2f}%  gap {r[2]:.2f}{tag}")
print("  Eikonal and l = 2 disagree for resisting curves: the l = 2 potential carries d(slope)/d eps")
print("  terms the eikonal limit drops, and its peak sits only ~1.6-2 tortoise units outside the floor,")
print("  where WKB is unreliable (erratic values at steeper p).  Neither method settles the class: a")
print("  full mode calculation with the floor's boundary condition is needed.")
