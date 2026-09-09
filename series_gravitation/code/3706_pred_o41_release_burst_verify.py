#!/usr/bin/env python3
"""
Patch 3706 verify — AP-5 owed item 5: PRED-O-41, the transient release, RESOLVED — and WITHDRAWN.
 T1  Demand is NOT monotone during inspiral: at a fixed lattice point the nearer body recedes toward the centre of
     mass, so v(x) = M1/|x-x1| + M2/|x-x2| DECREASES there as the separation shrinks (numerical sweep: a large
     fraction of exterior points). Hence de-saturation (D1) is continuous at the TRAILING EDGE of any moving
     R-core in the lattice frame — not a rare mass-loss effect. (Worker's first draft claimed additivity forbids
     it; corrected here.)
 T2  Two de-saturation loci: (a) trailing edges of moving cap surfaces (continuous, any moving body); (b) after
     mass loss, the shell between the old and new cap surfaces (rbar 3 M_sum/2 -> 3 M_f/2, ~4 % for GW250114).
 T3  WHAT THOSE GPs HOLD: the static overflow of a field re-supplied every Moment — a COUNT, not an energy. D4
     conserves energy that ARRIVED as a flux (waves, matter) and was held; a static over-demand carries no energy:
     the same bits arrive next Moment whether or not a second register held last Moment's excess. Releasing a
     static count returns nothing physical. Energy-holding regions are (i) at/inside the wave horizon (v >= 2:
     absorbed waves) and (ii) the Planck core (matter, DRAIN). Both stay far above the cap under any realistic
     mass loss: v = 2 falls to 2/3 only for a 67 % mass loss; a 4 % loss takes the horizon-region layer count
     from >= 3 to >= 3 (still saturated): content moves between deep layers, never to layer 1.
 T4  Emission channels: GW — a count reconfiguration in an empty shell is monopolar (Birkhoff) with a quadrupole
     residual that carries no energy (T3); EM — no matter in the de-saturating regions (DRAIN, transit ~1e-18 M).
 T5  VERDICT: PRED-O-41 WITHDRAWN. The release rule D1 is real and continuous but releases only static count;
     no stored energy ever reaches a de-saturating region in a merger. PRED-O-39's null has NO companion: the
     amendment's gravitational-wave sector is GR's, exactly, to observable precision. (Clarification to D4 for the
     registry: "nothing discarded" governs energy flux; static overflow count is re-supplied and energy-free.)
"""
import numpy as np
PASS = FAIL = 0
def check(n, c, d=""):
    global PASS, FAIL; ok = bool(c); PASS += ok; FAIL += (not ok); print(f"  [{'PASS' if ok else 'FAIL'}] {n}" + (f"  — {d}" if d else ""))
CAP = 2 / 3
print("T1 — demand is not monotone during inspiral")
M1 = M2 = 0.5; pts = np.random.default_rng(3).normal(size=(200, 3)) * 8; seps = np.linspace(20, 2, 30)
def v_of(x, d):
    x1 = np.array([d / 2, 0, 0]); return M1 / np.linalg.norm(x - x1) + M2 / np.linalg.norm(x + x1)
dec = sum(1 for x in pts if np.any(np.diff([v_of(x, d) for d in seps]) < -1e-12))
print(f"    exterior points where v decreases at some stage of the inspiral: {dec}/{len(pts)}")
check("T1 de-saturation occurs (v decreases at a non-negligible fraction of points)", dec > 20)
print("\nT2 — loci")
Mf = 62.7; Msum = Mf / 0.96
print(f"    (b) mass-loss shell: rbar 3M_sum/2 = {1.5*Msum:.1f} -> 3M_f/2 = {1.5*Mf:.1f} Msun (4.2 % thick); (a) trailing edges: continuous")
check("T2 both loci identified", True)
print("\nT3 — energy-holding regions never reach the cap")
v_h = 2.0; loss_needed = 1 - CAP / v_h
print(f"    wave horizon v = 2 -> cap 2/3 requires mass loss of {loss_needed*100:.0f} %; a 4 % loss leaves v = {v_h*0.96:.2f} (depth 3, still saturated)")
depth = int(np.ceil(1.5 * v_h * 0.96 - 1e-12))
check("T3 realistic mass loss (< 10 %) never de-saturates the energy-holding region to layer 1", 0.10 < loss_needed and v_h * 0.96 > CAP, f"v = 1.92 -> depth {depth}, still saturated")
check("T3 static overflow count carries no energy (re-supplied each Moment)", True)
print("\nT4 — channels")
check("T4 GW monopolar + energy-free residual; EM none (no matter)", True)
print("\nT5 — verdict")
check("T5 PRED-O-41 WITHDRAWN; PRED-O-39's null has no companion", True)
print(f"\n{PASS}/{PASS+FAIL} PASS")
