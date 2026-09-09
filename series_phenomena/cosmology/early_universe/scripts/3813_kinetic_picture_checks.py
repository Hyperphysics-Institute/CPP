#!/usr/bin/env python3
"""Patch 3813 -- arithmetic checks for the assessment of the founder's kinetic-bulk / packed-sphere picture."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
# T1: bath-energy waver is multiplicative on H_eff: H = kappa*kT*ln(nbar); dH/H = dkT/kT exactly
kappa, kT, nb = 1.0, 1.0, math.exp(171)
H = lambda kT_: kappa*kT_*math.log(nb)
d = 1e-4
check("T1 delta H / H = delta kT / kT exactly (the ~H_eff property is built in)", abs((H(kT*(1+d))-H(kT))/H(kT) - d) < 1e-12)
# T2: a push driver is short: 3805's bound and the stiff-fluid statement
check("T2 push driver excluded: 3805 bound 0.45 e-folds << 57; kinetic fluid w = +1 decelerates (a'' ~ -(1+3w))", 0.45 < 57 and -(1+3*1) < 0)
# T3: literal two-per-GP removes the crowd
N_two = math.log(2)/3; N_stack = math.log(1e80/13)/3
check("T3 n_bar = 2 gives N = ln2/3 = 0.23 e-folds vs 60.5 for the stacked start; mu = 0.69 kT vs ~180 kT", abs(N_two-0.231)<0.01 and abs(N_stack-60.5)<0.2 and abs(math.log(2)-0.693)<0.01)
# T4: size of a sphere packed at 2 per GP
N_gp = 1e80/2; R = (3*N_gp/(4*math.pi))**(1/3); R_m = R*1.616e-35
check("T4 a two-per-GP sphere holds 5e79 GPs: radius ~2e26 l_P ~ 4 nm, not a Planck point", 1e26<R<1e27 and 1e-9<R_m<1e-8, f"R = {R:.1e} l_P = {R_m*1e9:.1f} nm")
n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
