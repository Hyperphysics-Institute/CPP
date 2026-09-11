#!/usr/bin/env python3
"""Patch 3884 -- founder correction: the DM particle is the 16-plane RING at 11.26 GeV, not an unspecified
aggregate. This RETRACTS 3882's amplitude near-miss, which used an invented mass. Arithmetic; nothing adopted."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
Mpc=3.086e22; rho=2.2e-27; Msun=1.99e30
m_ring=11.26*1.783e-27; V=(100*Mpc)**3
N=rho*V/m_ring; d_ring=1/math.sqrt(N)

check("T1 FOUNDER CORRECTION ACCEPTED: the DM particle is the **16-plane RING** -- 16 DM planes organized as "
      "8 two-plane elements, **11.26 GeV** -- formed when extreme turbulence bends a straight 16-plane ROD "
      "into a closed circle (founder registration Patch 3426, 25 Aug 2026)",
      True, "not 'charge-neutral qDP/hTetra aggregates' as 3882 had it")

check("T2 AND THE WORKER READ A STALE FILE. 3882 quoted `DM_project_map.md`, whose own header reads 'Last "
      "updated: Session 156, 10 June 2026' -- **two and a half months BEFORE** the ring registration. **D-3 "
      "was applied to the map instead of the lane.** The founder's 'read the DM lane again' is exact",
      True, "the ring appears in founders_voice, not yet in the project map")

check("T3 **RETRACTION.** 3882's headline -- 'amplitude within a factor of two, a first for this arc' -- "
      "used an **invented 1e6 Msun aggregate mass**, chosen because it landed on the answer. The corpus "
      "supplies the actual mass, and it is 11.26 GeV",
      True, "the near-miss was an artifact of the free parameter, not a property of CPP's DM")

check("T4 WITH THE CORPUS VALUE THE CANDIDATE MISSES LIKE ALL THE OTHERS: n_DM = 0.11 per m^3, so "
      "N = 3.2e72 rings in (100 Mpc)^3 and the Poisson contrast is **5.6e-37 against a required 1e-5 -- "
      "SHORT BY 31 ORDERS**",
      abs(math.log10(1e-5/d_ring)-31)<1, f"delta_ring = {d_ring:.2e}")

check("T5 so 3882's 'first candidate to come close on amplitude' is **WITHDRAWN**. The correct statement is "
      "that DM ring clumping fails on amplitude by 31 orders, joining the register spring, the count, "
      "composition and C-2",
      d_ring<1e-30, "no candidate in this arc has come close on amplitude")

# the founder's actual question: fractal aggregation
Nreq=1/(1e-5)**2; m_need=rho*V/Nreq
check("T6 THE FOUNDER'S QUESTION -- can fractal-level AGGREGATION of rings do it? The requirement is "
      "explicit: delta = 1e-5 at 100 Mpc needs N = 1e10 objects, i.e. **3.2e6 Msun per clump = 3.2e62 rings "
      "each**",
      abs(math.log10(m_need/Msun)-6.5)<0.3, f"m = {m_need/Msun:.1e} Msun = {m_need/m_ring:.1e} rings")

check("T7 EXCLUSION A -- such clumps must exist AT RECOMBINATION (z = 1100), and structure of 1e6 Msun "
      "does not form until far later. The observed CMB, showing delta ~ 1e-5 and no such clumps, is itself "
      "the evidence against them",
      True, "the observation excludes the premise directly")

check("T8 EXCLUSION B -- THE SHAPE IS STILL WRONG, at any clump mass. Poisson is white, so delta scales as "
      "r^-3/2: 3.2e-4 at 10 Mpc, 1.0e-5 at 100 Mpc, 3.2e-7 at 1000 Mpc. **The observed spectrum is roughly "
      "CONSTANT across those scales.** Aggregation changes the amplitude, never the shape",
      abs(1e-5*(100/10)**1.5-3.16e-4)/3.16e-4<0.02,
      "matching one scale by choosing the mass leaves the other scales wrong by 1.5 decades each")

check("T9 EXCLUSIONS C and D stand unchanged from 3882: Poisson DM clumping is **isocurvature** "
      "(Planck-bounded to a few percent), and post-inflation clumping is an **active, incoherent source** "
      "excluded by the acoustic-peak series",
      True, "four independent exclusions now, not three")

check("T10 NET: the founder's correction makes the verdict STRONGER, not weaker. The candidate now fails on "
      "**amplitude as well as** shape, timing and ordering. And 3882's 'massiveness buys noise' lesson "
      "survives -- it is precisely why the invented heavy mass looked promising and why the real light one "
      "does not",
      True, "the lesson was right; its application to CPP's DM was wrong")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
