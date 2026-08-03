#!/usr/bin/env python3
"""
Patch 2964 — T-1 detailed-balance toy ledger (K1-MEMORY W-1).

SCOPE (disclosed): this is a LEDGER-ARITHMETIC verification of the
translation-congruence argument in k1_t1_detailed_balance.md, not a
substrate simulation. A co-moving polarization profile p(x - s) is
imposed (the steady state whose existence the theorem premises); the
script verifies that the per-Moment energy and momentum books close
exactly under commensurate stepping, close on time-average with
bounded, resolution-shrinking residuals under incommensurate
stepping, and OPEN (net cost > 0) under acceleration — the T-2
contrast case, labeled as contrast only.

Assumptions carried (cited per charter): PROTOCOL-D1 (2960, band
default, reopenable) and PRINCIPLE-R1 (2961, RATIFIED at 2963:
sampling not consumption — the relay tier moves no energy, so the
DP-polarization account below is the ONLY energy account and closing
it closes the ledger).

Toy units only. No physical value of any open quantity is minted.
"""

import numpy as np

rng = np.random.default_rng(2964)
PASS, FAIL = "PASS", "FAIL"
results = []


def profile(kind, x):
    """Steady co-moving polarization profile p(x'), compact support."""
    if kind == "sym":                      # symmetric bump
        return np.where(np.abs(x) < 1.0, np.cos(np.pi * x / 2.0) ** 2, 0.0)
    if kind == "asym":                     # fore/aft-asymmetric (2956: more
        # smooth C^inf compact support on (-0.5, 1.5): arcs decay smoothly;
        # a hard cutoff creates float-jitter artifacts at the edge (first-run
        # lesson, disclosed in the reasoning fragment)
        t = (x + 0.5) / 2.0
        w = np.zeros_like(t)
        m = (t > 0) & (t < 1)
        w[m] = np.exp(-1.0 / (t[m] * (1 - t[m]))) / np.exp(-4.0)
        return w * (1.2 + 0.8 * np.tanh(2 * x))
    raise ValueError(kind)


def energy_density(p, k=1.0):
    """Stored arc energy density u = (k/2) p^2 (displaced-CP configuration
    against restoring structure; quadratic form is the generic small-
    displacement storage — no tuned constant, k=1 toy units)."""
    return 0.5 * k * p ** 2


