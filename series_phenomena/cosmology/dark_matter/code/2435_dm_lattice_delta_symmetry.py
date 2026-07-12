#!/usr/bin/env python3
"""
PATCH 2435 -- Stage 1 proper: the DM-lattice charge-switching duty cycle delta,
counted from the lattice's OWN symmetry (the way SS-1 got delta=1/3 from C3).
Replaces the borrowed SS-1 reference (1/3) in 2434 with the DM number.

THE SYMMETRY THAT FIXES IT. The core is an 8-qCP cube that is COLOR-NEUTRAL:
4 plus / 4 minus (OPEN-COSMO-DM-3, genesis 0880); likewise the 8-eCP shell is
4+/4-. Charge-switching (the SU(3)-type ZBW hop, TLA) moves charges among the
equivalent sites. The same-charge apposition duty cycle delta for a neighbour pair
= the fraction of neutral (4+/4-) configurations in which that pair is same-charge.

COMBINATORIAL FACT (exact, geometry-independent): for 8 sites with 4+/4-, ANY
fixed pair is same-charge with probability
    delta = [C(6,2)_++  +  C(6,2)_--] / C(8,4) = (15+15)/70 = 30/70 = 3/7.
This is the DM analog of SS-1's 1/3 -- fixed by the 4+/4- NEUTRALITY symmetry
rather than C3, and it is the SAME 3/7 for axial edges, in-plane edges, and
cube-diagonal appositions (the count doesn't see geometry).

WHY UNIFORM (not Boltzmann-suppressed) SAMPLING IS JUSTIFIED. delta=3/7 is the
uniform-weight (degenerate-hop) value. It applies iff the switching samples
configs broadly rather than dwelling in the opposite-charge (Madelung-low) set.
The founder's own physics supplies exactly that: the qCP core is JELLO / Earnshaw
(no static minimum to settle into; large ZBW excursions, free superposition), so
there is no static opposite-charge ground state to get trapped in -- the sampling
is quasi-uniform, the SS-1 degenerate-hop analog. (Dynamical dwelling could
suppress delta below 3/7; it would have to fall below the 0.22 crossover -- a >2x
suppression -- to flip the verdict.)

RESULT. delta_core (qCP-qCP, the stiffness-dominant pair) = 3/7 = 0.429. Feed into
2434's core-dominated deep-branch relation kappa_theta/E_bond = 2*delta:
    kappa_theta/E_bond = 2*(3/7) = 6/7 = 0.857  >> 0.43  -> STIFF, with margin.
delta=3/7 > borrowed 1/3 > 0.22 crossover -> the survive-at-drifted-mass lean is
STRENGTHENED, not marginal.

Run: python3 2435_dm_lattice_delta_symmetry.py   (exit 0 iff battery green)
"""
import numpy as np, itertools, sys, json
from math import comb
FAIL=[]
def check(n,ok,d):
    print(f"   [{'PASS' if ok else 'FAIL'}] {n}: {d}")
    if not ok: FAIL.append(n)

# ---- brute-force the 4+/4- combinatorial same-charge fraction on a cube ----
# cube vertices 0..7 at (x,y,z) in {0,1}^3
verts=list(itertools.product([0,1],repeat=3))
def edges():   # orthogonal nearest neighbours (differ in 1 coord)
    return [(i,j) for i in range(8) for j in range(i+1,8)
            if sum(a!=b for a,b in zip(verts[i],verts[j]))==1]
def face_diags():  # differ in 2 coords
    return [(i,j) for i in range(8) for j in range(i+1,8)
            if sum(a!=b for a,b in zip(verts[i],verts[j]))==2]
def space_diags(): # differ in 3 coords
    return [(i,j) for i in range(8) for j in range(i+1,8)
            if sum(a!=b for a,b in zip(verts[i],verts[j]))==3]

configs=[set(c) for c in itertools.combinations(range(8),4)]   # the 4 '+' sites; 70 configs
def same_frac(pairs):
    tot=0; same=0
    for pos in configs:
        for (i,j) in pairs:
            tot+=1
            ip=i in pos; jp=j in pos
            if ip==jp: same+=1
    return same/tot

