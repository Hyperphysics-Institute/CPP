"""PATCH 2928 — THE REGISTERED PREDICTION c4 -> 0 UNDER FULL
SELF-CONSISTENCY IS REFUTED FOR THE DISPLACEMENT-FIELD FIXED-POINT
CLOSURE, IN BOTH RETURN CONVENTIONS.

Confronts the Patch 2900 registered prediction ("the steady-state
argument ... predicts c4 -> 0 under full self-consistency. That
prediction is registered before the fixed-point code exists, so it can
fail in public.") at its anticipated test: the fixed point of the
displacement map.

MODEL (registered in session chat before execution): the SC closure
solves  delta = eps * amp(y+delta) * u_hat(y+delta)  by fixed-point
iteration (tol 1e-12, divergence-guarded) — the DP's displacement
responds to the retarded CP field at the DP's ACTUAL position. Two
return conventions isolate the modeling fork:
  V1: F = amp(y)   * G(y+delta)   (2900's convention; displacement-only
                                    self-consistency — clean ablation)
  V2: F = amp(y+d) * G(y+delta)   (fully displaced response strength)

PRE-REGISTERED VERDICTS at the SC cancellation point eps*_SC (c = 0):
  CONFIRMED (this closure): |c4(eps*_SC)| < 0.03
  REFUTED   (this closure): |c4(eps*_SC)| > 0.15
  PARTIAL: between.  NO-ZERO: no c = 0 in the convergent region.
  Side prediction (advection amplifies): eps*_SC < 0.0589.

RESULTS (reference config m = 2, r = [1, 12], 480x720):
  V1: eps*_SC = 0.04222   c4(eps*_SC) = -0.923   -> REFUTED
  V2: eps*_SC = 0.02070   c4(eps*_SC) = -0.612   -> REFUTED
  Self-consistency makes the beta^4 pathology WORSE than one-shot
  (-0.373), not better; the c4 = 0 and c = 0 points do not coincide in
  either variant. eps*_SC < 0.0589 in both (side prediction PASS).
  The map's convergence boundary eps_conv ~ 0.0658 is variant-
  independent (same displacement map; internal check PASS) and the
  one-shot eps* = 0.0589 sits barely inside the basin.

SCOPE: refutation applies to the displacement-field fixed-point
closure. The stronger reading of "full self-consistency" — a
travelling steady state with Sea-side (DP-DP) coupling, absent from
this model class — is now sharply separated from displacement closure
and remains the live route for direction (A).

Run: python3 2928_sc_entrainment_c4_confrontation.py   (numpy)
"""
import numpy as np

FAIL = []


