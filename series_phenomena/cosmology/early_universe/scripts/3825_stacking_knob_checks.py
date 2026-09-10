#!/usr/bin/env python3
"""Patch 3825 -- the stacking knob: does k (CPs per GP at ignition) close the e-fold budget,
and is it independent of the lattice-resolution knob? Arithmetic only; nothing adopted."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

lP=1.616e-35; Robs=4.40e26; a_ratio=7.415e28
K3=math.log(4*math.pi/3)/3
def N_of(k,s): return math.log(1/s)+math.log(k)/3+K3          # k per GP, s in units of lP
def N_master(ncp,R_over_lP): return math.log(ncp)/3-math.log(R_over_lP)
s0=((4*math.pi/3)*12/1e84)**(1/3)

# T1 -- the generalised identity, and that it reduces to 3823's at k = 12
check("T1 N = ln(lP/s) + (1/3)ln k + (1/3)ln(4pi/3); reduces to 3823's N = ln(lP/s) + 1.306 at k = 12",
      abs(N_of(12,s0)-N_master(1e84,1.0))<1e-9 and abs(math.log(12)/3+K3-1.306)<1e-3,
      f"N(k=12,s0) = {N_of(12,s0):.3f}")

# T2 -- k IS an independent knob at fixed lattice
k_req=12*math.exp(3*10.5)
check("T2 k is independent of s: at FIXED s0 the budget closes at k ~ 5.8e14 CPs per GP",
      abs(N_of(k_req,s0)-74.97)<0.1 and k_req>1e14,
      f"k_req = {k_req:.2e} (vs 12; factor {k_req/12:.1e}), N = {N_of(k_req,s0):.2f}")

# T3 -- but BOTH routes land on the same total CP count: N depends on N_CP alone (at fixed R_init)
ncp_via_k=k_req*(1e84/12)
ncp_via_s=12*(4*math.pi/3)*(1/1.0e-32)**3
check("T3 both routes converge on N_CP ~ 5e97: the budget cares about the TOTAL count, not how it is arranged",
      abs(math.log10(ncp_via_k)-math.log10(ncp_via_s))<0.3,
      f"via stacking {ncp_via_k:.2e}; via resolution {ncp_via_s:.2e}")

# T4 -- independent cross-check from the end condition (1 CP per Planck sphere at N = 75)
R_end=lP*math.exp(75.0)
ncp_end=(1/((4*math.pi/3)*lP**3))*(4*math.pi/3)*R_end**3
check("T4 end-condition cross-check: 1 CP per Planck sphere at N = 75 gives the same ~5e97 independently",
      abs(math.log10(ncp_end)-math.log10(ncp_via_k))<0.3,
      f"N_CP from end condition = {ncp_end:.2e}; ball at end = {R_end*1e3:.1f} mm")

# T5 -- the implied present-day CP number density: the independent pin
Vobs=(4*math.pi/3)*Robs**3
n_today=ncp_end/Vobs
n_dilute=(1/((4*math.pi/3)*lP**3))/a_ratio**3
check("T5 implied CP number density today ~1.4e17 /m^3, confirmed two ways (volume count and dilution)",
      abs(math.log10(n_today)-math.log10(n_dilute))<0.1,
      f"volume {n_today:.2e}/m3, dilution {n_dilute:.2e}/m3; mean separation {(Vobs/ncp_end)**(1/3)*1e9:.0f} nm")

# T6 -- k = 5.8e14 contradicts the founder's own 3814 ignition (one CP per icosahedral vertex, k = 12)
check("T6 the required k is ~4.8e13 x the founder's twelve -- it resurrects the stack he disowned at 3814",
      k_req/12>1e13, f"k_req/12 = {k_req/12:.2e}")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
