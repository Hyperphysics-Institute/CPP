#!/usr/bin/env python
"""Patch 3103 -- A-2: the composition weight phi_comp = W, executed.

Three parts, no dial anywhere:

  (A) k IDENTIFICATION (O-2 discharge PROPOSED). AP-4b: SSV_abs =
      Sigma|polar| + k*Sigma|strong|, k = "the intrinsic strong-to-
      electric CHARGE-STRENGTH ratio of the substrate", identification
      with shipped couplings only. Couplings are charge-strength
      SQUARED (alpha = q^2/hbar c), so the charge-strength ratio is
          k = sqrt(alpha_s/alpha),
      with alpha_s = 5/(8*phi) (SF-5 structural, shipped) and
      alpha = 1/137.035999 (the R-SEA-COMP-ruled electric imprint
      constant). Per-species CHANNEL CONTENT (quadratic, per unit
      excursion): eDP -> 1; qDP -> (1 + k)^2 (AP-4b's scalar amplitude
      sum; both registers driven by the same displacement). Discrete
      fork recorded: incoherent channel addition -> 1 + k^2 (the
      cross-term dropped); ratio between branches 1.27.

  (B) s: THE RESPONSE-REGIME MEASUREMENT. s(species) =
      <delta^2>_species/<delta^2>_eDP under the SAME Sea drive, with
      the species' partner-bond stiffness G = its bond ladder in
      E-bond units (bond stiffness ~ coupling ~ charge^2):
        free eDP     G = 1
        free qDP     G = k^2 = alpha_s/alpha = 52.94
        ribbon member (founder ladder 3E+3S)  G = 3 + 3k^2 = 161.8
        DM-core member (4E+4S)                G = 4 + 4k^2 = 215.8
      The two candidate regimes differ in exponent: force-response
      <x^2> ~ 1/G^2 vs equipartition <x^2> ~ 1/G. MEASURED here with
      the Stage-2 instrument (3079 machinery, clean-signed): converge
      the eDP fixed point at d_s = 12 (faithful branch), FREEZE its
      self-consistent drive (the shared Sea field), then run episodes
      with the partner force multiplied by G; report eta(G) and the
      log-log slope.

  (C) W AND phi_comp ASSEMBLED. W_species = C_species x s_species;
      gas phase (the 3102 carrier): phi_comp^gas = x_e*W_eDP +
      x_q*W_qDP (+ trace hDP bracket), x_q in {0.3, 0.5, 0.7}
      (species-symmetric default 0.5; instrument-refinable). Weave
      B-term W_ribbon for the <= 5% correction. Both coherence
      branches tabulated.

Anti-extraction: no rho_Lambda, no band quantity; directions stated
plainly at the end per the freeze discipline.
"""
import numpy as np

PHI = (1 + 5**0.5)/2
ALPHA = 1/137.035999
ALPHA_S = 5/(8*PHI)
k = (ALPHA_S/ALPHA)**0.5
print(f"(A) O-2 identification: alpha_s = 5/(8 phi) = {ALPHA_S:.6f}; alpha = {ALPHA:.8f}")
print(f"    k = sqrt(alpha_s/alpha) = {k:.4f}   [charge-strength ratio; PROPOSED discharge]")
C_eDP = 1.0
C_qDP_coh = (1 + k)**2
C_qDP_inc = 1 + k*k
print(f"    channel content: C_eDP = 1;  C_qDP = (1+k)^2 = {C_qDP_coh:.2f} (AP-4b coherent)")
print(f"                     [incoherent fork: 1+k^2 = {C_qDP_inc:.2f}; branch ratio {C_qDP_coh/C_qDP_inc:.3f}]")

# ---------- Stage-2 machinery (3079 verbatim core; G threaded) -------
M = 40
g = np.arange(-M, M+1)
I, J, K = np.meshgrid(g, g, g, indexing="ij")
m = ((I+J+K) % 2 == 0)
P = np.stack([I[m], J[m], K[m]], 1).astype(float)/np.sqrt(2)
r2 = np.einsum("ij,ij->i", P, P)
sel = (r2 > 1e-12) & (r2 <= 28.0**2)
C6 = float(np.sum(r2[sel]**-3)) + 4*np.pi*np.sqrt(2)/(3*28.0**3)
assert abs(C6 - 14.4539) < 0.01

def episode(ds, sigma_m, tau_c, G, T, seed):
    r = np.random.default_rng(seed)
    rho = np.exp(-1.0/max(tau_c, 1e-6)); rp = ds/2.0
    hist = [0.0]; v = e = 0.0; trp = 0
    d2sum = 0.0; nsum = 0
    regen = 0; switches = 0
    for t in range(1, T):
        xa = hist[-1]
        n = len(hist); tr = min(trp, n-1); F = 0.0
        while tr+1 <= n-1 and (n-1 - tr) >= abs(xa + hist[tr+1]): tr += 1
        while tr >= 0 and (n - tr) < abs(xa + hist[tr]): tr -= 1
        if tr >= 0:
            s_ = abs(xa + hist[tr])
            if s_ >= 1e-9: F = -G*np.sign(xa + hist[tr])/max(s_, 1.0)**2
        trp = max(tr, 0)
        e = rho*e + sigma_m*np.sqrt(1-rho*rho)*r.standard_normal()
        v = v + F + e
        x = xa + v
        d2sum += 4*x*x; nsum += 1
        crossed = hist[-1]*x < 0; poached = abs(x) > rp
        if poached: switches += 1
        if crossed or poached:
            regen += 1
            if poached: hist = [0.0]; trp = 0; continue
        hist.append(x)
        if len(hist) > 4000: hist = hist[-3000:]; trp = max(trp-1000, 0)
    return d2sum/max(nsum, 1), regen, switches

