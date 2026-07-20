#!/usr/bin/env python3
"""
PATCH 2642 -- N2B-FUNNEL-3 EXECUTION under n2b_funnel3_prereg.md (2641) ONLY.
The w=4 funnel upper bound at dt-union {1/200,1/400}. Registered 2624 instrument
verbatim (sink-ON; registered-form classifier); grid walk b in {9,10,12,14,16},
both legs per cell, stop at first dt-stable non-CAP pair.
"""
import numpy as np, time, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2624_n2b_disc1_2.py")).read()
cut = src.index("stage=sys.argv[1]")
ns = {'__name__': 'funnel3', '__file__': os.path.join(HERE, "2624_n2b_disc1_2.py")}
exec(src[:cut], ns)
n1_gamma = ns['n1_gamma']; classify = ns['classify']; cell = ns['cell']; D = ns['D']

def run(b, dtf):
    r = cell(float(b), 0.10, 4.0, 0.5, dtf, disc=False)
    Hf = r['H']; cen4 = Hf[:4].mean(axis=0)
    d_inc = np.linalg.norm(Hf[4] - cen4)
    dcen = np.linalg.norm(cen4)
    return classify(r), d_inc, dcen

t0 = time.time()
print("=" * 78)
print("PATCH 2642 -- N2B-FUNNEL-3 (prereg 2641; verdicts read there)")
print("=" * 78)

print("[C-F3] convention-pin: b=9 w=4 ON dt=1/200 (must be CAP per 2640)")
c, d, _ = run(9, 1 / 200)
print(f"  b=9 dt=1/200: {c} (d_inc={d:.2f})")

print("[WALK] b in {9,10,12,14,16}, union {1/200,1/400}, stop at dt-stable non-CAP")
for b in (9, 10, 12, 14, 16):
    c1, d1, _ = run(b, 1 / 200)
    c2, d2, _ = run(b, 1 / 400)
    stab = (c1 == c2)
    print(f"  b={b}: 1/200 {c1}(d_inc={d1:.2f})  1/400 {c2}(d_inc={d2:.2f})  "
          f"{'dt-STABLE' if stab else 'dt-UNSTABLE'}"
          + (" [FRG]" if 'FRG' in (c1, c2) else ""))
    if stab and c1 != 'CAP':
        print(f"  STOP: first dt-stable non-CAP at b={b}")
        break
print(f"[{time.time()-t0:.0f}s]")
print("\nDone. Verdicts are read in n2b_funnel3_record.md against the prereg.")
