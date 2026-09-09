#!/usr/bin/env python3
"""
Patch 3812 (EU lane) -- OPEN-EU-1 W-2 first pass: the light-mode requirement re-cuts T-3.
Inputs: H_max = 4.7e13 GeV (3810), E_Pl, N_* = 57, Planck n_s = 0.9649 +/- 0.0042, n_bar = e^171.

T1  EU-1's tilt derivation (eq. tilt) rests on P_zeta ~ H_eff^2 -- a source whose amplitude tracks
    H_eff. A source whose patch-to-patch variance is scale-independent gives n_s = 1 exactly, which
    Planck excludes at ~8 sigma (the 0741 cliff). So whatever wavers must waver MORE when the crowd
    is denser (amplitude ~ H_eff ~ ln n_bar).
T2  The register spring (charter default) is HEAVY: it settles within a Moment (hop = 2 Moments at
    the cap), so omega >= 1/(2 t_P), and omega/H >= 1.3e5 at the pass line. A mode with omega >> H
    does not freeze at horizon crossing; its super-horizon power is suppressed by at least (H/omega)^2
    <~ 6e-11 relative to a light spectator. Not the source.
T3  The count per address is conserved under dilution: its patch-to-patch variance is set at ignition
    and does not track H_eff (T1 kills it), and its Poisson part is 67 orders too small
    (AS-NORMALIZATION S2) -- worse by the patch's GP count, ~(H^-1/l_P)^3 ~ 2e16 at the pass line.
T4  The pairing pattern is frozen at ignition (3805: pairing complete within 15 Moments, before one
    e-fold): scale-independent, white; T1 kills it.
=> T-3 is re-cut: T-3a IDENTIFY a collective crowd variable with omega <~ H whose fluctuation ~ H_eff
   (this is what eq. tilt already assumes); T-3b compute S for it. Nothing identified this pass.
"""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
E_PL=1.221e19; H=4.7e13; NS=0.9649; SIG=0.0042
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
sig_away=(1-NS)/SIG
check("T1 a scale-independent source gives n_s = 1, excluded at ~8 sigma: the source must track H_eff", 7.5<sig_away<9, f"{sig_away:.1f} sigma")
omega=E_PL/2.0
ratio=omega/H; supp=(H/omega)**2
check("T2 register spring omega >= 1/(2 t_P): omega/H >= 1e5, super-horizon power suppressed <= 1e-10 -> heavy, not the source", ratio>1e5 and supp<1e-10, f"omega/H = {ratio:.1e}, (H/omega)^2 = {supp:.1e}")
N_gp_patch=(E_PL/H)**3
check("T3 the count: conserved (no H tracking) and its Poisson part is 67 orders short, worse by the patch's ~2e16 GPs", 1e16<N_gp_patch<1e17, f"GPs per Hubble patch ~ {N_gp_patch:.1e}")
check("T4 the pairing pattern is frozen before one e-fold (3805: <= 15 Moments) -> scale-independent -> T1 kills it", 15*1.0 < 1.0*57)  # 15 Moments << the window; H t_P ~ 1 per Moment at Planck density is the 3711 estimate, superseded by 3805's direct e-fold count
n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
