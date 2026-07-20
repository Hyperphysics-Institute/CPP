#!/usr/bin/env python3
"""
PATCH 2622 -- N2B-DISC-1 DEFECT DIAGNOSTIC (the 2612 pattern; 2574-class disclosed).
Question from the 2621 RD3 record: is the eta=0 Edrift=25.4 MeV at the C2 cell an
integrator-baseline property (falls with dt at a clean order) or an eta=0 engine
defect (does not fall)? Measurement only; the corrected prereg's gate is designed
FROM these numbers. Engine: registered 2602 objects via the 2609 exec-load cut,
verbatim n1_gamma (no instrumentation needed for Edrift).
"""
import numpy as np, time, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2602_hgamma_gates_b1.py")).read()
ns = {}
exec(src[:src.index("t0=_t.time(); trunc_mode='DIST'")], ns)
n1_gamma = ns['n1_gamma']; rung = ns['rung']; D = ns['D']; TAUC = ns['TAUC']
H4, C4, S4 = rung(1)

def cellE(v, eta, dtf, TC=120, b=0.0, w=4.0):
    H0 = np.vstack([H4, [b * D, 0.0, 4 * D]]); C0 = np.append(C4, -1.0)
    S0 = S4 + ['q']; V0 = np.zeros((5, 3)); V0[4] = [0, 0, -v]
    r = n1_gamma(H0, C0, S0, dtf, w, eta, TC=TC, V0=V0)
    return r['Edrift'], r['Sea']

t0 = time.time()
print("=" * 78)
print("PATCH 2622 -- DISC-1 DEFECT DIAGNOSTIC: Edrift scaling at the C2 cell")
print("=" * 78)

print("\n[D1] eta=0 (sink OFF), transit cell v=0.10 b=0 w=4 TC=120: Edrift vs dt")
E = {}
for dtf in (1/100, 1/200, 1/400, 1/800):
    e, s = cellE(0.10, 0.0, dtf)
    E[dtf] = e
    print(f"  dt=1/{int(1/dtf)}: Edrift={e:.3f} MeV  (Sea={s:.1e})")
r1 = E[1/100] / E[1/200]; r2 = E[1/200] / E[1/400]; r3 = E[1/400] / E[1/800]
print(f"  ratios per halving: {r1:.2f}, {r2:.2f}, {r3:.2f} "
      f"(order-1 truncation -> ~2.0; no-fall -> ~1.0)")

print("\n[D2] eta=0.5 (sink ON), same cell: Edrift vs dt (ON baseline for comparison)")
for dtf in (1/100, 1/200, 1/400):
    e, s = cellE(0.10, 0.5, dtf)
    print(f"  dt=1/{int(1/dtf)}: Edrift={e:.3f} MeV  (Sea={s:.1f})")

print("\n[D3] localization: isolated square (no incident), eta=0, TC=120: Edrift vs dt")
for dtf in (1/100, 1/200, 1/400):
    r = n1_gamma(H4, C4, S4, dtf, 4.0, 0.0, TC=120)
    print(f"  dt=1/{int(1/dtf)}: Edrift={r['Edrift']:.3f} MeV")

print("\n[D4] eta=0 high-v leg v=0.95 (the reported C2r cell): Edrift vs dt")
for dtf in (1/100, 1/200, 1/400):
    e, s = cellE(0.95, 0.0, dtf)
    print(f"  dt=1/{int(1/dtf)}: Edrift={e:.3f} MeV")

print(f"\n[{time.time()-t0:.0f}s]  Reading happens in the diagnostic record only.")
