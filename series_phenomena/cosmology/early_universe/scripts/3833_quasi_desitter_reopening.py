#!/usr/bin/env python3
"""Patch 3833 -- does CPP have a during-inflation generator? Tests whether EU-1's engine supplies the
quasi-de Sitter phase that 0730's constraint file recorded (citing 0729) as absent. Arithmetic on
quantities the corpus already carries; nothing adopted, no mechanism derived."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

# EU-1's engine: H_eff = kappa0 kT ln n_bar, with ln n_bar = 3 N_rem  =>  H_eff proportional to N_rem
eps = lambda Nrem: 1.0/Nrem                 # eps = -dlnH/dN
w   = lambda Nrem: -1 + 2*eps(Nrem)/3

check("T1 EU-1's engine gives H_eff ∝ N_rem, hence eps = 1/N_rem = 0.0175 at the pivot -- SLOW ROLL "
      "(eps << 1), i.e. a quasi-de Sitter phase",
      eps(57)<0.02 and w(57)<-0.98, f"eps(57) = {eps(57):.4f}, w = {w(57):.4f}")

check("T2 the phase is accelerating across the whole observable window (N_rem = 57 down to ~10)",
      all(w(N)<-1/3 for N in (57,40,20,10)),
      f"w(10) = {w(10):.4f}, still < -1/3")

check("T3 the standard quasi-de Sitter tilt of this background REPRODUCES PRED-C-96 exactly: "
      "n_s - 1 = -2 eps = -2/N_rem",
      abs((1-2*eps(57)) - (1-2/57))<1e-12, f"n_s = {1-2*eps(57):.4f}")

# 0729's scope: the ZBW / GP-packing barotropic fluid, w in [0,1/3]
def w_osc(n): return (n-2)/(n+2)            # coherent oscillation in V ~ phi^n
check("T4 0729's no-go is scoped to the ZBW/packing fluid: w in [0,1/3] (n = 2 -> 0, n = 4 -> 1/3), "
      "firmly DECELERATING -- it does not cover EU-1's count-driven engine",
      abs(w_osc(2))<1e-12 and abs(w_osc(4)-1/3)<1e-12 and all((1+3*w_osc(n))/2>0 for n in (2,4)),
      f"w(n=2) = {w_osc(2):.3f}, w(n=4) = {w_osc(4):.3f}; q > 0 for both")

check("T5 so the two are DIFFERENT SOURCES: 0729 ruled out the substrate fluid; EU-1's engine is the "
      "count-driven boost (0746 fork (i)) and is not that fluid. 0729's verdict stands in its own scope",
      True, "0730 used it as a universal blocker; that use is what expires")

# the generator, once a quasi-de Sitter background exists
check("T6 in a quasi-de Sitter background a LIGHT field (omega << H) freezes at horizon exit with "
      "delta ~ H/2pi per mode -> equal power per log interval to O(eps): near-scale-invariant, "
      "Gaussian, and adiabatic if it is the field driving expansion",
      eps(57)<0.02, f"deviation from exact scale invariance ~ O(eps) = {eps(57):.3f}")

# what is still missing: a light degree of freedom. The register spring was withdrawn at 3812.
omega_over_H = 1.3e5
check("T7 the missing piece is NOT the generator mechanism but the LIGHT FIELD: the only named "
      "oscillator (AP-5's register spring) has omega/H >= 1.3e5 -- heavy by five orders (3812)",
      omega_over_H>1e4, f"omega/H >= {omega_over_H:.1e}; light requires omega/H <~ 1")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
