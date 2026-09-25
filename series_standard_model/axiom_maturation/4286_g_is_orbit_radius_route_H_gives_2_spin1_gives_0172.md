# g Is the Orbit Radius: Route (H)'s Orbit Gives g = 2 Exactly; 4281's 1.54 Was a Mis-Resolved Symbol; SPIN-1's Own Spin Carrier Gives g = 3 − 2√2

**Patch:** 4286. **Lane:** EW (with QM/SPIN and foundations). **Session:** 240.
**Verify:** `series_standard_model/code/4286_g_is_orbit_radius_route_H_gives_2.py`.
**Works:** TODO-4264-PASSTHROUGH (5)(i)–(ii), the quark orbital's g (boot card item 2).
**Critiques:** 4281 (D-7). **New finding against:** SPIN-1 (never computed its moment) and phenomena-SM-1 §C4 (cites a
derivation that is not in SM-1).

## 1. The identity (rows A)

In 4281's model, a massless pole of charge q moves at c with |p|c + V = E = mc² and L = ħ/2, and
g = ⟨E/E_kin(pole)⟩. On a **circle** of radius r, E_kin = cL/r is constant, so:

  **g = 2 r / r_ZBW**, with r_ZBW = ħ/mc.

This is kinematics plus the definitions; no well shape enters. It carries the whole result:
- **c04's r_th = ħ/2mc (Schrödinger's triad, ω = 2mc²/ħ): g = 1.** This is the classical ZBW's famous factor-2
  shortfall, and it is also the closest the pole can ever come (all energy kinetic, 4281 §3(iii)).
- **Route (H), r_ZBW = ħ/mc, ω = mc²/ħ: g = 2 exactly.** The pole carries half the rest energy as motion; the well
  stores the other half.

## 2. 4281 mis-resolved "route (H)" (D-7), rows C

4281 labelled the harmonic well V = kr²/2 with k = 1 "route (H)'s stiffness" and reported g = 1.54 there. Resolving
the symbol against the lane that wrote it: 4266 (a) and 4272 §1 define route (H) as **amplitude ħ/mc, angular frequency
mc²/ħ, speed c**. k = 1 is the potential of a *massive* oscillator at that frequency, ½mω²r². For a massless pole it
does not produce route (H)'s orbit:

```
(C) 4281's 'route (H) stiffness' k = 1 (V = k r^2/2, the massive oscillator's well at omega = mc^2/hbar), massless pole:
  petals r = 0.618 .. 1.000 r_ZBW, time-mean radius 0.805, mean angular rate 1.225 mc^2/hbar,  g = 1.5426
  virial check (massless, H = |p|c + V): <|p|c> = 0.6667  <r V'> = 0.6667
  -> neither route (H)'s radius (1) nor its frequency (1): the orbit's mean radius is smaller and it circulates faster.
```

So 1.54 is the g of a smaller, faster orbit that merely touches r_ZBW at its outer turning point. **At route (H)'s
actual orbit g = 2.** 4281 §4's consequence, that the nucleon moments scale by 0.77 and m_q falls to about 230 MeV,
is **withdrawn**. It was filed as held and never applied, so nothing downstream moves. The nucleon moments' g = 2
stands on the same route (H) the g_A arc uses. That is one convention serving both, not a second fit.

## 3. What the well must do (rows B, D, E)

A circle at r_ZBW with energy mc² requires V(r_ZBW) = mc²/2 (the stored half) and circular equilibrium
V′(r_ZBW) = cL/r² = mc²/2r_ZBW. Together these give **V = rV′ at the orbit**: the well must be locally linear through
V(0) = 0, a constant force there. In general, on any circle, **g − 1 = V/(rV′)** (stored energy over kinetic).

