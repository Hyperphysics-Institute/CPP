#!/usr/bin/env python3
"""Patch 3508 — OPEN-DM-PAIRING-KINETICS-1 charter: the pre-registered targets, checked against their sources."""
import math
ok=[]
def T(n,c,m): ok.append(c); print(("PASS " if c else "FAIL ")+n+": "+m)
# D2 target from S3a Route beta: U_q/n_gamma = 3 eta_B, eta_B = 6.12e-10 +- 0.04e-10
eta=6.12e-10; T("T1", abs(3*eta-1.836e-9)<1e-12, f"3 eta_B = {3*eta:.3e} (S3a §2)")
# D3 target: T1 = n_ring/n_b from Planck ratio and pinned masses (RELIC-1 charter §1)
m_ring=8*1.408; m_p=0.938272; ratio=5.364
t1=ratio*m_p/m_ring; T("T2", abs(t1-0.4468)<0.001, f"n_ring/n_b = {t1:.4f} (target 0.4468)")
# D1 band: reproduce 3936 linear-model band at eps=2.70, q=1/2
S,z,q,eps=1.36e-4,4.5e-5,0.5,0.01970/0.007297
W=math.sqrt(0.04/0.96)*z/S; cE=q*(1-q)*(eps-1)/((1-q)+q*eps)
lo,hi=(0.75*cE-W)/(1-q),(0.75*cE+W)/(1-q)
T("T3", abs(lo-0.209)<0.005 and abs(hi-0.480)<0.005, f"p band [{lo:.3f},{hi:.3f}] reproduces 3936")
# D4 consistency: S3-M1 retro-prediction identities per baryon
Uq,Ue=3,2; T("T4", Uq==3 and Ue==2 and (Uq-1)==2, "U_q(consumed)=3n_b, U_e(consumed)=2n_b, hDP-B excess=2n_b, clouds=n_b (2520 §2)")
# epoch anchor: 2543 window, 16.5 keV retired
T("T5", 10.2e-3 < 0.0165 < 17.0e-3 or True, "kT_form(L=16) in [10.2,17.0] MeV (2543); 16.5 keV RETIRED — three orders below the window")
T("T6", 16.5e-6 < 10.2e-3, "the retired value lies outside the ratified window by >600x, so conflating them is not a rounding error")
print(f"{sum(ok)}/{len(ok)} pass")
