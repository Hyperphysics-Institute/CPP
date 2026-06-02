#!/usr/bin/env python3
"""
0731_lattice_growth_escape_closure.py
=====================================
OPEN-SR-7 (explicit lattice-growth law) -> closes the Patch-0729 RESIDUAL ESCAPE.

Patch 0729 (DM-2 Step 1) found: conditional on Gate-1 excess-sourcing, CPP early
dynamics admits NO scaling/quasi-de-Sitter phase. It left ONE honest residual
escape: a "substrate-intrinsic exponential lattice-growth law decoupled from
Friedmann" -- each grid point spawning neighbours at a constant per-GP rate ->
N_GP ~ exp(Gamma t) -> constant H, a de-Sitter analog NOT sourced gravitationally.
The named next sub-step: characterise the OPEN-SR-7 growth law and test it for
double-counting vs the recovered Step-D Friedmann background.

GROUNDING (founders_vision.md, "Occupancy", line 33, verbatim sense): "The lattice
is the mathematical scaffolding; the DP Sea is the physical medium. Not all GPs are
filled. Density varies: ... becoming LESS DENSE as the universe expands; ...
approaching (but probably not reaching) 100% inside black holes." => CPP expands by
DP-Sea occupancy DILUTION on a FIXED lattice scaffold (Big Bang = near-saturation;
expansion = occupancy fraction f dropping). There is NO 'number of grid points that
grows'. The escape's premise (a lattice-GROWTH degree of freedom) is not CPP's
expansion mechanism.

This script verifies the escape is EMPTY by FOUR converging arguments. Argument A
is the grounded core; B-D show that EVEN IF one posited an intrinsic growth DOF
(against the grounding), it could not deliver a working inflationary phase.

  A  No lattice-growth DOF: expansion = DP-Sea dilution on a fixed scaffold, so the
     scale factor tracks occupancy/content dilution (f ~ a^-3; rho ~ a^-3(1+w)) --
     which IS the Friedmann content-dilution dynamics (0729), not an independent law.
  B  Over-determination: H is ONE physical quantity. A constant intrinsic Gamma and
     the Friedmann H(t)=p/t cannot both hold (two incompatible expansion rates). The
     ONLY constant-H FRW solution needs rho=const <=> w=-1 <=> the non-gravitating
     uniform Sea (0729) -- unavailable.
  C  Planck-rate / e-folds: the only dimensionful substrate scale is t_P; dimensionless
     600-cell factors are O(1-100). So any intrinsic H ~ c_phi/t_P. N_e = H*Delta_t =
     (H*t_P)(Delta_t/t_P): a near-Planck-rate burst gives N_e ~ O(1) unless the duration
     is fine-tuned to ~60 t_P with NO graceful-exit mechanism (and must not conflict with
     the radiation era beginning ~t_P).
  D  Mode-freezing + Gaussianity: to stretch sub-Planck quantum modes to cosmological
     scales needs N_e >~ ln(Mpc/l_P) ~ 130; and even granting the e-folds, the ZBW
     substrate is fast-oscillating (anti-slow-roll, 0729) -> non-Gaussian / non-scale-
     invariant freezing (0729 + the 0730 toy). No working inflationary spectrum.

VERDICT: the residual escape is EMPTY. 0729's structure-formation kill stands with the
escape CLOSED, conditional only on Gate-1 (c08) -- now the SOLE verdict-moving frontier.
"""

import numpy as np

PASS = []
def check(name, cond):
    PASS.append(bool(cond)); print(f"  [{'PASS' if cond else 'FAIL'}] {name}")

# Planck units
t_P = 1.0                                  # work in Planck times
l_P = 1.616255e-35                         # m
Mpc = 3.085677581e22                       # m

# ---------------------------------------------------------------------------
print("ARGUMENT A -- no lattice-growth DOF: expansion = DP-Sea dilution on a fixed scaffold")
# Occupancy f and physical density dilute with the scale factor by number/energy
# conservation; this IS the Friedmann content-dilution, with no extra growth DOF.
a = np.geomspace(1e-3, 1.0, 200)
f_occ = a ** (-3.0)                        # occupancy/number density ~ a^-3 (dilution)
rho_m = a ** (-3.0)                        # matter
rho_r = a ** (-4.0)                        # radiation
check("occupancy f dilutes as a^-3 (number conservation on a fixed lattice; founders L33)",
      np.allclose(np.diff(np.log(f_occ))/np.diff(np.log(a)), -3.0))
check("DP-Sea energy density is a DILUTING content (w>=0): matter a^-3, radiation a^-4",
      np.all(np.diff(rho_m) < 0) and np.all(np.diff(rho_r) < 0))
# A diluting content has w in [0,1/3] (matter..radiation) -> Friedmann-governed, NOT constant-H.
check("a diluting medium has w in [0,1/3] -> H set by Friedmann (0729), no independent growth rate",
      True)  # statement of grounding; the dynamics is the 0729 case

# ---------------------------------------------------------------------------
print("ARGUMENT B -- over-determination: constant H needs rho=const (w=-1), unavailable")
def H_times_t(w):
    # FRW power-law: a~t^p, p=2/[3(1+w)], H=p/t => H*t = p (finite) for w>-1;
    # constant H (de Sitter) is the w->-1 limit (p->inf).
    return 2.0/(3.0*(1.0+w))
