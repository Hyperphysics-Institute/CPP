# FA-SG-R1 LEG L4 RECORD — the mandatory J3 companion attack: the site-level normalization derived from the discrete-lattice Green function gives α′/α = 1.611; the charter's α^(−1/2) propagation law FAILS empirically (ℓ(α) is non-monotone, minimized at the frozen α); both propagations land outside the joint band — **J3-REVISE** — and the scan maps a three-regime structure with the frozen operating point at the staggered-evanescent minimum and a stability threshold at α_crit = 0.224 fm

**Patch 2688, 21 July 2026. Executing charter §2 R1-L4 as a derivation,
not a scan; the propagation reported explicitly, not assumed (both the
charter-stated law and the direct re-solve). Fence F1 honoured: the local
DP density n only. Verify: `code/2688_r1_l4_j3.py`. 79.5% not in scope.**

## §1 — The derivation

The frozen continuum matching is the self-consistency **α·S_cont(κ) = 1**
with S_cont(κ) = n∫d³r e^{−κr}/r = 4πn/κ² — identically α = κ²/(4πn)
(verified: 1/S_cont = 0.08193 fm = frozen α). The site-level alternative
replaces the homogenized integral with the actual z=12 lattice sum,
self-site excluded (no self-scattering), at the operating point κ·a = 2:

**α′·S_disc(κ) = 1, S_disc(κ) = Σ_{j≠0} e^{−κr_j}/r_j = 7.5761 /fm**
(converged by R = 15a), giving **α′ = 0.1320 fm, α′/α = 1.6110.**

Decomposition of the shift: the continuum core r < a contributes 59.4%
of S_cont and is excluded at site level; shell discreteness adds back
+21.5% (the 12-site nearest shell exceeds the smeared continuum tail).
The shift is therefore dominated by the physically motivated
self-exclusion, not by an artifact of the summation.

Supplementary constructions (reported, not the derivation): staggered-
sector sums at the FCC zone-boundary X and L points are small and
negative (S_X = −0.998, S_L = −0.452 /fm), giving α′(X) = 12.2α,
α′(L) = 27.0α — both EXCEED the operator stability threshold and are
non-viable as normalizations. The site-level normalization is thus
construction-dependent, with the isotropic-evanescent matching the
canonical viable construction.

## §2 — Propagation (explicit, both routes)

- Charter-stated law (ℓ ∝ α^{−1/2} through κ at fixed gap
  identification): **ℓ′ = 0.0717 fm.**
- Direct empirical propagation (re-solve the extended instrument at α′):
  **ℓ′ = 0.1679 fm**, with degraded envelope quality (log-lin R² = 0.55
  vs 0.93 at baseline) — at α′ the operator sits at 0.59·α_crit and the
  response is approaching the near-critical regime.

**The two routes disagree because the α^{−1/2} law itself fails
empirically** (§3). Under the frozen [ADJ] the verdict does not depend on
the route: joint L1/L3 band [0.0836, 0.0956] fm; scaled ℓ′ below it,
direct ℓ′ above it. **VERDICT: J3-REVISE.**

## §3 — The ℓ(α) map (labeled robustness scan; axis frozen pre-run)

| α/α₀ | ℓ_env (fm) | R² | staggered? | 1/(2κ_c) (fm) |
|---|---|---|---|---|
| 0.5 | 0.2031 | 1.000 | NO (neg 0.000) | 0.1287 |
| 1.0 | 0.0914 | 0.929 | yes (0.535) | 0.0910 |
| 1.5 | 0.1437 | 0.837 | yes | 0.0743 |
| 1.611 | 0.1679 | 0.554 | yes | 0.0717 |
| 2.0 | 0.1712 | 0.843 | yes | 0.0644 |
| 3.0 | fit fails (non-decaying) | 0.154 | yes | 0.0525 |

Three regimes: **pure-Yukawa** (weak coupling — perfectly exponential,
UNstaggered, ℓ near the continuum 1/κ_c); **staggered evanescent** (the
operating point); **near-critical** (α → α_crit = −1/λ_min(G) =
0.2241 fm = 2.74 α₀; past it the resolvent loses positivity and the
response stops decaying). ℓ(α) is non-monotone with its minimum at (or
near) the frozen α₀ — where, and only where, the identity ℓ = 1/(2κ_c)
holds (OBS-class, non-adjudicative; the α-scan now shows the identity is
NOT generic in α, sharpening the N2 observation without elevating it).
This map is also the mechanism behind the J2 scan result (L1 record §4):
the J2 d_DP-decoupling points land at α/α₀ = {2.62, 1, 0.38} — the same
three regimes.

## §4 — What J3-REVISE means for the packet (and what it does not)

J3-REVISE does NOT assert α′ is correct — it asserts the panel's
suspected joint is MATERIAL: the continuum-vs-site normalization choice
propagates the readout outside its own band, and the site-level route
does not deliver a clean revised value (degraded exponentiality at α′).
The revision on offer is that ℓ is **normalization-conditional**:
ℓ(α, continuum-matched) = 0.0904 ± 0.0028 fm (clean) vs ℓ(α′,
site-matched) ≈ 0.168 fm (degraded, R² 0.55) — with the α^{−1/2}
propagation the charter anticipated now shown not to hold in this
regime. Which normalization the derivation chain actually grounds is the
panel's adjudication; the re-derivation campaign (queued behind the R1
returns) targets whichever value the panel sustains. All at observation
grade; the cap stays. **Fence audit:** clean (local n only; shell sums
converge within femtometres). Reasoning: `reasoning/2688.md`.
