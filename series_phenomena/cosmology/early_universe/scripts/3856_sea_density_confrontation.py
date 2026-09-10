#!/usr/bin/env python3
"""Patch 3856 -- sanctioned DE/EM excursion: does an independent CPP determination of the sea density
pin N_CP? Read-only across lanes. Arithmetic on retrieved corpus values; nothing adopted."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

lP=1.616e-35; a_ratio=7.415e28; N_EU=1.4e17
DS=4.636                                   # DE-lane calibrated DP spacing, in l_P

check("T1 SF-6 CANNOT SERVE AS THE CHECK. OPEN-FP-6-CONSTANTS is titled 'First-principles electromagnetic "
      "constants WITHOUT parameter tuning' -- i.e. obtaining them untuned is the OPEN problem, so the "
      "shipped eps_0/mu_0 are parameter-tuned by the corpus's own statement and supply no independent density",
      True, "half of route 2's check is unavailable by the corpus's own admission")

n_lP3=1/DS**3; n_DP=n_lP3/lP**3; n_CP=2*n_DP
check("T2 THE DE LANE DOES HAVE A NUMBER: the calibrated Sea sits at d_s = 4.636 l_P (calibrated against "
      "the Lithium observable, c_Li = 0.8), giving n_DP = 1.00e-2 per l_P^3",
      abs(n_lP3-1.004e-2)/1.004e-2<0.01, f"n_DP = {n_lP3:.3e} /l_P^3 = {n_DP:.2e} /m3; n_CP ~ {n_CP:.2e} /m3")

ratio=n_CP/N_EU
check("T3 CONFRONTATION: the DE sea density exceeds the EU requirement by ~86 orders",
      85<math.log10(ratio)<87, f"n_CP(DE) / n_CP(EU) = {ratio:.1e} -> {math.log10(ratio):.0f} orders")

# independent cross-check in LENGTH
sp_EU=a_ratio                              # EU: spacing ~ l_P at inflation's end, then x a_ratio
check("T4 CROSS-CHECK IN LENGTH (independent of the density arithmetic): EU's dilution law puts today's "
      "spacing at ~l_P x a_ratio = 7.4e28 l_P; the DE lane's calibrated spacing is 4.64 l_P -- 28 orders "
      "in length, which cubes to the 85 orders of T3",
      abs(3*math.log10(sp_EU/DS)-85)<2,
      f"EU {sp_EU:.2e} l_P vs DE {DS} l_P; {math.log10(sp_EU/DS):.0f} orders in length, {3*math.log10(sp_EU/DS):.0f} cubed")

check("T5 READING (A) -- same population: an ~86-order CROSS-SECTOR CONTRADICTION, far larger than the "
      "e-fold budget question that prompted the check",
      True, "would be a programme-level inconsistency, not a lane matter")

check("T6 READING (B) -- different populations: the DE Sea is the non-diluting PAIRED VACUUM near the "
      "lattice scale (its spacing is 'HELD FIXED at the calibrated d_s' by construction, which is not "
      "how a diluting population behaves), while EU-1's n_bar is the DILUTING EXCESS OCCUPANCY riding on "
      "it. Then there is no contradiction -- and no pin either",
      True, "the textual evidence favours (B)")

check("T7 THE CORPUS DOES NOT SETTLE WHICH. EU-1 says expansion is 'dilution of DP-Sea occupancy', and "
      "'occupancy' is ambiguous between the sea itself and the excess above it. The ambiguity is "
      "load-bearing for EU-1's own dilution law, not only for this check",
      True, "definitional, and it sits inside EU-1")

check("T8 VERDICT: route 2's check is INCONCLUSIVE, and the blocker is definitional rather than "
      "numerical. No independent pin exists until the referent of 'the sea' is fixed",
      True, "register the referent question; escalate reading (A) to the maintainer")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
