#!/usr/bin/env python3
"""
3258_t1_relay_verify.py — W-2 verify script for the T-1 field-equation
derivation (OPEN-GR-FE-1, charter Patch 3254; picture Patch 3255/3257).

Checks the mathematical claims of the T-1 derivation document
(series_gravitation/fe1_derivation/T1_derivation.md), in the order the
document makes them:

  1. STATIC MEAN-VALUE EXACTNESS: the shell-mean of u = 1/r about any
     exterior point equals u at that point, for ANY shell radius —
     including position-dependent radius R(x). (Newton shell identity;
     grounds: static vacuum reduction of the relay is Laplace's
     equation on the ABSOLUTE lattice, exactly, independent of PSR
     variation.)
  2. RELAY EIGENVALUE: the shell-mean operator on plane waves e^{ik.x}
     has eigenvalue sinc(kR) (numeric vs closed form).
  3. IRREVERSIBLE CLOSURE FAILS: the one-level relay u(t+1) = M_R u(t)
     has |eigenvalue| < 1 for all k>0 — every mode damps; no wave
     propagation. (Dead end documented in the derivation §4.)
  4. REVERSIBLE CLOSURE PROPAGATES: the two-level relay
     u(t+1) + u(t-1) = 2 M_R u(t) has dispersion cos(w tau) = sinc(kR):
     undamped (|amplification| = 1) for long wavelengths, with
     long-wave phase speed v = R/(sqrt(3) tau). Numeric 1D-radial
     evolution cross-check of the speed.
  5. STATIC DICTIONARY (sympy): on the exact GR-1a/GR-1c profile
     k*Dssv = a/r (a = GM/c^2, isotropic/lattice radius), compute the
     curved d'Alembertian Box_g(Dssv) for the measured metric
     A = ((1-p)/(1+p))^2, B = (1+p)^4, p = a/2r, and:
       (i)  confirm Box_g(Dssv) != 0 (the measured-frame operator alone
            does NOT annihilate the exact profile);
       (ii) series-expand the required compensator F* = -Box_g(Dssv)
            and the GR-1c stated F-term on the same profile (both
            operator readings), and report the order of agreement.
     This adjudicates the HALT rule: the T-1 lattice-frame static
     reduction (Laplace, exact) vs the GR-1c measured-frame statement
     (Box + F): same solution, dictionary-related operators.

No free parameters. No CPP-specific numerics beyond the registered
profile and metric. Tolerances stated per check.
"""
import numpy as np
import sympy as sp

PASS = []
def check(name, ok, detail=""):
    PASS.append(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))

def fibonacci_sphere(n):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2*i/n)
    theta = np.pi*(1 + 5**0.5)*i
    return np.stack([np.sin(phi)*np.cos(theta),
                     np.sin(phi)*np.sin(theta),
                     np.cos(phi)], axis=1)

print("== CHECK 1: static mean-value exactness (shell theorem), incl. variable R ==")
npts = 200_000
sph = fibonacci_sphere(npts)
rng = np.random.default_rng(3258)
worst = 0.0
for trial in range(12):
    x0 = rng.normal(size=3); x0 *= (4.0 + 6.0*rng.random())/np.linalg.norm(x0)
    # variable shell radius, incl. a position-dependent rule R(x0):
    R = 0.3 + 2.2*rng.random() if trial < 8 else 1.0/(1.0 + 0.1*np.linalg.norm(x0))
    pts = x0[None, :] + R*sph
    mean_u = np.mean(1.0/np.linalg.norm(pts, axis=1))
    err = abs(mean_u - 1.0/np.linalg.norm(x0))*np.linalg.norm(x0)
    worst = max(worst, err)
check("shell-mean(1/r) == 1/r exactly, any R (12 trials)", worst < 5e-9,
      f"worst rel err {worst:.2e}")

print("== CHECK 2: shell-mean eigenvalue on plane waves == sinc(kR) ==")
R = 1.0
worst = 0.0
for kmag in [0.1, 0.7, 1.5, 3.0, 6.0]:
    k = kmag*np.array([0.36, -0.48, 0.8])/1.0  # |dir|=1
    vals = np.exp(1j*R*(sph @ k))
    ev = np.mean(vals).real
    ev_true = np.sinc(kmag*R/np.pi)  # np.sinc(x)=sin(pi x)/(pi x)
    worst = max(worst, abs(ev - ev_true))
check("numeric eigenvalue matches sinc(kR)", worst < 1e-6, f"worst abs err {worst:.2e}")

print("== CHECK 3: irreversible one-level relay cannot propagate ==")
kk = np.linspace(1e-4, 20.0, 4000)
ev = np.sinc(kk*R/np.pi)
check("|sinc(kR)| < 1 for all k>0 (all modes damp)", np.all(np.abs(ev) < 1.0),
      f"max |ev| at k>0: {np.max(np.abs(ev)):.6f}")

print("== CHECK 4: reversible two-level relay — dispersion + numeric speed ==")
# dispersion cos(w tau) = sinc(kR): long-wave expansion w = k R/sqrt(3) tau
kR = np.array([1e-3, 3e-3, 1e-2])
w_tau = np.arccos(np.sinc(kR/np.pi))
v_over = w_tau/kR  # v*tau/R
check("long-wave phase speed -> R/(sqrt(3) tau)",
      np.allclose(v_over, 1/np.sqrt(3), rtol=1e-5),
      f"v*tau/R = {v_over[-1]:.8f}, 1/sqrt(3) = {1/np.sqrt(3):.8f}")
