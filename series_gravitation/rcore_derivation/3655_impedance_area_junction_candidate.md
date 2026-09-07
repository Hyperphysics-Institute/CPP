# OPEN-GR-SURFACE-IMPEDANCE-1 attempt 4, first step: a parameter-free candidate for s. The cap has three constants of the right size — ψ⁴ = 256/81 = 3.160 (the areal/lattice area ratio at the surface, r² = ψ⁴r̄²), J = 32/9 = 3.556, 1/N² = 4. Scored cold on ℓ = 2, 3, 4: **all three sit in the GW150914 box**; ψ⁴ is the closest to the 3644 pin (1.9%) but the present box does not single it out. Named CANDIDATE-S-AREA with its mechanism (a waveguide-area junction: the exterior wave carried on the areal sphere, the interior on the lattice sphere; R = (s−1)/(s+1) = 0.52 vs the 0.55 requirement) — a candidate, not a result. Discriminant: the damping spread (+4 / +8 / +11%) against GW250114's ringdown, which needs KERRWALL-1. The static near-coincidence with 3633 is 3%: not an identity

**Patch 3655, Session 163, 6 Sep 2026.** Verify `code/3655_impedance_area_junction_candidate_verify.py` (8/8; execs 3644). Reasoning `reasoning/3655.md`. No paper touched.

## §1 The candidates, cold
| s | ℓ = 2 (δf / δτ) | ℓ = 3 | ℓ = 4 | box |
|---|---|---|---|---|
| 3.22 (pin, 3644) | −2.2 / +4.9 | −1.4 / −1.3 | −1.0 / −5.1 | in |
| **ψ⁴ = 3.160** | −2.3 / +4.3 | −1.4 / −1.9 | −1.0 / −5.8 | in |
| J = 3.556 | −1.7 / +7.7 | −1.1 / +2.1 | −0.8 / −1.4 | in |
| 1/N² = 4 | −1.1 / +11.0 | −0.8 / +6.1 | −0.6 / +3.0 | in |

The GW150914 box (δτ ∈ (−22, +24)%) is too wide to choose. The frequencies are nearly insensitive to s; the dampings spread by 7 points between ψ⁴ and 1/N². A ringdown box at the ±3% level in τ would decide.

## §2 CANDIDATE-S-AREA
`r² = ψ⁴ r̄²` at the cap. If the exterior wave is carried on the areal sphere and the interior wave on the lattice sphere, the surface is a junction between two waveguides whose cross-sections differ by ψ⁴, with amplitude impedance ratio ψ⁴ and reflectivity `(ψ⁴ − 1)/(ψ⁴ + 1) = 0.519` — 3644's requirement was `|R| ≈ 0.55`. This is a mechanism with a corpus constant, and it ties the impedance to the same conformal factor that sets the lapse floor: one cap, one number. It is not derived from the cycle; it is named so the next tests can kill it.

## §3 The static face
Neumann on Z at ω = 0 gives `y = −2.563`; 3633's harmonic-pattern lapse reading gives `y = −2.646` (recomputed here in 3624's normalisation; the 3633 k₂ = 0.033 was the structural convention). 3% apart: **a near-coincidence, not an identity.** Recorded; not used.

## §4 Standing and next
- H-SURFACE-IMPEDANCE: 4/4 descriptive; the number now has a candidate identity (ψ⁴|cap) with a mechanism; still a hypothesis.
- **Next, in order:** KERRWALL-1 (the SN↔local-wave dictionary at the Kerr wall) — required for any Kerr test and for using GW250114's ringdown (spinning remnant, SNR 80, the tightest GR-deviation bounds from one event) as the discriminating box; then the overtone (Leaver); then 5's write-up and V2.3 carrying: [PCD-EXT] excluded as derived (3653), the surface as an impedance (3654), CANDIDATE-S-AREA (3655), GW250114 (3651).
- Session 163 has run 3643–3655; a handover is due at the next natural break (before KERRWALL-1, which is a multi-patch item).