```
(B) put each power-law well's circle AT r_ZBW (A n = 1/2, from circular equilibrium cL/r^2 = V'(1)):
    then E_kin = 1/2 always, V(1) = A = 1/(2n), E = 1/2 + 1/(2n), and g = E/E_kin = 1 + 1/n.
  n = 0.5: A = 1.0000  circle radius 1.0000 r_ZBW  E = 1.5000 mc^2  g = 3.0000
  n = 1.0: A = 0.5000  circle radius 1.0000 r_ZBW  E = 1.0000 mc^2  g = 2.0000   <- the only one whose energy is the rest energy mc^2
  n = 2.0: A = 0.2500  circle radius 1.0000 r_ZBW  E = 0.7500 mc^2  g = 1.5000
  n = 3.0: A = 0.1667  circle radius 1.0000 r_ZBW  E = 0.6667 mc^2  g = 1.3333
```

In a linear well, with E = mc² and L = ħ/2, the petal family (rows D) keeps ⟨E_kin⟩ = mc²/2 exactly, by the massless
virial ⟨|p|c⟩ = ⟨rV′⟩. g is 2 on the circle and exceeds 2 for every petal (Jensen: g ≥ 1 + 1/n):

```
  s = 0.4800: petals 0.8333 .. 1.2500  mean r 1.0417  omega 0.9599  <E_kin> 0.5000 (virial <rV'> 0.5000)  g = 2.04092
  s = 0.4950: petals 0.9091 .. 1.1111  mean r 1.0101  omega 0.9900  <E_kin> 0.5000 (virial <rV'> 0.5000)  g = 2.01006
  s = 0.4999: petals 0.9861 .. 1.0143  mean r 1.0002  omega 0.9998  <E_kin> 0.5000 (virial <rV'> 0.5000)  g = 2.00020
```

**Not claimed:** that the well *is* linear, and anything about a_e. The sign of a petal's excess (g > 2) matches the
measured anomaly's sign, but fitting its size would be one number fitted to one number. It is recorded here so it is not
rediscovered as a prediction. The well itself is still underived. Deriving it is the owed item, and it is now a sharper
one: *show the orbital stores half its energy at a circular equilibrium at r_ZBW*.

## 4. SPIN-1's spin carrier cannot make the electron's magnet (rows F)

D-1 search: the one corpus statement of a Bohr magneton is phenomena-SM-1 §C4, *"the electron's orbital Dipole Pair
generates exactly one Bohr magneton (SM-1 §8)"*. **SM-1 §8 ("Connection to ZBW Spectrum and Geometric Suppression")
contains no magnetic-moment content.** The corpus's own mechanical model of the spin carrier is SPIN-1: a captured DP
around the −eCP core, +eCP at r_in and −eCP at r_out = 2r_in, each CP of mass m_e, circular Coulomb orbits,
co-rotating, with L = ħ/2 derived. SPIN-1 never computes that system's magnetic moment. It is fixed by SPIN-1's own
equations with no new input:

```
  r_in = 2.2698e-12 m = 5.878 r_ZBW;  w_in/w_out = 2.82843;  v_in/c = 0.0352, v_out/c = 0.0249
  L = 1.000000 hbar/2
  mu(+eCP, inner) = +0.20711 muB   mu(-eCP, outer) = -0.29289 muB   net = -0.08579 muB (antiparallel to L)
  g = |mu| / ((e/2m) L) = 0.171573 = (sqrt2 - 1)^2 = 3 - 2 sqrt2 = 0.171573  (constant-free, like SPIN-1's 2 sqrt2)
  measured electron: g = 2.0023193, |mu| = 1.00116 muB  ->  SPIN-1's carrier gives 0.0857 of it (1/11.67)
```

The sign is right: the outer −e dominates, so the moment is antiparallel to the spin, as for the electron. **The size is
1/11.7 of the measured value.** The cause is structural: the carrier is a *neutral* dipole, and its two opposite charges
nearly cancel. No choice of r_in helps, because g = 3 − 2√2 is independent of every constant. **So SPIN-1's carrier
derives the electron's spin but cannot supply its magnetic moment.** No number in print changes, since neither SPIN-1
nor SM-1 prints a moment. **phenomena-SM-1 §C4's claim, however, has no derivation behind it, and the corpus's own
carrier model contradicts it.** It is filed for correction.

