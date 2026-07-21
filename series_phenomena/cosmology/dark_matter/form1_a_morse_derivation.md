# FORM-1 Agenda A — the Morse-form derivation: VERDICT A-CLASS — the FORM CLASS is derived (Morse forced by quadratic registration energy + exponential amplitude screening, conditional on two named structural conditions); the WIDTH remains instrument-level with two zero-parameter lattice candidates registered; the §4 exhibits answered at the pre-registered qualitative level

**Patch 2659, 20 July 2026. Derivation under charter v1.1 Agenda A (spine item
6; Seats 1/2 demand at 2617). Inputs closed per charter §6: the registered
pins only — E_qq = α_s·ℏc/d [1812], d = 1.15 fm [2433 strong-SSV-set],
ℓ_unit = 0.589 fm and ℓ_edge = ℓ_unit/φ = 0.364 fm [SS-2], κ_q = 132 [SF-6].
Verify: `code/2659_form1_a_widths.py` (registered-constant arithmetic only).
No fit anywhere in this patch.**

## 1. FA-1 — the form-class theorem (conditional; the SS-9 conditional-closure pattern)

Let f(r) ∈ [0, ∞) be the pair's **registration amplitude** — the fractional
bond-polarization overlap of the two qCPs' Sea-polarization structures, with
f = 1 at full registration (the strong-SSV-set distance d [2433]) and f → 0
as r → ∞. Two structural conditions, named and carried:

- **FA-C1 (quadratic registration energy):** the pair-bond energy is
  quadratic in the registration amplitude with its minimum at full
  registration: U(f) = E_qq·[(1 − f)² − 1]. This is the unique quadratic in
  f with U(1) = −E_qq, U(0) = 0, and a quadratic cost for over-registration
  (f > 1, compression past the SSV-set distance) — harmonic response of the
  polarization medium about its registered configuration.
- **FA-C2 (exponential amplitude screening):** the registration amplitude
  decays exponentially in separation beyond a screening length ℓ:
  f(r) = e^{−(r−d)/ℓ}, continued to r < d (over-closure drives f > 1).
  Exponential decay is the generic response of a gapped polarization medium
  (the DP Sea is gapped by the pair binding); ℓ is the Sea's polarization
  screening length.

