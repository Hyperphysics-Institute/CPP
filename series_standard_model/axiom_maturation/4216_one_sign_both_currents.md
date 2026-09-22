# ONESIGN Item 3: the Neutral and Charged Currents Are One Sign — with 4197's Table Re-signed

**Patch:** 4216. **Lane:** EW. **Session:** 236.
**Verify:** `series_standard_model/code/4216_nc_cc_one_sign.py`.
**Works:** TODO-4214-ONESIGN item 3. **Amends:** the sign convention of 4197 §2 / 4198 (physics
unchanged; the weight that enters the displacement rule is −Q_W, not Q_W).

---

## 1. The two statements

- **Charged current (4201):** a lepton of label q leaves along q × its own spin. The electron leaves
  against its spin.
- **Neutral current (4196):** in the standard form H = G_F Q_W/(2√2 mc) · ½{σ·p, ρ}, an electron in
  weak-charged matter drifts along Q_W(partner) σ. A positron probe flips. So the drift is along
  **−q_probe · Q_W(partner) · σ.**

## 2. Rows verbatim (D-11)

```
charged current:  electron thrown AGAINST its spin (q = -1).
neutral current:  drift along -q*Q_W*sigma;  Q_W(neutron) = -1.000  ->  electron drifts AGAINST its spin.  SAME sign.
                  Q_W(proton)  = +0.0729  ->  along its spin, weakly (the cores win by 0.07).

so the contact weight in the displacement rule is -Q_W(partner):
   per linear oscillator (captured -eCP): +1.073    per +qCP core: -0.382
The linear oscillator -- the object the W captures -- carries the POSITIVE weight in both currents.
Caesium: Q_W measured -72.6 (negative), sign of E_PNC as predicted by the standard form: the input sign is measured, not assumed.
```

## 3. Verdict

**Passes.** In neutron-rich matter Q_W < 0, so the electron drifts **against** its spin — the same
direction the W throws it. The two currents are one rule, **displace along q × spin with a positive
weight**, provided the neutral-current weight is read as **−Q_W(partner)**: +1.073 per linear
oscillator, −0.382 per +qCP core. **4197's table stands numerically with its sign flipped**, and
the flip is the content of the test: **the linear oscillator — the very object the W captures —
carries the positive weight in both currents.** The +qCP cores oppose it, weakly; a proton's three
cores just outweigh its one oscillator (+0.07), which is why an electron drifts *along* its spin in
hydrogen and against it in everything heavier.

The input sign is measured, not assumed: caesium's E_PNC has the sign the standard form predicts
with Q_W = −72.6.

## 4. What the pass does not settle

The **mechanism** for the neutral current is still absent (OPEN-EW-NC, 4213). What this patch
fixes is the sign such a mechanism must deliver: an electron passing a linear oscillator is pushed
against its spin; passing a bare core, along it, more weakly.

## 5. PD-008

No convenient branch. Attack: §1's non-relativistic reduction γ₅ → σ·p/mc carries the sign that the
whole test rests on; the critic should re-derive it rather than take the standard form's sign from
me. Three of seven signs checked.
