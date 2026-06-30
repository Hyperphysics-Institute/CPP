#!/usr/bin/env python3
"""
Patch 1823 -- (2) per-fusion sigma/m drop + the first sigma/m(v) curve (assembling the gate into a prediction).
==============================================================================================================
The 1822 gate gives a velocity-dependent FUSION FRACTION (penetrating tail). (2) supplies the per-fusion
sigma/m DROP, and together they give a first sigma/m(v) curve -- the discriminating prediction, in form.

(2) PER-FUSION DROP. DM-1: sigma/m = 0.11 N (rigid rod, N elements). A fusion takes 2 rods (each N) -> 1
X-cross (2N elements, 4 arms of ~N/2 from a central glueball). The drop sigma/m_X / sigma/m_rod brackets by
junction stiffness:
  - RIGID X (welded junction): ~same interactive extent as one rod but 2x the mass -> drop ~ 1/2.
  - FLEXIBLE X (single-point glueball -> arms pivot/fold to ~half extent): ~1/4 - 1/8.
  => drop factor in [2, 8]. The single-point glueball favors FLEXIBLE (arms pivot), which is also what the
     full SIDM fall needs; RIGID (x2) alone is too weak but COMPOUNDS over repeated fusions at high v.

CURVE. sigma/m(v) = sigma/m_0 * [1 - p_fuse(v) (1 - drop)], with the penetration/perpendicularity acceptance
p_fuse(v) = sqrt(1 - (v_thr/v)^2) for v > v_thr (isotropic impact angle; from 1822), else 0.
v_thr ~ 2500 km/s (central of the 1822 cluster band 1700-3900). All inputs pinned/geometric; drop is the one
O(1) bracket.
"""
import numpy as np
def pfuse(v,vthr): return float(np.sqrt(np.clip(1-(vthr/v)**2,0,1))) if v>vthr else 0.0

print("="*72); print("(2) per-fusion drop: sigma/m_X/sigma/m_rod in [1/8 (flexible), 1/2 (rigid)]"); print("="*72)
print("  single-point glueball junction -> flexible favored; rigid compounds over repeated fusions\n")

for N in (10,20):
    som0=0.11*N
    print(f"=== sigma/m(v), N={N}, sigma/m_0={som0:.2f} cm^2/g (v_thr=2500 km/s) ===")
    print(f"  {'env':<11}{'v':>6} | {'rigid(1/2)':>10} | {'flex(1/8)':>10}")
    for env,v in (('dwarf',60),('galaxy',250),('group',700),('cluster',2000),('Bullet',4000),('hi-tail',6000)):
        r=som0*(1-pfuse(v,2500)*0.5); f=som0*(1-pfuse(v,2500)*0.875)
        print(f"  {env:<11}{v:>6} | {r:>10.2f} | {f:>10.2f}")
    print()

print("="*72)
print("SHAPE: a velocity THRESHOLD at v_thr ~ 2500 km/s -- FLAT (= sigma/m_0, cores) below, FALLING above.")
print("This is NOT a power law; it is a threshold, which is distinctive and falsifiable.")
print("Obs bands: dwarfs want sigma/m ~ 0.5-5 (cores); clusters want <~ 0.1-1.")
print("- N~10 (sigma/m_0~1.1): cores OK at dwarf; typical cluster (2000<v_thr) stays ~1.1 (marginal);")
print("  Bullet 0.7(rigid)/0.41(flex). Viable if v_thr sits low (~1700) so 2000 clears it.")
print("- N~20 (sigma/m_0~2.2): better dwarf cores, but typical cluster un-suppressed ~2.2 -> TENSION")
print("  with cluster bound unless v_thr<2000 and/or multiple-fusion compounding deepens the fall.")
print()
print("HONEST TENSION: with v_thr~2500, TYPICAL clusters (~2000 km/s) sit BELOW threshold -> NOT")
print("suppressed; only Bullet-like mergers + high tail fall. Viable window exists (smaller N, v_thr at")
print("the low end ~1700-2000) but it is CONSTRAINED. Pinning it needs (i) v_thr to the low end, (ii) the")
print("full convolution over the velocity DISTRIBUTION (the high-v tail of a 2000 km/s cluster reaches")
print("past v_thr) + impact parameter, (iii) multiple-fusion compounding, (iv) the observational")
print("sigma/m-v compilation. This is a FIRST curve: the SHAPE (threshold) is the prediction; the depth")
print("and exact v_thr are bracketed.")
print("="*72)
