#!/usr/bin/env python3
"""4250 -- TODO-4192-COHERENT: critic on 4192's exclusion of mixing at eps = a/r by coherently polarised sources.
Attacks 4192 s5's three points and the one reading that could void the test."""
import math
l_P,t_P=1.616e-35,5.391e-44; a=l_P/1e30
n_Fe=7.87e3/55.85e-3*6.022e23; s_Fe=2.2*n_Fe
caps={'ferro':(1.1e-45,0.5),'g2':(5.4e-47,0.01)}
rows=[('nuclear spin in a 5 mm iron domain-ball', a*2*math.pi*s_Fe*(5e-3)**2,'ferro'),
      ('1 g magnetised iron at 1 m', a*(1e-3/7.87e3*s_Fe)/1.0,'g2'),
      ('g-2 yoke, 680 t at 1 m, 99.9% cancelled', 1e-3*a*(6.8e5/7.87e3*s_Fe)/1.0,'g2')]
print("suppression the mixing needs to survive each row (pull/cap), against what each critic point can supply:")
for name,pull,c in rows:
    e,P=caps[c]; print(f"  {name:44s} needs 1/{pull/(e*P):.1e}")
print("  (i)  self-term weight w (own : received): pull scales 1/w; the founder's loop (4182) mixes own and received on equal")
print("       footing per Moment and carries the result -- w = O(1); no statement gives 1e6-1e12.")
print("  (ii) one unit per unpaired electron: iron carries 2.2 mu_B per atom; the count could be off by <= 2.2 either way.")
print("  (iii) 4170's tolerances: caps set at the order of the measured limits; an order of magnitude at most.")
print("  -> the three points supply <= O(10); the gap is 1e6-1e12. 4192 STANDS on the founder's reading.")
print("\nthe one reading that would void it: the environment's content does NOT stay with the CP (own A reasserts each Moment).")
tilt=a*(1e-3/7.87e3*s_Fe)/1.0
print(f"  then mixing is a per-Moment dressing of size ~{tilt:.1e} rad (1 g iron at 1 m), never accumulating: harmless -- and inert.")
print("  4182's ruling is the accumulating reading (the CP 'hops carrying' the mixed spin). Under EITHER reading mixing cannot")
print("  organise an electron (tilt 1e-43 per Moment vs O(1) needed): 4192's physics conclusion is reading-independent;")
print("  only whether A3' needs a by-hand suppression (accumulating) or is merely inert (non-accumulating) depends on it.")
print("\nfalloff: 1/r is grounded by GR-1j's Laplacian statics (4186); a 1/r^2 count-dilution reading would multiply every pull by a/r ~ 1e-65 and")
print("  void the exclusion -- but 4186 rules it out for a relayed static-snapshot payload. Recorded as the lever, not adopted.")
