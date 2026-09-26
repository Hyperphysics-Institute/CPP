#!/usr/bin/env python3
"""4299 -- founders_voice/4299: a DI-bit carries the message to move a CP one GP; a CP's emission must cover every GP on
the sphere at the smallest PSR.  Corpus inputs: PSR floor l_P/2 (founder ruling 1 Sep 2026, register limit);
GP spacing s: ~l_P/1e30 (founder GR-FE-1 ruling, "~10^30 GPs per PSR") or 9.9e-33 l_P (EU lane budget, Session 180)."""
import numpy as np
hbar=1.054571817e-34; c=299792458.0; G=6.67430e-11; me=9.1093837015e-31
lP=np.sqrt(hbar*G/c**3); tP=lP/c; pP=np.sqrt(hbar*c/G)*c; rC=hbar/(me*c); Rmin=lP/2
print("(1) GPs on the sphere at the smallest PSR (radius l_P/2) -- DI-bits per Moment needed to reach each at least once:")
for lab,s in (("GR-FE-1: s = l_P/1e30",lP/1e30),("EU budget: s = 9.9e-33 l_P",9.9e-33*lP)):
    N=4*np.pi*(Rmin/s)**2
    print(f"  {lab:28s}: N = 4 pi (R_min/s)^2 = {N:.2e}")
print("\n(2) what one DI-bit ('move one GP') changes: displacement s per Moment, i.e. a velocity step dv = s/t_P:")
for lab,s in (("s = l_P/1e30",lP/1e30),("s = 9.9e-33 l_P",9.9e-33*lP)):
    dv=s/tP
    for who,m,r in (("electron-scale CP at r_C",me/3,rC),("1 kg at 1 m",1.0,1.0)):
        dL=m*dv*r
        print(f"  {lab:16s}: dv = {dv/c:.1e} c;  {who:26s}: angular momentum per DI-bit = {dL/hbar:.2e} hbar")
print("  -> a fixed displacement per DI-bit gives angular momentum per DI-bit proportional to mass x lever arm:")
print("     it differs by ~1e35 between an electron and a 1 kg wheel. It is a quantum of LENGTH, not of action.")
print("\n(3) the coincidence (recorded, not claimed): (Planck momentum) x (smallest PSR) = m_P c x l_P/2 =",f"{pP*Rmin/hbar:.4f} hbar")
print("    identically, because l_P and m_P are defined with hbar; the only content is the 1/2 of the PSR floor.")
print(f"    and one Planck momentum is {pP/(me*c):.2e} x m_e c: no single DI-bit can hand that to an electron.")
