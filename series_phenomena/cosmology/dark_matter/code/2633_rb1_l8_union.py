#!/usr/bin/env python3
"""
PATCH 2633 -- R-B ITEM 1 EXECUTION under rb1_l8_truncation_prereg.md (2632) ONLY.
E_close(8) under the truncation-convention union. Machinery exec-loaded VERBATIM
from the registered 2557 artifact; reach variants bound in the chain namespace
(the 2574(c) lesson). Verdicts are read from the prereg against raw outputs.
"""
import numpy as np, time, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2557_reregistration_reach_s.py")).read()
cut = src.index('t0=time.time()')
ns = {'__name__': 'rb1'}
exec(src[:cut], ns)
scaffold_L = ns['scaffold_L']; dance_v8 = ns['dance_v8']
ssv_vectors = ns['ssv_vectors']; FLOOR = ns['FLOOR']; D = ns['D']

def make_reach(mode):
    """Reach-S with the truncation convention as the ONLY degree of freedom."""
    def reach(P, C, SP):
        NS = len(P); out = []
        counts = []
        for i in range(NS):
            dd = P - P[i]; r = np.sqrt((dd * dd).sum(axis=1)); r[i] = np.inf
            ki = i // 8
            if SP[i] == 'q':
                inpl = [j for j in range(NS) if SP[j] == 'q' and j // 8 == ki and r[j] < 1.8]
                axl = [j for j in range(NS) if SP[j] == 'q' and j // 8 != ki and r[j] < 1.3]
                ecp = [j for j in range(NS) if SP[j] == 'e' and r[j] < 0.6]
                qset = sorted(set(inpl + axl))
                counts.append(len(qset))
                if mode == 'INDEX':
                    qset = qset[:5]
                elif mode == 'DIST':
                    qset = sorted(qset, key=lambda j: r[j])[:5]
                # FULL: untruncated
                out.append(qset + ecp)
            else:
                eopp = sorted([j for j in range(NS) if SP[j] == 'e' and 0 < r[j] < 2.6],
                              key=lambda j: r[j])[:4]
                qown = [j for j in range(NS) if SP[j] == 'q' and r[j] < 0.6]
                out.append(eopp + qown)
        reach.last_counts = counts
        return out
    return reach

t0 = time.time()
print("=" * 78)
print("PATCH 2633 -- R-B ITEM 1: E_close(8) truncation-convention union (prereg 2632)")
print("=" * 78)

L = 8; kapL = 2 * np.pi / (L * D)
Pr, Cr, SPr = scaffold_L(L, kapL); Ps, Cs, SPs = scaffold_L(L, 0.0)
FREF = max(np.linalg.norm(ssv_vectors(Pr, Cr, SPr), axis=1).max(),
           np.linalg.norm(ssv_vectors(Ps, Cs, SPs), axis=1).max())

for mode in ('INDEX', 'DIST', 'FULL'):
    rf = make_reach(mode)
    rf(Pr, Cr, SPr)
    cr = rf.last_counts
    hist = {c: cr.count(c) for c in sorted(set(cr))}
    vals = []
    for dtf in (1 / 100, 1 / 50, 1 / 25):
        Er = dance_v8(Pr, Cr, SPr, FREF, dtf, rf)
        Es_ = dance_v8(Ps, Cs, SPs, FREF, dtf, rf)
        vals.append(Es_.mean() - Er.mean())
    above = all(v > FLOOR for v in vals)
    print(f"  [{mode:5s}] ring-count hist {hist} | E_close(8) = "
          + " ".join(f"{v:+7.1f}" for v in vals)
          + f"  | all > +FLOOR({FLOOR}): {above}")
print(f"[{time.time()-t0:.0f}s]")
print("\nDone. Verdicts are read in rb1_l8_union_record.md against the prereg.")
