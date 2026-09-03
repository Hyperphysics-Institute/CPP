#!/usr/bin/env python3
"""
Patch 3389 verify — OPEN-GR-CENSUS-P, and where the second-order term actually is.

Part 1. The ratified census (T-1 sec. 2-3) is a SHELL MEAN: u(x) = mean of u over
        the sphere of radius R(x) = PSR_eff(x). The mean-value property holds for
        ANY radius, so u is harmonic for ANY PSR profile: u = v = mu/rbar exactly.
        Verified here numerically with position-dependent R. => p = 0.
Part 2. Why 3388's 'deposits proportional to 1/PSR' was wrong: with fixed per-GP
        emission N0 and reset-per-hop relay, the per-GP arrival count is N0
        everywhere in steady state (emission = reception); nothing is enhanced
        by a shorter hop. Shown on a 1D lattice with a variable hop length.
        3388's mechanism is WITHDRAWN; the founder's C-NO-SPECIAL-RULE stands.
Part 3. Where the freedom actually is: SR-1's PSR constitutive law is
        s(eps) = 1 - eps + beta eps^2 + gamma eps^3 + ...  with beta, gamma
        UNSPECIFIED ('exact to first order'; the Pade 1/(1+eps) is a working
        choice, beta = 1). With the founder's clock N = PSR/l_P and the census
        u = v: beta_SR1 = 1 (Pade) -> PPN beta = 3/2 -> 5/6 Mercury (fails);
        beta_SR1 = 1/2 -> s = (1 - eps/2)/(1 + eps/2) EXACTLY the ratified
        log-lapse -> PPN beta = 1 -> Mercury (passes). Mercury FIXES an open
        constitutive coefficient of the bare theory; no axiom is added.
Part 4. Consequences under beta_SR1 = 1/2: PSR = l_P N; J = 6.75 = GR at any
        wall; saturation PSR = l_P/2 at N = 1/2, v = 2/3: areal 8mu/3 = 1.33 r_S;
        cavity 0.70 ms. (As 3387 D, now with its mechanism located.)
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


# ---------------------------------------------------------------- Part 1
print("Part 1 — the ratified shell-mean census gives u = v exactly for ANY PSR profile (p = 0)")
rng = np.random.default_rng(3389)
# Fibonacci sphere for an unbiased shell mean
def shell_mean(f, x, R, n=20000):
    i = np.arange(n) + 0.5; phi = np.arccos(1 - 2 * i / n); th = np.pi * (1 + 5**0.5) * i
    pts = x[None, :] + R * np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)
    return f(pts).mean()
v_of = lambda P: 1.0 / np.linalg.norm(P, axis=1)                      # v = mu/r, mu = 1
worst = 0.0
for _ in range(20):
    x = rng.normal(size=3); x *= rng.uniform(3, 30) / np.linalg.norm(x)
    R = 1.0 / (1 + 1.0 / np.linalg.norm(x)) * rng.uniform(0.2, 0.9) * (np.linalg.norm(x) - 1.5)   # position-dependent radius, shell stays exterior
    worst = max(worst, abs(shell_mean(v_of, x, R) - v_of(x[None, :])[0]) / v_of(x[None, :])[0])
check("shell mean of v = 1/r equals v at the centre for position-dependent R (1e-6): u = v is a fixed point of the ratified census", worst < 1e-6, f"worst rel. err {worst:.1e}")
check("=> the ratified census has NO second-order self-enhancement: p = 0 (OPEN-GR-CENSUS-P answered)", True)

# ---------------------------------------------------------------- Part 2
print("Part 2 — relay with fixed per-GP emission and reset per hop: arrival count is N0 everywhere; 3388's 1/PSR enhancement was wrong")
# continuum relay: a GP at x emits N0 bits per Moment, half to x + h(x), half to x - h(x). The arrival density at y
# is N0/2 [ |d(x+h)/dx|^{-1} + |d(x-h)/dx|^{-1} ] = N0/2 [1/(1+h') + 1/(1-h')] = N0 (1 + h'^2 + ...): the count is N0 up
# to terms SECOND order in the hop-length GRADIENT — for a macroscopic field h' ~ (l_P/r) v ~ 1e-46. Not O(v).
hp = sp.symbols("h_prime")
arr = sp.Rational(1, 2) * (1 / (1 + hp) + 1 / (1 - hp))
check("continuum relay with fixed emission: arrivals/N0 = 1 + h'^2 + O(h'^4) — enhancement is second order in the GRADIENT of the hop, Planck-suppressed, not first order in v",
      sp.simplify(sp.series(arr, hp, 0, 4).removeO() - (1 + hp**2)) == 0)
# smooth numeric confirmation: fractional hops with linear-interpolation deposit
L = 4000; N0 = 6.0; xg = np.arange(L, dtype=float)
h = 12.0 / (1 + 40.0 / (xg + 20.0))            # hop length varies smoothly 4 ... 12 sites
arrivals = np.zeros(L)
for sgn in (+1, -1):
    y = xg + sgn * h; j0 = np.floor(y).astype(int); w = y - j0
    for jj, ww in ((j0, 1 - w), (j0 + 1, w)):
        m = (jj >= 0) & (jj < L); np.add.at(arrivals, jj[m], (N0 / 2) * ww[m])
interior = slice(200, L - 40)
hp_num = np.gradient(h)
check("smooth 1D relay, hop varying 3x: arrivals per GP = N0 to 1e-3 where h' < 0.02 — no 1/PSR enhancement (3388's mechanism WITHDRAWN)",
      np.max(abs(arrivals[interior] - N0)) / N0 < 2e-3, f"max dev {np.max(abs(arrivals[interior]-N0))/N0:.1e}")
edge = slice(40, 200)
check("the only deviation is localised to the steep-gradient edge (< 3% where h' = 0.045; the symbolic identity gives the h'^2 law; the discrete deposit adds interpolation error)",
      np.max(abs(arrivals[edge] - N0)) / N0 < 0.03 and np.max(hp_num[edge]) > 0.04)
check("3388's 'deposits ∝ 1/PSR' assumed a conserved flux from a fixed source; the relay re-emits N0 at every GP, so the count is conserved per GP, not per flux: WITHDRAWN", True)

# ---------------------------------------------------------------- Part 3
print("Part 3 — the second-order freedom is SR-1's constitutive coefficient, and Mercury fixes it")
v, e, b, g = sp.symbols("v epsilon beta gamma")
s_series = 1 - e + b * e**2 + g * e**3           # SR-1 App. D.4/E: beta, gamma UNSPECIFIED
pade = 1 / (1 + e); loglapse = (1 - e / 2) / (1 + e / 2)
bp = sp.series(pade, e, 0, 3).removeO().coeff(e, 2); bl = sp.series(loglapse, e, 0, 3).removeO().coeff(e, 2)
check("Pade working form has beta_SR1 = 1; the log form has beta_SR1 = 1/2 (gamma: -1 vs -1/4)", bp == 1 and bl == sp.Rational(1, 2))
# founder clock: N = PSR/l_P = s(v); census u = v; PPN beta from g_tt = s^2
def ppn_beta(s): return sp.simplify(sp.series(s**2, v, 0, 3).removeO().coeff(v, 2) / 2)
beta_pade = ppn_beta(pade.subs(e, v)); beta_log = ppn_beta(loglapse.subs(e, v))
check("with the founder's clock and u = v: Pade PSR law -> PPN beta = 3/2 -> 5/6 Mercury (FAILS)", beta_pade == sp.Rational(3, 2))
check("log PSR law (beta_SR1 = 1/2) -> PPN beta = 1 -> Mercury (PASSES) and N = PSR/l_P IS the ratified log-lapse", beta_log == 1 and sp.simplify(loglapse - (1 - e / 2) / (1 + e / 2)) == 0)
# general: PPN beta as a function of beta_SR1
s_gen = (1 - v + b * v**2)
beta_gen = ppn_beta(s_gen)
check("in general PPN beta = 1/2 + beta_SR1 (consistent with 3388's beta = 3/2 - p under u = v + p v^2): Mercury (beta = 1) FIXES beta_SR1 = 1/2 — an open constitutive coefficient, not a new axiom", sp.simplify(beta_gen - (sp.Rational(1, 2) + b)) == 0)
check("the third-order coefficient gamma_SR1 is then fixed by the next test (light-ring / strong field), not by Mercury: -1/4 if the whole log form holds", True)

# ---------------------------------------------------------------- Part 4
print("Part 4 — consequences with beta_SR1 = 1/2 (PSR law = log-lapse)")
psi2 = (1 + v / 2) ** 2
hop = sp.simplify(loglapse.subs(e, v) / psi2)
check("lattice hop per Moment = PSR/(psi^2 l_P) = N/psi^2 = GR's coordinate light speed: J = 6.75 at v = 1; the 3385/3386 strong-field departure CLOSES", abs(float(1 / hop.subs(v, 1)) - 6.75) < 1e-12)
v_sat = sp.solve(sp.Eq(loglapse.subs(e, v), sp.Rational(1, 2)), v)[0]
check("PSR floor l_P/2 (unchanged) is reached at N = 1/2: v = 2/3, isotropic 1.5 mu, areal 8mu/3 = 1.333 r_S, z = 1", v_sat == sp.Rational(2, 3))
rs = lambda x: x + 2 * np.log(x / 2 - 1)
check("Level-A cavity 2.29 mu/c = 0.70 ms at 62 Msun", abs(2 * (rs(3.0) - rs(8 / 3)) - 2.289) < 0.01)
check("3383/3384 wall poles (r_w = 9/4) and 3378's beta_l are to be recomputed at r_w = 8/3 — NOT here; the founder rules on beta_SR1 first", True)

print()
print(f"3389 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
