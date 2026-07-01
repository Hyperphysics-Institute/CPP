#!/usr/bin/env python3
"""
Patch 1839 -- DM consumes SF G1a (OPEN-SS-40): the cluster-floor verdict from the edge-bond ratio g.
====================================================================================================
SF-2/SF-5 returned G1a (handover 2026-06-30_dm_g1a..., OPEN-SS-40, patches 2200-2202): the scale-free
edge-bond ratio g = kappa_scissor/kappa_bend is VIABLE, direction corpus-pinned. Physical band
g_pond = 0.000-0.025 (screened/steep regime, guaranteed by electrostatics: no sub-Coulomb field +
derived fm-scale screening), vs g_crit = 6/N. This is the DM-side consumption -- plug g into the
per-fusion drop -> cluster floor. VERDICT REPORTED PER SF GUIDANCE: viable, DIRECTION ROBUST; the
EXACT floor (0.4 vs 0.8) is NOT pinned (needs the ZBW amplitude = OPEN-FP-SF-2-eta). No single sharp
floor quoted as pinned. No DM-1 promotion off Layer-C on the floor alone (G1b/G2/G3 still open).

Corrections carried from SF: (1) the g~0.1 estimate (1835/1836) had the right DIRECTION but the wrong
provenance -- it imported the founder's scissor-vs-E_qq-CORE (~66 MeV) softness read as the ratio,
whereas the floor-relevant denominator is the E_ee in-line BEND (same perimeter shell); the hierarchy
CANCELS in the true ratio, leaving pure geometry ~0.02, MORE comfortably viable. 1836's ratio-collapse
FRAMING is confirmed; the number improves. (2) 1834's Earnshaw retraction is VINDICATED: SF's 2200
static pass reversed to g~1.6-3.8 (tense) -- the static operator IS wrong here; 2201's ponderomotive
|E|^2-curvature (the calc 1835 named "mine to run") resolves Earnshaw and gives the viable g.
"""
import numpy as np

# --- SF-delivered (OPEN-SS-40); consumed, not recomputed ---
g_phys_lo, g_phys_hi = 0.000, 0.025     # ponderomotive, screened/steep (p>~3), corpus-guaranteed
def g_crit(N): return 6.0/N             # flexibility threshold (1830/1836): flexible iff g < 6/N

print("(1) g vs g_crit across the arm-length range (floor-setting arms N~14):")
for N in (8,14,28):
    gc=g_crit(N); margin=gc/max(g_phys_hi,1e-9)
    print(f"   N={N:3d}: g_crit={gc:.3f}  g_phys<=0.025  -> FLEXIBLE, margin ~{margin:.0f}x")
print("   => hinge flexible with LARGE margin (~17x at N=14) for the whole physical g band.")

# --- floor from the 1825 convolution: floor = sigma/m0(dwarf) * drop, drop in [1/8 flex, 1/2 rigid] ---
sm0_dwarf = 3.1
cluster_bound = 1.0    # sigma/m <~ 1 cm^2/g (cluster/Bullet)
print("\n(2) floor = sigma/m0(dwarf ~3.1) * drop  [1825 convolution]; g<<g_crit -> drop toward flexible end:")
for label,drop in [("flexible end (1/8)",1/8),("mid (1/4, 1825 central)",1/4),("rigid end (1/2)",1/2)]:
    fl=sm0_dwarf*drop
    print(f"   drop={drop:.3f} [{label:24s}] -> floor ~{fl:.2f} cm^2/g  {'<= bound VIABLE' if fl<=cluster_bound else '> bound'}")
print(f"   g~0.02 (<<g_crit, 17x margin) selects the FLEXIBLE end -> floor lands in ~0.4-0.8 band.")
print(f"   The ENTIRE viable band (0.4-0.8) is <= the cluster bound {cluster_bound} -> VIABLE wherever it lands.")

print("\n(3) self-limiting (1826) re-confirmed by g<<g_crit:")
print("   free-hinge inertial decoupling (1831) is now corpus-backed -> per-fusion N/2 backing -> v_thr rises")
print("   -> fusion stalls at the floor (stable fixed point, 1825/1826); NO runaway to the ~0.07 over-depletion")
print("   fixed point (that needed a RIGID whole-X 2N backing, which g<<g_crit excludes).")

print("\n(4) stiff-vs-soft consistency (SF 2202, carry to panel):")
print("   sigma/m ~ 0.11*N needs a STIFF ribbon (large kappa_bend, ell_p~100-700 fm; 0860-0862).")
print("   g is a RATIO -> large kappa_bend is the DENOMINATOR that makes g small. The two DM requirements")
print("   REINFORCE. g~0.02 with kappa_bend large => kappa_scissor ~ kappa_bend/50: the junction is the")
print("   SOFTER OF TWO STIFF MODES, not a fragile joint -> 'flexible X' does NOT smuggle in 'fragile candidate'.")

print("\nVERDICT (DM cluster floor): VIABLE, DIRECTION ROBUST (corpus-pinned via SF 2200->2201->2202).")
print("Floor lands in ~0.4-0.8 cm^2/g, below the cluster bound ~1.0 across the whole band. EXACT floor")
print("(0.4 vs 0.8) PENDING the ZBW amplitude (OPEN-FP-SF-2-eta). Self-limiting secured; no over-depletion.")
print("NOT a DM-1 promotion: G1b (ell_p absolute), G2 (E_qq/E_ee), G3 (glueball-arrest, OPEN-SS-39) still open.")
