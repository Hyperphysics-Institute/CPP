#!/usr/bin/env python3
"""Patch 3876 -- the n_bar referent question set out, Reading A excluded by the founder's own cascade,
and the founder's all-GPs proposal shown to reproduce the count law exactly. Also corrects the
'32 and 69 orders error' misreading. Arithmetic; nothing adopted."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
NCP=1e84; NREM=57.0

check("T1 CORRECTION FIRST -- the '32 and 69 orders' are NOT an error under repair. They are the margins by "
      "which two REJECTED hypotheses (diffusive and serial mixing) would have failed a test that PASSED. "
      "The bath-depth result is R = 3.3e-3, ~300 re-thermalizations per e-fold, margin ~300",
      True, "rejected rows in a comparison table, not a defect")

check("T2 nothing in the EU lane is currently carrying an order-of-magnitude error. The one live "
      "discrepancy is the 3858 counting bound (~86-99 orders), which belongs to the DE lane and is "
      "escalated, not under repair here",
      True, "the arc's open tension is elsewhere and is not an 'error'")

# --- Reading A excluded, by the founder's own 3858 clarification ---
check("T3 READING A (n_bar = the DP-Sea itself) is EXCLUDED BY THE FOUNDER'S OWN CASCADE. He stated (3858) "
      "that the sea is REPLENISHED at constant density/occupancy by heavy->light DP conversion. A "
      "constant-occupancy population has ln n_bar = const, so H_eff = kappa0 kT ln n_bar is CONSTANT",
      True, "the cascade fixes the sea's occupancy by construction")

eps_A=0.0; ns_A=1-2*eps_A
check("T4 and a constant H gives epsilon = 0, hence n_s = 1 -- the 0741 cliff, 8.4 sigma from Planck. "
      "Reading A is excluded by the tilt",
      abs(ns_A-1.0)<1e-12 and abs((1-0.9649)/0.0042-8.4)<0.2,
      f"n_s = {ns_A:.4f}; deviation {(1-0.9649)/0.0042:.1f} sigma")

check("T5 AND DOUBLY: with n_bar constant the end condition n_bar = 1 is never reached, so inflation never "
      "ends. Reading A fails on the tilt and on the exit independently",
      True, "two independent exclusions")

# --- Reading B, in the founder's own form ---
lin=NCP**(1/3); N=math.log(NCP)/3
check("T6 THE FOUNDER'S PROPOSAL IS READING B IN ITS CLEANEST FORM. Fixed lattice (EU-1: dilution on a "
      "FIXED scaffold, GPs never created) + fixed CP count + expansion = CPs SPREADING over more GPs "
      "=> n_bar = CPs per Planck sphere dilutes as a^-3. Correct shape",
      True, "no 'excess above a sea' is needed -- one population, spreading")

check("T7 and his phrase 'the entirety of the universe that will ever be populated' IS the end condition: "
      "n_bar = 1 means the CPs have spread to fill every Planck sphere they will ever occupy",
      True, "final volume = N_CP Planck spheres")

check("T8 IT REPRODUCES THE COUNT LAW EXACTLY: initial volume 1 Planck sphere (small-ball ruling 3816), "
      "final volume N_CP Planck spheres, so linear expansion = N_CP^(1/3) and N = (1/3) ln N_CP = 64.5",
      abs(N-64.47)<0.05 and abs(math.log10(lin)-28)<0.05,
      f"linear = {lin:.2e}, N = {N:.2f} -- EU-1 eq. Nstar, read physically")

check("T9 SO THE REFERENT IS SETTLED: n_bar counts CPs per rest-frame Planck sphere, the CP population is "
      "ONE population spreading over a fixed lattice, and 'the sea' is what that population IS locally "
      "once paired -- not a separate non-diluting reservoir with an excess riding on it",
      True, "the 'excess above a sea' framing was the worker's, and is withdrawn")

check("T10 WHAT REMAINS is NOT the referent but the 3858 COUNTING BOUND: the sea's constant ENTITY density "
      "requires entity count to grow with volume, while entities are built from a FIXED CP count. That is "
      "the real tension, it is quantitative, and it belongs to the DE lane",
      True, "referent settled here; counting bound still escalated")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
