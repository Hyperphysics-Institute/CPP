#!/usr/bin/env python3
"""4318 -- (1) the founder's steady-state Planck ZBW on the Moment clock; (2) the equivalent readings of alpha.

(1) Founder 4318: two CPs oscillate about a centre, pass through each other at maximum speed, stop at apogee on
opposite sides simultaneously.  c04 Def. Level 1: nu_P = 1/(2 t_P) -> M = 2 Moments per full cycle.  A CP makes one
displacement per Moment, capped at one PSR = l_P (c04 spatial-step relation; founder 4288: light speed = one PSR per
Moment).  Sample the symmetric oscillation x_n = A cos(2 pi n / M): the largest per-Moment step is 2A sin(pi/M) for
even M (the centre crossing); requiring it <= l_P bounds A.  How many Moments are needed before the slow-apogee /
fast-centre profile the founder describes is even representable?

(2) Standard identities (CODATA 2018), checked numerically: alpha = e^2/(4 pi eps0 hbar c) = (e/e_P)^2
= Z0/(2 R_K) = r_e / lambdabar_C.  None contains G."""
import numpy as np

print("(1) the founder's pass-through oscillation sampled on the Moment clock (l_P = one PSR; max step <= l_P)")
print(f"{'M Moments/cycle':>16s} {'max A / l_P':>12s} {'half-cycle travel / l_P':>24s} {'distinct speeds':>16s}  profile")
for M in [2, 4, 6, 8, 12, 24]:
    n = np.arange(M+1)
    x = np.cos(2*np.pi*n/M)                      # unit amplitude
    steps = np.abs(np.diff(x))
    A = 1/steps.max()                            # scale so the largest step is exactly l_P
    travel = 2*A                                 # apogee to opposite apogee
    speeds = sorted(set(np.round(steps*A, 6)))
    prof = ("two-state flip: +A,-A; no apogee rest, no centre crossing sampled" if M == 2 else
            "constant speed: every step equal" if len(speeds) == 1 else
            f"speeds {', '.join(f'{s:.3f}' for s in speeds)} l_P/Moment")
    print(f"{M:16d} {A:12.4f} {travel:24.4f} {len(speeds):16d}  {prof}")
print("   c04's nu_P = 1/(2 t_P) is the M = 2 row: in one Moment the CP goes apogee to apogee, one full PSR (~1e30 GPs),")
print("   amplitude l_P/2.  M = 4 moves at constant speed.  'Slow near apogee, fastest through the centre' first appears")
print("   at M = 6; a finer profile needs more Moments per cycle, i.e. a ZBW slower than nu_P = 1/(2 t_P).")
# a Moment of rest at apogee: sample with a half-step phase offset so two samples straddle the apogee
for M in [4, 6]:
    x = np.cos(2*np.pi*(np.arange(M+1)+0.5)/M); st = np.abs(np.diff(x))
    print(f"   half-step-offset sampling, M = {M}: steps / max = {', '.join(f'{s/st.max():.2f}' for s in st)}"
          f"  (a 0 = one Moment at rest at apogee)")

print("\n(2) the readings of alpha (all the same number; none uses G)")
e=1.602176634e-19; h=6.62607015e-34; hbar=h/(2*np.pi); c=299792458.0; eps0=8.8541878128e-12
me=9.1093837015e-31; mu0=1.25663706212e-6
alpha = e**2/(4*np.pi*eps0*hbar*c)
eP = np.sqrt(4*np.pi*eps0*hbar*c)
Z0 = np.sqrt(mu0/eps0); RK = h/e**2
re = e**2/(4*np.pi*eps0*me*c**2); lbarC = hbar/(me*c)
rows = [("static Coulomb   e^2/(4 pi eps0 hbar c)", alpha),
        ("vertex (e/e_P)^2, e_P = sqrt(4 pi eps0 hbar c)", (e/eP)**2),
        ("radiative Z0/(2 R_K), R_K = h/e^2", Z0/(2*RK)),
        ("electron lengths r_e / lambdabar_C", re/lbarC)]
for name, v in rows:
    print(f"   {name:48s} = 1/{1/v:.6f}")
print(f"   Z0 = {Z0:.3f} ohm (the sea's impedance), R_K = {RK:.1f} ohm (h/e^2: action per charge squared)")
rth = lbarC/2
sigT = 8*np.pi/3*re**2
print(f"   c04 cloud: r_th = lambdabar_C/2 = {rth:.4e} m;  r_e = alpha lambdabar_C = 2 alpha r_th = {re:.4e} m")
print(f"   Thomson cross-section / c04 cloud area pi r_th^2 = (32/3) alpha^2 = {sigT/(np.pi*rth**2):.3e}")
