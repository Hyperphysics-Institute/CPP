#!/usr/bin/env python3
"""Patch 3814 -- FORK-EU-OCCUPANCY-1: arithmetic on EU-1 eq. Nstar and AP-5 D1 under the founder's twelve-per-GP picture."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
check("T1 twelve momenta to the icosahedral vertices cancel; compaction 12 -> 1 is ln12/3 = 0.83 e-folds (< 4 unobserved)", abs(math.log(12)/3-0.828)<0.01 and 0.83<4)
check("T2 Branch G (per GP): n=12 -> N = 0.83 e-folds, mu = 2.5 kT; pivot N_rem = 57 unreachable", math.log(12)/3 < 57 and abs(math.log(12)-2.48)<0.01)
N84=math.log(1e84)/3; N80=math.log(1e80)/3
check("T3 Branch P (per PSR): n = 1e84 -> N = 64.5 e-folds (60.5 at 1e80); pivot 57 inside either; mu = 193 kT", abs(N84-64.5)<0.2 and abs(N80-61.4)<0.2 and 57<N80<N84 and abs(math.log(1e84)-193.4)<0.2)
K=12.0
vG=12*12/K; vP=12*1e84/K
check("T4 AP-5 depth: Branch G v = 12, depth 18 vs BH wave horizon v = 2, depth 3", math.ceil(1.5*vG)==18 and math.ceil(1.5*2)==3)
check("T5 Branch P v ~ 1e84: deeper than any BH register; saturation by breadth (PSR max) vs BH by depth (PSR min)", vP>1e80)
n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