**FA-1 (theorem, conditional on FA-C1 ∧ FA-C2):** the qCP–qCP static strong
interaction is EXACTLY the Morse form, U(r) = E_qq·[(1 − e^{−β(r−d)})² − 1],
with β = 1/ℓ — depth pinned at the registered E_qq, minimum pinned at the
registered d, and the repulsive core arising as the quadratic
over-registration cost rather than as an added term. **The 2584-lineage
"Morse FORM convention" (ENDBOND-1's form gap) is hereby a derived CLASS
conditional on FA-C1/FA-C2, no longer a bare declaration.** What FA-1 does
NOT deliver: FA-C1 and FA-C2 from the axiom set (they are structural
conditions at the SS-9 C5–C8 register, individually attackable), and the
value of ℓ.

## 2. FA-2 — the width: instrument-level, with two zero-parameter lattice candidates registered (neither promoted)

β = 1/ℓ with ℓ a Sea screening length. The registered lattice content offers
exactly two zero-parameter candidates (verify script, registered constants):

  βd = d/ℓ_unit = **1.953**  (ω = 1.70 c/fm)  — per-unit-cell attenuation
  βd = d/ℓ_edge = **3.159**  (ω = 2.75 c/fm)  — per-edge attenuation

**Observations registered without claim:** (i) the SOFT bracket member
βd = 2 coincides with d/ℓ_unit to 2.4% — the registered soft width is,
numerically, the unit-cell screening candidate; (ii) diagnostic-grade only
(the onset window derives from quarantined widths and stays quarantined):
the two candidates STRADDLE the 2658 chaos-onset window ω ∈ (2.18, 2.61) —
the unit-cell candidate sits on the regular side, the edge candidate on the
chaotic side, so the candidate identification is not a bookkeeping choice:
the two candidates predict qualitatively different schedule physics.
Discriminating FA-C3 (which attenuation step the substrate takes) is the
named successor; nothing tonight licenses a pick. **The width bracket
{2, 4} therefore remains the instrument-level registration, now understood
as bracketing both lattice candidates.**

## 3. FA-3 — the §4 exhibit set, answered at the pre-registered qualitative level

1. **Stiffness as the thrice-recurring axis:** under FA-1 the form has ONE
   shape parameter, β; every stiffness-gated exhibit (2626 deposit
   sensitivity, the 2629/2658 schedule boundary, the 2638/2644 walls) is
   gated by ω ∝ β. The derivation names the family's discriminating axis as
   the form's single free scale — and 2658 supplies the axis its mechanism
   (chaos onset in ω). ANSWERED-AT-STRUCTURE.
2. **Steep-only walls:** marginal-aim capture requires the well to absorb
   transverse error; spatial forgiveness scales as 1/β (verify script: the
   registered analytic wells' 4.5D/2.5D = 1.8× matches the 1/β class 2×).
   The derived class predicts walls appear above a critical β and not below
   — the drawn steep-only structure in kind. CONSISTENT; which side the
   physical width falls on awaits FA-C3.
3. **The two-class face map:** the derived form is pairwise-universal —
   face-family structure cannot come from the form and must be bond-network
   geometry. Prediction of the class: face classes REPLICATE across widths.
   The exhibit shows exactly that (2644: second-decimal replication across
   widths and faces). **PRODUCED — the width-replication of the face map is
   the pairwise-universality signature, and the exhibit already exhibits it.**
4. **Wash-out/wall reconciliation:** under the form+sink decomposition
   (FA-1 + the 2655 FB-T1 transfer channel), reach at generous aim is
   DISSIPATION-limited (sink property — width-insensitive) while walls at
   marginal aim are FORGIVENESS-limited (form property — ∝ 1/β,
   width-split). The two-regime structure the 2644 §3 pre-writing demanded
   is produced by the decomposition itself. **PRODUCED.**
5. **Funnel boundary:** the OFF baseline is the form's analytic reach
   (∝ 1/β class); the ON reach is sink-mediated and washes the factor-2
   well difference out (2642) — the same decomposition, restated in data it
   was never fitted to. CONSISTENT.

## 4. Standing

**Agenda A verdict: A-CLASS** (sub-case registered by name per charter §5):
form-class derived conditional on FA-C1/FA-C2; width instrument-level with
FA-C3 as the named successor; exhibits 3 and 4 produced, 1 answered at
structure, 2 and 5 consistent. DEP-1 "Morse MED" row conversion executes at
the composite patch, same font. No fence moves; no consumer sentence rides;
quarantines carried; **79.5% untouched.** Reasoning: `reasoning/2659.md`.

---

## PANEL AMENDMENT (Patch 2664, additive; CONV-001 returns on the 2663 packet, Q1a ADOPTED-AMENDED 5–0)

A-CLASS is restated: **the Morse form is derived as the unique result within
the registered quadratic-registration and exponential-screening ansatz.** The
derivation does not establish that nature must use either ansatz. FA-C1's
uniqueness clause is completed: U(0) = 0, U(1) = −E_qq, U′(1) = 0, positive
curvature at f = 1, quadratic over-registration cost; harmonic response
motivates the quadratic locally near f = 1 only — the global extension is a
structural assumption. **THE 2664 RIDER (mandatory):** every Morse-class
consumer sentence carries: "conditional on FA-C1 and FA-C2, structural
conditions at the SS-9 C5–C8 register, neither yet derived from the axiom
set." Sea-level successor for FA-C2: FA-SEA-GREEN (see
`conv001_2026-07_form1_packet_returns_adjudication.md` §6). Nothing above this
line is edited.
