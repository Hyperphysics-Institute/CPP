#!/usr/bin/env python3
"""
PATCH 2612 -- N2-B-CH6 DEFECT DIAGNOSTIC (the RC4 follow-up; instrument audit, not
new-physics registration). Reproduces the registered stage-7 launch VERBATIM
(absolute-aim stage_capture from the 2604 artifact) on the registered soft and steep
6-clusters; logs cluster centroid position/velocity at launch and the launch line's
closest approach to the centroid; reads hypothesis H-drift against raw geometry.
Engine + stage_capture exec-loaded/copied VERBATIM from the registered 2604 artifact.
"""
import numpy as np, time, os

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2604_n2b_chain_b3_b4.py")).read()
cut = src.index("import sys; stage=sys.argv[1]")
ns = {}
exec(src[:cut], ns)
n1_gamma = ns['n1_gamma']; rung = ns['rung']; D = ns['D']; TAUC = ns['TAUC']
np_ = np
H4, C4, S4 = rung(1)
ETA = 0.5
CH = (0.5, 0.10)

def stage_capture(Hc, Vc, Cc, Sc, inc_q, bd, dtf, TC=120):
    """VERBATIM from the registered 2604 driver."""
    b, v = CH
    ztop = Hc[:, 2].max()
    H0 = np_.vstack([Hc, [b * D, 0.0, ztop + 4 * D]]); C0 = np_.append(Cc, inc_q); S0 = Sc + ['q']
    V0 = np_.vstack([Vc, [0, 0, -v]])
    res = n1_gamma(H0, C0, S0, dtf, bd, ETA, TC=TC, V0=V0)
    Hf = res['H']
    cen = Hf.mean(axis=0); dmax = np_.linalg.norm(Hf - cen, axis=1).max()
    ok = dmax < 3 * D
    return ok, res, H0, C0, S0

print("=" * 78)
print("PATCH 2612 -- CH6 DEFECT DIAGNOSTIC: verbatim absolute-aim stage 7 + geometry")
print("=" * 78)
t0 = time.time()
for bd, wname in ((2.0, 'soft'), (4.0, 'steep')):
    base = n1_gamma(H4, C4, S4, 1 / 100, bd, ETA, TC=60)
    Hc, Vc = base['H'].copy(), base['V'].copy(); Cc = C4.copy(); Sc = list(S4)
    for k, q in ((5, -1.0), (6, +1.0)):
        ok, res, H0, C0, S0 = stage_capture(Hc, Vc, Cc, Sc, q, bd, 1 / 100)
        Hc, Vc = res['H'].copy(), res['V'].copy(); Cc = np_.array(C0); Sc = S0
        print(f"  [{wname}] stage {k}: {'BOUND' if ok else 'UNBOUND'} "
              f"(registered path)")
    cen = Hc.mean(axis=0); vcen = Vc.mean(axis=0)
    # the registered launch geometry for stage 7:
    ztop = Hc[:, 2].max()
    start = np_.array([CH[0] * D, 0.0, ztop + 4 * D])
    # closest approach of the launch LINE (start + t*(0,0,-1)) to the centroid AT LAUNCH
    b_eff0 = np_.linalg.norm((start - cen)[:2])   # perpendicular distance to a -z line
    # time-of-flight to the centroid's z-plane; centroid position THEN (linear estimate)
    tof = (start[2] - cen[2]) / CH[1]
    cen_then = cen + vcen * tof
    b_eff_t = np_.linalg.norm((start - cen_then)[:2])
    print(f"  [{wname}] AT STAGE-7 LAUNCH: centroid=({cen[0]:+.2f},{cen[1]:+.2f},{cen[2]:+.2f}) fm  "
          f"v_cen=({vcen[0]:+.4f},{vcen[1]:+.4f},{vcen[2]:+.4f})c")
    print(f"  [{wname}]   launch column (x,y)=({CH[0]*D:.3f},0)  b_eff(now)={b_eff0:.2f} fm  "
          f"tof~{tof:.0f} fm/c  b_eff(at arrival, linear)={b_eff_t:.2f} fm  (D={D})")
    ok7, res7, _, _, _ = stage_capture(Hc, Vc, Cc, Sc, -1.0, bd, 1 / 100)
    Hf = res7['H']; cen6 = Hf[:6].mean(axis=0)
    d_inc = np_.linalg.norm(Hf[6] - cen6)
    print(f"  [{wname}] VERBATIM stage 7 (absolute aim): "
          f"{'BOUND' if ok7 else 'UNBOUND'}  Sea={res7['Sea']:.1f}  "
          f"gmax={res7['gmax']:.2f}  d_inc(final)={d_inc:.1f} fm")
    # dt-union on the diagnostic cell (2610 rule carried):
    ok7b, res7b, _, _, _ = stage_capture(Hc, Vc, Cc, Sc, -1.0, bd, 1 / 200)
    print(f"  [{wname}] VERBATIM stage 7 dt=1/200: {'BOUND' if ok7b else 'UNBOUND'} "
          f"Sea={res7b['Sea']:.1f}  -> {'dt-STABLE' if ok7==ok7b else 'dt-UNSTABLE'}")
print(f"\n[{time.time()-t0:.0f}s] Done. Reading in the 2612 patch document.")
