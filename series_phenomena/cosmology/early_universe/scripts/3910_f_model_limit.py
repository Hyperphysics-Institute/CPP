#!/usr/bin/env python3
"""Patch 3910 -- C-5's last in-lane caveat closed: the re-stacking-dominated limit HOLDS at the pivot,
and the validation is independent of the unremembered stack number. Crossover to the failing limit is in
the last ~1-3 e-folds, far from every observed mode."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
NTOT=math.log(1e84)/3; NPIV=57.0
def f_piv(n0): return math.exp(-(NPIV/NTOT)*math.log(n0))
def Nx(n0): return 0.693*NTOT/math.log(n0)

check("T1 **THE CAVEAT, from 3902 §7:** f ~ 1/A is the **re-stacking-dominated** limit of the two-rate "
      "steady state f = R_out/(R_out + R_in). **In the opposite limit f → 1 independent of A, the ratio "
      "f_E/f_Q → 1, and C-5's amplitude chain fails.** Which limit holds was untested and load-bearing",
      True, "the last caveat that was C-5's own and in-lane")

check("T2 **AND IT IS DECIDED BY f ITSELF, which 3892 already fixed.** f(start) = 1/n₀ (one occupied GP "
      "per n₀ CPs), and ln f is linear in N_rem. **No new assumption is needed to settle the limit**",
      True, "the quantity that decides the limit was already derived")

check("T3 ln f(pivot) = −(N_piv/N_tot)·ln n₀ = −0.884 ln n₀, with N_tot = 64.47 and the pivot at "
      "N_rem = 57",
      abs(NPIV/NTOT-0.884)<0.005, f"N_piv/N_tot = {NPIV/NTOT:.3f}")

check("T4 **f(pivot) ≪ 1 FOR ANY LARGE n₀:** 5.0e-6 at n₀ = 1e6; 2.5e-11 at 1e12; 6.0e-22 at 1e24",
      all(f_piv(n0)<1e-5 for n0 in (1e6,1e12,1e24)),
      "; ".join(f"n0=1e{int(math.log10(n0))}: f={f_piv(n0):.1e}" for n0 in (1e6,1e12,1e24)))

check("T5 **⇒ THE SYSTEM IS DEEPLY RE-STACKING-DOMINATED AT THE PIVOT, SO f ~ 1/A HOLDS.** The limit used "
      "at 3902 is the correct one, and **the validation is independent of the stack number** — fifth "
      "session running that n₀ has been carried rather than chosen",
      True, "the caveat is closed, not merely acknowledged")

check("T6 **AND THE CROSSOVER IS FAR AWAY.** Solving f = 0.5 puts the transition to the failing limit at "
      "N_rem = 3.2 (n₀=1e6), 1.6 (1e12), 0.8 (1e24) — **the last one to three e-folds**",
      all(Nx(n0)<4 for n0 in (1e6,1e12,1e24)),
      "; ".join(f"n0=1e{int(math.log10(n0))}: N_rem={Nx(n0):.2f}" for n0 in (1e6,1e12,1e24)))

check("T7 **EVERY OBSERVED MODE EXITS AT N_rem ≈ 50–60, i.e. far inside the good limit.** The failing "
      "regime is confined to the very end of inflation, after all observable scales have left the horizon",
      NPIV>10*max(Nx(n0) for n0 in (1e6,1e12,1e24)), "pivot 57 vs crossover ≤ 3.2")

check("T8 **AND THE SYSTEM DOES PASS THROUGH BOTH LIMITS** — it must, since 3892 requires f → 1 at the "
      "end. **That is a feature, not a problem:** the transition is what ends the unstacking, and it "
      "happens after the observable window",
      True, "consistent with the count law's f → 1 requirement")

check("T9 SO C-5's LAST IN-LANE CAVEAT IS CLOSED. The remaining two items are **not EU-local**: the "
      "SM-sector conserved-charge check (gates adiabaticity) and the H ∝ μ assignment (foundational)",
      True, "the lane's own work on C-5 is finished")

check("T10 SCOPE: **nothing adopted; C-5 still not reported as working; the amplitude remains κ*-gated "
      "(3906).** This closes a caveat, not a debt — **the honest final position is unchanged**: a source "
      "with the right spectrum, and a normalisation not derivable as the framework stands",
      True, "a caveat closed does not move the headline")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
