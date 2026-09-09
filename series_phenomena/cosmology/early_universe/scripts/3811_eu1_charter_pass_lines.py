#!/usr/bin/env python3
"""
Patch 3811 (EU lane) -- OPEN-EU-1 derivation charter. Verify: the pass lines are arithmetic on
inputs the corpus already carries (A_s, r < 0.036, M_Pl, N_* = 57); nothing is derived here.

T1  The corpus's own single-field calibration of A_s (AS-NORMALIZATION S4: A_s = H^2/(8 pi^2 eps M^2),
    eps = 1/(2N_*)) gives H_* ~ 9e13 GeV -- ABOVE the tensor pass line 4.7e13 GeV (3810) by ~2x,
    i.e. r ~ 0.14. So the provisional calibration, if it were the mode structure, would FAIL the
    tensor bound. The charter's T-3 exists because of this.
T2  Spectator/delta-N structure: P_zeta = (H/2 pi M)^2 * S with S the dimensionless delta-N
    sensitivity (M^2 N_sigma^2). Single-field S = N_* = 57. The pass line H <= 4.7e13 GeV at the
    observed A_s requires S >= ~220, i.e. >= 3.9x the single-field sensitivity. This is the
    charter's frozen T-3 target: compute S from the corpus's own delta-N chain; pass iff S >= 220.
T3  Consistency of the two pass-line statements: S >= 220  <=>  H <= 4.7e13 GeV at A_s = 2.1e-9.
T4  The shot-noise route is excluded by 67 orders (AS-NORMALIZATION S2): A_s ~ (1/9)/n_bar at n_bar
    = e^171. Recorded as the charter's bar 3 (do not revisit).
"""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
M = 2.435e18; A_S = 2.1e-9; R_B = 0.036; N_STAR = 57.0
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
H_max = math.pi*M*math.sqrt(R_B*A_S/2)
eps_sf = 1/(2*N_STAR)
H_sf = M*math.sqrt(8*math.pi**2*eps_sf*A_S)
r_sf = 2*H_sf**2/(math.pi**2*M**2*A_S)
check("T1 single-field calibration H_* ~ 9e13 GeV exceeds the pass line 4.7e13 by ~2x (r ~ 0.14)",
      1.7 < H_sf/H_max < 2.3 and 0.12 < r_sf < 0.16, f"H_sf = {H_sf:.2e} GeV, ratio {H_sf/H_max:.2f}, r = {r_sf:.3f}")
S_req = A_S/((H_max/(2*math.pi*M))**2)
S_sf  = A_S/((H_sf/(2*math.pi*M))**2)
check("T2 spectator sensitivity required: S >= ~220 vs single-field S = 57 (>= 3.9x)",
      200 < S_req < 240 and abs(S_sf-N_STAR) < 1, f"S_req = {S_req:.0f}, S_sf = {S_sf:.1f}, ratio {S_req/S_sf:.2f}")
H_from_S = 2*math.pi*M*math.sqrt(A_S/S_req)
check("T3 S >= 220 <=> H <= 4.7e13 GeV (round trip)", abs(H_from_S/H_max-1) < 1e-9)
A_shot = (1/9)/math.exp(171)
check("T4 shot-noise route excluded by ~67 orders (bar 3)", 60 < math.log10(A_S/A_shot) < 75, f"{math.log10(A_S/A_shot):.0f} orders")
n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
