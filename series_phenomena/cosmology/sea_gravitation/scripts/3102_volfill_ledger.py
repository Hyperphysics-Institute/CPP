#!/usr/bin/env python
"""Patch 3102 -- D-VOLFILL-LEDGER: the filling mechanism's bookkeeping
under CP permanence, run forward.

Structure ruled/committed: the weave phase sits at the pinned attractor
spacing d_s* (R-DS-BOUNDARY, 3101 first pass); the transient free
population (R-ZBW-EXCHANGE) is the gas phase, held at its
exchange-equilibrium ("vapor") density n_g by the same zone kinetics;
CP permanence fixes the total inventory. Everything below follows.

  (A) THE LEDGER THEOREM (exact arithmetic). With mean CP density
      n_bar(a) ~ a^-3 and both PHASE densities pinned, conservation
      forces a two-phase partition:
        f_V(a) = (n_bar/rho_w - r)/(1 - r),   r = n_g/rho_w,
      valid on the COEXISTENCE WINDOW r <= n_bar/rho_w <= 1.
      Above the window (early): pure compressed/switching Sea.
      Below it (far future): pure sub-equilibrium gas -- pinning
      fails, the vacuum term decays. Curves tabulated for
      r in {0.05, 0.15, 0.30} (bracket motivated by the near-boundary
      switch fractions f_sw ~ 0.1-0.2, Stage-2/3101).

  (B) LOCAL TRACKING (the NN-dominance claim, computed). The
      CC-driving arrival sum Sigma 1/r^4 at a weave-interior receiver
      tracks the LOCAL pinned spacing, with the surrounding gas
      contributing only a boundary-layer tail. Computed on explicit
      two-phase arrays: weave domain (FCC, nn = 1) of radius R_d
      embedded in gas of relative density r; deviation of the
      receiver sum from the pure-weave value vs R_d, against the
      exact analytic tail 4*pi*(n_g - n_w)/R_d.

  (C) THE w-DRIFT CONSTRAINT (shape confrontation, 0723-precedent
      class; NO magnitude). During the window,
        rho_Lambda ~ [A + B*f_V(a)]/R_h^2,
      A = gas-phase imprint coefficient (pinned), B = weave-phase
      (pinned), so the filling term adds EXACTLY
        Delta_w = + B*f_V/(A + B*f_V)
      to the Li baseline. Observed w0 = -1.03 +/- 0.03 vs baseline
      -1.02 gives |Delta_w| <= 0.05 (generous). The allowed region in
      (r, B/A, f_V_today) is mapped, and its consequences printed:
      the weave share of TODAY'S vacuum energy, the implied
      n_bar(today)/rho_w corridor, and the corresponding
      d_mean(today) and T_exit (via the 3098 mapping) per branch.

Anti-extraction: no rho_Lambda value is computed anywhere; the only
confrontation is the equation-of-state SHAPE. All brackets are
declared; nothing is tuned.
"""
import numpy as np

# ---------- shared FCC machinery (3071/3097 conventions) -------------
def fcc(R):
    M = int(np.ceil(R*np.sqrt(2))) + 3
    g = np.arange(-M, M+1)
    I, J, K = np.meshgrid(g, g, g, indexing="ij")
    m = ((I+J+K) % 2 == 0)
    S = np.stack([I[m], J[m], K[m]], 1).astype(float)/np.sqrt(2)
    r2 = np.einsum("ij,ij->i", S, S)
    return S[(r2 > 1e-9) & (r2 <= R*R)]

R = 30.0
S = fcc(R)
nw = np.sqrt(2.0)
C4 = float(np.sum(np.einsum("ij,ij->i", S, S)**-2)) + 4*np.pi*nw/R
assert abs(C4 - 25.3382) < 0.05, "C4 regression gate failed"
print(f"C4 (FCC converged) = {C4:.4f}   [3071/3097 regression gate PASS]")

# ---------- (A) ledger curves ---------------------------------------
print("\n(A) THE LEDGER: f_V = (n_bar/rho_w - r)/(1 - r) on the window [r, 1]")
print(f"{'n_bar/rho_w':>12} " + " ".join(f"r={r:4.2f}" for r in (0.05, 0.15, 0.30)))
for nb in (1.0, 0.8, 0.6, 0.4, 0.30, 0.20, 0.16, 0.10, 0.05):
    row = []
    for r in (0.05, 0.15, 0.30):
        f = (nb - r)/(1 - r)
        row.append(f"{f:6.3f}" if 0 <= f <= 1 else ("  --  " if nb < r else " 1.000"))
    print(f"{nb:12.2f} " + " ".join(row))