def check(name, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        FAIL.append(name)


def geometry_at(px, py, v, c=1.0):
    """Retarded quantities for DPs at arbitrary positions; return leg
    arrives at the CP (origin, t = 0)."""
    y = np.hypot(px, py)
    t2 = -y / c
    A = px - v * t2
    disc = A * A * v * v + (c * c - v * v) * (A * A + py * py)
    s = (A * v + np.sqrt(disc)) / (c * c - v * v)
    d_out = c * s
    t1 = t2 - s
    return d_out, v * t1


def sc_drive(v, eps, m, rmin, rmax, variant, nr=480, nth=720,
             tol=1e-12, itmax=300):
    """Self-consistent entrained drive; returns (drive, iters) or
    (None, iters) on divergence of the fixed-point map."""
    r = np.linspace(rmin, rmax, nr)
    th = np.linspace(0, np.pi, nth)
    R, TH = np.meshgrid(r, th, indexing='ij')
    yx, yp = R * np.cos(TH), R * np.sin(TH)
    w = (R ** 2) * np.sin(TH) * (r[1] - r[0]) * (th[1] - th[0]) * 2 * np.pi
    dx = np.zeros_like(yx)
    dy = np.zeros_like(yp)
    prev = np.inf
    for it in range(itmax):
        px, py = yx + dx, yp + dy
        d_out, cx = geometry_at(px, py, v)
        amp = 1.0 / d_out ** 2
        ux, up = (cx - px) / d_out, (0.0 - py) / d_out
        ndx, ndy = eps * amp * ux, eps * amp * up
        delta = max(np.max(np.abs(ndx - dx)), np.max(np.abs(ndy - dy)))
        if not np.isfinite(delta) or (it > 50 and delta > prev * 1.001
                                      and delta > 1e-6):
            return None, it + 1
        dx, dy = ndx, ndy
        prev = delta
        if delta < tol:
            break
    else:
        return None, itmax
    px, py = yx + dx, yp + dy
    if variant == 'V2':
        d_ret, _ = geometry_at(px, py, v)
    else:
        d_ret, _ = geometry_at(yx, yp, v)
    amp = 1.0 / d_ret ** 2
    yn = np.hypot(px, py)
    return float(np.sum((amp / yn ** m) * (px / yn) * w)), it + 1


def oneshot_drive(v, eps, m=2, rmin=1.0, rmax=12.0, nr=480, nth=720):
    """Verbatim 2900 one-shot model."""
    r = np.linspace(rmin, rmax, nr)
    th = np.linspace(0, np.pi, nth)
    R, TH = np.meshgrid(r, th, indexing='ij')
    yx, yp = R * np.cos(TH), R * np.sin(TH)
    w = (R ** 2) * np.sin(TH) * (r[1] - r[0]) * (th[1] - th[0]) * 2 * np.pi
    d_out, cx = geometry_at(yx, yp, v)
    amp = 1.0 / d_out ** 2
    ux, up = (cx - yx) / d_out, (0.0 - yp) / d_out
    px, py = yx + eps * amp * ux, yp + eps * amp * up
    yn = np.hypot(px, py)
    return float(np.sum((amp / yn ** m) * (px / yn) * w))


BETAS = np.array([0.01, 0.02, 0.03, 0.05, 0.08, 0.10, 0.15, 0.20])
X = np.column_stack([np.ones_like(BETAS), BETAS ** 2, BETAS ** 4])


def cfit(eps, variant, m=2, a=1.0, bnd=12.0, nr=480, nth=720):
    ys = []
    for bb in BETAS:
        d, _ = sc_drive(bb, eps, m, a, bnd, variant, nr, nth)
        if d is None:
            return None
        ys.append(d)
    y = np.array(ys) / BETAS
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    return coef[0], -coef[1] / coef[0], -coef[2] / coef[0]


print("PART A — sanity and O(eps) agreement with the one-shot model")
k0, c0, c40 = cfit(0.0, 'V1')
check("eps = 0 reduces to the base model (k = -15.554, c = 0.200008)",
      abs(k0 + 15.554) < 5e-3 and abs(c0 - 0.200008) < 1e-5)
# SC and one-shot share O(eps): (D_SC - D_os)/eps^2 must be ~constant
b_test = 0.10
diffs = []
for e in (1e-3, 2e-3):
    dsc, _ = sc_drive(b_test, e, 2, 1, 12, 'V1')
    dos = oneshot_drive(b_test, e)
    diffs.append((dsc - dos) / e ** 2)
check("V1 - one-shot vanishes at O(eps): (D_SC-D_os)/eps^2 constant to 1%",
      abs(diffs[0] / diffs[1] - 1) < 0.01)
print(f"    advection term at beta = {b_test}: "
      f"(D_SC-D_os)/eps^2 = {diffs[0]:+.4f}")

print("\nPART B — convergence boundary (variant-independent map)")
bounds = {}
for variant in ('V1', 'V2'):
    lo, hi = 0.05, 0.12
    for _ in range(9):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if cfit(mid, variant) is not None else (lo, mid)
    bounds[variant] = 0.5 * (lo + hi)
    print(f"    {variant}: eps_conv ~ {bounds[variant]:.4f}")
check("eps_conv identical across variants (same displacement map)",
      abs(bounds['V1'] - bounds['V2']) < 2e-3)
check("one-shot eps* = 0.0589 lies inside the SC basin (barely)",
      0.0589 < bounds['V1'])

print("\nPART C — pre-registered confrontation: c4 at the SC "
      "cancellation point")
results = {}
for variant in ('V1', 'V2'):
    lo, hi = 0.005, bounds[variant] * 0.97
    rlo, rhi = cfit(lo, variant), cfit(hi, variant)
    assert rlo is not None and rlo[1] > 0
    if rhi is None or rhi[1] > 0:
        print(f"    {variant}: NO-ZERO in convergent region")
        results[variant] = None
        continue
    for _ in range(14):
        mid = 0.5 * (lo + hi)
        rm = cfit(mid, variant)
        lo, hi = (mid, hi) if (rm is not None and rm[1] > 0) else (lo, mid)
    es = 0.5 * (lo + hi)
    k, c2, c4 = cfit(es, variant)
    results[variant] = (es, k, c4)
    verdict = ("CONFIRMED" if abs(c4) < 0.03
               else "REFUTED" if abs(c4) > 0.15 else "PARTIAL")
    print(f"    {variant}: eps*_SC = {es:.5f}   k = {k:.4f}   "
          f"c = {c2:.1e}   c4(eps*_SC) = {c4:.5f}   -> {verdict}")
check("V1 verdict: REFUTED band (|c4| > 0.15)",
      results['V1'] is not None and abs(results['V1'][2]) > 0.15)
check("V2 verdict: REFUTED band (|c4| > 0.15)",
      results['V2'] is not None and abs(results['V2'][2]) > 0.15)
check("side prediction: eps*_SC < 0.0589 in both variants",
      all(results[v][0] < 0.0589 for v in ('V1', 'V2')))
check("SC is WORSE than one-shot at its cancellation point "
      "(|c4| > 0.373 for V1)", abs(results['V1'][2]) > 0.373)

print("\nPART D — verdict robustness under grid refinement (V1)")
es = results['V1'][0]
r960 = cfit(es, 'V1', nr=960, nth=1440)
print(f"    c4 at eps*_SC(480-grid): 480 -> {results['V1'][2]:.4f}, "
      f"960 -> {r960[2]:.4f}")
check("c4 verdict grid-robust (960-grid value within 15%, same band)",
      abs(r960[2] / results['V1'][2] - 1) < 0.15 and abs(r960[2]) > 0.15)

print("\n" + ("ALL CHECKS PASS" if not FAIL else f"FAILURES: {FAIL}"))
raise SystemExit(1 if FAIL else 0)
