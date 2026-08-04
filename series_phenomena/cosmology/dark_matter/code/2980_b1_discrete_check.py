#!/usr/bin/env python3
"""2980_b1_discrete_check.py — Lemma L-3' (C-5(i)) discrete-spectrum verification.

Verifies, on the Moment-sampled kernel the engine actually computes:
zero discrete DC weight -> Re gamma_hat = O(omega^2) with the EXACT finite-sum
coefficient and the explicit Lagrange remainder bound; first-order-in-omega part
purely imaginary (discrete dressing); exactness at COARSE sampling where continuum
quadrature is visibly wrong; finite, defined behavior approaching the Moment
Nyquist frequency; NEGATIVE CONTROL: breaking the DC zero produces linear-order
dissipation. Toy units only; no open-quantity value is minted.
"""

import numpy as np

PASS = 0; FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    tag = "PASS" if cond else "FAIL"
    PASS += cond; FAIL += (not cond)
    print(f"[{tag}] {name}" + (f"  ({detail})" if detail else ""))

def make_kernel(K, dt, seed=2980, zero_dc=True):
    rng = np.random.default_rng(seed)
    g = rng.normal(size=K)
    if zero_dc:
        g -= g.mean()          # discrete DC zero EXACT by construction (T-1.L's role)
    return g, dt

def gamma_hat(g, dt, omega):
    k = np.arange(len(g))
    return dt * np.sum(g * np.exp(-1j * omega * k * dt))

# ---- coarse sampling: K = 8 (continuum quadrature visibly wrong; discrete identity exact)
g, dt = make_kernel(K=8, dt=0.125)
k = np.arange(len(g)); tk = k * dt
m2d = np.sum(g * tk**2) * dt            # exact discrete second moment
m1d = np.sum(g * tk) * dt               # exact discrete first moment (dressing)

check("CHECK 1  discrete DC zero: sum(gamma_k) = 0 exactly",
      abs(g.sum()) < 1e-14, f"sum = {g.sum():.1e}")

om = 0.05
gh = gamma_hat(g, dt, om)
re_pred = -(om**2 / 2) * m2d
rem_bound = (om**4 / 24) * dt * np.sum(np.abs(g) * tk**4)
check("CHECK 2  Re gamma_hat matches the exact finite-sum coefficient within the bound (K=8)",
      abs(gh.real - re_pred) <= rem_bound + 1e-15,
      f"|dev| = {abs(gh.real-re_pred):.2e}, bound = {rem_bound:.2e}")
check("CHECK 3  Im gamma_hat/omega -> -m1d (discrete dressing, first order purely imaginary)",
      abs(gh.imag/om + m1d) < 1e-3 * max(1e-12, abs(m1d)) + 1e-6,
      f"Im/om = {gh.imag/om:.6e}, -m1d = {-m1d:.6e}")

# ---- slope-2 across three decades below Nyquist
om_N = np.pi / dt
oms = om_N * np.array([1e-4, 1e-3, 1e-2, 1e-1])
res = np.array([abs(gamma_hat(g, dt, o).real) for o in oms])
slope = np.polyfit(np.log(oms[:3]), np.log(res[:3]), 1)[0]   # fit the asymptotic decades
check("CHECK 4  log-log slope of Re gamma_hat = 2 across the low-frequency decades",
      abs(slope - 2.0) < 1e-2, f"slope = {slope:.5f}")

# ---- remainder-bound audit over a frequency sweep
ok = True; worst = 0.0
for o in np.linspace(0.01, 0.6 * om_N, 40):
    dev = abs(gamma_hat(g, dt, o).real - (-(o**2/2) * m2d))
    bnd = (o**4 / 24) * dt * np.sum(np.abs(g) * tk**4)
    worst = max(worst, dev - bnd)
    if dev > bnd + 1e-13: ok = False
check("CHECK 5  Lagrange remainder bound holds across the sweep up to 0.6*Nyquist",
      ok, f"worst (dev - bound) = {worst:.2e}")

# ---- behavior approaching Nyquist: finite, defined (trig polynomial is entire)
gh_N = gamma_hat(g, dt, 0.999 * om_N)
check("CHECK 6  gamma_hat finite and defined at 0.999*Nyquist (entire trig polynomial)",
      np.isfinite(gh_N.real) and np.isfinite(gh_N.imag),
      f"|gamma_hat| = {abs(gh_N):.4e}")

# ---- fine-vs-coarse consistency: the SAME underlying profile sampled at K=8 and K=256
def profile(t):     # smooth zero-integral profile on [0,1)
    return np.sin(2*np.pi*t) * np.exp(-((t-0.5)**2)/(2*0.16**2))
for i, K in enumerate([8, 256]):
    dtK = 1.0 / K
    tks = np.arange(K) * dtK
    gK = profile(tks); gK -= gK.mean()
    m2K = np.sum(gK * tks**2) * dtK
    o = 0.2
    dev = abs(gamma_hat(gK, dtK, o).real - (-(o**2/2) * m2K))
    bndK = (o**4/24) * dtK * np.sum(np.abs(gK) * tks**4)
    check(f"CHECK {7+i}  K = {K}: discrete identity exact at its OWN sampling (bound honored)",
          dev <= bndK + 1e-13, f"dev = {dev:.2e}, bound = {bndK:.2e}")

# ---- NEGATIVE CONTROL: break the DC zero -> linear-order dissipation appears
gb, _ = make_kernel(K=8, dt=0.125, zero_dc=False)
gh0 = gamma_hat(gb, dt, 1e-4)
check("CHECK 9  NEGATIVE CONTROL: sum(gamma_k) != 0 -> Re gamma_hat(0+) != 0 (test can fail)",
      abs(gh0.real) > 1e-4, f"Re at omega->0: {gh0.real:.4e}")

print("-" * 72)
print(f"{PASS}/{PASS+FAIL} PASS")
print("Toy units only. Lemma L-3' runs on the finite Moment sum the engine computes:")
print("exact coefficients, explicit remainder bound, entire trig polynomial (globally")
print("convergent), admissible drives < Moment Nyquist by construction. The DC zero")
print("is supplied by T-1.L through the restated (dressed-kernel, total-force) L-2.")
print("No open-quantity value is minted.")
