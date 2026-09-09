#!/usr/bin/env python3
"""
Patch 3810 (EU lane) -- OPEN-EU-TENSOR-1 registered: the tensor-to-scalar exposure of the
crowding engine, and why the m^2 phi^2 value does not transfer. Verify script.

T1  The m^2 phi^2 analogy EU-1 draws for its tilt would, if it also fixed r, give
    r = 8/N_* ~ 0.14 at N_* = 57 -- EXCLUDED by BICEP/Keck 2021 (r < 0.036 at 95 %).
    Recorded so the exposure is stated in the corpus's own words.
T2  That transfer requires r = 16*epsilon with P_zeta = H^2/(8 pi^2 eps M^2), i.e. a canonical
    scalar field sourcing zeta. The crowding engine sources zeta by the held-stack boost in the
    delta-N formalism with an amplitude prefactor (kappa kT)^2 the corpus has not derived (A_s
    adopted, not counted). So r is NOT fixed by the tilt; it is fixed by H alone if the tensor
    sector is GR's: r = P_t / A_s = 2 H^2 / (pi^2 M_Pl^2 A_s).  Checked: r is monotone in H and
    independent of any engine constant.
T3  The bound r < 0.036 with A_s = 2.1e-9 is H_pivot <= 4.7e13 GeV -- the SAME number 3806
    already used as an input. So the tensor exposure collapses onto the open engine-rate debt
    (kappa_0): pass iff the derived H at the pivot is <= 4.7e13 GeV = 3.9e-6 E_Pl.
T4  With the corpus's own H_eff ~ N_rem (EU-1 eq. Heff), H at the pivot is 57/60.5 of H_init,
    so the bound on H_pivot is a bound on the whole window to within 6 %: the engine derivation
    has one number to hit, not a profile.
T5  Bookkeeping correction: the initial-stack occupation is n_init = N_CP/N_GP ~ 1e80/13 ~ 1e79
    (EU-1 eq. Nstar), not the 1e74 quoted at 3710/3805/3808 (that is n_bar at the OBSERVABLE
    epoch, e^171). Checked: ln(1e79)/3 = 60.6 (the paper's total) and ln(1e74)/3 = 56.8 (the
    pivot). 3808's sanity bounds get worse by 5 orders under the corrected value (still excluded).
"""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

M_PL_RED = 2.435e18     # reduced Planck mass, GeV
E_PL     = 1.221e19     # Planck energy, GeV
A_S      = 2.1e-9       # Planck 2018 scalar amplitude at the pivot
R_BOUND  = 0.036        # BICEP/Keck 2021, 95 %
N_STAR   = 57.0
N_TOT    = 60.5
ALPHA    = 7.2973525693e-3

res = []
def check(name, cond, detail=""):
    res.append(cond); print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))

# T1
r_m2phi2 = 8.0 / N_STAR
check("T1 m^2 phi^2 transfer would give r = 8/N_* ~ 0.14 > 0.036: excluded if it applied", r_m2phi2 > R_BOUND, f"r = {r_m2phi2:.3f}")

# T2: r as a function of H alone (tensor sector GR's)
def r_of_H(H_GeV): return 2.0*H_GeV**2 / (math.pi**2 * M_PL_RED**2 * A_S)
Hs = [1e12*(10**(0.1*i)) for i in range(40)]
rs = [r_of_H(h) for h in Hs]
monotone = all(rs[i+1] > rs[i] for i in range(len(rs)-1))
check("T2 with the tensor sector GR's, r = 2H^2/(pi^2 M^2 A_s) depends on H alone (monotone, no engine constant)", monotone)

# T3: the bound on H
H_max = math.pi * M_PL_RED * math.sqrt(R_BOUND * A_S / 2.0)
check("T3 r < 0.036 <=> H_pivot <= 4.7e13 GeV, the input 3806 already used", abs(H_max/4.7e13 - 1) < 0.03,
      f"H_max = {H_max:.2e} GeV = {H_max/E_PL:.1e} E_Pl")

# T4: H_pivot / H_init under H_eff ~ N_rem
ratio = N_STAR / N_TOT
check("T4 H_eff ~ N_rem: H_pivot/H_init = 57/60.5, the window is flat to ~6 %", abs(ratio - 0.942) < 0.01, f"{ratio:.3f}")

# T5: initial vs observable-epoch occupation
n_init = 1e80/13.0
check("T5 n_init = 1e80/13 ~ 1e79 gives the paper's total 60.5; 1e74 = e^171 is the pivot-epoch n_bar",
      abs(math.log(n_init)/3 - 60.5) < 0.2 and abs(math.log(1e74)/3 - 56.8) < 0.1,
      f"ln(n_init)/3 = {math.log(n_init)/3:.1f}; ln(1e74)/3 = {math.log(1e74)/3:.1f}")
# 3808 bounds under the corrected N (12 stacks of 1e79 -> wait: 12 stacks hold N_CP; per stack ~ 1e80/12)
N_stack = 1e80/12
E_univ = 3.0e54*(2.99792458e8)**2/1.956e9
orders_naive = math.log10(12*0.5*ALPHA*N_stack**2/E_univ)
orders_bind  = math.log10(6*N_stack*ALPHA/E_univ)
eps_max = E_univ/(12*N_stack)
check("T5b 3808's sanity bounds under N_stack ~ 1e79: naive +94 orders, binding +15, eps ~ 1e-18 E_Pl (~20 GeV)",
      orders_naive > 90 and 12 < orders_bind < 20 and 1e-20 < eps_max < 1e-16,
      f"+{orders_naive:.0f}, +{orders_bind:.0f}, eps_max ~ {eps_max*E_PL:.0f} GeV per CP")

n = sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n == len(res) else 1)