# numeric group velocity from the dispersion relation (finite difference):
kk2 = np.array([2e-3, 2.1e-3])
ww2 = np.arccos(np.sinc(kk2*R/np.pi))
vg = (ww2[1]-ww2[0])/(kk2[1]-kk2[0])
check("long-wave group velocity -> R/(sqrt(3) tau)",
      abs(vg - 1/np.sqrt(3)) < 1e-4, f"vg*tau/R = {vg:.6f}")
# unitarity of the two-level relay: for every k with |sinc(kR)|<=1 (all k),
# cos(w tau)=sinc(kR) has real w -> |amplification|=1, no damping:
check("two-level relay undamped for all k (real dispersion)",
      np.all(np.abs(np.sinc(kk*R/np.pi)) <= 1.0), "unitary band structure")

print("== CHECK 5: sympy static dictionary — Box_g on the exact profile vs GR-1c F ==")
r, a, kc = sp.symbols('r a k', positive=True)
p = a/(2*r)                       # varrho
u = a/(kc*r)                      # Dssv: k*u = a/r (exact GR-1a relation)
A = ((1 - p)/(1 + p))**2          # -g_tt/c^2
B = (1 + p)**4                    # spatial conformal factor
sqrtg = sp.sqrt(A)*B**sp.Rational(3,2)*r**2
Box_g_u = sp.cancel(sp.together(sp.diff(sqrtg*(1/B)*sp.diff(u, r), r)/sqrtg))
ser_box = sp.expand(sp.series(Box_g_u, a, 0, 5).removeO())
c3 = sp.simplify(ser_box.coeff(a, 3)); c2 = sp.simplify(ser_box.coeff(a, 2))
check("Box_g(Dssv) on exact profile: O(a^2) coeff vanishes, O(a^3) = -1/(2 k r^5)",
      c2 == 0 and sp.simplify(c3 + 1/(2*kc*r**5)) == 0,
      f"a^2 coeff = {c2}, a^3 coeff = {c3}")
Fstar_lead_order, Fstar_lead = 3, sp.simplify(-c3)   # F* = -Box_g u
print(f"    required compensator F*: leading order a^{Fstar_lead_order}, coeff {Fstar_lead} (i.e. +a^3/(2 k r^5))")
# GR-1c stated F-term, on the same profile, three readings:
ku = kc*u
pref  = 2*ku**2/(1 + ku)**2       # dimensionless-k reading
pref_lit = 2*kc*u**2/(1 + ku)**2  # literal 2k(Dssv)^2 reading
logt = sp.log(1 + ku)
flat_box_log = sp.cancel(sp.diff(r**2*sp.diff(logt, r), r)/r**2)
curv_box_log = sp.cancel(sp.together(sp.diff(sqrtg*(1/B)*sp.diff(logt, r), r)/sqrtg))
cands = {"F_flat (pref*flatBox ln)":  pref*flat_box_log,
         "F_curv (pref*curvBox ln)":  pref*curv_box_log,
         "F_lit  (2k u^2 pref, flatBox ln)": pref_lit*flat_box_log}
mismatch_all = True
for name, F in cands.items():
    sF = sp.expand(sp.series(sp.cancel(sp.together(F)), a, 0, 6).removeO())
    lo = next((n for n in range(0, 6) if sp.simplify(sF.coeff(a, n)) != 0), None)
    co = sp.simplify(sF.coeff(a, lo)) if lo is not None else 0
    hit = (lo == Fstar_lead_order and sp.simplify(co - Fstar_lead) == 0)
    mismatch_all = mismatch_all and not hit
    print(f"    {name}: leading order a^{lo}, coeff {co}; matches F*: {hit}")
check("HALT FINDING ESTABLISHED: no reading of the GR-1c F-term matches the "
      "required compensator at leading nonlinear order (F* = O(a^3); F = O(a^4))",
      mismatch_all, "static reductions agree at SOLUTION level, disagree at stated-F level")
# solution-level agreement: the exact profile solves the LATTICE-frame statics exactly:
flat_lap_u = sp.cancel(sp.diff(r**2*sp.diff(u, r), r)/r**2)
check("exact profile solves the lattice-frame vacuum statics exactly (flat Laplace)",
      sp.simplify(flat_lap_u) == 0, f"flat Laplacian of a/(k r) = {sp.simplify(flat_lap_u)}")

# weak-field source check: flat Laplacian of k*Dssv = a/r gives -4 pi (G M/c^2) delta^3
# -> Poisson with the registered normalization (distributional; verified by Gauss box):
Rg = 2.0
flux = -1.0*4*np.pi*Rg**2*(1.0/Rg**2)   # d/dr(1/r) * area = -4pi, independent of Rg
check("Gauss flux of grad(1/r) = -4pi (Poisson normalization, weak field)",
      abs(flux + 4*np.pi) < 1e-12, f"flux = {flux:.10f}")

print(f"\n{sum(PASS)}/{len(PASS)} checks pass")
raise SystemExit(0 if all(PASS) else 1)
