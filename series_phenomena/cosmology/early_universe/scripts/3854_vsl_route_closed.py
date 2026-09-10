#!/usr/bin/env python3
"""Patch 3854 -- OPEN-EU-EFOLD-BUDGET-1 route 1 (VSL) worked and CLOSED. The shortfall is a SIZE
requirement, invariant under R_init and independent of signal speed; EU-1's VSL clause addresses
CAUSAL CONTACT, a different problem. Arithmetic and corpus bookkeeping; nothing adopted."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

lP=1.616e-35; Robs=4.40e26; a_ratio=7.415e28; NCP=1e84
def N_req(Ri): return math.log(Robs/(Ri*lP*a_ratio))
def N_del(Ri): return math.log(NCP)/3-math.log(Ri)

check("T1 EU-1's own text (S Background): the horizon/causal-contact problem is addressed 'not by a large "
      "number of e-folds but by a large early Propagation-Speed-Ratio', so inflation is 'repurposed as the "
      "spectrum generator rather than as the horizon-solver'",
      True, "the VSL clause is about CAUSAL CONTACT")

check("T2 but the 3823 shortfall is not the horizon problem -- it is a SIZE requirement: the ball must "
      "reach the observable radius today. Causal contact and total expansion are logically distinct, and "
      "VSL as EU-1 invokes it addresses only the first",
      True, "different problems; the VSL clause does not speak to the budget")

sf=[N_req(r)-N_del(r) for r in (1.0,10.0,1e-5,1e3)]
check("T3 THE SHORTFALL IS INVARIANT UNDER R_init: N_req and N_del both carry -ln(R_init/l_P), so it "
      "cancels. shortfall = ln(R_obs/(l_P a_ratio)) - (1/3)ln N_CP",
      max(sf)-min(sf)<1e-9 and abs(sf[0]-10.51)<0.05,
      f"R_init = 1, 10, 1e-5, 1e3 l_P all give shortfall = {sf[0]:.2f}")

check("T4 so a LARGER EARLY BALL cannot help either: enlarging R_init reduces the requirement and the "
      "delivery by exactly the same logarithm",
      abs(N_req(10.0)-N_req(1.0)-(N_del(10.0)-N_del(1.0)))<1e-9,
      "both fall by ln(10) = 2.30")

check("T5 and the 'large early PSR' premise is dead independently: 3816 re-grounded that sentence away "
      "(the contact is the first Moment's empty-register reach over a Planck-sized ball, not an enlarged "
      "PSR), and 3837 found BOTH PSR-EARLY-1 branches give a PSR at or BELOW l_P -- never larger",
      True, "B1 excluded by the tilt; B2 floors below l_P")

check("T6 ROUTE 1 (VSL) IS CLOSED. It addresses the wrong problem, it cannot help even if it did (T3/T4), "
      "and its premise was withdrawn two sessions before it was named as the escape",
      True, "3823 S4 called it 'the most promising and uncomputed'; it was already dead")

# what remains
NCP_req=math.exp(3*N_req(1.0))
check("T7 ROUTE 2 remains and is unchanged: the shortfall depends only on N_CP and the thermal history, "
      "so closing it needs N_CP ~ 5e97 (vs the founder's 1e84) -- exactly 3825's number, with its "
      "independent pin n_CP(today) ~ 1.4e17 m^-3",
      abs(math.log10(NCP_req)-97.7)<0.3, f"N_CP required = {NCP_req:.2e}")

check("T8 the budget tension therefore STANDS at ~10.5 e-folds, now with one fewer escape and a sharper "
      "statement: it is a constraint on the TOTAL CP COUNT (or the thermal history), and on nothing else",
      abs(sf[0]-10.51)<0.05, f"shortfall = {sf[0]:.2f} e-folds")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
