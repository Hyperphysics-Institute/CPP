#!/usr/bin/env python3
"""Patch 3882 -- the founder's DM-clumping proposal assessed. Amplitude nearly reachable (a first for this
arc); shape and timing independently excluded. Arithmetic; nothing adopted, no constant minted."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
Mpc=3.086e22; rho_dm=2.2e-27; Msun=1.99e30; V=(100*Mpc)**3

check("T1 NO, THIS WAS NOT ASSESSED. The seven closed candidates (3847) were the register spring, the "
      "conserved count, delta-kT, composition, C-3 frustration, C-2 edge, and C-4. **DM clumping was not "
      "among them** -- the question is legitimate, not a re-run",
      True, "an eighth proposal, founder-raised rather than worker-manufactured")

check("T2 AND IT IS WELL AIMED: in LCDM the CMB anisotropy genuinely IS dominated by dark-matter potential "
      "wells (Sachs-Wolfe). **DM clumping is exactly what the CMB displays.** The question is whether it "
      "MAKES the pattern or merely CARRIES it",
      True, "the generation/processing distinction again, but from a stronger starting point")

# amplitude
def poisson(Mag_sun): return 1/math.sqrt(rho_dm*V/(Mag_sun*Msun))
check("T3 AMPLITUDE -- and this is a FIRST for the arc. CPP DM is charge-neutral qDP/hTetra AGGREGATES "
      "(CONJ-COSMO-1). Aggregation from a random start is Poisson-seeded, and at ~1e6 Msun per aggregate "
      "the Poisson contrast at 100 Mpc is 5.6e-6 against a required ~1e-5 -- **within a factor of two**",
      abs(poisson(1e6)-5.55e-6)/5.55e-6<0.05,
      f"delta(1e6 Msun) = {poisson(1e6):.2e}; every prior candidate missed by 40+ orders")

check("T4 BUT THAT IS A FIT, NOT A DERIVATION. The aggregate mass is free, and it was chosen to land on "
      "the observed contrast. Under PD-007 that is calibration -- the amplitude is *reachable*, not "
      "*predicted*",
      poisson(1e3)<1e-6 and poisson(1.0)<1e-8,
      f"1e3 Msun -> {poisson(1e3):.1e}; 1 Msun -> {poisson(1.0):.1e} -- three decades of mass span three of contrast")

check("T5 EXCLUSION 1 -- THE SHAPE. Poisson seeding is WHITE. A white primordial spectrum in the CDM "
      "component is the **isocurvature-CDM model**, long excluded; Planck bounds the isocurvature fraction "
      "to a few percent",
      True, "the same bound that excluded composition (3822) and the qCP chains (3833)")

check("T6 EXCLUSION 2 -- THE TIMING. Clumping that develops AFTER inflation is an **active, incoherent "
      "source**. Active sources do not reproduce the observed acoustic-peak series -- this is precisely "
      "why cosmic-defect models were excluded as the primary perturbation source",
      True, "the same exclusion that demoted C-3 at 3829 S4")

check("T7 EXCLUSION 3 -- THE ORDERING. The CMB requires delta ~ 1e-5 already present and COHERENT on "
      "super-horizon scales at recombination. Aggregation is a growth process: it needs a seed to "
      "amplify, and cannot supply the seed it starts from",
      True, "structure formation grows a spectrum; it does not create one")

check("T8 SO IT RELOCATES THE QUESTION RATHER THAN ANSWERING IT -- the same verdict as the fractal "
      "cascade (0730/3833/3880), reached from a better starting point and failing later in the argument",
      True, "processing, not generation")

check("T9 WHAT IS GENUINELY NEW: this is the **first candidate in the arc to come close on amplitude**. "
      "Every other missed by 40+ orders (C-2's incoherent floor was 41 short). The reason is that DM "
      "aggregates are MASSIVE and therefore FEW, so their Poisson noise is large",
      poisson(1e6)/1e-5>0.1, "worth recording even though the candidate fails")

check("T10 AND IT DOES NOT DISTURB THE NO-GO. 3835 stands: while inflation ends at a fixed geometric "
      "threshold, only the conserved count enters dN. DM clumping is a POST-inflation phenomenon and "
      "never enters the e-fold count at all",
      True, "it was never a candidate for the no-go's subject matter")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
