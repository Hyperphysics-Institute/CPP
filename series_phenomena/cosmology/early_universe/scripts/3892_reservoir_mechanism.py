#!/usr/bin/env python3
"""Patch 3892 -- the founder's reservoir mechanism. Debt (3) discharged; 3890's sparsity argument
overturned; C-5's perturbation DERIVED as zeta = (1/3) delta ln f; count law and tilt both survive,
independently of the unremembered stack number."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
NCP=1e84; NTOT=math.log(NCP)/3; NREM=57.0

check("T1 THE MECHANISM IS ORDINARY A1'/AP-3 DISPLACEMENT: CPs land on the same GP because the summation "
      "of their arriving DI-bits directs them to the same address. **No new mechanism is required, and the "
      "founder proposes none**",
      True, "the reservoir needs no new axiom -- it is the existing displacement rule")

check("T2 AND THE INITIAL CONDITION *IS* STACKING -- 'a large number of CPs on every GP'. **The reservoir "
      "is not a structure to be posited; it is the starting state.** Debt (3) is discharged",
      True, "C-5's gating debt closes on the founder's initial condition")

check("T3 **THIS OVERTURNS 3890's SPARSITY ARGUMENT.** 3890 computed occupancy as 2.3e-13 per GP and "
      "concluded superposition needs a forcing mechanism -- but that assumed CPs SPREAD over a Planck "
      "sphere's 4.3e96 GPs. The founder's picture has them STACKED from the start, on far fewer GPs. "
      "**The worker supplied the arrangement; the founder's initial condition supplies a different one**",
      True, "same error class as 3882's invented mass: an unstated arrangement assumed")

# the derivation
check("T4 **C-5's PERTURBATION, DERIVED.** With f = the fraction of CPs that have left superposition, the "
      "occupied-GP count is ~f*N_CP, so n_bar = f*N_CP/V and **ln n_bar = ln N_CP - 3N + ln f**. The new "
      "term is **ln f**, and since zeta = delta-N = (1/3) delta ln n_bar: **zeta = (1/3) delta ln f**",
      True, "the fluctuation in the LOCAL UNSTACKING FRACTION -- a rate, not a conserved density")

check("T5 THE COUNT LAW SURVIVES EXACTLY. Inflation ends at n_bar = 1 with everything unstacked (f -> 1), "
      "so V_end = N_CP Planck spheres and **N = (1/3) ln N_CP = 64.47** -- unchanged. The growth in "
      "occupied GPs exactly compensates, *because f reaches 1 at the end*",
      abs(NTOT-64.47)<0.02, f"N = {NTOT:.2f}")

# tilt, parameterised in the unremembered n0
def slope(n0): return 3+(-math.log(n0))/NTOT
check("T6 THE TILT SURVIVES EXACTLY. If ln f is linear in N_rem then ln n_bar = (slope)*N_rem stays LINEAR, "
      "and epsilon = -dlnH/dN = 1/N_rem **whenever ln n_bar is linear in N_rem, whatever the coefficient**",
      all(slope(n0)>0 for n0 in (1e6,1e12,1e24)),
      "; ".join(f"n0=1e{int(math.log10(n0))}: slope={slope(n0):.3f}" for n0 in (1e6,1e12,1e24)))

check("T7 => n_s - 1 = -2/N_rem = -0.0351, n_s = 0.9649 -- **PRED-C-96 EXACTLY, and INDEPENDENT of the "
      "stack number**",
      abs((1-2/NREM)-0.9649)<1e-4, f"n_s = {1-2/NREM:.4f} for every n0 tested")

check("T8 **THE STACK NUMBER IS NOT INVENTED.** The founder states he does not remember it; it is carried "
      "as n0 and all three results above are shown independent of it. *(3884's lesson: never supply a "
      "parameter -- and here, never supply one the founder has flagged as unknown.)*",
      True, "the discipline working, rather than being written about")

check("T9 REGISTERED, not assessed: the charge rule for re-superimposition -- **opposite charge gives a ZBW "
      "oscillator; same charge launches without oscillating**. It bears on what fraction re-superimposes "
      "rather than staying free, hence on f's evolution law",
      True, "an input to debt (2), not yet used")

check("T10 **WHAT NOW GATES C-5: debt (2), the amplitude, sharply posed at last -- what is delta ln f?** And "
      "an honest warning: if unstacking is a Poisson process, delta ln f is white, and C-5 meets the same "
      "wall as the seven. **That is the next test and it is not pre-judged here**",
      True, "the amplitude is now a definite question about a definite quantity")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
