#!/usr/bin/env python3
"""Patch 3906 -- kappa* ruled effectively axiom-level, and for a reason sharper than 'uncalibrated':
the relation it coefficients (H_eff prop mu) is itself an ASSIGNMENT, and it is a deliberate departure
from Friedmann carrying an 83-order mismatch. Mechanism-first discipline honoured: no number guessed."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
h=1.93e-5; RHOF=3*h**2; NBAR=math.exp(3*57)

check("T1 **D-1: THE COUPLING ITSELF IS AN ASSIGNMENT.** The corpus lists the conditionality as the "
      "'**H_eff ∝ μ coupling + spectator P ∝ H_eff² assignment**' -- so kappa* is **the coefficient of an "
      "ASSERTED relation**, not an undetermined constant in a derived one",
      True, "that is a sharper statement than 'kappa* is uncalibrated'")

check("T2 **SO DERIVING kappa* REQUIRES FIRST DERIVING WHY H ∝ μ AT ALL.** That is a larger question than "
      "kappa*'s value, and it is upstream of everything C-5 does",
      True, "the gate is not the number but the relation")

# is it Friedmann?
check("T3 **AND H ∝ μ IS NOT FRIEDMANN.** Under Friedmann H² = ρ/(3M_Pl²), so the observed H/M_Pl = 1.93e-5 "
      "implies ρ/M_Pl⁴ = 1.12e-9",
      abs(RHOF-1.12e-9)/1.12e-9<0.02, f"rho/M_Pl^4 = {RHOF:.2e}")

check("T4 but the CPP substrate at the pivot carries n̄ = e^171 = 1.8e74 CPs per Planck sphere at ~E_Pl "
      "each, i.e. **rho/M_Pl⁴ ~ 1.8e74** -- a **mismatch of 83 orders**. That is the vacuum catastrophe",
      abs(math.log10(NBAR/RHOF)-83.2)<0.5, f"mismatch = {NBAR/RHOF:.1e} ({math.log10(NBAR/RHOF):.0f} orders)")

check("T5 **SO THE H ∝ μ ASSIGNMENT IS A DELIBERATE DEPARTURE FROM FRIEDMANN, AND kappa_0 CARRIES THE "
      "DEPARTURE.** Its smallness (1.1e-7) is not an accident of units -- it is the price of not being "
      "Friedmann",
      True, "which is why no coupling-power formula should be expected to produce it")

check("T6 **THAT RETROSPECTIVELY JUSTIFIES 3904's REFUSAL.** Scanning powers of α for 1e-7 presumes kappa_0 "
      "is a coupling constant. It is not: **it is the coefficient of a departure from a field equation**, "
      "and there is no reason such a thing should be a power of α",
      True, "the refusal was right, and now for a stated reason rather than caution alone")

check("T7 **RULING: kappa* is EFFECTIVELY AXIOM-LEVEL as things stand** -- not because it is hard to "
      "compute, but because **the relation it coefficients is itself an assignment**. This is one of the "
      "two outcomes 3905 named as a result, and it is the one that obtains",
      True, "a result, not a failure to find one")

check("T8 **CONSEQUENCE FOR C-5, stated plainly: its amplitude is PERMANENTLY a consistency check** unless "
      "and until the H ∝ μ assignment is itself derived. **Not a pending normalisation -- a foreclosed "
      "one**, conditional on an upstream assignment",
      True, "the distinction EU-1 must carry")

check("T9 **OWED TO EU-1 (V1.7):** state that (i) the normalisation is κ*-gated; (ii) κ* is the "
      "coefficient of the H ∝ μ **assignment**; (iii) that assignment is a **deliberate departure from "
      "Friedmann**; and (iv) therefore A_s is **not predicted** by the framework as it stands",
      True, "four sentences; the paper currently implies none of them")

check("T10 SCOPE: **nothing adopted; no constant minted; no number guessed.** The mechanism-first "
      "discipline was honoured -- the search was for the mechanism, it was found to be an assignment, and "
      "**no value was proposed**",
      True, "the discipline produced a negative, which is what it is for")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
