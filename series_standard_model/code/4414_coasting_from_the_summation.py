"""Patch 4414 -- founder (on 4413): no speedometer and no pushing; the CP computes its displacement from the DI-bit
summation at each GP it lands on -- the rear displacement signal minus the front one -- and moves that amount each Moment.

Question: under that rule, do the CP's own returns give a step of exactly v at every speed?

Model (consistent geometry, after the critic's HOLD on the first draft): the CP moves at v along +x; at t = 0 it sits on
its landing GP at the origin.  It emitted DI-bits at earlier times t_e from (v t_e, 0, 0).  Reflectors at rest, spread
evenly in space, re-emit what reaches them evenly in all directions.  A return from reflector P arrives at the origin at
t = 0 only if P was reached at t = -|P|, i.e. from the emission time solving |P - v t_e x| = -|P| - t_e.  Its weight:
  emission density in the direction from the emission point to P  (U: even in the absolute frame -- the registered case,
                                                                   AP-4 / R-DIBIT / 4409;  H: 'headlight', even in the
                                                                   CP's own frame, for contrast)
  x 1/re^2 (spreading from the emission point)  x 1/(1 - v n_e.x) (arrival-rate compression at P)  x 1/|P|^2 (spreading
  back to the origin).  Each return arrives FROM the direction of P.
Ratio: projected net (vector sum of arrival directions along x, rear counted positive) / total -- the SSV_net component
over SSV_abs.  (A raw hemisphere count, rear minus front, is shown for contrast.)
"""
import numpy as np
rng = np.random.default_rng(3)

def ratio(v, emit='U', shell=(1.0, 2.0), n=2_000_000):
    u = rng.random(n); r = (shell[0]**3 + u*(shell[1]**3 - shell[0]**3))**(1/3)
    mu = rng.uniform(-1, 1, n); ph = rng.uniform(0, 2*np.pi, n); s = np.sqrt(1 - mu*mu)
    Px, Py, Pz = r*mu, r*s*np.cos(ph), r*s*np.sin(ph)
    te = (2*Px*v + 2*r)/(v*v - 1)            # nonzero root of (Px - v te)^2 + rho^2 = (r + te)^2
    Ex = Px - v*te; re = np.sqrt(Ex**2 + Py**2 + Pz**2); nex = Ex/re
    g2 = 1/(1 - v*v)
    dens = np.ones(n) if emit in ('U', 'count') else 1/(g2*(1 - v*nex)**2)
    w = dens/(re*re)/(1 - v*nex)/(r*r)
    from_x = Px/r                              # direction the return comes FROM
    rear_minus_front = -(w*from_x).sum()       # projected vector sum, rear counted positive
    if emit == 'count':
        return (w*(from_x < 0)).sum()/w.sum() - (w*(from_x > 0)).sum()/w.sum()
    return rear_minus_front/w.sum()

print("Part 1: projected net / total, the CP's own returns counted at its landing GP (Monte Carlo, ~+-0.001)")
print("   v      (U) even in the absolute frame (registered)    (H) headlight")
for v in (0.01, 0.1, 0.3, 0.5, 0.9):
    print(f"  {v:5}         {ratio(v, 'U'):+.4f}                              {ratio(v, 'H'):+.4f}")
print("  (U): equal to v within sampling noise, the excess arriving from BEHIND; with his rule (rear signal minus front signal) the step is")
print("       forward and equal to v -- coasting at every speed, for every kind of particle, never reaching c.")
print("  (H): about v/3 -- falls short (the first draft had these two the wrong way round).")
print("  check a different shell (U, v = 0.5):", round(ratio(0.5, 'U', (5.0, 9.0)), 4))
print("  raw hemisphere count (rear - front)/all, (U):", ", ".join(f"v={v}: {ratio(v, 'count'):.3f}" for v in (0.1, 0.5)),
      "-> about 1.5 v: on that reading the CP would speed up")
# exact quadrature for a fixed reflector distance (the critic's method)
from scipy.integrate import quad
def exact(v):
    def w1(mp):
        T = 2*(1 + v*mp)/(1 - v*v); re = T - 1; me = (mp + v*T)/re
        return 1/(1 - v*me)/re**2
    return -quad(lambda m: m*w1(m), -1, 1)[0]/quad(w1, -1, 1)[0]
print("  exact quadrature (fixed reflector distance):", ", ".join(f"v={v}: {exact(v):.10f}" for v in (0.01, 0.1, 0.5, 0.9)))

print("\nPart 2: the dilution obstacle -- outside DI-bits add to SSV_abs but not to SSV_net")
for s in (1.0, 0.99, 0.5, 1e-3):
    v = 0.5; vs = []
    for k in range(5):
        v = s*v; vs.append(v)
    print(f"  self share s = {s:6}: speed after 1..5 Moments " + ", ".join(f"{x:.4g}" for x in vs))
print("  -> unless the self-returns are compared only with each other (s = 1 exactly), a free CP slows, and slows more")
print("     where the outside count is higher (near masses, other charges): a breach of the first law.")
