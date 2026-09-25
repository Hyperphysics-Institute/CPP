# The Hub-and-Rim Electron: With the Inner +eCP ZBW-Locked to the Core, g = 2 Is Structural (Two CPs at the Hub, One on the Rim)

**Patch:** 4293. **Lane:** EW → QM/SPIN. **Session:** 240.
**Works:** TODO-4286-GMOMENT (F), a binding model starting from the pass-through ZBW lock (4292 §5). Founder
delegation: `founders_voice/4292_delegation_compute_what_works_outer_shape_open.md`.
**Verify:** `series_standard_model/code/4293_hub_and_rim_g.py`.

## 1. The model

- **Hub:** the core −eCP and the inner +eCP, **ZBW-locked**. The +eCP is the core's own pass-through partner (glossary
  l. 408: a CP oscillating through its opposite-charge partner), so the two stay together, separating only by the small
  ZBW swing.
- **Rim:** the outer −eCP, held to the inner +eCP by the captured DP's bond.
- The whole electron is a **dumbbell spinning about its centre of mass**. The hub circles at R/3 and the rim at 2R/3, on
  opposite sides. **The core is not at the centre.**
- Equal moving inertia per CP (4292's default, flagged); the electron's mass is their sum.

This is where 4292's first scan pointed: with the +eCP *on* the core, the spin share was exactly 1/6. There it was an
artefact, because Coulomb forces did not keep the +eCP there. Under a ZBW lock it does stay there.

## 2. Result (rows 1–2)

```
  R =  1.0, w =   1.0:  g = 2.000000   spin shares core/inner/rim = 0.1667/0.1667/0.6667
  R =  3.0, w =   0.2:  g = 2.000000   spin shares core/inner/rim = 0.1667/0.1667/0.6667
  R =  0.1, w =  40.0:  g = 2.000000   spin shares core/inner/rim = 0.1667/0.1667/0.6667
  -> the hub's +e and -e move together, so its magnet cancels; only the rim makes the magnet.
     g = (m_e/m_rim)(L_rim/S) = ((M+m)/m)(M/(M+m)) = M/m = 2: two CPs at the hub, one on the rim.
```

**g = 2 exactly, for any size, any spin rate, any bond law, any speed.** The hub is magnetically silent because its
opposite charges move together. The rim carries 2/3 of the spin with 1/3 of the inertia. The inner +eCP carries 1/6 of the
spin, exactly the target of 4292 §1. Row 2 shows the count is what matters: g = (hub CPs)/(rim CPs).

## 3. The hub's ZBW swing (rows 3)

```
  A = 0.1 R, swing in plane, along the dumbbell  : g = 1.99256
  A = 0.1 R, swing in plane, across              : g = 1.99253
  A = 0.1 R, swing out of plane                  : g = 2.00000
```

The hub's internal pass-through swing (the founder's "through the core") changes g only at second order in its amplitude
over the dumbbell's size, and not at all if it swings along the spin axis. A swing that turns with the dumbbell adds a
little spin and no net magnet, so g falls slightly below 2.

## 4. How this answers the founder's question

- **Rate:** there is no separate inner rate to tune. The inner rides with the core, and both go round once per rim
  revolution.
- **Outer shape:** a circle about the centre of mass, radius 2R/3. The core traces the smaller circle, R/3.
- **The inner's track:** its pass-through of the core is the hub's ZBW swing, small compared with R. It does not reach
  out to the rim, which is a different picture from the spirograph of 4291.
- **What holds the rim:** the hub is neutral, so its Coulomb pull on the rim is zero. That is 4292's finding again. The
  rim is held by the DP bond between the inner +eCP and the rim −eCP, which is a sea-mediated bond, not a Coulomb one.

## 5. Recorded, not claimed (rows 4)

```
  eps = 0.00116:  g = 2(1+eps) = 2.00232
```

If a fraction ε of the electron's mass-energy is outside the three CPs' inertia (bond, field) **and carries no spin**,
g = 2(1 + ε). The measured anomaly would then correspond to ε = a_e = 0.116%. This is one number matched to one number,
and the no-spin condition is unexamined. It is recorded so that it is not later rediscovered and taken for a prediction.

## 6. Still owed

- **(F1)** The DP bond that holds the rim: its law, and whether the spinning dumbbell is dynamically stable under it
  (4292 showed that Coulomb forces alone are not stable).
- **(F2)** ħ/2 still sets the size R, once the bond law and ω are known (the spin is still input, 4289).
- **(G) The equal-inertia assumption is now load-bearing:** g = M_hub/m_rim. If the core's inertia differs from the DP
  CPs', g moves with it.
- **(F-check)** 4292's 3-D, softening and duration checks of the breakup.

## 7. PD-008

- **Convenient branch, marked.** g = 2 from a simple count is exactly the kind of clean result to distrust. Its weight
  rests on two premises: the ZBW lock keeps the inner on the core, and the three CPs have equal inertia. Neither is
  derived. The dynamics holding the rim are not shown.
- **Where it departs from the founder.** His spirograph had the inner reaching out to the circle (4291). Here it stays at
  the hub, and the core circles the centre. That needs his judgement (§8).
- **In its favour, stated plainly.** It needs no tuned rate, radius or speed. It gives the spin share that 4292 said was
  required, and it explains why Coulomb forces could not hold the pair: the hub is neutral.

## 8. Founder question (a physical picture)

Does this match your conception? In this picture the inner +eCP stays with the core, the two passing through each other
in the core's own ZBW. The outer −eCP is held on the far end by its bond to the +eCP. The whole electron spins like a
dumbbell, with the core swinging round the centre rather than sitting at it.

**Erratum (Patch 4294):** §4's "the rim is held by … a sea-mediated bond" named no force. Charge falls short by α at the Compton scale, and a neutral hub supplies 10⁻³ of the needed force or less. A bond of ZBW strength would hold the rim, but it puts half the rest energy into the orbit, so §2's accounting (m_e = 3m, binding negligible) does not apply and **g = 2 here is provisional**. See `series_standard_model/axiom_maturation/4294_charge_cannot_hold_spin_zbw_force_can.md`.
