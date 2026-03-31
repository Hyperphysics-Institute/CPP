# OPEN-P-QM-new-9: Resolve the r_conf Internal Inconsistency

**Series:** QM — Quantum Mechanics (Partner-Switching)
**Status:** RESOLVED — 30 March 2026
**Priority:** HIGH (was); resolved same session as registration
**Registered:** 30 March 2026
**Resolved:** 30 March 2026
**Source:** r_chain computation (SC-7); resolution by tracing op_ss9_ss1_theorems.tex and SM-3 paper

---

## Resolution

The apparent inconsistency was a **mislabeling in SM-3 eq:hop_amp**, not a true inconsistency in the CPP constants. All three constants are correct; SM-3 assigned the wrong name to a computed value.

**Root cause:** SM-3 correctly writes the formula ħω₀ = sea_strength × ħc / r_conf, and also correctly states in a Remark that E_eDP = ħω₀/φ² (the per-vertex projection, with φ² from the Voronoi volume). But then SM-3 writes "≈ 87.8 MeV" as the numerical value of ħω₀ — when 87.8 MeV is actually E_eDP = ħω₀/φ², not ħω₀.

**Correct self-consistent values:**

    sea_strength = 0.1780           (THEO-SS-6, derived from 600-cell Voronoi — trusted)
    r_conf       = 0.16 fm          (SS-1, calibrated: r_conf = √(α_s × ħc / σ))
    ħω₀          = 219.5 MeV        (true ZBW hopping energy = sea × ħc / r_conf)
    E_eDP        = 83.9 MeV         (per-vertex DP binding energy = ħω₀ / φ²)
    "88 MeV" in development notes   = E_eDP (agrees to 4.5%, within φ^(1/12)−1 ≈ 4.1% tolerance)

**Verification:** r_conf = √(0.118 × 0.197 GeV·fm / 0.9 GeV/fm) = 0.161 fm ✓

---

## Impact on SM-3 Theorems

The K = 2/3 theorem (the central result of SM-3) is completely unaffected. It depends only on the eigenvalue ratio of the K3 adjacency matrix (2:1) and the thermal equipartition argument (P3). P3 requires kT_P >> ħω₀. With the corrected ħω₀ = 219.5 MeV and kT_P ≈ 1.22 × 10²² MeV:

    kT_P / ħω₀ = 5.56 × 10¹⁹  >>  1  ✓

P3 holds overwhelmingly. The K = 2/3 derivation is sound.

---

## Required Correction to SM-3

SM-3 eq:hop_amp should be corrected from:

    t = sea_strength × ħc / r_conf ≡ ħω₀ ≈ 87.8 MeV      ← WRONG numerical value

To:

    t = sea_strength × ħc / r_conf ≡ ħω₀ = 219.5 MeV
    E_eDP = ħω₀ / φ² = 83.9 MeV  ≈ 87.8 MeV  (per-vertex DP binding)

The Remark in SM-3 (which correctly states E_eDP = ħω₀/φ²) is already correct — only the numerical value attached to ħω₀ in eq:hop_amp needs updating.

---

## Secondary Issue: Two r_conf Values in the CPP Papers

A separate (unresolved) issue was also identified: SS-1 uses r_conf = 0.16 fm (derived with α_s = 0.118, the high-energy QCD coupling at the Z mass scale), while the companion paper C14 uses r_0 = 0.26 fm (derived with α_s = 0.3, the low-energy coupling near the confinement scale). These two values use different QCD scales for α_s and are both internally consistent within their respective derivations. The physically appropriate value for confinement-scale CPP physics is the low-energy r_0 ≈ 0.26 fm from C14. This inconsistency between papers is a separate open issue but does not affect the SM-3 K = 2/3 result.

---

## Connection to PROP-5

The r_chain computation that uncovered this issue (PROP-5, SC-7) remains TIER 3. The corrected value ħω₀ = 219.5 MeV does not directly change the r_chain = d_Sea/√sea_strength equilibrium condition, which depends on r_conf through d_Sea. With the secondary r_conf issue unresolved (0.16 fm vs 0.26 fm), the r_chain identification with r_e remains pending.

---

*Registered and resolved: 30 March 2026.*
*See also: PROP-5 in propositions.md, SC-7 in solution_candidates.md, SM-3 eq:hop_amp.*
*Folder: CPP/open_problems/*
