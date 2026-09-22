# ONESIGN Item 5: Neutrino Handedness Passes — and the Rule Answers SF-4's Open Majorana Question

**Patch:** 4217. **Lane:** EW (cross-lane SF-4). **Session:** 236.
**Verify:** `series_standard_model/code/4217_neutrino_wrong_helicity.py`.
**Works:** TODO-4214-ONESIGN item 5. **Bears on:** SF-4 §openwork "Majorana versus Dirac character —
NOT SPECIFIED … registered as open" (lines 165, 210, 1203–1204).

---

## 1. The sign

- The antineutrino is the Sea's counter-spinning partner of a core refill (4201), label q = +1,
  ejected **along** its spin: right-handed. The neutrino (SF-2's EC criterion: a pre-existing
  orbital detaching, matter-type), q = −1, ejected **against** its spin: left-handed. **Passes**, by
  the same rule as items 1–3, with no additional input.

## 2. "Only" left-handed — the rule's β → 1 limit, rows verbatim (D-11)

```
m_nu = 0.05 eV  reactor nubar, 3 MeV          wrong-helicity fraction 7.8e-17
m_nu = 0.05 eV  beta-decay nubar, 0.5 MeV     wrong-helicity fraction 2.5e-15
m_nu = 0.05 eV  solar pp nu, 0.3 MeV          wrong-helicity fraction 7.0e-15
m_nu = 0.50 eV  reactor nubar, 3 MeV          wrong-helicity fraction 6.9e-15
m_nu = 0.50 eV  beta-decay nubar, 0.5 MeV     wrong-helicity fraction 2.5e-13
m_nu = 0.50 eV  solar pp nu, 0.3 MeV          wrong-helicity fraction 6.9e-13

SM (Dirac): wrong-helicity amplitude^2 ~ m^2/(4E^2) at these energies -- the same number.
```

The rule's wrong-helicity fraction is (1 − β)/2, which for a neutrino of eV mass and MeV energy is
10⁻¹³ to 10⁻¹⁶. So "only left-handed" is not a separate fact: **it is the pion-decay suppression of
4215 taken to β ≈ 1.** The same expression gave 0.364 for the muon and 10⁻⁵ for the positron.

## 3. What the rule says about the Majorana question

SF-4 leaves Majorana-versus-Dirac open. The ejection rule does not: **a right-handed neutrino is
not forbidden as an object — a spinning unanchored Sea DP can carry either sense relative to its
motion — it is only produced at rate (1 − β)/2, and once produced it cannot couple back to a W,
because the vertex is the acquiring or shedding of an orbital and that is handed relative to the
motion (4199 §2 item 2).** That is a Dirac neutrino with an inert right-handed partner. **A Majorana
neutrino would be its own antiparticle; under inheritance ν and ν̄ are distinguished by the event
that made them (partner of a +qCP refill versus a detaching matter-side orbital, 4209 §2), and
nothing in the rule turns one into the other.** Consequences, stated as predictions of the working
model, not of SF-4:

- **Neutrinoless double-beta decay does not occur.** GERDA, CUORE, KamLAND-Zen and successors
  should keep finding nothing. **A detection kills the inheritance model as written.**
- **Right-handed neutrinos exist as states, at abundance ~m²/4E² of the left-handed ones, and are
  sterile.** This is a mild sterile-neutrino prediction of a specific kind: no new mass scale, no new
  cage, just the wrong-helicity population of the ordinary three.

**Not a registered prediction yet.** It is a consequence of a rule that is imposed (4214) and has
passed four sign tests; registering it in `predictions.md` and SF-4 should wait for the remaining
three (items 4, 6, 7). Filed.

## 4. PD-008

Convenient branch: none — a falsifiable prediction that could kill the model is the opposite of
convenient. Attack: §3's "cannot couple back" is 4199's argument, not a computation; and whether a
detaching matter-side orbital and a freshly induced Sea partner are truly different *objects* or
only different *histories* is the question a critic should press — if only histories, Majorana is
back.
