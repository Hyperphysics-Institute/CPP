#!/usr/bin/env python3
"""Patch 2529 verify — NB-T2-1 f_hTe pre-registration checks.

Checks (all pre-registration arithmetic; NO dial derivation performed here):
  1. Conservation-lock algebra (sympy): n(eDP)=n(qDP), n(hDP-A)=n(hDP-B)=N-n_q; f_hTe = 1-x; ceiling 1/2.
  2. T-2 band reproduction: B = (pi/96)*c_pack*phi^3*(r_c/l_unit)^3 in [0.678, 0.959] for c_pack in [1, sqrt2].
  3. Pass-window transposition: f = T1/B-edges -> [0.466, 0.659]; reachable intersection with ceiling -> [0.466, 0.500].
  4. Survival condition on the dial: x in [0.500, 0.534].
  5. Null-baseline trap: f=1/2 reproduces T1 at c_pack ~ 1.318 in [1, sqrt2].
  6. Fence position: 1/sqrt5 = 0.4472 < 0.466 (below the pass window).
  7. D-band mappings for a derived f (overlap logic as inequalities).
"""
import math
import sympy as sp

ok = True
def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and cond

# --- 1. Lock algebra (sympy) ---
N, nq = sp.symbols('N n_q', positive=True)
n_qDP = nq
n_hA = N - nq            # +qCP budget: n(qDP)+n(hDP-A)=N
n_eDP = N - n_hA         # -eCP budget: n(eDP)+n(hDP-A)=N
n_hB = N - nq            # by the same subtraction on the -qCP/+eCP budgets
check("lock: n(eDP) == n(qDP)", sp.simplify(n_eDP - n_qDP) == 0)
check("lock: n(hDP-A) == n(hDP-B) == N - n_q", sp.simplify(n_hA - n_hB) == 0)
total_CPs = 2*(n_qDP + n_eDP + n_hA + n_hB)   # 2 CPs per pair
check("lock: total CPs == 4N", sp.simplify(total_CPs - 4*N) == 0)
x = sp.symbols('x', positive=True)            # x = n_q/N
f_hTe = sp.together((2*2*(N - nq)) / (4*N)).subs(nq, x*N)  # hybrid-resident CP fraction
check("f_hTe == 1 - x", sp.simplify(f_hTe - (1 - x)) == 0)
check("ceiling: f_hTe <= 1/2 for x >= 1/2 (floor + registered skew direction)",
      sp.simplify(f_hTe.subs(x, sp.Rational(1, 2))) == sp.Rational(1, 2))

# --- 2. T-2 band ---
phi = (1 + math.sqrt(5)) / 2
r_c, l_unit = 1.0, 0.589
form = (math.pi / 96) * phi**3 * (r_c / l_unit)**3
B_lo, B_hi = form * 1.0, form * math.sqrt(2)
check(f"T-2 band [{B_lo:.3f}, {B_hi:.3f}] reproduces 2527's [0.678, 0.959]",
      abs(B_lo - 0.678) < 0.001 and abs(B_hi - 0.959) < 0.001)
check("phi^3 == 2 + sqrt5 (registered provenance of sqrt5)", abs(phi**3 - (2 + math.sqrt(5))) < 1e-12)

# --- 3. Pass window and reachable intersection ---
T1, dT1 = 0.4468, 0.0054
f_lo, f_hi = T1 / B_hi, T1 / B_lo
check(f"pass window [{f_lo:.3f}, {f_hi:.3f}] matches 2527's pre-stated 0.466-0.659",
      abs(f_lo - 0.466) < 0.001 and abs(f_hi - 0.659) < 0.001)
reach_lo, reach_hi = f_lo, min(f_hi, 0.5)
check(f"reachable intersection with ceiling = [{reach_lo:.3f}, {reach_hi:.3f}] == [0.466, 0.500]",
      abs(reach_lo - 0.466) < 0.001 and abs(reach_hi - 0.500) < 1e-9)

# --- 4. Survival condition on the dial ---
x_hi = 1 - f_lo
check(f"survival: x in [0.500, {x_hi:.3f}] — skew above floor <= {100*(x_hi-0.5):.1f} pct-pts",
      abs(x_hi - 0.534) < 0.001)

# --- 5. Null-baseline trap ---
c_null = T1 / (0.5 * (math.pi / 96) * phi**3 * (r_c / l_unit)**3)
check(f"null baseline f=1/2 reproduces T1 at c_pack = {c_null:.3f}, inside [1, sqrt2]",
      1.0 <= c_null <= math.sqrt(2) and abs(c_null - 1.318) < 0.005)

# --- 6. Fence position ---
inv_sqrt5 = 1 / math.sqrt(5)
check(f"1/sqrt5 = {inv_sqrt5:.4f} lies BELOW the pass window (K1-direction, not a pass)",
      inv_sqrt5 < f_lo)

# --- 7. D-band overlap mappings (inequality logic for a derived f) ---
Ds_lo, Ds_hi = 0.436, 0.458       # D-strong (charter v1.1)
Dd_lo, Dd_hi = 0.30, 0.67         # D-directional
def bands(f):
    mk_lo, mk_hi = f * B_lo, f * B_hi
    d_strong = (mk_lo <= Ds_hi) and (mk_hi >= Ds_lo)          # band overlap
    d_dir = (mk_hi >= Dd_lo) and (mk_lo <= Dd_hi)
    return mk_lo, mk_hi, d_strong, d_dir
# spot checks at the reachable edges and the baseline
for f_test, label in [(0.466, "reachable low edge"), (0.500, "ceiling/baseline")]:
    mk_lo, mk_hi, ds, dd = bands(f_test)
    print(f"       f={f_test:.3f} ({label}): m/k in [{mk_lo:.3f}, {mk_hi:.3f}]  D-strong-overlap={ds}  D-dir={dd}")
check("both reachable edges overlap the D-strong band (so a derived in-window f is decision-relevant)",
      bands(0.466)[2] and bands(0.500)[2])

print("\nALL CHECKS PASS" if ok else "\nCHECK FAILURES PRESENT")
raise SystemExit(0 if ok else 1)
