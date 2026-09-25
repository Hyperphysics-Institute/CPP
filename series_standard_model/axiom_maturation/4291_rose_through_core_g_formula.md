# The Inner Spirograph Is a Rose Through the Core: Its Magnet Comes Only From the Turning of Its Line; Tips at Twice the Outer's Rate Cancel the Magnet

**Patch:** 4291. **Lane:** EW → QM/SPIN. **Session:** 240.
**Founder:** `founders_voice/4291_ruling_same_direction_inner_spirograph_through_core.md` (answers 4290 §6: the same way).
**Verify:** `series_standard_model/code/4291_rose_through_core.py`.

## 1. The picture, settled

Both CPs of the captured DP circulate the **same way**. The outer −eCP runs on a circle. The inner +eCP traces a
**spirograph through the core**: through the central −eCP, out to the circle, back through the centre, out again, with
the touching point advancing in the same sense. The founder's "the +eCP produces a spin in one direction, the −eCP the
other" is true of their **magnets**. Their **angular momenta** (the spin proper) point the same way and add. A charge's
magnet flips with the sign of its charge; its angular momentum does not.

## 2. A spirograph through the core is a rose curve (rows 1)

The swing through the core along a line that slowly turns, r = R cos(ω_r t) on a line turning at W, is the rose
r = R cos((ω_r/W)θ). Its sweep is exact: r × v = r²θ̇ = r²W, so ⟨r × v⟩ = W⟨r²⟩ = WR²/2.

```
  w_r = 1.0, W = 0.5:  <r x v> traced = 0.25000   W/2 = 0.25000
  w_r = 3.0, W = 1.0:  <r x v> traced = 0.50000   W/2 = 0.50000
  w_r = 1.0, W = 2.0:  <r x v> traced = 1.00000   W/2 = 1.00000
  w_r = 5.0, W = 0.3:  <r x v> traced = 0.14999   W/2 = 0.15000
```

**The passes through the core carry nothing.** All of the inner's spin and magnet come from how fast its line turns,
independent of how fast it swings.

## 3. Does it make sense? Yes, with one requirement (rows 2)

A line through the core **cannot turn under the core's pull alone**. A central pull keeps the inner's angular momentum
at zero, and the swing stays on one fixed line. So the turning must come from the **partner**: the outer −eCP, circling,
pulls its +eCP around. Angular momentum then passes back and forth within the pair, and only the total is fixed. That is
physically natural, since the dipole's two CPs attract, and it matches "only the sum is detected". It also means the
inner's motion is set by the pair's dynamics, not by the core.

## 4. The magnet (rows 3)

With x = W/ω_o (how fast the tips advance compared with the outer), both circulating the same way:

  S = R²(m_o ω_o + m_i W/2),  μ = (e/2)R²(−ω_o + W/2),  **g = m_e (1 − x/2) / (m_o + m_i x/2).**

```
  tips advance at W = 0.0 w_o, m_o = 0.500, m_i = 0.500 m_e:  g = 2.000
  tips advance at W = 1.0 w_o, m_o = 0.167, m_i = 0.167 m_e:  g = 2.000
  tips advance at W = 2.0 w_o, m_o = 0.500, m_i = 0.500 m_e:  g = 0.000   <- the inner's magnet cancels the outer's exactly
```

- **Tips advancing at twice the outer's rate give no magnet at all**, whatever the inertias. The inner's field exactly
  cancels the outer's. The electron has a magnet, so the tips must advance **slower than twice** the outer's rate.
- Below that, g = 2 fixes the inertias: at W = 0 (a fixed diameter), m_o = m_e/2 (4288); at W = ω_o, equal inertias of
  m_e/6 each.

## 5. If the inner meets its partner at each tip (rows 4, 4b)

A natural reading of "out to the circumference" is that each swing reaches the outer −eCP, its partner. Tips alternate
sides of the core, so meeting at every tip requires **W = ω_o + (2j − 1)ω_r**. Checked on traced tips:

```
  j=0, w_r=w_o             W = 0.0: max tip-to-partner angle over 8 tips = 9.80e-16 rad
  j=1, w_r=w_o             W = 2.0: max tip-to-partner angle over 8 tips = 9.80e-16 rad
  j=0, w_r=w_o/2           W = 0.5: max tip-to-partner angle over 8 tips = 9.80e-16 rad
  j=1, w_r=w_o/2           W = 1.5: max tip-to-partner angle over 8 tips = 4.17e-15 rad
  W=w_o (not a solution)   W = 1.0: max tip-to-partner angle over 8 tips = 3.14e+00 rad
```

With one full swing per outer revolution, the meeting solutions are a fixed diameter (W = 0) and **tips at twice the
outer's rate (W = 2ω_o), which is the founder's remembered "twice the rate", and which gives zero magnet**. If that old
result carries over to the pass-through orbit, it is ruled out by the electron's magnet. The fixed-diameter solution
survives, with g = m_e/m_o.

## 6. The unit counting

With both CPs circulating the same way, the spin is L_o + L_i, a sum. If each CP had to carry whole units of ħ/2, the
only sum equal to ħ/2 is (ħ/2, 0): the fixed diameter, W = 0. Otherwise the ħ/2 applies to the pair's total, and the
inner's share WR²m_i/2 is whatever the dynamics make it.

## 7. What I think (answering the founder)

The spirograph makes sense, provided its turning is driven by the partner rather than the core (§3). It is the first
version of the inner orbit whose contribution can be computed exactly. The computation gives a sharp constraint:
**the inner's tips must advance slower than twice the outer's rate**, and the remembered "twice the rate" is precisely
the rate at which the electron would have no magnet. The simplest survivor is the inner swinging on a diameter locked to
its partner, with the outer carrying the spin and inertia m_e/2 (4288).

## 8. Founder question (a physical picture)

**While the outer −eCP goes once around, how many times does the inner +eCP swing out to touch the circle, and is its
partner right there each time it touches?** The answer fixes W, and with it g.

## 9. PD-008

- **Convenient branch, marked.** The fixed diameter (W = 0) reproduces 4288's simple result. It is favoured here only
  because the other natural meeting solution gives zero magnet, not because it has been derived.
- **Not claimed.** That the inner's swing is sinusoidal (⟨r²⟩ = R²/2 assumes it). For a general swing the magnet
  cancels at W = ω_o R²/⟨r²⟩, which is 2ω_o only for a sinusoidal swing. A swing that lingers near the circle
  (⟨r²⟩ > R²/2) cancels at a slower rate. §3's requirement and the sign structure of §4 do not depend on the profile.
