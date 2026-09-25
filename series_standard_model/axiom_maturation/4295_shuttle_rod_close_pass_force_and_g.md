# The Shuttle Rod Holds on Charge Alone: Close Passes Pull Hard; g = 2 at a 9.5% Overshoot; What Sets the Overshoot Is Open

**Patch:** 4295. **Lane:** EW → QM/SPIN. **Session:** 240.
**Founder:** `founders_voice/4295_ruling_dual_zbw_spinning_rod_plus_shuttle.md`. The electron is a spinning rod: two −eCP
poles, and a +eCP shuttling through each pole to just outside it and back, fast, holding the poles together.
**Verify:** `series_standard_model/code/4295_shuttle_rod.py`.
**Corrects:** 4294 §3 and §6. "Charge cannot hold" was specific to 4293's neutral-hub dumbbell; see the erratum there.

## 1. Close passes pull hard (rows 1)

The +eCP moves at one PSR per Moment, so its time is spread evenly along its track, from −L to L with L = d + s (s is its
overshoot beyond each pole). Its pull on a pole is enormous whenever it is near the pole. The part while it is inside and
the part while it is outside nearly cancel, and what survives is:

  inward pull = k e² (1/2L)(1/s − 1/(2d + s)), less the other pole's push k e²/(2d)².

```
  s = 0.300 d: numeric (softened) inward    0.865   formula    0.865   vs a plain Coulomb pull at d: 1.000 (+ the push)
  s = 0.095 d: numeric (softened) inward    4.339   formula    4.339   vs a plain Coulomb pull at d: 1.000 (+ the push)
  s = 0.010 d: numeric (softened) inward   49.005   formula   49.009   vs a plain Coulomb pull at d: 1.000 (+ the push)
```

**A small overshoot multiplies the pull by about d/2s.** This is the founder's "dropping enough +eCP DI-bits to keep both
−eCPs close": the +eCP spends its time right next to the poles, where charge is strong. (A first run of this row used a
1/r kernel by mistake; corrected before any conclusion was drawn.)

## 2. The magnet (rows 2)

```
  s = 0.0000 d:  f = 0.1429  g = 2.1429
  s = 0.0500 d:  f = 0.1552  g = 2.0686
  s = 0.0954 d:  f = 0.1667  g = 2.0000
  s = 0.2000 d:  f = 0.1935  g = 1.8387
  g = 2 at s = (sqrt(1.2) - 1) d = 0.0954 d  (overshoot 9.5%);  no overshoot gives g = 15/7 = 2.1429
```

With the +eCP spread evenly along its track, its share of the spin is ⟨r²⟩/(2d² + ⟨r²⟩). g = 2 needs the share 1/6
(4292), which the shuttle gives at an **overshoot of 9.5% of the half-length**. With no overshoot, g = 15/7.

## 3. The rod's size, from the balance of forces and spin ħ/2 (rows 3)

```
  d = 4.136 r_C (half-length), rod 8.27 r_C;  poles at 0.1511 c
  shuttle cycles per rotation = 9.5;  pole kinetic energy 0.0076 m_e c^2;  Coulomb energy ~ 0.0018 m_e c^2  (small: m_e = 3m holds to < 1%)
  with no overshoot allowance but the same force law, plain Coulomb at distance d (K = 0.75) would balance at
  d = 25.2 r_C: a symmetric rod needs far less than 4294's dumbbell (154 r_C).
```

**At the g = 2 overshoot the rod holds on charge alone.** Its half-length is 4.1 Compton lengths, the poles move at
0.15c, and the +eCP makes about 9.5 round trips per turn of the rod. The energies are small, so the equal-thirds
accounting of 4292 holds here, unlike 4294's ZBW-strength bond, which stored half the rest energy.

## 4. Correction to 4294

4294 concluded that charge cannot hold the electron's spinning structure at any size where the spin is carried below
light speed, except at the Bohr scale. That was true of 4293's geometry, a neutral locked hub whose only hold on the rim
is its faint polarisation. It is **not** true of the founder's rod. The symmetric geometry needs less force, and the close
passes supply more. 4294's arithmetic that charge at a Compton length is α times the Compton-scale force still stands. So
does its point that the ZBW itself, at the Compton frequency with a Compton-length amplitude, needs more than distant
charge supplies. Close passes are one way that "more" can arise from charge itself.

## 5. The open question: what sets the overshoot? (rows 4)

```
  d = 3.93e-11 r_C, pole speed 1.64e+10 c  -> far faster than light: an overshoot of one PSR binds far too hard.
```

If the +eCP turned back one PSR after passing a pole, the pull would be so strong that the rod would collapse to a tiny
size, and the spin ħ/2 would need poles faster than light. So **the +eCP must carry on about a tenth of the half-length
(≈ 0.4 r_C) past each pole before turning back.** A CP that always steps toward its SSV-net would turn back at once,
because the pull reverses the moment it passes the pole. Carrying on requires the +eCP to keep its heading for a while:
its inertia, the DP-arcs it has made (founder 4288). But inertia also means its speed varies along the track, which
changes both the pull and the spin share. That self-consistent shuttle is the next computation. 4292 tested only the
+eCP at rest in the middle (unstable at a 10⁻⁴ nudge); a shuttle through the poles was never tested there.

## 6. What I think

The founder's rod is the best picture yet. It uses charge only, it answers his own objection to 4293 (the +eCP keeps
returning before the poles can separate), and it can give the spin, the magnet and small binding energies at a physical
size with the poles well below light speed. Everything now hangs on one physical quantity: **how far the +eCP carries on
past a pole before turning back.** About 9.5% of the half-length gives g = 2 and fixes the rod's size.

## 7. Founder question (a physical picture)

**When the +eCP passes through a −eCP pole and comes out the far side, what makes it turn back, and how far out does it
go first?** Does it keep its heading for a while (its DP-arcs carrying it on), or does it turn back at once?

## 8. PD-008

- **Convenient branch, marked.** "g = 2 at a 9.5% overshoot" is a single overshoot tuned to a single number. It becomes a
  result only if the overshoot is derived.
- **My error, stated.** 4294's broad claim went beyond its computation; it is corrected here.
- **Assumptions.** The +eCP moves at uniform speed (founder's one PSR per Moment); equal inertia m_e/3 each, which sits
  uneasily with a +eCP moving at c when SF-6's inertia is m₀γ (flagged); planar; the poles' own ZBW is ignored.
- **Reading of "one PSR per Moment".** Taken as speed c. If each leg took one Moment, the rod would be about a PSR long,
  which cannot carry ħ/2 (§5).
