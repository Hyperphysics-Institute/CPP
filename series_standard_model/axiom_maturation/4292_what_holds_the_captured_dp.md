# What Works Is Fixed by What Holds the Captured Dipole, and Coulomb Forces Between Three Point CPs Do Not Hold It

**Patch:** 4292. **Lane:** EW → QM/SPIN. **Session:** 240.
**Founder:** `founders_voice/4292_delegation_compute_what_works_outer_shape_open.md`. He delegates the computation: find
the rate (and the outer orbit's shape) that makes inertia, spin and magnet come out right.
**Verify:** `series_standard_model/code/4292_what_holds_the_captured_dp.py`.

## 1. The target (rows A)

**Default, flagged as an assumption:** the three CPs (core −eCP, inner +eCP, outer −eCP) carry equal moving inertia, since
CPs are identical but for charge. At these speeds binding is negligible, so each carries m_e/3. Then:

  **g = 3 (1 − 2f),  f = L_inner / S**, about the centre of mass.

```
(A) g = 3(1 - 2f):  f=0.0000->g=3.000  f=0.1667->g=2.000  f=0.2500->g=1.500  f=0.5000->g=0.000
    g = 2 needs the inner +eCP to carry exactly 1/6 of the electron's spin; the two -eCPs carry 5/6.
```

**This is what "works" means**, independent of orbit shape: the +eCP carries one-sixth of the spin. If it carries none,
g = 3. If it carries half, the magnet vanishes.

## 2. In the rose picture (rows B)

With the core held still and the inner's swing sinusoidal (4291):

```
(B) static core, m_o = m_i = m_e/3: g = 3(1-x/2)/(1+x/2);  g = 2 at x = 0.4:  g = 2.0000,  f = (x/2)/(1+x/2) = 0.1667
    meeting the partner at each tip (W = w_o - w_r): w_r = 0.6 w_o -> 1.2 touches per outer revolution (6 touches per 5 circuits)
```

**The inner's line turns at 0.4 of the outer's rate.** If it meets its partner at each touch, it swings out 6 times in
every 5 circuits. This answers the question the founder handed over, *given* the circle, the equal inertias and the
still core.

## 3. But the three point CPs do not stay together (rows C)

Before trusting §2, the dynamics must actually produce such an orbit. Planar, pass-through-softened Coulomb forces,
equal inertias:

```
    54 bound-energy starts: 54 break up within t = 60 into a neutral (+,-) pair and a free -eCP  {'inner stays with core': 33, 'inner stays with outer': 21}
    Euler line (-,+,-) rotating rigidly at d = 0.5, +e in the middle, nudged by delta:
      delta = 0e+00: largest separation    1.01  (holds)
      delta = 1e-04: largest separation  123.68  (breaks up)
      delta = 1e-02: largest separation  126.03  (breaks up)
```

Every start with negative energy breaks up the same way. The +eCP pairs off with one −eCP into a neutral dipole, and the
other −eCP leaves. Sometimes the captured DP departs (21); sometimes the core keeps the +eCP and the former outer −eCP
departs (33). Even the perfectly symmetric rotating line survives only while exact.

**The reason is structural.** Seen from the outer −eCP, the core plus the inner +eCP is neutral. Nothing holds the outer
except the inner's excursions toward it, and the three-body motion is chaotic enough that the pair reshuffles. Known
physics has the same result: the positronium negative ion (e⁻e⁺e⁻) is not bound classically; it is bound only quantum
mechanically. And with equal inertias, Coulomb dynamics cannot even tell the "core" from the "outer" −eCP: they are
interchangeable.

**So Coulomb forces between the three point CPs select no rate and no outer shape, because they hold no orbit.** The
captured DP is held by something else. The rate and the shape are set by *that*.

## 4. What holds it: candidates already in the corpus

- **The core's polarization cloud (c04 / SF-6 DP-sea polarization).** The core −eCP is surrounded by a compressive
  polarization cloud of radius r_th. SPIN-2 already tried to anchor the pair to the cloud's standing wave, with the right
  instinct, but at the wrong scale (4289).
- **The pass-through ZBW lock (4265).** The inner +eCP's swing through the core is the core's own ZBW partner-oscillation,
  a resonant bond rather than a free Coulomb fall. That would make the inner +eCP the core's ZBW partner, and the
  "captured DP" the core's own oscillator, not a separate guest.
- **The lattice's minimum action (founder 4288/4290).** The spin ħ/2 is still input (4289). Whatever quantises it may be
  what binds: in quantum physics, Ps⁻ is bound exactly by quantisation.

## 5. What I think

The rate that works is known: the +eCP carries one-sixth of the spin, which on a circle is the inner's line turning at
0.4 of the outer's rate. What makes that motion *physical* is not yet on file. Point-CP Coulomb dynamics cannot provide
it, so the shape of the outer orbit is not a free choice to fit. It is an output of whichever binding holds the pair.
The next derivation is a binding model. I will start from the pass-through ZBW lock (§4, second bullet), because it
already carries route (H)'s radius and frequency (4266, 4272) and it is the one mechanism that distinguishes the core
from the outer −eCP.

## 6. PD-008

- **Convenient branch, marked.** §2's "0.4 the outer's rate" is a clean answer to what was asked. I am not reporting it as
  the answer, because §3 shows no Coulomb orbit realises it. It is the target, not a result.
- **Pitfall recorded (D-4).** The first scan started the inner on the core. With equal inertias the initial spin share is
  then exactly f = 1/6 by construction, and every run printed g ≈ 2 while flying apart. That was an artefact; only bound
  runs count.
- **Assumptions, stated.** Equal inertias; negligible binding; planar motion; a softening of 0.02 for pass-through; runs of
  t = 60. The breakup is consistent with the classical instability of e⁻e⁺e⁻; a 3-D run, other softenings and longer
  runs are cheap checks, filed.
