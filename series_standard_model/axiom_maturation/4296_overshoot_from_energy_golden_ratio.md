# The Pull of the Passed Pole Fixes the Overshoot at the Golden Ratio; g = 2 Needs a Finely Set Energy; Under Newton-Plus-Coulomb the Spinning Rod Breaks Up

**Patch:** 4296. **Lane:** EW → QM/SPIN. **Session:** 240.
**Founder:** `founders_voice/4296_ruling_pole_it_passed_pulls_plus_back.md`. What turns the +eCP back beyond a pole is the
pull of the pole it just passed through.
**Verify:** `series_standard_model/code/4296_inertial_shuttle.py`.
**Corrects:** 4295 (its uniform-speed picture, and "holds on charge alone"; see the erratum there).

## 1. The overshoot is fixed by energy (rows A)

If the passed pole's pull turns the +eCP back, and the +eCP has inertia, then it climbs out on the far side until it has
given back all the speed it gained falling in. Nothing is free to choose. The shuttle crosses the middle only if its
energy exceeds the crossing threshold (the middle is a hump between the two poles). Just above that threshold:

  **overshoot s = (√5 − 1)/2 · d = 0.618 d, the golden ratio.**

This replaces 4295's 9.5%, which assumed uniform speed. With inertia the +eCP flashes past the poles and lingers at its
turning points and on the central hump.

## 2. The magnet needs a finely set energy (rows A)

```
  delta 1.00e-01: overshoot 0.6564 d  <r^2> 0.9361 d^2  g 1.0870  inward pull 0.3149, net of push +0.0649
  delta 1.00e-03: overshoot 0.6184 d  <r^2> 0.4996 d^2  g 1.8007  inward pull 0.6408, net of push +0.3908
  delta 7.37e-05: overshoot 0.6181 d  <r^2> 0.4000 d^2  g 2.0000  inward pull 0.7128, net of push +0.4628
  delta 1.00e-06: overshoot 0.6180 d  <r^2> 0.3011 d^2  g 2.2149  inward pull 0.7838, net of push +0.5338
  delta 1.00e-10: overshoot 0.6180 d  <r^2> 0.1969 d^2  g 2.4623  inward pull 0.8587, net of push +0.6087
```

g = 2 occurs only at an energy 0.004% above the crossing threshold (δ = 7.4 × 10⁻⁵ in units of k e²/d). Near threshold g
changes only logarithmically. So g = 2 is a setting, not a result, unless something selects that energy. The spin share,
overshoot and pull were computed by principal-value integration. An adaptive simulation that carries the impulse as a
variable confirms the pull (0.3149 at δ = 0.1). An earlier uniform-time-sampled estimate (8, 17, −15) was wrong and is
discarded.

## 3. At g = 2 the shuttle is slower than the spin (rows B)

```
  delta 7.37e-05: half-length 38.6 r_C, poles 0.0162 c, shuttle frequency / rotation frequency = 0.71
```

Balancing the pull against the spin ħ/2 (equal inertias) gives a rod 77 Compton lengths long with the poles at 0.016c.
But the +eCP completes only 0.7 shuttles per rotation, so the premise of a fast shuttle between nearly fixed poles fails
exactly where g = 2.

## 4. The full dynamics break up (rows C)

```
  equal inertia, g = 2 energy             : over 4.3 rotations, pole separation reaches 43.4 d  (breaks up)
  +eCP 1/100 of a pole, robust crossing   : over 1.6 rotations, pole separation reaches 22.1 d  (breaks up)
```

Full planar three-body runs (softened pass-through) break up in every case tried. That covers equal inertia at the g = 2
energy and a light, fast +eCP (1/100 of a pole) crossing robustly. With Newtonian inertia and Coulomb forces, the spinning
shuttle rod does not hold, which agrees with 4292. **4295's "holds on charge alone" was a time-averaged force balance: a
necessary condition, never tested for stability.** It is corrected here.

## 5. What I think

The founder's rule (the passed pole pulls the +eCP back) is physically right, and with inertia it gives a clean,
parameter-free overshoot: the golden ratio. But every classical version of the electron so far has come apart: 4292's
free three-body problem, and now the shuttle rod, with equal or light +eCP. The common element is the *dynamics I have
been using*, Newton's F = ma with Coulomb forces between point charges. **That is not CPP's motion rule.** In CPP a CP
advances one PSR per Moment in the direction set by its SSV-net (founder 4288), and its inertia comes from the DP-arcs it
makes. That is a different kind of dynamics. A first-order, direction-following rule with a DP-arc memory can have stable
cycles that Newton-plus-Coulomb lacks. Known physics has the same lesson: the positronium negative ion exists, but not
classically.

The searches made here did not locate a coded version of the CP motion rule. So the next step is to write that rule down
precisely and simulate the rod with it, not with F = ma. That needs the founder's statement of the rule.

## 6. Founder question (a physical picture)

**Each Moment, how does a CP decide where to step?** Is it one PSR straight along its SSV-net, with no memory of its last
step? Or does it keep some of its previous heading, through the DP-arcs it has made, so that it coasts past a pole
before turning? If it keeps some, what sets how much?

## 7. PD-008

- **Convenient branch refused.** 4295's clean "rod of 8.3 r_C, g = 2 at 9.5%" is withdrawn. Its uniform speed conflicts
  with inertia, and its balance was not a stability test.
- **What stands.** The golden-ratio overshoot follows from the founder's rule plus energy conservation, with no freedom;
  g passes 2 only at a set energy; Newton-plus-Coulomb holds no spinning rod.
- **Limits.** Planar; softened pass-through; runs of four rotations or so; non-relativistic, although the +eCP's pole
  passes would reach c in CPP.
