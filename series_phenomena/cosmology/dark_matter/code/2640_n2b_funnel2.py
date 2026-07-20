#!/usr/bin/env python3
"""
PATCH 2640 -- N2B-FUNNEL-2 EXECUTION under n2b_funnel2_prereg.md (2639) ONLY.
Funnel upper bound (ON, b>8D, both widths) + w=2 OFF stabilization.
Engine exec-loaded VERBATIM from the registered 2624 artifact (-> 2602 engine):
n1_gamma/n1_disc, launch, classify, constants are the registered objects.
OFF-form classifier (prereg S1 disclosed item 1) = registered classify minus the
sink-referential Sea>0 conjunct, applied to eta=0 cells only, ALWAYS printed
beside the registered-form class. Stages: controls | f2a | f2b.
"""
import numpy as np, time, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2624_n2b_disc1_2.py")).read()
cut = src.index("stage=sys.argv[1]")
ns = {'__name__': 'funnel2', '__file__': os.path.join(HERE, "2624_n2b_disc1_2.py")}
exec(src[:cut], ns)
n1_gamma = ns['n1_gamma']; launch = ns['launch']; classify = ns['classify']
cell = ns['cell']; D = ns['D']

def classify_off(res):
    """OFF-form (prereg 2639 S1 item 1): registered classifier minus Sea>0."""
    Hf = res['H']; Vf = res['V']; cen4 = Hf[:4].mean(axis=0)
    d_inc = np.linalg.norm(Hf[4] - cen4)
    vr = np.dot(Vf[4] - Vf[:4].mean(axis=0), (Hf[4] - cen4) / max(d_inc, 1e-9))
    d4 = np.linalg.norm(Hf[:4] - cen4, axis=1); sq_ok = (d4.max() < 3 * D)
    if d_inc < 3 * D and sq_ok: return 'CAP'
    if d_inc > 4 * D and vr > 0 and sq_ok: return 'SCA'
    if not sq_ok: return 'FRG'
    return 'UNR'

def run(b, w, eta, dtf):
    r = cell(float(b), 0.10, w, eta, dtf, disc=False)
    Hf = r['H']; cen4 = Hf[:4].mean(axis=0)
    d_inc = np.linalg.norm(Hf[4] - cen4)
    dcen = np.linalg.norm(cen4)
    return r, classify(r), classify_off(r), d_inc, dcen

def off_row(b, w, dtf):
    r, cr, co, d_inc, dcen = run(b, w, 0.0, dtf)
    return (f"b={b}: REG={cr} OFF-form={co} "
            f"(d_inc={d_inc:.2f} Sea={r['Sea']:.1e} dcen={dcen:.2f})"), cr, co

stage = sys.argv[1] if len(sys.argv) > 1 else 'controls'
t0 = time.time()
print("=" * 78)
print(f"PATCH 2640 -- N2B-FUNNEL-2 (prereg 2639; verdicts read there)  stage={stage}")
print("=" * 78)

if stage == 'controls':
    print("[C-F1] convention-pin: registered 2624 brackets")
    r, cr, _, d, _ = run(8, 4.0, 0.5, 1 / 200)
    print(f"  w=4 ON  b=8 dt=1/200: {cr} (registered: CAP)  d_inc={d:.2f}")
    for b in (5, 6):
        r, cr, co, d, _ = run(b, 4.0, 0.0, 1 / 200)
        print(f"  w=4 OFF b={b} dt=1/200: REG={cr} (registered: {'CAP' if b==5 else 'SCA'})"
              f"  [C-F2 OFF-form={co}]  d_inc={d:.2f} Sea={r['Sea']:.1e}")
elif stage == 'f2a':
    for w in (4.0, 2.0):
        print(f"[F2a] upper-bound scan ON eta=0.5 w={w} dt=1/100")
        cls = {}
        row = []
        for b in (9, 10, 12, 14, 16):
            r, cr, _, d, dc = run(b, w, 0.5, 1 / 100)
            cls[b] = cr; row.append(f"b={b}:{cr}(d_inc={d:.2f})")
        print("  " + "  ".join(row))
        caps = [b for b in cls if cls[b] == 'CAP']
        noncaps = [b for b in cls if cls[b] != 'CAP']
        if caps and noncaps and min(noncaps) > max(caps):
            bc, bn = max(caps), min(noncaps)
        elif caps and not noncaps:
            bc, bn = max(caps), None
        elif not caps:
            bc, bn = None, min(noncaps)
        else:  # interleaved -- disclose raw, bracket at last-CAP/first-non above it
            bc = max(caps); above = [b for b in noncaps if b > bc]
            bn = min(above) if above else None
            print("  NOTE: interleaved classes on grid (disclosed)")
        for bb, tag in ((bc, "last-CAP"), (bn, "first-non-CAP")):
            if bb is None: continue
            _, c2, _, d2, _ = run(bb, w, 0.5, 1 / 200)
            print(f"  bracket {tag} b={bb}: dt=1/200 -> {c2} (d_inc={d2:.2f})")
elif stage == 'f2b':
    print("[F2b] w=2 OFF family, dt=1/200, both classifiers side by side")
    cls_r = {}; cls_o = {}
    for b in range(1, 9):
        line, cr, co = off_row(b, 2.0, 1 / 200)
        cls_r[b] = cr; cls_o[b] = co
        print("  " + line)
    # bracket under the primary (OFF-form) classifier, dt-union {1/200,1/400}
    caps = [b for b in cls_o if cls_o[b] == 'CAP']
    noncaps_above = [b for b in cls_o if caps and b > max(caps) and cls_o[b] != 'CAP']
    if caps:
        bc = max(caps)
        bn = min(noncaps_above) if noncaps_above else None
        for bb, tag in ((bc, "last-CAP"), (bn, "first-non-CAP")):
            if bb is None:
                print(f"  bracket {tag}: none above on grid")
                continue
            line, cr, co = off_row(bb, 2.0, 1 / 400)
            print(f"  bracket {tag} b={bb} dt=1/400: " + line)
    else:
        print("  NO CAP on grid under OFF-form classifier")
print(f"[{time.time()-t0:.0f}s]")
print("\nDone. Verdicts are read in n2b_funnel2_record.md against the prereg.")
