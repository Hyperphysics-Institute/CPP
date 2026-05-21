# Chirality Continuum Verification Notebooks

Verification suite for `chirality_continuum.tex` v1.0 SHIPPED 20 May 2026
(Session 137 Patch 0509).

Five Python notebooks numerically validate the paper's key claims at each
of the five verification points B1–B5 specified in
`templates/paper_completion_checklist.md` Section B.

## Suite contents

| File | Verifies | Reference |
|------|----------|-----------|
| `B1_verify_chi6_substrate_handle.py` | χ/6 = φ⁻³/6 ≈ 0.0394 substrate-handle numerical value + comparison to BAU back-derivation | THEO-CHIR-CONT-1.3 (Theorem 15.3.1) |
| `B2_verify_michel_rho_va.py` | Michel ρ = 3/4 at finite mass via V-A four-fermion kinematics + 1-loop QED + PDG 2024 comparison | THEO-CHIR-CONT-2.2 (Theorem 4.2) |
| `B3_verify_chirality_helicity_coincidence.py` | 100% LH at massless helicity limit via P_L^helicity(v) = (1+v)/2 | THEO-CHIR-CONT-2.3 (Theorem 4.3) |
| `B4_verify_cross_sector_convergence.py` | Single primary observable simultaneously validated by both Layer 4 closures | chirality_continuum.tex §6.5 |
| `B5_verify_capotauro_falsifier_6.py` | Three-threshold falsifier cascade (Michel + V+A admixture + leptogenesis) | chirality_continuum.tex §9.4; Capotauro v2.0 §13.4 Falsifier 6 |

## How to run

All five scripts are standalone Python — no external dependencies beyond
the Python standard library (`math`).  Tested with Python 3.10+.

```bash
cd flagship_papers/chirality_continuum/code/
python B1_verify_chi6_substrate_handle.py
python B2_verify_michel_rho_va.py
python B3_verify_chirality_helicity_coincidence.py
python B4_verify_cross_sector_convergence.py
python B5_verify_capotauro_falsifier_6.py
```

Each script prints a self-contained verification report including:
- the analytical claim being verified
- the numerical computation reproducing the claim
- empirical comparison against current experimental anchors
- falsifier-threshold check with PASS/TRIGGERED verdict

## Expected output at v1.0 SHIP

All five scripts should report `Verification: PASS` (or equivalent
"theory consistent" verdict) under current experimental data:

- **B1:** χ/6 = 0.039392 vs empirical anchor ~0.04 (leptogenesis back-derivation);
  within 2% (well below 10% framework uncertainty).
- **B2:** ρ = 3/4 = 0.7500 vs PDG 2024 ρ_obs = 0.7497 ± 0.0010; deviation 0.3σ.
- **B3:** Chirality-helicity coincidence holds at all v; V+A admixture
  suppressed across all LEP + LHC observables tested.
- **B4:** Channel A (V-A coupling path) and Channel B (thermodynamic path)
  converge on the same primary observable Δp_LR within O((χ/6)³) ~ 6×10⁻⁵.
- **B5:** All three Falsifier 6 thresholds NOT TRIGGERED:
  - (A) Michel: consistent at 0.3σ
  - (B) Massless-helicity: bound conservative ~10⁻² < threshold 3×10⁻²
  - (C) Leptogenesis: consistent within 2% of prediction

## Falsification cascade structure

Deviation at any Falsifier 6 threshold at > 3σ significance cascades
backward to question the theorem stack: Lemma 4.1 → Theorem 4.2 →
Theorem 15.3.1 → Definition 15.1.1 → Capotauro substrate-handle
identification (|χ| = φ⁻³ from FI-C-RC-1 + FI-C-RC-2).

Threshold (C) leptogenesis is the sharpest direct test, bypassing
kinematic intermediaries and testing the substrate-handle magnitude
inheritance directly via BAU back-derivation precision.

## Future-collider precision projections

The thresholds are currently set by 2024-era experimental precision.
Future-collider improvements (2030–2040+) could tighten:
- FCC-ee + MEG-II + CLIC + ILC → Michel ρ to ~10⁻⁴
- CMB-S4 + LiteBIRD → BAU η_B precision by factor 2–3
- HL-LHC + future colliders → V+A admixture bounds to ~10⁻⁴
- LEGEND-1000 + nEXO + CUPID → 0νββ + related lepton-number-violation
  observables sensitive to substrate-handle inheritance

## Cross-references

- Paper: `flagship_papers/chirality_continuum/chirality_continuum.tex`
- Companion suite: `flagship_papers/chirality_continuum/documentation_suite/`
- Programme registers:
  - `theorem-registry.md` SD section theorems #65 (THEO-CHIR-CONT-1) + #66 (THEO-CHIR-CONT-2) + #67 (THEO-CHIR-CONT-3)
  - `methods_catalogue.md` METH-CHIR-CONT-1+2+3+4
  - `predictions.md` Section 6 chirality continuum row
  - `master_glossary.md` "Chirality continuum terms" section
- TATWD chapter: `programme_orientation.md` Chapter 22h
- Capotauro v2.0 substrate-level prerequisites: `flagship_papers/capotauro/capotauro.tex` v2.0 v1.0 SHIPPED §§ 3, 5, 6
- Falsifier 6 inventory: Capotauro v2.0 §13.4

## Author

Anthropic Claude Opus 4, in collaboration with Dr. Thomas Lee Abshier, ND
(Hyperphysics Institute).

## Date

20 May 2026 (Session 137 Patch 0515; verification notebook suite B1–B5).
