# OPEN-GR-RCORE-3 — Leg A: Finite-ℓ Cavity Spectroscopy at χ = 0 + the Kerr Mode-Fate Reconnaissance

**Patch 3333, 21 Aug 2026 — Session 156.** Verify:
`code/3333_rcore3_legA_finite_ell_verify.py`, **9/9 PASS** (FAST subset
4/4). Charter: the founder's "proceed with the next physics on deck" —
the eikonal discharge GR-2 V1.0 names as its own dominant uncertainty.

---

## §1 THE LEG-A FINDING: at ℓ = 2, χ = 0, the eikonal echo comb does not survive — it collapses to a single top-of-barrier resonance

Frequency-domain scattering computation (validated instrument, §3):
the Dirichlet wall at the derived surface (areal 9M/4, tortoise
x_wall = −1.909) plus the ℓ = 2 barrier forms a cavity only ~3.5 M
long — too short to support a multi-mode trapped comb. The Wigner
delay τ(ω) = 2 dδ/dω shows exactly ONE prominent resonance per
parity:

| Parity | ω₁ [1/GM] | f₁ @ 62 M_⊙ | τ (lifetime) | Q = ω₁τ/2 |
|---|---|---|---|---|
| Regge–Wheeler (axial) | 0.4535 | **236 Hz** | 21.5 GM | 4.9 |
| Zerilli (polar) | 0.4513 | **235 Hz** | 19.5 GM | 4.4 |

The resonance sits ABOVE the barrier top (√V_max = 0.389): this is
top-of-barrier reprocessing, not a deep-cavity mode. Parity agreement
0.5%; TD cross-validation: an independent time-domain evolution's
late-time spectral peak lands at 0.4488 (−1.0%).

**Phenomenological restatement of the χ = 0 anchor.** The eikonal
picture "echo train with spacing Δt = (3/2 + 8 ln 2) GM/c³ =
2.15 ms" survives only as (a) the light-travel time governing the
FIRST few broadband transient bounces, and (b) the would-be comb
spacing 2π/Δω in a multi-mode limit the ℓ = 2 cavity does not reach.
The persistent finite-ℓ signature is instead **damped resonant
ringing at f₁ ≈ 236 Hz with quality factor Q ≈ 5** (bandwidth
Γ = 1/τ ≈ 48 Hz), fed by ringdown energy transmitted into the
cavity, plus the early transients. Both remain in-band.

**GR-2 V1.0 is NOT contradicted** — precisely because the CONV-033
adoptions scoped every template claim to "equatorial eikonal grade"
and named this systematic as the dominant uncertainty. The scoping
did its job on its first encounter with the finer calculation. The
GW150914-relevant question (does the LONGER Kerr retrograde cavity —
wall 2.267 M to retrograde ring 3.71 M — restore a multi-resonance
comb?) is **Leg B**, open below.

## §2 The Kerr mode-fate reconnaissance (χ = 0.68, geodesic grade)

Finite-ℓ mode barriers are spherical photon orbits at inclination
μ = m/(ℓ+½) ≈ ξ/√(ξ²+η), not the equatorial rings. Against the
θ-dependent derived surface (equator 2.267 M, pole 2.021 M):

| Mode | μ | r_sp [M] | θ_min | Verdict |
|---|---|---|---|---|
| (2,+2) | +0.800 | 2.163 | 52.7° | **FULLY-BURIED** |
| (3,+3) | +0.857 | 2.129 | 58.6° | FULLY-BURIED |
| (4,+4) | +0.889 | 2.111 | 62.3° | FULLY-BURIED |
| (2,+1) | +0.400 | 2.442 | 23.3° | EXPOSED |
| (2, 0) |  0.000 | 2.773 |  0.0° | EXPOSED |
| (2,−1) | −0.400 | 3.135 | 23.4° | EXPOSED |
| (2,−2) | −0.800 | 3.514 | 53.0° | EXPOSED |

