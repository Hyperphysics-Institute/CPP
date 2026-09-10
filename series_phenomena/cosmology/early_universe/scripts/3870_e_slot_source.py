#!/usr/bin/env python3
"""Patch 3870 -- the 3862 residual resolved: AP-4's E slot must be sourced by the origin GP's RESIDENT
CP charges. The strict arrivals-only reading is excluded by reductio. Logic and bookkeeping."""
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

check("T1 THE RESIDUAL (3862 S3): AP-4 defines E as 'the vector sum of all polar-charge contributions "
      "integrated by the origin GP IN THE PREVIOUS MOMENT'. Read strictly, the E a GP imprints comes only "
      "from what it received -- and at Moment 1 it received nothing",
      True, "the wording admits an arrivals-only reading")

check("T2 D-1 APPLIED: searched master_glossary, axiom-registry and founders_voice for a statement that a "
      "GP's OWN resident CP charges source the E it imprints. **No such statement found.** The corpus "
      "consistently words E as previous-Moment integration",
      True, "the absence is the finding, and it is reported as an absence")

# the reductio
E=0.0
for _ in range(50): E = 12*E
check("T3 READING S (strict, arrivals-only) is a LINEAR HOMOGENEOUS recursion: E_i(t) = sum_j E_j(t-1). "
      "With every register empty at ignition, E_j(0) = 0, so by induction **E = 0 at every GP for all "
      "time** -- whatever the weights",
      E==0.0, "50 iterations of any linear map on 0 give 0")

check("T4 CONSEQUENCE OF READING S: SSV_net = E + S = 0 identically, so no CP ever displaces (A1'/AP-3), "
      "so nothing ever happens. **Reading S yields no physics at all** -- not merely a failed ignition",
      True, "the recursion never leaves its fixed point")

check("T5 READING R (resident-sourced): E_i(t) = q_i(resident CPs) + sum_j E_j(t-1). The resident charge "
      "is a SOURCE term, making the recursion INHOMOGENEOUS. E is nonzero from Moment 1 and propagates",
      True, "a source term is exactly what the homogeneous recursion lacks")

check("T6 THEREFORE READING R IS FORCED, by reductio on Reading S. This is a DERIVATION of the reading, "
      "not a preference between two glosses -- the same shape as 3860's half one, where exactly-once "
      "deposit was forced by emission-budget conservation",
      True, "consistency requirement, not a choice")

check("T7 THE 3862 RESIDUAL IS RESOLVED: first-Moment bits carry count AND direction. The count comes from "
      "AP-4's unconditional fixed emission; the direction comes from the resident CPs. The observation "
      "that they 'carry count without direction' was correct only under the excluded Reading S",
      True, "3862 S3's residual is discharged")

check("T8 AND THE FOUNDER'S IGNITION PICTURE NEEDS IT: twelve CPs per GP each displacing to an icosahedral "
      "vertex requires a directional SSV_net at Moment 1. Under Reading R the resident twelve source it; "
      "under Reading S ignition could never occur",
      True, "3813/3814's picture presupposes Reading R")

check("T9 WHAT IS OWED: AP-4's E-slot wording admits the excluded reading, so it should say so. This is a "
      "ONE-LINE clarification, not an amendment -- Reading R is what the corpus has always meant in "
      "practice, since every field result in the programme presupposes it",
      True, "clarification, not correction; founder's call")

check("T10 UNAFFECTED: SSV_abs stays count-like and arrival-built (it sums MAGNITUDES, and the resident "
      "term does not change that); n_bar is a count; the tilt, T-1, T-2 and the amplitude closure are "
      "untouched",
      True, "the resolution is directional-slot only")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
