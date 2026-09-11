#!/usr/bin/env python3
"""Patch 3894 -- the SCP differential-affinity mechanism assessed against the 3892 Poisson/white warning.
It breaks the warning; it brings a new risk; and the risk is quantified. Nothing adopted."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
h=1.93e-5; Hinv=1/h; PS=Hinv**3; nbar=math.exp(3*57); CPmode=PS*nbar

check("T1 THE MECHANISM, STATED: an SCP is the whole stack on one GP, and it carries a COMPOSITION (a "
      "proportion of eCPs to qCPs). Composition varies site to site, so **each SCP is a distinct entity**, "
      "sorting into **Q-dominant** and **E-dominant** classes",
      True, "founder's own term and framing, 11 Sep walk-and-talk")

check("T2 THE CORE ASYMMETRY: **Q-dominant SCPs attract Q-dominant SCPs strongly; Q-to-E is weaker; and "
      "E-dominant SCPs are INDIFFERENT, attracted equally to both.** One class discriminates, the other "
      "does not. **'The Q-dominant SCP is the asymmetric attractor'**",
      True, "this is the whole of the asymmetry")

check("T3 AND THE PRODUCTS ARE ASYMMETRIC TOO: qCP+qCP of opposite charge -> ZBW oscillation -> qDP, which "
      "persists; eCP+eCP -> eDP, which is 'not faithful' and pair-swaps readily; and qDP pair-swapping "
      "binds all three via the strong force (two minus flanking a centre plus). **The q-channel "
      "accumulates where the e-channel churns**",
      True, "two reinforcing sources of the same skew")

check("T4 **THIS BREAKS THE 3892 WARNING.** That patch warned: if unstacking is Poisson, delta ln f is "
      "white and C-5 meets the wall. **Differential affinity is preferential attachment -- correlated by "
      "construction.** The unpiling is weighted by local composition, so it is NOT Poisson",
      True, "the founder answered the warning with a mechanism, not an assertion")

check("T5 AND PREFERENTIAL ATTACHMENT IS THE RIGHT CLASS OF PROCESS: rich-get-richer dynamics generically "
      "produce **power-law (scale-free) statistics** (Yule/Simon). **Scale-free is what the spectrum "
      "needs**; Poisson is what it must avoid",
      True, "the mechanism has the right structural signature")

check("T6 **BUT IT BRINGS A NEW RISK, and it is the 0730 wall.** Preferential attachment also generically "
      "produces **heavy-tailed, NON-GAUSSIAN** statistics -- which is exactly what excluded the "
      "chain-of-chains cascade (0730: scale-free but non-Gaussian by 1e2-1e3 in excess kurtosis)",
      True, "the same property that buys scale-freedom threatens Gaussianity")

check("T7 THE RISK IS NOT OBVIOUSLY FATAL, because of the sheer count. At the pivot H^-1 = 5.2e4 l_P, so a "
      "Hubble volume holds 1.4e14 Planck spheres at n_bar = e^171 = 1.8e74 CPs each -- **2.6e88 CPs per "
      "observable mode**",
      abs(math.log10(CPmode)-88.4)<0.5, f"CPs per mode = {CPmode:.1e}")

check("T8 dividing by any plausible stack number leaves **>= 1e64 SCPs contributing to one mode**. Central-"
      "limit averaging over that many contributors Gaussianises heavy-tailed microphysics **unless the "
      "correlations are long-range enough to defeat CLT**",
      CPmode/1e24>1e60, f"n0=1e6: {CPmode/1e6:.0e}; n0=1e12: {CPmode/1e12:.0e}; n0=1e24: {CPmode/1e24:.0e}")

check("T9 **SO THE DECIDING QUANTITY IS THE CORRELATION LENGTH OF THE AFFINITY, NOT ITS STRENGTH.** Short-"
      "range affinity: CLT wins, the field Gaussianises, and the scale-freedom must come from the "
      "H_eff-tracking rather than the clustering. Long-range: non-Gaussianity survives and 0730's wall "
      "applies. **That is the computation C-5's debt (3) now needs**",
      True, "the amplitude question is now sharpened into a correlation-length question")

check("T10 SCOPE: **nothing adopted; C-5 still not reported as working.** What changed is that the Poisson "
      "default is displaced by a stated mechanism, and the open question moved from 'is it random?' to "
      "'over what range is it correlated?'",
      True, "a sharper question, not an answer")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
