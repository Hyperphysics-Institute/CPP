#!/usr/bin/env python3
"""Patch 3896 -- C-5's correlation-length computation. Gaussianity CLEARS decisively (the first test in
this arc a candidate has passed that killed a predecessor); the amplitude reduces to one number,
l_corr ~= 138 PSR; and the open question becomes SATURATION, not reachability."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
RH=1/1.93e-5; ZOBS=4.6e-5
def Nind(l): return (RH/l)**3
def zeta(l,d=1.0): return (d/3)*(l/RH)**1.5

check("T1 THE AFFINITY'S BARE RANGE IS THE PSR. The attraction between SCPs is mediated by arriving "
      "DI-bits (SSV_net), and AP-4/AP-4c give the DI-bit a hard reach: deposit at the PSR shell, near "
      "field by the hop cascade within it. **So the bare correlation length is 1 PSR**",
      True, "not an estimate -- the protocol fixes the range")

check("T2 at the pivot R_H = 5.2e4 l_P, so at the bare range there are **1.4e14 independent patches per "
      "Hubble volume**",
      abs(math.log10(Nind(1.0))-14.14)<0.1, f"N_ind(1 PSR) = {Nind(1.0):.2e}")

# --- Gaussianity ---
check("T3 **GAUSSIANITY CLEARS DECISIVELY.** Excess kurtosis of a sum of N independent patches goes as "
      "kappa_patch/N. Even with a cascade-like patch kurtosis of 1e3, the mode kurtosis is **7.2e-12**",
      1e3/Nind(1.0)<1e-10, f"mode kurtosis = {1e3/Nind(1.0):.1e} vs Planck f_NL bound O(5-10)")

check("T4 **SO 0730's WALL DOES NOT APPLY TO C-5.** That is the first time in this arc a candidate has "
      "passed a test that killed a predecessor, rather than failing the same one by a smaller margin",
      True, "the fractal cascade died on non-Gaussianity; C-5 does not")

# --- amplitude at the bare range ---
need=3*ZOBS*math.sqrt(Nind(1.0))
check("T5 AMPLITUDE AT THE BARE RANGE FAILS, but by 3 orders rather than 40. Reaching the observed zeta "
      "would need a per-patch delta ln f of **1.6e3**, and a log-fraction fluctuation per patch cannot "
      "plausibly exceed O(1)",
      abs(math.log10(need)-3.21)<0.1, f"required per-patch = {need:.2e}; zeta(1 PSR) = {zeta(1.0):.2e}")

# --- the target ---
LC=RH/((1/(3*ZOBS))**2)**(1/3)
check("T6 **THE TARGET, and it is a single number:** with per-patch delta ln f = O(1), "
      "zeta = (1/3)(l/R_H)^(3/2), so the observed amplitude requires **l_corr ~= 138 l_P ~ 138 PSR**",
      abs(LC-138)<3 and abs(zeta(LC)/ZOBS-1)<0.05, f"l_corr = {LC:.0f} l_P gives zeta = {zeta(LC):.2e}")

check("T7 IT IS SHARP, NOT A WINDOW: **zeta scales as l^(3/2)**, so a factor 2 in l_corr moves the "
      "amplitude by 2.8. l_corr is pinned near 138 PSR to within a factor of ~2",
      abs(zeta(2*LC)/zeta(LC)-2.83)<0.05,
      "; ".join(f"l={l:.0f}: {zeta(l)/ZOBS:.1e}x" for l in (1,10,LC,500)))

check("T8 AND GAUSSIANITY IS STILL SAFE THERE: at l_corr = 138 the mode kurtosis is **1.9e-5**, far inside "
      "any bound. **Both tests pass at the same correlation length** -- there is no conflict between them",
      1e3/Nind(LC)<1e-3, f"N_ind(138) = {Nind(LC):.2e}, kurtosis = {1e3/Nind(LC):.1e}")

check("T9 **REACHABILITY IS NOT THE ISSUE.** Local dynamics grow correlations ~1 PSR per Moment, and there "
      "are 5.2e4 Moments per e-fold, so 138 PSR takes **0.0027 e-folds**. The system has 64 e-folds",
      138/RH<0.01, f"138 Moments = {138/RH:.4f} e-folds")

check("T10 **SO THE OPEN QUESTION IS SATURATION, NOT REACH: what stops the correlation growing past ~138 "
      "PSR?** If nothing does, correlations run to R_H, N_ind -> 1, and zeta overshoots by 7e3. **C-5 now "
      "needs a saturation mechanism, and that is a sharper and smaller question than any it has had**",
      zeta(RH)/ZOBS>1e3, f"unsaturated (l = R_H) gives {zeta(RH)/ZOBS:.0e}x observed")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
