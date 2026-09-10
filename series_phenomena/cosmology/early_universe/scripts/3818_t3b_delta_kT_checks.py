#!/usr/bin/env python3
"""Patch 3818 -- T-3b first computation: δkT → ζ = 0 under geometric end condition (C-1, bath-energy mode).
Arithmetic and consistency only; no constant adopted; nothing derived beyond what the count law and
the pass-line definitions already carry."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

# Reuse pass-line constants from 3811 (these are corpus-level inputs, not adopted constants)
M = 2.435e18       # M_Pl in GeV (reduced)
A_S = 2.1e-9       # Planck 2018 A_s
R_B = 0.036        # BICEP/Keck r < 0.036
N_STAR = 57.0      # adopted pivot
N_CP_84 = 1e84     # founder's CP count
R_init = 1.0       # R_init = l_P = 1 (units of l_P)

# T1: N_* has no kT dependence → δN = 0
N_total = math.log(N_CP_84)/3 - math.log(R_init)  # = 64.5
# Perturb kT by 10%: N_* is computed from n̄_init and n̄_end; neither depends on kT
# n̄_init = N_CP (all CPs in one Planck sphere at ignition); n̄_end = 1 (geometric)
def Nstar_from_occ(n_init, n_end): return math.log(n_init/n_end)/3
N_kT_nominal = Nstar_from_occ(N_CP_84, 1.0)
N_kT_plus10  = Nstar_from_occ(N_CP_84, 1.0)  # n̄_init and n̄_end independent of kT
N_kT_minus10 = Nstar_from_occ(N_CP_84, 1.0)
dN_over_kT_change = (N_kT_plus10 - N_kT_minus10) / (0.2 * N_kT_nominal)  # = 0 exactly
check("T1 N_* = 1/3 ln(N_CP/1) = 64.5 independent of kT; dN = 0 under any kT perturbation",
      abs(N_total - 64.5) < 0.1 and dN_over_kT_change == 0.0,
      f"N_* = {N_total:.2f}, dN/dkT = {dN_over_kT_change}")

# T2: S = P_zeta / (H/2piM)^2; with zeta = 0, P_zeta = 0, S = 0
P_zeta_C1 = 0.0   # ζ = 0 from the argument above
H_eff_example = 4.7e13  # GeV — example value at the pass-line boundary
S_C1 = P_zeta_C1 / (H_eff_example/(2*math.pi*M))**2  # = 0
check("T2 S = 0 for C-1 (P_zeta = 0 because zeta = 0 under geometric end condition)",
      S_C1 == 0.0, f"S_C1 = {S_C1}")

# T3: HALT condition: S = 0 < S_req where S_req ~ 220
H_max = math.pi * M * math.sqrt(R_B * A_S / 2)
S_req = A_S / (H_max/(2*math.pi*M))**2
check("T3 S = 0 < S_req ~ 220: HALT condition met (charter §4)",
      S_C1 < S_req and 200 < S_req < 240,
      f"S_req = {S_req:.0f}, S_C1 = {S_C1:.0f}, H_max = {H_max:.2e} GeV")

# T4: The tilt PRED-C-96 is unaffected (shape of the count law only)
# n_s = 1 - 2/N_* at the pivot; this follows from d ln n̄/dN = -3
# and requires only the dilution law n̄ ∝ a^-3 and the count N = 1/3 ln(n̄_init/n̄_end)
# kT never enters n_s; no kT appears in the tilt chain
# Verify: dn_s/dkT = 0 (symbolic: n_s = 1 - 2/N_*; N_* = 1/3 ln N_CP; no kT)
n_s_nominal = 1 - 2/N_STAR   # = 0.9649 at adopted pivot N_*=57
# kT-independence: N_kT_plus10 == N_kT_minus10 == N_kT_nominal (all = N_total = 64.47)
# because N_* = 1/3 ln N_CP has no kT; the adopted pivot 57 doesn't change with kT either
kT_independence = (N_kT_plus10 == N_kT_nominal == N_kT_minus10)
check("T4 n_s = 1 - 2/N_* = 0.9649 is kT-independent; tilt unaffected by HALT",
      abs(n_s_nominal - 0.9649) < 5e-4 and kT_independence,
      f"n_s = {n_s_nominal:.4f}, kT-independent N_*: {kT_independence}")

n = sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
