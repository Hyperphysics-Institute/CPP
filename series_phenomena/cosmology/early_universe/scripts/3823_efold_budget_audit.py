#!/usr/bin/env python3
"""Patch 3823 -- e-fold budget audit forced by the founder's edge question (3822).
Two results: (i) under packing closure the e-fold total is a function of GP resolution ALONE;
(ii) the re-grounded count (64.5) falls ~10 e-folds short of inflating the ball to the observable
universe. Standard post-inflation thermal history assumed and STATED as an assumption."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

lP=1.616e-35; MPl=2.435e18; GeV_K=1.1605e13; T0=2.7255
Robs=4.40e26; Mpc=3.086e22; NCP=1e84; g=106.75
K=math.log((4*math.pi/3)*12)/3     # = 1.308

def Nstar(ncp,R_over_lP): return math.log(ncp)/3 - math.log(R_over_lP)
def spacing_over_lP(R_over_lP,ncp=NCP): return R_over_lP*((4*math.pi/3)*12/ncp)**(1/3)

# T1 -- the identity N = ln(lP/s) + 1.308 under packing closure
ok=True
for R_over in (1.0,1e-3,2.75e-5,1e-8):
    s=spacing_over_lP(R_over)
    ok &= abs(Nstar(NCP,R_over) - (math.log(1/s)+K)) < 1e-9
check("T1 under packing closure N = ln(lP/s) + 1.308 exactly: the e-fold total depends on GP RESOLUTION ALONE",
      ok, f"K = {K:.4f}; verified at R/lP = 1, 1e-3, 2.75e-5, 1e-8")

# T2 -- required e-folds for the ball to contain the observable universe (standard history)
Hp=4.7e13                                   # tensor-line ceiling: the most FAVOURABLE case
Treh=(30*3*Hp**2*MPl**2/(math.pi**2*g))**0.25
a_ratio=Treh*GeV_K/T0*(g/3.91)**(1/3)
N_req=math.log(Robs/(lP*a_ratio))
check("T2 observable universe requires N >= ~75 from R_init = lP (H at the tensor ceiling = best case)",
      74<N_req<76, f"T_reh = {Treh:.2e} GeV, a_0/a_end = {a_ratio:.2e}, N_req = {N_req:.1f}")

# T3 -- the shortfall at the re-grounded count
N_have=Nstar(NCP,1.0)
short=N_req-N_have
check("T3 shortfall: 64.5 delivered vs ~75 required -> ~10 e-folds short",
      9<short<12, f"N_have = {N_have:.1f}, shortfall = {short:.1f}")

# T4 -- where the ball's edge sits today at N = 64.5
R_now=lP*math.exp(N_have)*a_ratio
check("T4 at N = 64.5 the WHOLE ball today is ~0.4 Mpc -- 5 orders inside the observable universe",
      0.1<R_now/Mpc<1.0, f"ball today = {R_now/Mpc:.2f} Mpc vs observable {Robs/Mpc:.0f} Mpc")

# T5 -- lower reheating makes it WORSE (a_ratio falls, N_req rises): the bound is one-sided
Hp_low=1e10
Treh_l=(30*3*Hp_low**2*MPl**2/(math.pi**2*g))**0.25
a_l=Treh_l*GeV_K/T0*(g/3.91)**(1/3)
check("T5 the requirement is one-sided: lower H (lower T_reh) raises N_req, so ~75 is a FLOOR",
      math.log(Robs/(lP*a_l))>N_req, f"at H = 1e10 GeV, N_req = {math.log(Robs/(lP*a_l)):.1f}")

# T6 -- resolution needed to close the budget, vs the glossary's unverified estimate
s_req=math.exp(-(N_req-K))
N_at_1e30=math.log(1e30)+K
check("T6 closing the budget needs >= ~1e32 GPs per lP linearly; the unverified 1e30 estimate gives only ~70.4",
      1e31<1/s_req<1e33 and 70<N_at_1e30<71,
      f"s_req = {s_req:.2e} lP (= {1/s_req:.2e} per lP); N at 1e30 = {N_at_1e30:.1f}, still {N_req-N_at_1e30:.1f} short")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
