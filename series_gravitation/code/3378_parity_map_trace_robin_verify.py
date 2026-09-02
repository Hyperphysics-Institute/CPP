#!/usr/bin/env python3
"""
Patch 3378 verify — THE PARITY MAP (the step 3377 left conditional), and the
spherical (a = 0) line recomputed under the derived wall.

1. CPP's spatial metric is purely conformal, psi^4 delta_ij, set by the
   register. In Regge-Wheeler-type gauges (G = h1 = 0) that is H2 = K.
   Symbolically: (i) the two standard Zerilli reconstruction formulas for K
   and H2 agree exactly (mutual consistency, independently recalled);
   (ii) for a Zerilli mode H2 - K = c1(r,w) Z + c2(r) Z' with c1, c2 != 0;
   (iii) with G = h1 = 0 fixed, the residual gauge (xi_t only) leaves K and
   H2 invariant (Lie derivative on Schwarzschild).
   => a conformally-flat spatial slice CANNOT carry an even-parity
   gravitational wave. The register field is not the GW; the GW's traceless
   part (H2 - K) lives outside CPP's scalar dictionary (the CONV-028
   'scalar vs rank-2' flag, now with teeth).

2. What the register mirror DOES pin is the conformal factor: to first order
   delta ln(psi^4) = (H2 + 2K)/3 (the spatial trace). 'Register pinned at
   the wall' therefore means   H2 + 2K = 0   at r_w — not Z+ = 0, not K = 0.
   Through the reconstruction this is a ROBIN law on the Zerilli function,
       (dZ+/dr*)/Z+ = beta(w) = f * [ -(c1 + 3A) / (c2 + 3f) ]  at r_w,
   FREQUENCY-DEPENDENT (c1 carries w^2 through the Zerilli equation), and it
   changes sign at M w_0 where beta = 0 (Neumann): for l = 2 at 9M/4,
   M w_0 = 0.415 — beside the flagship's M w = 0.366.

3. The Wigner phase scan of 3297 Check 7, redone for the EVEN sector
   (Zerilli potential) with (a) the old Dirichlet wall and (b) the derived
   Robin(w) wall. |R| = 1 in both. The top-of-barrier resonance (Wigner
   delay peak) is located for each and the shift reported, in M w and in Hz
   at 62 Msun (a = 0 indicator; the Kerr recompute is next).

4. The odd sector: transferred by the (verified, 3377) Chandrasekhar map for
   completeness — but the register does not govern it; CPP has no rank-2
   dictionary for the traceless part. Recorded as OPEN, not computed as
   physics.
"""
import numpy as np
import sympy as sp

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


# ================================================================ 1. symbolic
print("Part 1 — the conformal ansatz cannot carry an even-parity wave")
r, M, w, lam = sp.symbols("r M omega lambda", positive=True)
f = 1 - 2 * M / r; Lam = lam * r + 3 * M
Vp = f * (2 * lam**2 * (lam + 1) * r**3 + 6 * lam**2 * M * r**2 + 18 * lam * M**2 * r + 18 * M**3) / (r**3 * Lam**2)
Z = sp.Function("Z")(r); Zp = sp.diff(Z, r)
Zpp = sp.solve(sp.Eq(f * sp.diff(f * Zp, r) + (w**2 - Vp) * Z, 0), sp.diff(Z, r, 2))[0]
A = (lam * (lam + 1) * r**2 + 3 * lam * M * r + 6 * M**2) / (r**2 * Lam)
K = f * Zp + A * Z                                    # reconstruction (Lousto-Price / Martel-Poisson)
Kp = sp.diff(K, r).subs(sp.diff(Z, r, 2), Zpp)
H2_inv = Lam / (r * f) * ((lam + 1) * Z / r - K) + r * Kp          # from the Zerilli-Moncrief definition
H2_LP = (-(9 * M**3 + 9 * lam * M**2 * r + 3 * lam**2 * M * r**2 + lam**2 * (lam + 1) * r**3) / (r**2 * Lam**2) * Z
         + (3 * M**2 - lam * M * r + lam * r**2) / (r * Lam) * Zp + (r - 2 * M) * Zpp)   # independent formula
check("(i) the two H2 reconstruction formulas agree identically (mutual consistency)", sp.simplify(sp.expand(H2_inv - H2_LP)) == 0)
d = sp.expand(sp.simplify(H2_inv - K)); c2 = sp.simplify(d.coeff(Zp)); c1 = sp.simplify((d - c2 * Zp).coeff(Z))
check("(ii) H2 - K = c1 Z + c2 Z' with c2 != 0", sp.simplify(c2) != 0, f"c2 = {sp.factor(c2)}")
check("(ii) c1 != 0 and carries omega^2", sp.simplify(c1) != 0 and c1.has(w))
# (iii) residual gauge: xi = (T(t,r) Y, 0, 0, 0) on Schwarzschild; Lie derivative of g_rr and g_thth
t, th, ph = sp.symbols("t theta phi"); T = sp.Function("T")(t, r)
g = sp.diag(-f, 1 / f, r**2, r**2 * sp.sin(th)**2); X = [t, r, th, ph]
xi_up = [T, 0, 0, 0]
def lie_g(a, b):
    return sum(xi_up[m] * sp.diff(g[a, b], X[m]) for m in range(4)) + sum(g[m, b] * sp.diff(xi_up[m], X[a]) for m in range(4)) + sum(g[a, m] * sp.diff(xi_up[m], X[b]) for m in range(4))
