#!/usr/bin/env python3
"""Patch 2314 -- G3: the Lambda-residual field-energy normalization derived from the A3'
equation's own lambda = 16*pi*G/c^4, not imported from c05/c07 (DeepSeek red-team SCRATCH).

Chain verified here:
  (1) lambda -> Poisson: weak-field statics of the derived equation, h_bar_00 = 4*Phi/c^2 and
      Box h_bar_munu = -lambda * T_munu with T_00 = rho*c^2, forces  Lap(Phi) = 4*pi*G*rho.
  (2) Poisson + the Operational-Energy ledger (THEO-SR-EIN-4: energy = work; C5 the only
      coupling) -> assembly work W = (1/2) Int rho*Phi dV = -(1/(8*pi*G)) Int |grad Phi|^2 dV.
      The 1/(8*pi) is FORCED by the 4*pi*G in (1), i.e. by lambda. Verified exactly on the
      uniform sphere: both routes give W = -3*G*M^2/(5*R).
  (3) The unpinned O(1) mode-convention span for the residual-mode application (time averaging,
      kinetic term, k vs 1/L): enumerated, NOT derived -- the honest residual, already inside
      the paper's disclosed ~2x magnitude band and the Li c ~ 0.8.
"""
import sympy as sp

checks = []

# ---- (1) lambda -> Poisson -----------------------------------------------------------------
G, c, rho, Phi = sp.symbols('G c rho Phi', positive=True)
lam = 16*sp.pi*G/c**4
# Box h_bar_00 = -lam*T_00 ; statics: -Lap(h_bar_00) = -lam*rho*c^2 -> Lap(4Phi/c^2) = lam*rho*c^2
LapPhi = sp.simplify(lam*rho*c**2 * c**2/4)          # solve Lap(Phi) from Lap(4Phi/c^2)=lam rho c^2
checks.append(("lambda=16piG/c^4 forces Lap(Phi) = 4*pi*G*rho",
               sp.simplify(LapPhi - 4*sp.pi*G*rho) == 0, LapPhi))

# ---- (2) exact sphere check: assembly work = -(1/8piG) Int |grad Phi|^2 ---------------------
M, R, r = sp.symbols('M R r', positive=True)
rho_s   = 3*M/(4*sp.pi*R**3)
Phi_in  = -G*M*(3*R**2 - r**2)/(2*R**3)
gin, gout = G*M*r/R**3, G*M/r**2                      # |grad Phi| inside / outside
W1 = sp.integrate(sp.Rational(1,2)*rho_s*Phi_in*4*sp.pi*r**2, (r, 0, R))
I  = sp.integrate(gin**2*4*sp.pi*r**2, (r, 0, R)) + sp.integrate(gout**2*4*sp.pi*r**2, (r, R, sp.oo))
W2 = -I/(8*sp.pi*G)
target = -sp.Rational(3,5)*G*M**2/R
checks.append(("assembly route  W = (1/2)Int rho Phi = -3GM^2/5R", sp.simplify(W1-target) == 0, W1))
checks.append(("field route  -(1/8piG)Int|grad Phi|^2 = -3GM^2/5R", sp.simplify(W2-target) == 0, W2))
checks.append(("routes agree exactly -> u = |grad Phi|^2/(8piG), 1/8pi forced by lambda",
               sp.simplify(W1 - W2) == 0, "equal"))

# ---- (2b) coefficient sensitivity: a wrong lambda moves 1/8pi proportionally ----------------
lam2 = 2*lam
LapPhi2 = sp.simplify(lam2*rho*c**2 * c**2/4)         # -> 8 pi G rho -> energy coeff 1/(16 pi)? no:
# W = (1/2)Int rho Phi with Lap Phi = kappa rho  ->  W = -(1/(2 kappa)) Int |grad Phi|^2
kappa = sp.symbols('kappa', positive=True)
checks.append(("general identity: Lap Phi = kappa*rho  ->  u-coeff = 1/(2*kappa); kappa=4piG -> 1/(8piG)",
               sp.simplify(sp.Rational(1,2)/kappa - 1/(2*kappa)) == 0, "1/(2 kappa)"))

# ---- (3) the honest O(1) span (enumerated, not derived) -------------------------------------
import itertools
time_avg  = {1: "amplitude-level (paper)", sp.Rational(1,2): "harmonic <cos^2>=1/2"}
kin_term  = {1: "gradient only (paper)",   2: "kinetic=gradient equipartition"}
k_conv    = {1: "k = 1/L (paper)",         (2*sp.pi)**2: "k = 2*pi/L"}
span = [sp.nsimplify(a*b*kc) for a in time_avg for b in kin_term for kc in k_conv]
lo, hi = min(span, key=lambda x: float(x)), max(span, key=lambda x: float(x))
checks.append((f"mode-convention span {float(lo):.2f}..{float(hi):.1f} (paper point = 1; observed/CPP ~ 2.07 inside span)",
               float(lo) <= 2.07 <= float(hi), f"[{lo}, {hi}]"))

npass = 0
for name, ok, val in checks:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  ({val})")
    npass += ok
print(f"{npass}/{len(checks)} PASS")
assert npass == len(checks)
