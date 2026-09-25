# Petal Loops and the Magnetic Moment: Right Direction and Right Size Range; g Measures the Energy Split

**Patch:** 4281. **Lane:** EW (with foundations). **Session:** 239.
**Founder:** `founders_voice/4281_ruling_petal_loops_carry_spin.md`.
**Verify:** `series_standard_model/code/4281_petal_orbit_magnetic_moment.py`.

## 1. The model

The orbital eDP's −eCP pole is taken as a **massless point charge moving at c**. CPs carry no rest mass, so its inertia
is its kinetic energy (SF-6's arc store). It moves in a central well V(r) ≥ 0, with V = 0 at superposition. Its total
energy is the particle's rest energy (c04: mass = oscillation energy, KE + PE), and its angular momentum is ħ/2, the
spin carrier. In a central well L is conserved, and the orbit is a **rosette**: the founder's petal loops, between an
inner and an outer turning radius.

The moment of a charge circulating this way is μ = (q/2)⟨r × v⟩. Writing μ = g(q/2m)L gives exactly

  **g = ⟨E_total / E_kin(pole)⟩**, time-averaged over the petals.

## 2. Rows verbatim (D-11)

```
no well (V = 0): circle of radius L/(mc) = hbar/2mc -- c04's r_th -- at speed c:  g = 1 exactly
harmonic well V = k r^2/2, E = mc^2, L = hbar/2:
  k =  0.02: g = 2.534   petals between r = 0.501 and 9.740 r_ZBW
  k =  0.10: g = 2.127   petals between r = 0.506 and 4.197 r_ZBW
  k =  0.25: g = 1.894   petals between r = 0.517 and 2.534 r_ZBW
  k =  0.50: g = 1.718   petals between r = 0.539 and 1.675 r_ZBW
  k =  0.75: g = 1.615   petals between r = 0.569 and 1.272 r_ZBW
  k =  1.00: g = 1.543   petals between r = 0.618 and 1.000 r_ZBW  <- route (H) stiffness
  k =  1.10: g = 1.519   petals between r = 0.653 and 0.897 r_ZBW
  k =  1.15: g = 1.508   petals between r = 0.684 and 0.836 r_ZBW
  k =  1.20: no orbit with L = hbar/2 at this energy
  g = 2 (Dirac) at k = 0.165: petals between r = 0.511 and 3.199 r_ZBW

-> Petal loops give a moment along the spin, of the right size range: g = <E_total/E_kin(pole)>, from 1 for a free
   circle upward as more of the rest energy is stored in the well.  Route (H)'s stiffness (k = 1) gives g = 1.54;
   Dirac's g = 2 needs a well ~6x softer (k = 0.165), whose petals reach out to ~3.2 r_ZBW.
```

## 3. What I think (answering the founder)

**(i) Yes, in direction and in size range.** Petal loops carry the spin as a net circulation, and a circulating
charge makes a magnetic moment along that spin. The size comes out in the observed range:
- With no well, the pole runs a circle of radius ħ/2mc (c04's r_th) at c, and g = 1.
- Storing part of the rest energy in the well raises g.
- At route (H)'s stiffness, **g = 1.54**.
- **Dirac's g = 2** is reached with a well about 6× softer (k = 0.165), whose petals reach out to about 3.2 r_ZBW.

**(ii) g has a physical meaning in this picture.** g − 1 measures how much of the particle's rest energy sits in the
field rather than in the circulating pole's motion. g = 2 means that on (harmonic) average the pole carries half the
energy as motion, with the rest stored. That is a CPP-native reading of Dirac's 2, and it is testable against a
derived well.

**(iii) Petal geometry, as a consequence.** With L = ħ/2 and energy mc², the pole can never come closer to the core
than **ħ/2mc**, c04's r_th, in every case computed. So "just beside the centre" means at least about half the ZBW
radius away. The petals are broad loops, not near-misses.

## 4. What it implies for the nucleon work (filed)

The nucleon moments since 4242 take each quark as a Dirac particle (g = 2) with the motion factor S. If the quark's own
spin carrier is a petal orbit with the route (H) well, its g is 1.54, and μ_p and μ_n would scale by 0.77. The fitted
m_q would then fall to about 230 MeV. This model is minimal: it has one pole; the eDP's +eCP pole and its cloud are
left out, and the well's shape and depth for the quark's own orbital are not derived. So this is a lever to be
settled, not a correction to apply now.

**PD-008.** The convenient statement would be "petal loops give g = 2". They give g = 2 only for a particular softness
of well. That softness is recorded as what CPP must derive.

**Erratum (Patch 4286):** "route (H)'s stiffness (k = 1)" mis-resolves route (H) (D-7). Route (H) is amplitude ħ/mc, frequency mc²/ħ, speed c (4266 (a), 4272 §1); k = 1 is the massive oscillator's ½mω²r², and for the massless pole its orbit has mean radius 0.805 r_ZBW and angular rate 1.225 mc²/ħ. On a circle g = 2r/r_ZBW exactly, so **route (H)'s own orbit gives g = 2**, and §4's 0.77 scaling (m_q ≈ 230 MeV) is withdrawn. See `series_standard_model/axiom_maturation/4286_g_is_orbit_radius_route_H_gives_2_spin1_gives_0172.md`.
