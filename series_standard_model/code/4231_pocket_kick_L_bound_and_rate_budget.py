#!/usr/bin/env python3
"""4231 -- two consequences of the founder's binding/release statement, computed.
Binding: electrostatic, through the ZBW oscillation of the eDP's -eCP pole between the +qCP core (superposition,
zero-gradient reset Moment) and the outer orbit. Release: the -eCP pole transits the W0 centroid's zero-gradient
pocket, is reset there, and the strongest gradient present redirects it; the +eCP pole follows.
(1) Angular momentum about the core: a kick delivered while the pole is inside the pocket has a lever arm about
    the pole's position of at most the pocket radius; with a kick of order the pole's own momentum, the fractional
    change of L about the core is bounded by r_pocket / r_orbit.
(2) Rate budget: the neutron lifetime in ZBW cycles, and the per-cycle probability the mechanism must deliver as
    (W0 present at the orbit, aligned) x (pole in pocket) x (reset redirects outward)."""
import math
hbarc = 197.327; m_const = 313.0; m_W = 80379.0
r_orb = hbarc/m_const; r_pk = hbarc/m_W
dL_over_L = r_pk/r_orb
print(f"r_orbit = {r_orb:.3f} fm   r_pocket = {r_pk:.4f} fm   max |dL|/L from any kick inside the pocket = {dL_over_L:.2e}  (~{100*dL_over_L:.1f}%)")
print("   -> the released eDP leaves with the orbital's angular momentum to better than 1%: the vertex's B = +1 is what")
print("      this mechanism gives, not an extra assumption. A kick from a pocket 250x smaller than the orbit cannot")
print("      change L about the core; it can only change the RADIUS the pole goes to next.")
hbar_MeVs = 6.582e-22
f = m_const/hbar_MeVs/(2*math.pi)     # ZBW cycle frequency scale, mc^2/(2 pi hbar)
tau = 878.4
N = f*tau
hit = (2*r_pk)/(2*math.pi*r_orb)      # pocket on the orbit circle, in plane
print(f"\nZBW cycle frequency ~ mc^2/(2 pi hbar) = {f:.2e} /s;  cycles per neutron lifetime = {N:.2e};  per-cycle decay probability = {1/N:.2e}")
print(f"pole-in-pocket fraction per cycle (pocket on the orbit circle, in plane): {hit:.2e}")
print(f"=> (W0 present at the orbit, aligned) x (reset redirects outward) must be ~ {1/N/hit:.1e} per cycle")
print(f"   a virtual W0's own duration hbar/(m_W c^2) = {hbar_MeVs/m_W:.1e} s = {hbar_MeVs/m_W*f:.1e} ZBW cycles")
