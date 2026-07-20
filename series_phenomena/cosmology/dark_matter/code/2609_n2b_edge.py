#!/usr/bin/env python3
"""
PATCH 2609 -- N2-B-EDGE EXECUTION under n2b_edge_prereg.md (2608) ONLY.
Analytic model E-A (zero-freedom well + transit-shed condition, L_int declared band)
+ the declared high-v grid extension of B1 on the VERBATIM registered engine.
Engine import: this script exec-loads the function/constant block of the registered
artifact code/2602_hgamma_gates_b1.py (lines up to the stage driver) so n1_gamma,
strong_FU, classify, rung, and constants are the registered objects themselves --
no re-typing, no drift. Verdicts are read from the prereg against raw outputs (2579).
"""
import numpy as np, time, os, sys
from scipy.optimize import brentq, minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2602_hgamma_gates_b1.py")).read()
# execute only through the engine definitions (stop before the 2602 stage driver)
cut = src.index("t0=_t.time(); trunc_mode='DIST'")
ns = {}
exec(src[:cut], ns)
n1_gamma = ns['n1_gamma']; rung = ns['rung']
AHC = ns['AHC']; ALPHA_S = ns['ALPHA_S']; A_QQ = ns['A_QQ']; D = ns['D']
EQQ = ns['EQQ']; TAUC = ns['TAUC']; M = 132.0
np_ = np

H4, C4, S4 = rung(1)
ETA = 0.5   # the sole gamma-admitted point [2602]

# ---------------- E-A analytic model (prereg S2; zero freedom) ----------------
def U_inc(z, b, w):
    """Incident qCP (charge -1) potential at [b*D, 0, z] vs the settled square:
    4 Morse qq wells + alternating electric, registered forms verbatim."""
    pos = np_.array([b * D, 0.0, z])
    Utot = 0.0
    beta = w / D
    for k in range(4):
        r = max(np_.linalg.norm(pos - H4[k]), 1e-9)
        e = np_.exp(-beta * (r - D))
        Utot += EQQ * ((1 - e) ** 2 - 1)                       # Morse qq [2584]
        Utot += (-1.0) * C4[k] * ALPHA_S * AHC / np_.sqrt(r * r + A_QQ * A_QQ)
    return Utot

def W_of(b, w):
    res = minimize_scalar(lambda z: U_inc(z, b, w), bounds=(-2.0, 4 * D),
                          method='bounded', options={'xatol': 1e-8})
    return max(-res.fun, 0.0), res.x

def gamma_edge(W, Lint):
    """Solve [1-(1-eta)^N](m(g-1)+W) = m(g-1), N = Lint/(v_close*tauC)."""
    def excess(g):
        KE = M * (g - 1)
        gcl = 1 + (KE + W) / M
        vcl = np_.sqrt(1 - 1 / gcl ** 2)
        N = Lint / (vcl * TAUC)
        shed = (1 - (1 - ETA) ** N) * (KE + W)
        return shed - KE
    # capture at low g (excess>0); edge where excess crosses 0
    glo, ghi = 1.0005, 60.0
    if excess(ghi) > 0:
        return np_.inf
    return brentq(excess, glo, ghi, xtol=1e-8)

print("=" * 78)
print("PATCH 2609 -- N2-B-EDGE (prereg 2608; verdicts read there)  eta=0.5")
print("=" * 78)
print("\n[E-A] zero-freedom wells and analytic edges (L_int band {D,2D,3D})")
ANA = {}
for w in (2.0, 4.0):
    for b in (0.0, 0.5, 1.0):
        W, zmin = W_of(b, w)
        gn = 1 + W / M
        vn = np_.sqrt(1 - 1 / gn ** 2)
        band = []
        for L in (D, 2 * D, 3 * D):
            g = gamma_edge(W, L)
            band.append(np_.sqrt(1 - 1 / g ** 2) if np_.isfinite(g) else np_.inf)
        ANA[(w, b)] = (W, band)
        bs = ", ".join(f"{v:.3f}" if np_.isfinite(v) else "none" for v in band)
        print(f"  w={w} b={b}D: W={W:.1f} MeV (z_min={zmin:+.2f}) | "
              f"naive g={gn:.2f} v={vn:.3f}c | v_edge(L={{D,2D,3D}}) = [{bs}]c")

