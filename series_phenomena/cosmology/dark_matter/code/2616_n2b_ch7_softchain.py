#!/usr/bin/env python3
"""
PATCH 2616 -- N2-B-CH7 EXECUTION under n2b_ch7_prereg.md (2615) ONLY.
The soft-chain continuation: stages 7(-1)/8(+1) on the original-face channel, AIMED
convention, dt-union unconditional on verdicts; finished-object settle at 1/200.
Engine/launcher exec-loaded VERBATIM from the registered 2611 artifact (-> 2604).
"""
import numpy as np, time, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2611_n2b_ch6_scan.py")).read()
cut = src.index('print("=" * 78)')
ns = {'__name__': 'ch7', '__file__': os.path.join(HERE, '2611_n2b_ch6_scan.py')}
exec(src[:cut], ns)
regen6 = ns['regen6']; scan_cell = ns['scan_cell']; n1_gamma = ns['n1_gamma']
D = ns['D']
np_ = np
AX = (0, 0, 1)   # start side +z (the original face), moving -z; b=0.5D, phi=0

print("=" * 78)
print("PATCH 2616 -- N2-B-CH7: the soft-chain continuation (prereg 2615)")
print("=" * 78)
t0 = time.time()
H6, V6, C6, S6, log_s = regen6(2.0)
print(f"[C-R] soft regeneration stages: {log_s} (must be BOUND at 5 and 6)")

state = (H6, V6, C6, S6)
STEEP_BENCH = "steep bench: Rrms 0.77->0.92 fm, dmax<=1.06, Edrift=0.00 (2604)"
for k, q in ((7, -1.0), (8, +1.0)):
    Hc, Vc, Cc, Sc = state
    verd = {}
    for dtf in (1 / 100, 1 / 200):
        cl, res, d_inc = scan_cell(Hc, Vc, Cc, Sc, AX, 0.5, 0, q, 2.0, dtf)
        Hf = res['H']; cen = Hf.mean(axis=0)
        dmax = np_.linalg.norm(Hf - cen, axis=1).max()
        chain_ok = dmax < 3 * D
        bound = (cl == 'CAP') and chain_ok
        verd[dtf] = (cl, chain_ok, bound, res)
        print(f"  stage {k} dt=1/{int(1/dtf)}: scan={cl} chain_dmax={dmax:.2f} "
              f"({'ok' if chain_ok else 'FAIL'}) Sea={res['Sea']:.0f} "
              f"gmax={res['gmax']:.2f} -> {'BOUND' if bound else 'NOT-BOUND'}")
    b1, b2 = verd[1/100][2], verd[1/200][2]
    print(f"  stage {k}: {'dt-STABLE' if b1 == b2 else 'dt-UNSTABLE'} "
          f"verdict={'BOUND' if b1 else 'NOT-BOUND'}")
    if not (b1 and b2):
        print("  chain HALTS here per criteria."); break
    # propagate on the registered 1/100 path
    res = verd[1/100][3]
    n_prev = len(Hc)
    state = (res['H'].copy(), res['V'].copy(),
             np_.append(Cc, q), Sc + ['q'])
else:
    # completion settle at 1/200
    Hc, Vc, Cc, Sc = state
    res8 = n1_gamma(Hc, Cc, Sc, 1 / 200, 2.0, 0.5, TC=60, V0=Vc)
    cen = res8['H'].mean(axis=0)
    dc = np_.linalg.norm(res8['H'] - cen, axis=1)
    Rrms = float(np_.sqrt((dc * dc).mean())); dmax = float(dc.max())
    print(f"\n[8-object settle dt=1/200 TC=60] N={len(Hc)} Rrms={Rrms:.2f} fm "
          f"dmax={dmax:.2f} ({'BOUNDED' if dmax < 3*D else 'UNBOUND'}) "
          f"Edrift={res8['Edrift']:.2f}  |  {STEEP_BENCH}")
print(f"\n[{time.time()-t0:.0f}s] Done. Verdicts read in n2b_ch7_record.md.")
