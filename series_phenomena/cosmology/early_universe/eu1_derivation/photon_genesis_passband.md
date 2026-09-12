# OPEN-EU-PHOTON-GENESIS-1 worked as far as the corpus allows — **the condition becomes a one-line relation between two unknowns, and the corpus fixes one side of it.** Under the founder's picture the energy ratio is anchored at α_s/α = 2.70; the pass-band then requires the unpaired-inventory exponent to sit near **p ≈ 0.35 ± 0.13** (linear release) or **0.45 ± 0.13** (pair-statistics release). **Both textbook endpoints fail — p = 0 by ~3×, p = 1 by ~5× — but neither by the 30× of 3908.** Composition also contributes **17–23% of ζ**, which C-5's amplitude accounting must carry.

**Patch 3936, Session 226, 11 Sep 2026. Lane: EU.** Verify `scripts/3936_photon_genesis_passband.py` (8/8). Reasoning `reasoning/3936_photon_genesis_passband.md`. Inputs are all corpus (3908, 3902, founders_vision 0672a §6c); **no new constant, no rate computed** — NB-S3a-1 (the unregistered pairing-kinetics framework) is respected, not worked around. **C-5 remains a conditional pass. Nothing is reported as working. PRED-C-96, T-1, T-2, the count law: untouched.**

## §1 Set-up, in the founder's picture as agreed this session
Photon energy at reheating is released by qDP-entity collisions and binding, thermalised into the bath; photon number is not conserved, so a region's radiation entropy is fixed by the energy it releases: s ∝ E^{3/4}. Baryons are the unpaired +qCP residue (S3-M1): n_B ∝ n_q^p, **with p unknown** — the pairing kinetics that would fix it are not on file (S3a Route α, NB-S3a-1). Composition fraction q = n_q/(n_q+n_e) = ½ (the eDP:qDP = 1:1 lock, an equilibrium statement in the founders_vision register). A Hubble-scale composition fluctuation S = δ ln(n_q/n_e) = 1.36×10⁻⁴ (3908) at fixed total gives δ ln n_q = (1−q)S.

Two release models bracket the picture. **Linear:** each CP releases e_q or e_e, so δ ln E = q(1−q)(ε−1)/[(1−q)+qε]·S with ε = e_q/e_e. **Pair-statistics:** the strong channel opens only when both partners are q (3902 §1), so with random pairing the q-side enhancement enters as q²: δ ln E = 2q²(1−q)(ε−1)/[1+q²(ε−1)]·S. Under 3902's coupling structure **ε = α_s(M_Pl)/α = 2.70** — the corpus's own number for the q-side/e-side release ratio, if what is released is binding energy at the coupling. (If the bath comes instead from entity *collisions* weighted by species mass, ε is larger and unanchored; §3 covers that limit.)

## §2 The condition (verify T2–T5)
The baryon isocurvature is S_B = δ ln(n_B/s) = S·[(1−q)p − ¾·c_E], with c_E = δ ln E/S from §1. Planck's β ≲ 0.04 (3908's "few percent"; β = S_B²/(S_B²+ζ²)) gives |S_B|/ζ ≤ 0.204, i.e. **|½p − ¾c_E| ≤ 0.0675.** 3908 is reproduced as the p = 1, c_E = 0 corner (β = 0.90, T3).

| release model | c_E at ε = 2.70 | **pass-band in p** | p = 0 | p = 1 |
|---|---|---|---|---|
| linear | 0.230 | **[0.21, 0.48]**, centre 0.35 | fails 2.6× (β = 0.21) | fails 4.9× (β = 0.50) |
| pair-statistics | 0.298 | **[0.31, 0.58]**, centre 0.45 | fails 3.3× (β = 0.31) | fails 4.1× (β = 0.41) |

> **C-5 passes adiabaticity iff the unpaired +qCP inventory scales with local qCP density as a power between roughly ⅕ and ⅗** — sub-linear, but not density-independent. That is the whole content of OPEN-EU-PHOTON-GENESIS-1 once the release side is fixed at 2.70: **one number, p, which NB-S3a-1 says the corpus cannot yet produce.**

Two things the table says that were not known before it: **(i)** the founder's picture does *not* by itself secure the pass — putting release on the q side compensates only part of the baryon dependence, and full compensation needs p in the band; **(ii)** the failure at the naive endpoints is **~3–5× on S_B/ζ, not 30×** — the picture converts a certain kill into a near-miss whose resolution is a computable exponent.

## §3 How the band moves with ε (verify T7, T8)
The band is p*(ε) = 1.5c_E(ε) ± 0.135. At **ε = 1** (e-side releases as much as q-side) it requires **p ≤ 0.135** — near density-independent freeze-out. At **ε → ∞** (e-side negligible, the founder's "less frequent and less energetic" taken to the limit) it requires **p ∈ [0.62, 0.89]** — near-proportional. So the two unknowns trade off along a line, and *any* pairing-kinetics result for p will pick out the ε it needs, which is then a check against 2.70. **Two independent computations meet at one point or they don't — that is a real test, and it is registered as the closure route.**

## §4 The composition contribution to ζ — carry it (verify script)
Composition drives energy, so it is itself a curvature source: ζ_comp = ¼c_E·S = **7.8×10⁻⁶ (linear) to 1.0×10⁻⁵ (pair-statistics), i.e. 17–23% of the design ζ = 4.5×10⁻⁵.** Not double: a fifth. Whether it adds coherently to the unstacking source depends on the correlation between the two fluctuations, which 3908 noted coarse-grain identically but did not resolve. **Flag for C-5's amplitude accounting; not resolved here.** It does not touch the normalisation question (κ\*, 3906/3914), which remains as stated.

## §5 What this is and is not
- **Is:** the condition reduced to a computable relation with all corpus inputs; both naive endpoints ruled out; the pass-band stated; a closure route (independent p vs independent ε) named.
- **Is not:** a derivation of p, a claim that C-5 passes, an amplitude claim, or a rate model — NB-S3a-1 stands and Route α is not reopened from this lane.
- **Model caveats, named:** random pairing (q²) is an assumption; q = ½ is an equilibrium statement applied at reheating; s ∝ E^{3/4} assumes full thermalisation before freeze-out (agreed with the founder this session); ε = 2.70 identifies CPP's strong coupling with SM α_s run to M_Pl (3902's own caveat, inherited).
- **Wording:** C-5 conditional pass; never "the amplitude problem is closed"; the 1.0%/2.2% figures not quoted separately; 3920 not cited; no number retracted.

## §6 Standing
OPEN-EU-PHOTON-GENESIS-1 → **OPEN, sharpened**: closure = an independent value of p (requires the pairing-kinetics framework NB-S3a-1 names, a registered project in its own right, DM/FP lane) *or* an independent value of ε from a collision-channel model, checked against the band. Non-blocking. **Founder question standing (physical picture, no computation asked):** when unpaired +qCPs freeze out of pairing, does doubling the local qCP density roughly double the survivors, leave them unchanged, or something in between?
