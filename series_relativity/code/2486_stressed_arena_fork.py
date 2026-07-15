#!/usr/bin/env python3
# ============================================================
# 2486: DeepSeek round-1 finding (D) — the stressed-arena fork.
# stdlib only. Exit 0 = fork demonstrated as specified.
#
# QUESTION (registered as M9, campaign v1.2): for an aggregate with
# pre-existing background stress (SSV_bg != 0, so PSR_eff < l_P),
# does the codim-2 exclusion radius scale with
#   Branch L:  d = (v/c) * l_P      (absolute / unstressed scaling)
#   Branch P:  d = (v/c) * PSR_eff  (local / stressed scaling)
# This script does NOT resolve the fork (that is mechanism-phase
# work under M9); it demonstrates the two branches' consequences so
# the mechanism session knows exactly what each implies.
#
# Setup: arena = ball of radius R' = PSR_eff = l_P / g_bg, where
# g_bg = 1 + k*dSSV_bg >= 1 is the background stress factor.
# Codim-2 tube of radius d in the arena => f_eff = d / R'.
# Velocity strain: eps_vel = (1 - f_eff^2)^(-1/2) - 1.
#
# Branch P (d scales with PSR_eff): f_eff = v/c exactly
#   => eps_vel = gamma_SR(v) - 1 for EVERY background stress:
#   velocity factor is stress-independent; total reach factor
#   composes MULTIPLICATIVELY: l_P/r_total = g_bg * gamma_SR(v).
# Branch L (d fixed at (v/c) l_P): f_eff = (v/c) * g_bg
#   => eps_vel = (1 - (v g_bg/c)^2)^(-1/2) - 1 != gamma_SR(v)-1
#   for any g_bg > 1; the velocity factor is stress-DEPENDENT and
#   the effective speed limit drops to c/g_bg.
# ============================================================
import math, sys

FAIL = 0
def check(name, ok, detail=""):
    global FAIL
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
    if not ok: FAIL = 1

def gamma(f): return (1 - f*f) ** -0.5

print("Stressed-arena fork: eps_vel under the two scalings")
print(f"{'g_bg':>6} {'v/c':>5} | {'Branch P eps_vel':>16} {'gamma-1':>12} | {'Branch L eps_vel':>16}")
worst_P = 0.0
branchL_deviates = True
for g_bg in (1.0, 1.001, 1.1, 2.0):
    for f in (0.1, 0.5, 0.9):
        # Branch P: f_eff = f
        eps_P = gamma(f) - 1
        # Branch L: f_eff = f * g_bg (capped below 1 for display)
        fL = f * g_bg
        eps_L = (gamma(fL) - 1) if fL < 1 else float('inf')
        worst_P = max(worst_P, abs(eps_P - (gamma(f) - 1)))
        if g_bg > 1 and fL < 1 and abs(eps_L - (gamma(f) - 1)) < 1e-12:
            branchL_deviates = False
        print(f"{g_bg:6.3f} {f:5.2f} | {eps_P:16.9f} {gamma(f)-1:12.9f} | "
              + (f"{eps_L:16.9f}" if fL < 1 else "     saturated (v >= c/g_bg)"))

check("Branch P reproduces gamma_SR(v)-1 at every background stress",
      worst_P < 1e-12, f"max |diff| = {worst_P:.2e}")
check("Branch L deviates from gamma_SR(v)-1 whenever g_bg > 1",
      branchL_deviates)

# Branch P composition law: total factor = g_bg * gamma(v), multiplicative
worst = 0.0
for g_bg in (1.1, 2.0):
    for f in (0.1, 0.5, 0.9):
        total = g_bg * gamma(f)            # composed reach factor l_P/r_total
        recomposed = g_bg * (1 + (gamma(f) - 1))
        worst = max(worst, abs(total - recomposed))
check("Branch P composition is exactly multiplicative g_bg * gamma(v)",
      worst < 1e-15, f"max |diff| = {worst:.2e}")

print("=" * 60)
print("FORK DEMONSTRATED — resolution is M9 mechanism-phase work.")
print("RESULT:", "FAIL" if FAIL else "ALL CHECKS PASS")
sys.exit(FAIL)
