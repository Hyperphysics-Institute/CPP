# Acceleration at a PSR Radius Does Not Fix the Unit of Action: Action Needs Momentum, and Spin Quantisation Is the Same Lump at Every Scale

**Patch:** 4298. **Lane:** EW → QM/SPIN. **Session:** 240.
**Founder:** `founders_voice/4298_question_hbar_half_from_weakest_centripetal_at_psr.md`. His proposal: the smallest unit of
spin is set by the weakest centripetal acceleration that can act at a PSR radius.
**Verify:** `series_standard_model/code/4298_action_at_psr_scale.py`.

## 1. The lattice's own units (D-7)

In the glossary, the Moment is the Planck time (5.39 × 10⁻⁴⁴ s) and the PSR is the displacement per Absolute Moment (the
Planck length at the base SSV, shrinking with SSV_abs). A CP steps at most one PSR per Moment, which is c. The GP lattice
is a nested hierarchy of **600-cells** (founders_vision §2), not a cubic grid.

## 2. The centripetal acceleration at a PSR radius (rows 1)

```
    centripetal acceleration on a circle of radius one PSR at one PSR per Moment: a = c^2/l_P = 5.561e+51 m/s^2
```

This is the **largest** centripetal acceleration the lattice allows, not the smallest, because a CP cannot step faster
than one PSR per Moment. A weaker one means a slower CP (v²/PSR). **There is a minimum**, as the founder intuited. Landing
is quantised to grid points, and grid points sit at a finer, sub-Planck spacing (xi2_relay_computation l. 172; SR-1 Patch
0736). So the smallest nonzero step is one GP spacing, and with it come a minimum speed and a minimum centripetal
acceleration. Their values depend on that spacing and are not evaluated here. §3 shows why, whatever they are, they do not
fix a unit of action.

## 3. Acceleration is not action (rows 2)

Angular momentum is momentum times radius. The lattice supplies the radius; the momentum comes from the CP's inertia.

```
  electron-scale CP, m_e c/3  : L at one PSR = 1.395e-23 hbar
  half the Planck momentum    : L at one PSR = 5.000e-01 hbar
  -> hbar/2 at one PSR needs p = hbar/(2 l_P) = m_P c/2, energy 6.10e+18 GeV = 1.19e+22 m_e c^2
  -> at electron-scale momentum hbar/2 needs radius hbar/(2p): p = m_e c/3 -> 1.50 r_C = 3.58e+22 PSR
```

- A CP carrying an electron's share of energy, circling at one PSR, carries **10⁻²³ of ħ**.
- To carry ħ/2 at one PSR, a CP would need half the Planck momentum, about 10²² times the electron's energy.
- At the electron's own energy, ħ/2 requires a radius of order the Compton length, about 10²² PSR. That is where the
  structure of 4286–4297 lives. **The electron's spin is not a PSR-scale circulation.**

## 4. What the lattice does supply, and the "½" (rows 3)

The lattice's natural unit of action is ħ = (Planck momentum) × (one PSR) = (Planck energy) × (one Moment). Two
cautions:

- **This is partly bookkeeping.** The Planck length and time are themselves defined using ħ, so identifying the PSR and
  the Moment with them brings ħ in with the units. CPP derives ħ only if it fixes the PSR, the Moment and a unit of
  energy independently.
- **The half does not come from the lattice's smallest loops.** A CP stepping one PSR around a closed loop carries
  momentum × the loop's inradius. The 600-cell's loops give 0.289 PSR (triangle face), 0.433 PSR (four-step loop, a
  rhombus of two triangles) and 0.688 PSR (pentagonal ring). Only a regular square gives exactly ½. The 600-cell's faces
  are all triangles, so its four-step loops are rhombi, not squares.

## 5. The decisive test: size-independence (rows 4)

Measured angular momentum comes in steps of ħ/2 for an electron, an atom and a spinning bowling ball alike. A minimum set
at one radius by one acceleration gives an action proportional to the momentum there, not a fixed lump. So the rule
cannot be "the smallest orbit". It has to be a rule about **how much action changes hands in each exchange**, the same
lump whatever the size or energy of the thing turning. In standard physics this comes from how rotations combine: a
spin-½ object needs two full turns to return to its starting state.

## 6. Where the lump could come from in CPP

- **Per DI-bit.** The glossary calls the DI-bit "the fundamental quantum of information/energy transfer between CPs". If
  each DI-bit exchange transfers a fixed action, every change of turning comes in that lump, at any scale. That is the
  size-independent rule that is needed.
- **The half, as a lead only.** In the pass-through ZBW (4265) a CP crosses its partner and returns to its starting
  state only after a second crossing. That is structurally like needing two turns to return. It is flagged to be tested,
  not claimed.

## 7. Founder question (a physical picture)

**What does a single DI-bit carry?** When one DI-bit arrives and changes a CP's V_i, is there a fixed amount of that
change, a smallest nudge, and does it transfer a fixed amount of energy or momentum? If there is a fixed lump per DI-bit,
that lump is where ħ/2 would come from.

## 8. PD-008

- **Convenient branch refused.** A square loop gives ħ/2 = (Planck momentum) × (½ PSR) exactly. It is not the corpus's
  lattice, and the Planck momentum is not the electron's, so it is not reported as a result.
- **Corrected before commit.** A first draft said the lattice has no minimum step; GP-quantised landing at a sub-Planck
  spacing gives one.
- **What is solid.** The acceleration at a PSR radius at one PSR per Moment is the lattice's maximum; action needs momentum, so an
  electron-scale CP at one PSR carries 10⁻²³ ħ; spin quantisation's size-independence rules out any fixed-radius
  mechanism.
