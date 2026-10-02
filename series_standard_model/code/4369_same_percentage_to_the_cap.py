#!/usr/bin/env python3
"""Patch 4369 - the founder's ruling (2 Oct 2026): the PSR's rate of shrinking changes naturally at the
radius where the GPs enclosed by the PSR equal N, the DI-bit count every GP emits per Moment (the
count reset each Moment, equalised by DI-bit migration at the end of the PCD cycle).

Reading TESTED here (Claude's, conditional; the founder said only that the pace CHANGES at n = N):
below that point the PSR shrinks by the same percentage per unit of stress, PSR = PSR_inf * exp(-eps),
and the n = N point is R-DIBIT-COUNT-AT-FLOOR.  Consequences for a non-spinning mass m (G = c = 1), isotropic r:
  1. where the cap sits, as a function of n_inf/N;
  2. whether the photon sphere lies outside the cap (then the shadow is the exponential metric's);
  3. the shadow and the eikonal ringdown frequency against Schwarzschild;
  4. the ringdown shift against the GW250114 box; 5. the throat (no strict horizon).
"""
import sympy as sp
import math
print(__doc__)

m, r = sp.symbols('m r', positive=True)
lapse = sp.exp(-m / r)                 # one PSR for clocks and rulers: g00 = -q^2, g_ij = q^-2 delta
areal = r * sp.exp(m / r)

# 1-2. the cap and the photon sphere
print("1-2. Cap at n = N:  q_cap = (N/n_inf)^(1/3),  eps_cap = (1/3) ln(n_inf/N),  isotropic r_cap = m/eps_cap")
r_ph = 2 * m                            # d(areal/lapse)/dr = 0  (4365)
eps_ph = sp.Rational(1, 2)
print(f"   photon sphere: r = 2m, eps = 1/2, q = e^-1/2 = {math.exp(-0.5):.4f}")
print(f"   photon sphere lies OUTSIDE the cap iff eps_cap > 1/2, i.e. n_inf/N > e^1.5 = {math.exp(1.5):.3f}")
for ratio, label in ((8, "corpus floor l_P/2 (4356: n_inf/N = 8; Claude's identification, not the founder's number)"),
                     (4, "illustrative n_inf/N = 4 (cap outside the photon sphere)")):
    ec = math.log(ratio) / 3
    rc = 1 / ec
    print(f"   n_inf/N = {ratio}: q_cap = {ratio**(-1/3):.4f}, eps_cap = {ec:.4f}, cap at r = {rc:.4f} m,"
          f" areal {rc*math.exp(ec):.4f} m   [{label}]")

# 3. shadow and eikonal ringdown
b_exp = float((areal / lapse).subs(r, r_ph) / m)        # 2e
b_gr = 3 * math.sqrt(3)
print(f"\n3. shadow (critical impact parameter): exponential {b_exp:.4f} m vs Schwarzschild {b_gr:.4f} m  ({100*(b_exp/b_gr-1):+.2f}%)")
print(f"   eikonal ringdown, omega_R ~ 1/b_c: exponential/Schwarzschild = {b_gr/b_exp:.4f}  ({100*(b_gr/b_exp-1):+.2f}%)")
# Lyapunov (damping) exponent for a static metric ds^2 = -A dt^2 + B dr^2 + C dOmega^2 (isotropic: B = q^-2, C = areal^2)
A = lapse**2; Bm = lapse**-2; C = areal**2
V = A / C                                                # photon potential (per L^2)
lam = sp.sqrt(-sp.diff(V, r, 2) / (2 * Bm * V) * A)     # standard: lambda = sqrt(-V''/(2 V) * A/B) at r_ph
lam_exp = float(lam.subs(r, r_ph).subs(m, 1))
lam_gr = 1 / (3 * math.sqrt(3))                          # Schwarzschild eikonal damping
print(f"   eikonal damping (Lyapunov) exponential {lam_exp:.5f}/m vs Schwarzschild {lam_gr:.5f}/m  ({100*(lam_exp/lam_gr-1):+.1f}%)")
print("   Non-spinning eikonal estimate only: LIGO remnants spin (chi ~ 0.7), and no spinning exponential solution is on file.")

# 4. the GW250114 box (conv042 L33; 3668): f220 = 247 +- 6 Hz (+-2.4%), damping (-15, +17)%
f_shift = b_gr / b_exp - 1
print(f"\n4. GW250114 box: df +-2.4%, dtau (-15, +17)%.  Eikonal non-spinning shift {100*f_shift:+.1f}% in frequency"
      f" = {abs(f_shift)/0.024:.1f} box-widths outside; damping {100*(lam_exp/lam_gr-1):+.1f}% (inside).")
print("   A live risk for the steady-percentage-to-the-cap reading, NOT a computed failure: no spin (chi_f = 0.68),")
print("   eikonal only, and CPP's tensor-wave operator on this exterior is not derived (4369 critic).")

# 5. no strict horizon: the exponential exterior has a throat
amin = sp.N(sp.minimum(areal.subs(m, 1), r, sp.Interval.open(0, sp.oo)), 6)
print(f"\n5. Exponential exterior: the areal radius has a minimum (throat) {amin} m at isotropic r = m; the lapse")
print("   vanishes only as r -> 0, at infinite proper distance and infinite tortoise time: black in practice,")
print("   with no strict horizon (4369 critic). The draft's DRAIN-core redshift figure is withdrawn (it used a")
print("   physical core size as an isotropic radius, inside the capped region where this exterior does not apply).")
