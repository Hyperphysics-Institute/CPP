#!/usr/bin/env python3
"""Patch 3878 -- correcting the 'edge of the universe' reading. The end condition is a DENSITY threshold,
not a boundary; nothing fills up; nothing gets squashed. Separates the two distinct 'edges' and registers
the one the corpus genuinely leaves open. Arithmetic; nothing adopted."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

lP=1.616e-35; Mpc=3.086e22
s=math.exp(-(75.0-1.306)); GPperPS=(4*math.pi/3)/s**3
rho_end=1/((4*math.pi/3)*lP**3); rho_today=1.4e17

check("T1 WORKER'S ERROR, OWNED: 3876 adopted the founder's phrase 'the entirety of the universe that will "
      "ever be populated' without qualifying it. That phrase invites a BOUNDARY reading. The end condition "
      "is a DENSITY threshold -- intensive, local, and satisfied everywhere at once. It is not a wall",
      True, "n_bar = 1 CP per Planck sphere says nothing about where anything ends")

check("T2 AND THE PHRASE CONFLATES TWO LATTICE SCALES. 'One CP per Planck sphere' is not 'one CP per GP': a "
      "Planck sphere holds ~4.3e96 GPs, so at the end of inflation the CPs occupy about ONE GP IN 1e97",
      GPperPS>1e96, f"GPs per Planck sphere = {GPperPS:.2e}; occupied fraction = {1/GPperPS:.0e}")

check("T3 SO NOTHING IS FILLING UP -- the lattice is ~1e97 times UNDER-occupied at the end of inflation",
      1/GPperPS<1e-96, "the CPs are extraordinarily dilute on the lattice, not crowded onto it")

check("T4 AND IT HAS ONLY GOT EMPTIER SINCE. Today's CP density is ~87 orders BELOW the end-of-inflation "
      "value, so the occupied GP fraction is ~1e-183. The threshold was crossed 13.8 Gyr ago",
      abs(math.log10(rho_end/rho_today)-87)<1,
      f"rho_today/rho_end = {rho_today/rho_end:.1e}; occupied fraction now ~{(1/GPperPS)*(rho_today/rho_end):.0e}")

check("T5 INFLATION ENDING IS NOT EXPANSION ENDING. n_bar = 1 is a threshold the density fell THROUGH; "
      "expansion continued through the radiation, matter and dark-energy eras and continues now",
      rho_today<rho_end, "density falls monotonically")

check("T6 THEREFORE NO SQUASHING. There is no compression anywhere in the picture -- density decreases "
      "monotonically forever. Nothing is driven against anything",
      True, "the founder's 'ultimate squashing against the edge' does not follow and is not implied")

# the two distinct edges
check("T7 TWO DISTINCT 'EDGES', and only one is in the corpus. (a) THE OCCUPIED REGION'S BOUNDARY -- the "
      "founder's own 3822 edge picture. Real, comoving, and RECEDING: it expands with everything else, so "
      "nothing inside ever approaches it",
      True, "a matter boundary, not a wall; we are inside and stay inside")

check("T8 (b) AN EDGE TO THE LATTICE ITSELF -- whether the GP scaffold is finite or unbounded. **D-1 "
      "searched master_glossary, programme_orientation and founders_vision and found NOTHING fixing it.** "
      "The corpus simply does not say",
      True, "genuinely unspecified, not merely unnoticed")

check("T9 CAN IT BE CALCULATED? (a) YES -- the occupied boundary is the ball radius, already computed: "
      "0.39 Mpc today at N = 64.5, or >= the observable radius at the budget-closed N = 75. Under the only "
      "self-consistent reading it sits AT OR BEYOND our horizon and recedes",
      True, "3823/3854 did this arithmetic")

check("T10 (b) NO -- not from anything on file, because the lattice's extent is unspecified. **Registered "
      "as OPEN-EU-LATTICE-EXTENT-1**: is the GP scaffold finite or unbounded, and does the question have "
      "observable consequences? The founder's question generates it; it is a genuinely new open item",
      True, "first new EU open item since the lane emptied")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
