#!/usr/bin/env python
"""Patch 3101 -- D-DS-BOUNDARY first pass: locating the fidelity-monogamy
boundary d_s* with the Stage-2 self-consistent machinery (3079; the 1D
instrument the 3088 sign audit certified CLEAN), refined grid, three
seeds, and the A-1 weave variant.

R-DS-BOUNDARY rules that the boundary PRODUCES d_s. The Stage-2 coarse
scan bracketed it ([4: RUNAWAY] [6: MARGINAL] [7: jittering]). Here:

  (A) FINE SCAN, E-register reference (one unit dipole per site, the
      3079 convention): d_s in {4.5 .. 8.0} step 0.25-0.5, seeds
      {11, 23, 47}. Per cell the damped fixed point is classified:
        RUNAWAY  : f_sw >= 0.5, or the fixed point fails to converge
                   (relative d2 step > 0.5 at final iteration), or
                   apogee-class d2 beyond the poaching scale.
        FAITHFUL : converged, f_sw < 0.5.
      d_s* = midpoint of the highest-RUNAWAY / lowest-FAITHFUL pair
      that is consistent across all seeds; half-width = grid step /2
      plus seed spread.

  (B) WEAVE VARIANT (A-1 census applied to the DRIVE): each neighbour
      site carries TWO incoherent unit dipoles (eDP + qDP electric)
      => <E^2> doubles => sigma_m x sqrt(2). Expected shift ~2^{1/6}
      = 1.122 by the drive^{1/6} scaling; measured here.

  (C) SIXTH-ROOT ROBUSTNESS: the boundary's sensitivity to the drive
      normalisation -- scan drive multipliers {0.5, 1, 2, 4} at the
      reference geometry and fit d_s*(drive) to a power law. The
      exponent near 1/6 is the reason O(1) uncertainties (arrangement
      bracket, C6 reference, coordination corrections) move the
      boundary only ~10%-class.

Provenance: episode/fixed_point are the 3079 functions verbatim,
except (i) a drive multiplier `dmul` threaded into sigma_m,
(ii) explicit runaway classification, (iii) iters=9 for tighter
convergence near the fold. No band quantity appears anywhere.
"""
import numpy as np

# ---- C6 for the FCC reference array at nn = 1 (exact; 3079 verbatim) ----
M = 40
g = np.arange(-M, M+1)
I, J, K = np.meshgrid(g, g, g, indexing="ij")
msk = ((I+J+K) % 2 == 0)
P = np.stack([I[msk], J[msk], K[msk]], 1).astype(float)/np.sqrt(2)
r2 = np.einsum("ij,ij->i", P, P)
sel = (r2 > 1e-12) & (r2 <= 28.0**2)
C6 = float(np.sum(r2[sel]**-3)) + 4*np.pi*np.sqrt(2)/(3*28.0**3)
assert abs(C6 - 14.4539) < 0.01, "failed to reproduce the 3079 C6"
print(f"C6 (FCC, nn=1) = {C6:.4f}   [3079 regression gate PASS]")

def episode(ds, sigma_m, tau_c, T, seed):
    r = np.random.default_rng(seed)
    rho = np.exp(-1.0/max(tau_c, 1e-6))
    rp = ds/2.0
    hist = [0.0]; v = e = 0.0; trp = 0
    d2sum = 0.0; nsum = 0; vsum = 0.0
    regen = 0; switches = 0; t_last = 0; regs = []
    apmax = 0.0; apos = []
    for t in range(1, T):
        xa = hist[-1]
        n = len(hist); tr = min(trp, n-1); F = 0.0
        while tr+1 <= n-1 and (n-1 - (tr)) >= abs(xa + hist[tr+1]):
            tr += 1
        while tr >= 0 and (n - tr) < abs(xa + hist[tr]):
            tr -= 1
        if tr >= 0:
            s = abs(xa + hist[tr])
            if s >= 1e-9:
                F = -np.sign(xa + hist[tr])/max(s, 1.0)**2
        trp = max(tr, 0)
        e = rho*e + sigma_m*np.sqrt(1-rho*rho)*r.standard_normal()
        v = v + F + e
        x = xa + v
        d = 2*abs(x); d2sum += d*d; nsum += 1; vsum += v*v
        apmax = max(apmax, d)
        crossed = hist[-1]*x < 0
        poached = abs(x) > rp
        if poached:
            switches += 1
        if crossed or poached:
            regen += 1; regs.append(t - t_last); t_last = t
            apos.append(apmax); apmax = 0.0
            if poached:
                hist = [0.0]; trp = 0
                continue
        hist.append(x)
        if len(hist) > 4000: hist = hist[-3000:]; trp = max(trp-1000, 0)
    return dict(d2=d2sum/max(nsum,1), vrms=np.sqrt(vsum/max(nsum,1)),
                Treg=np.mean(regs[2:]) if len(regs) > 5 else float('nan'),
                fsw=switches/max(regen,1), regen=regen)

