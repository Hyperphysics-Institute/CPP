#!/usr/bin/env python3
"""
PATCH 2611 -- N2-B-CH6 EXECUTION under n2b_ch6_prereg.md (2610) ONLY.
The 6-cluster channel scan: 23 declared cells x dt-union {1/100,1/200} UNCONDITIONAL.
Engine exec-loaded VERBATIM from the registered 2604 artifact; cluster regeneration
is the registered chain itself, deterministically. Controls C-A (soft miss), C-B
(steep cap), C-R (stages 5-6 bound) gate the reading. Verdicts read from the prereg
against raw outputs (2579).
"""
import numpy as np, time, os

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2604_n2b_chain_b3_b4.py")).read()
cut = src.index("import sys; stage=sys.argv[1]")
ns = {}
exec(src[:cut], ns)
n1_gamma = ns['n1_gamma']; rung = ns['rung']
D = ns['D']; TAUC = ns['TAUC']
np_ = np

H4, C4, S4 = rung(1)
ETA = 0.5
CH = (0.5, 0.10)   # the registered declared channel [2604]

def stage_capture(Hc, Vc, Cc, Sc, inc_q, bd, dtf, TC=120):
    """VERBATIM from the registered 2604 driver (cited copy; the chain's stage)."""
    b, v = CH
    ztop = Hc[:, 2].max()
    H0 = np_.vstack([Hc, [b * D, 0.0, ztop + 4 * D]]); C0 = np_.append(Cc, inc_q); S0 = Sc + ['q']
    V0 = np_.vstack([Vc, [0, 0, -v]])
    res = n1_gamma(H0, C0, S0, dtf, bd, ETA, TC=TC, V0=V0)
    Hf = res['H']
    cen = Hf.mean(axis=0); dmax = np_.linalg.norm(Hf - cen, axis=1).max()
    ok = dmax < 3 * D
    return ok, res, H0, C0, S0

def regen6(bd):
    """Registered chain to the 6-object: settle 4-square, +5(-1), +6(+1). C-R gate."""
    base = n1_gamma(H4, C4, S4, 1 / 100, bd, ETA, TC=60)
    Hc, Vc = base['H'].copy(), base['V'].copy(); Cc = C4.copy(); Sc = list(S4)
    log = []
    for k, q in ((5, -1.0), (6, +1.0)):
        ok, res, H0, C0, S0 = stage_capture(Hc, Vc, Cc, Sc, q, bd, 1 / 100)
        log.append((k, ok))
        Hc, Vc = res['H'].copy(), res['V'].copy(); Cc = np_.array(C0); Sc = S0
    return Hc, Vc, Cc, Sc, log

def scan_cell(Hc, Vc, Cc, Sc, axis, b, phi_deg, inc_q, bd, dtf):
    """One scan cell: incident from 4D out along -axis, offset b*D in the declared
    transverse direction (lexicographically-first perpendicular axis, rotated by phi
    about the approach axis). Classifier = registered B1 final-state form verbatim."""
    a = np_.array(axis, float); a /= np_.linalg.norm(a)
    # deterministic transverse rule
    perp = None
    for e in (np_.array([1., 0, 0]), np_.array([0, 1., 0]), np_.array([0, 0, 1.])):
        if abs(np_.dot(e, a)) < 0.9:
            perp = e - np_.dot(e, a) * a; perp /= np_.linalg.norm(perp); break
    if phi_deg:
        c, s = np_.cos(np_.radians(phi_deg)), np_.sin(np_.radians(phi_deg))
        p2 = np_.cross(a, perp)
        perp = c * perp + s * p2
    cen0 = Hc.mean(axis=0)
    if dtf < 1 / 150:   # declared 1/200 economy: brief re-settle of the 1/100 object
        rs = n1_gamma(Hc, Cc, Sc, dtf, bd, ETA, TC=20, V0=Vc)
        Hb, Vb = rs['H'].copy(), rs['V'].copy()
    else:
        Hb, Vb = Hc, Vc
    ext = max(np_.linalg.norm(Hb - Hb.mean(axis=0), axis=1).max(), 0.0)
    start = Hb.mean(axis=0) + a * (ext + 4 * D) + perp * (b * D)
    H0 = np_.vstack([Hb, start]); C0 = np_.append(Cc, inc_q); S0 = Sc + ['q']
    V0 = np_.vstack([Vb, -CH[1] * a])
    res = n1_gamma(H0, C0, S0, dtf, bd, ETA, TC=120, V0=V0)
    Hf = res['H']; Vf = res['V']; n6 = len(Hb)
    cen = Hf[:n6].mean(axis=0)
    d_inc = np_.linalg.norm(Hf[n6] - cen)
    vr = np_.dot(Vf[n6] - Vf[:n6].mean(axis=0), (Hf[n6] - cen) / max(d_inc, 1e-9))
    d6 = np_.linalg.norm(Hf[:n6] - cen, axis=1); cl_ok = (d6.max() < 3 * D)
    if d_inc < 3 * D and cl_ok and res['Sea'] > 0: cl = 'CAP'
    elif d_inc > 4 * D and vr > 0 and cl_ok: cl = 'SCA'
    elif not cl_ok: cl = 'FRG'
    else: cl = 'UNR'
    return cl, res, d_inc

