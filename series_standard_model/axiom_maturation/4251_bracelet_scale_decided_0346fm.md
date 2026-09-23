# The Bracelet's Working Size: 0.346 fm, the 600-Cell's Own — Five Constraints, One Lattice, Two Numbers Re-owed

**Patch:** 4251. **Lane:** EW. **Session:** 238. **Decides:** TODO-4248-BRACELET-SCALE (working value) under the founder's
delegation at `founders_voice/4251_*`.
**Verify:** `series_standard_model/code/4251_bracelet_scale_decision.py`.

## 1. Triangulation — rows verbatim (D-11)

```
constraint                                                        (i) 0.0025 fm    (ii) 0.346 fm
C1 one lattice: bracelet at SS-2's l_unit (no second scale)     needs 2nd scale              yes
C2 SF-2 Delta E_centroid = O(m_e): ring well alpha hbar c / r_B          587 MeV            4 MeV
C3 trap beats the core's pull at d ~ r_B: (2/3) alpha hbar c / r_B   587 vs 391 MeV       4 vs 3 MeV
C4 linear -eCP oscillation (0.105 fm) inside the ring (held, 4247/4248)    no (43x ring)   yes (0.30 r_B)
C5 NC occupancy f = 1 (4246/4247)                                  only if held              yes

DECISION (worker, PD-006 under the founder's 4251 delegation): (ii) r_B = 0.346 fm -- G-EW-BRACELETSCALE-4251, working value.
  (i) fails C1 and C2 outright and C4/C5 unless the trap is assumed; (ii) meets all five with no new scale introduced.

consequences, recomputed:
  4231 kick bound: max |dL|/L = r_kick/r_orb.  At the pocket 0.0025 fm: 3.9e-03 (0.4%).  If the kick can land anywhere
  inside the ring: 0.55 (55%) -- the geometric guarantee of B = +1 is LOST; L-preservation must come from the
  reset happening at the ring's zero-gradient CENTRE (lever arm << r_B) or from the pair state (4223/4228). Re-owed.
  4233 budget at (i) Compton   : pole-in-ring per cycle = 1.24e-03;  (W0 present, aligned) x (outward) = 1.17e-23 = 4.37e+00 x (m_e/m_W)^4 (m_e/m_const)
  4233 budget at (ii) 600-cell : pole-in-ring per cycle = 1.75e-01;  (W0 present, aligned) x (outward) = 8.26e-26 = 3.10e-02 x (m_e/m_W)^4 (m_e/m_const)
  -> at 0.346 fm the ring is crossed on 18% of circulations, so the whole 1.4e-26 per cycle sits in (W0 present) x (outward):
     the (E/m_W)^2 bracelet-formation target of 4233 stands, its O(1) coefficient changes from 4.4 to 0.03. Re-owed with the target.
```

## 2. Decision

**G-EW-BRACELETSCALE-4251 (working value, calibration not derivation): the W⁰ bracelet is a 600-cell substructure at
the same lattice as the nucleon, r_B = 0.58779 × l_unit = 0.346 fm.** Grounds: it introduces no second scale (the
600-cell lattice calibrated once at SS-2 is the corpus's one length calibration); it gives SF-2's own ΔE_centroid =
O(m_e) (4 MeV) instead of 587 MeV; the ring's well beats the core's pull at the ring's distance; the down quark's linear
oscillation (0.105 fm) sits inside it, which is what "held" (4247) and the founder's internal-ZBW trap (4248) need; and
the neutral-current occupancy f = 1 (4246) follows. The Compton reading (0.0025 fm) was 4229's assumption, made without
these checks; it fails C1 and C2 outright.

## 3. What changes, owned

- **4231's L-preservation bound** was r_pocket/r_orbit = 0.4% and gave *"B = +1 by geometry."* At r_B = 0.346 fm a kick
  anywhere inside the ring could change L by up to 55%. The guarantee now needs either that the reset happens at the ring's
  zero-gradient centre (lever arm ≪ r_B — the founder's 4248 picture puts the trapped −eCP oscillating *among the +CPs*,
  not at the centre) or the pair-state argument (4223/4228: the antineutrino leaves with the orbital's L). **Re-owed:
  TODO-4251-LKICK.** B = +1 stands on 4223/4228 meanwhile.
- **4233's rate budget:** the pole crosses the ring on 18% of circulations, not 0.12%, so the whole per-cycle
  probability 1.4×10⁻²⁶ sits in (W⁰ present) × (outward branch); the (E/m_W)² bracelet-formation target stands with its
  O(1) coefficient 4.4 → 0.03. **Re-owed with the target: TODO-4251-LIFETIME** (supersedes 4233's numbers, not its form).
- 4246/4247/4248 strengthen; nothing else on file used the pocket size.

## 4. PD-008

Convenient: pick the size that makes the founder's trap strongest (0.0025 fm, 587 MeV) — it also keeps 4231 and 4233
intact. Refused: it needs a second length scale the corpus never introduced and contradicts SF-2's own centroid energy.
The inconvenient consequence of the chosen size — two shipped numbers re-owed — is registered rather than absorbed.
Under the founder's own terms this is calibration in explore mode; nothing here is a derivation of the W's size.
