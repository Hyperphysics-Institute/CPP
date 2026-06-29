#!/usr/bin/env python3
"""
Patch 1818 -- the bending fork (calc #2 of the collisional program, 1815 sec5; selected by the 1816 v_pen gate).
==============================================================================================================
v_pen (1816) showed the eCP coat HOLDS dwarf->cluster, so the operative regime is BENDING: a long Cross-Rod
struck transversely at mid-length (Thomas's "two rods collide mid-length, opposite directions, 90 deg") is a
three-point bending impact. Two thresholds, both from pinned quantities + ONE O(1) energy-focusing factor g:

 (A) v_init(N) -- BENDING-FRACTURE INITIATION. The outer-fiber E_ee shell bonds (largest lever arm from the
     neutral axis) reach breaking first while the E_qq core sits near the neutral axis -- which is WHY E_ee
     governs the bend threshold though E_qq is stronger. The whole-rod transverse collision energy
     (1/2)(N m_el/2) v^2 focuses into bending at the impact section; fracture initiates when it reaches the
     outer-fiber breaking energy ~ g*E_ee:
         v_init(N) = 2 sqrt( g * E_ee / (N m_element) )      ->   ~1/sqrt(N): LONG RODS BREAK EASIER.

 (B) v_through(N) -- CRACK PROPAGATION vs ARREST. Once the outer crack initiates, does it run THROUGH the
     E_qq core (clean fragmentation, mode 1) or ARREST at the ~73x tougher core boundary (shell-stripping,
     mode 2)? Running through must supply the core cut energy ~ n_w^2 * E_qq:
         v_through(N) = 2 n_w sqrt( E_qq / (N m_element) ),    v_through/v_init = n_w sqrt(E_qq/(g E_ee)).

All pinned: E_ee=0.9 (1813), E_qq=66 (1812), m_element=4qDP+4eDP=1408 (0886), n_w~2-4 (w~2fm, 0860). g~O(1).
"""
import numpy as np
c = 299792.458
E_ee, E_qq, m_el = 0.9, 66.0, 1408.0          # MeV (pinned)
def v_init(N, g=1.0):     return 2*np.sqrt(g*E_ee/(N*m_el))*c
def v_through(N, n_w=3):  return 2*n_w*np.sqrt(E_qq/(N*m_el))*c
DWARF, CLUSTER, BULLET = 60, 2000, 4000

print("="*74)
print("The bending fork: v_init (shell crack initiates) and v_through (crack cuts core)")
print("="*74)
print(f"  pinned: E_ee={E_ee} E_qq={E_qq} MeV (toughness ratio {E_qq/E_ee:.0f}x)  m_element={m_el:.0f} MeV")
print(f"  v_through/v_init = n_w*sqrt(E_qq/(g E_ee)) = {3*np.sqrt(E_qq/E_ee):.0f}x (n_w=3,g=1) -- robustly >> 1\n")
print(f"  {'N':>4} | {'v_init [km/s]':>13} | {'v_through [km/s]':>16} | regime @ dwarf/cluster/Bullet")
for N in (5,10,20,30,60,100,300):
    vi, vt = v_init(N), v_through(N)
    def reg(v): return "core" if v<vi else ("strip" if v<vt else "FRAG")
    print(f"  {N:>4} | {vi:>13.0f} | {vt:>16.0f} | {reg(DWARF):>5}/{reg(CLUSTER):>5}/{reg(BULLET):>5}")

print("\n  g-sensitivity of v_init (the one O(1) knob; v_init ~ sqrt(g)):  N=30")
for g in (0.1,1.0,10.0):
    print(f"    g={g:>4} -> v_init(30) = {v_init(30,g):6.0f} km/s")

print("\n" + "="*74)
print("THE SCISSION-MODE-vs-VELOCITY CURVE (first piece):")
print(f"  v < v_init(N) ~ {v_init(60):.0f}-{v_init(10):.0f} km/s  : ELASTIC / cores. Dwarfs ({DWARF}) here for ALL N.")
print(f"  v_init < v < v_through                       : SHELL-STRIPPING / crack-arrest (mode 2),")
print(f"                                                 number-conserving damage. CLUSTERS sit HERE")
print(f"                                                 (N>~30 strip at ~2000-4000 km/s).")
print(f"  v > v_through ~ {v_through(30):.0f} km/s (N=30)         : clean FRAGMENTATION (mode 1) -- NEVER")
print(f"                                                 reached in DM halos (>> cluster).")
print("="*74)
print("FINDINGS:")
print(" 1. v_init(N) ~ 1/sqrt(N) lands in the cluster band and FAR above dwarf -> reproduces the")
print("    dwarf-cores / cluster-active split mechanistically (Thomas's 'long rods break easier').")
print(" 2. But CLEAN fragmentation (cutting the E_qq core) needs ~10^5 km/s -- the 73x toughness jump")
print("    means the crack ARRESTS at the core at ALL DM velocities. The operative cluster mode is")
print("    SHELL-STRIPPING (mode 2), NOT clean bisection (mode 1).")
print(" 3. => REVISES the DM-1 v1.0 mechanism: 'fragments in two at clusters' -> 'sheds outer shell")
print("    at clusters'. BOTH give sigma/m falling with v (SIDM-preferred), but the mechanism and the")
print("    quantitative sigma/m(v) differ. FLAG for DM-1 (founder-gated); do NOT fold unilaterally.")
print(" 4. Eventual true fragmentation must come from ACCUMULATED shell damage / glueball weak-points")
print("    (mode 4) over many collisions -- the next question.")
print("="*74)
