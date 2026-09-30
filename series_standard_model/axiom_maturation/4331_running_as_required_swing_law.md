# T1 Made Quantitative: the Running of α Requires the Swing to Shorten by PSR/(3π) per e-Fold Inside the Electron's Polarisation Cloud, Starting at c04's Cloud Diameter

**Patch:** 4331. **Lane:** EW → foundations. **Session:** 241.
**Verify:** `series_standard_model/code/4331_running_as_swing_law.py`.
**Owed by:** 4326 T1 (the stress law for L against QED's logarithm). **No founder input this patch** (queued; PD-006).

## 1. The required law (rows)

With α = PSR/(2L) (4330), the measured running fixes how the swing must shorten as a charge is probed closer. At
leading log, 1/α(Q) = 1/α₀ − (2/3π) Σ_f N_c Q_f² ln(Q/m_f) for Q above each fermion's mass, and a probe of momentum
Q resolves distances r ~ ħ/(Qc). So:

  **dL/d ln r = (PSR/3π) · Σ_{f : r < λ̄_f} N_c Q_f²**

**Inside each charged species' reduced Compton length, the swing shortens by PSR/(3π) × N_c Q_f² for every factor of e
closer.** For the electron alone that is 0.106 PSR per e-fold:

```
   r / lambdabar_C     1/alpha (e only)   L (PSR)
        1.000e+00          137.036     68.518
        1.000e-01          136.547     68.274
        1.000e-02          136.059     68.029
        1.000e-03          135.570     67.785
leptons only, to the Z (the hadronic part is taken from data in QED, not from this formula):
   1/alpha(M_Z) leptonic leading log = 132.20  (measured, all species, MS-bar: ~127.95)
   L(M_Z) = 66.10 PSR from leptons; 63.98 PSR with the measured value
```

## 2. Where it starts: c04's cloud

QED's electron running starts at r ~ λ̄_C. c04 puts the electron's eDP polarisation cloud at radius r_th = λ̄_C/2
(c04 eq. rth), a diameter of λ̄_C. So **the swing must start shortening where a probe enters the electron's polarisation
cloud**, the charge-stressed (SSV_net) region, and shorten logarithmically deeper in. That places the founder's 4327
split (SSV_net moves the DP-arcs) where it has to act: inside the cloud.

The match of onset scales is order-of-magnitude only: QED's logarithm carries O(1) constants in its argument, so "λ̄_C
versus the cloud's diameter" is an alignment of scales, not a factor-2 prediction.

## 3. What the DP-arc stress model must now deliver

A candidate stress law for the swing counts as passing T1 only if it gives:

1. no shortening outside the cloud (r > ~λ̄_C);
2. a shortening **logarithmic** in depth inside it, at **PSR/(3π) per e-fold per unit charge** (N_c Q_f² for other
   species); and
3. additivity over species, each switching on inside its own Compton length.

The second item carries the teeth: a power law (for example, a shortening ∝ SSV_net ∝ 1/r²) would fail. A logarithm
arises naturally from **scale-free, layered screening**, equal contributions from every shell of the cloud when
counted per e-fold. In the founder's picture that would mean each layer of the eDP cloud screens the same fraction per
factor of distance.

## 4. What I think

This turns T1 from a sign into a sharp, falsifiable requirement, and it fits the founder's picture at the right place:
the running begins at the electron's polarisation cloud, which c04 already places at the right scale. Whether the DP-arc
dynamics produce a logarithm with coefficient 1/(3π) is now a well-posed question for the cloud's layered structure.
Nothing is derived here; the law is read off QED.

## 5. Founder question (a physical picture)

**Inside an electron's polarisation cloud, does each layer screen the same share, however far in?** α grows as you
probe closer to an electron, and in the swing picture that means the Planck ZBW's swing gets shorter in the same small
step (about a tenth of a PSR) every time the distance to the electron is cut by a factor of about 2.7. That is the
pattern of a cloud in which every layer, near or far, contributes equally per factor of distance. Is that how you
picture the eDP cloud's layers?

## 6. PD-008

- **Convenient branch, marked.** "The onset matches c04's cloud" is an order-of-magnitude alignment (QED's log has O(1)
  constants); it is not claimed as a factor-2 match.
- **Solid:** the required coefficient PSR/(3π) per e-fold per unit charge (read off leading-log QED with α = PSR/(2L));
  the leptonic leading log to the Z (132.2), with the measured 127.95 including hadrons.
- **For the critic in the next window:** whether α = PSR/(2L) should be matched to the MS-bar or on-shell running.
- **Checked here (D-1): no registered screening law.** c04, SF-6 and c06 contain no logarithmic or layer-by-layer
  screening statement; the corpus's only "vacuum polarisation" mentions are in the dark-matter lane (DM-1 corona,
  CONJ l.303) and concern bound eDP creation, not charge screening.
