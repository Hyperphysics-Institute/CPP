# The complex ray at Kerr (METH-L1-015 on the CD Z⁺ instrument): validated on Leaver's (2,2) first overtone at χ = 0.68 to 5e−5 — and the prograde comparator (2,+1), NOT LOCATED since 3359 §4, is located on both model walls. The ordering discriminator of PRED-O-39 (e) moves from eikonal-WKB grade to exact grade for the model walls: under one wall, Q rises monotonically from prograde to retrograde — Dirichlet Q(2,+2) = 0.60 < Q(2,+1) = 0.68 < Q(2,0) = 0.81 < Q(2,−2) = 1.02; Neumann 1.86 < 2.15 < 2.63 < 3.52. The retrograde line is the sharpest and the prograde ones the broadest on either wall. Recorded as a result on MODEL walls (the two ends of the compliance family), not on a derived law.

**Patch 3672, Session 165, 7 Sep 2026.** Verify `code/3672_complex_ray_kerr_cd_zplus_21_comparator_verify.py` (9/9; exec's 3668's instrument; ~8 min). Reasoning `reasoning/3672.md`. Paper: GR-2 → V2.7 at 3673. Ledger §5 updated (the (2,+1) item struck). Methods: METH-L1-015 reused (cited at 3673 in the catalogue's reuse line); the CD Z⁺ instrument registered as a method at 3673.

## §1 The instrument at Kerr
3659's ray, r* = r*_w + t e^{iθ}, with the CD Z⁺ potential of 3668 (closed-form, analytic in r — the reason Z⁺ rather than SN carries the ray: SN's U needs a numerical derivative and is not fit for a complex path), r carried as a complex state with dr/dr* = Δ/(r²+a²), λ = A_{−2,ℓm}(aω) + a²ω² − 2amω at complex ω (Leaver's angular CF), the outgoing series fitted on the ray, the horizon side on the reflected ray with r₊ approached by the near-horizon inversion of r*(r). θ = 60°, T = 60 (out) / 40 (horizon).

**Validation (before any wall number):** the ray closes on the real wall to 4e−13 / 3e−10; the (2,2) fundamental via the horizon law = Leaver (3358's radial CF) to **1e−7**; **the (2,2) first overtone 0.51194 − 0.24653i via the horizon law = Leaver's n = 1 root to 5e−5** — Im ω ≈ −0.25 at Kerr, where direct integration stalls (3359 §4, 3646); (2,+1) and (2,−2) fundamentals to 2e−11 / 3e−11; θ/far-end independence at the overtone 8e−5. Leaver's Kerr fundamentals at χ = 0.68 for the record: (2,+2) 0.52398 − 0.08151i, (2,+1) 0.45091 − 0.08268i, (2,0) 0.3928 − 0.0848i, (2,−2) 0.31116 − 0.08875i.

## §2 The wall family on Z⁺ at r_w = 2.7344 M
Model walls — the two ends of the compliance family (3390/3391): Dirichlet Z⁺ = 0 (the even-variable node; **not** 3359's X = 0 on the SN variable, which is a different condition on a different variable) and Neumann dZ⁺/dr* = 0. Each root: residual < 1e−7, θ/T-independent to 1e−5, from a four-point guess set; the least-damped converged root reported. f at 62.7 M_⊙.

| (2,m) | Dirichlet ω, f, Q | Neumann ω, f, Q | Kerr QNM Q |
|---|---|---|---|
| +2 | 0.32222 − 0.26855i, 166.1 Hz, **0.60** | 0.41418 − 0.11146i, 213.5 Hz, **1.86** | 3.21 |
| +1 | **0.34494 − 0.25415i, 177.8 Hz, 0.68** | **0.40948 − 0.09537i, 211.0 Hz, 2.15** | 2.73 |
| 0 | 0.37903 − 0.23378i, 195.4 Hz, 0.81 | 0.40262 − 0.07647i, 207.5 Hz, 2.63 | 2.32 |
| −2 | 0.31941 − 0.15668i, 164.6 Hz, 1.02 | 0.31215 − 0.04428i, 160.9 Hz, 3.52 | 1.75 |

**(2,+1) is located** on both walls. On Dirichlet it is a Q = 0.68 feature — the broad, top-of-barrier mode 3359 §4 could not reach; on Neumann Q = 2.15.

## §3 The ordering test (PRED-O-39 (e))
Under either wall **Q rises monotonically from prograde to retrograde**: the prograde-exposed comparator is broader than the retrograde-keyed line, and (2,+2) is the broadest of all. This is the retrograde-keying *ordering* at exact grade for the model walls: the prograde modes are the ones a wall at 8M/3 cannot hold (the prograde cavity is the shallow one — 3352/3355's burial picture), the retrograde the ones it holds best. Two things this does not say: it does not fix the *values* (the wall law is not derived — the two model walls differ by a factor 3–5 in Q and 3–13% in frequency), and it does not say which line dominates (amplitudes are not computed; PRED-O-39 (d)). Note the Kerr QNMs themselves order the other way (Q_Kerr falls from 3.21 to 1.75, prograde sharpest): the wall's ordering is the wall's, not the exterior's — which is the discriminator's content.

## §4 Records
- 3359 §2's "(2,+1) NOT LOCATED — the method's limit" is discharged at Kerr by this instrument. 3359's Dirichlet (2,−2) 191.2 Hz, Q 2.09 was X = 0 on SN; it is not superseded by the Z⁺ = 0 line here (164.6 Hz, Q 1.02) — different variable, different wall; both are model walls.
- Neumann (2,−2) at 160.9 Hz sits at V2.0's retrograde line 159→162 Hz (the lossless→horizon family) — consistent, not new.
- 3358's withdrawn scalar (2,+1) stays withdrawn (scalar sector; not recomputed).
- PRED-O-39 (e): "NOT LOCATED … ordering at eikonal-WKB grade only" → located; ordering at exact grade on the model walls, values conditional on the wall law (3673).

## §5 Standing and next
- Instrument residue: the Kerr complex ray on CD Z⁺ — any wall law, any (ℓ, m), any Q; the (3,±3) and (2,±2) overtones are one call away. Registered with METH-L1-015's reuse and the CD Z⁺ method (3673).
- The lane's queue after this: the re-cut derivation question of 3670 §6 (does the cycle propagate A3′'s tensor wave as Einstein's equations do above the cap?) with OPEN-GR-CORE-DISSIPATION-1 — the physics act; and the Session-165 handover at the founder's call.
