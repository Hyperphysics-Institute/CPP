# The Corpus's Mass Calibration Against What This Session Used — Founder's Request at Close

**Patch:** 4238. **Lane:** EW. **Session:** 237 (post-close addendum).
**Founder (verbatim, 22 Sep):** *"you said there was no interpretation/conversion/CPP-calibration of 'mass'. I believe
the SM section includes such a calibration. As I recall, it was calibrated using the electron mass. It may not be what
you are looking for, or a first-principles derivation, but we should at least compare what the corpus said with what
we derived in this session."*
**Verify:** `series_standard_model/code/4238_mass_calibration_comparison.py`.

## 1. He is right, twice

My 4232 first draft said the corpus had no statement locating mass. The absence gate failed it and the unscoped
search found **c04**, the mechanism: rest mass is the energy of one Compton ZBW cycle of the polarization cloud,
mc² = hν_C. What I did not then say — and the founder is pointing at — is that the corpus also has the **calibration**:
**one dimensionful constant, m_e** (SM-2/SM-6; SF-3 Route A derives the heavy quark masses from m_e, the 600-cell
and SU(3) with no parameter fitted, RMS 2.1%, m_c predicted), and **SS-2 derives m_const = 312.7 MeV**, the free-cage
constituent scale, from which r_ZBW = ħc/m_const = 0.631 fm follows (glossary). Not a first-principles derivation of
mass from the axioms, as he says; but a mechanism plus a single calibration that the rest of the corpus rests on.

## 2. Comparison — rows verbatim (D-11)

```
r_ZBW from SS-2's m_const = 0.6310 fm  (glossary 0.631);  from this session's 313 MeV = 0.6304 fm  -> difference 0.10%
c04 Compton frequency nu_C = m c^2 / h = 7.569e+22 /s;  4231/4233 cycle frequency m c^2/(2 pi hbar) = 7.569e+22 /s  -> identical
energy locus: c04 puts the rest mass in the cloud's oscillation, not in any DP -> reading (alpha) of 4232, as used.
direction of inference: SS-2 derives m_const; this session took it as input and never re-derived it from r_ZBW (4188 rule kept).
electron: c04 calibrates to m_e = 0.511 MeV; 4204/4228 have the electron's rest mass established at the event as its Compton cloud forms about the captured -eCP; consistent.
```

| quantity | corpus | this session | consistent |
|---|---|---|---|
| constituent mass | SS-2 derives 312.7 MeV | 313 MeV used as input (4229, 4231, 4233) | yes, 0.1% |
| ZBW radius | glossary 0.631 fm = ħc/m_const | 0.630 fm | yes |
| ZBW cycle frequency | c04: one Compton cycle, ν_C = mc²/h | m_const c²/(2πħ) (4231 L bound, 4233 lifetime) | identical |
| where the mass is | c04: the cloud's oscillation energy | (α): stays with the core when the DP is reset away (4232) | yes — (α) *is* c04 |
| electron rest mass | c04 calibration to m_e | created at the event as the cloud forms about the captured −eCP (4204 §3, 4228) | yes |
| direction | SS-2: m_const → r_ZBW; 4188: never backwards | m_const taken as input only | rule kept |

## 3. What the comparison adds

Nothing this session derived contradicts the corpus's mass calibration, and two things lean on it: the lifetime's
per-cycle number (4233) is in c04's Compton cycles, and the energy reading (α) is c04's mechanism, not a new one.
The one thing the session *does* say about mass that the corpus did not: **the neutrino's mass is not a residue of
the quark's** (4232 — 2×10⁻¹⁰ of it); the released orbital's mass-energy was the core's configuration and stays there.
That is consistent with SF-4 (neutrino mass from cage eigenmodes) and is now stated in the EW lane too.

## 4. Correction to my own record

4232's first draft: "no corpus statement decides it" — false, caught by the gate, corrected in the shipped patch to
c04. 4232 as shipped still under-stated the calibration side; this patch supplies it. The founder's recall was right.