f_edge=same_frac(edges()); f_face=same_frac(face_diags()); f_space=same_frac(space_diags())
f_all=same_frac(edges()+face_diags()+space_diags())

# ---- analytic value ----
delta_analytic=(comb(6,2)+comb(6,2))/comb(8,4)   # 30/70

# ================================================================ RUN
print("="*72)
print("DM-LATTICE delta from the 4+/4- neutrality symmetry (Patch 2435, stage 1)")
print("="*72)
print(f"  8-qCP cube, color-neutral 4+/4-  (analog of SS-1's C3 -> 1/3)")
print(f"  brute force over all C(8,4)={len(configs)} neutral configs:")
print(f"    same-charge fraction, orthogonal edges   : {f_edge:.4f}")
print(f"    same-charge fraction, face-diagonals     : {f_face:.4f}")
print(f"    same-charge fraction, space-diagonals    : {f_space:.4f}")
print(f"    all pair types (geometry-independent)    : {f_all:.4f}")
print(f"  analytic: delta = 30/70 = 3/7 = {delta_analytic:.4f}")
print()
delta=delta_analytic
print(f"  => DM-lattice delta = 3/7 = {delta:.3f}   (vs borrowed SS-1 ref 1/3 = 0.333)")
print(f"     uniform sampling justified: qCP core JELLO/Earnshaw -> no static")
print(f"     opposite-charge minimum to trap in -> quasi-uniform (SS-1 hop analog).")
print()

# feed into 2434 deep-branch relation kappa/E_bond = 2*delta
ratio_deep=2*delta
Nstab=14.07*ratio_deep
crossover=0.22
print(f"  MAKE-OR-BREAK (deep branch, 2434): kappa_theta/E_bond = 2*delta = 2*(3/7) = {ratio_deep:.3f}")
print(f"    vs threshold 0.43 -> {'STIFF (clears)' if ratio_deep>=0.43 else 'soft'} ; vs crossover {crossover} -> {'ABOVE with margin' if delta>crossover else 'below'}")
print(f"    N_stab ~ {Nstab:.0f} -> ring family N ~ {Nstab:.0f} ({Nstab*1.408:.0f} GeV), DD-clear")
print()
print(f"  VERDICT LEAN (stage 1 complete): delta=3/7 EXCEEDS both the borrowed 1/3 and")
print(f"  the 0.22 crossover -> the survive-at-drifted-mass lean is STRENGTHENED. The")
print(f"  make-or-break clears on the DM lattice's own symmetry number, not a borrowed one.")
print(f"  Remaining: (i) dynamical dwell suppression below 3/7 (would need >2x to flip),")
print(f"  (ii) which axial bond fragments (deep E_qq vs shallow E_ee -> drifted ring vs linear).")

json.dump({"delta_DM":delta,"f_edge":f_edge,"f_face":f_face,"f_space":f_space,
           "ratio_deep_2delta":ratio_deep,"crossover":crossover,"Nstab":Nstab},
          open('2435_results.json','w'),indent=2)

# ---------------------------------------------------------------- VERIFY
print("\n"+"-"*72); print("VERIFY BATTERY"); print("-"*72)
check("V1 delta = 3/7 exactly (analytic)", abs(delta_analytic-3/7)<1e-12, f"{delta_analytic:.6f}")
check("V2 brute-force edges match 3/7", abs(f_edge-3/7)<1e-9, f"{f_edge:.6f}")
check("V3 geometry-independent (edge=face=space=all)",
      max(abs(f_edge-f_face),abs(f_edge-f_space),abs(f_edge-f_all))<1e-9,
      f"edge{f_edge:.4f} face{f_face:.4f} space{f_space:.4f}")
check("V4 delta=3/7 exceeds SS-1 ref 1/3 AND the 0.22 crossover", delta>1/3 and delta>crossover,
      f"3/7={delta:.3f} > 1/3 and > 0.22")
check("V5 deep-branch kappa/E_bond=2delta clears 0.43 (survives)", ratio_deep>=0.43, f"2*3/7={ratio_deep:.3f}")
print("-"*72)
if FAIL: print("BATTERY RED:",FAIL); sys.exit(1)
print("BATTERY GREEN (5/5)"); sys.exit(0)
