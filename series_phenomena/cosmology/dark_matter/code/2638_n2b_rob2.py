#!/usr/bin/env python3
"""
PATCH 2638 -- N2B-ROB-2 EXECUTION under n2b_rob2_prereg.md (2637) ONLY.
Economy-matched re-run of ROB-1's two UNDRAWN cells (phi=45, +y face).
Engine + launcher exec-loaded VERBATIM from the registered 2611 artifact
(-> 2604 engine) with the SINGLE preregistered amendment: the 1/200 economy
re-settle branch in scan_cell is disabled by an exact one-condition source
substitution (verified unique), so BOTH dt legs of every stage launch at the
bitwise-identical propagated chain state. Everything else (transverse rule,
launch distance, B1 classifier, chain criteria, constants) is the registered
object. Stages: controls | cells | escalate | refine.
"""
import numpy as np, time, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2611_n2b_ch6_scan.py")).read()

# ---- the single preregistered amendment (2637 S1): economy leg removed ----
OLD = "if dtf < 1 / 150:   # declared 1/200 economy: brief re-settle of the 1/100 object"
NEW = "if False:   # ROB-2 MATCHED (prereg 2637): economy re-settle leg REMOVED"
assert src.count(OLD) == 1, "economy-leg anchor not unique -- STOP"
src_m = src.replace(OLD, NEW)

cut = src_m.index('print("=" * 78)')
ns = {'__name__': 'rob2', '__file__': os.path.join(HERE, "2611_n2b_ch6_scan.py")}
exec(src_m[:cut], ns)
scan_cell = ns['scan_cell']; n1_gamma = ns['n1_gamma']
D = ns['D']; ETA = ns['ETA']; H4 = ns['H4']; C4 = ns['C4']; S4 = ns['S4']
np_ = np
CHARGES = ((5, -1.0), (6, +1.0), (7, -1.0), (8, +1.0))

def chain(axis, b, phi, bd, label, dts=(1 / 100, 1 / 200)):
    """Matched-launcher chain 4->8. dt-union = dts (coarse, fine); propagate on
    dts[0]; completion settle at dts[1] (2637 S3 escalation rule). Base settle
    verbatim 2630 S1 (TC=60 at 1/100)."""
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
    return complete, halt, lines

stage = sys.argv[1] if len(sys.argv) > 1 else 'controls'
t0 = time.time()
print("=" * 78)
print(f"PATCH 2638 -- N2B-ROB-2 (prereg 2637; verdicts read there)  stage={stage}")
print("=" * 78)

if stage == 'controls':
    print("[C-M1] matched registered-channel control, w=4")
    chain((0, 0, 1), 0.5, 0, 4.0, "MATCHED axis=+z b=0.5 phi=0 (REGISTERED)")
    print("[C-M2] drawn-cell conservatism control: phi=30, w=4")
    chain((0, 0, 1), 0.5, 30, 4.0, "MATCHED phi=30deg")
elif stage == 'cells':
    print("[CELL A] phi=45, w=4, matched, dt-union {1/100,1/200}")
    chain((0, 0, 1), 0.5, 45, 4.0, "MATCHED phi=45deg")
    print("[CELL B] +y face, w=4, matched, dt-union {1/100,1/200}")
    chain((0, 1, 0), 0.5, 0, 4.0, "MATCHED axis=+y")
elif stage == 'escalate':
    which = sys.argv[2]
    if which in ('A', 'both'):
        print("[ESC A] phi=45, dt-union {1/200,1/400}, propagate 1/200")
        chain((0, 0, 1), 0.5, 45, 4.0, "MATCHED phi=45deg ESC", dts=(1/200, 1/400))
    if which in ('B', 'both'):
        print("[ESC B] +y face, dt-union {1/200,1/400}, propagate 1/200")
        chain((0, 1, 0), 0.5, 0, 4.0, "MATCHED axis=+y ESC", dts=(1/200, 1/400))
elif stage == 'refine':
    print("[REFINE] phi=37.5, w=4, matched (runs iff Cell A read RM1-WALL)")
    chain((0, 0, 1), 0.5, 37.5, 4.0, "MATCHED phi=37.5deg")
print(f"[{time.time()-t0:.0f}s]")
print("\nDone. Verdicts are read in n2b_rob2_record.md against the prereg.")