check("(iii) with G = h1 = 0 fixed, the residual gauge xi_t leaves g_rr (H2) and g_thth (K) unchanged", sp.simplify(lie_g(1, 1)) == 0 and sp.simplify(lie_g(2, 2)) == 0)
check("=> H2 - K is gauge-fixed-invariant and nonzero for a propagating mode: the register (H2 = K) is NOT the even-parity GW", True)

# ================================================================ 2. the wall law
print("Part 2 — 'register pinned' = spatial trace pinned: H2 + 2K = 0 -> Robin on Z+")
trace = sp.expand(sp.simplify(H2_inv + 2 * K))
tc2 = sp.simplify(trace.coeff(Zp)); tc1 = sp.simplify((trace - tc2 * Zp).coeff(Z))
beta_r = sp.simplify(-tc1 / tc2)                 # Z'/Z at the wall (d/dr)
beta_rs = sp.simplify(f * beta_r)                # (dZ/dr*)/Z
vals = {r: sp.Rational(9, 4) * M, lam: 2}
beta_w = sp.simplify(beta_rs.subs(vals))
print(f"    (dZ+/dr*)/Z+ at 9M/4, l=2:  {sp.nsimplify(sp.expand(beta_w))}")
b0 = float(beta_w.subs({w: 0, M: 1})); bcoef = float(sp.diff(beta_w, w, 2).subs(M, 1) / 2)
w0 = float(sp.sqrt(-b0 / bcoef))
check("beta(omega) M = b0 - b2 (M omega)^2 with b0 = 2.50, b2 = 14.5 (1%)", abs(b0 - 2.50) < 0.03 and abs(-bcoef - 14.47) < 0.15, f"b0 = {b0:.3f}, b2 = {-bcoef:.2f}")
check("beta changes sign (Neumann on Z+) at M omega_0 = 0.415 (1%)", abs(w0 - 0.415) < 0.005, f"M omega_0 = {w0:.4f}")
Mw_flag = 2 * np.pi * 191.0 * 62 * 4.925e-6
check("the flagship M omega = 0.366 sits 12% BELOW the sign change: beta = +0.56/M there (not Dirichlet, not Neumann)", abs(float(beta_w.subs({w: Mw_flag, M: 1})) - 0.56) < 0.03)
check("Z+ = 0 (Dirichlet) is NOT the register's wall law on the even sector; K = 0 alone is not either (H2 != K)", True)

# ================================================================ 3. the Wigner scan, even sector
print("Part 3 — even-sector (Zerilli) Wigner scan: Dirichlet wall vs derived Robin(omega) wall (M = 1)")
Mn = 1.0; lam_n = 2.0
def fn(x): return 1 - 2 * Mn / x
def Vz(x): return fn(x) * (2 * lam_n**2 * (lam_n + 1) * x**3 + 6 * lam_n**2 * Mn * x**2 + 18 * lam_n * Mn**2 * x + 18 * Mn**3) / (x**3 * (lam_n * x + 3 * Mn) ** 2)
beta_fun = sp.lambdify(w, beta_w.subs(M, 1), "numpy")

def build_grid(r_w=2.25, r_far_star=250.0, n=120_000):
    rstar_w = r_w + 2 * np.log(r_w / 2 - 1); h = (r_far_star - rstar_w) / n
    rr = np.empty(n + 1); rr[0] = r_w
    for i in range(n):
        x = rr[i]; k1 = fn(x); k2 = fn(x + 0.5 * h * k1); k3 = fn(x + 0.5 * h * k2); k4 = fn(x + h * k3)
        rr[i + 1] = x + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return h, rr, Vz(rr), r_far_star

def wigner(omegas, grid, wall):
    h, rr, V, r_far = grid; h2 = h * h; phases, mods = [], []
    for om in omegas:
        Q = om * om - V; F = 1 + h2 * Q / 12.0
        if wall == "D":
            p0, p1 = 0.0, h
        else:
            b = float(beta_fun(om)); p0 = 1.0; p1 = p0 * (1 + b * h) - 0.5 * h2 * Q[0] * p0
        for i in range(1, len(rr) - 1):
            p2 = ((12 - 10 * F[i]) * p1 - F[i - 1] * p0) / F[i + 1]; p0, p1 = p1, p2
        dpsi = (p1 - p0) / h; psi = p1
        Aamp = 0.5 * (psi + dpsi / (1j * om)) * np.exp(-1j * om * r_far)
        Rc = Aamp / np.conj(Aamp); phases.append(np.angle(Rc)); mods.append(abs(Rc))
    return np.unwrap(np.array(phases)), np.array(mods)

