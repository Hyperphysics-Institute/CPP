#!/usr/bin/env python3
"""
PATCH 2644 -- N2B-ROB-3 EXECUTION under n2b_rob3_prereg.md (2643) ONLY.
Soft-width (w=2) confirmation of ROB-2's drawn walls. Instrument = the ROB-2
MATCHED launcher (2638 source substitution, verified unique), chain builder
verbatim. Stages: controls | cells | escalate | refine.
"""
import numpy as np, time, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2611_n2b_ch6_scan.py")).read()
OLD = "if dtf < 1 / 150:   # declared 1/200 economy: brief re-settle of the 1/100 object"
NEW = "if False:   # ROB-2 MATCHED (prereg 2637): economy re-settle leg REMOVED"
assert src.count(OLD) == 1, "economy-leg anchor not unique -- STOP"
src_m = src.replace(OLD, NEW)
cut = src_m.index('print("=" * 78)')
ns = {'__name__': 'rob3', '__file__': os.path.join(HERE, "2611_n2b_ch6_scan.py")}
exec(src_m[:cut], ns)
scan_cell = ns['scan_cell']; n1_gamma = ns['n1_gamma']
D = ns['D']; ETA = ns['ETA']; H4 = ns['H4']; C4 = ns['C4']; S4 = ns['S4']
np_ = np
CHARGES = ((5, -1.0), (6, +1.0), (7, -1.0), (8, +1.0))

def chain(axis, b, phi, bd, label, dts=(1 / 100, 1 / 200)):
    base = n1_gamma(H4, C4, S4, 1 / 100, bd, ETA, TC=60)
    Hc, Vc, Cc, Sc = base['H'].copy(), base['V'].copy(), C4.copy(), list(S4)
    lines = []; complete = True; halt = None
    for k, q in CHARGES:
        verd = {}
        for dtf in dts:
            cl, res, d_inc = scan_cell(Hc, Vc, Cc, Sc, axis, b, phi, q, bd, dtf)
            Hf = res['H']; cen = Hf.mean(axis=0)
            dmax = np_.linalg.norm(Hf - cen, axis=1).max()
            bound = (cl == 'CAP') and (dmax < 3 * D)
            verd[dtf] = (cl, dmax, bound, res)
        (c1, m1, b1, r1), (c2, m2, b2, r2) = verd[dts[0]], verd[dts[1]]
        dstab = (b1 == b2)
        dcen = np_.linalg.norm(r1['H'][:len(Hc)].mean(axis=0) - Hc.mean(axis=0))
        lines.append(f"    st{k}: {dts[0]:.5f} {c1}(dmax={m1:.2f}) "
                     f"{dts[1]:.5f} {c2}(dmax={m2:.2f}) "
                     f"{'dt-STABLE' if dstab else 'dt-UNSTABLE'} "
                     f"Sea={r1['Sea']:.0f}/{r2['Sea']:.0f} "
                     f"gmax={r1['gmax']:.2f}/{r2['gmax']:.2f} |dcen|={dcen:.2f}"
                     + (" [FRG]" if 'FRG' in (c1, c2) else ""))
        if not (b1 and b2 and dstab):
            complete = False; halt = k; break
        Hc, Vc = r1['H'].copy(), r1['V'].copy()
        Cc = np_.append(Cc, q); Sc = Sc + ['q']
    settle = ""
    if complete:
        r8 = n1_gamma(Hc, Cc, Sc, dts[1], bd, ETA, TC=60, V0=Vc)
        cen = r8['H'].mean(axis=0); dc = np_.linalg.norm(r8['H'] - cen, axis=1)
        ok8 = dc.max() < 3 * D
        settle = (f"    settle@{dts[1]:.5f}: Rrms={np_.sqrt((dc*dc).mean()):.2f} "
                  f"dmax={dc.max():.2f} ({'BOUNDED' if ok8 else 'UNBOUND'}) "
                  f"Edrift={r8['Edrift']:.2f}")
        complete = complete and ok8
    tag = 'COMPLETE' if complete else f'HALT@st{halt}'
    print(f"  [{label}] -> {tag}")
    for ln in lines: print(ln)
    if settle: print(settle)
    return complete

stage = sys.argv[1] if len(sys.argv) > 1 else 'controls'
t0 = time.time()
print("=" * 78)
print(f"PATCH 2644 -- N2B-ROB-3 (prereg 2643; verdicts read there)  stage={stage}")
print("=" * 78)

if stage == 'controls':
    print("[C-S1] matched soft registered-channel control, w=2 "
          "(RS1/2631 soft-row settle for comparison: 0.84/0.86/0.01)")
    chain((0, 0, 1), 0.5, 0, 2.0, "MATCHED w=2 axis=+z b=0.5 phi=0 (REGISTERED)")
    print("[C-S2] drawn-soft-cell conservatism: phi=30, w=2")
    chain((0, 0, 1), 0.5, 30, 2.0, "MATCHED w=2 phi=30deg")
elif stage == 'cells':
    print("[CELL A-soft] phi=45, w=2, matched, dt-union {1/100,1/200}")
    chain((0, 0, 1), 0.5, 45, 2.0, "MATCHED w=2 phi=45deg")
    print("[CELL B-soft] +y face, w=2, matched, dt-union {1/100,1/200}")
    chain((0, 1, 0), 0.5, 0, 2.0, "MATCHED w=2 axis=+y")
elif stage == 'escalate':
    which = sys.argv[2]
    if which in ('A', 'both'):
        print("[ESC A-soft] phi=45 w=2, dt-union {1/200,1/400}")
        chain((0, 0, 1), 0.5, 45, 2.0, "MATCHED w=2 phi=45deg ESC", dts=(1/200, 1/400))
    if which in ('B', 'both'):
        print("[ESC B-soft] +y w=2, dt-union {1/200,1/400}")
        chain((0, 1, 0), 0.5, 0, 2.0, "MATCHED w=2 axis=+y ESC", dts=(1/200, 1/400))
elif stage == 'refine':
    print("[REFINE] phi=37.5, w=2, matched (runs iff Cell A-soft HALTED dt-stably)")
    chain((0, 0, 1), 0.5, 37.5, 2.0, "MATCHED w=2 phi=37.5deg")
print(f"[{time.time()-t0:.0f}s]")
print("\nDone. Verdicts are read in n2b_rob3_record.md against the prereg.")
