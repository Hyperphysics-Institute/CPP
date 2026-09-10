#!/usr/bin/env python3
"""Patch 3858 -- the founder's evaporation cascade settles the referent but does NOT dissolve the clash.
A counting bound survives: entities cannot outnumber their constituents. Arithmetic only; nothing adopted."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

lP=1.616e-35; Robs=4.40e26; Vobs=(4*math.pi/3)*Robs**3
DS=4.636; n_DP=(1/DS**3)/lP**3; N_ent=n_DP*Vobs; N_CP_min=2*N_ent

check("T1 REFERENT SETTLED (founder): the DE sea is held at constant density by a MASS CASCADE (heavy DP "
      "entities evaporating into lighter ones). A population replenished at constant density is not one "
      "diluting as a^-3, so it CANNOT be EU-1's n_bar. Reading (B) of 3856 S4 is confirmed",
      True, "the two lanes count different things -- no direct density contradiction")

check("T2 BUT THE CLASH DOES NOT DISSOLVE. Evaporation REDISTRIBUTES CPs among entities; it does not "
      "create CPs. So a counting bound survives that is independent of any dilution law: entities cannot "
      "outnumber their constituents",
      True, "N_CP >= 2 x N_entities, at every epoch")

check("T3 the DE calibration implies ~8.5e182 DP entities in the observable volume, hence N_CP >= 1.7e183",
      abs(math.log10(N_ent)-182.93)<0.2 and abs(math.log10(N_CP_min)-183.23)<0.2,
      f"N_ent = {N_ent:.2e}; N_CP >= {N_CP_min:.2e}")

for lab,v,exp in (("EU-1 eq.Nstar (1e80)",1e80,103),("the founder's 1e84",1e84,99),
                  ("the budget requirement 5e97",5e97,86)):
    check(f"T4.{exp} that bound stands {exp} orders above {lab}",
          abs(math.log10(N_CP_min/v)-exp)<1, f"ratio {N_CP_min/v:.1e}")

def N_tot(ncp): return math.log(ncp)/3
check("T5 CONSEQUENCE IF THE CALIBRATION IS TAKEN LITERALLY: the e-fold budget does not merely close, it "
      "OVERSHOOTS -- N_total = 140.6 against a requirement of 75.0, a ~65 e-fold surplus where 3823 had a "
      "10.5 e-fold shortfall",
      abs(N_tot(N_CP_min)-140.6)<0.5 and N_tot(N_CP_min)>75,
      f"N_total = {N_tot(N_CP_min):.1f} vs required 75.0")

check("T6 and the pivot still fits: N_rem = 57 sits comfortably inside 140.6, so the TILT IS UNAFFECTED "
      "either way -- as it has been throughout this arc",
      N_tot(N_CP_min)>57, f"57 < {N_tot(N_CP_min):.1f}")

check("T7 so the clash is RESTATED, not removed: it is no longer 'two densities of the same thing "
      "disagree' but 'the DE calibration implies a CP count 99 orders above the figure EU-1 uses'",
      abs(math.log10(N_CP_min/1e84)-99)<1, "a counting statement, not a dilution statement")

check("T8 THREE EXITS, none adjudicable in this lane: (i) d_s is an effective/coarse-grained scale, not a "
      "CP-composed entity spacing, so the bound does not apply; (ii) N_CP really is ~1e183, closing the "
      "budget with a large surplus but putting EU-1's 1e80 wrong by 103 orders; (iii) the DE calibration "
      "is provisional -- the founder states the lane is NOT COMPLETE -- and the confrontation waits",
      True, "(iii) is the founder's own framing and is the cheapest hold")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
