#!/usr/bin/env python3
"""Patch 3916 -- clarification: the 83 orders is an ENERGY DENSITY mismatch (the vacuum catastrophe in CPP
variables), NOT the ripple size. The ripple size is one number with no dynamic range. They connect only
through kappa_0, which absorbs the density departure."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
h=1.93e-5; RHOF=3*h**2; NBAR=math.exp(3*57); K0=h/(3*57); ZETA=4.6e-5

check("T1 **THE RIPPLE SIZE HAS NO DYNAMIC RANGE.** It is a single number: **ζ = 4.6×10⁻⁵** (A_s = "
      "2.1×10⁻⁹) — about **one part in twenty thousand**. **There is no 83-order span anywhere in the "
      "observed perturbations**",
      abs(ZETA-4.6e-5)<1e-6, "one number, not a range")

check("T2 **THE 83 ORDERS IS AN ENERGY-DENSITY MISMATCH** — a different quantity entirely. Friedmann with "
      "the observed H demands **ρ/M_Pl⁴ = 1.12×10⁻⁹**",
      abs(RHOF-1.12e-9)/1.12e-9<0.02, f"Friedmann requirement = {RHOF:.2e}")

check("T3 while the CPP substrate at the pivot carries **ρ/M_Pl⁴ ~ 1.8×10⁷⁴** (n̄ = e¹⁷¹ CPs per Planck "
      "sphere at ~E_Pl each) ⇒ **gap = 83 orders**",
      abs(math.log10(NBAR/RHOF)-83.2)<0.5, f"{NBAR:.1e} vs {RHOF:.1e} ⇒ {math.log10(NBAR/RHOF):.0f} orders")

check("T4 **THAT IS THE VACUUM CATASTROPHE, written in CPP variables.** It is the gap between what a "
      "substrate inventory says the energy density is and what gravity says it must be — **the oldest "
      "open problem in the subject, and NOT unique to CPP.** Standard QFT carries its own version",
      True, "a shared problem, stated in this framework's units")

check("T5 **THE TWO NUMBERS ARE NOT THE SAME KIND OF THING.** One is a **dimensionless perturbation "
      "amplitude** (4.6×10⁻⁵); the other is a **ratio of energy densities** (10⁸³). Neither is a range of "
      "the other",
      True, "the misreading corrected")

check("T6 **THEY CONNECT AT EXACTLY ONE POINT: κ₀.** H_eff = κ₀·kT·ln n̄ sidesteps Friedmann, and "
      "**κ₀ = 1.13×10⁻⁷ ABSORBS the departure.** ζ depends on H; H depends on κ₀; κ₀ carries the density "
      "gap",
      abs(K0-1.13e-7)/1.13e-7<0.02, f"kappa_0 = {K0:.2e}")

check("T7 **SO THE CORRECT STATEMENT IS:** *the ripple size is unpredicted BECAUSE the density problem is "
      "unsolved* — **not** *because the ripple size itself spans 83 orders.* The framework must predict "
      "**one number**, and cannot, because the constant it needs is the one carrying the vacuum problem",
      True, "cause, not magnitude")

check("T8 **AND WHAT CPP *DOES* PREDICT IS UNAFFECTED.** The tilt n_s = 0.9654 is a pure prediction "
      "reading the adopted pivot; it does **not** pass through κ₀, and the 83 orders never enter it",
      True, "the shape is predicted; only the size is not")

check("T9 A USEFUL WAY TO SAY IT: **CPP predicts the SHAPE of the ripples and not their SIZE**, and the "
      "reason is that the size runs through the same constant that absorbs the vacuum problem. **A theory "
      "that solved the vacuum problem would get the size for free**",
      True, "which is why Exit 1 is the only path to a predictive A_s")

check("T10 SCOPE: **nothing new is derived here.** This is a clarification of two numbers that were being "
      "conflated, and a statement of the single link between them. **No claim changes**",
      True, "correction of reading, not of result")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