# ---------------- declared numeric grid (prereg S3) ----------------
def b1g(b, v, bd, dtf):
    """B1 cell VERBATIM geometry/classifier [2598/2602]."""
    H0 = np_.vstack([H4, [b * D, 0.0, 4 * D]])
    C0 = np_.append(C4, -1.0)
    S0 = S4 + ['q']
    V0 = np_.zeros((5, 3)); V0[4] = [0, 0, -v]
    res = n1_gamma(H0, C0, S0, dtf, bd, ETA, TC=120, V0=V0)
    Hf = res['H']; Vf = res['V']; cen4 = Hf[:4].mean(axis=0)
    d_inc = np_.linalg.norm(Hf[4] - cen4)
    vr = np_.dot(Vf[4] - Vf[:4].mean(axis=0), (Hf[4] - cen4) / max(d_inc, 1e-9))
    d4 = np_.linalg.norm(Hf[:4] - cen4, axis=1); sq_ok = (d4.max() < 3 * D)
    if d_inc < 3 * D and sq_ok and res['Sea'] > 0: return 'CAP', res
    if d_inc > 4 * D and vr > 0 and sq_ok: return 'SCA', res
    if not sq_ok: return 'FRG', res
    return 'UNR', res

VS = (0.40, 0.50, 0.60, 0.70, 0.80, 0.85, 0.90, 0.95)
t0 = time.time()
cl0, r0 = b1g(0.0, 0.40, 4.0, 1 / 100)
print(f"\n[timing cell] w=4 b=0 v=0.40 dt=1/100: {cl0} "
      f"(g={r0['gmax']:.2f}, Sea={r0['Sea']:.0f}) in {time.time()-t0:.1f}s "
      f"-> full grid foreground-sized: proceeding")

GRID = {}
for w in (2.0, 4.0):
    for b in (0.0, 0.5, 1.0):
        row = []
        for v in VS:
            cl, res = b1g(b, v, w, 1 / 100)
            GRID[(w, b, v)] = (cl, res['gmax'], res['Sea'])
            row.append(f"v={v}:{cl}(g={res['gmax']:.1f},S={res['Sea']:.0f})")
        print(f"  w={w} b={b}D: " + "  ".join(row))

print(f"\n[grid complete in {time.time()-t0:.0f}s]")

# ---------------- brackets + dt-confirmation (prereg S3 rule) ----------------
print("\n[brackets] per family: highest-v CAP, lowest-v non-CAP; re-run at dt=1/200")
for w in (2.0, 4.0):
    for b in (0.0, 0.5, 1.0):
        caps = [v for v in VS if GRID[(w, b, v)][0] == 'CAP']
        nons = [v for v in VS if GRID[(w, b, v)][0] != 'CAP']
        if not caps:
            print(f"  w={w} b={b}D: NO CAP on grid (lowest cell already "
                  f"{GRID[(w,b,VS[0])][0]}) -- bracket = below-grid")
            continue
        if not nons:
            print(f"  w={w} b={b}D: MAP TOTAL through 0.95c -- no edge on grid")
            continue
        vc, vn_ = max(caps), min([v for v in nons if v > max(caps)] or nons)
        c1, _ = b1g(b, vc, w, 1 / 200)[0], None
        c2 = b1g(b, vn_, w, 1 / 200)[0]
        g1 = GRID[(w, b, vc)][0]; g2 = GRID[(w, b, vn_)][0]
        stab = (c1 == g1 and c2 == g2)
        print(f"  w={w} b={b}D: bracket [{vc}({g1}) -> {vn_}({g2})]c ; "
              f"dt=1/200 gives [{c1} -> {c2}] : {'dt-STABLE' if stab else 'dt-UNSTABLE'}")

print("\nDone. Verdicts are read in n2b_edge_record.md against the prereg.")