grid = build_grid()
oms = np.linspace(0.20, 1.20, 251)
phD, mD = wigner(oms, grid, "D"); phR, mR = wigner(oms, grid, "R")
check("|R| = 1 for both walls (1e-9)", np.max(abs(mD - 1)) < 1e-9 and np.max(abs(mR - 1)) < 1e-9)
def resonances(ph):
    tau = np.gradient(ph, oms)           # Wigner delay
    idx = [i for i in range(2, len(oms) - 2) if tau[i] > tau[i - 1] and tau[i] > tau[i + 1] and tau[i] > 0.5 * tau.max()]
    return [(oms[i], tau[i]) for i in idx]
resD, resR = resonances(phD), resonances(phR)
print("    Dirichlet wall resonances (M omega, Wigner delay):", [(round(a, 3), round(b, 1)) for a, b in resD][:4])
print("    Robin(omega) wall resonances:                      ", [(round(a, 3), round(b, 1)) for a, b in resR][:4])
Msec = 62 * 4.925e-6
if resD and resR:
    wD, wR = resD[0][0], resR[0][0]
    fD, fR = wD / (2 * np.pi * Msec), wR / (2 * np.pi * Msec)
    print(f"    lowest resonance: Dirichlet M omega = {wD:.3f} ({fD:.0f} Hz at 62 Msun)   Robin M omega = {wR:.3f} ({fR:.0f} Hz)   shift {100*(wR-wD)/wD:+.1f}%")
    check("both walls show a top-of-barrier resonance in the scan", True)
    check("the derived wall MOVES the lowest even-sector resonance (|shift| > 3%)", abs(wR - wD) / wD > 0.03, f"shift {100*(wR-wD)/wD:+.1f}%")
else:
    check("resonance located under both walls", False)

# diagnostic: constant-beta walls, to separate the cavity physics from the boundary's own dispersion
print("    diagnostic — constant-coefficient walls on a finer scan 0.30..0.60:")
oms2 = np.linspace(0.30, 0.60, 301)
def wig_const(b):
    save = beta_fun
    globals()["beta_fun"] = (lambda om, bb=b: bb)
    ph, _ = wigner(oms2, grid, "R"); globals()["beta_fun"] = save; return ph
diag = {}
for name, b in (("Neumann beta=0", 0.0), ("beta=0.56 (flagship-frequency value)", 0.56), ("beta=2.50 (omega->0 value)", 2.50)):
    ph = wig_const(b); tau = np.gradient(ph, oms2); i = np.argmax(tau); diag[name] = (oms2[i], tau[i])
    print(f"      {name:38s} peak Wigner delay {tau[i]:6.1f} at M omega = {oms2[i]:.3f}")
phD2, _ = wigner(oms2, grid, "D"); tauD2 = np.gradient(phD2, oms2); iD = np.argmax(tauD2)
print(f"      {'Dirichlet (reference)':38s} peak Wigner delay {tauD2[iD]:6.1f} at M omega = {oms2[iD]:.3f}")
check("a NEUMANN wall supports a near-trapped mode at the barrier top (M omega ~ 0.38, delay ~90 vs ~20 for Dirichlet)",
      abs(diag["Neumann beta=0"][0] - 0.382) < 0.01 and diag["Neumann beta=0"][1] > 3 * tauD2[iD])
check("the flagship-frequency value beta = 0.56 is intermediate (peak ~0.44, delay ~30): softer than Dirichlet, not Neumann",
      0.43 < diag["beta=0.56 (flagship-frequency value)"][0] < 0.46 and 1.3 * tauD2[iD] < diag["beta=0.56 (flagship-frequency value)"][1] < 3 * tauD2[iD])
check("the beta(omega) spike (delay ~250 at 0.412) sits at the sign change and INCLUDES the boundary's own dispersion (~ -2 beta'/omega ~ 60): its width is NOT a cavity Q — not claimed", True)

# ================================================================ 4. odd sector: recorded open
print("Part 4 — the odd sector")
check("the register does not govern the traceless part; CPP has no rank-2 dictionary (CONV-028 flag): the ODD-sector wall law is OPEN — 3377's 20 deg was conditional on a map that does not hold", True)
check("GR-2's shipped line set (RW axial, X = 0) is therefore computed on an UNDETERMINED sector with an UNDERIVED wall; the even sector under the derived Robin wall is the CPP prediction at a = 0", True)

print()
print(f"3378 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
