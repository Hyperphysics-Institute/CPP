# Is the 18% robust? No — and the reason is better than the number. The horizon itself, expressed as a wall law at 2.734 M, has β_Kerr = −0.032 + 0.039i: its real part is the ringdown-calibrated impedance, and its imaginary part is absorption. The damping residual measures how absorbing the R-core surface is relative to a horizon: 0% (fully absorbing, indistinguishable from Kerr in the ringdown) to 18% (lossless). The theory's wall is lossy (A3′)

**Patch 3619, Session 161, 4 Sep 2026.** Founder: "we are predicting something different than GR — that seems risky; can we see whether that number agrees with GR, or if we are confident?" Verify `code/3619_lossy_wall_kerr_limit_verify.py` (5/5). Reasoning `reasoning/3619.md`.

## §1 The Kerr limit, computed properly — and it validates the machinery
A black hole is a wall law too: the log-derivative at 2.734 M of the solution that is *ingoing at the horizon*. Integrating the SN equation from `r₊ + 10⁻³` outward and root-finding with that law gives `Mω = 0.5242 − 0.0810i` — **within 0.7% in frequency and 1.3% in damping of the literature Kerr QNM.** The SN ladder, the wall placement, and the root-finder are validated against GR at the level the ringdown tests need. (3619's first attempt — "ingoing *at the wall*" — was wrong by 21%/65%: a wall at 2.7 M is not the horizon; the potential between them matters. Corrected in the same patch.)

**The Kerr point of the impedance map is `β_Kerr(ω_QNM) = −0.0316 + 0.0390i` (1/M).**

## §2 The finding
- **Real part.** `Re β_Kerr = −0.032`. The ringdown calibration (3616) gave `β = −0.025 ± 0.005` for a *lossless* wall. **The calibration recovered the horizon's real impedance.** That is a consistency the calibration did not assume: a surface at 1.33 r_S rings like a black hole only if its real impedance is the horizon's, and GW150914's ringdown says it is.
- **Imaginary part.** `Im β_Kerr = +0.039` — absorption. A lossless wall has `Im β = 0`. **The 18% damping deficit of 3618 is exactly the difference between a lossless wall and a horizon at the same real impedance.**
- **The path.** Along `β(s) = (1−s)(−0.025) + s·β_Kerr`: `s = 0` → δf −3.8%, δτ −18.5%; `s = 0.25` → −1.5%, −11%; `s = 0.5` → −1.0%, −5%; `s = 0.75` → −0.8%, −1.3%; `s = 1` → −0.7%, +1.3%. **Every point stays inside GW150914's box.** The ringdown constrains the wall's *real* impedance tightly and its *absorption* only loosely.

## §3 The answer to the founder
- The **18% is not a robust prediction.** It is the lossless-wall extreme.
- The **robust statement**: the R-core's ringdown damping is shorter than Kerr's by an amount between **0 and ~18%**, set by *how much of the wave the surface absorbs* — i.e. transmits into the core — relative to a horizon, which absorbs everything. A surface that absorbs as a horizon does is **indistinguishable from a black hole in the ringdown**; only a partially reflecting surface leaves a residual.
- The **theory's wall is lossy by construction**: under A3′ the traceless `Q_ij` content transmits into the core and returns only after the interior turn-around (3609–3610). The absorption fraction is exactly what OPEN-GR-JUNCTION-1 computes. So the theory sits *between* the lossless value and the Kerr point, and the residual is a computable number, not a free one.
- **Where the risk actually is** — and it is smaller than "we predict something different from GR": the theory predicts a ringdown *at most* 18% shorter-lived than Kerr's, *at least* indistinguishable, and the ringdown measurements already sit inside that range. What would falsify the surface is a measured τ₂₂₀ *longer* than Kerr's, or a real impedance away from −0.03 — neither of which the data show.

## §4 What this changes downstream
- 3618 §4 ("the R-core predicts τ ~18% shorter") is **restated**: 0–18%, absorption-dependent; the V2.0 paragraph carries the restated form.
- The calibrated lines (159 / 255 Hz) were computed with the lossless β = −0.025; with the Kerr-point impedance `β_Kerr` they move slightly (the real part −0.032 vs −0.025 is inside the band; the loss broadens them). **The prediction to write is the line set along the path**, with the lossless and horizon-equivalent ends as the bracket — computable now, one root-find per line per end.
- The impedance map gains its most important marked point: **the black hole itself**, at `−0.032 + 0.039i`.

## §5 Next
Compute the (2,−2) and (3,−3) lines at the horizon-equivalent end (`β_Kerr(ω)`) and at the midpoint; V2.0 carries the bracket. Then JUNCTION-1 places the theory on the path.