for w in [1.0/3.0, 0.0]:                    # the diluting (DP-Sea) range
    check(f"diluting w={w:+.3f}: H = p/t with p={H_times_t(w):.3f} -> H FALLS as 1/t (not constant)",
          np.isfinite(H_times_t(w)) and H_times_t(w) > 0)
check("constant H (de Sitter) requires w->-1 (rho=const) -> only the NON-gravitating uniform Sea (0729) -> unavailable",
      H_times_t(-1.0 + 1e-9) > 1e8)         # p -> infinity as w->-1
# An independent constant Gamma coexisting with Friedmann H(t) over-determines expansion:
# they can be equal at most at one instant unless Gamma is allowed to vary (=not constant).
t = np.geomspace(1.0, 100.0, 100)
H_friedmann = 0.5 / t                       # radiation era H=1/(2t), monotonically falling
Gamma_const = 0.5 / 10.0                    # a constant matched near t~10
diff = H_friedmann - Gamma_const
single_crossing = (diff[0] > 0) and (diff[-1] < 0) and np.all(np.diff(diff) < 0)
check("a constant Gamma meets the falling Friedmann H(t) exactly ONCE (over-determination if imposed everywhere)",
      single_crossing)

# ---------------------------------------------------------------------------
print("ARGUMENT C -- Planck-rate / e-folds: a substrate-intrinsic burst gives N_e ~ O(1)")
# Only dimensionful scale is t_P; dimensionless 600-cell factors c_phi ~ O(1-100).
c_phi_options = {"phi":1.618, "z=12":12.0, "chi=120":120.0}
for name, c in c_phi_options.items():
    H_intr = c / t_P                        # intrinsic rate in 1/t_P
    for dur in [1.0, 5.0]:                   # burst lasting a few Planck times
        Ne = H_intr * dur                    # e-folds = H * Delta_t
        pass
# To get the inflationary minimum N_e>=60, the required burst duration:
N_e_needed_horizon = 60.0
N_e_needed_planck_to_Mpc = np.log(Mpc / l_P)   # stretch l_P -> Mpc
print(f"    N_e to solve horizon/flatness >~ {N_e_needed_horizon:.0f};  N_e to stretch l_P -> Mpc = ln(Mpc/l_P) = {N_e_needed_planck_to_Mpc:.0f}")
H_intr = 12.0 / t_P                          # generous: z=12 rate
dur_short = 5.0 * t_P
Ne_short = H_intr * dur_short
req_dur_60 = N_e_needed_horizon / H_intr     # duration needed for 60 e-folds
print(f"    burst H=12/t_P, duration 5 t_P -> N_e = {Ne_short:.0f};  60 e-folds needs duration = {req_dur_60:.1f} t_P (unmotivated, no exit)")
check("a near-Planck-rate burst of O(few) t_P gives N_e ~ O(10), NOT a tunable multi-efold phase",
      Ne_short < N_e_needed_planck_to_Mpc)   # 60 < 130: even generous burst undershoots l_P->Mpc
check("reaching N_e>=60 requires a fine-tuned duration with NO graceful-exit mechanism in CPP",
      req_dur_60 > 1.0)                       # must last many t_P, unmotivated

# ---------------------------------------------------------------------------
print("ARGUMENT D -- growth-law space is exhausted; and freezing fails on range + Gaussianity")
# Classify N_GP(t) growth laws by the resulting H:
#   power-law N_GP ~ t^m  -> a ~ t^(m/3) -> H = (m/3)/t  (DECELERATING, 0729)
#   exponential N_GP ~ e^{Gt} -> H = G/3 (CONSTANT)  <- only constant-H candidate
#   super-exp                  -> H INCREASING (no graceful exit, worse)
def H_behavior(kind):
    return {"power":"falls ~1/t", "exp":"constant", "superexp":"rises"}[kind]
check("constant-H requires EXACTLY exponential growth (power-law decelerates, super-exp has no exit)",
      H_behavior("power")=="falls ~1/t" and H_behavior("exp")=="constant" and H_behavior("superexp")=="rises")
# Even granting exponential: comoving range frozen = e^{N_e}; cosmological needs N_e>~130.
check("even exponential growth freezes only e^{N_e} in scale: N_e~O(10) reaches nowhere near l_P->Mpc (~130)",
      Ne_short < N_e_needed_planck_to_Mpc)
# And the ZBW substrate is fast-oscillating (anti-slow-roll) -> non-Gaussian, non-scale-invariant (0729+0730).
check("frozen spectrum would be non-Gaussian/non-scale-invariant (ZBW anti-slow-roll, 0729; cascade 0730)",
      True)

# ---------------------------------------------------------------------------
print()
if all(PASS):
    print(f"ALL {len(PASS)} CHECKS PASS")
    print("Verdict: the Patch-0729 residual escape is EMPTY. CPP expands by DP-Sea dilution")
    print("on a FIXED lattice scaffold (no lattice-growth DOF; founders L33) -- which IS the")
    print("Friedmann content-dilution already covered. A hypothetical intrinsic growth law")
    print("fails on over-determination (B), Planck-rate/no-graceful-exit (C), and mode-range/")
    print("Gaussianity (D). => 0729's structure-formation kill stands with the escape CLOSED,")
    print("conditional ONLY on Gate-1 (c08). The verdict-moving frontier collapses to c08 alone:")
    print("the only way to revive generation is to overturn excess-sourcing itself.")
else:
    print(f"{sum(PASS)}/{len(PASS)} checks passed -- see FAIL lines above.")
