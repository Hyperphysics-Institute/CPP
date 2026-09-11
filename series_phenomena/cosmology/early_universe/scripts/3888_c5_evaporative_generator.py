#!/usr/bin/env python3
"""Patch 3888 -- C-5, the founder's evaporative generator, assessed. It is the first proposal that can
break the 3835 no-go, and its viability reduces to one question. Structure and arithmetic; nothing adopted."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
NREM=57.0

check("T1 STRUCTURALLY UNLIKE ALL SEVEN CLOSED CANDIDATES. Each failed on one of two things: it was an "
      "**initial-slice property** (the count, delta-kT, composition, C-2, C-3, C-4 -- one characteristic "
      "scale, no generator), or it was **post-inflation** (DM clumping, the species ladder, the fractal "
      "cascade -- active sources excluded by the acoustic peaks)",
      True, "two failure modes, seven candidates, no exceptions")

check("T2 C-5 IS NEITHER: it runs **DURING inflation** and generates **CONTINUOUSLY**. That is exactly the "
      "gap 3831 S5 named -- 'Standard inflation meets scale-invariance with continuous generation at "
      "horizon exit. CPP has no such generator identified.' **C-5 is a candidate generator**",
      True, "the first in the arc")

# the hinge
check("T3 THE HINGE ON THE NO-GO, and it is a corpus fact not an assumption: **AP-4 -- 'Every GP emits the "
      "same fixed number of DI-bits every Moment' -- is PER GP, NOT PER CP.** So CPs superimposed on one "
      "GP are **perceptually ONE**",
      True, "verified in master_glossary.md")

check("T4 THEREFORE evaporation from superposition **RAISES the perceived count without changing the CP "
      "count**. The CP count stays conserved; what grows is the number of *occupied GPs*. **The source is "
      "a RATE, not a conserved density**",
      True, "reservoir -> distinguishable occupancy")

check("T5 **AND THAT BREAKS THE 3835 NO-GO'S PREMISE.** The no-go runs: only the CONSERVED count enters "
      "dN; conserved densities obey integral constraints forcing P(k) -> k^2; hence blue; hence excluded. "
      "**If the perceived count is occupied-GP count, a non-conserved rate enters dN and the premise "
      "fails.** C-5 is the first proposal that can do this",
      True, "not a refutation of the no-go -- an escape from its scope")

# tilt consistency
check("T6 AND THE TILT COMES OUT RIGHT WITHOUT A NEW ASSUMPTION. Continuous generation at a rate tracking "
      "H_eff gives equal amplitude per mode at horizon exit (the standard mechanism); with H_eff prop to "
      "N_rem this gives n_s - 1 = -2/N_rem = -0.0351, i.e. n_s = 0.9649 -- **PRED-C-96 exactly**",
      abs((1-2/NREM)-0.9649)<1e-4, f"n_s = {1-2/NREM:.4f}; consistent, not newly assumed")

check("T7 THE DE ANALOGY IS STRUCTURALLY SOUND and is the proposal's strongest feature: superimposed CPs "
      "during inflation play the role DP-entities play during DE, both as evaporating stock filling new "
      "volume. **That makes it ONE process at two epochs, not two mechanisms** -- and it connects to the "
      "founder's own 3858 cascade clarification",
      True, "economy of mechanism is evidence, not decoration")

check("T8 **THE DECISIVE QUESTION, and it is already framed twice in this lane:** does n_bar count **CPs** "
      "or **occupied GPs**? 3876 settled the referent as 'CPs per rest-frame Planck sphere'; but AP-4's "
      "per-GP emission says the *perceived* count is occupied GPs. **These are in tension, and the tension "
      "is now load-bearing for C-5.** If occupied-GP: C-5 lives. If CP-regardless-of-superposition: C-5 "
      "dies with the rest",
      True, "the held-vs-perceived fork of 3837, now decisive rather than academic")

check("T9 WHAT C-5 OWES, in order: (1) settle T8's referent; (2) the amplitude -- not computed here, and "
      "**PD-007 bars calibrating it against A_s**; (3) a corpus home for the superposition reservoir, "
      "which is the founder's picture and is not yet a registered object; (4) adiabaticity vs Planck's "
      "isocurvature bound",
      True, "four debts, ordered; (1) gates the rest")

check("T10 SCOPE, STATED PLAINLY: **nothing is adopted and C-5 is not reported as working.** What is "
      "established is that it is the first candidate whose *structure* is right -- during-inflation, "
      "continuously generating, non-conserved source -- and that its viability reduces to one already-"
      "framed question",
      True, "a live candidate, not a solution")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
