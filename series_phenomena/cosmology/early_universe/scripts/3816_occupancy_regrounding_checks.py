#!/usr/bin/env python3
"""Patch 3816 -- occupancy re-grounding (Branch P, small-ball reading): arithmetic and consistency checks only; no constant adopted."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
lP=1.0
def Nstar(NCP,R): return math.log(NCP)/3 - math.log(R/lP)
check("T1 N* = 1/3 ln N_CP - ln(R_init/l_P): 1e84,l_P -> 64.5 = ln 1e28; 1e80 -> 61.4; 1e84,10 l_P -> 62.2",
      abs(Nstar(1e84,1)-64.5)<0.2 and abs(Nstar(1e84,1)-math.log(1e28))<1e-9 and abs(Nstar(1e80,1)-61.4)<0.2 and abs(Nstar(1e84,10)-62.2)<0.2)
spacing_req=(4*math.pi/3/1e83)**(1/3)
check("T2 1e83 addresses inside one Planck sphere need spacing <~ 3.5e-28 l_P; '1e30 per l_P' linear (1e-30) suffices, volumetric (1e-10) does not",
      abs(spacing_req-3.5e-28)/3.5e-28<0.05 and 1e-30<spacing_req and 1e-10>spacing_req, f"spacing_req={spacing_req:.2e} l_P")
a=[math.exp(N) for N in (0,10,30)]
nbar=[1e84*(1/x)**3 for x in a]
check("T3 n = rho * (4pi/3) l_P^3 with rho ~ a^-3 reproduces n ~ e^-3N; end n=1 at a_end/a_init = 1e28",
      all(abs(nbar[i]/(1e84*math.exp(-3*N)) -1)<1e-9 for i,N in enumerate((0,10,30))) and abs((1e84)**(1/3)/1e28-1)<1e-6)
K=12.0; D=12*1e84; v=D/K
check("T4 Moment 2: ~1e84 arrivals per GP vs cap K=12 -> v ~ 1e83, depth ~1.5e83 (AP-5); saturation by breadth, one Moment after empty registers",
      v>1e82 and math.ceil(1.5*v)>1e83)
Rmax84=math.exp(Nstar(1e84,1)-57); Rmax80=math.exp(Nstar(1e80,1)-57)
check("T5 pivot N_rem=57 survives for R_init up to ~1800 l_P (1e84) / ~80 l_P (1e80)",
      abs(Rmax84-1800)/1800<0.05 and abs(Rmax80-80)/80<0.05, f"{Rmax84:.0f}, {Rmax80:.0f}")
h=1e-6
check("T6 dN*/d ln R_init = -1 exactly; a contracted reach PSR_min changes the *perceived* end by 3 ln(PSR_min/l_P) e-folds",
      abs((Nstar(1e84,math.exp(h))-Nstar(1e84,1))/h + 1)<1e-4 and abs(3*math.log(0.1)+6.91)<0.01)
n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
