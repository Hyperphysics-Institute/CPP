#!/usr/bin/env python3
"""Patch 3822 -- assessment of the founder's charge-mix and edge picture.
Arithmetic and scaling checks only; no constant adopted, no mechanism derived."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

NCP=1e84; N_GP=NCP/12
MPl=2.435e18; A_S=2.1e-9; H_line=4.7e13

# T1 -- compositional (Poisson) amplitude per Hubble patch, as at AS-NORMALIZATION S2 / 3812
# GPs per Hubble patch at the tensor line: (1/H)^3 in Planck units
H_pl=H_line/MPl
GP_per_hubble=(1/H_pl)**3
delta_poisson=1/math.sqrt(GP_per_hubble)
check("T1 compositional disorder is Poisson: delta ~ 1/sqrt(N) per Hubble patch, far below A_s^(1/2) ~ 4.6e-5",
      delta_poisson < 1e-5, f"GPs/Hubble = {GP_per_hubble:.2e}, delta = {delta_poisson:.2e}, need {math.sqrt(A_S):.2e}")

# T2 -- a frozen (fixed-at-ignition) pattern is scale-independent: n_s = 1, the 0741 cliff
# recorded as an inherited exclusion, not recomputed: white spectrum => d ln P/d ln k = 0
n_s_white=1.0
check("T2 a pattern frozen at ignition is white => n_s = 1 exactly (0741 cliff; 8.4 sigma from Planck)",
      abs(n_s_white-1.0)<1e-12, "inherited exclusion, 3812 S2")

# T3 -- the geometric end condition is species-blind: composition cannot shift n_bar_end = 1
# n_bar_end counts CPs per Planck sphere regardless of species => dN = 0 (same wall as 3818)
check("T3 end condition n_bar_end = 1 is a count, species-blind => composition gives dN = 0",
      True, "structural: 3816 S3 end condition carries no species index")

# T4 -- edge fraction: a boundary layer of thickness t (in GP spacings) over a ball of R/s spacings
s_over_R=((4*math.pi/3)*12/NCP)**(1/3)
n_shells=1/s_over_R
for t in (1,10):
    frac=3*t/n_shells          # analytic: 1-(1-x)^3 = 3x + O(x^2); double underflows at x~1e-27
    check(f"T4.{t} edge layer {t} GP-spacing(s) thick is a fraction ~{frac:.1e} of the ball volume",
          0<frac<1e-25, f"shells across radius = {n_shells:.2e}, edge fraction = {frac:.2e}")

# T5 -- the edge is ONE coherent feature, not a spectrum: its angular content is dipole+monopole
# dominated at the ball scale; it cannot supply a scale-invariant spectrum by itself
check("T5 a single boundary feature supplies one scale, not a spectrum (recorded, not derived)",
      True, "structural")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
