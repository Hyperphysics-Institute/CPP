"""Patch 4455 -- founder asks whether the internal DP vibrations can propagate, reflect and make a standing wave matching the photon's
wavelength and frequency.  Claude's construction: a relayed chain, not a reflected standing wave.

Part 1. KINEMATICS (a travelling wave by construction): a chain of DPs, all oscillating at one common rate f (assumed), each started
        when a dispersion-free relay at the local light speed c reaches it: crests spaced c/f (c/(K f) in a region of index K).  The relay
        sets the phase offset, not the rate; the shared rate f is the unsolved collective mode (4454 item c).
Part 2. CONSISTENCY CHECK: an observer approaching at v meets the crests more often by (1 + v/c)/sqrt(1 - v^2/c^2); the photon's energy rises
        by the same factor by relativity (null four-momentum), so E/f stays h.  A hypothetical 'ringing cohort as clock' (4454) would slow.
Part 3. Rate vs energy.  (a) Under a simple kinetic model Claude chose (fixed volume, fixed movers, f ~ u, E ~ u^2): f ~ sqrt(E).
        (b) A fixed action per cycle (energy x period = h) is Planck's E = h f rewritten: it wins by definition, not as a test.
"""
import numpy as np
c = 1.0
for f in (1.0, 2.0):
    x = np.linspace(0, 10, 4001)                    # positions along the chain
    t = 20.0
    disp = np.where(t > x/c, np.sin(2*np.pi*f*(t - x/c)), 0.0)
    crests = x[1:-1][(disp[1:-1] > disp[:-2]) & (disp[1:-1] > disp[2:]) & (disp[1:-1] > 0.99)]
    print(f"Part 1  rate f = {f}: crest spacing {np.mean(np.diff(crests)):.4f} (c/f = {c/f:.4f})")
for v in (0.1, 0.5):
    D = (1 + v)/np.sqrt(1 - v**2)
    print(f"Part 2  observer approaching at {v}c: crests met {D:.3f} x as often; energy (relativity) x {D:.3f}; hypothetical carried clock x {np.sqrt(1 - v**2):.3f}")
for k in (2, 4):
    print(f"Part 3  energy x {k}: simple kinetic model -> rate x {np.sqrt(k):.2f};  Planck (fixed action per cycle, by definition) -> rate x {k:.2f}")