**Searched unscoped (gate-required).** The whole tree, several phrasings: `magnet|mu_B|Bohr magneton|g-factor|gyromagnetic` across `spin_papers/` (every hit is "electromagnetic" or a photon's magnetic curl); files naming SPIN-1, c20 or a captured DP that also mention a magnetic moment (only `future_projects.md` Project 7, an unstarted goal, and 4112); and inner/outer-eCP current-loop phrasings (none). **One D-10 pointer:** 4112 (chirality_axiom_maturation l. 875) writes the nucleon moment as ⟨L̂ + 2Ŝ⟩. That **uses** g_s = 2 as the Dirac operator factor rather than deriving it, and it assigns the spin half to the CP's A_i register (Option B, A3′), whose retirement is pending (TODO-4181/4182). That is a candidate for reading (c) in §6.

This also resolves the tension with §1. Route (H)'s g = 2 needs a **single net charge** carrying L = ħ/2 around a circle
of radius ħ/mc. A neutral dipole cannot be that charge. What CAN is a CPP physics question, and it goes to the founder
(§6).

**Premise note (D-2, not resolved here).** SPIN-1 (Mar 2026) gives each CP rest mass m_e and slow (0.03c) Coulomb
orbits at about 6 r_ZBW. Since then, SF-6 (l. 170) has treated inertial mass as a coherent ZBW pattern (4281's
massless pole follows it), R-ZBW-PASS-THROUGH (4265) has made ZBW a speed-c transit, and 4281 has put the orbital pole in
petal loops at c. None of these explicitly supersedes SPIN-1's premises, and whether a bare CP has rest mass is
axiom-level. The moment result above is SPIN-1's on SPIN-1's own premises.

## 5. For the quark (the item as queued)

The nucleon moments since 4242 assume the quark's spin carrier has g = 2. On §1–§2 that holds exactly if a single net
charge circulates at the quark's own r_ZBW = ħ/m_q c. It fails badly (×0.086) if the carrier is a neutral captured DP of
SPIN-1's form. μ_p cannot discriminate, because m_q is fitted to it (4268), and μ_n/μ_p is independent of both m_q and an
overall g. **The electron is the test, not the nucleon.** Its measured g = 2.0023 passes the single-charge route (H)
reading and fails SPIN-1's carrier.

## 6. Founder question (a physical picture)

When the electron makes its magnetic field, **which charge is actually going around?**

- **(a) The two ends of the captured spin dipole** (SPIN-1's plus-inside, minus-outside pair). Their opposite charges
  nearly cancel, and the magnet comes out about 1/12 of what is measured.
- **(b) The electron's own −eCP charge**, swinging on its ZBW circle of radius ħ/mc at the speed of light while it
  carries the half-unit of spin. This gives the measured magnet, g = 2, exactly, provided whatever holds it there
  stores half of its energy.
- **(c) Something else** in your picture. For example, the moment could come from each CP's own spin register (4112's
  Option B), in which case neither orbit sets g.

## 7. PD-008

- **Convenient branch taken, and marked.** "Route (H) gives g = 2" is the convenient reading. It rescues the nucleon
  moments' assumption and joins g_A's convention to the electron's g. Its weight rests on the §1 identity, which is only
  kinematics. The physics is all in the premise that **one net charge circulates at ħ/mc**, and I have not derived that
  premise. §4 shows the corpus's only worked carrier model does *not* satisfy it.
- **Branch not taken.** Keeping 4281's 1.54 and applying the 0.77 scaling (m_q ≈ 230 MeV) would rest on the
  mis-resolved symbol of §2.
- **Inconvenient finding, stated at full strength.** SPIN-1's carrier fails the electron's magnet by 11.7×, with no free
  constant to adjust. If the founder's answer is (a), the programme has no account of the electron's magnetic moment.
- **For the next context window, press this:** (i) whether the central −eCP's own ZBW motion, which SPIN-1 fixes at
  r = 0, can supply the single charge of reading (b) without breaking SPIN-1's L = ħ/2; (ii) whether a massless-pole
  version of SPIN-1's two-pole carrier (4281's inertia, SPIN-1's geometry) changes 3 − 2√2. Both are computations,
  filed under TODO-4286-GMOMENT.
