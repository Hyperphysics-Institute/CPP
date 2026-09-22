# The Inheritance Model Reproduces the Pure-GT Limit Exactly, and Fails Where the Channels Must Interfere

**Patch:** 4206. **Lane:** EW. **Session:** 236.
**Verify:** `series_standard_model/code/4206_inheritance_correlations_full.py`.
**Works:** the averaging owed at 4205. **Result:** the refill bias f cannot rescue A, because A does
not depend on it; what is missing is coherence between the two refill senses. Nothing adopted.

---

## 1. Rows verbatim (D-11)

```
                                                   a       A       B
SM, measured lambda                           -0.107  -0.119  +0.987
SM, pure GT limit                             -0.333  -0.667  +0.667
SM, pure Fermi limit                          +1.000  +0.000  +0.000
model, SU(6) P=5/6, pure GT (g=1)             -0.333  -0.667  +0.667
model, SU(6) P=5/6, pure Fermi (g=0)          +0.333  -0.667  -0.667
model, SU(6) P=5/6, g=0.83 (measured GT fraction)  -0.220  -0.667  +0.440
model, P=0.71, g=0.83                         -0.220  -0.420  +0.277

Pure-GT limit: model = SM exactly, all three coefficients, with the SU(6) d-quark polarisation 5/6.
Pure-Fermi limit: model a=+1/3, A=-2/3, B=-2/3 vs SM a=+1, A=0, B=0 -- the model assigns each lepton
a definite spin along s inside what must be a singlet; and the measured A needs the Fermi-GT
INTERFERENCE term (+0.434 of the SM's -0.119), which classical channel probabilities cannot produce.
```

## 2. The result I like — flagged as such (PD-008)

**In the pure Gamow–Teller limit the model gives a = −1/3, A = −2/3, B = +2/3 — the Standard Model's
values, exactly, all three** — using only the SU(6) d-quark polarisation 5/6, the ejection rule at
full helicity, and the antineutrino's spin = +s. Nothing was fitted. This is a test the model was
not built for, and it passes it in the channel that is 83% of neutron decay.

## 3. The failure, located precisely

- **A does not depend on the refill bias.** The electron's spin is inherited before the refill
  happens, so 4205's hope — that averaging over channels with f would shrink A — was wrong.
  **The two open items are not one item; the persistence question does not bear on A.**
- **The Fermi channel is wrong in kind.** The model gives a = +1/3, A = −2/3, B = −2/3 where the SM
  gives +1, 0, 0. The reason is structural: in the Fermi channel the lepton pair is a **singlet**,
  and a singlet does not give either lepton a definite spin along s. The model's semi-classical
  assignment (electron +s, antineutrino −s, each ejected along its own spin) is exactly what a
  singlet forbids.
- **The measured A needs interference.** SM: A = −0.553 (pure GT²) + 0.434 (Fermi×GT cross term).
  The cross term exists only if the two refill senses are **amplitudes of one event**, not
  probabilities of two. The founder's own phrase — *one event, two outcomes* — is right; the model
  as I wrote it made them classical alternatives.

## 4. What this asks of CPP

The corpus already has the object that turns classical alternatives into interfering ones: **c03
derives the Born rule from the 12-edge selection statistics under ZBW fluctuation.** The question is
whether the refill — a Sea DP pulled into the core's ZBW orbit — is one 12-edge selection whose
*sense* is undetermined until the ejection resolves it, so that the two senses carry a relative
phase. If c03's mechanism does that, the interference term is derivable and A is a prediction. If
the refill sense is fixed at capture, the model is stuck at the pure-GT column. **Not attempted.**
The Fermi-limit failure would be repaired by the same coherence: a singlet is what two opposite
senses look like when they are amplitudes.

## 5. PD-008

Convenient branch: none, unless "it reduces to c03" counts as one — it hands the problem to a
mechanism already on file rather than a new one. Attack: §2's exact match uses maximal helicity
bias h = 1 for both leptons (the SM gives the antineutrino h = 1 and the electron −β; at β → 1 the
same); a critic should check that the factor-of-3 conventions (X = 3⟨cos⟩) are the standard ones.
