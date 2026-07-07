# G4 · S2-3 — the friction computation: the gate reduces to one Sea spectrum (Patch 2321, 7 July 2026)

**Campaign:** G4 Stage 2 item 3, executed under the FORK-DISS-1 D-C ruling (founder, 2320).
**Model named (condition C-g):** disorder = DP-scale occupancy fluctuations, ℓ_dis = r_c = 1.0 fm
(the founder's named generators live at DP scale), δ² = f_occ(1−f_occ) ≈ 0.09; Rayleigh-class
ℓ_mfp(k) = ℓ/((kℓ)⁴δ²); dynamic bath carries spectral factor Θ(ω) ∈ [ωτ_b, 1], τ_b = r_c/c.
**Verify:** `code/2321_g4_s2_3_friction.py` (6/6). **No resting paper touched.**

## 1. Protections shown, not assumed (spec item 1 — and the consistency triple)

- **Λ/W2:** λ⁴ transparency — ℓ_mfp(1 m EM) = 7×10⁴² m (×10¹⁵ beyond the observable universe);
  horizon mode ℓ_mfp = 7×10¹⁴⁶ m. The friction bath cannot touch IR Lorentz or DM-2's coherence mode.
- **Halo steady-state:** at Θ = 1 a comoving coat would spin down in ~3×10⁻¹³ s — a catastrophe
  that PROVES Θ(ω→0)→0 is mandatory; any physical fast bath supplies it (S(0) ≈ 2δ²τ_b, golden
  rule). The same structure that protects halos protects Λ/W2. Consistency, not tuning: the
  bath is *required* to be frequency-selective, and physics makes it so automatically.

## 2. The computation (spec items 2–3)

f(b, v) = f_geo(b, v) × Θ(ω_enc), with f_geo from the coat-maintenance broadcast (path (2b)(c/v),
scattering at k ~ 1/R_s; accounting A — the mutual-field reservoir — is dead at all anchors,
consistent with 2318):

| v | f_geo (Θ=1) | bar (E_col/E_coat) | **Θ_crit** | Θ lower bound (ωτ_b) |
|---|---|---|---|---|
| 10 km/s | ~1.9 (saturates) | 1.2–4.9×10⁻⁵ | **6.3×10⁻⁶–2.6×10⁻⁵** | 2.3×10⁻⁷ |
| 50 | 0.20 | 2.9×10⁻⁴–1.2×10⁻³ | **1.4–6.0×10⁻³** | 2.1×10⁻⁶ |
| 200 | 0.020 | 4.7×10⁻³–2.0×10⁻² | **0.23–0.98** | 2.2×10⁻⁵ |

Two structural results ride on the grid:
- **The velocity shape is right.** f_geo *falls* with v (saturating → 0.20 → 0.02): capture
  efficiency decreasing with encounter velocity — capture-dominated at dwarf kinematics, marginal
  at 200 km/s — is qualitatively the shape DM-1's phenomenology wants (dwarf cores, high-v floor).
  Pending Grok propagation for the quantitative form.
- **The residue is one number.** The Ohmic-fast lower bound misses the dwarf bar by only ×27–115.
  Survival requires the Sea's configurational bath to carry ~×30–100 more weight at ω_enc than a
  bare fm-scale Ohmic tail — a soft ask for a configurational bath (slow/1-f-type components
  generically supply orders of magnitude), but **not derived**. Everything now hangs on one
  derivable Sea quantity: **S(ω) at encounter frequencies.**

## 3. Verdict (spec item 4) and posture

**G4 = UNRESOLVED-QUANTIFIED.** Not kill: the Ohmic lower bound is a bound, not the bath, and it
misses by only 1.5 orders at dwarfs while the geometric factor clears by 5 orders. Not survive:
Θ(ω_enc) is underived and the pre-registered bar is not met by any *derived* quantity yet. The
gate's entire fate is the bath spectrum — computable in principle from the registered PCD/ZBW
dynamics (a Sea autocorrelation computation; a natural DM-4/Stage-3 target), and the founder's
"eternally time-varying configurational" description bears on it without deciding it.

**Release (20 July):** exactly the pre-stated rule's case — G4 unresolved → founder decides hold
vs release-with-named-open-condition. The decision input is now maximally sharp: the open
condition is a single named spectrum with quantified survive/kill thresholds per anchor, the
consistency triple (Λ/W2/halo) shown, and the velocity structure qualitatively favorable.
**Grok propagation** is next work in either branch and can begin before the spectrum lands.
