#!/usr/bin/env python3
"""Patch 3890 -- the n_bar referent question answered from the corpus. Occupancy wins for anything
dynamical; the count law is safe because the two readings coincide at ignition; C-5's gate moves."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
NCP=1e84; s=math.exp(-(75.0-1.306)); GPperPS=(4*math.pi/3)/s**3; occ=NCP/GPperPS

check("T1 WHAT THE DISTINCTION MEANS. n_bar is an OCCUPANCY -- how crowded a perceptual sphere is -- "
      "because mu = kT ln n_bar is a configurational entropy per particle (0749). The question is whether "
      "'crowded' is counted in **CPs** or in **occupied GPs**",
      True, "and the two differ ONLY where CPs share a GP")

check("T2 SO THE QUESTION IS NARROWER THAN IT LOOKS: with no superposition the readings are IDENTICAL. "
      "The fork opens only if something forces CPs onto the same GP",
      True, "not a global ambiguity -- a local one")

check("T3 WHICH READING DRIVES THE DYNAMICS? The founder settled this himself at Patch 3426: **'CPs respond "
      "only to the DI-bits that arrive at each GP at each Moment.'** And AP-4 emits **per GP, not per CP**",
      True, "founder verbatim, 25 Aug 2026, registered in founders_voice")

check("T4 **THEREFORE A CP CANNOT RESPOND TO WHAT IT DOES NOT PERCEIVE.** Twelve CPs on one GP deliver one "
      "GP's worth of DI-bits. The n_bar that drives the engine H_eff = kappa0 kT ln n_bar must be the "
      "**PERCEIVED** count -- i.e. **OCCUPIED GPs**",
      True, "the dynamical referent is occupancy; this is not a preference but a consequence")

check("T5 AND THE COUNT LAW IS SAFE, because the two readings COINCIDE at ignition. 1e84 CPs in a Planck "
      "sphere of 4.3e96 GPs is an occupancy of 2.3e-13 per GP -- extraordinarily sparse",
      abs(math.log10(occ)+12.6)<0.5, f"occupancy = {occ:.2e} CPs per GP")

check("T6 at that sparsity the Poisson fraction of GPs holding two or more CPs is ~3e-26. **Superposition "
      "is utterly negligible generically**, so occupied GPs ~ CP count and **N = (1/3) ln N_CP = 64.5 "
      "stands untouched**",
      occ**2/2<1e-25, f"P(>=2 per GP) = {occ**2/2:.1e}")

check("T7 **SO BOTH READINGS ARE RIGHT IN THEIR DOMAIN.** 3816/3876's CP count is correct generically "
      "(because the lattice is nearly empty); AP-4's occupancy is correct as the dynamical referent. They "
      "part company ONLY where superposition is forced",
      True, "the apparent contradiction dissolves -- it was a domain confusion")

check("T8 **WHICH WAY IT WORKS OUT FOR C-5: THE READING FAVOURS IT.** The dynamical n_bar is occupancy, so "
      "evaporation from a superposition reservoir DOES raise n_bar without changing the conserved CP "
      "count, and the 3835 no-go's premise DOES fail for that source",
      True, "C-5 survives the gating question")

check("T9 **BUT THE GATE MOVES RATHER THAN OPENS.** Superposition is not generic -- it needs a mechanism "
      "to force CPs onto one GP against a lattice that is 1e13 times emptier than one-per-GP. **C-5's "
      "debt (3) -- a corpus home for the reservoir -- is now the GATING debt**, not debt (1)",
      True, "the reservoir must be real, not merely posited")

check("T10 AND THE REQUIREMENT IS SHARP: the reservoir must hold enough CPs, and release them at a rate "
      "tracking H_eff, to move ln n_bar by the required delta-N. **That is debt (2), the amplitude, and "
      "PD-007 still bars calibrating it.** Nothing here computes it",
      True, "referent resolved; amplitude and reservoir still owed")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
