#!/usr/bin/env python3
"""
PATCH 2631 -- N2B-ROB-1 EXECUTION under n2b_rob1_prereg.md (2630) ONLY.
Aim-sensitivity envelope on the assembly chain. Engine + aimed launcher exec-loaded
VERBATIM from the registered 2611 artifact (-> 2604 engine). scan_cell carries every
stage; stage_capture excluded by citation. Chain criteria verbatim (ch7 lineage).
Stages: control | f1 | f2 | f3 | soft.
"""
import numpy as np, time, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2611_n2b_ch6_scan.py")).read()
cut = src.index('print("=" * 78)')
ns = {'__name__': 'rob1', '__file__': os.path.join(HERE, '2611_n2b_ch6_scan.py')}
exec(src[:cut], ns)
scan_cell = ns['scan_cell']; n1_gamma = ns['n1_gamma']
D = ns['D']; ETA = ns['ETA']; H4 = ns['H4']; C4 = ns['C4']; S4 = ns['S4']
np_ = np
CHARGES = ((5, -1.0), (6, +1.0), (7, -1.0), (8, +1.0))

def chain(axis, b, phi, bd, label):
    """Uniform-launcher chain 4->8; returns (COMPLETE?, per-stage lines, settle line)."""
    base = n1_gamma(H4, C4, S4, 1 / 100, bd, ETA, TC=60)
    Hc, Vc, Cc, Sc = base['H'].copy(), base['V'].copy(), C4.copy(), list(S4)
    lines = []; complete = True; halt = None
    for k, q in CHARGES:
        verd = {}
        for dtf in (1 / 100, 1 / 200):
            cl, res, d_inc = scan_cell(Hc, Vc, Cc, Sc, axis, b, phi, q, bd, dtf)
            Hf = res['H']; cen = Hf.mean(axis=0)
            dmax = np_.linalg.norm(Hf - cen, axis=1).max()
            bound = (cl == 'CAP') and (dmax < 3 * D)
            verd[dtf] = (cl, dmax, bound, res)
        c1, m1, b1, r1 = verd[1 / 100]; c2, m2, b2, r2 = verd[1 / 200]
        dstab = (b1 == b2)
        dcen = np_.linalg.norm(r1['H'][:len(Hc)].mean(axis=0) - Hc.mean(axis=0))
        lines.append(f"    st{k}: 1/100 {c1}(dmax={m1:.2f}) 1/200 {c2}(dmax={m2:.2f}) "
                     f"{'dt-STABLE' if dstab else 'dt-UNSTABLE'} "
                     f"Sea={r1['Sea']:.0f} gmax={r1['gmax']:.2f} |dcen|={dcen:.2f}"
                     + (" [FRG]" if 'FRG' in (c1, c2) else ""))
        if not (b1 and b2 and dstab):
            complete = False; halt = k; break
        Hc, Vc = r1['H'].copy(), r1['V'].copy()
        Cc = np_.append(Cc, q); Sc = Sc + ['q']
    settle = ""
    if complete:
        r8 = n1_gamma(Hc, Cc, Sc, 1 / 200, bd, ETA, TC=60, V0=Vc)
        cen = r8['H'].mean(axis=0); dc = np_.linalg.norm(r8['H'] - cen, axis=1)
        ok8 = dc.max() < 3 * D
        settle = (f"    settle: Rrms={np_.sqrt((dc*dc).mean()):.2f} dmax={dc.max():.2f} "
                  f"({'BOUNDED' if ok8 else 'UNBOUND'}) Edrift={r8['Edrift']:.2f}")
        complete = complete and ok8
    tag = 'COMPLETE' if complete else f'HALT@st{halt}'
    print(f"  [{label}] -> {tag}")
    for ln in lines: print(ln)
    if settle: print(settle)
    return complete

stage = sys.argv[1] if len(sys.argv) > 1 else 'control'
t0 = time.time()
print("=" * 78)
print(f"PATCH 2631 -- N2B-ROB-1 (prereg 2630; verdicts read there)  stage={stage}")
print("=" * 78)

if stage == 'control':
    print("[C-R'] uniform-launcher registered-channel chain, w=4")
    chain((0, 0, 1), 0.5, 0, 4.0, "w=4 axis=+z b=0.5 phi=0 (REGISTERED)")
elif stage == 'f1':
    print("[F1] lateral offset, w=4 (b=0.5 satisfied by C-R')")
    for b in (0.0, 1.0, 1.5, 2.0):
        chain((0, 0, 1), b, 0, 4.0, f"b={b}D")
elif stage == 'f2':
    print("[F2] orientation, w=4")
    for phi in (15, 30, 45):
        chain((0, 0, 1), 0.5, phi, 4.0, f"phi={phi}deg")
elif stage == 'f3':
    print("[F3] approach face, w=4")
    for ax, nm in (((1, 0, 0), '+x'), ((0, 1, 0), '+y'), ((0, 0, -1), '-z')):
        chain(ax, 0.5, 0, 4.0, f"axis={nm}")
elif stage == 'soft':
    print("[SOFT] w=2 confirm rows: registered + largest steep survivors "
          "(fixed by the steep outcome per prereg S1: b=2.0D, phi=30, axis=+x)")
    for (ax, b, phi, nm) in (((0, 0, 1), 0.5, 0, "registered"),
                             ((0, 0, 1), 2.0, 0, "b=2.0D"),
                             ((0, 0, 1), 0.5, 30, "phi=30deg"),
                             ((1, 0, 0), 0.5, 0, "axis=+x")):
        chain(ax, b, phi, 2.0, f"w=2 {nm}")
print(f"[{time.time()-t0:.0f}s]")
print("\nDone. Verdicts are read in n2b_rob1_record.md against the prereg.")
