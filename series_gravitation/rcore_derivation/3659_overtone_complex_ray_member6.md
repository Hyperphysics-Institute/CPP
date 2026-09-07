# The ℓ = 2 first overtone computed with a COMPLEX-RAY instrument (validated on Leaver's 0.34671 − 0.27391 i to five figures; the very-broad-mode instrument 3359 §5 registered as open is DISCHARGED at a = 0): H-SURFACE-IMPEDANCE member 6 is INSIDE GW250114's overtone box (δf −11.9% against a ±30% box; damping unconstrained by data) and FAR FROM GR (−11.9% / −25.2%) — descriptive at the data's precision, the group's worst member against the theory; the damping residual is s-independent, so it is not the number. The ringdown box RE-CUT to GW250114: δf ± 2.4%, δτ (−15, +17)% at χ_f = 0.68

**Patch 3659, Session 164, 7 Sep 2026.** Verify `code/3659_overtone_complex_ray_member6_verify.py` (7/7; run from the repo root; ~4 min). Reasoning `reasoning/3659.md`. Data searched before scoring (BLOCKING 3): LVK, *GW250114: Testing Hawking's Area Law and the Kerr Nature of Black Holes*, PRL 135, 111403 (2025), DOI 10.1103/kw5g-d732. No paper touched. CONV-042 held. Ledger row 7 and §5 updated.

## §1 The instrument
Direct inward integration on the real r* axis fails at the overtone because the ingoing contaminant grows by e^{2|Im ω|Δr*} ≈ e^{24} (3646, 3359 §4). Along the ray `r* = r*_w + t e^{iθ}` the outgoing solution's modulus is `e^{−t(ω_R sin θ + ω_I cos θ)}`: for `θ > arctan(|ω_I|/ω_R)` (≈ 38° at the overtone) it grows toward the wall and the contaminant decays — inward integration is stable. The horizon side is the reflected ray `r* = r*_w − t e^{iθ}` (Re r* → −∞, ψ → e^{−iωr*}); same θ, same stability. The ODE runs in t with complex r as a state (dr/dr* = 1 − 2/r); the Zerilli potential is analytic; the path avoids r = 0, 2; the outgoing series is fitted at complex points on the ray; θ = 60°.

Validation, before any hypothesis number: the ray returns to the real wall to 8e−15; the fundamental reproduces 3644's real-axis poles (horizon law 0.37367 − 0.08896 i, hypothesis 0.3656 − 0.0848 i to 5e−5); **the overtone via the horizon-equivalent law is 0.34671 − 0.27391 i — Leaver's value to five figures**; θ = 50°/70° and far-end 50/70 M agree to 1e−11. **The very-broad-mode instrument (3359 §5, "Q ≲ 1.5 needs a Leaver-type series or a Riccati/contour formulation") exists at a = 0.** The same ray applies to the SN equation at Kerr (F, U analytic; r carried as a state) — 3359's (2,+1) "NOT LOCATED" and 3358's withdrawn scalar comparator are now reachable; not run here (out of scope for the hypothesis; registered as the next use).

## §2 Member 6 — the overtone, s = 3.218 unchanged
| | ω (M = 1) | vs GR (Leaver) | @ 62.7 M☉ |
|---|---|---|---|
| GR n = 1 | 0.34671 − 0.27391 i | — | 178 Hz, γ = 887 Hz |
| **hypothesis** | **0.3055 − 0.3659 i** | **δf −11.9%, δτ −25.2%** | 157 Hz, γ = 1185 Hz |

The horizon seen from 8M/3 at the overtone frequency: `β_hor(ω₂₂₁) = −0.418 + 0.307 i` — not an admittance at all (the fundamental's is +0.009 − 0.116 i); the re-read pin there would be 1.4. s-sensitivity: δf runs −18% (s = 2) → −6% (s = 8) while **δτ sits at −25% for every s** — the overtone's damping residual is not the impedance number.

**Against the data (GW250114, the only overtone measurement with a Kerr-deviation test):** δf₂₂₁ = 0.1 ± 0.3 (log; 90%), δγ₂₂₁ uninformative → frequency box (−18%, +49%), no damping box. **Member 6 is inside the box.** Honest reading: descriptive at the data's precision, not at GR's — the fundamentals sit 1–2% from GR, the overtone 12%/25%. Under rule 6 it counts as a member that did not fail; it is the group's weakest and it will fail the first overtone measurement that constrains damping to better than ~25%. Both facts are recorded.

## §3 The ringdown box re-cut (handover item 2)
GW250114 (PRL 135, 111403): M_f = 62.7 +1.0/−1.1 M☉, χ_f = 0.68 ± 0.01; single-mode from 10.5 t_M: f₂₂₀ = 247 ± 6 Hz, γ₂₂₀ = 221 +39/−32 Hz; two-mode from 6 t_M: f₂₂₁ = 249 +8/−9 Hz, γ₂₂₁ = 708 +116/−107 Hz (Kerr-parametrized); deviation test as above. **Fundamental box: δf ∈ (−2.4, +2.4)%, δτ ∈ (−15, +17)%** — replaces GW150914's (−4.8, +6.3)% / (−22, +24.4)% (3616) as the lane's pinned empiric for the (2,2) fundamental at χ ≈ 0.68. For scale only (the box is Kerr's, the members a = 0): all five a = 0 fundamentals (even ℓ = 2, 3, 4; odd ℓ = 2, 3) sit inside a box of that shape. The Kerr member does not exist (3657), so the re-cut box discriminates nothing for this hypothesis; it is the box for whatever law meets 3657 §4's Kerr requirement (|R| = 0.71 at −17°).

## §4 Standing
- **H-SURFACE-IMPEDANCE: 5/6 computed members** — ℓ = 2, 3, 4 fundamentals and the static Love number descriptive at the percent level; overtone inside the data box at the ±30% level, −12%/−25% from GR; Kerr (2,2) FAILS (3657). Never adopted; s `UNEXPLAINED`.
- **New instrument, registered:** the complex-ray solver (`code/3659_*`: `wall_values_ray`, `beta_horizon_ray`) — Layer-1 reusable, catalog-first-then-cite at next use (methods catalogue entry owed with the SN version). Discharges 3359 §5's open instrument at a = 0; the Kerr (2,+1) comparator and 3358's ordering test are its next use.
- **Box re-cut:** GW250114 fundamental box as §3; PRED-O-39's box statement is owed the amendment at V2.3 (with the rest of the 163/164 package), not patched here.
- Remaining on the lane (ledger §5): odd-sector re-run at 8M/3 with J = 32/9 (item 4); closure-interior stability record (item 5); V2.3; CONV-042 re-cut. KERRWALL-1b literature-bound.
