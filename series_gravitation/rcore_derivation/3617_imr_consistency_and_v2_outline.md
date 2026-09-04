# GWTC-1's inspiral–merger–ringdown consistency test: a second, independent empirical constraint on the post-inspiral being Kerr-like (GW150914 GR quantile 55.5%; all seven events consistent). It does not sharpen the 3616 band, but it closes a loophole. And the outline of GR-2 V2.0, which the record can now support

**Patch 3617, Session 161, 4 Sep 2026.** Source: GWTC-1 TGR (arXiv:1903.04467) §IV "Inspiral–merger–ringdown consistency test" and Table III, pasted by the founder. No new computation. Reasoning `reasoning/3617.md`.

## §1 What the IMR consistency test is, and what it adds
The low-frequency (inspiral) and high-frequency (post-inspiral, `f > f_c` with `f_c` the ISCO frequency of the inferred Kerr remnant — 132 Hz for GW150914) parts of the signal are analysed *separately*; each yields an estimate of the remnant's mass and spin via NR fits; GR requires the two to agree. Table III: GW150914 (`ρ_IMR = 25.3`, `ρ_insp = 19.4`, `ρ_post-insp = 16.1`) GR quantile **55.5%**; GW170814 (`ρ_post-insp = 7.2`) 7.8%; all seven events consistent with `ΔM_f/M̄_f = 0, Δa_f/ā_f = 0`, combined posterior consistent with GR.

**What it adds to 3616.** The direct (f₂₂₀, τ₂₂₀) measurement (3616) is the sharp test. The IMR-consistency test is a *different* observable — the post-inspiral segment as a whole must yield the same (M_f, a_f) as the inspiral does — and a wall that modified the post-inspiral waveform (shifted mode, altered damping, a modified-ringdown "cavity" signature at 0.7 ms) would bias the post-inspiral (M_f, a_f) away from the inspiral's. That it does not, at SNR 16 in the post-inspiral of GW150914, is a second, independent statement that the post-inspiral is Kerr-like, and it closes a loophole 3616 left: even if the (f₂₂₀, τ₂₂₀) fit were absorbing a wall's effect into a shifted (M_f, χ_f) (Table XIII's ringdown-only `χ_f = 0.76` vs the IMR's ≈ 0.68 — a mild tension worth noting), the inspiral-vs-post-inspiral comparison would expose it. It does not sharpen the numerical band (its precision on M_f, a_f is coarser than the pSEOB box), but it makes the band's *conclusion* robust to that loophole.

## §2 The empirical picture, now complete enough to write
1. **Exterior dynamics:** GR's tensor equations — forced by the ringdown frequency itself (a scalar relay would sit 29% off; 3612).
2. **Echo searches (GWTC-2 template; GWTC-3 morphology-independent):** no evidence; no amplitude limit; windows begin *after* the ringdown; a 0.7 ms cavity is outside them by construction (3615–3616).
3. **The ringdown (GWTC-3 Table XIII):** GW150914's (f₂₂₀, τ₂₂₀) confine a wall at 1.33 r_S to a near-Neumann impedance sliver, `β ≈ −0.02 … −0.03` (1/M) at the ringdown frequency; hard and soft walls excluded (3616; edges provisional pending the pSEOB deviation table).
4. **IMR consistency (GWTC-1 Table III):** the post-inspiral is Kerr-like independently of the mode fit (this patch).

## §3 GR-2 V2.0 — the outline the record supports (draft on the founder's word)
- **Title of the section:** *The line set as a map: the wall impedance β(ω), what the ringdown fixes, what an echo would add.*
- **Surface:** areal 8M/3 = 1.33 r_S under R-PSR-LAW-LOG (Mercury-calibrated second order; founder-ratified completion).
- **The a = 0 map** (3613) and **the χ = 0.68 map** (3614): the ℓ = 2 line vs β for both sectors; envelopes 117–224 / 116–239 Hz (a = 0) and 122–188 Hz (Kerr (2,−2)); softer → lower and sharper.
- **The barrier transmission** (3614): for lossless walls the first echo is |T|² ≈ 0.44 at the ringdown frequency, independent of β.
- **The ringdown band** (3616): prograde (2,2) at χ = 0.68 vs β; GW150914's box → β ≈ −0.02 … −0.03; the V1.6 hard wall excluded; exact edges from the pSEOB deviation table when supplied.
- **The IMR consistency test** as an independent confirmation.
- **The predictions at the calibrated β:** the (2,−2) line and the ℓ = 3 line at β ≈ −0.025 (to be computed — one root-find each, both spins) — *the* V2.0 numbers, with their provenance: a wall impedance fixed by GW150914's ringdown, at a surface fixed by Mercury and the founder's clock.
- **Standing statements:** the RW-gauge laws of 3378–3391 are one gauge's model and are superseded as physics by the map; the lattice-frame (C5) law is OPEN with a numerical target and a falsifier (3616 §4); the Kerr surface radius remains the one carried assumption (ansatz A); the odd/even junction under A3′ is OPEN.
- **What an echo would add:** β's frequency dependence — the ℓ = 3 line's position relative to ℓ = 2, and the interior return.

## §4 Next (worker's)
1. The two calibrated-β predictions (ℓ = 2 (2,−2) and ℓ = 3 at both spins at β = −0.025) — the numbers V2.0 carries.
2. Draft V2.0 on the founder's word; recompile; ledger; PRED-O-39 → the map.
3. The C5-frame wall and LATTICE-FRAME-1 against the target.