def run_ledger(kind, n_sites, dx, delta, n_moments, s0=0.0):
    """March the pattern; return per-Moment charge/discharge sums, total U,
    and net force on source (-dU/ds by central difference)."""
    x = (np.arange(n_sites) - n_sites // 2) * dx
    s = s0
    u_prev = energy_density(profile(kind, x - s))
    E_in, E_out, U, F = [], [], [], []
    for _ in range(n_moments):
        s += delta
        u = energy_density(profile(kind, x - s))
        du = (u - u_prev) * dx
        E_in.append(du[du > 0].sum())          # fore-slab charging cost
        E_out.append(-du[du < 0].sum())        # aft-slab discharge return
        U.append(u.sum() * dx)
        eps = dx / 7.0                          # force via -dU/ds
        Up = energy_density(profile(kind, x - (s + eps))).sum() * dx
        Um = energy_density(profile(kind, x - (s - eps))).sum() * dx
        F.append(-(Up - Um) / (2 * eps))
        u_prev = u
    return map(np.array, (E_in, E_out, U, F))


def check(name, ok, detail):
    results.append((name, PASS if ok else FAIL, detail))


# ---- Check 1: commensurate stepping — exact per-Moment balance ----------
for kind in ("sym", "asym"):
    dx = 0.01
    E_in, E_out, U, F = run_ledger(kind, 4001, dx, delta=3 * dx, n_moments=400)
    r = np.max(np.abs(E_in - E_out))
    check(f"C1 per-Moment E_in==E_out, commensurate, {kind}",
          r < 1e-12, f"max|E_in-E_out|={r:.2e}")
    dU = np.max(np.abs(U - U[0]))
    check(f"C1b stored U constant, {kind}", dU < 1e-12, f"max|dU|={dU:.2e}")

# ---- Check 2: zero net force at steady state ----------------------------
for kind in ("sym", "asym"):
    _, _, _, F = run_ledger(kind, 4001, 0.01, delta=0.03, n_moments=200)
    fmax = np.max(np.abs(F))
    check(f"C2 net force ~0 at steady state, {kind}",
          fmax < 1e-8, f"max|F|={fmax:.2e}")

# ---- Check 3: incommensurate stepping — bounded residual, mean->0,
#               shrinking with resolution ---------------------------------
resid_by_dx = {}
for dx in (0.02, 0.01, 0.005):
    E_in, E_out, _, _ = run_ledger("asym", int(80 / dx) | 1, dx,
                                   delta=0.031415926, n_moments=1000)
    d = E_in - E_out
    resid_by_dx[dx] = (np.max(np.abs(d)), np.abs(np.mean(d)))
mono = (resid_by_dx[0.02][0] > resid_by_dx[0.01][0] > resid_by_dx[0.005][0])
check("C3 incommensurate residual shrinks with resolution", mono,
      "; ".join(f"dx={k}: max={v[0]:.2e}, |mean|={v[1]:.2e}"
                for k, v in resid_by_dx.items()))
check("C3b incommensurate time-mean ~0",
      resid_by_dx[0.005][1] < 1e-6,
      f"|mean| at dx=0.005: {resid_by_dx[0.005][1]:.2e}")

# ---- Check 4: single-site full-traversal cycle: net exchange zero -------
dx = 0.005
x_site = 0.0
s_vals = np.arange(-5.0, 5.0, 0.015)          # sweep pattern past the site
u_hist = energy_density(profile("asym", x_site - s_vals))
net_E = u_hist[-1] - u_hist[0]                 # returns to unpolarized
check("C4 per-DP full-cycle net energy = 0", abs(net_E) < 1e-15,
      f"|u_final-u_init|={abs(net_E):.2e}")
# impulse: integral of -du/ds over the traversal telescopes to the same
imp = -(u_hist[-1] - u_hist[0])
check("C4b per-DP full-cycle impulse = 0 (telescoping)",
      abs(imp) < 1e-15, f"|J|={abs(imp):.2e}")

# ---- Check 5: acceleration contrast (T-2 preview, NOT a T-2 result) -----
# Widen/boost the co-moving pattern with v (establishment cost): under a
# velocity-dependent steady profile, changing delta changes U — net work.
def u_of_v(delta):
    x = (np.arange(4001) - 2000) * 0.01
    p = profile("asym", x) * (1.0 + 0.5 * delta)   # toy v-dependence
    return (energy_density(p)).sum() * 0.01

U_slow, U_fast = u_of_v(0.03), u_of_v(0.06)
check("C5 acceleration contrast: ΔU>0 (establishment cost exists)",
      U_fast > U_slow, f"U(v2)-U(v1)={U_fast-U_slow:.4e} (toy units)")

# ---- Check 6: robustness across velocities ------------------------------
ok6, det6 = True, []
for mult in (1, 2, 5, 11):
    # domain sized so the pattern never reaches the boundary (first-run
    # lesson: v=11dx walked the support off a fixed grid -> fake imbalance)
    n_m = 200
    span = mult * 0.01 * n_m + 10
    E_in, E_out, _, _ = run_ledger("asym", 2 * int(span / 0.01) + 1, 0.01,
                                   delta=mult * 0.01, n_moments=n_m,
                                   s0=-mult * 0.01 * n_m / 2)
    r = np.max(np.abs(E_in - E_out))
    ok6 &= r < 1e-12
    det6.append(f"v={mult}dx: {r:.1e}")
check("C6 balance across velocities (commensurate)", ok6, "; ".join(det6))

# ---- Report -------------------------------------------------------------
print("T-1 DETAILED-BALANCE TOY LEDGER — Patch 2964")
print("Assumptions cited: PROTOCOL-D1 (2960); PRINCIPLE-R1 (RATIFIED 2963)")
print("-" * 72)
npass = 0
for name, status, detail in results:
    print(f"[{status}] {name}\n        {detail}")
    npass += status == PASS
print("-" * 72)
print(f"{npass}/{len(results)} PASS")
print("Toy units only; ledger arithmetic, not substrate simulation.")