Burial threshold **μ_crit = 0.774** at χ = 0.68. Since
μ(ℓ,ℓ) = ℓ/(ℓ+½) ≥ 0.8 for all ℓ ≥ 2, **the entire corotating
dominant (ℓ,ℓ) branch is buried** — GR-2's burial claim survives its
first finite-ℓ test, sharpened: burial is a statement about the
(ℓ,ℓ) branch, while lower-|m| prograde modes keep exposed barriers
at larger radii (different cavities, different delays). Two honest
cautions: (i) **the (2,+2) margin is thin** (μ = 0.800 vs 0.774);
(ii) **the finite-ℓ burial onset moves UP**: the (2,+2) mode buries
only for **χ ≥ 0.665** (vs the eikonal equatorial onset 0.555) —
the inclined orbit reaches latitudes where the surface sits lower.
GR-2's "buried for χ ≳ 0.55" is an eikonal-grade statement; the
mode-resolved onset is 0.665 at geodesic grade. GW150914-class
remnants (χ ≈ 0.68) remain inside the buried regime, with less
margin than the eikonal picture suggested.

## §3 The instrument, its validation, and the retracted provisional claim

Five instrument designs failed before the validated one, and the
fifth failure was itself the finding. Trail (full detail in the
script header, kept per computation-before-claims): (1) outside-in
TD burst spacing — contaminated by initial-data artifacts and QNM
ringdown, exposed by a NO-WALL control run; (2) raw-signal
autocorrelation — locks onto the carrier; (3) envelope
autocorrelation — intra-burst ringing; (4) WKB round trip at the
resonance — inapplicable, the resonance is above the barrier top;
(5) in-cavity leakage-train spacing — **failed the wall-shift test**:
its measured 7.00 GM/c³ was π/ω₁, the resonance carrier half-period,
whose match to the eikonal 7.045 is STRUCTURAL (ω₁ ≈ π/2L). **A
provisional "+1–3% finite-ℓ correction to the comb spacing" was
nearly claimed from instruments (1) and (5) and is RETRACTED here:
the corrected statement is that the comb-spacing quantity does not
exist at ℓ = 2, χ = 0.** The validated instrument — the scattering
phase δ(ω) with Wigner delay — passes the decisive test: under an
inward wall displacement δ = 2.0, the high-ω plateau grows by 4.12
vs the geometric 4.00 (3%), and is stable under grid/box refinement
(<1%).

## §4 Registry impact

- **OPEN-GR-RCORE-3: Leg A DISCHARGED** (Schwarzschild finite-ℓ
  spectroscopy, both parities, validated + cross-validated; Kerr
  mode-fate at geodesic grade). **REMAINS OPEN — Leg B:** the Kerr
  finite-ℓ computation on the retrograde cavity (comb restoration
  question; the m-resolved analog of §1), surface co-rotation
  ω(r_surf) in the boundary condition, and the Zel'dovich
  growth-time bounds.
- **PRED-O-39: refinement note flagged, NOT yet executed** — on Leg
  B, the search-target language refines from "comb at Δt" toward
  "resonance(s) near the finite-ℓ frequencies + early transients."
  No predictions.md edit until the Kerr (GW150914-relevant) numbers
  exist; the χ = 0 anchor f₁ ≈ 236 Hz is registered here unminted.
- **GR-2 amendment queue (next round/ratification, not executed):**
  §3 gains the Leg-A pointer; the burial onset sentence gains the
  mode-resolved 0.665; the thin-margin caution enters §7. All are
  additive under the existing eikonal scoping — no shipped claim is
  false as scoped.

## §5 Honest limits

Leg A is χ = 0 (the wall+barrier system exactly spherically
symmetric); the Kerr mode-fate table is geodesic/eikonal-
correspondence grade (μ-mapping approximate at ℓ = 2); the burial
verdict uses the A1–A3 surface and inherits its conditionality
(OPEN-GR-RCORE-4); resonance widths are read from the Wigner
lifetime, not a complex-pole computation; no waveform or SNR
statement is made anywhere.
