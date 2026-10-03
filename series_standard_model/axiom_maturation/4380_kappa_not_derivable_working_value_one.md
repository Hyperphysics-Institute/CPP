# κ Is Not Derivable from the Corpus as It Stands: GW250114 Allows 0.70 ≤ κ ≤ 1.21, Natural Normalisations Scatter from 0.3 to 6, and the Recommended Working Value Is κ = 1 (a Calibration, Like Mercury's ½), Pending a Fresh Critic and the Consistency Pass

**Patch:** 4380. **Lane:** foundations, with GR. **Session:** 242.
**Founder:** `founders_voice/4380_mechanism_slows_clocks_magnitude_deferred.md` (the mechanism slows clocks; magnitude
deferred to calculation).
**Verify:** `series_standard_model/code/4380_kappa_window_and_normalisations.py` (sympy + scipy).

## 1. The window

With the round-trip clock (4379) and GR-1c's self-consistency, GW250114's ±2.4% (eikonal, non-spinning) allows

    0.70 ≤ κ ≤ 1.21,   with κ = 1 exact Einstein.

## 2. Can the corpus fix κ? Not yet

The natural move is to set the extra leg asymmetry equal to "the extra part of the sphere informed directly". That needs
a normalisation, and the natural-looking ones disagree:

| normalisation of the extra direct informing | κ | in the window? |
|---|---|---|
| a. extra fill fraction Δf | 0.750 | yes |
| b. Δf relative to the uninformed remainder, Δf/(1 − f₀) | 0.857 | yes |
| c. Δf relative to the ordinary fill, Δf/f₀ | 6.000 | no |
| d. extra band depth (radius fraction) | 0.273 | no |
| e. extra band depth relative to the ordinary depth | 6.277 | no |

**None is forced.** Two land in the window (a, b), three do not. κ needs a PCD-level model of how the leg asymmetry
follows from near-field informing, which the corpus does not have. Choosing (a) or (b) because they pass would be
fitting.

**One condition is derived** (script part 3): if ordinary space already had a leg asymmetry β₀, the round trip would
carry a first-order term −2β₀δβ/(1 − β₀²), which Cassini forbids. So **the ordinary-space round trip must be symmetric**,
with all the asymmetry coming from the fill excess. This is 4377's "induced, not standing" condition, in round-trip
form.

## 3. What κ does and does not touch

- **First order is untouched for every κ.** X enters at second order in the stress. So 4364's source rule (injection ∝
  the GP count, derived at first order in the background: EIH, local G and α) stands as derived, as do Cassini,
  Shapiro and the clocks.
- **Second order:** the ratified ½ (Mercury) belongs to the **clock** (lapse). Once clock ≠ ruler, the PSR's own curve
  is the clock's divided by X. For κ = 1 the ruler is 1/(1 + ϱ)² = 1 − ε + ¾ε², so the PSR's second-order coefficient
  becomes ¾ (rulers; unmeasured in the solar system). R-PSR-LAW-LOG would then be restated as the clock law.
- **The count (4368)** follows the ruler: n ∝ (1 + ϱ)⁻⁶ for κ = 1. 4365's "steady percentage" holds for neither clock
  nor ruler beyond first order at κ = 1; it was the one-PSR (κ = 0) reading.

## 4. Recommendation (PD-006; founder deferred the magnitude): working value κ = 1

**Reasons:**
- κ = 1 is inside the window.
- It is the value the corpus's GR lane already embodies throughout:
  - GR-1c's boxed exact-Schwarzschild theorem and artanh Form A;
  - AP-5's cap at clock ½, v = ⅔;
  - THEO-PCD-SEA's horizon at v = 2;
  - 3390's floor and 3702/3703's ringdown work.
- Adopting it costs nothing in the GR lane, whereas any κ ≠ 1 would require redoing all of it.
- It has a mechanism now (4377 + 4379), where before it had none.

**Its standing:** a **calibration**, like Mercury's ½ (3390), not a derivation. κ itself stays owed.

**Not registered in this patch.** Registration amends the founder's 4362 ruling at second order and restates
R-PSR-LAW-LOG as the clock law. Under PD-008 the argument first goes to a fresh critic, together with the consistency
pass in TODO-4365-THIRDORDER:
- 4364's checks re-run with clock ≠ ruler;
- 4365/4368's count curve restated;
- the floor / cap separation resolved (4373 flag);
- 4375's wormhole exterior retired;
- 4369's conditional readings closed.

## 5. PD-008

- **The convenient branch, marked:** κ = 1 because it restores GR-1c and the whole GR lane. That convenience is real
  and is the stated reason. It is not evidence that κ = 1 is what the substrate does. A derived κ could land elsewhere
  in 0.70–1.21, or outside.
- **Refused:** promoting normalisation (a) or (b) as "the" derivation because it passes.
- **No question to the founder:** he has deferred the magnitude. The remaining physics question (what sets κ in the
  PCD cycle) is Claude's work.