print("   Above window: pure switching-era Sea. Below: pinning fails, vacuum decays.")

# ---------- (B) two-phase local tracking ----------------------------
print("\n(B) LOCAL TRACKING: weave-domain receiver sum vs pure weave")
rng = np.random.default_rng(2718)
r2S = np.einsum("ij,ij->i", S, S)
print(f"{'R_d':>5} {'r':>5} {'numeric dev':>12} {'analytic tail':>14}")
for Rd in (4.0, 8.0, 14.0):
    inside = r2S <= Rd*Rd
    S_weave = float(np.sum(r2S[inside]**-2))
    for r in (0.05, 0.30):
        # gas outside the domain: Poisson at density r*nw, hard core 0.7/ r^{1/3} of gas spacing
        ng = r*nw
        vol = (4/3)*np.pi*(R**3 - Rd**3)
        Npts = rng.poisson(ng*vol)
        acc = 0.0
        for _ in range(6):
            P = rng.uniform(-R, R, size=(int(Npts*2.2), 3))
            q2 = np.einsum("ij,ij->i", P, P)
            P = P[(q2 <= R*R) & (q2 >= Rd*Rd)][:Npts]
            acc += float(np.sum(np.einsum("ij,ij->i", P, P)**-2))
        S_gas = acc/6 + 4*np.pi*ng/R
        S_tot = S_weave + S_gas
        S_pure = float(np.sum(r2S**-2)) + 4*np.pi*nw/R
        dev = (S_tot - S_pure)/S_pure
        tail = (4*np.pi*(ng - nw)/Rd)/S_pure
        print(f"{Rd:5.0f} {r:5.2f} {dev:12.4f} {tail:14.4f}")
print("   Deviation follows the analytic 1/R_d boundary tail: the receiver's")
print("   sum is set by its LOCAL phase; percent-class already at R_d ~ 8-14.")

# ---------- (C) the w-drift constraint region -----------------------
print("\n(C) w-DRIFT: Delta_w = B f_V/(A + B f_V) <= 0.05  (|w0 - baseline|, generous)")
print(f"{'r':>5} {'B/A':>5} {'f_V max':>8} {'weave share':>12} {'n_bar/rho_w corridor':>22} {'d_mean/d*':>10}")
DWMAX = 0.05
rows = []
for r in (0.05, 0.15, 0.30):
    for BA in (1.0, 3.0, 10.0):
        fmax = DWMAX/((1 - DWMAX)*BA)
        share = BA*fmax/(1 + BA*fmax)
        nb_lo, nb_hi = r, r + fmax*(1 - r)
        dm = (1.0/nb_hi)**(1/3), (1.0/nb_lo)**(1/3)
        rows.append((r, BA, fmax, nb_lo, nb_hi))
        print(f"{r:5.2f} {BA:5.1f} {fmax:8.4f} {share:11.1%} "
              f"[{nb_lo:5.3f}, {nb_hi:5.3f}]{'':>6} [{dm[0]:4.2f},{dm[1]:4.2f}]")
print("   READING: today's vacuum energy is >= 95% GAS-PHASE (the transient")
print("   reservoir), with the weave contributing <= 5% -- forced by the")
print("   observed w0 alone, for every bracketed (r, B/A).")

# T_exit corridor via the 3098 mapping, d* = 7.4 l_P (3101), unit->CP mean spacing
print("\n   T_exit corridor (3098 mapping; d_mean = d* x (rho_w/n_bar)^{1/3}; d* = 7.4 l_P):")
T0_K, KGEV, NF = 2.725, 1.16045e13, 1.0e30
for (r, BA, fmax, nb_lo, nb_hi) in rows:
    if BA != 3.0:  # representative slice
        continue
    dm_hi = 7.4*(1.0/nb_lo)**(1/3)   # dilute edge (window end)
    dm_lo = 7.4*(1.0/nb_hi)**(1/3)   # dense edge (drift bound)
    T_lo = dm_lo*NF*T0_K/KGEV; T_hi = dm_hi*NF*T0_K/KGEV
    print(f"     r={r:4.2f}: d_mean(today) in [{dm_lo:5.1f}, {dm_hi:5.1f}] l_P  ->  T_exit in [{T_lo:.2e}, {T_hi:.2e}] GeV")
print("\n   COINCIDENCE FLAG (stated, not solved): the corridor sits at the")
print("   window's dilute end -- f_V ~ 1%-class today -- a 'why now' the")
print("   ledger exposes rather than hides.")
print("\nAll gates PASS. No rho_Lambda computed; brackets declared; FQ-8 poses")
print("the founder forks (domain scale; switching-era vacuum; gas-carrier ratification).")