def fixed_point(ds, dmul, T=6000, iters=9, seed=11):
    d2 = (ds/4.0)**2; Treg = 20.0; vrms = 1.0
    out = None; step = 1.0
    for it in range(iters):
        sigma_m = np.sqrt(dmul*2*C6*d2/3.0)/ds**3
        tau_c = max(1.0, min(Treg, ds/max(vrms, 1e-3)))
        out = episode(ds, sigma_m, tau_c, T, seed+it)
        if out['regen'] < 6:
            return dict(state='FROZEN', fsw=0.0, eta=0.0)
        d2new = 0.5*d2 + 0.5*out['d2']
        step = abs(d2new - d2)/max(d2, 1e-9)
        d2 = d2new
        Treg = out['Treg'] if np.isfinite(out['Treg']) else Treg
        vrms = max(out['vrms'], 1e-3)
    eta = d2/ds**2
    runaway = (out['fsw'] >= 0.5) or (step > 0.5) or (eta > 1.5)
    return dict(state='RUNAWAY' if runaway else 'FAITHFUL',
                fsw=out['fsw'], eta=eta, step=step)

SEEDS = (11, 23, 47)

def scan(dmul, label, grid):
    print(f"\n--- {label} (drive multiplier {dmul}) ---")
    print(f"{'d_s':>6} " + " ".join(f"{'seed'+str(s):>16}" for s in SEEDS) + "   verdict")
    verdicts = {}
    for ds in grid:
        cells = [fixed_point(ds, dmul, seed=s) for s in SEEDS]
        v = ("RUNAWAY" if any(c['state'] == 'RUNAWAY' for c in cells)
             else "FAITHFUL" if all(c['state'] == 'FAITHFUL' for c in cells)
             else "MIXED")
        verdicts[ds] = v
        cols = " ".join(f"{c['state'][:4]:>6} f{c['fsw']:.2f} e{min(c['eta'],9.99):4.2f}" for c in cells)
        print(f"{ds:6.2f} {cols}   {v}")
    lo = max([d for d, v in verdicts.items() if v == 'RUNAWAY'], default=None)
    hi = min([d for d, v in verdicts.items() if v == 'FAITHFUL' and (lo is None or d > lo)], default=None)
    if lo is not None and hi is not None:
        mid, half = (lo+hi)/2, (hi-lo)/2
        print(f"  BOUNDARY: last-RUNAWAY {lo:.2f} | first-clean-FAITHFUL {hi:.2f}  =>  d_s* = {mid:.2f} +/- {half:.2f}")
        return mid, half
    print("  BOUNDARY: bracket not closed on this grid")
    return None, None

grid_ref = (4.5, 5.0, 5.5, 5.75, 6.0, 6.25, 6.5, 6.75, 7.0, 7.5, 8.0)
ref_mid, ref_half = scan(1.0, "(A) E-register reference (3079 convention)", grid_ref)

grid_wv = (5.0, 5.5, 6.0, 6.25, 6.5, 6.75, 7.0, 7.25, 7.5, 8.0, 8.5)
wv_mid, wv_half = scan(2.0, "(B) WEAVE variant (two incoherent dipoles per site)", grid_wv)
if ref_mid and wv_mid:
    print(f"\n(B) shift check: measured x{wv_mid/ref_mid:.3f} vs drive^(1/6) prediction x{2**(1/6):.3f}")

print("\n(C) sixth-root robustness: d_s*(drive)")
pts = []
for dm in (0.5, 1.0, 2.0, 4.0):
    m, h = scan(dm, f"(C) drive x{dm}", (4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 9.0))
    if m: pts.append((dm, m))
if len(pts) >= 3:
    lx = np.log([p[0] for p in pts]); ly = np.log([p[1] for p in pts])
    slope = np.polyfit(lx, ly, 1)[0]
    print(f"\n(C) power-law fit: d_s* ~ drive^{slope:.3f}   [sixth-root class = 0.167]")
print("\nDone. Classification thresholds and grid declared above; the 3D")
print("arc-force confirmation cells are specified in the derivation note.")