print("=" * 78)
print("PATCH 2611 -- N2-B-CH6: the channel scan (prereg 2610; verdicts read there)")
print("=" * 78)
t0 = time.time()

# ---- C-R: regeneration ----
H6s, V6s, C6s, S6s, log_s = regen6(2.0)
H6t, V6t, C6t, S6t, log_t = regen6(4.0)
print(f"[C-R] soft stages: {log_s}  steep stages: {log_t}  "
      f"(both must be BOUND=True at 5 and 6)")

AXES = {'-z': (0, 0, -1), '+z': (0, 0, 1), '-x': (-1, 0, 0),
        '+x': (1, 0, 0), '-y': (0, -1, 0), '+y': (0, 1, 0)}
# NOTE: approach axis a = direction FROM cluster TO start; velocity is -a (inward).

cells = []
for ax in ('-z', '+z', '-x', '+x', '-y', '+y'):
    for b in (0.0, 0.5, 1.0):
        cells.append(('soft', ax, b, 0, -1.0))
for phi in (45, 90, 135):
    cells.append(('soft', '-z', 0.5, phi, -1.0))
cells.append(('soft', '-z', 0.5, 0, +1.0))          # charge flip
cells.append(('steep', '-z', 0.5, 0, -1.0))          # C-B

# NOTE the original 2604 channel approaches from ABOVE (+z side) moving -z:
# in this parameterization that is axis '+z' start side... The registered geometry
# places the incident at ztop+4D moving -v z: start side +z, velocity -z.
# Axis key here = START side; '-z' means start BELOW moving +z. The original
# channel is therefore ('+z', b=0.5) in this script's convention. C-A reads there.

results = {}
for (w, ax, b, phi, q) in cells:
    bd = 2.0 if w == 'soft' else 4.0
    Hc, Vc, Cc, Sc = (H6s, V6s, C6s, S6s) if w == 'soft' else (H6t, V6t, C6t, S6t)
    row = {}
    for dtf in (1 / 100, 1 / 200):
        cl, res, d_inc = scan_cell(Hc, Vc, Cc, Sc, AXES[ax], b, phi, q, bd, dtf)
        row[dtf] = (cl, res['Sea'], res['gmax'], d_inc)
    results[(w, ax, b, phi, q)] = row
    c1, c2 = row[1 / 100][0], row[1 / 200][0]
    stab = 'dt-STABLE' if c1 == c2 else 'dt-UNSTABLE'
    tag = ''
    if (w, ax, b, phi, q) == ('soft', '+z', 0.5, 0, -1.0): tag = '  <-- C-A (original)'
    if w == 'steep': tag = '  <-- C-B (steep control)'
    if q > 0: tag = '  <-- charge-flip'
    print(f"  {w:5s} start={ax:2s} b={b}D phi={phi:3d} q={q:+.0f}: "
          f"1/100={c1}(S={row[1/100][1]:.0f},d={row[1/100][3]:.1f}) "
          f"1/200={c2}(S={row[1/200][1]:.0f},d={row[1/200][3]:.1f}) {stab}{tag}")

print(f"\n[scan complete in {time.time()-t0:.0f}s]")
ncap = sum(1 for k, r in results.items()
           if k[0] == 'soft' and r[1/100][0] == 'CAP' == r[1/200][0])
nuns = sum(1 for r in results.values() if r[1/100][0] != r[1/200][0])
print(f"[summary] soft dt-stable CAP channels: {ncap} ; dt-unstable cells: {nuns}")
print("Done. Verdicts are read in n2b_ch6_record.md against the prereg.")
