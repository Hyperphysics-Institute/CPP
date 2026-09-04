# The family, gauge-free: the R-core's echo line as a function of the wall impedance β = (dZ/dr*)/Z at the ratified surface. Every gauge, dictionary and residual choice is a point on this map. Envelope at a = 0: 117–224 Hz (even), 116–239 Hz (odd) over lossless constant walls; a softer wall gives a lower, sharper line

**Patch 3613, Session 161, 4 Sep 2026.** Verify `code/3613_pole_family_over_impedance_verify.py` (5/5; 3356/3383 machinery, r_w = 8M/3). Reasoning `reasoning/3613.md`. First step of the 3612 plan, reformulated so that no gauge choice is needed to state the family.

## §1 Why the impedance, not the residual

3612 named the wall's residual gauge pattern `ρ_w` as the calibration parameter. But `ρ_w` is a coordinate object; what the exterior *sees* is one gauge-invariant number per frequency: the log-derivative of the (gauge-invariant) Zerilli / RW master function at the wall,

    β(ω) = (dZ/dr*)/Z |_{r_w}.

Every wall law the week produced — trace-Dirichlet (3378), free-surface (3391), the odd-sector interior law (3384), the C5-frame law still to be built, and any residual choice inside it — is a function `β(ω)` and nothing else reaches the poles. So **the calibration object is β(ω)**, and the *constant-β locus* is its one-parameter envelope: the map from wall impedance to echo line, with the RW-gauge laws as marked points. This is the family the founder asked for, stated in the only variable that is frame-independent.

## §2 The map (ℓ = 2, a = 0, r_w = 8M/3, 62 M_⊙)

| β (in 1/M) | even (Zerilli) pole | Hz | Q | odd (RW) pole | Hz | Q |
|---|---|---|---|---|---|---|
| ±∞ (Dirichlet, the shipped assumption) | 0.3855 − 0.204i | 201 | 0.9 | 0.4592 − 0.199i | 239 | 1.2 |
| +0.5 | 0.4291 − 0.148i | 224 | 1.5 | 0.4366 − 0.134i | 228 | 1.6 |
| +0.2 | 0.4223 − 0.102i | 220 | 2.1 | 0.4265 − 0.092i | 222 | 2.3 |
| **0 (Neumann)** | 0.3905 − 0.060i | 204 | 3.3 | 0.3933 − 0.053i | 205 | 3.7 |
| −0.1 | 0.3589 − 0.038i | 187 | 4.7 | 0.3610 − 0.033i | 188 | 5.5 |
| −0.2 | 0.3096 − 0.018i | 161 | 8.6 | 0.3105 − 0.015i | 162 | 10.5 |
| −0.3 | 0.2241 − 0.004i | **117** | **31** | 0.2220 − 0.003i | 116 | 43 |

Tracked continuously from Neumann outward; beyond `β ≈ +0.5` the lowest pole heads toward the Dirichlet value, beyond `β ≈ −0.3` into ever more deeply trapped modes (lower, sharper — the "soft wall" limit of the barrier cavity). Q rises **monotonically** as β decreases through Neumann into negative values.

**Envelope** over the tracked lossless walls plus Dirichlet: even **117–224 Hz** (Mω 0.224–0.430), odd **116–239 Hz**. **The wall impedance moves the line by tens of percent, up to a factor ~2 — not orders of magnitude.** The two sectors track each other closely for the same β (their potentials differ only in the 1/r³ term).

## §3 Where the week's laws sit on the map
- Shipped `X = 0` (GR-2 V1.6 basis): Dirichlet, 201/239 Hz, broad.
- RW-gauge free-surface (3391): `β₂(ω) = 7.6 − 55ω²` — at its own pole `β ≈ −0.1`, but with a *positive boundary mass* `b₂ > 0`, which is why its Q (99) far exceeds the constant-β line at −0.1 (Q 4.7): frequency dependence sharpens. Its position, 195 Hz, sits between the −0.1 and 0 rows.
- Registered-shear odd law (3384, J = 6.75): `β ≈ (1/J)k·g(kμ)` ≈ 0.44 at low ω, dispersive; its pole 208 Hz / Q 8 sits near the +0.2 to +0.5 rows in position but sharper for the same reason.
- The C5-frame law (to be built): unknown point; its residual `ρ_w` moves it along this map.

## §4 What the empirics bound (S-EMPIRICS-ARBITER)
The echo searches' null results bound the *amplitude* of any echo relative to the ringdown at the detected events; a sharper line (high Q) at a given reflectivity concentrates the echo's power and is more detectable in a matched search, so the null results cut most sharply against the **trapped, high-Q, low-frequency** corner of the map (β ≲ −0.2) if `|R| ≈ 1` there — that corner predicts narrow lines at 115–160 Hz that would likely have been seen. Quantifying the excluded region requires the reflectivity `|R(ω)|` on the real axis for each β and the events' sensitivities — the next step of the plan (§5).

## §5 Next
1. `|R(ω)|` on the real axis across the map (lossless walls give |R| = 1; the C5-frame two-channel wall will not) and the echo amplitude ratio → the excluded region of the map under the published limits.
2. The C5-frame wall law `β_C5(ω; ρ_w)` — placing the theory's own point(s) on the map (OPEN-GR-LATTICE-FRAME-1 in parallel).
3. Kerr: the same map at χ = 0.68 via the SN ladder with a general β (the 3392 machinery already takes an arbitrary Robin law) — a family, not an ansatz.
4. GR-2 V2.0: **the map**, with the calibration named as β(ω) and the shipped/RW-gauge points marked.