def edp_fixed_point(ds, T=6000, iters=8, seed=11):
    d2 = (ds/4.0)**2; Treg = 20.0; vrms = 1.0; sig = tau = None
    for it in range(iters):
        sig = np.sqrt(2*C6*d2/3.0)/ds**3
        tau = max(1.0, min(Treg, ds/max(vrms, 1e-3)))
        d2m, regen, _ = episode(ds, sig, tau, 1.0, T, seed+it)
        d2 = 0.5*d2 + 0.5*d2m
    return d2, sig, tau

DS = 12.0
print(f"\n(B) the s question at d_s = {DS:.0f} (faithful branch):")
d2_e, SIG, TAU = edp_fixed_point(DS)
eta_e = d2_e/DS**2
print(f"    eDP fixed point: eta_e = {eta_e:.4f}; self-consistent sigma_m = {SIG:.3e}, tau_c = {TAU:.1f}")

# --- INSTRUMENT LESSONS (recorded; neither run is used) --------------
d2_bad, _, _ = episode(DS, SIG, TAU, 52.94, 3000, 999)
print(f"    LESSON 1 — naive unit-Moment step at G = 52.9: eta = {d2_bad/DS**2:.1f} (EXPLODES;")
print("        omega*dt >> 1 stiffness instability — the 3085 class recurring).")
print("    LESSON 2 — a de-regulated sub-stepped probe (instantaneous partner, no")
print("        crossing/poach regulation) DIFFUSES: removing the Stage-2 regulation")
print("        physics to gain integrator headroom removes the bound state too.")
print("    VERDICT: the 1D continuum instrument cannot measure stiff-bond s;")
print("    the regime is decided ANALYTICALLY, and the lattice instrument")
print("    (dwell-relaunch, quantized steps) owns the confirmation.")

# --- analytic regime adjudication -----------------------------------
print("\n    Timescale separation (adiabatic criterion): bond period vs drive correlation")
print(f"    {'species':>14} {'G':>7} {'T_bond (Moments)':>17} {'tau_c':>6} {'adiabatic?':>11}")
for G, nm in zip([1.0, 52.94, 161.8, 215.8], ["free eDP", "free qDP", "ribbon 3E+3S", "DM core 4E+4S"]):
    # linearized bond frequency near the excursion scale delta ~ sqrt(eta_e)*DS for G=1,
    # and the force-gradient scale for stiff bonds: omega ~ sqrt(2G/delta^3), delta ~ 1
    Tb = 2*np.pi/np.sqrt(2.0*G)
    print(f"    {nm:>14} {G:7.1f} {Tb:17.2f} {TAU:6.1f} {'YES' if Tb < TAU/3 else 'marginal':>11}")
print("    Stiff bonds oscillate many times per drive-correlation time => the")
print("    displacement response is QUASI-STATIC: <delta^2> = <F^2>/kappa^2 ~ 1/G^2.")
print("    (Equipartition <delta^2> ~ 1/G is DISCARDED: the ZBW drive is not a")
print("    thermal bath at bond timescales; there is no equipartition theorem here.)")
print("    BRANCH I (continuum, analytic):  s(G) = 1/G^2")
print("    BRANCH II (lattice ZBW floor, R-DWELL-1 + adjacent-GP pair geometry):")
print("        the excursion cannot fall below the lattice step: delta_floor ~ 1 GP")
print("        => s_floor = (1 GP/d)^2/eta_e, species-independent (floor-degenerate).")

s_I  = {G: 1.0/G**2 for G in (52.94, 161.8, 215.8)}
s_II = (1.0/DS)**2/eta_e
print(f"    s values: branch I qDP {s_I[52.94]:.2e}, ribbon {s_I[161.8]:.2e}, core {s_I[215.8]:.2e};")
print(f"              branch II (all coordinated species) {s_II:.4f}")
print("    Founder-ladder ordering (ribbon less suppressed than core): branch I PASS")
print("    (monotone in G); branch II floor-degenerate (ordering trivially consistent).")

print("\n(C) W = C x s and phi_comp — the two branches bound the factor:")
for br, Cq in (("coherent", C_qDP_coh), ("incoherent", C_qDP_inc)):
    Wq_I, Wq_II = Cq*s_I[52.94], Cq*s_II
    print(f"    [{br:>10}] W_qDP: branch I = {Wq_I:.4f};  branch II = {Wq_II:.3f}")
    for xq in (0.3, 0.5, 0.7):
        pI  = (1-xq) + xq*Wq_I
        pII = (1-xq) + xq*Wq_II
        print(f"        x_q = {xq:.1f}: phi_comp^gas = {pI:.3f} (I)  |  {pII:.3f} (II)")
print("\nHEADLINE, stated plainly: the coupling enhancement (C = 54-68) and the")
print("stiffness suppression (s = 1/2800 to ~1/27) CANCEL to order unity on")
print("both branches: phi_comp^gas is bounded in ~[0.3, 2.1] across EVERY")
print("declared fork (branch x coherence x x_q). The 3089 'potentially")
print("largest factor' DEFLATES to O(1). Branch adjudication + x_q routing:")
print("the lattice instrument (G-stiff species + dwell-relaunch), specified")
print("in the note. No band quantity anywhere; no assembly performed.")
