<!--
  Extracted from Research_Frontier.md lines 1101-1164
  Source range: Quantum Mechanics
  Extraction date: 2026-05-25
  Master dashboard: Research_Frontier.md
-->

## Quantum Mechanics (QM) — 6 problems (5 QM + 1 quantum-optics phenomena)

### OPEN-QM-1: Born Rule from CPP Statistics
**Status:** OPEN
**Sector(s):** QM
**Priority:** HIGHEST
**One-line statement:** Prove P(i) = |⟨ψ_i|ψ⟩|² — specifically the square, not another power.
**What a solution looks like:** Derivation from ZBW phase averaging giving exactly the squared amplitude.
**Dependencies:** None blocking
**Cross-sector connections:** OPEN-SM-7b (ZBW-1 postulate is a special case)
**Current best lead:** Mechanism identified (DI-bit processing rate ∝ |ψ|²); exact derivation not complete.
**Paper(s):** QM-5
**Last updated:** 23 March 2026

---

### OPEN-QM-3: Spin-½ and Pauli Exclusion from Cage Geometry
**Status:** OPEN
**Sector(s):** QM
**Priority:** HIGH
**One-line statement:** Derive s = 1/2 from ZBW orbital topology; derive Pauli exclusion from hDP chain antisymmetry.
**Dependencies:** None blocking
**Cross-sector connections:** Connects to the inner/outer ZBW orbital relationship (CONJ-P-SS-1, corrected: radius ratio 2, angular-frequency ratio 2√2 — NOT a 2:1 frequency; phase-locked; registered as THEO-SPIN-1 v1.1, Patch 0572f)
**Paper(s):** QM-6, QM-7
**Last updated:** 23 March 2026

---

### OPEN-QM-5: Entanglement Decoherence Threshold at ~10¹⁵ eV
**Status:** OPEN
**Sector(s):** QM
**Priority:** MEDIUM
**One-line statement:** Derive E_thresh from Nexus lattice path limits.
**Dependencies:** None blocking
**Cross-sector connections:** Falsifiable prediction
**Paper(s):** QM-4
**Last updated:** 23 March 2026

---

### OPEN-QM-6: Discrete Spectra Deviations at ~10¹⁰ Hz
**Status:** OPEN
**Sector(s):** QM
**Priority:** MEDIUM
**One-line statement:** Compute exact δE_n corrections from 600-cell lattice discreteness.
**Dependencies:** None blocking
**Cross-sector connections:** Falsifiable prediction at accessible frequencies
**Paper(s):** QM-2
**Last updated:** 23 March 2026

---

### OPEN-QM-7: QFT Second Quantisation from Multi-CP Lattice Excitations
**Status:** OPEN
**Sector(s):** QM
**Priority:** MEDIUM
**One-line statement:** Derive field operators, Fock space, creation/annihilation operators from 600-cell normal modes.
**Dependencies:** None blocking
**Cross-sector connections:** OPEN-G-2 (formal QFT framework)
**Paper(s):** QM-6, QM-7
**Last updated:** 23 March 2026

---

### OPEN-TP-1: Leading-log coefficient C for shutter-induced photon creation (quantum-optics phenomena, TP-1)
**Status:** PARTIAL (advanced v1.1) — class closed, cutoff grounded, coefficient *structure* resolved; only the absolute $O(1)$ value remains.
**Sector(s):** QM (quantum optics); draws on QM-4, QM-5
**Priority:** LOW (foundational, not falsifiable in the testable regime)
**One-line statement:** Fix the $O(1)$ coefficient $C$ in $\langle N\rangle_{\max}=C\ln(\omega_{\max}/\omega_\gamma)$ for the truncated photon (Rukan–Gulla–Skaar) from the 600-cell Hilbert–Schmidt mode sum $\|T_2\|^2_{\mathrm{HS}}$ near the band top.
**What a solution looks like:** Evaluate the mode sum with the 600-cell density of states (van Hove near the band top $\omega_{\max}=\sqrt{12}/t_P$) for a representative cut profile, returning a definite $O(1)$ number.
**Progress:** v0.1 OPEN → v0.2 PARTIAL (logarithmic divergence class derived from the RGS kernel) → v0.4 cutoff grounded as the intrinsic 600-cell band top $\omega_{\max}=\sqrt{\lambda_{\max}}\,c/\ell_P=\sqrt{12}/t_P=2\sqrt3/t_P$ (QM-5 dispersion, $\lambda_{\max}=z=12$), ceiling $\approx 64.5\,C$ → **v1.1 (Patch 1712, script `1712`):** the *structure* of $C$ is resolved — it is the **continuum** coefficient $A\,g_0$ (the leading log is range-dominated, so the lattice does **not** enhance $C$); the lattice's only coefficient-level contribution is an $O(1)$ van Hove band-top correction $\Delta$ to the log argument ($\Delta=\ln2\approx0.69$ for the representative dispersion $\omega=\omega_{\max}\sin(\pi k/2k_{\max})$, raising the ceiling $64.5\,C\to\approx65.2\,C$). Framework-specific content confirmed to be the **cutoff** $\omega_{\max}$, not the coefficient. Residual: the absolute $C$ (RGS normalization × profile) and the exact $\Delta$ (true dispersion).
**Dependencies:** QM-5 mode spectrum / density of states near the band top.
**Paper(s):** TP-1 (`series_phenomena/quantum_optics/photon_truncation/TP-1/`), v1.0 SHIPPED.
**Last updated:** 21 June 2026 (Patch 1712)

---

