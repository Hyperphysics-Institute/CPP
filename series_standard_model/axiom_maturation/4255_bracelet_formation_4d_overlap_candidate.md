# The (E/m_W)² Bracelet-Formation Amplitude: a 4D-Overlap Candidate That Has the Shape and Not the Coefficient

**Patch:** 4255. **Lane:** EW. **Session:** 238. **Works:** 4233's target; TODO-4251-LIFETIME. **Registers:**
CAND-EW-4DOVERLAP-4255 (candidate, not adopted).
**Verify:** `series_standard_model/code/4255_bracelet_formation_4d_overlap_candidate.py`.

## 1. Searched first (D-1, D-10)

SF-2 says the virtual bracelet *"forms transiently from the DP Sea"* (§5.7.1 steps, and "6 hDPs assembled from DP Sea
fluctuations" for colliders) and gives the activated W⁰'s *decay* width (Prop. lifetime, Γ ~ m_W e⁻ᴺ, N ≈ 3.5 calibrated) —
but no rule for the *formation* probability at low energy. That absence is what 4233 named as the sector's missing input.

## 2. The candidate

In the Standard Model form the neutron's per-cycle decay probability is P = 2π[g⁴|V|²(1+3λ²)f/64π³] (m_e/m_W)⁴ (m_e/m_const):
the fourth power is the squared W propagator, the m_e⁵ is phase space at the Q-value scale. **Candidate CPP reading:** the
600-cell substrate is 4-dimensional, and the probability that the released pair's wave (4-extent λ = ħc/E) coheres with
the bracelet's zero-gradient pocket (4-extent ħc/m_W) is a 4-volume ratio, **(E/m_W)⁴** — the propagator squared as a
4D overlap. In this reading the bracelet's geometric ring (0.346 fm, 4251) is the *trap* and its Compton pocket is the
coherent *core* where the reset acts; 4229's 0.0025 fm returns in that role only.

## 3. Rows verbatim (D-11)

```
per-cycle decay probability (4233): P = 1.444e-26
  4D overlap with E = m_e         : (E/m_W)^4 = 1.633e-21;  P / overlap = 8.843e-06;  x (m_const/E) = 5.417e-03
  4D overlap with E = Q (n-p-m_e) : (E/m_W)^4 = 8.959e-21;  P / overlap = 1.612e-06;  x (m_const/E) = 6.453e-04
  -> with E = m_e, P/(E/m_W)^4 = 8.8e-6 = (m_e/m_const) x 5.4e-3; with E = Q, 1.6e-6. Neither leaves O(1): the candidate has the
     SHAPE of the target (a lepton-scale energy to the fourth over m_W) and the coefficient 5e-3 is not supplied.
  the SM's own coefficient in this form: g^4 |V|^2 (1+3 lam^2) f / (64 pi^3) = 7.462e-04  (g^2 = 0.397) -- the weak
     coupling squared, times the f/(64 pi^3) phase-space normalisation: in CPP these would be the bracelet's own coupling to the
     released pair and the 4D phase-space measure. Not on file.

status: candidate registered (CAND-EW-4DOVERLAP-4255); not adopted. Needs: (i) a substrate statement that coherence over a 4-volume
gives an overlap probability; (ii) what supplies the g^4-scale coefficient; (iii) a picture ruling on whether the bracelet forms by
Sea chance (E-independent) or is pulled together by the process (E-dependent).
```

## 4. What it gives and what it does not

It gives the **shape** — a lepton-scale energy to the fourth power over m_W, times the ZBW-cycle fraction m_e/m_const
— with nothing fitted. It does **not** give the coefficient: 5×10⁻³ remains, which in the SM is g⁴f/(64π³), the weak
coupling squared times a phase-space normalisation. In CPP those would be the bracelet's coupling to the released pair
and the 4D phase-space measure — neither on file. And the reading itself needs a substrate statement that coherence over
a 4-volume gives an overlap probability, which no axiom or theorem currently makes. **Registered as a candidate;
TODO-4251-LIFETIME stays open with the candidate named as its first test.**

## 5. PD-008

Convenient: adopt the candidate — it is elegant and reproduces the SM's structure. Refused: it lacks its coefficient by
two to three orders and its central step is unsupported by the axioms. Recorded so the next window tests it rather than
rediscovers it.

## 6. Handed up (PD-006(a), one picture)

**When a virtual W⁰ appears beside a quark for a Moment, does it come together by chance — six hDPs of the Sea happening
to fall into the hexagon, regardless of what the quark is doing — or is it pulled together by the quark's own
gradient, so that the energy the process has available decides how often it forms?** If by chance, the formation rate
cannot depend on E and the (E/m_W)⁴ must live entirely in the capture; if pulled, E enters at formation, which is where
the candidate puts it.
